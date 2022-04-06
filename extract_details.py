import spacy
from get_name import *
from datetime import date


def extract(text):
    name = get_name(text)
    age = get_age(text)
    today = date.today().isoformat()

    medicines = []
    med7 = spacy.load("./model")
    doc = med7(text)
    d = {}
    for ent in doc.ents:
        if ent.label_ == 'DRUG':
            medicines.append(d)
            d.clear()
        d[ent.label_] = ent.text
    return name, age, today, medicines


if __name__ == "__main__":
    print(extract("A patient kumar aged 22 was prescribed paracetamol 500mg thrice for 5 days and viagra 250mg night for 2 days."))
