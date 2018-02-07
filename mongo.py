from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://localhost:27017")

db = client.test

result = db.item.insert_one(
	{
		"name": "pi",
		"price":"52.65"
	}
)
print(result.inserted_id)

