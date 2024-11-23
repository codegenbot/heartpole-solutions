import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8:
        return 3  # Ensure rest after long periods without sleep
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # High health risk indicators, sleep
    if hypertension > 0.5 and hypertension <= 0.7:
        return 3  # Moderate hypertension needs attention
    if intoxication > 0.3:
        return 3  # Sleep to reduce even moderate intoxication levels
    if alertness < 0.4 and hypertension <= 0.5:
        return 1  # Drink coffee if alertness is low
    if work_done < 0.7 and alertness >= 0.5:
        return 0  # Work if conditions are appropriate
    return 0  # Default to working if no conditions are triggered

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)