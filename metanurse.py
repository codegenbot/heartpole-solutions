import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Health Risk Avoidance
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Strategically use coffee to boost alertness if safe
    if alertness < 0.5 and hypertension <= 0.6 and intoxication <= 0.2:
        return 1  # Drink coffee

    # Safe and productive state
    if alertness >= 0.6 and hypertension <= 0.7:
        return 0  # Just work

    # Consider beer to manage moderate stress levels
    if hypertension < 0.65 and intoxication < 0.3:
        return 2  # Drink beer wisely

    return 3  # Default to sleep as a safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)