import requests

endpoint = "https://clck.ru/--"

def generate_short_link(links: tuple) -> tuple:
    short_links = []
    for link in links:
        params = {"url": link}
        response = requests.get(endpoint, params=params)
        short_links.append(response.text)
    return tuple(short_links)
