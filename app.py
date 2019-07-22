from bs4 import BeautifulSoup
from selenium import webdriver
import requests

from connector import Theme, session

import re


def get_data(link):
    try:
        driver.get(link)
        message_content = driver.find_element_by_class_name('messageContent').text
        text = re.sub(r"[^A-Za-z0-9А-Яа-я :/!\"#$%&()*+,.;<=>?@_`{|}~]+", '', message_content)
        title = driver.find_element_by_class_name('titleBar').find_element_by_tag_name('h1').text
        tags = ''
        description = driver.find_element_by_id('pageDescription')
        try:
            username = description.find_element_by_class_name('username').text
        except AttributeError as error:
            print(error)
            username = ''
        try:
            date_time = description.find_element_by_tag_name('span').text
        except AttributeError as error:
            print(error)
            date_time = ''
        new_theme = dict(title=title, tags=tags, text=text, username=username, date_time=date_time)
        return new_theme
    except Exception as error:
        print(error)
        return dict(title='', tags='', text='', username='', date_time='')


def get_links():
    data = {
        'tab_id': '2',
        'modern_statistic_id': '1',
        'hard_reload': 'false',
        'limit': '15250',
        '_xfRequestUri': '/',
        '_xfNoRedirect': '1',
        '_xfResponseType': 'json'
    }

    response = requests.post('https://labrc.net/brms-statistic/statistics.json', data=data)
    soup = BeautifulSoup(response.json().get('tabContentHtml'), features='html.parser')

    links = ['https://labrc.net/' + div.find('a')['href'] or None for div in
             soup.find_all(class_='listBlock itemTitle')]
    for link in links:
        new_theme = Theme(link=link)
        session.add(new_theme)
        session.commit()
    return links


themes = session.query(Theme).all()
driver = webdriver.Firefox('/usr/local/Cellar/geckodriver/0.24.0/bin/')

for theme in themes:
    if theme.author:
        continue
    theme_data = get_data(link=theme.link)
    theme.title = theme_data.get('title')
    theme.text = theme_data.get('text')
    theme.tags = theme_data.get('tags')
    theme.author = theme_data.get('username')
    theme.date = theme_data.get('date_time')
    print(theme_data)
    session.commit()
