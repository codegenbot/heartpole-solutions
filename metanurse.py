import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Use coffee only when alertness is moderately low but within safe levels
    if alertness < 0.55 and hypertension <= 0.55 and intoxication <= 0.3:
        return 1  # Drink coffee

    # Prefer working with optimal alertness and safe hypertension
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.25:
        return 0  # Just work

    # Use beer sparingly, only when slightly stressed but not intoxicated
    if hypertension < 0.6 and intoxication < 0.4:
        return 2  # Drink beer wisely

    return 3  # Default to sleep as a safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)