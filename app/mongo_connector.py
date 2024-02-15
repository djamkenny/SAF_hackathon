# mongo_connector.py

from pymongo import MongoClient

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "agriculture_monitoring"
COLLECTION_NAME = "sensor_data"

def log_sensor_data(data):
    """
    Log sensor data to MongoDB.
    """
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_URI)
        database = client[DATABASE_NAME]
        collection = database[COLLECTION_NAME]

        # Create a document with the sensor data
        sensor_document = {
            "moisture": data[0],
            "ph": data[1],
            "nutrients": data[2],
            "temperature": data[3],
            "chlorophyll": data[4],
            "leaf_moisture": data[5],
            "disease_presence": data[6],
            "decision": data[7],
        }

        # Insert the document into the collection
        collection.insert_one(sensor_document)

        print("Sensor data logged to MongoDB successfully.")

    except Exception as e:
        print(f"Error logging sensor data to MongoDB: {str(e)}")

    finally:
        # Close the MongoDB connection
        if client:
            client.close()

# Other MongoDB-related functions (e.g., querying data) can be added here.
