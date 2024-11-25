import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If alertness is low or health issue thresholds are crossed, prioritize sleep
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep

    # If alertness is optimal and health parameters are under control, work
    if alertness > 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness, safe hypertension levels, and controlled intoxication encourage coffee
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # If hypertension and intoxication are medium, relax with beer
    if 0.4 < hypertension <= 0.5 and intoxication <= 0.2:
        return 2  # Drink beer and work

    # Default to sleep if criteria for other actions are not met
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)