import requests
import selenium
from bs4 import BeautifulSoup

cookies = {
    'xf_session': '804d96c92888202f457fe7ed84f5ce7d',
    'xf_id': '769afcbc8cf2b714fa9dfbbc7e4c72ae',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'bigbro.biz',
    'Accept-Language': 'uk-ua',
    'Accept-Encoding': 'br, gzip, deflate',
    'Origin': 'https://bigbro.biz',
    'Referer': 'https://bigbro.biz/',
    'Content-Length': '1894',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Ajax-Referer': 'https://bigbro.biz/',
}

data = {
    'sections[users-new][sectionId]': 'users-new',
    'sections[users-new][typeMajor]': 'users',
    'sections[users-new][type]': 'users_new',
    'sections[users-new][action]': 'users-new',
    'sections[users-new][encodedParams]': 'eyJpdGVtTGltaXQiOjgwMDB9',
    'sections[threads-recent][sectionId]': 'threads-recent',
    'sections[threads-recent][typeMajor]': 'threads',
    'sections[threads-recent][type]': 'threads_recent',
    'sections[threads-recent][action]': 'threads-recent',
    'sections[threads-recent][encodedParams]': 'eyJub2RlX2lkcyI6IjEzMywyNjUsMjU0LDE5NSwxNjAsMjYsMTYxLDIyNSwyNjMsMjQsMTIsMjU4LDI3MSwyNzksMjUzLDM2OCwyNzcsMzM0LDM0MCwzNzAsMjMyLDMxMSwzNTQsMjgxLDIxOCwyNTcsMjY4LDM0MywzNTUsMzYwLDM3NCwxMTEsMTEyLDEzNywxNTAsMTUxLDE1MiwzNjEsMzYyLDM2NCwzNjMsNSwxMzYsMTQsMzQ5LDM3MSwyODAsMjgsMzA4LDMxMCwzMTQsMzIwLDMzMSwzMjgsMzQ1LDMzNywzNDQsMzQ2LDM0NywzNTYsMzY2LDM2NSwzNzUsMzc2LDIwLDMwOSwzMCwzNTksMzczLDMxLDMyLDI4NSwxODQsMzEzLDM1MSwyMjgsMjQ2LDI0MywyMDUsMjk2LDI5MiwyNzMsMTY1LDI3MiwyMzksMzIyLDMwNywyOTksMjYwLDMzMywzMjUsMzI5LDMyMSwzMzYsMzM4LDMzOSwzNDEsMzQ4LDM1MywzNTIsMzU4LDE3NSwzNjcsMzcyLDMzLDM0LDQxLDIyMiw0NCw0Miw0Myw0Nyw5Myw5NCw5NSw5NiwxMywyMiw3LDgsMTcsMTgsMTksMzYsMzcsMzgsNDYsMTYsNzgsODAsODEsODIsNzksODMsODQsODUsNTEsNTIsNTMsNTQsNTUsNTcsNTYsNTgsMjI0LDU5LDYwLDYyLDIwMCw2Myw2NCw2NSw2Niw2Nyw2OCw2OSw3MSw3MCw3Miw3Myw5Nyw3NCwxNTQsNzUsNzYsMjExLDEyMSwxMjcsMTkxLDI1MSwyNzQsMzEyLDM0MiwyMDQsMjA2LDIyMywyMjYsMjI5LDIzMywyNTksMjkxLDEyNiwxODMsMTk3LDIwOCwyMTIsMjMxLDIzOCwyNDEsMjQyLDI0NSwyNDcsMjQ4LDI1MCwyNjYsMjcwLDE1MywxNzksMTg2LDE4OCwyMDIsMjE5LDI0MCwxNzcsMjYyLDI5MCwyMTMsMjY5LDI1NiwyODcsMjg4LDMwMSwzMDIsMjk3LDMwNiwyOTMsMjk4LDI4OSwzMDMsMzE3LDI1MiwyNzYsMzE1LDI0OSwzMTYsMzE4LDMxOSwzMjQsMzIzLDI1NSwyMjcsOTAsMTE3LDEyMywxLDEzMCw5OCwxMjgsMTMyLDkyIiwiaGFzaCI6IjIyOGJlYzRlZGVmMjExMTUzYTc0MzBjOGUwMDk1OTEzIiwiaXRlbUxpbWl0Ijo4MDAwfQ==',
    'itemLimit': '7000',
    'updateInterval': '70',
    '_xfRequestUri': '/',
    '_xfNoRedirect': '1',
    '_xfResponseType': 'json'
}

response = requests.post('https://bigbro.biz/advstats/bulk-update', headers=headers, cookies=cookies, data=data)
html = response.text
print(html)
from seleniumrequests import Firefox

webdriver = Firefox()
response = webdriver.request('POST', 'https://bigbro.biz/advstats/bulk-update', headers=headers, cookies=cookies, data=data)
print(response.content)
