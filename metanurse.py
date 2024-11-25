import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust sleep logic: more conservative recovery
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Need sleep

    # Productive condition for working
    if alertness > 0.85 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work

    # Adjust coffee logic for more frequent use
    if 0.45 <= alertness < 0.85 and hypertension < 0.7 and intoxication < 0.2:
        return 1  # Coffee and work

    # Adjust beer logic for effective recovery
    if alertness < 0.45 and hypertension < 0.5 and intoxication < 0.2:
        return 2  # Beer and work
    
    # Default to sleep to maintain recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)