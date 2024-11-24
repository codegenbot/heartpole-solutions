import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritizing health: Sleep if necessary
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 5:
        return 3  # Prioritize sleep

    # Use coffee when alertness is moderate but avoid it if hypertension or intoxication is rising
    if 0.4 <= alertness < 0.6 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Favor working if alertness is high and health indicators are low
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Just work

    # Consider beer if intoxication is low and it can help reduce stress mildly
    if 0.2 < intoxication < 0.3 and hypertension < 0.5:
        return 2  # Drink beer and work

    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)