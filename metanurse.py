import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep with slightly less strict conditions to allow more work
    if (
        alertness < 0.4
        or hypertension > 0.6
        or intoxication > 0.5
        or time_since_slept > 14
    ):
        return 3  # Sleep to ensure no health risks are ignored

    # Allow more work without coffee if the health indicators are positive
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work when health metrics are optimal

    # Use coffee more liberally if conditions are not critical, boost alertness
    if 0.4 <= alertness < 0.8 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Coffee and work when alertness needs aid

    # Avoid beer for better health management; fallback to sleep to maintain balance
    return 3  # Default to sleep for conservative health management


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)