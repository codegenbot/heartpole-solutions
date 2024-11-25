import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 12 or alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep
    if 0.5 < hypertension <= 0.7 and intoxication <= 0.6:
        return 2  # Drink beer and work to slightly reduce hypertension
    if alertness >= 0.6 and hypertension < 0.6 and intoxication < 0.4:
        return 0  # Just work
    if 0.35 <= alertness < 0.6 and hypertension < 0.7 and intoxication < 0.5:
        return 1  # Drink coffee and work
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)