import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest for any elevated health risk
    if hypertension > 0.35 or intoxication > 0.35:
        return 3  # Sleep

    # Rest if significantly tired or alertness is concerningly low
    if alertness < 0.5 or time_since_slept > 12:
        return 3  # Sleep

    # Use coffee strategically for moderate fatigue early in the day
    if alertness < 0.7 and time_elapsed < 4:
        return 1  # Drink coffee and work

    # Default to work if conditions are reasonably stable
    if alertness > 0.6 and hypertension < 0.25 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleeping if unsure
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)