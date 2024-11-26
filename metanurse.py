import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate need to sleep in case of serious health risks
    if hypertension > 0.02 or intoxication > 0.02 or alertness < 0.25:
        return 3

    # Proactive sleep to maintain alertness
    if time_since_slept > 2.5 or (alertness < 0.3 and time_since_slept > 2):
        return 3

    # Use coffee strategically for maintaining alertness with low hypertension
    if alertness < 0.3 and hypertension < 0.02:
        return 1

    # Work if alertness suffices and no immediate risks are present
    if alertness >= 0.40:
        return 0

    # Default to just work if coffee can't be taken and other conditions don't trigger
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)