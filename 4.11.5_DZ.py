import requests

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://parsinger.ru/4.6/1/index.html',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.816 YaBrowser/24.7.6.816 (beta) Yowser/2.5 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(
    'https://parsinger.ru/714FAF10-B2A8-4A18-8232-B054303674AA/DB964956-C576-4FC2-B095-851A8A08E881/from?get&nocache=10c05',
    headers=headers,
)
print(response)