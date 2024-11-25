import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if alertness is critically low or haven't slept for too long
    if alertness < 0.5 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is moderate and no significant hypertension risk
    if 0.5 <= alertness < 0.6 and hypertension < 0.03:
        return 1

    # Just work if alertness is adequately high and health is stable
    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.03:
        return 0

    # Default to a relaxed state with beer if other conditions don't apply
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)