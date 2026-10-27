/**
 * Electric Vehicle Market Performance & Insights
 * Epic 7: Client-side Visualizations & Interactive Controllers
 */

// Global Chart Instances Cache
const charts = {};

// Color palettes
const COLORS = {
  blue: "#3b82f6",
  cyan: "#06b6d4",
  green: "#10b981",
  amber: "#f59e0b",
  purple: "#8b5cf6",
  pink: "#ec4899",
  indigo: "#6366f1",
  red: "#ef4444",
  palette: ["#3b82f6", "#10b981", "#06b6d4", "#f59e0b", "#8b5cf6", "#ec4899", "#6366f1"]
};

// Global Chart.js Defaults for Dark Theme
if (typeof Chart !== "undefined") {
  Chart.defaults.color = "#9ca3af";
  Chart.defaults.font.family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";
  Chart.defaults.plugins.tooltip.backgroundColor = "rgba(17, 24, 39, 0.95)";
  Chart.defaults.plugins.tooltip.titleColor = "#ffffff";
  Chart.defaults.plugins.tooltip.bodyColor = "#d1d5db";
  Chart.defaults.plugins.tooltip.borderColor = "rgba(255, 255, 255, 0.1)";
  Chart.defaults.plugins.tooltip.borderWidth = 1;
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.plugins.legend.labels.usePointStyle = true;
  Chart.defaults.plugins.legend.labels.boxWidth = 8;
}

/**
 * Updates KPI metric cards based on active filter selections
 */
async function refreshKPIs() {
  const year = document.getElementById("filter-year")?.value || "all";
  const cat = document.getElementById("filter-cat")?.value || "all";
  const reg = document.getElementById("filter-region")?.value || "all";

  try {
    const res = await fetch(`/api/stats?year=${year}&category=${cat}&region=${reg}`);
    const data = await res.json();

    const salesEl = document.getElementById("kpi-sales");
    if (salesEl) salesEl.innerText = data.sales.toLocaleString();

    const revEl = document.getElementById("kpi-revenue");
    if (revEl) revEl.innerText = `$${(data.revenue_usd / 1e9).toFixed(1)}B`;

    const rangeEl = document.getElementById("kpi-range");
    if (rangeEl) rangeEl.innerText = `${data.avg_range_km} km`;

    const rateEl = document.getElementById("kpi-rating");
    if (rateEl) rateEl.innerText = `${data.avg_rating} / 5.0`;

    const co2El = document.getElementById("kpi-co2");
    if (co2El) co2El.innerText = `${(data.total_co2_tons / 1e6).toFixed(2)}M Tons`;
  } catch (err) {
    console.error("Error refreshing KPIs:", err);
  }
}

/**
 * Initializes Scenario 1 (Emily Johnson) Charts
 */
