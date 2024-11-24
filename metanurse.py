import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.5 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Use coffee wisely when alertness is moderate and pressure is manageable
    if 0.5 <= alertness < 0.65 and hypertension <= 0.55 and intoxication <= 0.25:
        return 1  # Drink coffee

    # Work when alert and healthy
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.25:
        return 0  # Just work

    # Use beer when it can safely lower hypertension slightly without increasing intoxication too much
    if 0.25 < intoxication < 0.35 and hypertension < 0.5:
        return 2  # Drink beer

    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)