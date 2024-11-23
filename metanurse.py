import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # sleep to address health concerns
    if time_since_slept > 8:
        return 3  # sleep if too much time has passed without rest
    if alertness < 0.4:
        if alertness < 0.2:
            return 3  # sleep if alertness is very low
        return 1  # drink coffee and work
    if time_elapsed > 10 and work_done < 0.7:
        return 0  # just work to manage tasks within sustainable hours
    return 0  # just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)