from dispatch import Dispatch
from realtime import RealTime
from quality import Quality
import time

# ---------- RAW MATERIAL STOCK ----------
raw_material = {
    "flour": 20000,
    "sugar": 8000,
    "butter": 6000,
    "milk_powder": 3000,
    "baking_powder": 500,
    "salt": 300,
    "essence": 1000
}

# ---------- PER BISCUIT REQUIREMENT ----------
per_biscuit = {
    "flour": 6,
    "sugar": 2.5,
    "butter": 2,
    "milk_powder": 0.8,
    "baking_powder": 0.2,
    "salt": 0.1,
    "essence": 0.4
}

# ---------- MACHINES ----------
ovens = {
    "Oven_1": "free",
    "Oven_2": "free",
    "Oven_3": "free"
}

dispatch = Dispatch(raw_material, per_biscuit, ovens)
realtime = RealTime()
quality = Quality()

production_queue = []
waiting_queue = []
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
        time.sleep(2)

        if dispatch.check_raw_material(qty):

            dispatch.consume_raw_material(qty)

            job = dispatch.create_job(qty)

            oven, assigned_job = dispatch.assign_machine()

            if assigned_job:
                production_queue.append((oven, assigned_job))
                print("Job moved to production queue")
            else:
                waiting_queue.append(job)
                print("Job added to waiting queue")

        else:
            print("Insufficient raw materials")

# ======================================================
# START PRODUCTION
# ======================================================
    elif choice == "2":

        if production_queue:

            oven, job = production_queue.pop(0)

            print(f"\nStarting production for Job {job['job_id']} in {oven}")
            time.sleep(2)

            target, produced = realtime.start_production(job)

            downtime, utilisation, defects = realtime.calculate_metrics(
                target, produced
            )

            realtime.show_summary(target, produced, downtime, utilisation)

            completed_queue.append((job, produced, defects))

            dispatch.ovens[oven] = "free"
            print(f"{oven} is now FREE")

# 🔁 AUTO ASSIGN FROM WAITING
            if waiting_queue:

                for free_oven, status in dispatch.ovens.items():

                    if status == "free":

                        next_job = waiting_queue.pop(0)

                        dispatch.ovens[free_oven] = "busy"

                        production_queue.append((free_oven, next_job))

                        print(f"Waiting Job {next_job['job_id']} now assigned to {free_oven}")
                        break

# SHOW REMAINING
            if production_queue:
                print("\nJobs waiting for production:")
                for oven, j in production_queue:
                    print(f"Job {j['job_id']}")

        else:
            print("First create & assign job")

# ======================================================
# QUALITY CHECK
# ======================================================
    elif choice == "3":

        if completed_queue:

            job, produced, defects = completed_queue.pop(0)

            print(f"\nQuality checking for Job {job['job_id']}")
            time.sleep(2)

            print("\nBatch Summary:")
            print("Target:", job["quantity"])
            print("Produced:", produced)
            print("Defects:", defects)

            produced, defects = quality.check_quality(produced, defects)

            if completed_queue:
                print("\n⏳ Batches waiting for quality check:")
                for j, _, _ in completed_queue:
                    print(f"Job {j['job_id']}")

        else:
            print("No completed production for quality check")

# ======================================================
    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")