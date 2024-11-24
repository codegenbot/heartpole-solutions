import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.2 and time_since_slept < 6:
        return 1  # Drink coffee and work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work
    if alertness < 0.7 and intoxication < 0.2 and hypertension < 0.5:
        return 2  # Drink beer and work
    return 3  # Default to sleep for any ambiguous state

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)