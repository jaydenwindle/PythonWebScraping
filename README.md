# Intro to Web Scraping with Python

### [Get Started →](https://github.com/jaydenwindle/PythonWebScraping/blob/master/tasks.md)

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

If you know these, you should be ready to give this project a try! 

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

As you're working through the project, it's highly recommended to run the following command, which will watch for any changes to your files and then re-run the tests automatically whenever you save them. You can run this command once, and then look back at the terminal after you've made changes to the `scraping.py` file.

```
$ pipenv run watch
```

### [Get Started →](https://github.com/jaydenwindle/PythonWebScraping/blob/master/tasks.md)