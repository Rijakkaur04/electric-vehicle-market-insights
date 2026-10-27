# Technical Architecture & System Workflow

## 1. End-to-End System Architecture

The **Electric Vehicle Market Performance & Insights** analytics platform follows a multi-tier decoupled architecture comprising data ingestion, warehousing, business intelligence modeling, and web presentation layers.

```
+-----------------------------------------------------------------------------------+
|                            DATA COLLECTION & EXTRACTION                           |
|  - Multi-OEM Vehicle Registries (US DOE, EEA, Vahan, Open Data Repositories)      |
|  - Battery Electrochemical Specifications (Wh/kg, Cathode Chemistry, Degradation)  |
|  - Raw CSV Extraction: EV_Market_Data_Raw.csv                                     |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                        DATA PREPARATION & FEATURE PIPELINE                        |
|  - Automated Cleansing & Outlier Resolution (Python 3.14 + Pandas Engine)        |
|  - Feature Engineering: Range Efficiency (km/kWh), Price per km, CSI Segments     |
|  - SQL Data Warehouse Ingestion: fact_ev_market_performance + Dim Views           |
|  - Cleaned Relational Data: EV_Market_Performance_Cleaned.csv                     |
+-----------------------------------------------------------------------------------+
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
+-------------------------------------+         +-------------------------------------+
|      TABLEAU VISUAL ENGINE          |         |       FLASK WEB INTEGRATION         |
|  - Worksheets (9 Core Visuals)      |         |  - Flask 3.1 REST APIs              |
|  - Dashboards (3 Persona Portals)   |         |  - Dynamic Filter Query Engine      |
|  - Tableau Story (5 Guided Points)  |         |  - Interactive Chart.js Visuals     |
|  - LOD Calculations & Hyper Extract |         |  - Live Data Explorer & CSV Export  |
|  - File: .twb & .twbx Archives      |         |  - Automated Benchmark Engine       |
+-------------------------------------+         +-------------------------------------+
                  │                                               │
                  └───────────────────────┬───────────────────────┘
                                          ▼
+-----------------------------------------------------------------------------------+
|                             STAKEHOLDER INTERFACES                                |
|  - Scenario 1: Emily Johnson (Market Strategy Director - Portfolio Planning)      |
|  - Scenario 2: David Chen (Automotive BI Manager - Competitive Benchmarking)       |
|  - Scenario 3: Dr. Sarah Williams (Sustainable Mobility Researcher - Clean Tech)  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Data Warehouse Star Schema

The analytical warehouse organizes vehicle specifications and performance metrics into an optimized Star Schema design:

```
                  ┌────────────────────────┐
                  |    dim_manufacturer    |
                  +------------------------+
                  | PK  make_id            |
                  |     make_name          |
                  |     headquarters_co    |
                  |     production_region  |
                  +────────────────────────+
                              │ 1
                              │
                              │ N
+────────────────────────+    │    +────────────────────────+
|   dim_vehicle_category |    │    |    dim_battery_tech    |
+────────────────────────+    │    +────────────────────────+
| PK  category_id        |──┐ │ ┌──| PK  tech_id            |
|     category_name      |  │ │ │  |     tech_code          |
|     target_segment     |  │ │ │  |     tech_name          |
+────────────────────────+  │ │ │  |     energy_density     |
                            │ │ │  |     cathode_chemistry  |
                            ▼ ▼ ▼  +────────────────────────+
                  +─────────────────────────────────────+
                  |    fact_ev_market_performance       |
                  +─────────────────────────────────────+
                  | PK  record_id                       |
                  | FK  model_year                      |
                  | FK  make                            |
                  |     model                           |
                  |     model_variant                   |
                  | FK  vehicle_category                |
                  | FK  battery_technology              |
                  |     battery_capacity_kwh            |
                  |     driving_range_km                |
                  |     base_price_usd                  |
                  |     fast_charge_time_mins           |
                  |     annual_sales_units              |
                  |     sales_revenue_usd               |
                  |     customer_rating                 |
                  |     carbon_offset_tons              |
                  |     manufacturing_country           |
                  |     range_efficiency_km_kwh         |
                  |     price_per_km_usd                |
                  |     market_share_pct                |
                  +─────────────────────────────────────+
```

---

## 3. Persona Analytical Workflows

### 3.1 Scenario 1: Emily Johnson (EV Market Strategy Director)
1. **Macro Sizing:** Consults the Executive Strategy Dashboard to identify total sales contributions by vehicle category.
2. **Segment Leadership:** Analyzes SUV and Sedan dominant revenue generators to prioritize next-generation model redesigns.
3. **Consumer Sentiment:** Evaluates customer ratings across categories to address vehicle-specific satisfaction bottlenecks.
4. **Action:** Allocates R&D capital towards mid-market SUVs powered by cost-efficient LFP cells.

### 3.2 Scenario 2: David Chen (Automotive BI Manager)
1. **Market Share Monitoring:** Tracks competitive OEM rankings, noting BYD and Tesla's consolidated global share.
2. **Supply Chain Footprint:** Investigates manufacturing country distributions to identify tariffs and geographical logistics vulnerabilities.
3. **Affordability vs Range:** Examines the Price-to-Range matrix to benchmark client vehicle offerings against market price frontiers.
4. **Action:** Delivers strategic entry blueprints advising clients to co-locate Gigafactories in target consumer regions.

### 3.3 Scenario 3: Dr. Sarah Williams (Sustainable Mobility Researcher)
1. **Chemistry Evaluation:** Analyzes the empirical trade-offs among LFP, NMC, NCA, Solid-State, and Sodium-Ion cells.
2. **Range vs Capacity Efficiency:** Studies scatter plot regressions comparing battery pack size to effective driving range.
3. **Decarbonization ROI:** Calculates lifecycle carbon offset across private passenger cars vs municipal transit buses.
4. **Action:** Publishes clean transportation policy briefs highlighting commercial fleet electrification as the highest ROI carbon mitigation strategy.

