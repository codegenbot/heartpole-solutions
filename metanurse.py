import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If very low alertness or risky health indicators, prioritize sleep
    if alertness < 0.2 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Sleep

    # Productive conditions with safe limits
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Work

    # Moderate alertness: use coffee moderately
    if 0.4 <= alertness < 0.8 and hypertension < 0.5:
        return 1  # Coffee and work

    # Maintain low intoxication; use beer only if safe
    if alertness < 0.4 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Beer and work

    # Default action to maintain balance
    return 3  # Sleep by default if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)