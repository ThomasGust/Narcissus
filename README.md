# GitHub Profile View Increaser

This is a Python script that uses multithreading to automate the process of increasing the view count of a GitHub profile. It uses '`selenium` and the `undetected_chromedriver` package to automate a Chrome browser, which visits the specified GitHub profile repeatedly.

## How it Works

The script takes in three command line arguments: the GitHub username, the refresh lag (time between page reloads), and the number of views to be added. 

It then constructs the URL for the GitHub profile and starts a Chrome browser using `undetected_chromedriver`. Currently, all of the windows will run with GUIs, which is something I might work on soon.

The script then enters a loop where it reloads the GitHub profile page and then waits for a random amount of time before reloading again. The random wait time is either slightly more or slightly less than the specified refresh lag.

If the number of views to be added is set to 0, the script will continue to reload the page until it is manually interrupted.

## Getting Started
There isn't much special you need to do to use this code
- Clone the repository
- Install any missing prerequisites
- Big thing here: make sure you have the CORRECT VERSION of chromedriver for your chrome version and operating system, the one that comes with this project is for Windows 11 x64.
- Enjoy!

### Prerequisites

- Python 3.x
- `undetected_chromedriver` package
- `selenium`

## Usage
The script (`main.py`)accepts the following command line arguments:

- `-u` or `--Username`: GitHub Profile Username
- `-t` or `--Threads`: Number of windows or threads to be used
- `-w` or `--Wait-Time`: Average length of delay in between page reloads
- `-v` or `--Views`: The number of views to be added, 0 means run until interrupted

Here is an example of how to use the script:

```bash
python driver.py myusername 5 100