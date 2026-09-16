# excel_cleaner.py - Day 6 - Google Data Analytics M2: Spreadsheets
# Skill: Data Cleaning, Excel Logic, Attention to Detail (AI Trainer job)

import csv
from datetime import datetime

class ExcelCleaner:
    """Simulates cleaning Excel data - like Google M2 & AI Trainer jobs"""
    
    def __init__(self):
        print("Excel Cleaner Ready - Data Cleaning Mode ON")
        self.cleaned_rows = []
        self.errors = 0

    def clean_row(self, row_id, name, age, email, salary):
        # QA Check - exactly like data_annotator.py
        if not name or not email:
            print(f"Row {row_id}: MISSING data - SKIP")
            self.errors += 1
            return False
        
        # Clean Age - remove blank like Titanic dataset
        try:
            age = int(age)
            if age < 0 or age > 120:
                print(f"Row {row_id}: Invalid age {age} - SKIP")
                self.errors += 1
                return False
        except:
            print(f"Row {row_id}: Age blank or text - FIX to 0")
            age = 0

        # Clean Email - check @ like real Excel formula
        if "@" not in email:
            print(f"Row {row_id}: Bad email {email} - SKIP")
            self.errors += 1
            return False

        # Clean Salary - remove $ and commas like Excel CLEAN
        try:
            salary = salary.replace("$","").replace(",","")
            salary = float(salary)
        except:
            salary = 0.0

        cleaned = {
            "id": row_id,
            "name": name.strip().title(),  # Title Case like Excel PROPER
            "age": age,
            "email": email.strip().lower(),
            "salary": salary,
            "cleaned_at": datetime.now().isoformat()
        }
        
        self.cleaned_rows.append(cleaned)
        print(f"Row {row_id}: CLEANED - {cleaned['name']} | ${cleaned['salary']}")
        return True

    def report(self):
        print(f"\n=== CLEANING REPORT ===")
        print(f"Cleaned: {len(self.cleaned_rows)} rows")
        print(f"Errors/Dirty: {self.errors} rows")
        print(f"Clean Rate: {len(self.cleaned_rows)/(len(self.cleaned_rows)+self.errors)*100:.1f}%")

# Demo - This is Google Data Analytics M2 work
if __name__ == "__main__":
    print("=== Excel Data Cleaning - Superstore Style ===")
    cleaner = ExcelCleaner()
    
    # Simulate dirty Excel rows (like Titanic blanks)
    cleaner.clean_row(1, "  hebh abed ", "42", "HEBH@EMAIL.COM", "$65,000")
    cleaner.clean_row(2, "", "25", "test@email.com", "50000")  # Missing name
    cleaner.clean_row(3, "John Doe", "", "john@email.com", "$70,000")  # Blank age
    cleaner.clean_row(4, "Sara Smith", "30", "bad-email", "80000")  # Bad email
    cleaner.clean_row(5, "Ali Khan", "35", "ali@email.com", "$95,500")
    
    cleaner.report()
    print("\n✅ Day 6 complete - Skill: Data Cleaning (Google M2)")