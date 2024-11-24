import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health parameters:
    if alertness < 0.8 or time_since_slept > 6:
        return 3
    if hypertension > 0.4 or intoxication > 0.25:
        return 3
    
    # Balance productivity:
    if alertness < 0.9 and hypertension <= 0.3 and intoxication < 0.1:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)