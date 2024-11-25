import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.6
        or hypertension > 0.05
        or intoxication > 0.04
        or time_since_slept >= 2.5
    ):
        return 3  # Sleep when alertness or health indicators are concerning

    if 0.6 <= alertness < 0.8 and hypertension < 0.04 and intoxication < 0.03:
        return 1  # Drink coffee to maintain moderate alertness safely

    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.02:
        return 0  # Work efficiently under optimal conditions

    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.3:
        return 2  # Use beer only when productivity is extremely low

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)