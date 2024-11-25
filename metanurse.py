import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or health metrics are outside safe bounds
    if alertness < 0.5 or hypertension > 0.65 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Optimal conditions for working continue without intervention
    if alertness > 0.85 and hypertension < 0.35 and intoxication < 0.05:
        return 0  # Just work

    # Use coffee strategically for moderate alertness improvement
    if alertness <= 0.6 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Default to sleep if no other conditions match to ensure rest
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)