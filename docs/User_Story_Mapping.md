# Agile User Story Mapping & Task Breakdown
**Project:** Electric Vehicle Market Performance & Insights  
**Program:** Data Analytics with Tableau (SmartBridge / Skill Wallet)  
**Total Epics:** 8 | **Total Tasks:** 14 | **Subtasks:** 0 | **Status:** 100% Completed  

---

## Agile Hierarchy Matrix

```
[EPIC 1: Data Collection & Extraction]
  ├── Task 1.1: Multi-source EV dataset sourcing & extraction (CSV/Registries) [DONE]
  └── Task 1.2: Relational database schema design & SQL staging ingestion [DONE]

[EPIC 2: Data Preparation]
  ├── Task 2.1: Data cleansing, missing value imputation & standardization [DONE]
  └── Task 2.2: Feature engineering & Tableau calculated field derivations [DONE]

[EPIC 3: Data Visualizations]
  ├── Task 3.1: Core analytical worksheets design (Sales, OEMs, Chemistries, Maps) [DONE]
  └── Task 3.2: Advanced analytical worksheets (Range vs Capacity, Efficiency matrix) [DONE]

[EPIC 4: Dashboards Development]
  ├── Task 4.1: Executive Market Strategy Dashboard (Emily Johnson) [DONE]
  └── Task 4.2: Competitive Intelligence & BI Dashboard (David Chen) [DONE]

[EPIC 5: Tableau Story]
  ├── Task 5.1: Structured 5-point narrative story construction [DONE]
  └── Task 5.2: Story formatting, callout annotations & executive takeaways [DONE]

[EPIC 6: Performance Testing]
  └── Task 6.1: Automated query latency, LOD calculation & extract benchmarking [DONE]

[EPIC 7: Web Integration]
  ├── Task 7.1: Responsive Flask web platform & REST API development [DONE]
  └── Task 7.2: Client-side interactive visual charts & Tableau embedding [DONE]

[EPIC 8: Project Demonstration & Documentation]
  ├── Task 8.1: Comprehensive technical project report & documentation [DONE]
  └── Task 8.2: GitHub repository staging, demonstration video guide & links setup [DONE]
```

---

## Detailed Story & Task Specifications

### Epic 1: Data Collection & Extraction
* **Complexity:** Medium | **Estimated Duration:** 5h 0m | **Status:** 100% Complete
* **Task 1.1 — Data Sourcing & Synthesis:**
  * *User Story:* As a Data Analyst, I want to collect and synthesize comprehensive EV market registration and performance metrics across global manufacturers so that multi-dimensional market analysis is possible.
  * *Acceptance Criteria:* Dataset must span 2019-2025, 16+ OEMs, 6 vehicle categories (SUV, Sedan, Hatchback, Truck, Bus, 2-Wheeler), and 5 battery chemistries (LFP, NMC, NCA, Solid-State, Sodium-Ion).
  * *Artifact:* `data/raw/EV_Market_Data_Raw.csv`
* **Task 1.2 — Database Schema Definition:**
  * *User Story:* As a Database Engineer, I want to structure a relational star schema so that analytical queries can be extracted with high efficiency.
  * *Acceptance Criteria:* DDL script creating `dim_manufacturer`, `dim_battery_tech`, `dim_vehicle_category`, and `fact_ev_market_performance` with proper indexes and analytical SQL views.
  * *Artifact:* `data/raw/ev_market_database.sql`

---

### Epic 2: Data Preparation
* **Complexity:** Medium | **Status:** 100% Complete
* **Task 2.1 — Data Cleansing & Validation:**
  * *User Story:* As an Analytics Engineer, I want to validate data integrity, impute missing values, and standardize classifications to ensure zero data anomalies.
  * *Acceptance Criteria:* Zero nulls in core dimensions, validated range bounds, standardized categorizations.
  * *Artifact:* `scripts/data_extraction_and_cleaning.py`, `data/processed/EV_Market_Performance_Cleaned.csv`
* **Task 2.2 — Feature Engineering & Calculated Metrics:**
  * *User Story:* As a BI Specialist, I want to engineer key business metrics including Range Efficiency (`km/kWh`), Price per km Range (`$/km`), Gross Revenue (`$`), Market Share (`%`), and Customer Satisfaction Index tiers.
  * *Acceptance Criteria:* Formulas implemented in Python pipeline and defined for Tableau calculations.
  * *Artifact:* `tableau/calculated_fields_and_parameters.md`

---

### Epic 3: Data Visualizations
* **Complexity:** High | **Status:** 100% Complete
* **Task 3.1 — Core Analytical Worksheets:**
  * *User Story:* As a Visualization Designer, I want to build foundational worksheets visualizing vehicle category sales, top manufacturer leaderboards, battery chemistry distribution, and geographical assembly maps.
  * *Acceptance Criteria:* 5 core worksheets configured in Tableau XML with custom color palettes and tooltips.
  * *Artifact:* `tableau/Electric_Vehicle_Market_Performance.twb` (Worksheets 1 - 5)
