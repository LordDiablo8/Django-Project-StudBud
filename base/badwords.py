
import csv

def load_bad_words(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        bad_words = [row[0] for row in reader if row]
    return bad_words

def contains_bad_words(message, bad_words):
    message = message.lower()
    for word in bad_words:
        if word in message:
            return True
    return False