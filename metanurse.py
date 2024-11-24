import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 7:
        return 3  # Sleep

    if alertness > 0.75 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work

    if 0.45 <= alertness <= 0.75 and hypertension < 0.55 and intoxication < 0.35:
        return 1  # Drink coffee and work

    if hypertension > 0.55 or intoxication > 0.35:
        return 3  # Sleep to recover from high stress/intoxication

    return 2  # Drink beer and work as last resort if no critical health flags

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)