import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 10 or alertness < 0.5:
        return 3  # Sleep
    
    if hypertension > 0.15 or intoxication > 0.06:
        return 3  # Sleep

    if alertness < 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    if alertness >= 0.9 and hypertension <= 0.05 and intoxication < 0.02:
        return 2  # Drink beer and work

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)