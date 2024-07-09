# import influxdb_client, os, time
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS

# token = os.environ.get("INFLUXDB_TOKEN")

# org = "sa"
# url = "http://localhost:8086"

# write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


# bucket="bucket1"

# write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
# for value in range(10):
#   point = (
#     Point("measurement1")
#     .tag("tagname1", "tagvalue1")
#     .field("field1", value)
#   )
#   ss= write_api.write(bucket=bucket, org=org, record=point)
#   print(ss,value)
#   time.sleep(2) # separate points by 1 second

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
import random
from datetime import datetime

# Configuration
token = os.environ.get("INFLUXDB_TOKEN")
org = "sa"
url = "http://localhost:8086"
bucket = "bucket1"

# Create client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Function to generate radar data
def generate_radar_data():
    x = round(random.uniform(-100.0, 100.0), 2)
    y = round(random.uniform(-100.0, 100.0), 2)
    z = round(random.uniform(-100.0, 100.0), 2)
    doppler = round(random.uniform(-10.0, 10.0), 2)
    timestamp = datetime.utcnow().isoformat()
    return x, y, z, doppler, timestamp

# Send data to InfluxDB
for _ in range(10000):
    x, y, z, doppler, timestamp = generate_radar_data()
    point = (
        Point("radar_measurement")
        .field("x", x)
        .field("y", y)
        .field("z", z)
        .field("doppler", doppler)
        .time(timestamp, WritePrecision.NS)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Written: x={x}, y={y}, z={z}, doppler={doppler}, time={timestamp}")
    time.sleep(.5)  # Separate points by 2 seconds

print("Data generation completed.")
