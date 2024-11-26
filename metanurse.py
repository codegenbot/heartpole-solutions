import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Tighter control on health indicators
    if hypertension > 0.03 or intoxication > 0.07:
        return 3
    if time_since_slept > 6.0:
        return 3

    # Offer better productivity decisions with stricter health constraints
    if alertness < 0.6 and hypertension < 0.025 and intoxication < 0.025:
        return 1

    # Make beer an even lower priority
    if alertness < 0.5 and intoxication < 0.03 and hypertension < 0.015:
        return 2

    # Allow work if health indicators are largely normal
    if alertness >= 0.75 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    return 3  # Default to rest for safe recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)