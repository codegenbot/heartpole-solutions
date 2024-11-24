import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when alertness is critically low or health indicators are too high
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Sleep

    # Use coffee strategically when alertness is moderate and health conditions are safe
    if alertness < 0.6 and hypertension <= 0.3 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Encourage work when alertness is high and health indicators are within safe limits
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Use beer cautionarily to recover from slight declines in alertness while managing intoxication
    if 0.5 <= alertness < 0.6 and intoxication < 0.3 and hypertension < 0.5:
        return 2  # Drink beer and work

    # Default to sleep as a safe fallback
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)