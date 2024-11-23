import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for severe hypertension or intoxication
    if hypertension > 0.3 or intoxication > 0.2:
        return 3
    
    # Sleep if alertness is low or significant time has passed since last sleep
    if alertness < 0.6 or time_since_slept > 10:
        return 3

    # Use coffee early when work done is low and alertness needs boosting
    if alertness < 0.7 and time_elapsed < 6 and work_done < 0.2:
        return 1

    # Work if optimal conditions are met
    if alertness >= 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 0

    # Default to sleep to avoid health issues
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)