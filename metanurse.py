import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep conditions prioritizing health
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Prioritize sleep for recovery

    # Use coffee to increase alertness if hypertension and intoxication are low
    if 0.4 <= alertness < 0.6 and hypertension < 0.15 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Optimal work condition
    if alertness >= 0.6 and hypertension < 0.2 and intoxication < 0.15:
        return 0  # Just work

    # Default to work if conditions aren't critical but not optimal
    return 0  # Default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)