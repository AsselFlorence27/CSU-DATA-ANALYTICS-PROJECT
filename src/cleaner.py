# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

class CSUDataCleaner:
    """Modular data cleaning and feature engineering for CSU data."""
    
    @staticmethod
    def clean_student_demographics(df):
        """Cleans student demographic data."""
        # Handle missing age with median
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        df['age'] = df['age'].fillna(df['age'].median())
        
        # Standardize college names
        df['college'] = df['college'].str.strip().str.title()
        return df

    @staticmethod
    def engineer_scholarship_status(df_merged):
        """Calculates scholarship risk levels based on GPA."""
        def get_status(gpa):
            if gpa > 3.0: return "Revoked"
            if gpa >= 2.5: return "Warning"
            return "Active"
            
        df_merged['scholarship_status'] = df_merged['gpa'].apply(get_status)
        return df_merged

    @staticmethod
    def categorize_income(monthly_income):
        """Categorizes income into brackets."""
        if monthly_income < 10957: return "Poor"
        if monthly_income < 21914: return "Low Income"
        if monthly_income < 43828: return "Lower Middle"
        if monthly_income < 76669: return "Middle Income"
        return "High Income"
