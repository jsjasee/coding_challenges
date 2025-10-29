def finish_all(number_of_jobs, jobs_list):

    def get_start_points(list_of_points):
        discard_numbers = []
        # number_of_points = len(list_of_points) - 1 # number of points IS NOT the number of itmes in the list!!
        for num in range(number_of_jobs):
            # find the elements to be the start points to start checking. These start points have numbers which did not appear in the first item of any lists!
            for point in list_of_points:
                if point[0] == num:
                    discard_numbers.append(num)

        keep = [item for item in list_of_points if item[1] not in discard_numbers]
        print(number_of_jobs, keep)
        return keep

    def check_jobs(current_job_list, job_to_check):
        completed_jobs = [job for job in current_job_list if job[1] == job_to_check[0]]
        for job_to_remove in completed_jobs:
            # print(f"dependent job found: {job_to_remove}")
            if job_to_check != job_to_remove[::-1]:
                print("conducting check...")
                # this only removes the job if the job is NOT a circular one, aka [a,b] & [b,a], when we flip [b,a] we get [a,b]
                current_job_list.remove(job_to_remove)
            # print(current_job_list)
            check_jobs(current_job_list, job_to_remove)


    start_points = get_start_points(jobs_list)

    for start_point in start_points:
        # print(f"Starting with: {start_point}")
        if start_point in jobs_list:
            # we need this if-statement in case the other start point is already checked by the previous start point,
            # eg. in the case of 2 jobs, [2,1] and [1,0], if we start from [1,0], then the dependent job [2,1] will already be checked and removed from the jobs list
            jobs_list.remove(start_point)
        check_jobs(jobs_list, start_point)

        # This below block is used to structure the recursion function.
        # for job in jobs_list:
        #     if job[1] == start_point[0]:
        #         print(f"dependent job found: {job}")
        #         jobs_list.remove(job)
        #         for second_job in jobs_list:
        #             if second_job[1] == job[0]:
        #                 print(f"next dependent job found: {second_job}")
        #                 jobs_list.remove(second_job)

    # print(jobs_list)
    if not jobs_list:
        print("Output: True")
    else:
        print("Output: False")


finish_all(2, [[1, 0]])
finish_all(2, [[1, 0], [0, 1]])
finish_all(3, [[1, 0], [2, 1]])
finish_all(1, [])
finish_all(11, [[6, 10], [4, 3], [9, 2], [2, 3], [6, 1], [2, 8], [10, 1], [10, 2], [5, 3], [0, 10], [7, 4], [6, 1]])
finish_all(3, [[1,0],[2,1],[0,2]])
finish_all(4, [[1,0],[2,0],[3,1],[3,2]])  # 0→1, 0→2, and both → 3
finish_all(4, [[1,0],[2,1],[0,2]])