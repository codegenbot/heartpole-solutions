import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # If any critical condition exists, prioritize sleep
    if alertness < 0.4 or hypertension > 0.75 or intoxication > 0.45 or time_since_slept > 10:
        return 3  # Need sleep

    # Optimal condition just for work
    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.15:
        return 0  # Just work

    # Use coffee to maintain productivity
    if 0.6 <= alertness < 0.85 and hypertension < 0.7 and intoxication < 0.25:
        return 1  # Coffee and work

    # Use beer only if alertness is notably low
    if alertness < 0.6 and intoxication < 0.3 and hypertension < 0.5:
        return 2  # Beer and work

    # When in doubt, prefer sleep to ensure health
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)