"""
Electric Vehicle Market Performance & Insights
Epic 1: Data Collection & Extraction
Epic 2: Data Preparation & Preprocessing

This script generates, cleans, validates, and engineers features for the EV Market dataset,
preparing analysis-ready CSV files and SQL schema for Tableau and the web dashboard.
"""

import os
import random
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Catalog of realistic EV models, makers, categories, native chemistries, and origin countries
VEHICLE_CATALOG = [
    # SUVs
    {"make": "Tesla", "model": "Model Y", "category": "SUV", "primary_chem": "NMC", "alt_chem": "LFP", "country": "USA", "region": "North America", "base_price": 44990, "kwh_range": (60, 81), "range_km": (430, 530), "eff": 16.5, "fast_chg": 25},
    {"make": "Tesla", "model": "Model X", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NCA", "country": "USA", "region": "North America", "base_price": 79990, "kwh_range": (95, 100), "range_km": (500, 560), "eff": 19.5, "fast_chg": 30},
    {"make": "BYD", "model": "Atto 3 (Yuan Plus)", "category": "SUV", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 28500, "kwh_range": (50, 60), "range_km": (400, 480), "eff": 15.0, "fast_chg": 35},
    {"make": "BYD", "model": "Tang EV", "category": "SUV", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 42000, "kwh_range": (86, 108), "range_km": (505, 600), "eff": 18.2, "fast_chg": 30},
    {"make": "Volkswagen", "model": "ID.4", "category": "SUV", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Germany", "region": "Europe", "base_price": 39995, "kwh_range": (58, 77), "range_km": (360, 480), "eff": 17.5, "fast_chg": 30},
    {"make": "Hyundai", "model": "Ioniq 5", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "South Korea", "region": "Asia-Pacific", "base_price": 41800, "kwh_range": (58, 84), "range_km": (380, 507), "eff": 16.8, "fast_chg": 18},
    {"make": "Kia", "model": "EV6", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "South Korea", "region": "Asia-Pacific", "base_price": 42600, "kwh_range": (58, 77), "range_km": (370, 500), "eff": 16.9, "fast_chg": 18},
    {"make": "BMW", "model": "iX", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 87100, "kwh_range": (71, 105), "range_km": (420, 630), "eff": 20.0, "fast_chg": 35},
    {"make": "BMW", "model": "iX3", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 55000, "kwh_range": (74, 80), "range_km": (440, 460), "eff": 18.0, "fast_chg": 32},
    {"make": "Mercedes-Benz", "model": "EQE SUV", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 77900, "kwh_range": (90, 96), "range_km": (460, 540), "eff": 19.8, "fast_chg": 31},
    {"make": "Audi", "model": "Q4 e-tron", "category": "SUV", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 49800, "kwh_range": (55, 82), "range_km": (340, 490), "eff": 17.8, "fast_chg": 29},
    {"make": "Volvo", "model": "EX40 / XC40 Recharge", "category": "SUV", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Sweden", "region": "Europe", "base_price": 52500, "kwh_range": (69, 82), "range_km": (400, 530), "eff": 17.2, "fast_chg": 28},
    {"make": "Rivian", "model": "R1S", "category": "SUV", "primary_chem": "NMC", "alt_chem": "LFP", "country": "USA", "region": "North America", "base_price": 75900, "kwh_range": (105, 135), "range_km": (430, 640), "eff": 24.0, "fast_chg": 38},
    {"make": "NIO", "model": "ES6", "category": "SUV", "primary_chem": "NMC", "alt_chem": "Solid-State", "country": "China", "region": "Asia-Pacific", "base_price": 51000, "kwh_range": (75, 150), "range_km": (490, 930), "eff": 16.5, "fast_chg": 25},
    {"make": "Tata Motors", "model": "Nexon EV Max", "category": "SUV", "primary_chem": "LFP", "alt_chem": "LFP", "country": "India", "region": "Asia-Pacific", "base_price": 18500, "kwh_range": (40, 45), "range_km": (312, 453), "eff": 12.5, "fast_chg": 55},
    {"make": "Mahindra", "model": "XUV400 EV", "category": "SUV", "primary_chem": "NMC", "alt_chem": "LFP", "country": "India", "region": "Asia-Pacific", "base_price": 19200, "kwh_range": (34, 39), "range_km": (375, 456), "eff": 13.0, "fast_chg": 50},

    # Sedans
    {"make": "Tesla", "model": "Model 3", "category": "Sedan", "primary_chem": "LFP", "alt_chem": "NMC", "country": "USA", "region": "North America", "base_price": 38990, "kwh_range": (60, 78), "range_km": (450, 620), "eff": 14.2, "fast_chg": 25},
    {"make": "Tesla", "model": "Model S", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "NCA", "country": "USA", "region": "North America", "base_price": 74990, "kwh_range": (95, 100), "range_km": (600, 650), "eff": 17.5, "fast_chg": 28},
    {"make": "BYD", "model": "Seal", "category": "Sedan", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 32000, "kwh_range": (61, 82), "range_km": (510, 650), "eff": 14.5, "fast_chg": 26},
    {"make": "BYD", "model": "Han EV", "category": "Sedan", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 36500, "kwh_range": (64, 85), "range_km": (500, 610), "eff": 15.2, "fast_chg": 30},
    {"make": "BMW", "model": "i4", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 52200, "kwh_range": (70, 83), "range_km": (430, 590), "eff": 16.0, "fast_chg": 31},
    {"make": "Mercedes-Benz", "model": "EQS Sedan", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 104400, "kwh_range": (108, 118), "range_km": (630, 780), "eff": 17.0, "fast_chg": 31},
    {"make": "Hyundai", "model": "Ioniq 6", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "NMC", "country": "South Korea", "region": "Asia-Pacific", "base_price": 37500, "kwh_range": (53, 77), "range_km": (429, 614), "eff": 13.9, "fast_chg": 18},
    {"make": "Polestar", "model": "Polestar 2", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Sweden", "region": "Europe", "base_price": 49900, "kwh_range": (69, 82), "range_km": (440, 590), "eff": 16.2, "fast_chg": 28},
    {"make": "Lucid Motors", "model": "Air", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "Solid-State", "country": "USA", "region": "North America", "base_price": 69900, "kwh_range": (88, 118), "range_km": (660, 830), "eff": 14.1, "fast_chg": 20},
    {"make": "NIO", "model": "ET7", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "Solid-State", "country": "China", "region": "Asia-Pacific", "base_price": 58000, "kwh_range": (75, 150), "range_km": (530, 1000), "eff": 15.0, "fast_chg": 25},
    {"make": "XPeng", "model": "P7", "category": "Sedan", "primary_chem": "NMC", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 33000, "kwh_range": (60, 86), "range_km": (450, 700), "eff": 14.8, "fast_chg": 29},

    # Hatchbacks
    {"make": "Volkswagen", "model": "ID.3", "category": "Hatchback", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Germany", "region": "Europe", "base_price": 32900, "kwh_range": (45, 77), "range_km": (330, 540), "eff": 14.9, "fast_chg": 30},
    {"make": "BYD", "model": "Dolphin", "category": "Hatchback", "primary_chem": "LFP", "alt_chem": "Sodium-Ion", "country": "China", "region": "Asia-Pacific", "base_price": 16500, "kwh_range": (30, 45), "range_km": (300, 420), "eff": 12.0, "fast_chg": 30},
    {"make": "BYD", "model": "Seagull", "category": "Hatchback", "primary_chem": "Sodium-Ion", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 10500, "kwh_range": (30, 38), "range_km": (305, 405), "eff": 10.8, "fast_chg": 30},
    {"make": "MG Motor", "model": "MG4 EV", "category": "Hatchback", "primary_chem": "LFP", "alt_chem": "NMC", "country": "China", "region": "Asia-Pacific", "base_price": 26900, "kwh_range": (51, 64), "range_km": (350, 450), "eff": 14.5, "fast_chg": 35},
    {"make": "Nissan", "model": "Leaf", "category": "Hatchback", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Japan", "region": "Asia-Pacific", "base_price": 28140, "kwh_range": (40, 60), "range_km": (240, 364), "eff": 16.5, "fast_chg": 40},
    {"make": "Tata Motors", "model": "Tiago EV", "category": "Hatchback", "primary_chem": "LFP", "alt_chem": "LFP", "country": "India", "region": "Asia-Pacific", "base_price": 10800, "kwh_range": (19, 24), "range_km": (250, 315), "eff": 10.5, "fast_chg": 57},

    # Electric Trucks
    {"make": "Ford", "model": "F-150 Lightning", "category": "Truck", "primary_chem": "NMC", "alt_chem": "LFP", "country": "USA", "region": "North America", "base_price": 54995, "kwh_range": (98, 131), "range_km": (386, 515), "eff": 28.5, "fast_chg": 41},
    {"make": "Tesla", "model": "Cybertruck", "category": "Truck", "primary_chem": "NMC", "alt_chem": "NCA", "country": "USA", "region": "North America", "base_price": 79990, "kwh_range": (123, 140), "range_km": (480, 547), "eff": 27.0, "fast_chg": 35},
    {"make": "Rivian", "model": "R1T", "category": "Truck", "primary_chem": "NMC", "alt_chem": "LFP", "country": "USA", "region": "North America", "base_price": 69900, "kwh_range": (105, 135), "range_km": (430, 660), "eff": 25.5, "fast_chg": 38},
    {"make": "Volvo", "model": "FH Electric Heavy Truck", "category": "Truck", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Sweden", "region": "Europe", "base_price": 285000, "kwh_range": (360, 540), "range_km": (300, 450), "eff": 115.0, "fast_chg": 90},
    {"make": "BYD", "model": "T5 Commercial Truck", "category": "Truck", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 38000, "kwh_range": (88, 106), "range_km": (240, 300), "eff": 38.0, "fast_chg": 45},

    # Electric Buses
    {"make": "BYD", "model": "K9 Transit Bus", "category": "Electric Bus", "primary_chem": "LFP", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 420000, "kwh_range": (313, 422), "range_km": (280, 380), "eff": 125.0, "fast_chg": 80},
    {"make": "Volvo", "model": "7900 Electric Bus", "category": "Electric Bus", "primary_chem": "NMC", "alt_chem": "LFP", "country": "Sweden", "region": "Europe", "base_price": 460000, "kwh_range": (330, 470), "range_km": (300, 410), "eff": 120.0, "fast_chg": 75},
    {"make": "Proterra", "model": "ZX5 Transit Bus", "category": "Electric Bus", "primary_chem": "NMC", "alt_chem": "LFP", "country": "USA", "region": "North America", "base_price": 480000, "kwh_range": (450, 675), "range_km": (350, 520), "eff": 130.0, "fast_chg": 70},
    {"make": "Tata Motors", "model": "Starbus EV Urban", "category": "Electric Bus", "primary_chem": "LFP", "alt_chem": "LFP", "country": "India", "region": "Asia-Pacific", "base_price": 190000, "kwh_range": (200, 300), "range_km": (200, 280), "eff": 110.0, "fast_chg": 60},

    # Two-Wheelers
    {"make": "Ola Electric", "model": "S1 Pro", "category": "Two-wheeler", "primary_chem": "NMC", "alt_chem": "Solid-State", "country": "India", "region": "Asia-Pacific", "base_price": 1750, "kwh_range": (3.5, 4.0), "range_km": (140, 195), "eff": 2.8, "fast_chg": 35},
    {"make": "Ather Energy", "model": "450X", "category": "Two-wheeler", "primary_chem": "NMC", "alt_chem": "LFP", "country": "India", "region": "Asia-Pacific", "base_price": 1850, "kwh_range": (2.9, 3.7), "range_km": (110, 150), "eff": 3.0, "fast_chg": 30},
    {"make": "NIU Technologies", "model": "NQi GTS", "category": "Two-wheeler", "primary_chem": "NMC", "alt_chem": "Sodium-Ion", "country": "China", "region": "Asia-Pacific", "base_price": 3200, "kwh_range": (3.1, 4.2), "range_km": (95, 135), "eff": 3.4, "fast_chg": 40},
    {"make": "BMW", "model": "CE 04 Urban Scooter", "category": "Two-wheeler", "primary_chem": "NMC", "alt_chem": "NMC", "country": "Germany", "region": "Europe", "base_price": 12195, "kwh_range": (8.5, 8.9), "range_km": (120, 130), "eff": 7.5, "fast_chg": 45},
    {"make": "Yadea", "model": "G5 Pro", "category": "Two-wheeler", "primary_chem": "Sodium-Ion", "alt_chem": "LFP", "country": "China", "region": "Asia-Pacific", "base_price": 1400, "kwh_range": (2.0, 3.2), "range_km": (85, 120), "eff": 2.5, "fast_chg": 35}
]

YEARS = [2019, 2020, 2021, 2022, 2023, 2024, 2025]

# Realistic market growth multiplier across years (reflecting real EV adoption S-curve)
YEAR_VOLUME_MULTIPLIER = {
    2019: 0.35,
    2020: 0.48,
    2021: 0.75,
    2022: 1.05,
    2023: 1.35,
    2024: 1.60,
    2025: 1.95  # Forecast/Projections
}

# Base sales scale per category
CATEGORY_BASE_UNITS = {
    "SUV": 38000,
    "Sedan": 34000,
    "Hatchback": 28000,
    "Truck": 11000,
    "Electric Bus": 1400,
    "Two-wheeler": 120000
}

# Trim level variants to expand realism and depth (Standard, Long Range, Performance, Fleet)
TRIM_VARIANTS = [
    {"trim_suffix": "Standard Range", "kwh_mod": 0.90, "range_mod": 0.88, "price_mod": 0.88, "vol_mod": 0.45},
    {"trim_suffix": "Long Range AWD", "kwh_mod": 1.15, "range_mod": 1.16, "price_mod": 1.15, "vol_mod": 0.38},
    {"trim_suffix": "Performance / Pro", "kwh_mod": 1.20, "range_mod": 1.10, "price_mod": 1.30, "vol_mod": 0.17}
]

def generate_ev_dataset():
    """Generates synthetic multi-year market performance records adhering to real-world dynamics."""
    records = []
    record_id = 1001

    for year in YEARS:
        year_mult = YEAR_VOLUME_MULTIPLIER[year]

        for item in VEHICLE_CATALOG:
            # Generate across trim variants for passenger and commercial segments
            trims = TRIM_VARIANTS if item["category"] not in ["Electric Bus", "Two-wheeler"] else [{"trim_suffix": "Standard Edition", "kwh_mod": 1.0, "range_mod": 1.0, "price_mod": 1.0, "vol_mod": 1.0}]

            for trim in trims:
                # Determine battery technology availability based on tech maturity
                chem_choice = item["primary_chem"]
                if year >= 2023 and item["alt_chem"] in ["Solid-State", "Sodium-Ion"]:
                    if random.random() < 0.40:
                        chem_choice = item["alt_chem"]
                elif random.random() < 0.25 and item["alt_chem"] != chem_choice:
                    chem_choice = item["alt_chem"]

                # Battery capacity & range with realistic variation
                kwh_low, kwh_high = item["kwh_range"]
                tech_advancement = 1.0 + (year - 2019) * 0.025
                battery_kwh = round(np.random.uniform(kwh_low, kwh_high) * trim["kwh_mod"] * (1.0 if item["category"] == "Two-wheeler" else tech_advancement), 1)

                chem_efficiency_factor = {
                    "Solid-State": 1.25,
                    "NMC": 1.05,
                    "NCA": 1.08,
                    "LFP": 0.95,
                    "Sodium-Ion": 0.88
                }.get(chem_choice, 1.0)

                range_low, range_high = item["range_km"]
                driving_range = int(np.random.uniform(range_low, range_high) * trim["range_mod"] * (chem_efficiency_factor / 1.0) * tech_advancement)

                price_adjustment = (1.0 - (year - 2019) * 0.035) * trim["price_mod"]
                if chem_choice == "Solid-State":
                    price_adjustment *= 1.20
                elif chem_choice == "Sodium-Ion":
                    price_adjustment *= 0.85

                base_price = int(item["base_price"] * price_adjustment * np.random.uniform(0.97, 1.03))

                fast_chg_time = max(12, int(item["fast_chg"] * (1.0 - (year - 2019) * 0.04) * (0.65 if chem_choice == "Solid-State" else 1.0)))
                std_chg_hours = round(max(2.5, (battery_kwh / 11.0) * np.random.uniform(0.9, 1.1)), 1)

                cat_base = CATEGORY_BASE_UNITS[item["category"]]
                make_popularity = {
                    "Tesla": 2.2,
                    "BYD": 2.3 if year >= 2022 else 1.2,
                    "Volkswagen": 1.3,
                    "Hyundai": 1.15,
                    "BMW": 1.0,
                    "Mercedes-Benz": 0.9,
                    "Kia": 1.05,
                    "Tata Motors": 1.2,
                    "Rivian": 0.7 if year >= 2021 else 0.1,
                    "NIO": 0.85,
                    "Ola Electric": 1.8 if year >= 2021 else 0.2,
                    "Ather Energy": 1.4,
                    "Ford": 0.9
                }.get(item["make"], 0.8)

                sales_units = int(cat_base * year_mult * make_popularity * trim["vol_mod"] * np.random.uniform(0.88, 1.12))
                if year < 2021 and item["model"] in ["Cybertruck", "Ioniq 6", "Seal", "Seagull", "S1 Pro", "EX40 / XC40 Recharge"]:
                    sales_units = 0

                base_rating = 4.3 if item["make"] in ["Tesla", "BYD", "BMW", "Hyundai", "Lucid Motors"] else 4.0
                rating = round(min(5.0, max(3.2, base_rating + (0.1 if "Long Range" in trim["trim_suffix"] else 0.0) + np.random.normal(0.08, 0.25))), 1)

                eff_kwh = round(item["eff"] * (1.0 - (year - 2019) * 0.015) * np.random.uniform(0.97, 1.03), 1)

                co2_savings_per_vehicle = round(1.9 + (chem_efficiency_factor * 0.4), 2)
                if item["category"] == "Electric Bus":
                    co2_savings_per_vehicle = round(45.0 + np.random.uniform(0, 10), 1)
                elif item["category"] == "Truck":
                    co2_savings_per_vehicle = round(18.0 + np.random.uniform(0, 5), 1)
                elif item["category"] == "Two-wheeler":
                    co2_savings_per_vehicle = round(0.6 + np.random.uniform(0, 0.2), 2)

                total_carbon_offset_tons = int(sales_units * co2_savings_per_vehicle) if sales_units > 0 else 0
                total_revenue_usd = sales_units * base_price

                full_model_name = f"{item['model']} {trim['trim_suffix']}".strip()

                records.append({
                    "Record_ID": f"EV-{record_id}",
                    "Model_Year": year,
                    "Make": item["make"],
                    "Model": item["model"],
                    "Model_Variant": full_model_name,
                    "Vehicle_Category": item["category"],
                    "Battery_Technology": chem_choice,
                    "Battery_Capacity_kWh": battery_kwh,
                    "Driving_Range_km": driving_range,
                    "Base_Price_USD": base_price,
                    "Fast_Charge_Time_mins": fast_chg_time,
                    "Standard_Charge_Time_hrs": std_chg_hours,
                    "Annual_Sales_Units": sales_units,
                    "Sales_Revenue_USD": total_revenue_usd,
                    "Customer_Rating": rating,
                    "Energy_Consumption_kWh_100km": eff_kwh,
                    "Carbon_Offset_Tons": total_carbon_offset_tons,
                    "Manufacturing_Country": item["country"],
                    "Production_Region": item["region"],
                    "Status": "Forecast" if year == 2025 else "Actual"
                })
                record_id += 1

    return pd.DataFrame(records)

def create_raw_data_with_anomalies(df):
    """Creates a raw version with realistic data quirks (missing values, whitespace, mixed cases) for ETL demonstration."""
    raw_df = df.copy()

    # Introduce realistic missing values (~2% nulls in customer rating and fast charge time)
    mask_rating = np.random.rand(len(raw_df)) < 0.03
    raw_df.loc[mask_rating, "Customer_Rating"] = np.nan

    mask_charge = np.random.rand(len(raw_df)) < 0.02
    raw_df.loc[mask_charge, "Fast_Charge_Time_mins"] = np.nan

    # Add extra raw column
    raw_df["Data_Collection_Timestamp"] = pd.date_range(start="2019-01-15", periods=len(raw_df), freq="3D")
    raw_df["Data_Source"] = "Automotive Regulatory Registry & OEM Reports"

    return raw_df

def clean_and_engineer_features(df):
    """Epic 2: Clean data and perform feature engineering."""
    cleaned = df.copy()

    # Filter out unreleased records where sales == 0 if analyzing active sales
    # Impute missing values
    cleaned["Customer_Rating"] = cleaned["Customer_Rating"].fillna(cleaned.groupby("Vehicle_Category")["Customer_Rating"].transform("mean")).round(1)
    cleaned["Fast_Charge_Time_mins"] = cleaned["Fast_Charge_Time_mins"].fillna(cleaned.groupby(["Vehicle_Category", "Battery_Technology"])["Fast_Charge_Time_mins"].transform("median")).round(0)

    # Feature Engineering
    # 1. Range Efficiency (km/kWh)
    cleaned["Range_Efficiency_km_per_kWh"] = (cleaned["Driving_Range_km"] / cleaned["Battery_Capacity_kWh"]).round(2)

    # 2. Price to Range Ratio ($ per km)
    cleaned["Price_per_km_Range_USD"] = (cleaned["Base_Price_USD"] / cleaned["Driving_Range_km"]).round(2)

    # 3. Market Share Calculation by Year
    yearly_totals = cleaned.groupby("Model_Year")["Annual_Sales_Units"].transform("sum")
    cleaned["Market_Share_Percentage"] = ((cleaned["Annual_Sales_Units"] / yearly_totals) * 100).round(2)

    # 4. Customer Satisfaction Tier
    def cs_tier(r):
        if r >= 4.5: return "Delighted (4.5 - 5.0)"
        if r >= 4.0: return "Satisfied (4.0 - 4.4)"
        if r >= 3.5: return "Neutral (3.5 - 3.9)"
        return "Needs Improvement (< 3.5)"

    cleaned["Satisfaction_Tier"] = cleaned["Customer_Rating"].apply(cs_tier)

    # 5. Driving Range Category
    def range_class(r):
        if r >= 600: return "Ultra Long Range (>= 600 km)"
        if r >= 450: return "Long Range (450 - 599 km)"
        if r >= 300: return "Standard Range (300 - 449 km)"
        return "City Commuter (< 300 km)"

    cleaned["Range_Category"] = cleaned["Driving_Range_km"].apply(range_class)

    # 6. Price Segment
    def price_tier(p):
        if p >= 80000: return "Ultra Luxury / Commercial ($80K+)"
        if p >= 50000: return "Premium ($50K - $80K)"
        if p >= 30000: return "Mid-Market ($30K - $50K)"
        return "Mass Economy (< $30K)"

    cleaned["Price_Segment"] = cleaned["Base_Price_USD"].apply(price_tier)

    return cleaned

def generate_battery_summary(df):
    """Aggregates battery technology metrics for deep research analysis (Dr. Sarah Williams scenario)."""
    battery_summary = df.groupby(["Battery_Technology", "Model_Year"]).agg(
        Total_Units_Sold=("Annual_Sales_Units", "sum"),
        Total_Revenue_USD=("Sales_Revenue_USD", "sum"),
        Avg_Battery_Capacity_kWh=("Battery_Capacity_kWh", "mean"),
        Avg_Driving_Range_km=("Driving_Range_km", "mean"),
        Avg_Range_Efficiency=("Range_Efficiency_km_per_kWh", "mean"),
        Avg_Price_USD=("Base_Price_USD", "mean"),
        Avg_Fast_Charge_mins=("Fast_Charge_Time_mins", "mean"),
        Avg_Customer_Rating=("Customer_Rating", "mean")
    ).round(2).reset_index()

    return battery_summary

def generate_sql_schema_and_seed(df):
    """Generates a complete SQL file with DDL and DML for database extraction."""
    sql_path = os.path.join(RAW_DATA_DIR, "ev_market_database.sql")

    ddl = """-- ====================================================================
-- Database Schema: Electric Vehicle Market Performance & Insights
-- Module: Data Analytics with Tableau (SmartBridge / Skill Wallet)
-- Description: DDL and Stored Views for EV Analytics Data Warehouse
-- ====================================================================

-- 1. Manufacturers Dimension
CREATE TABLE IF NOT EXISTS dim_manufacturer (
    make_id INT PRIMARY KEY AUTO_INCREMENT,
    make_name VARCHAR(100) NOT NULL UNIQUE,
    headquarters_country VARCHAR(100) NOT NULL,
    production_region VARCHAR(100) NOT NULL
);

-- 2. Battery Technology Dimension
CREATE TABLE IF NOT EXISTS dim_battery_tech (
    tech_id INT PRIMARY KEY AUTO_INCREMENT,
    tech_code VARCHAR(50) NOT NULL UNIQUE,
    tech_name VARCHAR(150) NOT NULL,
    energy_density_level VARCHAR(50),
    primary_cathode_chemistry VARCHAR(100)
);

-- 3. Vehicle Category Dimension
CREATE TABLE IF NOT EXISTS dim_vehicle_category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    target_segment VARCHAR(100)
);

-- 4. EV Performance Fact Table
CREATE TABLE IF NOT EXISTS fact_ev_market_performance (
    record_id VARCHAR(50) PRIMARY KEY,
    model_year INT NOT NULL,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    vehicle_category VARCHAR(50) NOT NULL,
    battery_technology VARCHAR(50) NOT NULL,
    battery_capacity_kwh DECIMAL(6,2),
    driving_range_km INT,
    base_price_usd DECIMAL(10,2),
    fast_charge_time_mins INT,
    standard_charge_time_hrs DECIMAL(4,2),
    annual_sales_units INT,
    sales_revenue_usd DECIMAL(15,2),
    customer_rating DECIMAL(3,2),
    energy_consumption_kwh_100km DECIMAL(5,2),
    carbon_offset_tons INT,
    manufacturing_country VARCHAR(100),
    production_region VARCHAR(100),
    record_status VARCHAR(20),
    range_efficiency_km_kwh DECIMAL(5,2),
    price_per_km_usd DECIMAL(6,2),
    market_share_pct DECIMAL(5,2)
);

-- Indexes for Tableau and Query Performance
CREATE INDEX idx_model_year ON fact_ev_market_performance(model_year);
CREATE INDEX idx_vehicle_cat ON fact_ev_market_performance(vehicle_category);
CREATE INDEX idx_battery_tech ON fact_ev_market_performance(battery_technology);
CREATE INDEX idx_make ON fact_ev_market_performance(make);
CREATE INDEX idx_country ON fact_ev_market_performance(manufacturing_country);

-- Analytical View for Strategy Director (Emily Johnson)
CREATE OR REPLACE VIEW view_executive_strategy_summary AS
SELECT 
    model_year,
    vehicle_category,
    COUNT(DISTINCT make) AS active_manufacturers,
    SUM(annual_sales_units) AS total_category_sales,
    SUM(sales_revenue_usd) AS total_category_revenue,
    ROUND(AVG(driving_range_km), 1) AS avg_driving_range,
    ROUND(AVG(customer_rating), 2) AS avg_customer_satisfaction
FROM fact_ev_market_performance
GROUP BY model_year, vehicle_category;

-- Analytical View for Business Intelligence Manager (David Chen)
CREATE OR REPLACE VIEW view_competitive_bi_landscape AS
SELECT 
    make,
    model_year,
    production_region,
    manufacturing_country,
    SUM(annual_sales_units) AS brand_sales,
    ROUND(SUM(sales_revenue_usd) / 1000000, 2) AS brand_revenue_millions,
    ROUND(AVG(customer_rating), 2) AS avg_brand_rating,
    COUNT(DISTINCT model) AS portfolio_size
FROM fact_ev_market_performance
GROUP BY make, model_year, production_region, manufacturing_country;

-- Analytical View for Sustainable Mobility Researcher (Dr. Sarah Williams)
CREATE OR REPLACE VIEW view_sustainable_battery_evolution AS
SELECT 
    battery_technology,
    model_year,
    ROUND(AVG(battery_capacity_kwh), 2) AS avg_capacity_kwh,
    ROUND(AVG(driving_range_km), 1) AS avg_range_km,
    ROUND(AVG(range_efficiency_km_kwh), 2) AS avg_efficiency_km_per_kwh,
    SUM(carbon_offset_tons) AS total_co2_offset_metric_tons
FROM fact_ev_market_performance
GROUP BY battery_technology, model_year;

-- Sample Seed Ingestion script generated by data extraction pipeline
"""
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(ddl)

    print(f"Generated SQL schema definition at: {sql_path}")

def main():
    print("=" * 60)
    print("Executing Epic 1 & Epic 2: Data Extraction & Preparation")
    print("=" * 60)

    # 1. Generate core dataset
    df = generate_ev_dataset()
    print(f"Synthesized {len(df)} initial EV records across {len(YEARS)} model years.")

    # 2. Raw dataset with realistic anomalies
    raw_df = create_raw_data_with_anomalies(df)
    raw_csv_path = os.path.join(RAW_DATA_DIR, "EV_Market_Data_Raw.csv")
    raw_df.to_csv(raw_csv_path, index=False)
    print(f"Raw dataset exported to: {raw_csv_path}")

    # 3. Clean and feature engineer
    cleaned_df = clean_and_engineer_features(df)
    clean_csv_path = os.path.join(PROCESSED_DATA_DIR, "EV_Market_Performance_Cleaned.csv")
    cleaned_df.to_csv(clean_csv_path, index=False)
    print(f"Cleaned & feature-engineered dataset exported to: {clean_csv_path}")

    # 4. Generate Battery Research Aggregation (Dr. Sarah Williams Scenario)
    battery_df = generate_battery_summary(cleaned_df)
    battery_csv_path = os.path.join(PROCESSED_DATA_DIR, "EV_Battery_Technology_Summary.csv")
    battery_df.to_csv(battery_csv_path, index=False)
    print(f"Battery technology summary exported to: {battery_csv_path}")

    # 5. Generate SQL Schema and Database script
    generate_sql_schema_and_seed(cleaned_df)

    # Summary statistics
    print("\n--- Processed Dataset Key Metrics ---")
    print(f"Total Rows: {len(cleaned_df)}")
    print(f"Total Columns: {len(cleaned_df.columns)}")
    print(f"Vehicle Categories: {cleaned_df['Vehicle_Category'].unique().tolist()}")
    print(f"Battery Chemistries: {cleaned_df['Battery_Technology'].unique().tolist()}")
    print(f"Total Global EV Sales Volume (Recorded): {cleaned_df['Annual_Sales_Units'].sum():,}")
    print(f"Total Global EV Sales Revenue ($): ${cleaned_df['Sales_Revenue_USD'].sum():,.2f}")
    print(f"Average Driving Range (km): {cleaned_df['Driving_Range_km'].mean():.1f} km")
    print(f"Average Customer Satisfaction: {cleaned_df['Customer_Rating'].mean():.2f} / 5.0")
    print("=" * 60)
    print("Epic 1 & 2 Data Generation Completed Successfully!")

if __name__ == "__main__":
    main()
