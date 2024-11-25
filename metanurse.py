import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or alertness < 0.4 or hypertension > 0.6:
        return 3  # Sleep if needing rest or high hypertension

    if alertness >= 0.7 and hypertension < 0.3 and intoxication == 0.0:
        return 0  # Safely work

    if alertness >= 0.5 and hypertension < 0.5 and intoxication < 0.05:
        return 1  # Drink coffee and work when moderately alert

    if 0.3 <= alertness < 0.5 and intoxication == 0.0 and hypertension < 0.4:
        return 2  # Drink beer to relax only when alertness is low and not intoxicated

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)