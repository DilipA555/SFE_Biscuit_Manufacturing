from dispatch import Dispatch
from realtime import RealTime
from quality import Quality
import time

# ---------- Raw Material Stock ----------
raw_material = {
    "flour": 20000,
    "sugar": 8000,
    "butter": 6000,
    "milk_powder": 3000,
    "baking_powder": 500,
    "salt": 300,
    "essence": 1000
}

# ---------- Per Biscuit Requirement ----------
per_biscuit = {
    "flour": 6,
    "sugar": 2.5,
    "butter": 2,
    "milk_powder": 0.8,
    "baking_powder": 0.2,
    "salt": 0.1,
    "essence": 0.4
}

# ---------- Machines ----------
ovens = {
    "Oven_1": "free",
    "Oven_2": "free",
    "Oven_3": "free"
}

dispatch = Dispatch(raw_material, per_biscuit, ovens)
realtime = RealTime()
quality = Quality()

production_queue = []
completed_queue = []

while True:

    print("\n===== Biscuit Manufacturing System =====")
    print("1. Create & Assign Job")
    print("2. Start Production")
    print("3. Quality Check")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

# ======================================================
# CREATE JOB
# ======================================================
    if choice == "1":

        qty = int(input("Enter biscuit quantity: "))
        print("\nChecking raw materials...")
        time.sleep(5)

        if dispatch.check_raw_material(qty):
            dispatch.consume_raw_material(qty)
            print("\nCreating job...")
            time.sleep(5)
            job = dispatch.create_job(qty)
            time.sleep(3)

            print("\nAssigning to machine...")
            time.sleep(5)
            oven, assigned_job = dispatch.assign_machine()
            if assigned_job:
                production_queue.append((oven, assigned_job))
                print("Job moved to production queue")
            else:
                print("All machines are busy -> Job waiting inside dispatch queue")

        else:
            print("Insufficient raw materials")

# ======================================================
# START PRODUCTION
# ======================================================
    elif choice == "2":

        if production_queue:
            oven, job = production_queue.pop(0)
            print(f"\nStarting production for Job {job['job_id']} in {oven}")
            time.sleep(5)
            target, produced = realtime.start_production(job)
            print("\nProduction in progress...")
            time.sleep(10)
            print("\nProduction is completed, evaluate the metrics.")
            time.sleep(3)
            print("\nEvaluating the metrics...")
            time.sleep(5)
            downtime, utilisation, defects = realtime.calculate_metrics(target, produced)
            print("\nFetching production summary...")
            time.sleep(5)
            realtime.show_summary(target, produced, downtime, utilisation)
            completed_queue.append((job, produced, defects))
            dispatch.ovens[oven] = "free"
            time.sleep(3)
            print(f"\n{oven} is now FREE")
            time.sleep(3)

            # AUTO ASSIGN NEXT JOB FROM DISPATCH INTERNAL QUEUE
            next_oven, next_job = dispatch.assign_machine()
            time.sleep(3)

            if next_job:
                production_queue.append((next_oven, next_job))

            # SHOW REMAINING
            if production_queue:
                print("\nJobs waiting for production:")
                for oven, j in production_queue:
                    print(f"Job {j['job_id']}")

        else:
            print("\nFirst create & assign job")

# ======================================================
# QUALITY CHECK
# ======================================================
    elif choice == "3":

        if completed_queue:

            job, produced, defects = completed_queue.pop(0)

            print("\n------Batch Summary------")
            print("Job id", job["job_id"])
            print("Target:", job["quantity"])
            print("Produced:", produced)
            print("Defects:", defects)
            time.sleep(5)

            print(f"\nQuality checking for Job {job['job_id']} in progress...")
            time.sleep(5)

            produced, defects = quality.check_quality(produced, defects)

            if completed_queue:
                time.sleep(3)
                print("\nBatches waiting for quality check:")
                for j, _, _ in completed_queue:
                    print(f"Job {j['job_id']}")

        else:
            print("\nProduction not completed yet for quality check")

# ======================================================
    elif choice == "4":
        print("\nExited from the system")
        break

    else:
        print("Invalid choice")