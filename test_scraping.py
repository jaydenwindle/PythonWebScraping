import scraping
import os
from bs4 import ResultSet, Tag

def test_imports_request():
    assert hasattr(scraping, 'requests'), \
        "Import the requests library at the top of your scraping.py file"

def test_scraping_defines_url():
    assert hasattr(scraping, 'url'), \
        "Define a variable called `url` that contains the string 'https://www.pluralsight.com/'"

def test_scraping_defines_correct_url():
    assert scraping.url == 'https://www.pluralsight.com/', \
        "Make sure the variable `url` is equal to 'https://www.pluralsight.com/'"

def test_scraping_sends_request():
    assert hasattr(scraping, 'response'), \
        "Send a GET request to `url` using the request library, and store the response in a variable named `response`"

def test_scraping_sends_request_to_correct_url():
    assert scraping.response.request.url == scraping.url, \
        "Make sure you send your GET request to 'https://www.pluralsight.com/'"

def test_scraping_request_succeeds():
    assert scraping.response.status_code == 200, \
        "It looks like your GET request failed. Make sure that your internet is working and that you sent your request to 'https://www.pluralsight.com/'"

def test_imports_beautifulsoup():
    assert hasattr(scraping, 'BeautifulSoup'), \
        "Import the BeautifulSoup from the bs4 library at the top of your scraping.py file"

def test_loads_html_into_beautifulsoup():
    assert hasattr(scraping, 'soup'), \
        "Load the text from your response into BeautifulSoup, and store the return value in a variable called `soup`"

def test_loads_correct_html_into_beautifulsoup():
    assert scraping.soup == scraping.BeautifulSoup(scraping.response.text, features="html.parser"), \
        "Make sure you passed `response.text` as an argument to the BeautifulSoup constructor"

def test_defines_trending_topic_elements():
    assert hasattr(scraping, 'trending_topic_elements'), "Store the results of `soup.select` in an array called `trending_topic_elements`"

def test_trending_topic_elements_is_result_set():
    assert type(scraping.trending_topic_elements) == ResultSet, "Looks like `trending_topic_elements` isn't an array of results. Make sure you're calling `soup.select` properly"

def test_trending_topic_elements_result_set_is_not_empty():
    assert len(scraping.trending_topic_elements) > 0, "Looks like there are no elements in your `trending_topic_elements` array. Make sure you called `soup.select` with the correct CSS selector string (\"ul.glide__slides > li\")"

def test_defines_trending_topics():
    assert hasattr(scraping, 'trending_topics'), "Create an array called `trending_topics` to store your scraping results"

def test_trending_topics_is_list():
    assert type(scraping.trending_topics) == list, "Looks like `trending_topics` isn't an array. Make sure you've defined an empty array variable called `trending_topics`"

def test_defines_name_element():
    assert hasattr(scraping, 'name_element'), "Make sure you've stored the result of `topic_element.find` in a variable called `name_element` inside of your `for` loop"

def test_name_element_is_tag():
    assert type(scraping.name_element) == Tag, "Looks like `name_element` isn't an element. Make sure you've selected the right element using `topic_element.find(\"h5\")` and stored the result in a variable called `name_element` inside of your `for` loop."

def test_name_element_tag_is_h5():
    assert scraping.name_element.name == 'h5', "Looks like `name_element` isn't an `h5` element. Make sure you've selected the right element using `topic_element.find(\"h5\")` and stored the result in a variable called `name_element` inside of your `for` loop."

def test_defines_name():
    assert hasattr(scraping, 'name'), "Make sure you've stored the attribute `name_element.text` in a variable called `name` inside of your `for` loop"

def test_name_is_string():
    assert type(scraping.name) == str, "Looks like `name` is not a string. Make sure you've stored the attribute `name_element.text` in a variable called `name` inside of your `for` loop"

def test_defines_url_element():
    assert hasattr(scraping, 'topic_url_element'), "Make sure you've stored the result of `topic_element.find` in a variable called `topic_url_element` inside of your `for` loop"

def test_url_element_is_tag():
    assert type(scraping.topic_url_element) == Tag, "Looks like `topic_url_element` isn't an element. Make sure you've selected the right element using `topic_element.find(\"a\")` and stored the result in a variable called `topic_url_element` inside of your `for` loop."

def test_url_element_is_a_tag():
    assert scraping.topic_url_element.name == 'a', "Looks like `topic_url_element` isn't an `a` element. Make sure you've selected the right element using `topic_element.find(\"a\")` and stored the result in a variable called `topic_url_element` inside of your `for` loop."

def test_defines_topic_url():
    assert hasattr(scraping, 'topic_url'), "Make sure you've stored the attribute `topic_url_element[\"href\"]` in a variable called `topic_url` inside of your `for` loop"

def test_topic_url_is_string():
    assert type(scraping.topic_url) == str, "Looks like `topic_url` is not a string. Make sure you've stored the attribute `topic_url_element[\"href\"]` in a variable called `topic_url` inside of your `for` loop"

def test_topic_url_is_valid_url():
    assert scraping.url.startswith('http'), "Looks like `topic_url` isn't a proper URL. Make sure you've stored the attribute `topic_url_element[\"href\"]` in a variable called `topic_url` inside of your `for` loop"

def test_defines_topic():
    assert hasattr(scraping, 'topic'), "Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_topic_is_dict():
    assert type(scraping.topic) == dict, "Looks like `topic` isn't a dictionary. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_name_in_topic_dict():
    assert 'name' in scraping.topic, "Looks like `topic` doesn't contain the key `\"name\"`. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_correct_name_in_topic_dict():
    assert scraping.topic['name'] == scraping.name, "Looks like `topic[\"name\"]` isn't equal to the variable `name`. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_url_in_topic_dict():
    assert 'url' in scraping.topic, "Looks like `topic` doesn't contain the key `\"url\"`. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"
    assert scraping.topic['url'] == scraping.topic_url, "Looks like `topic[\"url\"]` isn't equal to the variable `topic_url`. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_correct_url_in_topic_dict():
    assert scraping.topic['url'] == scraping.topic_url, "Looks like `topic[\"url\"]` isn't equal to the variable `topic_url`. Make sure you've created a dictionary called `topic` with the keys `name` and `url` inside of your `for` loop"

def test_appended_topic_to_trending_topics():
    assert len(scraping.trending_topics) == len(scraping.trending_topic_elements), "Make sure you've appended the dictionary `topic` to the `trending_topics` array inside your `for` loop"

def test_appended_topic_is_dict():
    assert type(scraping.trending_topics[0]) == dict, "Looks like the `trending_topics` array contains an element that's not a dictionary. Make sure you've appended the dictionary `topic` to the `trending_topics` array inside your `for` loop"

def test_imported_json():
    assert hasattr(scraping, 'json'), \
        "Import the json library at the top of your scraping.py file"

def test_trending_topics_json_file_exists():
    assert os.path.isfile('trending_topics.json'), "Make sure you've written your `trending_topics` array in JSON format to the file `trending_topics.json` using `json.dump`."

def test_trending_topics_json_file_has_correct_content():
    json_file = open('trending_topics.json', 'r')
    trending_topics = scraping.json.load(json_file)
    assert trending_topics == scraping.trending_topics, "Looks like the JSON in `trending_topics.json` doesn't match your `trending_topics` array. Make sure you've written your `trending_topics` array in JSON format to the file `trending_topics.json` using `json.dump`."