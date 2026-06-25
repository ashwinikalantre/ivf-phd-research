const renderResearchDashboard = () => {
  if (!window.Chart) return;

  window.__researchDashboardCharts = window.__researchDashboardCharts || {};

  const chartColors = [
    "#00796b",
    "#3949ab",
    "#f57c00",
    "#c62828",
    "#6a1b9a",
    "#2e7d32",
    "#455a64",
  ];

  const makeBar = (id, labels, values, title) => {
    const el = document.getElementById(id);
    if (!el) return;
    if (window.__researchDashboardCharts[id]) {
      window.__researchDashboardCharts[id].destroy();
    }
    new Chart(el, {
      type: "bar",
      data: {
        labels,
        datasets: [{ label: title, data: values, backgroundColor: chartColors }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: { y: { beginAtZero: true, ticks: { precision: 0 } } },
      },
    });
    window.__researchDashboardCharts[id] = Chart.getChart(el);
  };

  const makeDoughnut = (id, labels, values) => {
    const el = document.getElementById(id);
    if (!el) return;
    if (window.__researchDashboardCharts[id]) {
      window.__researchDashboardCharts[id].destroy();
    }
    new Chart(el, {
      type: "doughnut",
      data: {
        labels,
        datasets: [{ data: values, backgroundColor: chartColors }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: "bottom" } },
      },
    });
    window.__researchDashboardCharts[id] = Chart.getChart(el);
  };

  makeBar(
    "gapChart",
    [
      "External validation",
      "Clinical decision support",
      "Deployment evidence",
      "Retrospective design",
      "Trustworthy AI",
      "Prospective/RCT",
      "Single-center",
    ],
    [26, 18, 9, 9, 8, 7, 6],
    "Frequency"
  );

  makeBar(
    "yearChart",
    ["2021", "2022", "2023", "2024", "2025", "2026"],
    [1, 3, 1, 8, 21, 1],
    "Papers"
  );

  makeDoughnut(
    "themeChart",
    [
      "Outcome prediction",
      "XAI/trustworthy AI",
      "Embryo selection",
      "Ovarian stimulation/CDSS",
      "FET/ultrasound",
      "Indian/lifestyle",
    ],
    [17, 12, 6, 5, 3, 4]
  );
};

document.addEventListener("DOMContentLoaded", renderResearchDashboard);
document.addEventListener("md-content-rendered", renderResearchDashboard);
