import time

class Dispatch:
    """
    Handles job creation, raw material validation,
    machine assignment for biscuit production.
    """

    def _init_(self):
        # Available raw materials in grams
        pass

    def check_raw_material(self, qty):
        """Check whether enough raw materials exist for given quantity."""
        pass

    def consume_raw_material(self, qty):
        """Reduce raw material after job creation."""
        pass

    def create_job(self, qty):
        """Create a production job."""
        pass

    def assign_machine(self):
        """Assign free oven to next job in queue."""
        pass