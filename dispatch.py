class Dispatch:
    """
    Handles job creation, raw material validation,
    machine assignment for biscuit production.
    """

    def __init__(self,raw_material, per_biscuit, ovens):
        # Available raw materials in grams
        self.raw_material = raw_material
        # Required grams per biscuit
        self.per_biscuit = per_biscuit
        # Oven status
        self.ovens = ovens
        self.queue = []
        self.job_id = 1

    def check_raw_material(self, qty):
        """Check whether enough raw materials exist for given quantity."""

        for item in self.per_biscuit:
            required = self.per_biscuit[item] * qty
            if self.raw_material[item] < required:
                print(f"\nNot enough {item}")
                return False

        print("\nRaw materials sufficient")
        return True

    def consume_raw_material(self, qty):
        """Reduce raw material after job creation."""

        for item in self.per_biscuit:
            self.raw_material[item] -= self.per_biscuit[item] * qty

    def create_job(self, qty):
        """Create a production job."""

        job = {"job_id": self.job_id, "quantity": qty}
        self.queue.append(job)
        self.job_id += 1
        print(f"Job created → {job}")
        return job


    def assign_machine(self):
        """Assign free oven to next job in queue."""

        for oven in self.ovens:
            if self.ovens[oven] == "free" and self.queue:
                job = self.queue.pop(0)
                self.ovens[oven] = "busy"
                print(f"Job {job['job_id']} assigned to {oven}")
                print("\nDispatching completed.")
                return oven, job
        return None, None