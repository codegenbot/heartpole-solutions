import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any critical condition for health or alertness
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 8:
        return 3

    # Drink coffee if alertness is low and health metrics allow it
    if alertness < 0.7 and hypertension < 0.6 and intoxication < 0.25 and time_since_slept <= 8:
        return 1

    # Work if alertness and other conditions are optimal
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0

    # Drink beer if all health parameters are low risk
    if hypertension < 0.4 and intoxication < 0.5:
        return 2

    # Default to sleeping if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)