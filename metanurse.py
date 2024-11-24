import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.9 or intoxication > 0.9 or time_since_slept > 16:
        return 3  # Sleep

    if alertness < 0.3 and hypertension < 0.7 and intoxication < 0.4:
        return 1  # Drink coffee and work
    
    if alertness >= 0.7 and hypertension < 0.6 and intoxication < 0.3:
        return 0  # Just work
    
    if intoxication < 0.5 and hypertension < 0.6 and 6 <= time_since_slept <= 10:
        return 2  # Drink beer and work

    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)