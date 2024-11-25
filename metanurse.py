import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is very low or health metrics are critical
    if alertness < 0.4 or time_since_slept > 10 or hypertension > 0.8:
        return 3  # Sleep

    # Work safely when conditions are optimal
    if alertness > 0.8 and hypertension < 0.2 and intoxication == 0.0:
        return 0  # Just work

    # Use coffee to boost alertness moderately
    if 0.6 <= alertness < 0.8 and hypertension < 0.5 and intoxication == 0.0:
        return 1  # Drink coffee and work

    # Only use beer if alertness is low but health is relatively stable
    if alertness < 0.4 and hypertension < 0.5 and intoxication < 0.05:
        return 2  # Drink beer and work

    # Default to sleeping if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)