async function initStrategyCharts() {
  const year = document.getElementById("filter-year")?.value || "all";

  // 1. Category Sales Bar Chart
  try {
    const res = await fetch(`/api/charts/category-sales?year=${year}`);
    const data = await res.json();
    const ctx = document.getElementById("chart-category-sales");
    if (ctx) {
      if (charts.catSales) charts.catSales.destroy();
      charts.catSales = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.categories,
          datasets: [
            {
              label: "Sales Volume (Units)",
              data: data.sales,
              backgroundColor: "rgba(59, 130, 246, 0.75)",
              borderColor: COLORS.blue,
              borderWidth: 1,
              borderRadius: 6
            },
            {
              label: "Revenue ($ Billions)",
              data: data.revenue,
              backgroundColor: "rgba(6, 182, 212, 0.75)",
              borderColor: COLORS.cyan,
              borderWidth: 1,
              borderRadius: 6,
              yAxisID: "y1"
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { color: "rgba(255, 255, 255, 0.05)" } },
            y: {
              grid: { color: "rgba(255, 255, 255, 0.05)" },
              title: { display: true, text: "Units Sold" }
            },
            y1: {
              position: "right",
              grid: { drawOnChartArea: false },
              title: { display: true, text: "Revenue ($B)" }
            }
          }
        }
      });
    }
  } catch (err) {
    console.error("Error loading category sales:", err);
  }

  // 2. Top OEM Leaderboard Chart
  try {
    const res = await fetch(`/api/charts/oem-leaderboard?year=${year}`);
    const data = await res.json();
    const ctx = document.getElementById("chart-oem-leaderboard");
    if (ctx) {
      if (charts.oemRank) charts.oemRank.destroy();
      charts.oemRank = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.makes,
          datasets: [{
            label: "Global Unit Sales",
            data: data.sales,
            backgroundColor: [
              "#3b82f6", "#10b981", "#06b6d4", "#f59e0b", "#8b5cf6",
              "#ec4899", "#6366f1", "#14b8a6", "#f97316", "#a855f7"
            ],
            borderRadius: 6
          }]
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { color: "rgba(255, 255, 255, 0.05)" } },
            y: { grid: { color: "rgba(255, 255, 255, 0.05)" } }
          }
        }
      });
    }
  } catch (err) {
    console.error("Error loading OEM leaderboard:", err);
  }

  // 3. Multi-year Trajectory Line Chart
  try {
    const res = await fetch("/api/charts/yearly-trajectory");
    const data = await res.json();
    const ctx = document.getElementById("chart-yearly-trajectory");
    if (ctx) {
      if (charts.trajectory) charts.trajectory.destroy();
      const datasets = Object.keys(data.categories).map((cat, idx) => ({
        label: cat,
        data: data.categories[cat],
        borderColor: COLORS.palette[idx % COLORS.palette.length],
        backgroundColor: COLORS.palette[idx % COLORS.palette.length],
        tension: 0.35,
        fill: false,
        borderWidth: 2
      }));

      charts.trajectory = new Chart(ctx, {
        type: "line",
        data: { labels: data.years, datasets },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: { mode: "index", intersect: false },
          scales: {
            x: { grid: { color: "rgba(255, 255, 255, 0.05)" } },
            y: { grid: { color: "rgba(255, 255, 255, 0.05)" } }
          }
        }
      });
    }
  } catch (err) {
    console.error("Error loading yearly trajectory:", err);
  }
}

/**
 * Initializes Scenario 2 (David Chen) Charts
 */
async function initBICharts() {
  const year = document.getElementById("filter-year")?.value || "all";

  // 1. Battery Distribution Doughnut
  try {
    const res = await fetch(`/api/charts/battery-distribution?year=${year}`);
    const data = await res.json();
    const ctx = document.getElementById("chart-battery-share");
    if (ctx) {
      if (charts.battShare) charts.battShare.destroy();
      charts.battShare = new Chart(ctx, {
        type: "doughnut",
        data: {
          labels: data.chemistries,
          datasets: [{
            data: data.sales,
            backgroundColor: ["#10b981", "#3b82f6", "#f59e0b", "#8b5cf6", "#06b6d4"],
            borderColor: "rgba(10, 14, 23, 0.8)",
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: "bottom" }
          },
          cutout: "65%"
        }
      });
    }
  } catch (err) {
    console.error("Error loading battery share:", err);
  }

  // 2. Manufacturing Country Distribution
  try {
    const res = await fetch("/api/charts/country-production");
    const data = await res.json();
    const ctx = document.getElementById("chart-country-volume");
    if (ctx) {
      if (charts.countryVol) charts.countryVol.destroy();
      charts.countryVol = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.countries,
          datasets: [{
            label: "Vehicle Units Produced",
            data: data.units,
            backgroundColor: "rgba(99, 102, 241, 0.8)",
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { color: "rgba(255, 255, 255, 0.05)" } },
            y: { grid: { color: "rgba(255, 255, 255, 0.05)" } }
          }
        }
      });
    }
  } catch (err) {
    console.error("Error loading country production:", err);
  }
}

/**
 * Initializes Scenario 3 (Dr. Sarah Williams) Charts
 */
