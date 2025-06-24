from ocr_engine import extract_text
from PIL import Image
import re


# Function for extracting the address from a long string
def extract_location(loc_string):
    return loc_string.partition('(')[0]



# Function for extracting the necessary data from the detected text
def extract_data(imgFileName: str):
    detected_txt = extract_text(imgFileName)

    pickup_location, drop_off_location, date, fare = '', '', '', ''

    # Detect the text from the image using ocr_engine.py
    # Splitting text to a list of lines
    lines = detected_txt.splitlines()
    
    lines = [line for line in lines if re.search(r"\w+", line)]   # Removing the empty lines
    

    for i, line in enumerate(lines):
        
        # Removing spaces in each line
        line = line.strip() 

        # Using Regex to extract pickup and drop-off locations
        if re.search(r"pickup location", line, re.IGNORECASE):
            pickup_location = lines[i+1].strip()

            pickup_location = extract_location(pickup_location)

        if re.search(r"drop-off location", line, re.IGNORECASE):
            drop_off_location = lines[i+1].strip()

            drop_off_location = extract_location(drop_off_location)
        

        # Using Regex to extract the date from the line (if a date was found)
        date_match = re.search(r"[A-Za-z]+\s+\d{1,2},\s+\d{4}", line)
        if date_match:
            date = date_match.group()

        # Using Regex to extract the fare from the lines (if a fare was found)
        fare_match = re.search(r"EGP\s+(\d+[.,]\d+)", line)
        if fare_match:
            fare = fare_match.group(1).replace(',', '.')

        # Converting fare to float. If not, an integer. If not, left as a string.
        try:
            fare = float(fare)
        except:
            fare = fare
    
    return [pickup_location, drop_off_location, date, fare]



