import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.35 or intoxication > 0.3 or time_since_slept > 10:
        return 3  # Sleep
    if alertness < 0.5 and hypertension <= 0.25:
        return 1  # Drink coffee and work when slightly less alert
    if work_done > 30 and intoxication < 0.2:
        return 2  # Relax with beer
    if alertness >= 0.6 and intoxication <= 0.1 and time_since_slept <= 8:
        return 0  # Just work if in good condition
    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)