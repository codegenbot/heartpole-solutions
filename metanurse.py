import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept >= 6.0:
        return 3

    if intoxication > 0.05 or hypertension > 0.04:
        return 3

    if alertness < 0.6 and hypertension <= 0.02:
        return 1

    if 0.5 <= alertness < 0.7 and intoxication <= 0.03:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)