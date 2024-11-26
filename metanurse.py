import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or time_since_slept >= 5 or intoxication > 0.10:
        return 3  # Sleep to recover alertness, reduce time since slept, and intoxication
    if alertness < 0.5:
        return 1  # Drink coffee when alertness is low, but not critically low
    if alertness >= 0.8 and intoxication < 0.05 and hypertension < 0.03:
        return 0  # Work normally when conditions are sufficiently healthy
    if 0.5 <= alertness < 0.8 and intoxication < 0.08 and hypertension < 0.02:
        return 2  # Drink beer when alertness is moderate and health indicators are slightly raised
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)