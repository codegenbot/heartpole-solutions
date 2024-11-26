import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Enhance health management by adjusting thresholds
    if hypertension > 0.02 or intoxication > 0.12:
        return 3  # sleep to avoid serious health risks
    
    if alertness < 0.35 or time_since_slept >= 7:
        return 3  # sleep if lacking alertness or rest
    
    if time_since_slept >= 6 or (0.35 <= alertness < 0.6 and hypertension < 0.015 and intoxication < 0.1):
        return 1  # coffee if needed for moderate alertness in safe thresholds
    
    return 0  # work if health parameters and alertness are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)