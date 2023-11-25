import pandas as pd
import requests
from bs4 import BeautifulSoup
import validators
import time
import csv
import re


CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

asmd = pd.read_csv("/Users/samarthsrinivasa/Desktop/Classes/CS178A/course-project-fifty-fifty/asmd_incidents.csv")

asmd_link = asmd["Original Link(s)"]

text_data = []  # List to store website URL and text data
link_count = 0  # Initialize link count to zero

output_file = 'scraped_data.csv'

with open(output_file, 'a+', encoding='utf-8-sig', newline='') as file:
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

                            # Extract text using the provided HTML structure
                            text_elements = soup.find_all('p', class_='article__paragraph')
                            page_text = ' '.join([element.text for element in text_elements])

                            # Remove unwanted patterns using regular expressions
                            ad_patterns = re.compile(r'\b(?:ad|advertisement)\b', flags=re.IGNORECASE)
                            page_text = re.sub(ad_patterns, '', page_text)

                            # Remove HTML tags using the cleanhtml function
                            cleantext = cleanhtml(page_text)
                            text_data.append([link, cleantext])
                            writer.writerow([link, cleantext])

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
