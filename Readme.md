# 🌐 IoT MQTT Sensor Simulator for Grafana

This project simulates an IoT device that continuously publishes environmental sensor data (temperature, humidity, air quality, and pressure) to an MQTT broker. The data can be visualized on platforms like **Datacake**, stored in **MongoDB**, and monitored in real time using **Grafana** dashboards.

---

## 🧰 Features

- Simulates four sensor readings every 5 seconds
- Publishes data to `test.mosquitto.org` over MQTT (`sensorvalues/iot`)
- Subscribes to `sensorvalues/iot/control` to receive control commands (e.g., `Relay_Output`)
- Sends and receives data in JSON format
- Easily integrates with Datacake, MongoDB, and Grafana
- Optional Docker-based visualization stack with MongoDB backend

---

## 📁 Project Structure

```bash
IoT_Project/
├── datacake_simulator.py     # Main simulator script
├── docker-compose.yml        # Docker stack: MongoDB + Telegraf + Grafana
├── telegraf.conf             # Telegraf config: MQTT → MongoDB
└── README.md                 # You're here!
```

---

## 🚀 Getting Started

### 1. Clone this Repository

```bash
git clone https://github.com/nidhi276/IoT_Project.git
cd IoT_Project
```

### 2. Install Python Requirements

```bash
pip install paho-mqtt
```

### 3. Run the Simulator

```bash
python datacake_simulator.py
```

This will start publishing data to the MQTT topic `sensorvalues/iot` and listen for relay control on `sensorvalues/iot/control`.

---

## 📡 Example Sensor Payload

```json
{
  "TEMPERATURE_C": 21.85,
  "HUMIDITY_PERCENT": 62.4,
  "AIR_QUALITY_INDEX": 76,
  "PRESSURE_KPA": 101.25
}
```

---

## 🧪 Example Control Message

```json
{ "Relay_Output": true }
```

Console output:
```
🔌 Relay ON - Simulated action executed.
```

---

## 🔌 Extension: Real-Time Monitoring with Docker + MongoDB + Grafana

This simulator can be extended to store and visualize data using Dockerized services: **MongoDB** for storage, **Telegraf** for MQTT ingestion, and **Grafana** for real-time dashboards.

### 🐳 What the Extension Includes

- `docker-compose.yml`: Spins up MongoDB, Telegraf, and Grafana.
- `telegraf.conf`: Subscribes to `sensorvalues/iot` from the MQTT broker, parses JSON, and stores it in MongoDB.
- Grafana: Reads from MongoDB and displays sensor metrics in visual panels.

### ⚙️ How to Use It

1. Make sure Docker and Docker Compose are installed.
2. Copy `docker-compose.yml` and `telegraf.conf` to your project directory.
3. Run:

```bash
docker-compose up -d
```

4. Open Grafana at [http://localhost:3000](http://localhost:3000)  
   Login: `admin` / `admin`

5. Add **MongoDB** as a data source in Grafana:
   - URL: `mqtt_mongodb:27017`
   - Database: `iot_data`
   - Collection: `sensor_readings`

6. Build dashboards using your real-time sensor data.

### 📡 Architecture Overview

```text
[Python Simulator] 
     ↓ MQTT (sensorvalues/iot)
[test.mosquitto.org Broker] 
     ↓
[Telegraf MQTT Input]
     ↓
[MongoDB → Grafana Dashboard]
```

> 💡 This setup helps you simulate and monitor an end-to-end IoT pipeline, from virtual sensors to a live dashboard.

---

## 🛡️ Notes

- This project uses the public broker `test.mosquitto.org` (for testing/demo only)
- For production, use a secured and authenticated broker
- MongoDB and Grafana run locally via Docker (can be deployed to the cloud)

---

## 📄 License

MIT License. You are free to use, modify, and distribute.

---

## 🙋‍♀️ Author

Developed by [Nidhi Shah](https://github.com/nidhi276)  
💬 Feel free to open issues or discussions on this repository!
