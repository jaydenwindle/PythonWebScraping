import requests
from bs4 import BeautifulSoup
import json

url = "https://www.pluralsight.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, features="html.parser")

trending_topic_elements = soup.select('ul.glide__slides > li')

trending_topics = []

for topic_element in trending_topic_elements:
    name_element = topic_element.find('h5')
    name = name_element.text
    topic_url_element = topic_element.find('a')
    topic_url = topic_url_element["href"]

    topic = {
        "name": name,
        "url": topic_url
    }

    trending_topics.append(topic)

with open('trending_topics.json', 'w') as json_file:
    json.dump(trending_topics, json_file)