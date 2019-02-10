from pymongo import MongoClient

Client = MongoClient(host = "ubuntu", port = 27017)

database = Client["Pythonistas"]

pythonista = {
	"name" : "Daniel",
	"age" : 28,
	"hobby" : "python"
}

database.users.insert_one(pythonista)
