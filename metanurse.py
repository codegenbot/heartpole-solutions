import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.6 or time_since_slept > 8:
        return 3
    if hypertension > 0.55:
        return 3
    if intoxication >= 0.25:
        return 3
    if 0.15 <= intoxication < 0.25 and alertness > 0.7:
        return 2
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.15:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)