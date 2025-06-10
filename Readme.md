
# 🌐 IoT MQTT Sensor Simulator

This project simulates an IoT device that publishes sensor data to an MQTT broker and optionally visualizes the data in real time using Grafana.

---

## 🔍 Overview

This simulator mimics an IoT setup that:

- 📡 Publishes synthetic sensor data (temperature, humidity, air quality, pressure) every 5 seconds  
- 📨 Subscribes to control commands (e.g., `Relay_Output` toggle) via MQTT  
- 🧰 Uses `test.mosquitto.org` as the default MQTT broker  
- 📊 Optionally integrates with MongoDB and Grafana via a Dockerized stack for real-time monitoring

---

## 📁 Project Structure

```
IoT_Project/
├── datacake_simulator.py   # Main simulator script
└── README.md               # Project overview and instructions
```

---

## 🚀 Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nidhi276/IoT_Project.git
   cd IoT_Project
   ```

2. **Install requirements:**

   ```bash
   pip install paho-mqtt
   ```

3. **Run the simulator:**

   ```bash
   python datacake_simulator.py
   ```

   Sensor data will be published to:
   - Topic: `sensorvalues/iot`

---

## 🧪 Example Data

**Sensor Payload:**
```json
{
  "TEMPERATURE_C": 21.85,
  "HUMIDITY_PERCENT": 62.4,
  "AIR_QUALITY_INDEX": 76,
  "PRESSURE_KPA": 101.25
}
```

**Control Message:**
```json
{ "Relay_Output": true }
```

---


## 🛡️ Notes

- Public MQTT broker (`test.mosquitto.org`) is used for testing only  
- Replace with a secure broker for production use  
- MongoDB + Grafana setup is optional and can be deployed locally or to the cloud

---

