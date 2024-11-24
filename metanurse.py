import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 7:
        return 3  # Sleep

    # High alertness with stable conditions
    if alertness > 0.7 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work

    # Moderate alertness, coffee can boost productivity
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Low alertness but safe hypertension and intoxication
    if 0.4 < alertness < 0.5 and hypertension < 0.3 and intoxication < 0.1:
        return 2  # Drink beer and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)