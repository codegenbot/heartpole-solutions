import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.65 or intoxication > 0.25 or time_since_slept >= 5:
        return 3  # Sleep
        
    if alertness < 0.75 and hypertension <= 0.4 and intoxication <= 0.05:
        return 1  # Coffee and work
        
    if alertness >= 0.75 and hypertension <= 0.55 and intoxication <= 0.1:
        return 0  # Just work

    if intoxication <= 0.1:
        return 0  # Default to just work

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)