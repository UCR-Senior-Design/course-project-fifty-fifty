import pandas as pd
import requests
from bs4 import BeautifulSoup
import validators
import time
import csv

asmd = pd.read_csv(r'')  # Fixed the path

asmd_link = asmd["Original Link(s)"]

text_data = []  # List to store website URL and text data

link_count = 0  # Initialize link count to zero

# Define the name of the output CSV file
output_file = 'scraped_data.csv'

with open(output_file, 'a+', encoding='utf-8-sig', newline='') as file:
    # Save the data to a CSV file with two columns (website and text)
    writer = csv.writer(file)
    writer.writerow(['Website', 'Text'])
    for cell in asmd_link:  # Changed from asmd["Original Link(s)"]
        if pd.notna(cell):  # Check if the cell is not NaN
            # Split the cell content by semicolon to get individual URLs
            links = cell.split(';')
            for link in links:
                link = link.strip()  # Remove leading/trailing whitespace
                if validators.url(link):
                    try:
                        response = requests.get(link, timeout=10)  # Set the timeout to 10 seconds
                        link_count += 1  # Increment the link count
                        print(f'Reading link {link_count}: {link}')  # Print a visual indicator for each URL
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            page_text = soup.get_text()
                            text_data.append([link, page_text])  # Append URL and text to the list

                            # Write the current URL and text to the CSV file immediately
                            writer.writerow([link, page_text])

                            time.sleep(2)  # Sleep for 2 seconds to avoid overloading the server
                        else:
                            print(f"Invalid URL: {link}")
                    except Exception as e:
                        print(f"Error processing URL {link}: {e}")
                        time.sleep(2)  # Sleep for 2 seconds in case of an error
                else:
                    print(f"Invalid URL: {link}")
                    time.sleep(2)  # Sleep for 2 seconds for invalid URLs

print(f'All {link_count} links from the web pages have been read and saved to {output_file}')
