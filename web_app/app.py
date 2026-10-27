"""
Electric Vehicle Market Performance & Insights
Epic 7: Web Integration Application
Backend Web Server (Flask)

Serves the interactive web portal, REST API endpoints, and analytical views
integrating Tableau visualizations and interactive dashboards for all 3 persona scenarios.
"""

import os
import json
import pandas as pd
from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

# Base Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "EV_Market_Performance_Cleaned.csv")
BATTERY_SUMMARY_PATH = os.path.join(BASE_DIR, "data", "processed", "EV_Battery_Technology_Summary.csv")
PERF_JSON_PATH = os.path.join(BASE_DIR, "performance_testing", "test_results.json")
TWB_PATH = os.path.join(BASE_DIR, "tableau", "Electric_Vehicle_Market_Performance.twb")
TWBX_PATH = os.path.join(BASE_DIR, "tableau", "Electric_Vehicle_Market_Performance.twbx")

def load_data():
    """Helper to load cleaned EV market dataset."""
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame()

# ---------------------------------------------------------
# Web Page Routes
# ---------------------------------------------------------

@app.route("/")
def index():
    """Executive Landing Page with high-level KPIs and scenario navigation."""
    df = load_data()
    total_sales = int(df["Annual_Sales_Units"].sum()) if not df.empty else 0
    total_rev_b = round(df["Sales_Revenue_USD"].sum() / 1e9, 2) if not df.empty else 0
    avg_range = round(df["Driving_Range_km"].mean(), 1) if not df.empty else 0
    avg_rating = round(df["Customer_Rating"].mean(), 2) if not df.empty else 0
    total_co2_m = round(df["Carbon_Offset_Tons"].sum() / 1e6, 2) if not df.empty else 0

    kpis = {
        "total_sales": f"{total_sales:,}",
        "total_revenue_b": f"${total_rev_b}B",
        "avg_range_km": f"{avg_range} km",
        "avg_rating": f"{avg_rating} / 5.0",
        "total_co2_m": f"{total_co2_m}M Tons"
    }
    return render_template("index.html", kpis=kpis, active_page="home")

@app.route("/strategy")
def strategy():
    """Scenario 1: Emily Johnson - EV Market Strategy Director."""
    return render_template("dashboard_strategy.html", active_page="strategy")

@app.route("/bi")
def bi():
    """Scenario 2: David Chen - Automotive Business Intelligence Manager."""
    return render_template("dashboard_bi.html", active_page="bi")

@app.route("/research")
def research():
    """Scenario 3: Dr. Sarah Williams - Sustainable Mobility Research Analyst."""
    return render_template("dashboard_research.html", active_page="research")

@app.route("/story")
def story():
    """Epic 5: Tableau Story Mode - Guided 5-Step Market Transformation Narrative."""
    return render_template("tableau_story.html", active_page="story")

@app.route("/explorer")
def explorer():
    """Interactive Data Explorer table with multi-filter and CSV export."""
    return render_template("data_explorer.html", active_page="explorer")

@app.route("/performance")
def performance():
    """Epic 6: Live Performance Testing Results & Technical Benchmarks."""
    perf_data = {}
    if os.path.exists(PERF_JSON_PATH):
        with open(PERF_JSON_PATH, "r", encoding="utf-8") as f:
            perf_data = json.load(f)
    return render_template("performance.html", perf=perf_data, active_page="performance")

# ---------------------------------------------------------
# REST API Endpoints for Interactive Visualizations
# ---------------------------------------------------------

@app.route("/api/stats")
def api_stats():
    """Provides dynamic filtered summary KPI metrics."""
    df = load_data()
    year = request.args.get("year")
    category = request.args.get("category")
    region = request.args.get("region")

    if year and year != "all":
        df = df[df["Model_Year"] == int(year)]
    if category and category != "all":
        df = df[df["Vehicle_Category"] == category]
    if region and region != "all":
        df = df[df["Production_Region"] == region]

    if df.empty:
        return jsonify({"sales": 0, "revenue": 0, "range": 0, "rating": 0})

    return jsonify({
        "sales": int(df["Annual_Sales_Units"].sum()),
        "revenue_usd": round(float(df["Sales_Revenue_USD"].sum()), 2),
        "avg_range_km": round(float(df["Driving_Range_km"].mean()), 1),
        "avg_rating": round(float(df["Customer_Rating"].mean()), 2),
        "total_co2_tons": int(df["Carbon_Offset_Tons"].sum()),
        "top_maker": df.groupby("Make")["Annual_Sales_Units"].sum().idxmax(),
        "record_count": len(df)
    })

@app.route("/api/charts/category-sales")
def api_category_sales():
    """Aggregates sales units and revenue by vehicle category."""
    df = load_data()
    year = request.args.get("year")
    if year and year != "all":
        df = df[df["Model_Year"] == int(year)]

    grouped = df.groupby("Vehicle_Category").agg(
        total_sales=("Annual_Sales_Units", "sum"),
        total_revenue=("Sales_Revenue_USD", "sum")
    ).reset_index()

    return jsonify({
        "categories": grouped["Vehicle_Category"].tolist(),
        "sales": grouped["total_sales"].tolist(),
        "revenue": (grouped["total_revenue"] / 1e9).round(2).tolist()
    })

