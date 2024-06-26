import pandas as pd
import re

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
    # Handle case where the input is not a string
    if isinstance(raw_html, str):
        cleantext = re.sub(CLEANR, '', raw_html)
        return cleantext
    else:
        return ''  # or another suitable default value

# Read the CSV file
input_csv_path = '/Users/samarthsrinivasa/Desktop/Classes/CS178A/course-project-fifty-fifty/scraped_data.csv'
output_csv_path = '/Users/samarthsrinivasa/Desktop/Classes/CS178A/course-project-fifty-fifty/cleanedforcsv.csv'

df = pd.read_csv(input_csv_path)

# Apply cleanhtml function to the HTML data column
df['Cleaned_Text'] = df['Text'].apply(cleanhtml)

# Save the result to a new CSV file
df[['Website', 'Cleaned_Text']].to_csv(output_csv_path, index=False)

print(f'Cleaning and saving complete. Output saved to {output_csv_path}')
