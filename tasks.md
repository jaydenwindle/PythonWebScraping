# Intro to Web Scraping with Python

## Let's get scraping!

Welcome to Intro to Web Scraping with Python! In this project you'll learn step by step how to scrape data from a website using common web scraping tools. You'll do that by scraping a list of "Trending Topics", along with their names and URLs, from the Pluralsight homepage (https://www.pluralsight.com/).

### Task #1: Import the `requests` library

You're going to use the [`requests`](https://requests.readthedocs.io/en/master/) Python library to make requests to the Pluralsight homepage and download the HTML source code.

To start, `import requests` at the top of your `scraping.py` file.

### Task #2: Add the Pluralsight homepage URL

Create a variable called `url` that stores the string `"https://www.pluralsight.com/"`, which is the URL of the Pluralsight homepage which you're going to scrape data from.

### Task #3: Fetch Pluralsight homepage HTML

Fetch the HTML source code for Pluralsight homepage by calling the `requests.get` function and passing in the variable `url` as a parameter. Store the response in a variable called `response`.

If you want to see the source code of the Pluralsight homepage, try printing it to the console with `print(response.text)`

## Parsing the HTML

Nice, you've got the source code! Now that you've downloaded the HTML source code for the Pluralsight homepage, you're going to need to parse it in order to extract the "Trending Topics" data that you're after.

### Task #4: Import BeautifulSoup

To parse the HTML source code and extract the "Trending Topics" data, you're going to use a Python library called [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

First, you're going to import the `BeautifulSoup` class from the `bs4` module at the top of your `scraping.py` file.

### Task #5: Loading the HTML into BeautifulSoup

Next, you're going to load the HTML source code from the Pluralsight homepage into BeautifulSoup.

Create an instance of the `BeautifulSoup` class and store it in a variable called `soup`. Pass in `response.text` as the first parameter to `BeautifulSoup`, and pass in a named parameter called `features` with the string value `"html.parser"` to tell BeautifulSoup that you want it to parse HTML.

### Task #6: Finding the trending topics

If you inspect the HTML source code from the Pluralsight homepage, you'll see that the list of trending topics is represented as an unordered list (`ul`) with the class `.glide_slides`, and each trending topic card represented as a child list item (`li`).

`BeautifulSoup` has a really useful method called `select`, that allows you to get all elements that match a given CSS selector from the provided HTML.

To get the list of trending topic elements, call the `soup.select` method and pass in the following CSS selector string as an argument: `"ul.glide__slides > li"`. Store the results in an array called `trending_topic_elements`.

### Task #7: Getting the topic name

Now you've got a list of the trending topic elements from the homepage, but there's still some work to do to get the name and URL for each trending topic. 

Create an empty array called `trending_topics`. You'll use this later to store a dictionary with the keys `name` and `url` for each trending topic.

If you inspect the HTML source code from the Pluralsight homepage, you'll see that inside each trending topic `li` element, the `name` value is wrapped in an `h5` tag, and the `url` value is stored in the `href` attribute of an `a` tag.

You can use the `find` method from `BeautifulSoup` to find elements by their tag name. To get the `name` and `url` values from each trending topic element, create a `for` loop that loops through each `topic_element` in the `trending_topic_elements` array. Inside your loop, call the `topic_element.find` method and pass in the string `"h5"` to get the `h5` element that stores the trending topic name. Store it in a variable called `name_element`.

You can access the name of a trending topic as a string using the `text` attribue of `name_element`. Store the attribute `name_element.text` in a variable called `name`. If you want to see whether you've grabbed the name properly, try printing it with `print(name)`.

### Task #8: Getting the topic URL

Now that you've got the trending topic's name, you're going to grab the trending topic's URL as well. Inside your `for` loop from the last step, call the `trending_topic.find` method and pass in the string `"a"` to get the `a` element that links to the trending topic's URL. Store it in a variable called `topic_url_element`.

You can access the trending topic's URL as a string by grabbing the `href` attribute from `topic_url_element`. Store the attribute `topic_url_element["href"]` in a variable called `topic_url`. If you want to see whether you've grabbed the URL properly, try printing it with `print(topic_url)`.

### Task #9: Formatting the data

Now that you've got the `name` and `url` for each trending topic, you'll want to store the details of each trending topic in your `trending_topics` array. You'll use a dictionary with the keys `name` and `url` to represent each trending topic.

Inside your `for` loop from the previous two steps, create a dictionary called `topic` where the `name` key is set to the value of your `name` variable and the `url` key is set to the value of your `topic_url` variable. Append the dictionary to the `trending_topics` array by calling `trending_topics.append(topic)`.

If you print your `trending_topics` array, you should see all of the topics from the Pluralsight homepage and their corresponding URLs.

## Exporting the Data

Awesome! You've parsed and extracted the "Trending Topics" data, and formatted it correctly. Now you're going to export it to a file so that the data can be used later.

### Task #10: Writing to a file

To start, `import json` at the top of your `scraping.py` file.

Next, `open` a file called `trending_topics.json` in write mode and store the file pointer in a variable called `json_file`, like so:

```python
with open('trending_topics.json', 'w') as json_file:
```

Inside of your `with` block, call the `json.dump` method, passing in your `trending_topics` array as the first argument and `json_file` as the second argument. This will write your `trending_topics` array to the `trending_topics.json` in JSON format.

Once you've done this correctly, you should see a new file in your project folder called `trending_topics.json`, and inside you should see the list of trending topics with their names and URLs.

## Next Steps

Congrats! You've successfully scraped data from a website, formatted it, and stored it in a file. You've learned how to send requests with the `requests` library, how to parse and traverse HTML documents using `BeautifulSoup`, and how to export data to a file in JSON format.

If you want an extra challenge, try scraping some other elements from the Pluralsight homepage (e.g. the "Discover more ways to stay ahead" section).

Have fun scraping!