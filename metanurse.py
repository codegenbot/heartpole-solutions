import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if necessary
    if time_since_slept > 6 and (alertness < 0.5 or hypertension > 0.6 or intoxication > 0.3):
        return 3  # Sleep
    
    # Use coffee when more alertness is needed but within safe health parameters
    if alertness < 0.5 and hypertension <= 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Regular work if health indicators are within optimal range
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Fall back to sleep if in doubt or under risky conditions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)