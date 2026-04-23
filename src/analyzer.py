# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CSUDataAnalyzer:
    """Modular analysis and visualization for CSU project."""
    
    def __init__(self, master_df):
        self.df = master_df
        # Use a clean plotting style
        sns.set_theme(style="whitegrid")

    def get_at_risk_summary(self):
        """Returns summary counts of scholarship status."""
        return self.df['scholarship_status'].value_counts()

    def plot_income_vs_gpa(self, output_path=None):
        """Generates a scatter plot of income vs GPA."""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=self.df, 
            x='monthly_income', 
            y='gpa', 
            hue='scholarship_status',
            palette={'Active': '#2ecc71', 'Warning': '#f1c40f', 'Revoked': '#e74c3c'},
            alpha=0.6
        )
        plt.title('Monthly Household Income vs Latest GPA (PH System)')
        plt.xlabel('Monthly Income (PHP)')
        plt.ylabel('Latest GPA (1.0 is Best)')
        
        if output_path:
            plt.savefig(output_path)
        return plt

    def plot_status_by_college(self, output_path=None):
        """Generates a stacked bar chart of status by college."""
        plt.figure(figsize=(12, 6))
        status_pivot = self.df.groupby(['college', 'scholarship_status']).size().unstack().fillna(0)
        status_pivot.plot(kind='bar', stacked=True, color=['#2ecc71', '#e74c3c', '#f1c40f'], ax=plt.gca())
        
        plt.title('Scholarship Status Distribution by College')
        plt.ylabel('Number of Students')
        plt.xticks(rotation=45, ha='right')
        
        if output_path:
            plt.savefig(output_path)
        return plt
