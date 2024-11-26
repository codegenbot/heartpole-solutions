import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or hypertension > 0.06 or intoxication > 0.07 or time_since_slept >= 8.0:
        return 3
    if alertness < 0.5 and hypertension <= 0.03:
        return 1
    if 0.5 <= alertness < 0.65 and intoxication <= 0.03 and hypertension <= 0.02:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)