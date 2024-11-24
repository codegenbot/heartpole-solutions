import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or hypertension >= 0.25 or intoxication >= 0.1 or time_since_slept >= 6:
        return 3
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.05:
        return 1
    if 0.15 <= hypertension < 0.25 and intoxication < 0.05 and alertness >= 0.4:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)