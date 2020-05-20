# A simple python script to retrieve web data and return a string with the response body
# can emulate any user agent for compatibility defaults to win 10 with chrome 42.0
import requests

def get_webdata(urls):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246 '})
    response = session.get(urls)
    return response.text

