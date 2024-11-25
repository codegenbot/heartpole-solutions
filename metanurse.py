import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep on poor conditions
    if alertness < 0.3 or hypertension > 0.80 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Need sleep

    # Productive conditions: prioritize work
    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness: carefully use coffee
    if 0.5 <= alertness < 0.85 and hypertension < 0.65 and intoxication < 0.2:
        return 1  # Coffee and work

    # If very low alertness and low hypertension and intoxication, fallback to beer
    if alertness < 0.5 and hypertension < 0.5 and intoxication < 0.15:
        return 2  # Beer and work

    # Default to sleep to ensure recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)