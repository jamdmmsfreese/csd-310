import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ptdopkt.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")

print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()

result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Jackson II"}})

print ("-- DISPLAYING UPDATED STUDENT DOCUMENTS FROM find_one() QUERY --") 
doc = students.find_one({"student_id": 1007})
print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
input("\n\n  End of program, press any key to exit... ")  