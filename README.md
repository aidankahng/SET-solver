## SET Solver using Selenium

This program will automatically open a browser and solve the daily SET game for you.
Has the option to input your username as well after solving the daily set puzzle.

### How To Use:

1. Download this repo
2. inside of the repo, open cmd console and run the following:
```
> [MAC] python3 -m venv venv OR [PC] python -m venv venv
> [MAC] venv/bin/activate OR [PC] venv\Scripts\activate
> pip install selenium
```
3. Download a stable "chromedriver" for your OS and place in the same directory
```
> https://googlechromelabs.github.io/chrome-for-testing/
```
4. Modify the defaults as you like to change timing or even submit under a specified username
5. Run the file with the command:
```
> python selenium_set_scraper.py
```
6. That's it! Enjoy your new SET highscore!

### How it Works:

This program solves the SET game using python and selenium by converting card identifiers into ternary and comparing their values. Changes to the setgame website may break this script and all cards but be visible while running in order to properly click the cards.

### It's Broken / I Need Help! / Could you build {COOL_THING_HERE} next?

For bug-fixing and other project ideas
Contact me at: aidankahng@gmail.com