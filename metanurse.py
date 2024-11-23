import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strong health checks
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep for safety
    if time_since_slept > 12 or alertness < 0.3:
        return 3  # Critical need for sleep
    
    # Strategic productivity
    if alertness < 0.5 and hypertension < 0.25:
        return 1  # Drink coffee to boost alertness and work

    # Begin to favor rest over productivity when reaching risky scores
    if alertness < 0.4 and time_since_slept > 8:
        return 3  # Select sleep over further caffeine use

    # Default healthy working conditions
    if alertness >= 0.6 and hypertension <= 0.2 and intoxication <= 0.15:
        return 0  # Continue work

    # Abstain if conditions are too risky
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)