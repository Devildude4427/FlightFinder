# FlightFinder [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

One of the things I enjoy doing the most is traveling. But, as a university student, I need to travel on a budget. That is why I love tools like SkyScanner, which can show the cheapest destinations for a given port of departure. The goals with this tool include relearning Python and to make a desktop app that will give me a simple readout of destinations 1 week in advance, maybe even have it send an email containing pertinent information. This will be a novelty app and little more, as large sites already have this functionality and more.

Current future plans include to expand the options menu, so that a user can change the locale, currency, and date range, and to add direct links to quote offerings so a user can jump from the app right to purchase.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use.

Current options/abilities of the program:

- Creates a simple GUI and web server
- Allows a user to enter an airport, and returns round-trip flight quotes

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
