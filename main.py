import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'long_url': url,
        'title': url
    }
    response = requests.post(api_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, link):
    parsed_url = urlparse(link)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    parsed_url = urlparse(url)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(f'{api_url}/{bitlink}', headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('BYTLY_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    url = args.url
    try:
        if is_bitlink(token, url):
            print(f'Count of clicks: {count_clicks(token, url)}')
        else:
            bitlink_id = shorten_link(token, url)
            print(f'For {url} Bitlink id = {bitlink_id}')
    except requests.exceptions.HTTPError as error:
        print(f'Error: {error}')
