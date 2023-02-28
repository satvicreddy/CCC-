def job_sequence(jobs, deadlines):
    """
    A function that takes a list of jobs and their corresponding deadlines and returns the maximum profit
    that can be earned by scheduling the jobs before their respective deadlines.
    """
    # Sort the jobs by their profits in descending order
    sorted_jobs = sorted(zip(jobs, deadlines), key=lambda x: x[0], reverse=True)
    # Initialize the time and profit
    time, profit = 0, 0
    # Iterate through the sorted jobs
    for job, deadline in sorted_jobs:
        # If there is still time to complete the job before its deadline
        if deadline > time:
            # Add the profit to the total profit and update the time
            profit += job
            time += 1
    return profit
jobs = [35, 20, 25, 12, 15, 5]
deadlines = [3, 4, 4, 2, 3, 1]
print(job_sequence(jobs, deadlines))