@app.route("/api/charts/battery-distribution")
def api_battery_distribution():
    """Aggregates sales volume share by battery technology."""
    df = load_data()
    year = request.args.get("year")
    if year and year != "all":
        df = df[df["Model_Year"] == int(year)]

    grouped = df.groupby("Battery_Technology")["Annual_Sales_Units"].sum().reset_index()
    return jsonify({
        "chemistries": grouped["Battery_Technology"].tolist(),
        "sales": grouped["Annual_Sales_Units"].tolist()
    })

@app.route("/api/charts/oem-leaderboard")
def api_oem_leaderboard():
    """Returns top manufacturers by sales and average satisfaction."""
    df = load_data()
    year = request.args.get("year")
    if year and year != "all":
        df = df[df["Model_Year"] == int(year)]

    grouped = df.groupby("Make").agg(
        total_sales=("Annual_Sales_Units", "sum"),
        avg_rating=("Customer_Rating", "mean"),
        total_revenue=("Sales_Revenue_USD", "sum")
    ).sort_values("total_sales", ascending=False).head(10).reset_index()

    return jsonify({
        "makes": grouped["Make"].tolist(),
        "sales": grouped["total_sales"].tolist(),
        "ratings": grouped["avg_rating"].round(2).tolist(),
        "revenue_billions": (grouped["total_revenue"] / 1e9).round(2).tolist()
    })

@app.route("/api/charts/range-capacity-scatter")
def api_range_capacity():
    """Provides scatter plot points of Driving Range vs. Battery Capacity."""
    df = load_data()
    year = request.args.get("year")
    if year and year != "all":
        df = df[df["Model_Year"] == int(year)]

    points = []
    for _, row in df.iterrows():
        points.append({
            "x": float(row["Battery_Capacity_kWh"]),
            "y": int(row["Driving_Range_km"]),
            "model": f"{row['Make']} {row['Model_Variant']}",
            "tech": row["Battery_Technology"],
            "category": row["Vehicle_Category"],
            "price": int(row["Base_Price_USD"])
        })
    return jsonify(points)

@app.route("/api/charts/yearly-trajectory")
def api_yearly_trajectory():
    """Returns annual sales growth trajectory across 2019-2025 by category."""
    df = load_data()
    pivot = df.pivot_table(
        index="Model_Year",
        columns="Vehicle_Category",
        values="Annual_Sales_Units",
        aggfunc="sum",
        fill_value=0
    )
    years = [int(y) for y in pivot.index.tolist()]
    series = {}
    for col in pivot.columns:
        series[col] = [int(v) for v in pivot[col].tolist()]

    return jsonify({
        "years": years,
        "categories": series
    })

@app.route("/api/charts/country-production")
def api_country_production():
    """Returns manufacturing country volume analysis."""
    df = load_data()
    grouped = df.groupby("Manufacturing_Country").agg(
        total_units=("Annual_Sales_Units", "sum"),
        revenue=("Sales_Revenue_USD", "sum")
    ).sort_values("total_units", ascending=False).reset_index()

    return jsonify({
        "countries": grouped["Manufacturing_Country"].tolist(),
        "units": grouped["total_units"].tolist(),
        "revenue_b": (grouped["revenue"] / 1e9).round(2).tolist()
    })

@app.route("/api/records")
def api_records():
    """Returns paginated or filtered raw records for data explorer."""
    df = load_data()
    limit = int(request.args.get("limit", 100))
    search = request.args.get("search", "").lower()

    if search:
        mask = (
            df["Make"].str.lower().str.contains(search) |
            df["Model"].str.lower().str.contains(search) |
            df["Vehicle_Category"].str.lower().str.contains(search) |
            df["Battery_Technology"].str.lower().str.contains(search) |
            df["Manufacturing_Country"].str.lower().str.contains(search)
        )
        df = df[mask]

    records = df.head(limit).to_dict(orient="records")
    return jsonify({"total_count": len(df), "records": records})

# ---------------------------------------------------------
# Deliverables Download Routes
# ---------------------------------------------------------

@app.route("/download/csv")
def download_csv():
    """Direct download of cleaned dataset."""
    return send_file(DATA_PATH, as_attachment=True, download_name="EV_Market_Performance_Cleaned.csv")

@app.route("/download/twb")
def download_twb():
    """Direct download of Tableau Workbook (.twb)."""
    return send_file(TWB_PATH, as_attachment=True, download_name="Electric_Vehicle_Market_Performance.twb")

@app.route("/download/twbx")
def download_twbx():
    """Direct download of Tableau Packaged Workbook (.twbx)."""
    return send_file(TWBX_PATH, as_attachment=True, download_name="Electric_Vehicle_Market_Performance.twbx")

if __name__ == "__main__":
    print("Starting Electric Vehicle Market Performance Web Application on http://127.0.0.1:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=False)

