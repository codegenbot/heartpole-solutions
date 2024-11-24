import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.75 or intoxication > 0.5 or time_since_slept >= 7:
        return 3
    if alertness < 0.3:
        return 3
    if alertness < 0.65 and hypertension <= 0.65 and intoxication <= 0.25:
        return 1
    if alertness >= 0.75 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0
    if hypertension <= 0.6 and intoxication < 0.3:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)