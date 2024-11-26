import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if intoxication > 0.12 or hypertension > 0.025 or time_since_slept >= 8:
        return 3
    if alertness < 0.5 or (time_since_slept >= 6 and alertness < 0.55):
        return 3
    if alertness < 0.7 and hypertension < 0.025 and intoxication < 0.08:
        return 1
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.08:
        return 0
    if intoxication >= 0.08 and hypertension < 0.02:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)