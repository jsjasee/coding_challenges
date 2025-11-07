def bed_time(*args):
    rest_timings = []

    for wake_time in args:
        wake_hour_minutes = (int(wake_time[0].split(":")[0]), int(wake_time[0].split(":")[1]))
        rest_hour_minutes = (int(wake_time[1].split(":")[0]), int(wake_time[1].split(":")[1]))
        # print(wake_hour_minutes)
        # print(rest_hour_minutes)
        rest_time: list = []
        if wake_hour_minutes[0] - rest_hour_minutes[0] < 0:
            rest_time.append(24 + wake_hour_minutes[0] - rest_hour_minutes[0])
        else:
            rest_time.append(wake_hour_minutes[0] - rest_hour_minutes[0])

        if wake_hour_minutes[1] - rest_hour_minutes[1] < 0:
            rest_time[0] -= 1
            rest_time.append(60 + wake_hour_minutes[1] - rest_hour_minutes[1])
        else:
            rest_time.append(wake_hour_minutes[1] - rest_hour_minutes[1])

        # print(rest_time)
        # format the numbers into 2 dp
        rest_timings.append(f"{rest_time[0]:02d}:{rest_time[1]:02d}")

    print(rest_timings)


bed_time(["07:50", "07:50"])
# output = ["00:00"]
#
bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
# output = ["20:15", "22:00", "23:30"]
#
#
bed_time(["05:45", "04:00"], ["07:10", "04:30"])
# output = ["01:45", "02:40"]