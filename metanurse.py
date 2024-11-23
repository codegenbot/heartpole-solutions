import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep conditions based on health and alertness
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 5:
        return 3  # Prioritize sleep for recovery if low alertness or high health risk

    # Coffee strategy for moderate alertness without high hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.2:
        return 1  # Coffee intake allowed when conditions are safe

    # Beer to control hypertension if slightly high, ensure alcohol tolerance
    if 0.4 < hypertension <= 0.5 and intoxication < 0.1:
        return 2  # Control hypertension with beer if safe to drink

    # Continue working if conditions are optimal
    if alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 0  # Continue working under ideal conditions

    # Default action (when no other actions are optimal)
    return 0  # Default to work if no immediate health issue detected

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)