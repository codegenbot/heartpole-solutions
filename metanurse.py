import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.75 or intoxication >= 0.55:
        return 3

    if time_since_slept >= 8 or (hypertension >= 0.65 and time_since_slept >= 6):
        return 3

    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.25:
        return 0

    if 0.4 < alertness < 0.8 and hypertension < 0.5:
        return 1

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)