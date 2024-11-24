import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.4 or hypertension > 0.55 or intoxication > 0.35 or time_since_slept > 6:
        return 3  # Sleep

    # High alertness with stable conditions
    if alertness > 0.75 and hypertension < 0.35 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness, coffee can boost productivity without health risks
    if 0.5 <= alertness <= 0.75 and hypertension < 0.45 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Low alertness close to safe hypertension and intoxication thresholds
    if 0.45 < alertness < 0.5 and hypertension < 0.35 and intoxication < 0.05:
        return 2  # Drink beer and work

    # Default to sleep for safety
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)