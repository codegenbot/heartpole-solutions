import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Sleep is prioritized for safety
    if alertness < 0.5 and hypertension <= 0.7 and intoxication <= 0.2:
        return 1  # Drink coffee to boost low alertness if health parameters are within limits
    if alertness >= 0.8 and hypertension < 0.6 and intoxication <= 0.1:
        return 0  # Conditions are optimal for working
    if 0.5 <= alertness < 0.8 and hypertension < 0.7 and intoxication < 0.3:
        return 0  # Work is feasible when conditions are manageable
    if hypertension <= 0.5 and intoxication <= 0.3:
        return 2  # Drink beer if hypertension is manageable to relieve stress
    return 3  # Sleep by default if none of the above conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)