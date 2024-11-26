import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.05 or intoxication >= 0.10:
        return 3
    if time_since_slept >= 6:
        return 3

    if alertness < 0.5:
        if hypertension < 0.04 and intoxication < 0.06:
            return 1
        return 3

    if 0.6 <= alertness < 0.75 and hypertension < 0.02 and intoxication < 0.02:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)