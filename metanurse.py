import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is critically low or not slept for a long period
    if alertness < 0.3 or time_since_slept > 8:
        return 3
    
    # Use coffee after alertness drops, but ensure hypertension is controlled
    if alertness < 0.6 and hypertension < 0.2:
        return 1
    
    # Rarely use beer unless intoxication is almost negligible
    if alertness < 0.4 and intoxication < 0.1 and time_since_slept <= 5:
        return 2

    # Work without supplements in good conditions
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0

    # Default working condition if no immediate recovery required
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)