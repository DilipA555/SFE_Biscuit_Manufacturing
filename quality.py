import time
import random

class Quality:
    """
    Handles defect calculation, quality decision and rework.
    """
    def calculate_defect(self, produced, defects):
        """Calculates defect percentage."""
        total = produced + defects
        defect_percent = (defects / total)*100
        print(f"\n Defect % -> {round(defect_percent,2)}")
        return defect_percent
    
    def check_quality(self, defect_percent, threshold=10):
        """Checks quality and approve or reject based on defect percentage."""
        if defect_percent <= threshold:
            print("Approved")
        else:
            print("Rejected, sent for rework.")
            self.rework()

    def rework(self, defects):
        """Perform rework for rejected batch."""
        print("\n Rework in progress...")
        time.sleep(2)

        # Assuming we fix 50% to 80% of defects
        fixed_defects = int(defects * (random.uniform(0.5, 0.8)))
        remaining_defects = defects - fixed_defects

        print(f"Defects received for rework: {defects}")
        print(f"Defects fixed: {fixed_defects}")
        print(f"Remaining defects: {remaining_defects}")
        print("Rework completed")

        return remaining_defects


