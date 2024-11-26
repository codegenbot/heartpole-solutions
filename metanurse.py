import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Priority 1: Health
    if alertness < 0.6 or time_since_slept > 6.0:
        return 3
    if hypertension > 0.05 or intoxication > 0.05:
        return 3
    # Priority 2: Improving productivity when health is stable
    if alertness < 0.75 and hypertension <= 0.02 and intoxication <= 0.02:
        return 1
    if intoxication <= 0.02 and hypertension <= 0.02:
        return 0
    if alertness < 0.85 and intoxication <= 0.03:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)