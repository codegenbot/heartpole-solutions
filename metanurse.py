import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious health risks
    if hypertension > 0.02 or intoxication > 0.02 or alertness < 0.25:
        return 3

    # Sleep if prolonged wakefulness or low alertness
    if time_since_slept > 4 or alertness < 0.4:
        return 3

    # Drink coffee if alertness is moderate and health indicators are safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.015:
        return 1

    # Work if alertness is high, otherwise default to cautious work
    if alertness >= 0.6:
        return 0

    return 0  # Default to work, safeguards handled prior

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)