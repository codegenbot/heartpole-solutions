def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.015 or intoxication >= 0.08:
        return 3
    if alertness < 0.55 or time_since_slept >= 6:
        return 3
    if alertness < 0.75 and hypertension < 0.010 and intoxication < 0.04:
        return 1
    return 0


import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)