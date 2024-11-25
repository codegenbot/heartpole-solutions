import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for critical health issues
    if hypertension > 0.2 or intoxication > 0.12:
        return 3
    # Rest if moderately fatigued or long time without sleep
    if alertness < 0.65 or time_since_slept > 6:
        return 3
    # Drink coffee for moderate alertness with strict health conditions
    if alertness < 0.7 and hypertension < 0.15 and intoxication < 0.08:
        return 1
    # Default to just working (avoid beer)
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)