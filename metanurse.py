import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.05 or intoxication > 0.05:
        return 3
    
    if time_since_slept > 4.0:
        return 3

    if alertness < 0.75 and hypertension <= 0.02:
        return 1

    if alertness >= 0.75 and intoxication <= 0.02:
        return 0

    if alertness >= 0.7 and intoxication > 0.02 and intoxication <= 0.04:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)