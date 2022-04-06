import spacy
import re

from nltk.corpus import stopwords
stop = stopwords.words('english')


def extract_names(text):
    nlp = spacy.load("en_core_web_sm")
    names = []
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
    return names


def get_age(text):
    return re.findall(r'\d{1,3}', text)[0]


def get_name(text):
    return extract_names(text)[0]


if __name__ == "__main__":
    print(get_name("A patient rishi kumar aged 22 was prescribed paracetamol 500mg thrice for 5 days and viagra 250mg night for 2 days."))