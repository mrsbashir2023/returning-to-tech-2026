# grade_calculator.py - Hebh Abed - Day 2 - C++ to Python
# Translated from classic C++ if/else program

def grade_calculator():
    print("=== Grade Calculator ===")
    
    try:
        score = float(input("Enter your score (0-100): "))
        
        if score < 0 or score > 100:
            print("Invalid! Score must be between 0-100")
            return
        
        # C++ version had if(score>=90) { cout<<"A"; } — same logic, Python syntax
        if score >= 90:
            grade = "A"
            message = "Excellent!"
        elif score >= 80:
            grade = "B"
            message = "Great job!"
        elif score >= 70:
            grade = "C"
            message = "Good effort!"
        elif score >= 60:
            grade = "D"
            message = "You passed!"
        else:
            grade = "F"
            message = "Keep studying!"
            
        print(f"Score: {score} -> Grade: {grade} - {message}")
        
        # Bonus: Pass/Fail like your tutoring experience
        if score >= 60:
            print("Status: PASS")
        else:
            print("Status: FAIL - Need tutoring? (like you did!)")
            
    except ValueError:
        print("Please enter a number only!")

if __name__ == "__main__":
    grade_calculator(grade_calculator.py)