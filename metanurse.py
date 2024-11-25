import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or hypertension > 0.8 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep if at least one condition is risky

    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work if alert and relatively healthy

    if 0.5 <= alertness <= 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Coffee and work if alertness needs a boost and health is acceptable

    if intoxication > 0.2:
        return 2  # Drink beer if intoxication to simulate a break or decompression

    return 3  # Default to sleep for safety if no other conditions are met well

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)