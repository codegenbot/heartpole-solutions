import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # sleep
    if time_since_slept > 14:
        return 3  # sleep
    if alertness < 0.5:
        if alertness < 0.2:
            return 3  # sleep if alertness is very low
        return 1  # drink coffee and work
    return 0  # just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)