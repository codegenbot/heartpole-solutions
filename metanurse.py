import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.55 or time_since_slept > 4:
        return 3  # Sleep to address health issues proactively
    if alertness < 0.75 and hypertension < 0.15 and intoxication < 0.05:
        return 1  # Drink coffee to boost alertness if safe
    if time_since_slept > 2.5 and time_elapsed > 15:
        return 3  # Sleep regularly to maintain health
    return 0  # Default action is working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)