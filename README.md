# Cover Test Monkey
This test suite was developed for Amy at Cover. The test suite is designed to test the following website: https://www.monkeyuser.com/

## Installation instructions
In order to run this suite, the following need to be installed:

* Python 3.7 - Available from Anaconda:  https://www.anaconda.com/distribution/ (Follow instructions)
* Selenium framework - Selenium for python https://pypi.org/project/selenium/
* PyCharm (optional) - Free Community Version https://www.jetbrains.com/pycharm/download

Clone this repository and add to PATH.

## Selection of Tools/Technology
### Language - Python 3.7
Python is high-level general application language that is easy to understand and read. It is well suited for a basic web testing suite. It has many in-built libraries and can work well with external libraries and automation frameworks. Lower-level languages would less practical and time-consuming to test with (if it works). 

### Test Framework - Selenium
Selenium is a portable testing framework specialized for web applications. As this excercise required testing a website, I needed to use a web testing framework. Selenium is one of the most versatile test frameworks, working with Python, Ruby, Java [etc](https://en.wikipedia.org/wiki/Selenium_(software)). It can even be used without these languages in its own IDE. Using a web-testing framework was new territory for me, so I chose the framework I understood as most versatile and offered most flexibility.

### IDE - PyCharm
Though it is not inheirent to the test suite, these tests were developed in PyCharm. It is a commonly used IDE that has a lot of useful features for developers such as debuging, breaks, #ToDo, version control, variable replacement etc. If the test code can be read easily in PyCharm, it likely reads well for most users. I recomend inspecting the code using PyCharm as it will color highlight """ Extended Comments """ and #ToDo's. I use these to explain the test details, limitations and further improvements. 

## Executing Tests
Once python and the selenium framwork is installed, run the test.py file using an IDE or from the command line. 

## Test Design and Assumptions
Test-specific design choices and assumptions are documented within the code.

### Test improvements
For each test, # ToDO improvements are flagged within the code. Some test improvement themes include:
* More accurate test criteria
   * Most checks for whether the user can view X comic depend on comparing the previous and new url. This doesn't include checks on whether the comic has changed. A more rigorous test would verify that not only has navigation occured, but the content has changed also.
 * More comprehensive feature testing
   * Some features occur multiple times on a webpage, for example, two "random comic" buttons. A comprehensive test would scan for x features and test each one

## Test Suite Improvements/Needs Work
During the course of this excercise, there were many opportunities for improvement I found that would benefit the test suite's overall functionality. These improvement tasks include:

* Provide Setup() function
  * As of now there is no function that can be called externally to setup the webpage and driver. Adding a setup function would complete the test suit such that its modules can be called by other scripts or via the command line, without having to set up the driver manually.
* Add multiple browser driver options (Firefox, Edge, Safari) so multiple web browsers can be tested
* Develop a test result printout/html/csv page so test results can be summarized outside of the python output window and are easily exportable.
* Add timer and test time elapsed report

