import random
import time
from typing import Tuple

class Quality:
    """
    Handles defect calculation, quality decision and rework.
    """

    def calculate_defect(self, produced: int, defects: int) -> float:
        """Calculates defect percentage."""

        total: int = produced + defects
        if total == 0:
            print("\nNo production data to calculate defects")
            return 0.0
        defect_percent = (defects / total)*100
        print(f"\nDefect % -> {round(defect_percent,2)}")
        return defect_percent
    
    
    def check_quality(self, produced: int, defects: int, threshold: int = 10) -> Tuple[int, int]:
        """Checks quality and approve or reject based on defect percentage."""

        try:
            defect_percent = self.calculate_defect(produced, defects)        
            if defect_percent <= threshold:
                print("Approved")
            else:
                print("Rejected, sent for rework.")
                time.sleep(3)
                produced, defects = self.rework(produced, defects)
                time.sleep(3)
                print("\nChecking the quality again after rework...")
                time.sleep(5)
                defect_percent_after_rework = self.calculate_defect(produced, defects)
                if defect_percent_after_rework <= threshold:
                    print("Approved after rework.")
                else:
                    print("Rejected after rework.")
            return produced, defects
        
        except Exception as e:
            print("\nError during quality checking:", str(e))
            return produced, defects
        
        finally:
            print("\nQuality checking completed.")


    def rework(self, produced: int, defects: int) -> Tuple[int, int]:
        """Perform rework for rejected batch."""

        print("\nRework in progress...")
        time.sleep(5)
        # Assuming we fix 50% to 80% of defects
        fixed_defects = int(defects * (random.uniform(0.5, 0.8)))
        produced += fixed_defects
        remaining_defects = defects - fixed_defects
        print("\n------Rework summary------")
        print(f"Defects received for rework: {defects}")
        print(f"Defects fixed: {fixed_defects}")
        print(f"Remaining defects: {remaining_defects}")
        print("\nRework completed")
        return produced, remaining_defects


