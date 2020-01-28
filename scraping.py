import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.pluralsight.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, features="html.parser")

trending_topics = []

trending_topic_elements = soup.select('ul.glide__slides > li')

for topic in trending_topic_elements:
    name = topic.find('h5').text
    description = topic.select('.path__slide--desc-p')[0].text.strip()
    topic_url = topic.find('a')['href']

    trending_topics.append({
        "name": name,
        "description": description,
        "url": topic_url
    });

with open('trending_topics.json', 'w') as json_file:
    json.dump(trending_topics, json_file)