async function initResearchCharts() {
  const year = document.getElementById("filter-year")?.value || "all";

  // 1. Scatter Plot: Driving Range vs. Battery Capacity
  try {
    const res = await fetch(`/api/charts/range-capacity-scatter?year=${year}`);
    const data = await res.json();
    const ctx = document.getElementById("chart-range-capacity");
    if (ctx) {
      if (charts.rangeScatter) charts.rangeScatter.destroy();

      const colorMap = {
        "LFP": "#10b981",
        "NMC": "#3b82f6",
        "NCA": "#f59e0b",
        "Solid-State": "#8b5cf6",
        "Sodium-Ion": "#06b6d4"
      };

      const techGroups = {};
      data.forEach(pt => {
        if (!techGroups[pt.tech]) techGroups[pt.tech] = [];
        techGroups[pt.tech].push({ x: pt.x, y: pt.y, model: pt.model, price: pt.price });
      });

      const datasets = Object.keys(techGroups).map(tech => ({
        label: tech,
        data: techGroups[tech],
        backgroundColor: colorMap[tech] || "#ffffff",
        pointRadius: 5,
        pointHoverRadius: 8
      }));

      charts.rangeScatter = new Chart(ctx, {
        type: "scatter",
        data: { datasets },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            tooltip: {
              callbacks: {
                label: function(ctx) {
                  const raw = ctx.raw;
                  return `${raw.model}: ${raw.x} kWh, ${raw.y} km ($${raw.price.toLocaleString()})`;
                }
              }
            }
          },
          scales: {
            x: {
              title: { display: true, text: "Battery Pack Capacity (kWh)" },
              grid: { color: "rgba(255, 255, 255, 0.05)" }
            },
            y: {
              title: { display: true, text: "Official Driving Range (km)" },
              grid: { color: "rgba(255, 255, 255, 0.05)" }
            }
          }
        }
      });
    }
  } catch (err) {
    console.error("Error loading range scatter:", err);
  }
}

/**
 * Initializes Data Explorer Table
 */
async function loadExplorerRecords() {
  const search = document.getElementById("explorer-search")?.value || "";
  const tableBody = document.getElementById("explorer-tbody");
  if (!tableBody) return;

  tableBody.innerHTML = `<tr><td colspan="10" style="text-align:center; padding: 2rem;">Loading data records...</td></tr>`;

  try {
    const res = await fetch(`/api/records?search=${encodeURIComponent(search)}&limit=150`);
    const data = await res.json();

    if (data.records.length === 0) {
      tableBody.innerHTML = `<tr><td colspan="10" style="text-align:center; padding: 2rem;">No matching EV records found.</td></tr>`;
      return;
    }

    let rows = "";
    data.records.forEach(r => {
      let badgeClass = "badge-nmc";
      if (r.Battery_Technology === "LFP") badgeClass = "badge-lfp";
      else if (r.Battery_Technology === "NCA") badgeClass = "badge-nca";
      else if (r.Battery_Technology === "Solid-State") badgeClass = "badge-solid";
      else if (r.Battery_Technology === "Sodium-Ion") badgeClass = "badge-sodium";

      rows += `
        <tr>
          <td><strong>${r.Record_ID}</strong></td>
          <td>${r.Model_Year}</td>
          <td>${r.Make}</td>
          <td>${r.Model_Variant}</td>
          <td>${r.Vehicle_Category}</td>
          <td><span class="badge ${badgeClass}">${r.Battery_Technology}</span></td>
          <td>${r.Battery_Capacity_kWh} kWh</td>
          <td>${r.Driving_Range_km} km</td>
          <td>$${r.Base_Price_USD.toLocaleString()}</td>
          <td>${r.Annual_Sales_Units.toLocaleString()}</td>
          <td>⭐ ${r.Customer_Rating}</td>
          <td>${r.Manufacturing_Country}</td>
        </tr>
      `;
    });

    tableBody.innerHTML = rows;
    const countEl = document.getElementById("record-count-badge");
    if (countEl) countEl.innerText = `${data.records.length} of ${data.total_count} records displayed`;
  } catch (err) {
    console.error("Error loading explorer records:", err);
  }
}

/**
 * Setup Event Listeners
 */
document.addEventListener("DOMContentLoaded", () => {
  // Filter change listeners
  const filterInputs = ["filter-year", "filter-cat", "filter-region"];
  filterInputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener("change", () => {
        refreshKPIs();
        if (typeof initStrategyCharts === "function") initStrategyCharts();
        if (typeof initBICharts === "function") initBICharts();
        if (typeof initResearchCharts === "function") initResearchCharts();
      });
    }
  });

  // Story tab switcher
  const storyTabs = document.querySelectorAll(".story-tab");
  storyTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      storyTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      const targetId = tab.getAttribute("data-target");
      document.querySelectorAll(".story-content-panel").forEach(p => p.classList.remove("active"));
      const panel = document.getElementById(targetId);
      if (panel) panel.classList.add("active");
    });
  });

  // Explorer search
  const searchInput = document.getElementById("explorer-search");
  if (searchInput) {
    let timeout = null;
    searchInput.addEventListener("input", () => {
      clearTimeout(timeout);
      timeout = setTimeout(loadExplorerRecords, 300);
    });
  }
});

