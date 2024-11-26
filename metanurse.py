import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for very high-risk hypertension or intoxication
    if hypertension > 0.015 or intoxication > 0.07:
        return 3
    
    # Mandatory sleep if alertness is low or sleep deprivation is high
    if alertness < 0.6 or time_since_slept > 3:
        return 3
    
    # Drink coffee to boost alertness if still in safe ranges
    if alertness < 0.8 and hypertension < 0.012 and intoxication < 0.03:
        return 1

    # Default to just work if everything is balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)