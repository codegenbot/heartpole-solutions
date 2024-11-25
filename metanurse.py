import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6:
        return 3  # Sleep

    if hypertension > 0.7 or intoxication > 0.3:
        return 3  # Sleep

    if alertness < 0.5:
        return 3  # Sleep

    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    if 0.5 <= alertness <= 0.8 and hypertension < 0.4:
        return 1  # Drink coffee and work

    if 0.3 <= hypertension <= 0.5 and intoxication < 0.1:
        return 2  # Drink beer and work

    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)