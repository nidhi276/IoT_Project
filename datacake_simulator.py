import paho.mqtt.client as mqtt
import time
import random
import json
import ssl

# === MQTT Configuration ===
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_USERNAME = ""  # Not required for test.mosquitto.org
MQTT_PASSWORD = ""

# === Unique Client ID ===
CLIENT_ID = "mqtt-device"

# === Topics ===
MQTT_TOPIC = "sensorvalues/iot"
MQTT_CONTROL_TOPIC = "sensorvalues/iot/control"

# === Callback: When Connected ===
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(MQTT_CONTROL_TOPIC)
        print(f"📥 Subscribed to {MQTT_CONTROL_TOPIC}")
    else:
        print(f"❌ Failed to connect, return code {rc}")

# === Callback: When Published ===
def on_publish(client, userdata, mid, properties=None, reason_code=None):
    pass  # Can log publish confirmations here

# === Callback: When Control Message Received ===
def on_message(client, userdata, msg):
    try:
        print(f"[⬇️] Received from {msg.topic}: {msg.payload.decode()}")
        payload = json.loads(msg.payload.decode())

        if "Relay_Output" in payload:
            if payload["Relay_Output"]:
                print("🔌 Relay ON - Simulated action executed.")
            else:
                print("❌ Relay OFF - Simulated action stopped.")
    except Exception as e:
        print(f"❗ Error in message handling: {e}")
6
# === Setup MQTT Client ===
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

# === Connect and Start Loop ===
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"❌ Error connecting to broker: {e}")
    exit()

client.loop_start()
time.sleep(1)  # Allow time to connect

# === Simulate Sensor Values ===
def simulate_sensor_data():
    return {
        "TEMPERATURE_C": round(20 + random.uniform(-2, 2), 2),
        "HUMIDITY_PERCENT": round(60 + random.uniform(-5, 5), 2),
        "AIR_QUALITY_INDEX": random.randint(50, 100),
        "PRESSURE_KPA": round(101.3 + random.uniform(-0.3, 0.3), 2)
    }

# === Main Loop: Publish Sensor Data Every 5 Seconds ===
try:
    while True:
        data = simulate_sensor_data()
        payload = json.dumps(data)
        client.publish(MQTT_TOPIC, payload)
        print(f"[📤] Published to {MQTT_TOPIC}: {payload}")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n[EXIT] MQTT Client shutting down.")
    client.loop_stop()
