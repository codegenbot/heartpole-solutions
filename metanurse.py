import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.3 or hypertension > 0.65 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee to boost alertness, but consider hypertension limits
    if 0.4 <= alertness < 0.6 and hypertension < 0.5 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Sufficient alertness, safe to work
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.05:
        return 0  # Just work

    # If alertness is moderate and intoxication is low, manage productivity with beer
    if 0.3 <= alertness < 0.6 and intoxication <= 0.15:
        return 2  # Drink beer and work

    return 3  # Default to sleep for safety and recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)