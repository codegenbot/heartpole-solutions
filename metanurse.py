import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if alertness is very low, time since slept is high, or intoxication is critical
    if time_since_slept > 8 or alertness < 0.3 or intoxication >= 0.1:
        return 3
    
    # Use coffee if alertness is low-medium and health markers allow it
    if 0.3 <= alertness < 0.55 and hypertension < 0.02 and intoxication <= 0.04:
        return 1

    # Optimal to work if alertness is adequate and health conditions are not critical
    if alertness >= 0.6 and hypertension < 0.03 and intoxication < 0.05:
        return 0
    
    # Default to work if no critical need for sleep or coffee
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)