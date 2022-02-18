# Python Behave Example With Sauce Labs

> ###### Disclaimer
>
> The code in these scripts is provided on an "AS-IS" basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. These scripts are provided for educational and demonstration purposes only, and should not be used in production. Issues regarding these scripts should be submitted through GitHub. These scripts are maintained by the Technical Services team at Sauce Labs.
>
> Some examples in this repository, may require a different account tier beyond free trial. Please contact the [Sauce Labs Sales Team](https://saucelabs.com/contact) for support and information.

## Prerequisites

In order to complete these exercises you must complete the following prerequisite installation and configuration steps:

* Install Git
* Install `python` and `pip`
* (Optional) Install an IDE (PyCharm, Visual Studio Code, Komodo Edit etc.)

**NOTE*: All code here is written in Python 3, and is not guaranteed to work with Python 2. Since Python 2.x is now EOL, it is strongly, **strongly* recommended you either migrate to Python 3.5+ if you are using Python 2, or get started using Python 3.5+. 


## Running Tests on Sauce Labs

The main purpose of this repository is to show how Sauce Labs works with [Behave](https://behave.readthedocs.io/en/stable/). This example will execute tests on desktop web browsers on Sauce virtual devices.

Behave is known to have issues with running features and scenarios in parallel, since it doesn't currently have parallelization included with the `behave` runner.

First, install dependendencies

```bash
pip install -r requirements.txt
```

and to run tests using

```bash
make run_parallel
```

Since Python includes some C dependencies, Python also include support for `make`. This approach allows for parallelization with Behave.