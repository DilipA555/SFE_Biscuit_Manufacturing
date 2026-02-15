import time
import random

class Quality:
    """
    Handles defect calculation, quality decision and rework.
    """

    def calculate_defect(self, produced, defects):
        """Calculates defect percentage."""

        total = produced + defects
        if total == 0:
            print("No production data to calculate defects")
            return 0
        defect_percent = (defects / total)*100
        print(f"\n Defect % -> {round(defect_percent,2)}")
        return defect_percent
    
    def check_quality(self, produced, defects, threshold=10):
        """Checks quality and approve or reject based on defect percentage."""

        defect_percent = self.calculate_defect(produced, defects)        
        if defect_percent <= threshold:
            print("Approved")
        else:
            print("Rejected, sent for rework.")
            time.sleep(2)

            produced, defects = self.rework(produced, defects)
            defect_percent_after_rework = self.calculate_defect(produced, defects)
            if defect_percent_after_rework <= threshold:
                print("Approved after rework.")
            else:
                print("Rejected after rework.")
        return produced, defects


    def rework(self, produced, defects):
        """Perform rework for rejected batch."""

        print("\n Rework in progress...")
        time.sleep(2)

        # Assuming we fix 50% to 80% of defects
        fixed_defects = int(defects * (random.uniform(0.5, 0.8)))
        produced += fixed_defects
        remaining_defects = defects - fixed_defects

        print(f"Defects received for rework: {defects}")
        print(f"Defects fixed: {fixed_defects}")
        print(f"Remaining defects: {remaining_defects}")
        print("Rework completed")

        return produced, remaining_defects


