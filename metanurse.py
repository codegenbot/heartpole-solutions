import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.45 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 5:
        return 3  # Prioritize sleep

    # Use coffee only when alertness is moderately low and at safe levels
    if 0.45 <= alertness < 0.6 and hypertension <= 0.55 and intoxication <= 0.25:
        return 1  # Drink coffee

    # Prefer working naturally when alertness is high and health indicators are normal
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # Avoid beer when intoxication is already rising
    if 0.2 < intoxication < 0.3 and hypertension < 0.55:
        return 2  # Drink beer
    
    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)