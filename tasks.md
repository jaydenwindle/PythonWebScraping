# Intro to Web Scraping with Python

## Description

This project will teach you the basics of web scraping with Python. You'll learn step by step how to use standard Python web scraping tools to scrape the list of "Trending Topics" from the PluralSight homepage and export them as a JSON file.

## Required Applications and Tools

You'll need to have access to the following tools on your local machine to complete this project.

* Git
* GitHub
* Code Editor
* Command Line / Terminal Access
* Python 3 (see: https://realpython.com/installing-python/)
* Pipenv (see: https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

Never used Git and don’t have a code editor? We have a video that walks you through all the steps you’ll need to set this up.

## Prerequisite Knowledge

Completing all of the tasks in this project requires knowledge of basic Python concepts.

You'll also need to have a working knowledge of git to commit local changes and push them up to a GitHub repository.  We'll walk you through that part, so if you haven't used Git before -- don't worry. We recommend that you should have already completed the following Pluralsight Courses:

* [Python Fundamentals](https://app.pluralsight.com/library/courses/python-fundamentals/table-of-contents)

And have an understanding of the following topics:

* How to define and use variables
* How to create and append data to arrays and dictionaries
* How to iterate over arrays using a `for` loop
* How to initialize an instance of a class
* How to call class methods and pass positional and named arguments
* How to access class attributes
* How to open and write to files

If you know these, you should be all set to jump in and give this project a shot!

## Setting Up The Project

In order to get this working, you'll need to have [Git](https://git-scm.com/) installed on your computer, and have a GitHub account. If this is your first time setting up Git, I'd recommend checking out Pluralsight's video on How to Setup Git for Pluralsight Projects in 5 Minutes to learn what you need to know.

The very first step is to fork this repository to your personal GitHub account and clone it down locally. We'll be editing the `scraping.py` file in the root directory for this project.

### Installation

To install the dependencies for this project, run the following command in the root folder of the `PythonWebScraping` project.

```
$ pipenv install
```

### Verify Setup

You can test that everything has been set up correctly by running the following command, which will show you a list of failing tests. This is a good thing! You'll gradually fix these test cases as you progress through the project. By the end of this project, all of the tests will pass.

```
$ pipenv run test
```

We recommend also running the following command, which will watch for any changes to your files and then re-run the tests automatically. This makes things easier, since you'll see updates immediately when you save your files! You can run this command once, and then look back at the terminal after you've made changes to the `scraping.py` file.

```
$ pipenv run watch
```

## Let's get scraping!

### Import the `requests` library

You're going to use the [`requests`](https://requests.readthedocs.io/en/master/) Python library to make requests to the Pluralsight homepage (`https://www.pluralsight.com/`) and download the HTML source code.

To start, `import requests` at the top of your `scraping.py` file.

### Add the Pluralsight homepage URL

Create a variable called `url` that stores the string `"https://www.pluralsight.com/"`, which is the web page we're going to scrape our data from.

### Fetch Pluralsight homepage HTML

Fetch the HTML source code for Pluralsight homepage by calling the `requests.get` function and passing in the variable `url` as a parameter. Store the response in a variable called `response`.

If you want to see the source code of the Pluralsight homepage, try printing it to the console with `print(response.text)`

## Parsing the HTML

### Import BeautifulSoup

Now that we've downloaded the HTML source code for the Pluralsight homepage, we're going to need to parse it in order to pull out the trending topics data that we're after. To do this, we're going to use a Python library called [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (aka `bs4`).

First, we'll need to import the `BeautifulSoup` class from the `bs4` module at the top of our `scraping.py` file.

### Loading the HTML into BeautifulSoup

Next, we'll need to load the HTML source code from the Pluralsight homepage into BeautifulSoup.

Create an instance of the `BeautifulSoup` class and store it in a variable called `soup`. Pass in `response.text` as the first parameter to `BeautifulSoup`, and pass in a named parameter called `features` with the string value `"html.parser"` to tell BeautifulSoup that we want it to parse HTML.

### Finding the list of trending topics

If you inspect the HTML source code from the Pluralsight homepage, you'll see that the list of trending topics is represented as an unordered list (`ul`) with the class `.glide_slides`, and each trending topic card represented as a child list item (`li`).

`BeautifulSoup` has a really useful method called `select`, that allows us to get all elements that match a given CSS selector from the provided HTML.

To get the list of trending topic elements, call the `soup.select` method and pass in the following CSS selector string as an argument: `"ul.glide__slides > li"`. Store the results in an array called `trending_topic_elements`.

### Getting the topic name

Now we've got a list of the trending topic elements from the homepage, but we still have some work to do to get the relevant data for each trending topic. In our case, we want to get the `name` of each topic, and it's PluralSight `url`.

Create an empty array called `trending_topics`, where we'll store a dictionary with the keys `name` and `url` for each trending topic.

If you inspect the HTML source code from the Pluralsight homepage, you'll see that inside each trending topic `li` element, the `name` value is wrapped in an `h5` tag, and the `url` value is stored in the `href` attribute of an `a` tag.

We can use the `find` method from `BeautifulSoup` to find elements by their tag name. To get the `name` and `url` values from each trending topic element, create a `for` loop that loops through each `topic_element` in the `trending_topic_elements` array. Inside your loop, call the `topic_element.find` method and pass in the string `"h5"` to get the `h5` element that stores the trending topic name. Store it in a variable called `name_element`.

You can access the name of a trending topic as a string using the `text` attribue of `name_element`. Store the attribute `name_element.text` in a variable called `name`. If you want to see whether you've grabbed the name properly, try printing it with `print(name)`.

### Getting the topic URL

Now let's grab the trending topic's URL. Inside your `for` loop from the last step, call the `trending_topic.find` method and pass in the string `"a"` to get the `a` element that links to the trending topic's URL. Store it in a variable called `topic_url_element`.

You can access the trending topic's URL as a string by grabbing the `href` attribute from `topic_url_element`. Store the attribute `topic_url_element["href"]` in a variable called `topic_url`. If you want to see whether you've grabbed the URL properly, try printing it with `print(topic_url)`.

### Formatting our data

Now that we've got the `name` and `url` for each trending topic, we want to store the details of each trending topic in an array. We'll use a dictionary with the keys `name` and `url` to represent each trending topic.

Inside your `for` loop from the previous two steps, create a dictionary called `topic` where the `name` key is set to the value of your `name` variable and the `url` key is set to the value of your `topic_url` variable. Append the dictionary to the `trending_topics` array by calling `trending_topics.append(topic)`.

If you print your `trending_topics` array, you should see all of the topics from the Pluralsight homepage and their corresponding URLs.
### Exporting our data

Now that you've formatted the data properly, let's export it to a file so the data can be used later on.

To start, `import json` at the top of your `scraping.py` file.

Next, let's `open` a file called `trending_topics.json` in write mode and store the file pointer in a variable called `json_file`, like so:

```python
with open('trending_topics.json', 'w') as json_file:
```

Inside of your `with` block, call the `json.dump` method, passing in your `trending_topics` array as the first argument and `json_file` as the second argument. This will write your `trending_topics` array to the `trending_topics.json` in JSON format.

## Next Steps

Congrats! You've successfully scraped data from a website, formatted it, and stored it in a file. You've learned how to send requests with the `requests` library, how to parse and traverse HTML documents using `BeautifulSoup`, and how to export data to a file in JSON format.

If you want an extra challenge, try scraping some other elements from the Pluralsight homepage (e.g. the "Discover more ways to stay ahead" section).