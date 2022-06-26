import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zml9gw6.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")

students.delete_many({})
def insert_one(student): 
    return students.insert_one(student).inserted_id
print ("-- INSERT STATEMENTS --")
bill = {"student_id": 1007,
    "first_name": "Bill",
    "last_name": "Jackson"}
bill_student_id = insert_one(bill)
print("Inserted student record {} {} into the students collection with document_id {}".format(bill["first_name"], bill["last_name"], bill_student_id))

ella = {"student_id": 1008,
    "first_name": "Ella",
    "last_name": "Jackson"}
ella_student_id = insert_one(ella)
print("Inserted student record {} {} into the students collection with document_id {}".format(ella["first_name"], ella["last_name"], ella_student_id))

kim = {"student_id": 1009,
    "first_name": "Kim",
    "last_name": "Jackson"}
kim_student_id = insert_one(kim)
print("Inserted student record {} {} into the students collection with document_id {}".format(kim["first_name"], kim["last_name"], kim_student_id))
input("\n\n  End of program, press any key to exit... ")


===
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
print("Inserted student record {} {} into the students collection with document_id {}".format(kenny["first_name"], kenny["last_name"], kenny_student_id))
print()

print ("-- DISPLAYING NEW STUDENT LIST DOC --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
    print()
    
doc.students.remove_one({"student_id": "1010"})