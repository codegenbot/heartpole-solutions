import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # If any severe health concern, prioritize sleep
    if (
        time_since_slept > 8
        or alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.6
    ):
        return 3  # Sleep

    # Use Coffee only when alertness is slightly low but not compromising health
    if 0.3 <= alertness < 0.5 and hypertension <= 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Maintain productive work mode if conditions allow
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    # If other measures aren't possible, rest is default for recovery
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)