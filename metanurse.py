import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for low alertness or if it's been too long without sleep
    if alertness < 0.5 or time_since_slept >= 8.0:
        return 3
    
    # If hypertension is high, avoid actions that could exacerbate it
    if hypertension > 0.06:
        return 3
    
    # Use coffee sparingly if alertness is moderately low and hypertension allows
    if 0.5 <= alertness < 0.7 and hypertension <= 0.05:
        return 1

    # Use beer cautiously only if intoxication is zero and slight alertness boost is needed
    if 0.6 <= alertness < 0.8 and intoxication == 0 and hypertension <= 0.04:
        return 2

    # Default to working if all conditions are within comfortable thresholds
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)