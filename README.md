# CSU Scholarship Retention Analysis
**Caraga State University (Main Campus, Butuan City)**  
*Apr 2026 | Python · SQLite · EDA · Data Engineering · Tableau*

Developed a professional-grade analytics pipeline to simulate and solve real-world student retention challenges at Caraga State University. The project identifies students at risk of losing financial aid by correlating academic performance (GPA) with socio-economic factors, providing actionable insights for university administrators to optimize scholarship distribution.

---

## 📁 Repository Structure
```text
csu_project/
├── data/                    # Unified data storage
│   ├── raw/                 # Original synthetic university datasets
│   └── processed/           # SQL database and cleaned master analytics
├── notebooks/               # Interactive Step-by-Step Project Walkthrough
│   ├── 01_Data_Generation.ipynb
│   ├── 02_Database_Setup.ipynb
│   ├── 03_Data_Cleaning.ipynb
│   └── 04_Analysis_and_Insights.ipynb
├── src/                     # Modular "Engine" Code
│   ├── generator.py         # Logic for synthetic record creation
│   ├── db_manager.py        # SQLite connectivity and table management
│   ├── cleaner.py           # Preprocessing and risk flagging logic
│   └── analyzer.py          # Statistics and visualization components
├── setup_data.py            # Utility script to generate the entire dataset
└── requirements.txt         # Project dependencies
```

## 🚀 Impact & Key Findings
- **Risk Identification**: Surfaced 120+ students on "Warning" or "Revoked" scholarship status across Engineering and Computing colleges.
- **Socio-Economic Insights**: Identified a critical correlation between household income brackets and academic resilience, recommending targeted support for low-income student-athletes.
- **Strategic Policy**: Produced a policy-ready analytic CSV formatted specifically for executive Tableau dashboards to streamline university decision-making.

## 🛠️ Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Rerun the full data generation:
   ```bash
   python setup_data.py
   ```
