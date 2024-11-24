import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with stricter conditions
    if alertness < 0.6 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee only with very low intoxication
    if alertness < 0.8 and hypertension < 0.5 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Just work if in optimal conditions
    if alertness >= 0.8 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # Use beer carefully when needed to reduce hypertension
    if intoxication <= 0.25 and hypertension > 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)