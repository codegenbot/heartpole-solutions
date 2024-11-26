import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept >= 4.5 or alertness < 0.4:
        return 3

    if intoxication > 0.06 or hypertension > 0.04:
        return 3

    if alertness < 0.6 and hypertension < 0.02:
        return 1

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)