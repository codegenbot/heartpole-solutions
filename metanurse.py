import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health indicators are critical
    if alertness < 0.3 or hypertension > 0.25 or intoxication > 0.25 or time_since_slept > 6:
        return 3
    
    # Work if conditions are optimal
    if alertness >= 0.6 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0
    
    # If below optimal alertness and working conditions met, drink coffee
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.05 and time_since_slept <= 5:
        return 1

    # If work done is low and mildly relaxed state, allow a break
    if work_done < 0.2 and alertness > 0.5 and hypertension < 0.1 and intoxication < 0.05:
        return 2

    # Default to sleep to reset if conditions aren't optimal or understood
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)