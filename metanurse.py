import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.6 or time_since_slept >= 5:
        return 3
    if hypertension >= 0.01 or intoxication > 0.08:
        return 3
    if 0.6 <= alertness < 0.75 and hypertension < 0.01:
        return 1
    if 0.75 <= alertness < 0.85 and intoxication < 0.05:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)