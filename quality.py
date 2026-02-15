import time

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
        pass

    def rework(self):
        """Perform rework for rejected batch."""
        pass


