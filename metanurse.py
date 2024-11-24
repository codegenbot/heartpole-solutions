import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 8 or hypertension > 0.55 or intoxication >= 0.45:
        return 3
    if alertness < 0.7 and hypertension <= 0.5 and intoxication < 0.3:
        return 1
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)