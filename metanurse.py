import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health indicators suggest fatigue
    if alertness < 0.5 or time_since_slept > 4.5 or hypertension > 0.5:
        return 3  # Sleep

    # Optimal condition to only work
    if alertness > 0.85 and hypertension < 0.25 and intoxication < 0.01:
        return 0  # Just work

    # Encouraging coffee when moderate alertness and acceptable health conditions
    if 0.6 <= alertness <= 0.85 and hypertension < 0.4 and intoxication < 0.02:
        return 1  # Drink coffee and work

    # Only drink beer if alertness needs boosting but with very low intoxication
    if 0.5 <= alertness < 0.6 and intoxication < 0.005 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default to sleeping in ambiguous situations for health safety
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)