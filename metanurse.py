import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or hypertension > 0.6 or alertness < 0.2:
        return 3  # Sleep to restore health
    if alertness > 0.8 and hypertension < 0.4 and intoxication <= 0.05:
        return 0  # Work only when in optimal condition
    if alertness < 0.6 and hypertension < 0.3 and intoxication <= 0.1:
        return 1  # Drink coffee if more alertness is needed without high intoxication
    if 0.4 <= alertness < 0.7 and hypertension < 0.2 and intoxication < 0.05:
        return 2  # Drink beer under safe conditions
    return 0  # Default to work if none of the above conditions hold

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)