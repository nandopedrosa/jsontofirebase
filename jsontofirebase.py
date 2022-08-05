#article reference: https://www.daryllukas.me/how-to-import-data-into-firebases-firestore/

import json
import os
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("service_key.json") # Download from firebase console
firebase_admin.initialize_app(cred)

db = firestore.client()

for filename in os.listdir('data'): #Iterate through each json in the data directory
    if filename.endswith('.json'):        
        collection_name = filename.split('.')[0] # The name of the collection is the file prefix
        f = open('data/' + filename, 'r', encoding='UTF-8')
        docs = json.loads(f.read())
        for doc in docs:            
                db.collection(collection_name).add(doc)

print("Finished sending the json files to Firebase.")
