import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical hypertension or intoxication
    if hypertension > 0.7 or intoxication > 0.3:
        return 3
    
    # Sleep if alertness is low or it's been too long since last sleep
    if alertness < 0.4 or time_since_slept > 12:
        return 3

    # Coffee only in moderate hypertension/intoxication states to boost early work capacity
    if alertness < 0.7 and time_elapsed < 8 and work_done < 0.3 and hypertension < 0.4 and intoxication < 0.2:
        return 1

    # Favor work if conditions are reasonable
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 0

    # Default to sleep at night or for recovery
    if time_elapsed >= 16 or time_elapsed < 6:
        return 3

    # Default to sleep to maintain longer-term health
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)