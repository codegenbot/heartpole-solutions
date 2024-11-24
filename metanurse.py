import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical necessity for sleep
    if hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Sleep

    # Moderate necessity for sleep
    if alertness < 0.3 or time_since_slept > 6:
        return 3  # Sleep

    # Balance between productivity and health
    # Work if alertness is high and health indicators are safe
    if alertness >= 0.6 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work

    # Drink coffee to boost productivity slightly without health risk
    if 0.4 <= alertness < 0.6 and hypertension < 0.4 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Consider resting to recover from mild stress or intoxication
    if alertness < 0.5 or hypertension > 0.5 or intoxication > 0.35:
        return 3  # Sleep

    return 0  # Default to just work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)