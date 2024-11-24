import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize immediate sleep if necessary
    if alertness < 0.5 or hypertension > 0.6 or intoxication >= 0.3 or time_since_slept > 5:
        return 3  # Prioritize sleep
    
    # Use coffee when moderate alertness level and health risks are low
    if 0.5 <= alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.25:
        return 1  # Drink coffee and work

    # Use work if alertness is high and health factors are low
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Use beer if intoxication and hypertension are in lower range
    if intoxication < 0.2 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)