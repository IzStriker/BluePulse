from influxdb import InfluxDBClient

DB_NAME = "bluepulse"

def main():
    client = InfluxDBClient(host="localhost", port=8086)
    
    dbs = client.get_list_database()
    res = list(filter(lambda item: item["name"] == DB_NAME, dbs))

    if (len(res) == 1):
        print("Database already exists.")
        return
    
    print(f"Creating new database, {DB_NAME}.")

    client.create_database(DB_NAME)

    dbs = client.get_list_database()
    res = list(filter(lambda item: item["name"] == DB_NAME, dbs))


    if (len(res) == 1):
        print("Database created")
    else:
        print("Failed to create database")

if __name__ == "__main__":
    main()
