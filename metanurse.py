import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health
    if time_since_slept > 7 or hypertension > 0.7 or alertness < 0.3:
        return 3  # Sleep in these cases

    # Safely work when fully alert and in good health
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.02:
        return 0  # Just work

    # Use coffee to boost productivity cautiously
    if alertness >= 0.5 and hypertension < 0.5 and intoxication <= 0.02:
        return 1  # Drink coffee and work

    # Relax without serious health risk
    if alertness < 0.5 and intoxication == 0.0 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)