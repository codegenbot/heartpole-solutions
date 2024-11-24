import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for serious health conditions
    if (alertness < 0.4 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6):
        return 3
    # Drink coffee cautiously if conditions allow
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1
    # Work as default action if conditions are neutral
    if alertness >= 0.6 and hypertension < 0.65 and intoxication < 0.2:
        return 0
    # Consider a beer when stressed but not intoxicated
    if hypertension < 0.55 and intoxication < 0.15:
        return 2
    # Default to sleep if uncertain
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)