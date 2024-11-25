import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleeping if critically low alertness or high fatigue
    if alertness < 0.4 or time_since_slept > 6 or hypertension > 0.6:
        return 3  # Sleep

    # Preferred condition to just work
    if 0.8 <= alertness <= 1.0 and hypertension <= 0.25 and intoxication == 0.0:
        return 0  # Just work

    # Drink coffee when alertness is moderate and health indicators are acceptable
    if 0.5 <= alertness < 0.8 and hypertension < 0.4 and intoxication < 0.01:
        return 1  # Drink coffee and work

    # Avoid beer if intoxication is non-zero or if hypertension is concerning
    if 0.45 <= alertness < 0.5 and intoxication == 0.0 and hypertension < 0.3:
        return 2  # Drink beer and work

    # If conditions are not optimal, prioritize health by resting
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)