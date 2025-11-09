# job
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to schedule jobs using a greedy approach
def job_sequencing(jobs):
    # Step counter
    steps = 0

    # Step 1: Sort all jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    steps += len(jobs)  # sorting comparisons count roughly as one per job

    # Step 2: Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    steps += 1

    # Step 3: Create a time slot list initialized with None
    slots = [None] * (max_deadline + 1)

    total_profit = 0
    job_sequence = []

    # Step 4: Schedule jobs
    for job in jobs:
        # Find a free slot for this job (starting from its deadline)
        for t in range(job.deadline, 0, -1):
            steps += 1  # count each slot check
            if slots[t] is None:
                slots[t] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit, steps


# ---- MAIN PROGRAM ----
n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job_id = input(f"Enter Job ID {i+1}: ")
    deadline = int(input(f"Enter Deadline for {job_id}: "))
    profit = int(input(f"Enter Profit for {job_id}: "))
    jobs.append(Job(job_id, deadline, profit))

sequence, profit, steps = job_sequencing(jobs)

print("\nOptimal Job Sequence:", sequence)
print("Total Profit:", profit)
print("Total Steps:", steps)

# Enter number of jobs: 4
# Enter Job ID 1: J1
# Enter Deadline for J1: 4
# Enter Profit for J1: 20
# Enter Job ID 2: J2
# Enter Deadline for J2: 1
# Enter Profit for J2: 10
# Enter Job ID 3: J3
# Enter Deadline for J3: 1
# Enter Profit for J3: 40
# Enter Job ID 4: J4
# Enter Deadline for J4: 1
# Enter Profit for J4: 30


# ### 🧾 **Definition:**

# **Job Sequencing with Deadlines** is a problem in which we are given a set of jobs.
# Each job has:

# * a **Deadline** → the latest time by which the job should be completed.
# * a **Profit** → the amount of profit earned if the job is completed within its deadline.

# The main **goal** is to schedule the jobs in such an order that:
# ✅ Every job finishes **before or on its deadline**, and
# ✅ The **total profit** earned from all selected jobs is **maximum**.

# ---

# ### ⚙️ **Explanation:**

# * We can perform **only one job at a time**.
# * We use a **Greedy Algorithm**, which means:

#   * First, choose the job that gives the **highest profit**.
#   * Then, assign it the **latest possible time slot** before its deadline (so we can leave earlier slots free for other jobs).
# * Repeat this process for all jobs.

# ---

# ### 💡 **Example:**

# | Job | Deadline | Profit |
# | --- | -------- | ------ |
# | J1  | 4        | 20     |
# | J2  | 1        | 10     |
# | J3  | 1        | 40     |
# | J4  | 1        | 30     |

# If we arrange jobs in decreasing profit order → **J3, J4, J1, J2**

# After scheduling, the best sequence is **J3 → J1**
# ✅ Total Profit = 40 + 20 = **60**

# ---

# ### 🧠 **Key Points:**

# * Uses **Greedy Method**.
# * Jobs are arranged in **descending order of profit**.
# * Each job is assigned a slot **just before or on its deadline**.
# * The aim is to **maximize profit** without missing deadlines.

# ---

# ### 🗣️ **Simple Definition to Remember:**

# > Job Sequencing with Deadlines is a scheduling method where we select and arrange jobs to get **maximum profit**, ensuring that each job is done **before its deadline** using a **greedy approach**.