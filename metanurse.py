import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health conditions necessitating sleep
    if (
        alertness < 0.4
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 10
    ):
        return 3  # Need sleep

    # Optimal conditions for just working
    if alertness > 0.7 and hypertension < 0.45 and intoxication < 0.05:
        return 0  # Just work

    # Coffee to enhance alertness with mild conditions
    if 0.4 <= alertness < 0.7 and hypertension < 0.6 and intoxication < 0.25:
        return 1  # Coffee and work

    # Use of beer should be rare; low intoxication limit
    if alertness < 0.5 and 0.05 < intoxication <= 0.2 and hypertension < 0.5:
        return 2  # Beer and work

    # Default action to maintain health and recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)