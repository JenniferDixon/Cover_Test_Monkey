# Cover Test Monkey
This test suite was developed for Amy at Cover. The test suite is designed to test the following website: https://www.monkeyuser.com/

## Installation instructions
In order to run this suite, the following need to be installed:

* Python 3.7 - Available from Anaconda:  https://www.anaconda.com/distribution/ (Follow instructions)
* Selenium framework - Selenium for python https://pypi.org/project/selenium/
* PyCharm (optional) - Free Community Version https://www.jetbrains.com/pycharm/download

## Selection of Tools/Technology
### Language - Python 3.7
Python is high-level general application language that is easy to understand and read. It is well suited for a basic web testing suite. It has many in-built libraries and can work well with external libraries and automation frameworks. Lower-level languages would less practical and time-consuming to test with (if it works). 

### Test Framework - Selenium
Selenium is a portable testing framework specialized for web applications. As this excercise required testing a website, I needed to use a web testing framework. Selenium is one of the most versatile test frameworks, working with Python, Ruby, Java [etc](https://en.wikipedia.org/wiki/Selenium_(software)). It can even be used without these languages in its own IDE. Using a web-testing framework was new territory for me, so I chose the framework I understood as most versatile and offered most flexibility.

### IDE - PyCharm
Though it is not inheirent to the test suite, these tests were developed in PyCharm. It is a commonly used IDE that has a lot of useful features for developers such as debuging, breaks, #ToDo, version control, variable replacement etc. If the test code can be read easily in PyCharm, it likely reads well for most users. I recomend inspecting the code using PyCharm as it will color highlight """ Extended Comments """ and #ToDo's. I use these to explain the test details, limitations and further improvements. 

## Executing Tests

## Test Design


### Assumptions


### Test improvements



## Test Suite Improvements/Needs Work
* Provide Setup() function
  * As of now there is no function that can be called externally to setup the webpage and driver. Adding a setup function would complete the test suit such that its modules can be called by other scripts or via the command line, without having to set up the driver manually.
* Add multiple browser driver options (Firefox, Edge, Safari) so multiple web browsers can be tested

