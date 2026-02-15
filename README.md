# Biscuit Manufacturing System

This project is a console-based application that shows the complete flow of a biscuit manufacturing process.

It starts with checking raw materials and creating a production job.  
If an oven is free, the job is assigned automatically.  
If all ovens are busy, the job waits in the queue and gets assigned when a machine becomes available.

Production is done in the same order as the jobs are created.  
After production, each batch goes through quality checking where it is either approved or sent for rework based on the defect percentage.

The system prints clear step-by-step messages so the user can easily understand what is happening at each stage.

---

## How to Run

1. Download or clone the repository  
2. Open the project folder in the terminal  
3. Run:

bash
python main.py


---

## Menu Options

1. Create & Assign Job  
2. Start Production  
3. Quality Check  
4. Exit  

---

## Process Flow

- Raw materials are checked before creating a job  
- Job is assigned to a free oven automatically  
- If all ovens are busy, the job waits in the queue  
- Production runs in sequence  
- Completed batches move to quality check  
- Batches are approved or sent for rework  

---

## Project Structure

- main.py – Controls the overall flow and user interaction  
- dispatch.py – Handles job creation and oven assignment  
- realtime.py – Handles production and metrics  
- quality.py – Handles defect calculation and quality decision  

---