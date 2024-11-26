import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for critical conditions
    if time_since_slept >= 6 or hypertension > 0.05 or intoxication > 0.15:
        return 3
    # Lower threshold to prompt action before severe conditions
    if alertness < 0.5:
        return 3
    # Allow coffee only if alertness is mid-range and time since slept is managed
    if 0.5 <= alertness < 0.7 and time_since_slept < 4:
        return 1
    # Allow beer in relaxed conditions
    if 0.7 <= alertness < 0.8 and hypertension < 0.02 and intoxication < 0.05:
        return 2
    # Default action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)