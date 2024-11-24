import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep more strictly
    if alertness < 0.6 or hypertension > 0.65 or intoxication > 0.3 or time_since_slept > 4:
        return 3  # Sleep
    
    # Use coffee under slightly stricter conditions
    if alertness < 0.7 and hypertension < 0.35 and intoxication < 0.1:
        return 1  # Coffee and work

    # Just work if all conditions are good
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Use beer selectively if intoxication is very low
    if intoxication < 0.15 and hypertension > 0.5:
        return 2  # Drink beer and work

    return 3  # Default to sleep if conditions are suboptimal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)