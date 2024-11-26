import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is too low or if it's been too long since slept
    if alertness < 0.7 or time_since_slept >= 8:
        return 3
    
    # Avoid actions if hypertension is above a low threshold
    if hypertension > 0.03:
        return 3
    
    # If alertness is moderate and manageable hypertension, use coffee
    if alertness < 0.8 and hypertension <= 0.02:
        return 1
    
    # Use beer if alertness is sufficient, minimal intoxication, and low hypertension
    if 0.5 <= alertness < 0.9 and intoxication == 0 and hypertension <= 0.01:
        return 2
    
    # If all conditions are acceptable, just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)