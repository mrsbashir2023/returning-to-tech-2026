# data_annotator.py - Hebh Abed - Day 4 - AI Data Trainer Portfolio
# Skills: Data Annotation, QA, Attention to Detail, Python, JSON
# BCS 2007 C++ Logic -> Python for AI Training

import json
from datetime import datetime

class DataAnnotator:
    """Simulates real AI Data Annotation work - like Scale AI / Outlier jobs"""
    
    def __init__(self, annotator_name):
        self.annotator = annotator_name
        self.annotations = []
        print(f"Annotator {self.annotator} ready - QA Mode ON")

    def annotate_text(self, text_id, text_content, label, confidence):
        """Core task: Label data for AI training - exactly what AI Trainer jobs do"""
        if not text_content or not label:
            print(f"Error ID {text_id}: Missing content or label - QA FAIL")
            return False
            
        if confidence < 0 or confidence > 100:
            print(f"Error ID {text_id}: Confidence must be 0-100 - QA FAIL")
            return False

        annotation = {
            "id": text_id,
            "text": text_content,
            "label": label,
            "confidence": confidence,
            "annotator": self.annotator,
            "timestamp": datetime.now().isoformat(),
            "qa_status": "PASS" if confidence >= 80 else "REVIEW"
        }
        
        self.annotations.append(annotation)
        print(f"Annotated ID {text_id}: '{label}' ({confidence}%) -> {annotation['qa_status']}")
        return True

    def quality_check(self):
        """QA Tester skill - required for $20-$65/hr AI jobs"""
        if not self.annotations:
            print("No annotations to check")
            return
            
        total = len(self.annotations)
        passed = sum(1 for a in self.annotations if a["qa_status"] == "PASS")
        review = total - passed
        avg_conf = sum(a["confidence"] for a in self.annotations) / total if total else 0
        
        print("\n=== QA REPORT ===")
        print(f"Total: {total} | PASS: {passed} | REVIEW: {review}")
        print(f"Average Confidence: {avg_conf:.1f}%")
        print(f"Accuracy Rate: {(passed/total*100):.1f}%" if total else "0%")
        
        # Attention to detail check - like real job
        low_quality = [a for a in self.annotations if a["confidence"] < 70]
        if low_quality:
            print(f"⚠️  {len(low_quality)} items need re-annotation (confidence <70%)")

    def export_json(self, filename="training_data.json"):
        """Export for AI model training - JSON is #1 skill in job posts"""
        with open(filename, 'w') as f:
            json.dump(self.annotations, f, indent=2)
        print(f"\nExported {len(self.annotations)} records to {filename} - Ready for ML training")

# Demo - This is what you do in a real AI Data Trainer interview
if __name__ == "__main__":
    print("=== AI Data Annotation Demo - Remote AI Trainer ===")
    
    # You are the annotator
    heba = DataAnnotator("Hebh Abed - Bilingual EN/AR")
    
    # Simulate annotating customer support data (your TTEC background)
    heba.annotate_text(1, "My internet is not working", "Technical_Issue", 95)
    heba.annotate_text(2, "How much is the bill?", "Billing_Question", 90)
    heba.annotate_text(3, "شكرا لك", "Thank_You_Arabic", 98)  # Bilingual edge!
    heba.annotate_text(4, "", "Empty_Text", 50)  # QA test - should fail
    heba.annotate_text(5, "The app crashes when I open it", "Bug_Report", 88)
    
    heba.quality_check()
    heba.export_json()

    print("\n✅ Day 4 complete - Skills demonstrated: Python, JSON, QA, Annotation, Bilingual")