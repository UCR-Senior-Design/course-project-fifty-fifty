import pandas as pd
import re

# Read the CSV file
asmd = pd.read_csv('/Users/samarthsrinivasa/Desktop/Classes/CS178A/course-project-fifty-fifty/cleanedforcsv.csv')

# Drop rows with NaN values in the "Cleaned_Text" column
asmd_cleaned = asmd.dropna(subset=['Cleaned_Text'])

# Define a function to remove specific strings, weird symbols, cells with 1-3 spaces, and cells with only the word "Text"
def clean_text(text):
    # Remove specific strings
    specific_strings_to_ignore = [
        "No related articles found for this article.",
        "Get free summaries of new opinions delivered to your inbox!",
        "Secure .gov websites use HTTPS A lock LockA locked padlock or https // means you ve safely connected to the .gov website. Share sensitive information only on official, secure websites.",
        "Select an article in the document viewer.",
        "The Record of North Jersey",
        '''PDF-1.5       1 0 obj  endobj 2 0 obj stream                                                                                                                                                                         Non-Precedential                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           endstream endobj 3 0 obj /ExtGState/ProcSet /PDF/Text/ImageB/ImageC/ImageI /MediaBox 0 0 612 792 /Contents 9 0 R/Group/Tabs/S/StructParents 1/Parent 10 0 R endobj 9 0 obj stream x    o 8     Z S Ey      k     . k       C E I    Eq ! 7O  d   Og      n     G   G   G Oo  n         O              5     4     buxpzqxp  p     C'V    U- ..  / Lq       /        w0  N  O  9  LTj M d Fb   ?8   s    5r J  R   g   r   H  x. T  xV d t    b       F   T   m Dc  I  KP d IEd    Z ,     "y    HG  a x  y 2uGH 8   h9   'bt K    E2 sd HQ   ' h    K   O   m    xb  b5   7  u   H     '   6  6 YU     1p  ' i   R R   9  t  6 lBM  1qa xx5 o eh    Wn 2N   C  ilws  Y     4  Vv t    Gg  9   O "    J   S   y p     B . TU   5 ?      fV   v     1          t8 YP    E     7 N7  L 38 p9u    .  D4 f YVv      u6         Q       P ?S7qG m    nV y?  42     8  t    g grFt   t  HC  ?Wh J3 0vV   L  "9        f 6 a  q oys2  Y  I-     p   X d   J   o         /      C sG g O VU    4     E M  , J   T G    I   h j           W5 lJ  wb  .   hL   wq  A   YT J C f ?    D   C  ,D    dk  TvN    hlc ek      T       Mf.b  T  k''',
        '''Secure .gov websites use HTTPS                                 A lock                 LockA locked padlock                 or https // means you ve safely connected to the .gov website. Share sensitive                 information only on official, secure websites.''',
        '''PDF-1.4       2 0 obj stream x   y TG xW  f an    AFT    0       E1 xabL n4 I Gc d! X s g  q Z!  bC  " X  AXN 3  qJ    8h  Y3?5. q!B      k      t b X        B/      L   H.y        o   nn  4 K   O k  q   n    Dc  a 6 0     /   f 7  l   L  i ,     G  S      fjV Mb      DXb,  4     '  y K y 4  d      L ? ?    4  d G          N   b I    A  '  r Z   '  9   v   O  7 qxv      N a'  S      4''',
        "Thank you for your donation!             There was an issue submitting your request.",
        "Secure .gov websites use HTTPS                                               A lock                 LockA locked padlock                 or https // means you ve safely connected to the .gov website. Share sensitive                 information only on official, secure websites."

    ]
    
    for ignore_string in specific_strings_to_ignore:
        text = text.replace(ignore_string, '')

    if "Secure .gov websites use HTTPS" in text:
        return None 
    
    cleaned_text = re.sub(r'[^A-Za-z0-9.,!?/\-\'"]', ' ', str(text))
    
    if re.match(r'^\s{1,3}$', cleaned_text):
        return None 
    
    if cleaned_text.lower() == 'text':
        return None  
    
    return cleaned_text.strip()  

asmd_cleaned['Cleaned_Text'] = asmd_cleaned['Cleaned_Text'].apply(clean_text)

asmd_cleaned = asmd_cleaned[asmd_cleaned['Cleaned_Text'] != '']

asmd_cleaned = asmd_cleaned.dropna(subset=['Cleaned_Text'])

asmd_cleaned = asmd_cleaned.drop_duplicates(subset=['Cleaned_Text'])

asmd_cleaned.to_csv('/Users/samarthsrinivasa/Desktop/Classes/CS178A/course-project-fifty-fifty/cleaned_dataset.csv', index=False)
