import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for concerning hypertension or intoxication
    if hypertension > 0.01 or intoxication > 0.05:
        return 3
    
    # Mandatory sleep if alertness is low or sleep deprivation higher
    if alertness < 0.6 or time_since_slept > 4:
        return 3
    
    # Drink coffee to boost alertness if still in safe ranges
    if alertness < 0.7 and hypertension < 0.01 and intoxication < 0.03:
        return 1

    # Default to just work if conditions are balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)