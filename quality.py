class Quality:
    """
    Handles defect calculation, quality decision and rework.
    """
    def calculate_defect(self, produced, defects):
        """Calculates defect percentage."""
        pass

    def rework(self):
        """Perform rework for rejected batch."""
        pass

    def check_quality(self, defect_percent, threshold=10):
        """Checks quality and approve or reject based on defect percentage."""
        pass
