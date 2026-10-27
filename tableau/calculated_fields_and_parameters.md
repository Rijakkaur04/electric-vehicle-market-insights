# Tableau Calculated Fields & Parameters Reference

## Overview
This document outlines all calculated fields, Level of Detail (LOD) expressions, parameters, and table calculations configured for the **Electric Vehicle Market Performance & Insights** Tableau workbook (`Electric_Vehicle_Market_Performance.twb`).

---

## 1. Core Calculated Fields

### 1.1 Gross Sales Revenue
* **Field Name:** `[Sales Revenue ($)]`
* **Tableau Syntax:**
  ```tableau
  [Annual Sales Units] * [Base Price USD]
  ```
* **Data Type:** Currency (USD)
* **Purpose:** Calculates total sales revenue generated per model trim.

### 1.2 Battery Range Efficiency
* **Field Name:** `[Range Efficiency (km/kWh)]`
* **Tableau Syntax:**
  ```tableau
  ROUND([Driving Range km] / [Battery Capacity kWh], 2)
  ```
* **Data Type:** Float (Number)
* **Purpose:** Measures energy utilization efficacy — higher values represent superior engineering efficiency.

### 1.3 Price per Kilometer Range
* **Field Name:** `[Price per km Range ($/km)]`
* **Tableau Syntax:**
  ```tableau
  ROUND([Base Price USD] / [Driving Range km], 2)
  ```
* **Data Type:** Currency (USD)
* **Purpose:** Consumer value proposition metric indicating price paid per kilometer of single-charge freedom.

### 1.4 Customer Satisfaction Tier
* **Field Name:** `[Satisfaction Tier]`
* **Tableau Syntax:**
  ```tableau
  IF [Customer Rating] >= 4.5 THEN "Delighted (4.5 - 5.0)"
  ELSEIF [Customer Rating] >= 4.0 THEN "Satisfied (4.0 - 4.4)"
  ELSEIF [Customer Rating] >= 3.5 THEN "Neutral (3.5 - 3.9)"
  ELSE "Needs Improvement (< 3.5)"
  END
  ```
* **Data Type:** String (Dimension)
* **Purpose:** Qualitative segmentation for sentiment analysis and customer retention studies.

### 1.5 Driving Range Segment
* **Field Name:** `[Range Category]`
* **Tableau Syntax:**
  ```tableau
  IF [Driving Range km] >= 600 THEN "Ultra Long Range (>= 600 km)"
  ELSEIF [Driving Range km] >= 450 THEN "Long Range (450 - 599 km)"
  ELSEIF [Driving Range km] >= 300 THEN "Standard Range (300 - 449 km)"
  ELSE "City Commuter (< 300 km)"
  END
  ```
* **Data Type:** String (Dimension)
* **Purpose:** Classifies range capabilities to address consumer range anxiety research.

### 1.6 Price Segment Classification
* **Field Name:** `[Price Segment]`
* **Tableau Syntax:**
  ```tableau
  IF [Base Price USD] >= 80000 THEN "Ultra Luxury / Commercial ($80K+)"
  ELSEIF [Base Price USD] >= 50000 THEN "Premium ($50K - $80K)"
  ELSEIF [Base Price USD] >= 30000 THEN "Mid-Market ($30K - $50K)"
  ELSE "Mass Economy (< $30K)"
  END
  ```
* **Data Type:** String (Dimension)
* **Purpose:** Categorizes market pricing tiers for executive portfolio management.

---

## 2. Advanced Table Calculations & LODs

### 2.1 Dynamic Market Share Percentage
* **Field Name:** `[Market Share %]`
* **Tableau Syntax:**
  ```tableau
  SUM([Annual Sales Units]) / TOTAL(SUM([Annual Sales Units])) * 100
  ```
* **Compute Using:** Table (Across / Down) or specific Dimension (`Make`)
* **Purpose:** Computes the relative market share of manufacturers per year/region.

### 2.2 Category Benchmark LOD Expression
* **Field Name:** `[Category Avg Range LOD]`
* **Tableau Syntax:**
  ```tableau
  { FIXED [Vehicle Category] : AVG([Driving Range km]) }
  ```
* **Purpose:** Provides a fixed benchmark to compare individual vehicle trims against their respective segment average regardless of filters.

### 2.3 Manufacturer Total Sales LOD
* **Field Name:** `[OEM Global Sales LOD]`
* **Tableau Syntax:**
  ```tableau
  { FIXED [Make], [Model Year] : SUM([Annual Sales Units]) }
  ```
* **Purpose:** Retains total OEM sales context across multi-trim drill downs.

---

## 3. Dynamic Interactive Parameters

### 3.1 Parameter: `[Select Metric]`
* **Data Type:** String
* **Allowable Values:**
  * `"Sales Units"`
  * `"Gross Revenue"`
  * `"Average Range"`
  * `"Customer Satisfaction"`
* **Associated Dynamic Measure Field:**
  ```tableau
  CASE [Select Metric]
      WHEN "Sales Units" THEN SUM([Annual Sales Units])
      WHEN "Gross Revenue" THEN SUM([Sales Revenue USD])
      WHEN "Average Range" THEN AVG([Driving Range km])
      WHEN "Customer Satisfaction" THEN AVG([Customer Rating])
  END
  ```

### 3.2 Parameter: `[Top N Manufacturers]`
* **Data Type:** Integer
* **Current Value:** `5`
* **Allowable Values:** Range from `3` to `15` (Step: `1`)
* **Purpose:** Dynamic filtering of leaderboard charts to prevent visual clutter.
