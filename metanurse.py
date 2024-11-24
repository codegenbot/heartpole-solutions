import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep is prioritized if alertness is low, hypertension or intoxication is high, or lack of sleep is evident
    if alertness < 0.5 or hypertension > 0.4 or intoxication > 0.25 or time_since_slept >= 4:
        return 3  # Sleep
    
    # Use coffee if alertness is slightly low but within manageable health limits
    if 0.5 <= alertness < 0.65 and hypertension <= 0.35 and intoxication < 0.2:
        return 1  # Coffee and work

    # Just work when all conditions are optimal
    if alertness >= 0.65 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work
    
    # Use beer when alertness is moderate but conditions allow for slight relaxation
    if 0.5 <= alertness < 0.55 and intoxication <= 0.1 and hypertension <= 0.35:
        return 2  # Drink beer and work

    # Default to working if conditions are manageable but not ideal for other actions
    return 0  # Just work if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)