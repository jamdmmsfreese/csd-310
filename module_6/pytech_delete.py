import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zml9gw6.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")

print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
    print()

def insert_one(student): 
    return students.insert_one(student).inserted_id
print ("-- INSERT STATEMENTS --")
kenny = {"student_id": 1010,
    "first_name": "Kenny",
    "last_name": "Smith"}
kenny_student_id = insert_one(kenny)
print("Inserted student record {} into the students collection with document_id {}".format(kenny["student_id"], kenny_student_id))
print()

print ("-- DISPLAYING NEW STUDENT LIST DOC --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
    print()
    
print ("-- DISPLAYING NEW STUDENT LIST DOC --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
    print()
    
students.delete_one({"student_id": 1010})

print ("-- DELETED STUDENT ID 1010 --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
    print()
input("\n\n  End of program, press any key to exit... ")