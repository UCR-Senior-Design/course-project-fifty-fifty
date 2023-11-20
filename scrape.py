import pandas as pd
import requests
from bs4 import BeautifulSoup
import validators
import time
import csv
#from lxml.etree import tostring
#import lxml.html
#https://pypi.org/project/adblockparser/
#from adblockparser import AdblockRules
from readability import Document
import re


asmd = pd.read_csv(r'/Users/15623/Desktop/scraping/course-project-fifty-fifty/asmd_incidents.csv')  # Fixed the path

asmd_link = asmd["Original Link(s)"]

text_data = []  # List to store website URL and text data

link_count = 0  # Initialize link count to zero

# Define the name of the output CSV file
output_file = 'scraped_data.csv'

with open(output_file, 'a+', encoding='utf-8-sig', newline='') as file:
    # Save the data to a CSV file with two columns (website and text)
    writer = csv.writer(file)
    writer.writerow(['Website', 'Text'])
    
    for cell in asmd_link:
        if pd.notna(cell):
            links = cell.split(';')
            for link in links:
                link = link.strip()
                if validators.url(link):
                    try:
                        response = requests.get(link, timeout=10)
                        link_count += 1
                        print(f'Reading link {link_count}: {link}')

                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            
                            # Use Readability to extract the main content
                            doc = Document(response.text)
                            page_text = doc.summary()

                            # Remove unwanted patterns using regular expressions
                            ad_patterns = re.compile(r'\b(?:ad|advertisement)\b', flags=re.IGNORECASE)
                            page_text = re.sub(ad_patterns, '', page_text)

                            text_data.append([link, page_text])
                            writer.writerow([link, page_text])

                            time.sleep(2)
                        else:
                            print(f"Invalid URL: {link}")
                    except Exception as e:
                        print(f"Error processing URL {link}: {e}")
                        time.sleep(2)
                else:
                    print(f"Invalid URL: {link}")
                    time.sleep(2)

print(f'All {link_count} links from the web pages have been read and saved to {output_file}')
