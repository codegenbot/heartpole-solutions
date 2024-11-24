import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for recovery if severe health concerns or very low alertness
    if hypertension > 0.30 or intoxication > 0.30 or time_since_slept > 6:
        return 3
    # Drink coffee to boost low alertness while keeping safe health indicators
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.10:
        return 1
    # Work more often if alertness is above moderate and no severe health indicators
    if alertness >= 0.6 and hypertension < 0.15 and intoxication < 0.10:
        return 0
    # Allow beer if work is progressing well and health is reasonably good
    if work_done > 5 and alertness > 0.5 and intoxication < 0.15:
        return 2
    # Default to working if conditions are not met for specific actions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)