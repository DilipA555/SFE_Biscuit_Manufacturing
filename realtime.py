import random
class RealTime:
    """
    Handles production execution,
    downtime tracking and utilisation.
    """

    def start_production(self, job):
        """Start production for assigned job."""

        target = job["quantity"]
        produced = random.randint(int(target*0.85),target)
        return target,produced

    def calculate_metrics(self, target, produced):
        """Calculate downtime, utilisation and defects."""

        downtime = random.randint(1,5)
        utilisation = (produced/target) * 100
        defects = target - produced
        return downtime, utilisation, defects

    def show_summary(self, target, produced, downtime, utilisation):
        """Display production summary."""

        print("\n------Production Summary------")
        print("\nTarget:", target)
        print("Produced:", produced)
        print("Downtime:", downtime, "mins")
        print("Utilisation:", round(utilisation, 2), "%")
        print("\nRealtime tracking completed ")
        
