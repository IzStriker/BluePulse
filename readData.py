from influxdb import InfluxDBClient

DB_NAME = "bluepulse"

def main():
    client = setup()
    read(client)

def setup():
    client = InfluxDBClient(host='localhost', port=8086)

    dbs = client.get_list_database()
    res = list(filter(lambda item: item["name"] == DB_NAME, dbs))

    if (len(res) != 1):
        sys.exit(f"Database, {DB_NAME}, does not exist.")

    client.switch_database(DB_NAME)
    return client

def read(client):
    data = client.query(f'SELECT * FROM "device"')
    print(data)
if __name__ == "__main__":
    main()
