import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # High priority to handle sleep if necessary
    if alertness < 0.5 or hypertension > 0.1 or intoxication > 0.1 or time_since_slept >= 5:
        return 3

    # Use coffee more liberally to maintain productivity
    if alertness < 0.7 and hypertension < 0.06 and intoxication < 0.06:
        return 1

    # Work when health is optimal
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Use beer minimally if beneficial for productivity and low intoxication
    if alertness < 0.4 and hypertension < 0.07 and intoxication <= 0.03:
        return 2

    # Default to working if conditions are acceptable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)