# FlightFinder [![Build Status](https://travis-ci.org/RyanChristian4427/FlightFinder.svg?branch=master)](https://travis-ci.org/RyanChristian4427/FlightFinder) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

One of the things I enjoy doing the most is traveling. But, as a university student, I need to travel on a budget. That is why I love tools like SkyScanner, which can show the cheapest destinations for a given port of departure. The goals with this tool include relearning Python and to make a desktop app that will give me a simple readout of destinations 1 week in advance, maybe even have it send an email containing pertinent information. This will be a novelty app and little more, as large sites already have this functionality and more.

Current future plans include to add direct links to quote offerings so a user can jump from the app right to purchase, to expand the options menu, so that a user can change the locale, currency, and date range, and to add data validation on the display, as currently, there is none.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use. Currently, this has only been tested on a Linux machine, though the webview should be cross platform. Other platforms (or systems that don't have webkit2gtk as the default rendering engine) are untested.

Current options/abilities of the program:

- Creates a webview for rendering the content of the Flask server
- Allows a user to enter an airport, and returns round-trip flight quotes
- Users can change locale and currency for the quotes (quotes differ by locale, interestingly)

### Prerequisites

What things you need:

```
Python3/pip3
```

### Running

First, navigate to the root project directory and create a virtual environment:

```
python3 -m venv /env
source env/bin/activate
```

Then, install project dependencies:

```
pip install -r requirements.txt
```

Finally, start the app:

```
python3 setup.py
```

A GUI will appear that you can use to run the program.


## Running the tests

All tests are located in ~/tests, and can be ran using the following command from the project root:

```
python -m unittest discover -s tests
```

### Test Methadology

As of now, the only item tested is the data processing for a static and mock data file. This at least ensures at no point does the underlying logic break due to changes in Flask's jsonify implementation or anything similar. Ideally, I'd like to set up a periodic request to the flight API has not changed drastically, but that is something for the future, if I even want to keep this updated.

### Code Style

All Python code is styled by [Black](https://github.com/ambv/black), with no deviations. The styler can be run after setting the virual environment with the command:

```
black flightfinder
```

or 

```
black tests
```

## Authors

* **Ryan Christian** - *Entire Project* - [Ryan Christian](https://github.com/RyanChristian4427)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
