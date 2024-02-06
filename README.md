# GitHub Profile View Increaser

This is a Python script that uses multithreading to automate the process of increasing the view count of a GitHub profile. It uses '`selenium` and the `undetected_chromedriver` package to automate a Chrome browser, which visits the specified GitHub profile repeatedly.

## How it Works

The script takes in three command line arguments: the GitHub username, the refresh lag (time between page reloads), and the number of views to be added. 

It then constructs the URL for the GitHub profile and starts a Chrome browser using `undetected_chromedriver`. The browser is set to not display a startup window and to not use a sandbox for security reasons.

The script then enters a loop where it reloads the GitHub profile page and then waits for a random amount of time before reloading again. The random wait time is either slightly more or slightly less than the specified refresh lag, to make the page visits appear more natural.

If the number of views to be added is set to 0, the script will continue to reload the page until it is manually interrupted.

## Getting Started

### Prerequisites

- Python 3.x
- `undetected_chromedriver` package

### Installing

1. Clone the repository
2. Install Python 3.x if you haven't already
3. Install the `undetected_chromedriver` package using pip: `pip install undetected-chromedriver`

## Usage

Here is an example of how to use the script:

```bash
python driver.py myusername 5 100