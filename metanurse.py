import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 7 or hypertension >= 0.6 or intoxication >= 0.5:
        return 3
    if alertness < 0.5 or time_since_slept > 5:
        return 3
    if alertness < 0.7 and hypertension < 0.5:
        return 1
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.25:
        return 0
    return 2 if intoxication < 0.3 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)