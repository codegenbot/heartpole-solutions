import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If extremely low alertness or risky health indicators, prioritize sleep
    if alertness < 0.3 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Sleep

    # Productive conditions with safe health limits
    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Work

    # Use coffee if moderately alert and hypertension is controlled
    if 0.4 <= alertness <= 0.7 and hypertension < 0.5:
        return 1  # Coffee and work

    # Conserve resources, only use beer if safe
    if alertness < 0.4 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Beer and work

    # Default action to maintain health balance
    return 3  # Sleep by default if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)