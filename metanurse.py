import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if serious health risks are detected
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee to boost alertness while managing hypertension
    if 0.5 <= alertness < 0.7 and hypertension <= 0.2 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # High alertness and low intoxication yields work focus
    if alertness >= 0.6 and intoxication <= 0.1:
        return 0  # Just work

    # Default to sleep if none of the above conditions apply
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)