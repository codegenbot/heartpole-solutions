import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any indicators suggest a significant health risk
    if alertness < 0.5 or hypertension > 0.5 or intoxication > 0.2 or time_since_slept >= 6:
        return 3  # Sleep
    
    # Use coffee only with moderate alertness and low hypertension/intoxication
    if 0.5 <= alertness < 0.65 and hypertension <= 0.35 and intoxication <= 0.05:
        return 1  # Coffee and work

    # Just work if conditions are optimal
    if alertness >= 0.65 and hypertension <= 0.45 and intoxication <= 0.1:
        return 0  # Just work

    # Default to working if conditions are somewhat suboptimal but manageable
    return 0  # Just work if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)