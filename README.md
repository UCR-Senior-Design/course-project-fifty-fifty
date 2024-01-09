# GenderEqualityChatbot

### Webscraper

To run webscraper: Afer cloning project onto local device, within Scrape.py, change the path to asmd_incidents.csv to your local path, then you can run python3 scrape.py to run the code and scrape all the data. It normally takes around 2-3 hours to fully scrape all the websites, which after you can clean the data further (removing unncessesary characters, symbols, specific strings that were not caught, and empty cells) using python3 dataset.py (with the paths changed). Finally, run python3 clean.py (after changing the input and output paths in the code) to convert the outputted CSV file to a json format. 
