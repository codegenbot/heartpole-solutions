import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.08 or intoxication > 0.3:
        return 3  # Urgently sleep to mitigate high health risks

    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep to recharge and maintain health

    if alertness < 0.6 and intoxication < 0.1:
        return 1  # Coffee and work to boost alertness without much intoxication
    
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.2:
        return 0  # Work when conditions allow without additional stimulants

    return 0  # Default to working as fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)