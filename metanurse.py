import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.6 or time_since_slept >= 4 or intoxication >= 0.1:
        return 3
    if alertness < 0.7 and hypertension < 0.03:
        return 1
    if 0.7 <= alertness < 0.75 and intoxication < 0.05 and hypertension < 0.02:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)