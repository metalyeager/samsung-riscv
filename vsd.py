import requests
import time
import serial

CHANNEL_ID = "2786157"
READ_API_KEY = "MKNBDAL4P325PF2P"
THINGSPEAK_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"

PARAMETERS = {
    "humidity": {"range": (30, 85), "remark": "High in monsoon, low in summer."},
    "soil_moisture": {"range": (10, 30), "remark": "Low to moderate, requires irrigation."},
    "potassium": {"range": (100, 200), "remark": "Moderate; generally sufficient for crops."},
    "nitrogen": {"range": (200, 400), "remark": "Low; requires regular organic or urea inputs."},
    "phosphorus": {"range": (5, 15), "remark": "Low; requires phosphatic fertilizer inputs."},
    "temperature": {"range": (15, 40), "remark": "Optimal at 20–30°C for most crops."},
}

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

def fetch_data_from_thingspeak():
    try:
        response = requests.get(THINGSPEAK_URL, params={"api_key": READ_API_KEY, "results": 1})
        response.raise_for_status()
        data = response.json()
        if "feeds" in data and data["feeds"]:
            latest_entry = data["feeds"][0]
            return {
                "humidity": float(latest_entry.get("field1", 0)),
                "soil_moisture": float(latest_entry.get("field2", 0)),
                "potassium": float(latest_entry.get("field3", 0)),
                "nitrogen": float(latest_entry.get("field4", 0)),
                "phosphorus": float(latest_entry.get("field5", 0)),
                "temperature": float(latest_entry.get("field6", 0)),
            }
    except:
        return None

def analyze_data(data):
    analysis = {}
    for key, value in data.items():
        if key in PARAMETERS:
            low, high = PARAMETERS[key]["range"]
            remark = PARAMETERS[key]["remark"]
            if low <= value <= high:
                analysis[key] = f"{value} (OK): {remark}"
            else:
                analysis[key] = f"{value} (Out of range!): {remark}"
    return analysis

def send_to_vsdsquadron(data):
    ser.write((str(data) + "\n").encode())

def main():
    while True:
        data = fetch_data_from_thingspeak()
        if data:
            analysis = analyze_data(data)
            send_to_vsdsquadron(analysis)
        time.sleep(60)

if __name__ == "__main__":
    main()
