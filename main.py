#!/usr/bin/python3

from influxdb import InfluxDBClient
import bluetooth
import sys
import time

DB_NAME = "bluepulse"

def main():
    client = setup()
    while True:
        scan(client)
        time.sleep(15)

def setup():
    client = InfluxDBClient(host='localhost', port=8086)

    dbs = client.get_list_database()
    res = list(filter(lambda item: item["name"] == DB_NAME, dbs))

    if (len(res) != 1):
        sys.exit(f"Database, {DB_NAME}, does not exist.")

    client.switch_database(DB_NAME)
    return client

def scan(client):
    print("Scanning for bluetooth devices")
    
    json_body = []

    devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)

    num_devices = len(devices)
    print(num_devices, "Devices found")

    for addr, name, d_class in devices:
        data = {
                "measurement": "device",
                "tags": { "MAC": addr },
                "fields": {"Name": name, "class": d_class} 
            }
        
        json_body.append(data)
    
    if len(json_body) > 0:
        client.write_points(json_body)

if __name__ == "__main__":
    main()

