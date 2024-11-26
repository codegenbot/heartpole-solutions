import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk hypertension or intoxication
    if hypertension > 0.015 or intoxication > 0.07:
        return 3
    
    # Mandatory sleep if near dangerously low alertness or excess deprivation
    if time_since_slept > 4.5 or alertness < 0.5:
        return 3
    
    # Consider reducing coffee intake to keep indicators balanced
    if alertness < 0.7 and hypertension < 0.015 and intoxication < 0.02:
        return 1

    # Stop work if productivity is sufficient
    if work_done > 0.8:
        return 3

    # Default work to continue productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)