import re

# Function to remove punctuations 
def preprocessor(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()
