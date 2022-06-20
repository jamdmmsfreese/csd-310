import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ptdopkt.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
db = client.pytech
print("-- Pytech Collection List")
print(db.list_collection_names())
input("\n\n  End of program, press any key to exit... ")