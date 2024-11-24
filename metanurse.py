import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for health concerns
    if hypertension > 0.6 or intoxication > 0.35 or time_since_slept > 6:
        return 3  # Sleep
    # Use coffee if alertness is low but health is acceptable
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.25:
        return 1  # Drink coffee and work
    # Normal working conditions
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    # Occasionally use beer if slight alertness drop and conditions are safe
    if alertness >= 0.5 and intoxication < 0.15:
        return 2  # Drink beer and work
    return 1  # Default to working with coffee for mild alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)