import pymongo 

# Provide the mongodb localhost url to connect python to mongodb 
client = pymongo.MongoClient("mongodb://localhost:27017")

# Create or connect to a database
database = client["mydatabase"]

# collection Name 
collection = database['Products']

# Sample Data 
documents = {'companyName': 'SFSU',
                        'product': 'Affordable School',
                        'courseOffered': 'Computer Science'}

# Insert above records in the collection / Insert documents into the collection
result = collection.insert_one(documents)
print(f"Inserted document IDs: {result.inserted_ids}")

# let verify all the record at once present in the record 
all_record = collection.find()

# Query: Find all documents
all_documents = collection.find()
print("All documents:")
for doc in all_documents:
    print(doc)