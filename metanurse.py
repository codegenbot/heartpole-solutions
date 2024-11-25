import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5 or hypertension > 0.5 or alertness < 0.3 or intoxication > 0.6:
        return 3  # Sleep to restore health balance
    if alertness > 0.85 and hypertension < 0.35 and intoxication < 0.15:
        return 0  # Work if all parameters indicate a healthy state
    if alertness < 0.4 and hypertension < 0.4 and intoxication < 0.4:
        return 1  # Drink coffee when alertness needs a boost
    if intoxication > 0.4 and alertness < 0.4:
        return 2  # Drink beer to mitigate intoxication when alertness is low
    return 0  # Default to work when safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)