import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 7:
        return 3  # Sleep to recover health
    if alertness < 0.5 and hypertension < 0.1 and intoxication < 0.05 and time_since_slept <= 5:
        return 1  # Drink coffee to boost productivity when safe
    if time_elapsed > 10 and work_done < 0.5:
        return 0  # Just work, sufficient time to correct course
    return 0  # Default action is to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)