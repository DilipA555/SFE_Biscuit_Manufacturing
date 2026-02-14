class Dispatch:
    """
    Handles job creation, raw material validation,
    and machine assignment.
    """

    def _init_(self):
        """Initialize raw materials, ovens and job queue."""
        pass

    def check_raw_material(self, qty):
        """Check whether enough raw material is available."""
        pass

    def consume_raw_material(self, qty):
        """Reduce raw materials after job creation."""
        pass

    def create_job(self, qty):
        """Create a production job."""
        pass

    def assign_machine(self):
        """Assign job to a free oven."""
        pass