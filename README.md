# 🚀 Python-Based High Throughput Log Analytics Monitoring Engine

A **real-time log analytics and anomaly detection system** built using **Python, Dask, and Streamlit**.
This project simulates real-time log generation, processes logs in parallel, detects anomalies using statistical techniques, and visualizes them through an interactive dashboard.

---

## ✨ Key Features

* Real-time log generation
* Parallel log ingestion & processing using **Dask**
* Z-score–based anomaly detection
* Interactive **Streamlit + Plotly** dashboard
* Modular & scalable architecture
* MIT Licensed

---

## 🗂️ Project Structure

```
.
├── anomaly/
│   └── detector.py
│
├── config/
│   ├── dask_config.py
│   └── email_config.py
│
├── dashboard/
│   └── app.py
│
├── ingestion/
│   ├── loader.py
│   └── parser.py
│
├── processing/
│   └── pipeline.py
│
├── log_generator/
│   ├── realtime_log_producer.py
│   └── realtime_logs.csv
│
├── schema/
│   └── schema.py
│
├── data/
│   └── sample_log.log
│
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
└── logvenv/
```

---

## 📄 File Overview

### 🔹 `log_generator/realtime_log_producer.py`

Simulates **real-time log generation** and continuously writes logs into `realtime_logs.csv`.

* Random log levels: `INFO`, `WARN`, `ERROR`
* Random services: `auth`, `payment`, `orders`, `search`
* Mimics real production log streams

---

### 🔹 `main.py`

Acts as the **core controller** of the system:

* Initializes Dask cluster
* Runs log ingestion & processing pipeline
* Detects anomalies
* (Optional) Sends email alerts

---

### 🔹 `dashboard/app.py`

A **Streamlit dashboard** that:

* Reads processed logs
* Detects anomalies
* Visualizes anomaly scores using Plotly
* Allows threshold-based filtering via slider

> Runs independently from `main.py`

---

### 🔹 `processing/pipeline.py`

Builds the log processing pipeline:

* Loads logs using Dask Bag
* Parses logs
* Converts them into a Dask DataFrame
* Handles timestamp conversion

---

### 🔹 `ingestion/loader.py`

Loads log files efficiently using **Dask Bag** for parallel processing.

---

### 🔹 `ingestion/parser.py`

Parses raw log lines using **regular expressions** and extracts:

* timestamp
* level
* service
* message

---

### 🔹 `anomaly/detector.py`

Detects anomalies by:

* Filtering `ERROR` logs
* Aggregating errors per minute
* Computing **Z-scores**
* Flagging statistically significant spikes

---

### 🔹 `config/dask_config.py`

Configures and launches a **local Dask cluster** with:

* Multiple workers
* Threaded execution
* Dask dashboard enabled

---

### 🔹 `schema/schema.py`

Defines the expected schema of logs to ensure consistency during processing.

---

### 🔹 `data/sample_log.log`

Sample log file for testing and validation.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Activate Virtual Environment

```bash
logvenv\Scripts\activate   # Windows
# or
source logvenv/bin/activate  # macOS/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If needed manually:

```bash
pip install dask[distributed] streamlit plotly pandas
```

---

## ▶️ How to Run the Project

### 🟢 Step 1: Start Real-Time Log Producer

```bash
python log_generator/realtime_log_producer.py
```

This will continuously generate logs in real time.

---

### 🟢 Step 2: Run Main Processing Engine

```bash
python main.py
```

This will:

* Start Dask
* Process logs
* Detect anomalies

---

### 🟢 Step 3: Launch Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📊 Dashboard Capabilities

* View detected anomalies
* Interactive anomaly score line chart
* Threshold-based anomaly filtering
* Tabular display of anomalous entries

---

## 🔐 Security Note

For production use:

* Move email credentials to **environment variables**
* Avoid hardcoding sensitive information

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Tanisha Gupta
```

See the full license in the `LICENSE` file.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## ⭐ Acknowledgements

* **Dask** – Parallel computing
* **Streamlit** – Interactive dashboards
* **Plotly** – Data visualization


