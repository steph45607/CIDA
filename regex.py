import re

# text = "#hashtag"

# pattern = re.compile(r'(\#)(\w+)')

# match = pattern.search(text)

# if match:
#     print(match.group(2))
# else:
    

# text = match.group(2)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE) #remove URLs
    text = re.sub(r'\@\w+', '', text) #remove mentions

    pattern = re.compile(r'(\#)(\w+)')
    match = pattern.search(text)
    if match:
        replace = match.group(2)
    else:
        replace = ''

    text = re.sub(r'\#\w+', replace, text) #remove tags, keep word
    text = re.sub(r'\n', ' ', text) #replace new lines with spaces
    text = re.sub(r'[^\w\s]', '', text) #remove punctuations
    print(text)
    # return text.strip()

clean_text("dksajfld httpsfjasdfjsad 258-134 --.., #hashtag2021")