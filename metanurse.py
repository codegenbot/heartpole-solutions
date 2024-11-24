import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 5 or hypertension >= 0.5 or intoxication >= 0.4:
        return 3
    if alertness < 0.7 and hypertension < 0.45 and intoxication < 0.35:
        return 1
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.25:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)