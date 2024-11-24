import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.35 or hypertension > 0.65 or intoxication > 0.45 or time_since_slept >= 8:
        return 3  # Sleep

    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work

    if 0.5 <= alertness <= 0.8 and hypertension < 0.55 and intoxication < 0.35:
        return 1  # Drink coffee and work

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)