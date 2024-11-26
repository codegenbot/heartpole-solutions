import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for low alertness or high time since slept
    if alertness < 0.6 or time_since_slept >= 6.0:
        return 3
    
    # Avoid working if hypertension is above a safe level
    if hypertension > 0.05:
        return 3
    
    # If alertness is low but hypertension is manageable, coffee can help
    if alertness < 0.7 and hypertension <= 0.04:
        return 1
    
    # Avoid beer if intoxication is not zero to not increase it
    if 0.5 <= alertness < 0.8 and intoxication == 0 and hypertension <= 0.03:
        return 2
    
    # Default action if conditions are acceptable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)