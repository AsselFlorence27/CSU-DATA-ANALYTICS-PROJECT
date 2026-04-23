# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import os
from faker import Faker

class CSUDataGenerator:
    """Modular record utility for the CSU Scholarship Project."""
    
    def __init__(self, seed=42):
        self.fake = Faker('en_PH')
        random.seed(seed)
        np.random.seed(seed)
        
        self.COLLEGES = {
            "College of Computing and Information Sciences": [
                "BS Computer Science", "BS Information Technology", "BS Information Systems"
            ],
            "College of Engineering and Geosciences": [
                "BS Civil Engineering", "BS Electrical Engineering", "BS Mechanical Engineering"
            ],
            "College of Management, Economics, and Business": [
                "BS Business Administration", "BS Accountancy", "BS Economics"
            ],
            "College of Education": [
                "Bachelor of Secondary Education", "Bachelor of Elementary Education"
            ],
            "College of Arts and Sciences": [
                "BS Biology", "BS Mathematics", "BA Communication"
            ]
        }
        
    def generate_students(self, n=800):
        students = []
        for i in range(n):
            sid = f"CSU-{2021 + (i // 200):04d}-{str(i % 9999 + 1000).zfill(4)}"
            college = random.choice(list(self.COLLEGES.keys()))
            course = random.choice(self.COLLEGES[college])
            sex = random.choice(["Male", "Female"])
            
            students.append({
                "student_id": sid,
                "last_name": self.fake.last_name(),
                "first_name": self.fake.first_name_male() if sex == "Male" else self.fake.first_name_female(),
                "sex": sex,
                "age": random.randint(17, 26),
                "college": college,
                "course": course,
                "year_level": random.randint(1, 4),
                "scholarship_type": random.choices(
                    ["CHED UniFAST", "DOST SEI", "LGU Sponsored", "None"], 
                    weights=[30, 15, 15, 40]
                )[0]
            })
            
        df = pd.DataFrame(students)
        # Inject some noise for cleaning exercise
        df.loc[random.sample(range(n), 20), 'age'] = np.nan
        return df

    def generate_academic_records(self, df_students):
        records = []
        for _, student in df_students.iterrows():
            # Generate 2nd semester record
            gpa = round(random.uniform(1.0, 5.0), 2)
            records.append({
                "student_id": student["student_id"],
                "academic_year": "2023-2024",
                "semester": "2nd Semester",
                "gpa": gpa,
                "units_enrolled": 21,
                "units_earned": 21 if gpa <= 3.0 else random.randint(12, 18)
            })
        return pd.DataFrame(records)

    def generate_financials(self, df_students):
        financials = []
        for _, student in df_students.iterrows():
            financials.append({
                "student_id": student["student_id"],
                "monthly_income": random.randint(5000, 150000),
                "working_student": random.choice([0, 1])
            })
        return pd.DataFrame(financials)
