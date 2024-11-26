import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep
    if alertness < 0.65 or hypertension > 0.07 or intoxication > 0.04 or time_since_slept >= 3.5:
        return 3  # More aggressive in choosing to sleep for recovery

    # Safe coffee consumption to boost alertness
    if alertness < 0.75 and hypertension < 0.03:
        return 1  # Slightly more tolerant with alertness level with safe hypertension

    # Controlled beer consumption for balance
    if 0.7 <= alertness < 0.8 and hypertension <= 0.05 and intoxication <= 0.015:
        return 2  # Adjust intoxication factor for safer beer choice

    # Default productive action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)