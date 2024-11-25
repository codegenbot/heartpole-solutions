import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with more conservative thresholds
    if alertness < 0.5 or time_since_slept > 6 or hypertension > 0.5:
        return 3  # Sleep

    # Work without additional substances if health indicators are optimal
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.05:
        return 0  # Just work safely

    # Use coffee only if alertness is middling but health supports
    if 0.6 <= alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Avoid beer to maintain health, optional: use if absolutely necessary
    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)