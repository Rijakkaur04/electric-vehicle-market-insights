# ⚡ Electric Vehicle Market Performance & Insights
### *Enterprise Data Analytics, Tableau Dashboarding & Web Integration Platform*

[![Tableau](https://img.shields.io/badge/Tableau-Desktop%20%7C%20Public-E97627?style=for-the-badge&logo=Tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.14-3776AB?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=Flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Project%20Status-100%25%20Completed-10B981?style=for-the-badge)](https://myskillwallet.ai)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

---

## 📌 Submission Overview & Quick Links
* **Capstone Platform:** [MySkillWallet.ai](https://myskillwallet.ai) (Powered by SmartBridge / SmartInternz)
* **Program:** Data Analytics with Tableau
* **Project Module:** `data-analytics-with-tableau-6abcef62500f0d3aeede46d5`
* **Local Web Demo:** `http://127.0.0.1:5000` (Launch via `run_app.bat`)
* **Tableau Workbooks:**
  * [`tableau/Electric_Vehicle_Market_Performance.twbx`](tableau/Electric_Vehicle_Market_Performance.twbx) (Packaged Workbook with Data)
  * [`tableau/Electric_Vehicle_Market_Performance.twb`](tableau/Electric_Vehicle_Market_Performance.twb) (XML Workbook Definition)
* **Comprehensive Project Report:** [`docs/Project_Report.md`](docs/Project_Report.md)

---

## 📖 Executive Summary
The electric vehicle (EV) industry is experiencing exponential global expansion, driven by environmental mandates, declining battery manufacturing costs, and growing consumer demand for clean mobility. 

This repository provides an enterprise-grade analytics solution analyzing global EV sales, pricing frontiers, battery chemistry trade-offs (LFP, NMC, NCA, Solid-State, Sodium-Ion), manufacturing geography, and customer satisfaction across six vehicle categories (SUVs, Sedans, Hatchbacks, Electric Trucks, Buses, and Two-Wheelers).

---

## 🎯 Three Stakeholder Scenarios Addressed

| Stakeholder Persona | Role & Domain | Primary Mandate & Delivered Solution |
| :--- | :--- | :--- |
| **Emily Johnson** | **EV Market Strategy Director** | • Evaluates sales and revenue contributions by vehicle category.<br>• Identifies leading manufacturers and monitors customer satisfaction.<br>• Optimizes future vehicle trim portfolios via the **Executive Strategy Dashboard**. |
| **David Chen** | **Automotive Business Intelligence Manager** | • Monitors global manufacturer market share and regional assembly hubs.<br>• Analyzes battery chemistry distribution (LFP vs. NMC).<br>• Delivers data-driven market entry consulting via the **Competitive BI Dashboard**. |
| **Dr. Sarah Williams** | **Sustainable Mobility Research Analyst** | • Studies electrochemical energy density and range efficiency ($km/kWh$).<br>• Evaluates commercial fleet life-cycle carbon abatement.<br>• Informs clean transportation policy via the **Sustainable Mobility Research Dashboard**. |

---

## 🏗️ System Architecture

```
                  +----------------------------------------------------+
                  |            DATA EXTRACTION & CLEANING PIPELINE     |
                  |  - Raw CSV Extraction: EV_Market_Data_Raw.csv      |
                  |  - Python Cleansing & Imputation Pipeline          |
                  |  - SQL Schema: ev_market_database.sql              |
                  |  - Cleaned Relational Data: 861 Records / 26 Cols  |
                  +----------------------------------------------------+
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
  +-----------------------------------+           +-----------------------------------+
  |       TABLEAU VISUAL ENGINE       |           |       FLASK WEB INTEGRATION       |
  |  - 9 Analytical Worksheets        |           |  - Flask 3.1 REST APIs            |
  |  - 3 Persona Dashboards           |           |  - Interactive Chart.js Analytics |
  |  - 5-Point Guided Tableau Story   |           |  - Filterable Data Explorer Table |
  |  - Formats: .twb and .twbx        |           |  - Automated Latency Benchmarking |
  +-----------------------------------+           +-----------------------------------+
                    │                                               │
                    └───────────────────────┬───────────────────────┘
                                            ▼
                  +----------------------------------------------------+
                  |               INTERACTIVE USER INTERFACES          |
                  |  - Scenario 1: Strategy Director Portal            |
                  |  - Scenario 2: Competitive BI Portal               |
                  |  - Scenario 3: Sustainable Research Portal         |
                  |  - Tableau Story Mode & Instant CSV/TWBX Exports   |
                  +----------------------------------------------------+
```

---

## 🏆 Project Epics & Tasks Tracking Matrix (100% Completed)

| Epic # | Epic Name | Task ID | Story Description | Status | Deliverable Artifact |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **1** | **Data Collection & Extraction** | Task 1.1 | Multi-source EV dataset sourcing & synthesis | ✅ Completed | `data/raw/EV_Market_Data_Raw.csv` |
| | | Task 1.2 | Relational star schema & SQL database definition | ✅ Completed | `data/raw/ev_market_database.sql` |
| **2** | **Data Preparation** | Task 2.1 | Data cleansing, missing value imputation & standardization | ✅ Completed | `data/processed/EV_Market_Performance_Cleaned.csv` |
| | | Task 2.2 | Feature engineering: Range Efficiency, CSI, Revenue | ✅ Completed | `tableau/calculated_fields_and_parameters.md` |
| **3** | **Data Visualizations** | Task 3.1 | Core worksheets: Category sales, OEM ranks, Chemistries | ✅ Completed | `tableau/Electric_Vehicle_Market_Performance.twb` |
| | | Task 3.2 | Advanced worksheets: Range vs. Capacity, Trajectory | ✅ Completed | 9 Tableau Worksheet XML definitions |
| **4** | **Dashboard Development** | Task 4.1 | Executive Strategy Dashboard (Emily Johnson) | ✅ Completed | `Dashboard 1 - Executive Strategy` |
| | | Task 4.2 | Competitive BI & Manufacturing Dashboard (David Chen) | ✅ Completed | `Dashboard 2 - Competitive BI` |
| **5** | **Story** | Task 5.1 | 5-point narrative Tableau Story point structure | ✅ Completed | `Story - EV Market Transformation` |
| | | Task 5.2 | Story annotations, executive takeaways & 2030 roadmap | ✅ Completed | Interactive Tableau Storybook |
| **6** | **Performance Testing** | Task 6.1 | Latency benchmarks, LOD efficiency & extract SLA tests | ✅ Completed | `performance_testing/Performance_Testing_Report.md` |
| **7** | **Web Integration** | Task 7.1 | Full-stack responsive Python/Flask web portal | ✅ Completed | `web_app/app.py`, `templates/`, `static/` |
| | | Task 7.2 | Interactive client-side Chart.js & dynamic REST APIs | ✅ Completed | 15 Verified REST & Page Endpoints |
| **8** | **Project Demonstration & Docs** | Task 8.1 | Formal capstone report & architecture documentation | ✅ Completed | `docs/Project_Report.md` |
| | | Task 8.2 | GitHub repository staging, demonstration setup & guide | ✅ Completed | Complete Git Repository & Launcher |

---

## 📊 Tableau Worksheets, Dashboards & Story

### 9 Core Worksheets:
1. **Sales by Vehicle Category:** Stacked bar chart breakdown of volume and turnover across vehicle categories.
2. **Top Manufacturers Leaderboard:** Ranked bar visualization with dual-variable color encoding for gross revenue.
3. **Battery Technology Adoption:** Proportional share analysis of LFP, NMC, NCA, Solid-State, and Sodium-Ion.
4. **Driving Range vs. Battery Capacity:** Multi-chemistry scatter plot illustrating electrochemical pack efficiency.
5. **Global Manufacturing Footprint:** Symbol map detailing country-level vehicle production volumes.
6. **Customer Satisfaction Heatmap:** Segment satisfaction index across vehicle classes and battery types.
7. **Market Growth Trajectory YoY:** Longitudinal multi-line chart tracking adoption curves (2019-2025).
8. **Price vs. Range Efficiency Matrix:** Affordability frontier comparing dollar cost per kilometer range.
9. **Carbon Offset Sustainability:** Quantitative avoided emissions bar chart comparing fleet segments.

### 3 Persona Dashboards:
* **Dashboard 1: Executive Strategy (Emily Johnson)**
* **Dashboard 2: Competitive BI & Manufacturing (David Chen)**
* **Dashboard 3: Sustainable Mobility Research (Dr. Sarah Williams)**

### 5-Point Tableau Story (`Story - EV Market Transformation`):
1. *The Global Adoption Surge (2019-2025)*
2. *Category Dynamics & Revenue Supremacy*
3. *The Electrochemical Frontier: Battery Tech Disruption*
4. *Global Manufacturing Hegemony & Supply Chains*
5. *Strategic Roadmap: Sustainable Mobility Toward 2030*

---

## ⚡ Performance Testing Results & SLA Benchmarks

Automated benchmarks were executed via `performance_testing/benchmark_tests.py`:

| Test Benchmark | Target SLA | Measured Latency | Evaluation |
| :--- | :---: | :---: | :---: |
| **Data Ingestion (861 Records)** | < 250 ms | **4.65 ms** | ✅ Optimal (< 5ms) |
| **Temporal Year Filter (2024)** | < 50 ms | **2.48 ms** | ✅ Instantaneous |
| **Multi-Dimension Filter (SUV/NMC)** | < 50 ms | **1.92 ms** | ✅ Instantaneous |
| **Numerical Range Filter (Price/Range)**| < 50 ms | **1.02 ms** | ✅ Instantaneous |
| **Worksheet Aggregation Query** | < 100 ms | **5.46 ms** | ✅ 18x Faster than SLA |
| **Calculated Field Evaluation** | > 100K ops/sec | **5,049,853 ops/sec** | ✅ Blazing Fast |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
* Python 3.10+ installed
* Modern Web Browser (Chrome, Edge, Firefox)
* Optional: Tableau Desktop or Tableau Public (to open `.twbx` or `.twb` directly)

### 2. Launching the Web Portal
Double-click `run_app.bat` on Windows, or execute via terminal:

```bash
# Navigate to web application directory
cd web_app

# Install dependencies (Flask, pandas, numpy)
pip install -r requirements.txt

# Start the Flask web server
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### 3. Opening in Tableau
Open [`tableau/Electric_Vehicle_Market_Performance.twbx`](tableau/Electric_Vehicle_Market_Performance.twbx) directly in Tableau Desktop or Tableau Public.

---

## 📝 Updating Demo and GitHub Links on MySkillWallet

To submit your project to your mentor on [MySkillWallet](https://myskillwallet.ai):

1. **GitHub Link:**
   * Create a new repository on your GitHub account (e.g. `electric-vehicle-market-insights`).
   * Push this repository to GitHub:
     ```bash
     git remote add origin https://github.com/<your-username>/electric-vehicle-market-insights.git
     git branch -M main
     git push -u origin main
     ```
   * Copy your GitHub repository URL: `https://github.com/<your-username>/electric-vehicle-market-insights`
   * Click **"Add Github Link"** on your MySkillWallet project page and paste the link.

2. **Demo Link:**
   * Option A (Tableau Public): Open `Electric_Vehicle_Market_Performance.twbx` in Tableau Public, click **Server > Tableau Public > Save to Tableau Public**, and copy the published dashboard URL.
   * Option B (Web App Hosting): Deploy this Flask web app to Render, Railway, or PythonAnywhere (free tier) and copy the URL (e.g. `https://ev-market-insights.onrender.com`).
   * Option C (Local Demo / Loom Video): Record a 2-3 minute video demonstration walking through the dashboards and paste the Loom / YouTube unlisted link.
   * Click **"Add Demo Link"** on your MySkillWallet project page and paste the URL.

---

## 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
