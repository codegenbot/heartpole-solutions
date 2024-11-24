import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 10:
        return 3  # Sleep
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work
    if intoxication < 0.35 and hypertension < 0.5 and 6 <= time_since_slept <= 9:
        return 2  # Drink beer and work
    return 3  # Default to Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)