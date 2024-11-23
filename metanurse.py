import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Priority checks for serious health issues
    if hypertension > 0.6 or intoxication > 0.3:
        return 3  # Sleep due to significant health issues
    # Encourage sleep for maintaining balanced alertness
    if alertness < 0.5 or time_since_slept > 8:
        return 3  # Sleep if alertness is low or awake too long
    # Use coffee for boosting alertness cautiously
    if 0.5 <= alertness < 0.7 and time_since_slept <= 6:
        return 1  # Drink coffee and work if beneficial
    # Work more if alert and work is not yet sufficient
    if alertness >= 0.8 and work_done < 0.9:
        return 0  # Just work if alert
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)