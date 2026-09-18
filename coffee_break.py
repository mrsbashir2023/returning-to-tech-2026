# coffee_break.py - Because even coders need coffee!
# Day: Rest Day - Mental Health Break - Just for Hebh

import time
from datetime import datetime

def coffee_break():
    print("☕ Hey Hebh! It's coffee break time!")
    print(f"   Time: {datetime.now().strftime('%I:%M %p')}")
    print()
    
    steps = [
        "1. Laptop closed? ✓",
        "2. Coffee in hand? ☕",
        "3. Deep breath in... (4 seconds)",
        "4. Deep breath out... (4 seconds)",
        "5. You have 7 files on GitHub. You are ahead. 💪",
        "6. Titanic can wait till tomorrow. No rush.",
        "7. BCS 2007 → 2026 comeback is happening.",
    ]
    
    for step in steps:
        print(step)
        time.sleep(1)  # 1 second pause like sipping coffee
    
    print()
    print("✨ Reminder: You don't have to finish everything today.")
    print("✨ Come back when the coffee is done and head feels light.")
    print()
    print("Status: On Break - 7/7 files done - Proud of you! ☕💛")

if __name__ == "__main__":
    coffee_break()