* **Task 3.2 — Advanced Analytical Views:**
  * *User Story:* As a Research Analyst, I want to visualize the correlation between driving range and battery capacity, multi-year adoption trajectories, price efficiency matrices, and net carbon offsets.
  * *Acceptance Criteria:* 4 advanced analytical worksheets configured with scatter trendlines, dual-axis line charts, and bar comparisons.
  * *Artifact:* `tableau/Electric_Vehicle_Market_Performance.twb` (Worksheets 6 - 9)

---

### Epic 4: Dashboards Development
* **Complexity:** High | **Status:** 100% Complete
* **Task 4.1 — Executive Strategy Dashboard (Emily Johnson):**
  * *User Story:* As an EV Market Strategy Director, I need an executive dashboard displaying KPI cards, category turnover, manufacturer rankings, and regional filters to drive product portfolio planning.
  * *Acceptance Criteria:* Responsive layout with dynamic filters for Year, Category, and Region; connected KPI cards.
  * *Artifact:* `Dashboard 1 - Executive Strategy` in Tableau and `/strategy` in web app.
* **Task 4.2 — Competitive BI Dashboard (David Chen):**
  * *User Story:* As an Automotive BI Manager, I need a dashboard showing manufacturer market shares, geographic production concentrations, and battery chemistry distribution to guide market entry advisory.
  * *Acceptance Criteria:* Synchronized multi-chart filtering, brand comparison charts, and competitive benchmarking matrix.
  * *Artifact:* `Dashboard 2 - Competitive BI` in Tableau and `/bi` in web app.

---

### Epic 5: Tableau Story
* **Complexity:** Medium | **Status:** 100% Complete
* **Task 5.1 — Structured Narrative Story Points:**
  * *User Story:* As an Industry Researcher, I want a 5-step guided narrative story that leads stakeholders through the EV revolution from 2019 adoption inflection to the 2030 strategic roadmap.
  * *Acceptance Criteria:* 5 distinct story points with captions, narrative sidebars, and contextual visual dashboards.
  * *Artifact:* `Story - EV Market Transformation` in Tableau and `/story` in web app.
* **Task 5.2 — Executive Takeaways & Annotations:**
  * *User Story:* As an Executive Stakeholder, I want action-driven strategic callouts highlighting segment takeaways.
  * *Acceptance Criteria:* Actionable recommendations for strategy, consulting, and clean-tech policy.
  * *Artifact:* Strategic insight callouts in Tableau Story and Web Portal.

---

### Epic 6: Performance Testing
* **Complexity:** Medium | **Status:** 100% Complete
* **Task 6.1 — Benchmarking & SLA Validation:**
  * *User Story:* As a Technical Architect, I want to benchmark data query speed, filter response times, and calculated field execution to guarantee interactive dashboard response times < 250ms.
  * *Acceptance Criteria:* Automated performance test script producing empirical latency metrics, JSON log, and optimization documentation.
  * *Artifact:* `performance_testing/benchmark_tests.py`, `performance_testing/Performance_Testing_Report.md`, `performance_testing/test_results.json`

---

### Epic 7: Web Integration
* **Complexity:** High | **Status:** 100% Complete
* **Task 7.1 — Full-Stack Flask Web Server:**
  * *User Story:* As an End User, I want a web application that integrates the analytics and allows browsing all scenarios from any browser.
  * *Acceptance Criteria:* Flask application with 15 verified routes serving landing page, 3 scenario portals, Tableau story, data explorer, and JSON REST APIs.
  * *Artifact:* `web_app/app.py`, `web_app/templates/`
* **Task 7.2 — Interactive Frontend & Chart.js Integration:**
  * *User Story:* As a Stakeholder, I want responsive visual charts with live hover tooltips, multi-criteria filtering, and one-click data downloads.
  * *Acceptance Criteria:* Dark glassmorphism CSS theme, Chart.js live charts, filter listeners, and CSV export.
  * *Artifact:* `web_app/static/css/style.css`, `web_app/static/js/main.js`

---

### Epic 8: Project Demonstration & Documentation
* **Complexity:** Medium | **Status:** 100% Complete
* **Task 8.1 — Technical Project Report & Architecture:**
  * *User Story:* As an Academic/Industry Evaluator, I want a complete technical project report documenting methodology, data dictionary, architecture, and findings matching SmartBridge evaluation rubrics.
  * *Acceptance Criteria:* Formal capstone documentation with diagrams, tables, and references.
  * *Artifact:* `docs/Project_Report.md`, `docs/Architecture_and_Workflow.md`
* **Task 8.2 — GitHub Repository Staging & Demonstration Links:**
  * *User Story:* As a Student Intern, I want a Git repository with README, badges, quickstart instructions, and links to submit on MySkillWallet.
  * *Acceptance Criteria:* Git initialized, clean commit history, README with scenario walkthroughs, demo hosting guide.
  * *Artifact:* `.git/`, `README.md`, `run_app.bat`
