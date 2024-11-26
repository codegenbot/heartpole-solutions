import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any serious threshold is reached
    if alertness < 0.5 or hypertension >= 0.02 or intoxication > 0.1 or time_since_slept >= 8:
        return 3
    # Use coffee if alertness is low and hypertension is manageable
    if 0.5 <= alertness < 0.7 and hypertension < 0.015:
        return 1
    # Drink beer if intoxication is low and time since last sleep isn't critical
    if intoxication <= 0.05 and time_since_slept < 6:
        return 2
    # Continue working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)