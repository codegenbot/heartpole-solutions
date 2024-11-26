import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators reach less strict levels
    if hypertension > 0.05 or intoxication > 0.1:
        return 3
    if time_since_slept > 6.5:  # Ensure regular rest
        return 3

    # Use coffee or beer more conservatively and only when really needed
    if alertness < 0.6 and hypertension < 0.03 and intoxication < 0.03:
        return 1

    if alertness < 0.5 and intoxication < 0.05:
        return 2

    # Work only when alertness is adequately high
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    return 3  # Default to rest if conditions don't favor productivity

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)