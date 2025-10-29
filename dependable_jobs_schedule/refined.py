from collections import defaultdict, deque

def finish_all(number_of_jobs, jobs_list):

    def get_start_points(list_of_points):
        # WRONG: This function tries to derive "start points" by filtering EDGES,
        # using whether a job appears as the FIRST element (dependent) and then
        # keeping edges whose SECOND element (prerequisite) is not among those.
        # This mixes roles and returns EDGES, not JOBS. It also ignores jobs that
        # never appear in any pair (independent jobs).
        #
        # We keep this for reference/debug only.

        discard_numbers = []
        for num in range(number_of_jobs):  # FIX (partial): iterate job labels, not edge indices
            for point in list_of_points:
                if point[0] == num:
                    discard_numbers.append(num)

        keep_edges = [item for item in list_of_points if item[1] not in discard_numbers]
        print("\nDEBUG(get_start_points - edge-centric ‘starts’):", keep_edges)

        # FIX: Compute *true* start JOBS (indegree == 0), for your understanding.
        # This is what a correct algorithm uses to begin processing.
        all_jobs = set(range(number_of_jobs))
        jobs_that_depend_on_others = {a for (a, _b) in list_of_points}  # jobs appearing as FIRST (dependents)
        true_start_jobs = sorted(all_jobs - jobs_that_depend_on_others)  # jobs with no prerequisites
        print("DEBUG(get_start_points - true start jobs):", true_start_jobs)

        # Return the old edge-based "keep_edges" only so the existing caller doesn't break.
        # NOTE: The final correctness decision below will NOT rely on this.
        return keep_edges

    def check_jobs(current_job_list, job_to_check):
        # WRONG (fragile approach):
        # 1) Mutates current_job_list while iterating/recursing → can skip elements.
        # 2) Blocks only the exact reverse pair [a,b] vs [b,a] (detects 2-cycles),
        #    but misses longer cycles (e.g., 0→1→2→0).
        # 3) Works on EDGES instead of JOBS; outcome depends on incidental order/content.
        # Kept for reference + your debug prints, but not used for the final decision.
        completed_jobs = [job for job in current_job_list if job[1] == job_to_check[0]]
        for job_to_remove in completed_jobs:
            if job_to_check != job_to_remove[::-1]:
                print("conducting check... (edge removed by fragile method)")
                current_job_list.remove(job_to_remove)
            check_jobs(current_job_list, job_to_remove)

    # Step 1: show debug info for your old get_start_points idea
    start_points = get_start_points(jobs_list)

    # =========================================================
    # FIX: Robust decision using Kahn’s topological sort on JOBS
    # =========================================================
    print("\n========== BUILD GRAPH ==========")
    outgoing_edges_from_job = defaultdict(list)   # job -> list of jobs that depend on it
    indegree_count = [0] * number_of_jobs         # job -> number of prerequisites it still needs
    print("Initial indegree_count:", indegree_count)

    for dependent_job, prerequisite_job in jobs_list:
        outgoing_edges_from_job[prerequisite_job].append(dependent_job)
        indegree_count[dependent_job] += 1
        print(f"Added dependency: {prerequisite_job} -> {dependent_job}")
        print("Current outgoing_edges_from_job:", dict(outgoing_edges_from_job))
        print("Current indegree_count:", indegree_count)

    print("\n========== INITIAL QUEUE ==========")
    queue = deque([job for job in range(number_of_jobs) if indegree_count[job] == 0])
    print("Jobs with no prerequisites (start jobs):", list(queue))

    processed_job_count = 0
    step = 1

    print("\n========== PROCESSING LOOP ==========")
    while queue:
        print(f"\nStep {step}: Current queue (ready jobs):", list(queue))
        job_done = queue.popleft()  # take the first job that’s ready
        print(f"Processing job: {job_done}")
        processed_job_count += 1
        print("Processed job count:", processed_job_count)

        # Show the jobs that this one unlocks
        print(f"Jobs unlocked when {job_done} completes:", outgoing_edges_from_job[job_done])

        # For every job that depends on this one, reduce its remaining prerequisites
        for unlocked_job in outgoing_edges_from_job[job_done]:
            indegree_count[unlocked_job] -= 1
            print(f"  Reduced indegree of job {unlocked_job} → now {indegree_count[unlocked_job]}")
            if indegree_count[unlocked_job] == 0:
                queue.append(unlocked_job)
                print(f"  Job {unlocked_job} is now ready → added to queue")

        print("Queue after this step:", list(queue))
        print("Current indegree_count:", indegree_count)
        step += 1

    print("\n========== FINAL DECISION ==========")
    print("Total jobs processed:", processed_job_count, "/", number_of_jobs)
    can_finish_all_jobs = (processed_job_count == number_of_jobs)
    print("Processed all jobs? →", can_finish_all_jobs)

    if can_finish_all_jobs:
        print("Output: True")
    else:
        print("Output: False")


# =========================
# Your original print tests
# =========================
finish_all(2, [[1, 0]])
finish_all(2, [[1, 0], [0, 1]])
finish_all(3, [[1, 0], [2, 1]])
finish_all(1, [])
finish_all(11, [[6, 10], [4, 3], [9, 2], [2, 3], [6, 1], [2, 8], [10, 1], [10, 2], [5, 3], [0, 10], [7, 4], [6, 1]])
finish_all(3, [[1,0],[2,1],[0,2]])
