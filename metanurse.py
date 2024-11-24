import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 9:
        return 3  # Prioritize sleep for health recovery
    if alertness < 0.5:
        return 3  # Sleep if alertness is critically low
    if alertness < 0.7 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Use coffee to boost alertness when health allows
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work when all conditions are relatively safe
    return 2  # Use beer even more sparingly


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)