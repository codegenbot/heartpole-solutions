import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep more strongly
    if alertness < 0.5 or time_since_slept > 5.0:
        return 3
    
    # Respond aggressively to health hazards
    if hypertension > 0.02:
        return 3
    if intoxication > 0.02:
        return 3
    
    # Use coffee more cautiously
    if 0.5 <= alertness < 0.7 and hypertension <= 0.015:
        return 1

    # Consider careful beer use to maximize productivity with high alertness
    if alertness >= 0.7 and intoxication <= 0.005 and hypertension <= 0.015:
        return 2

    # Default to working if conditions are generally favorable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)