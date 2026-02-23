class InsufficientRawMaterialError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class NoOvenAvailableError(Exception):
    pass

class Dispatch:
    """
    Handles job ceation, raw material validation,
    machine assignment for biscuit production.
    """

    MAX_BATCH_SIZE = 100

    def __init__(self,raw_material: dict[str,int], per_biscuit: dict[str,float | int], ovens:dict[str,str])->None:
        # Available raw materials in grams
        self.raw_material = raw_material
        # Required grams per biscuit
        self.per_biscuit = per_biscuit
        # Oven status
        self.ovens = ovens
        self.queue = []
        self.job_id = 1

    def check_raw_material(self, qty:int)->None:
        """Check whether enough raw materials exist for given quantity."""

        if qty <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")

        for item in self.per_biscuit:
            if item not in self.raw_material:
                raise KeyError(f"{item} missing in raw material inventory")

            required = self.per_biscuit[item] * qty

            if self.raw_material[item] < required:
                raise InsufficientRawMaterialError(
                    f"Not enough {item}. Required: {required}, "
                    f"Available: {self.raw_material[item]}"
                )

        return True

    def consume_raw_material(self, qty:int)->None:
        """Reduce raw material after job creation."""

        for item in self.per_biscuit:
            self.raw_material[item] -= self.per_biscuit[item] * qty

    def create_job(self, qty:int)->dict[str:int]:
        """Create a production job."""

        try:
            self.check_raw_material(qty)

            batches = []
            remaining = qty

            while remaining > 0:
                batch_qty = min(remaining, self.MAX_BATCH_SIZE)

                job = {
                    "job_id": self.job_id,
                    "quantity": batch_qty
                }

                self.queue.append(job)
                batches.append(job)

                self.job_id += 1
                remaining -= batch_qty

            self.consume_raw_material(qty)

            print(f"{len(batches)} job(s) created successfully.")
            return batches

        except (InvalidQuantityError,
                InsufficientRawMaterialError,
                KeyError) as e:

            print(f"Job creation failed → {e}")
            return []


    def assign_machine(self)-> tuple[dict[str,str],dict[str,int]]|None:
        """Assign free oven to next job in queue."""

        try:
            if not self.queue:
                raise ValueError("No jobs in queue")

            for oven in self.ovens:
                if self.ovens[oven] == "free":

                    job = self.queue.pop(0)
                    self.ovens[oven] = "busy"

                    print(f"Job {job['job_id']} assigned to {oven}")
                    return oven, job

            raise NoOvenAvailableError("All ovens are busy")

        except (ValueError, NoOvenAvailableError) as e:
            print(f"Dispatch failed → {e}")
            return None, None