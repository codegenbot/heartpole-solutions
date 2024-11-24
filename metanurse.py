import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with stricter conditions
    if alertness < 0.65 or hypertension > 0.65 or intoxication > 0.3 or time_since_slept >= 5:
        return 3  # Sleep

    # Use coffee more effectively
    if alertness < 0.75 and hypertension < 0.5 and intoxication <= 0.15:
        return 1  # Coffee and work

    # Just work if in optimal conditions
    if alertness >= 0.8 and hypertension <= 0.45 and intoxication <= 0.2:
        return 0  # Just work

    # Use beer very cautiously
    if intoxication <= 0.2 and hypertension > 0.5:
        return 2  # Drink beer and work

    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)