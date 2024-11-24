import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 4:
        return 3  # Prioritize sleep

    # Use coffee only when alertness is low and other indicators are safe
    if 0.5 <= alertness < 0.7 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee

    # Prefer working when alertness is high and health indicators are normal
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # Avoid beer unless stress indicators low, relying more on sleep or coffee
    if 0.2 < intoxication < 0.3 and hypertension < 0.5:
        return 2  # Drink beer

    return 3  # Default to sleep to prevent serious health risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)