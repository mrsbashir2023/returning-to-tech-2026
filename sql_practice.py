# sql_practice.py - Day 9 - Google M2 SQL Basics + AI Trainer Logic
# Skill: SQL, Filtering, SELECT WHERE - Top job requirement

class SQLPractice:
    """Simulates SQL in Python - since you don't have SQL server yet"""
    
    def __init__(self):
        # Fake database table - like Superstore Sales
        self.employees = [
            {"id": 1, "name": "Hebh Abed", "dept": "Support", "salary": 65000, "city": "Niagara Falls"},
            {"id": 2, "name": "John Doe", "dept": "Tech", "salary": 90000, "city": "Buffalo"},
            {"id": 3, "name": "Sara Smith", "dept": "Support", "salary": 70000, "city": "Niagara Falls"},
            {"id": 4, "name": "Ali Khan", "dept": "Data", "salary": 95000, "city": "Remote"},
            {"id": 5, "name": "Mike Lee", "dept": "Support", "salary": 60000, "city": "Niagara Falls"},
        ]
        print("Database Loaded: 5 employees")

    def select_where(self, department=None, min_salary=0):
        # This is SELECT * FROM employees WHERE dept = X AND salary > Y
        print(f"\n--- SQL: SELECT * WHERE dept='{department}' AND salary>{min_salary} ---")
        results = []
        for emp in self.employees:
            if (department is None or emp["dept"] == department) and emp["salary"] >= min_salary:
                results.append(emp)
                print(f"ID {emp['id']}: {emp['name']} | {emp['dept']} | ${emp['salary']} | {emp['city']}")
        
        if not results:
            print("No rows found - like empty SQL result")
        return results

    def count_group_by(self):
        # This is SELECT dept, COUNT(*) GROUP BY dept - Google M2
        print("\n--- SQL: SELECT dept, COUNT(*) GROUP BY dept ---")
        counts = {}
        for emp in self.employees:
            counts[emp["dept"]] = counts.get(emp["dept"], 0) + 1
        
        for dept, count in counts.items():
            print(f"Department {dept}: {count} employees")

# Demo - SQLBolt Lesson 1-3 in Python
if __name__ == "__main__":
    print("=== SQL Practice - Google Data Analytics M2 ===")
    db = SQLPractice()
    
    # Task 1: SELECT WHERE - Find Support team (your TTEC background)
    db.select_where(department="Support")
    
    # Task 2: SELECT WHERE salary filter - Find high earners $80k+
    db.select_where(min_salary=80000)
    
    # Task 3: GROUP BY - Count by department
    db.count_group_by()
    
    print("\n✅ Day 9 complete - Skill: SQL SELECT, WHERE, GROUP BY")
    print("Next: Try real SQL at sqlbolt.com Lesson 1-3 (free, 20 mins)")