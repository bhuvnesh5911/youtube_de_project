# 🎥 YouTube Data Engineering Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/PostgreSQL-16-blue?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Linux-Arch-black?style=for-the-badge&logo=arch-linux">
</p>

---

# 📌 Project Overview

This project is an end-to-end **Data Engineering Pipeline** built completely on **Linux (Arch Linux)**.

The pipeline extracts YouTube channel and video data using the **YouTube Data API v3**, stores raw data in PostgreSQL, transforms it into a dimensional warehouse model, and finally visualizes business insights through interactive Power BI dashboards.

The project follows a modern ETL architecture:

**Extract → Load → Transform → Analyze**

---

# 🏗️ Architecture

```text
YouTube API
     │
     ▼
Python Extraction Scripts
     │
     ▼
Raw Layer (PostgreSQL)
     │
     ▼
Staging Layer
     │
     ▼
Warehouse Layer (Star Schema)
     │
     ▼
Power BI Dashboard
```

---

# 🚀 Tech Stack

| Tool           | Purpose                    |
| -------------- | -------------------------- |
| Python         | Data Extraction & ETL      |
| YouTube API    | Data Source                |
| Pandas         | Data Processing            |
| PostgreSQL     | Data Warehouse             |
| SQLAlchemy     | Database Connection        |
| SQL            | Transformations            |
| Docker         | Containerization           |
| Docker Compose | Multi-container Management |
| Power BI       | Dashboard & Analytics      |
| Git/GitHub     | Version Control            |
| VS Code        | Development Environment    |
| Arch Linux     | Operating System           |

---

# 📂 Project Structure

```text
youtube_de_project/
│
├── raw/                        # Raw CSV files
│
├── scripts/                   # Python ETL scripts
│   ├── extract.py
│   ├── load_raw.py
│   ├── load_videos.py
│   └── transform.py
│
├── sql/
│   ├── raw_sql/
│   ├── staging_sql/
│   └── warehouse_sql/
│
├── config/                    # API KEY
│
├── dashboard/
│   ├── dashboard_overview.png
│   ├── channel_analysis.png
│   └── top_videos_chart.png
│
├── dashboards/
│   └── youtube_dashboard.pbix
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
│
├── requirements.txt
└── README.md
```

---

# 📥 Data Extracted

## Channel Information

* Channel ID
* Channel Name
* Channel Created Date
* Subscribers
* Total Views
* Total Videos

## Video Information

* Video ID
* Channel ID
* Video Title
* Published Date
* Views
* Likes
* Comments

---

# 🗄️ Data Warehouse Design

## Raw Layer

Stores data exactly as received from the API.

Tables:

* `raw.raw_channels`
* `raw.raw_videos`

## Staging Layer

Cleans and standardizes raw data.

Tables:

* `staging.stg_channels`
* `staging.stg_videos`

## Warehouse Layer

Implements a Star Schema.

Dimension Tables:

* `warehouse.dim_channels`
* `warehouse.dim_videos`

Fact Table:

* `warehouse.fact_video_metrics`

---

# 📊 Dashboard Features

✅ Total Subscribers KPI

✅ Total Views KPI

✅ Total Likes KPI

✅ Top 10 Videos by Views

✅ Top Channels by Subscribers

✅ Upload Trend Analysis

✅ Likes vs Views Analysis

✅ Channel-wise Performance

✅ Interactive Filters

---

# 🖥️ Dashboard Preview

<h2 align="center">📈 Complete Dashboard Overview</h2>

<p align="center">
  <img src="dashboard/dashboard_overview.png" width="90%">
</p>

---

<h2 align="center">📊 Channel Analytics Dashboard</h2>

<p align="center">
  <img src="dashboard/channel_analysis.png" width="85%">
</p>

---

<h2 align="center">🏆 Top Videos Analysis</h2>

<p align="center">
  <img src="dashboard/top_videos_chart.png" width="85%">
</p>

---

# ⚙️ How to Run

## Clone Repository

```bash
git clone https://github.com/bhuvnesh5911/youtube_de_project.git
cd youtube_de_project
```

## Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Extraction

```bash
python scripts/extract.py
```

## Load Raw Data

```bash
python scripts/load_raw.py
python scripts/load_videos.py
```

## Run Transformations

```bash
python scripts/transform.py
```

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t youtube-de-project .
```

## Run Docker Container

```bash
docker run --rm youtube-de-project
```

## Run Using Docker Compose

```bash
docker compose up --build
```

---

# 📈 Future Improvements

* Apache Airflow Integration
* Incremental Data Loading
* Data Quality Checks
* CI/CD Pipeline using GitHub Actions
* Cloud Deployment (AWS/GCP)
* Monitoring & Logging

---

# 🎯 Key Learnings

* REST API Integration
* ETL Pipeline Development
* Data Warehousing
* Star Schema Modeling
* SQL Transformations
* PostgreSQL Administration
* Docker Containerization
* Power BI Dashboarding
* Linux-based Development
* Git & GitHub Workflow

---

# 👨‍💻 Author

## BHUVNESH LODHA

**Aspiring Data Engineer**

<p align="center">
⭐ If you found this project useful, consider giving it a star!
</p>
