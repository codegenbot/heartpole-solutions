import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness and health parameters suggest so
    if alertness < 0.6 or hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 10:
        return 3  # Sleep
    
    # Consider taking coffee if alertness is marginally low and conditions are stable
    if alertness >= 0.6 and alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work
    
    # Avoid beer if intoxication is noticeable
    if intoxication > 0.1:
        return 0  # Just work

    # Default to just working to maintain productivity
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)