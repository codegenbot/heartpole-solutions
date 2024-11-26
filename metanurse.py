import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strongly prioritize sleep if deeply below healthy thresholds
    if alertness < 0.5 or hypertension >= 0.015 or intoxication > 0.07 or time_since_slept >= 5:
        return 3
    # Use coffee if alertness is low, with caution on hypertension
    if alertness < 0.7 and hypertension < 0.012:
        return 1
    # Opt for relaxation with beer if both hypertension and intoxication are low
    if 0.7 <= alertness < 0.9 and hypertension < 0.008 and intoxication < 0.04:
        return 2
    # Default to working if health parameters are stable and productive
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)