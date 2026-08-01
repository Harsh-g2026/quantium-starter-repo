# Quantium Starter Repo — Pink Morsel Sales Visualiser

An interactive Dash application built to help Soul Foods analyze the impact of a price change on Pink Morsel sales and profitability. This project was completed as part of Quantium's Software Engineering Job Simulation on Forage.

## 📌 Problem Statement

Soul Foods needed to answer a key business question:

> **"Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"**

This repo processes raw transaction data and presents it through an interactive dashboard, enabling data-driven decision-making at a glance.

## 🚀 Features

- **Data Processing Pipeline** — Cleans and merges three raw CSV files into a single formatted dataset (filters Pink Morsel rows, computes `Sales = quantity × price`)
- **Interactive Dashboard** — Built with Plotly Dash, featuring:
  - A line chart visualizing sales trends over time
  - A region filter (North, East, South, West, All) to explore sales by area
  - Custom CSS styling for a clean, engaging UI
- **Automated Test Suite** — Verifies the header, chart, and region picker render correctly using `dash.testing`
- **CI-Ready Bash Script** — Automatically activates the virtual environment, runs the test suite, and returns proper exit codes

## 🗂️ Project Structure

```
quantium-starter-repo/
├── data/                  # Raw transaction CSV files
├── process_data.py        # Data cleaning & transformation script
├── output.csv             # Formatted output (Sales, Date, Region)
├── app.py                 # Dash application
├── test_app.py            # Test suite (pytest + dash.testing)
├── run_tests.sh           # Bash script to run tests automatically
├── requirements.txt       # Python dependencies
└── README.md
```

## 🛠️ Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Harsh-g2026/quantium-starter-repo
   cd quantium-starter-repo
   ```

2. **Create and activate a virtual environment (Python 3.9)**
   ```bash
   py -3.9 -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

**Process the raw data:**
```bash
python process_data.py
```

**Run the dashboard:**
```bash
python app.py
```
Open the local URL printed in the terminal (typically `http://127.0.0.1:8050`).

**Run tests:**
```bash
pytest test_app.py
```

**Run tests via bash script (CI-friendly):**
```bash
./run_tests.sh
```

## 📊 Key Insight

The dashboard reveals a clear, sustained increase in Pink Morsel sales following the January 15, 2021 price change — directly answering Soul Foods' business question.

## 🧰 Tech Stack

- **Python** — Pandas, Plotly Dash
- **Testing** — Pytest, Dash Testing (Selenium-based)
- **Styling** — CSS
- **Automation** — Bash scripting

## 📎 Related

- [Quantium Software Engineering Job Simulation on Forage](https://www.theforage.com/simulations/quantium/software-engineering-j6ci)
