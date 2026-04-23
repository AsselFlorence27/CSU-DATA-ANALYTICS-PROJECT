# -*- coding: utf-8 -*-
import sys
import os
from src.generator import CSUDataGenerator
from src.db_manager import CSUDatabaseManager
from src.cleaner import CSUDataCleaner
import pandas as pd

# Fix encoding for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def run_full_pipeline():
    print("[FINAL] Starting Project Data Preparation...")
    
    # 1. Generation
    print("   -> Generating raw data...")
    gen = CSUDataGenerator()
    df_s = gen.generate_students(800)
    df_a = gen.generate_academic_records(df_s)
    df_f = gen.generate_financials(df_s)
    
    os.makedirs("data/raw", exist_ok=True)
    df_s.to_csv("data/raw/students_raw.csv", index=False)
    df_a.to_csv("data/raw/academic_records_raw.csv", index=False)
    df_f.to_csv("data/raw/financial_info_raw.csv", index=False)
    
    # 2. Database & Processing
    print("   -> Setting up database and cleaning...")
    db = CSUDatabaseManager("data/processed/csu_analytics.db")
    cleaner = CSUDataCleaner()
    
    db.load_table(df_s, "students_raw")
    db.load_table(df_a, "academic_records_raw")
    db.load_table(df_f, "financial_info_raw")
    
    query = """
    SELECT s.*, a.gpa, f.monthly_income 
    FROM students_raw s
    JOIN academic_records_raw a ON s.student_id = a.student_id
    JOIN financial_info_raw f ON s.student_id = f.student_id
    """
    df_merged = db.query_to_df(query)
    df_cleaned = cleaner.clean_student_demographics(df_merged)
    df_final = cleaner.engineer_scholarship_status(df_cleaned)
    
    os.makedirs("data/processed", exist_ok=True)
    df_final.to_csv("data/processed/csu_master_analytics.csv", index=False)
    db.load_table(df_final, "master_analytics")
    
    print("\n[SUCCESS] All data prepared and processed.")
    print("      - Raw data: data/raw/")
    print("      - Processed results: data/processed/")

if __name__ == "__main__":
    run_full_pipeline()
