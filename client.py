import requests
import time
import myrio_base as myRIO
from myrio_base import G, B, R, BLUE, GREEN, RED, RGB_OFF

URL = "http://127.0.0.1:5000"
URL_PATH = URL + "/api/data"

myrio1 = myRIO.MyRIO()

while True:
    data = {
        "device_id": "sensor_1" ,
        "value": round(myrio1.read_MXP_temperature(), 2)
    }
    r = requests.post(URL_PATH, json=data)
    print(f"Sent: {data}, Response: {r.json()}")
    time.sleep(5)
