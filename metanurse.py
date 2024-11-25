import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when health metrics demand rest or alertness is severely low
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    # Work under safe conditions with optimal alertness
    if alertness > 0.75 and hypertension < 0.35 and intoxication < 0.05:
        return 0  # Just work

    # Drink coffee when alertness is moderate and no hypertension issues
    if 0.4 <= alertness <= 0.75 and hypertension < 0.55:
        return 1  # Drink coffee and work

    # Default to a more conservative approach for health maintenance
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)