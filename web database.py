import firebase_admin
from firebase_admin import firestore

cred = credentials.Certificate("/Users/brighamcvalentine/Documents/CS/CS246 Design and Development/web-database-9f4dc-firebase-adminsdk-t6ca9-bc6fd8685a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('people')  # opens 'people' collection
doc = collection.document('john')  # specifies the 'john' document

res = collection.document('josh').set({
    
    'hobbies': [
        'hiking',
        'biking',
        'baking'
    ]
})
print(res)