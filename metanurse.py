import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any serious threshold is reached
    if alertness < 0.4 or hypertension >= 0.02 or intoxication > 0.1 or time_since_slept >= 6:
        return 3
    # Use coffee if alertness is moderately low, and hypertension is manageable
    if 0.4 <= alertness < 0.6 and hypertension < 0.015:
        return 1
    # Consider beer if hypertension and intoxication are low and more relaxation is needed
    if 0.6 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.05:
        return 2
    # Continue working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)