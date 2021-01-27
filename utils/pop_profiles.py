import pickle
from utils.couchWriter import couchWriter

# set these keys for uniform documents
keys = set(['State','Chamber_of_Congress','Name','Party','Twitter','username'])

cw = couchWriter() #couchWriter instance

with open('C:/Users/johnr/OneDrive/Documents/GitHub/Plato/politician_profiles.pickle','rb') as f:
    f.seek(0)
    data = pickle.load(f)

failures = []

for doc in data.values():
    doc = dict(doc)

    del doc['name']
    try:
        del doc['Instagram']
    except KeyError:
        pass

    for key in keys-set(doc.keys()):

        doc[str(key)] = ''

    try:
        cw.save_doc(doc,dbname='data_profiles')

    except ValueError:

        print(doc)