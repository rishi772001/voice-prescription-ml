from get_name import *
from datetime import date


def extract(text):
    name = get_name(text)
    age = get_age(text)
    today = date.today().isoformat()

    medicines = []
    model = spacy.load("./model")
    doc = model(text)
    d = {}
    for ent in doc.ents:
        if ent.label_ == 'DRUG' and len(d) > 0:
            medicines.append(d.copy())
            d.clear()
        d[ent.label_] = ent.text
    medicines.append(d)
    return name, age, today, medicines


if __name__ == "__main__":
    print(extract("A patient kumar aged 22 was prescribed paracetamol 500mg thrice for 5 days and Amoxicillin 650mg night for 2 days."))
