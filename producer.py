import json
import time

from kafka import KafkaProducer
from geopy.geocoders import ArcGIS


ORDER_KAFKA_TOPIC = "order_detail"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Will generate one unique order every 5 seconds")
time.sleep(10)

arc=ArcGIS()
for i in range(ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i,
        "items": arc.geocode('haifa'),
    }

    producer.send("order_details", json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(5)