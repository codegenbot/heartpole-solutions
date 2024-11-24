import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low, time since sleep is high, or health risks are present
    if alertness <= 0.4 or hypertension >= 0.6 or intoxication >= 0.5 or time_since_slept > 5:
        return 3  # Sleep to recover and manage health

    # If alertness is high, continue working
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.5:
        return 0  # Just work

    # Drink coffee if alertness is moderate to high with low health risks
    if 0.4 < alertness <= 0.8 and hypertension < 0.5 and intoxication < 0.5:
        return 1  # Drink coffee and work

    # Default action if conditions are alertness moderate-low and hypertension is low
    return 3  # Default to sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)