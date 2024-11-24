import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.25 or hypertension > 0.9 or intoxication > 0.5 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Use coffee to boost alertness while keeping within hypertension & intoxication limits
    if alertness < 0.5 and hypertension <= 0.65 and intoxication <= 0.4:
        return 1  # Drink coffee

    # Prefer work if alertness is high and health markers are safe
    if alertness >= 0.55 and hypertension <= 0.55 and intoxication <= 0.3:
        return 0  # Just work

    # Consider drinking beer if it can help stress with minimal risk increase
    if hypertension <= 0.7 and intoxication < 0.5:
        return 2  # Drink beer wisely

    return 3  # Default to sleep as a safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)