import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest for concerning health conditions
    if hypertension > 0.2 or intoxication > 0.2:
        return 3  # Sleep

    # Sleep if alertness is very low or long time since last sleep
    if alertness < 0.4 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee strategically early on, when alertness can still be improved
    if alertness < 0.6 and time_elapsed < 5:
        return 1  # Drink coffee and work

    # Allow beer for a slight morale boost only if almost done and it's safe
    if work_done > 0.9 and intoxication < 0.05 and time_elapsed > 6:
        return 2  # Drink beer and work

    # Default to just work if conditions are stable and alertness is decent
    if alertness >= 0.7 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleep as a fallback otherwise
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)