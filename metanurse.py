import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep

    # High alertness with stable conditions
    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness, safe to use coffee
    if 0.5 <= alertness <= 0.8 and hypertension < 0.5 and intoxication < 0.15:
        return 1  # Drink coffee and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)