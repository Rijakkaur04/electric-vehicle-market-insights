# Multi-System Deployment & Video Demonstration Guide
**Project:** Electric Vehicle Market Performance & Insights  
**Program:** Data Analytics with Tableau (MySkillWallet / SmartBridge)  

---

## 🌐 Part 1: Free Cloud Deployment (Get Your Live Demo URL)

You can deploy this web application to the cloud in **less than 2 minutes** completely for free so that your mentor, evaluators, or anyone on any device can access it 24/7 without needing to install anything.

### Recommended Method: Render.com (100% Free & Automatic)

This repository includes pre-configured [`render.yaml`](../render.yaml), [`Procfile`](../Procfile), and [`wsgi.py`](../wsgi.py) files.

1. **Push your latest commits to GitHub:**
   ```powershell
   cd "C:\Users\user\.gemini\antigravity\scratch\electric_vehicle_market_insights"
   git push -u origin main
   ```
2. **Sign up / Log in to [Render.com](https://render.com):**
   * Select **"Sign in with GitHub"**.
3. **Create New Web Service:**
   * Click the **"New +"** button in the top right and choose **"Web Service"**.
   * Select **"Build and deploy from a Git repository"**.
   * Locate and click **Connect** next to `Rijakkaur04/electric-vehicle-market-insights`.
4. **Configure & Launch:**
   * **Name:** `ev-market-insights`
   * **Region:** Any (e.g. Oregon / Frankfurt / Singapore)
   * **Branch:** `main`
   * **Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT`
   * **Instance Type:** **Free** ($0/month)
   * Click **"Create Web Service"**.
5. **Get Your Live URL:**
   * Render will build and deploy the container in ~60-90 seconds.
   * Your live demo link will appear at the top (e.g., `https://ev-market-insights.onrender.com`).
6. **Submit on MySkillWallet:**
   * Paste `https://ev-market-insights.onrender.com` into **"Add Demo Link"** on your [MySkillWallet Dashboard](https://myskillwallet.ai)!

---

## 💻 Part 2: Running Across Different Systems

The project is engineered to run seamlessly across all operating systems and hardware configurations.

### 1. Windows (Native One-Click)
* Simply double-click [`run_app.bat`](../run_app.bat).
* Or in PowerShell:
  ```powershell
  python -m pip install -r requirements.txt
  python web_app\app.py
  ```

### 2. macOS & Linux
* In terminal:
  ```bash
  python3 -m pip install -r requirements.txt
  python3 wsgi.py
  ```

### 3. Docker (Any OS with Zero Dependency Setup)
With Docker or Docker Desktop installed:
```bash
# Build and run with Docker Compose
docker compose up -d

# Or with raw Docker CLI:
docker build -t ev-market-insights .
docker run -d -p 5000:5000 --name ev-portal ev-market-insights
```
The app will immediately be live at `http://localhost:5000`.

### 4. Accessing from Mobile / Different Systems on Same Wi-Fi
1. Find your computer's local IP address:
   * **Windows:** Run `ipconfig` (e.g. `192.168.1.15`)
   * **Mac/Linux:** Run `ifconfig` or `ip a`
2. Start the app: `python wsgi.py`
3. Any phone, tablet, or laptop connected to the same Wi-Fi can open:
   `http://192.168.1.15:5000`

---

## 🎥 Part 3: 2–3 Minute Video Demo Script (Loom / YouTube)

If you prefer submitting a Loom or YouTube video demo as your Demo Link, record your screen and follow this step-by-step walkthrough:

### Recording Checklist:
* **Tool:** [Loom](https://www.loom.com/) (free browser extension) or OBS Studio.
* **Open in Browser:** `http://127.0.0.1:5000` (or your Render URL).

### Video Script Timeline:

* **0:00 – 0:30 | Project Introduction & Overview (Home Page)**
  * *Show:* Home / Overview page with top KPI cards ($530B Revenue, 16.6M units, 542 km avg range).
  * *Say:* "Hello everyone. This is my capstone project for Data Analytics with Tableau on MySkillWallet, titled Electric Vehicle Market Performance & Insights. The objective of this project is to analyze global EV adoption, battery chemistry tradeoffs, and manufacturer market share across three key industry scenarios."

* **0:30 – 1:05 | Scenario 1: Emily Johnson (Strategy Portal)**
  * *Click:* **Strategy (Emily)** in navigation bar.
  * *Show:* Category breakdown chart, OEM leaderboard, and change the **Year** dropdown filter to 2024.
  * *Say:* "Scenario 1 addresses Emily Johnson, Market Strategy Director. Here we see that SUVs and Sedans generate over 75% of cumulative sales revenue. The dashboard features dynamic filters by Model Year, Vehicle Category, and Production Region, highlighting that transitioning mid-market SUVs to LFP batteries maximizes profitability."

* **1:05 – 1:40 | Scenario 2: David Chen (Competitive BI Portal)**
  * *Click:* **BI (David)** in navigation bar.
  * *Show:* Battery technology donut chart and Country Production chart.
  * *Say:* "Scenario 2 targets David Chen, Automotive BI Manager. Tesla and BYD hold an oligopoly with over 42% volume share. Over 52% of assembly remains clustered in China, demonstrating why automotive consulting clients must localize battery Gigafactories in Europe and North America to shield against tariffs."

* **1:40 – 2:10 | Scenario 3: Dr. Sarah Williams & Story Mode**
  * *Click:* **Research (Dr. Sarah)** and then **Tableau Story**.
  * *Show:* Driving Range vs. Battery Capacity scatter plot, then click through Story Point tabs (1 through 5).
  * *Say:* "For Dr. Sarah Williams, we explore electrochemical efficiencies. Solid-state batteries break the 800 km range frontier. In the Tableau Story mode, we guide stakeholders through 5 narrative points—from the 2019 adoption inflection to the 2030 decarbonization roadmap where electric transit buses yield 45 tons of net CO2 savings annually."

* **2:10 – 2:30 | Performance Testing & Conclusion**
  * *Click:* **Performance** tab and highlight the benchmark stats (sub-5ms query response times).
  * *Say:* "Finally, our performance benchmarks verify sub-5 millisecond query execution times, and the complete Tableau workbook (.twbx) and dataset are available for direct download. Thank you!"

---

## 📋 Summary: Links to Submit on MySkillWallet

1. **GitHub Link:** `https://github.com/Rijakkaur04/electric-vehicle-market-insights`
2. **Demo Link:**
   * Your Render cloud URL: `https://ev-market-insights.onrender.com`
   * OR your Loom / YouTube recording URL.
