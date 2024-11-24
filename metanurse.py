import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any critical condition for health
    if alertness < 0.6 or hypertension > 0.6 or intoxication > 0.35 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is low and health metrics allow it
    if alertness < 0.75 and hypertension < 0.5 and intoxication < 0.2 and time_since_slept <= 6:
        return 1

    # Work if alertness and other conditions are optimal
    if alertness >= 0.85 and hypertension < 0.4 and intoxication < 0.15:
        return 0

    # Drink beer if all health parameters are low risk
    if hypertension < 0.3 and intoxication < 0.3 and alertness > 0.65:
        return 2

    # Default to sleeping if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)