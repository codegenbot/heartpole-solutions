import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping when alertness is significantly low or after a long duration awake
    if alertness < 0.5 or time_since_slept >= 7:
        return 3  # Sleep

    # Drink coffee to boost alertness when it's moderate, with controlled hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.6 and intoxication <= 0.2:
        return 1  # Coffee and work

    # Opt to work if alertness levels are high and health parameters are favorable
    if alertness >= 0.7 and hypertension <= 0.4:
        return 0  # Just work

    # Allow beer only if needing a quick alertness adjustment in low-risk settings
    if alertness < 0.5 and intoxication <= 0.1:
        return 2  # Beer and work

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)