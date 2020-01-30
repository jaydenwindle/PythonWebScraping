import scraping

def test_imports_request():
    assert hasattr(scraping, 'requests'), \
        "Import the requests library at the top of your scraping.py file"

def test_scraping_defines_correct_url():
    assert hasattr(scraping, 'url'), \
        "Define a variable called `url` that contains the string 'https://www.pluralsight.com/'"
    assert scraping.url == 'https://www.pluralsight.com/', \
        "Make sure the variable `url` is equal to 'https://www.pluralsight.com/'"

def test_scraping_sends_request_to_correct_url():
    assert hasattr(scraping, 'response'), \
        "Send a GET request to `url` using the request library, and store the response in a variable named `response`"
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
    assert scraping.soup == scraping.BeautifulSoup(scraping.response.text, features="html.parser"), \
        "Make sure you passed `response.text` as an argument to the BeautifulSoup constructor"

def test_trending_topics_list():
    assert hasattr(scraping, 'trending_topics'), "Create an array called `trending_topics` to store your scraping results"
    assert type(scraping.trending_topics) == list, "Looks like `trending_topics` isn't an array. Make sure you've defined an empty array variable called `trending_topics`"

def test_trending_topics_list_items():
    assert hasattr(scraping, 'trending_topics'), "Create an array called `trending_topics` to store your scraping results"
    assert type(scraping.trending_topics) == list, "Looks like `trending_topics` isn't an array. Make sure you've defined an empty array variable called `trending_topics`"