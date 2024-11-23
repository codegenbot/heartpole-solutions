import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust sleep criteria to ensure proactive rest
    if (
        alertness < 0.4
        or hypertension > 0.6
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3  # Sleep

    # Refine coffee usage for slight alertness boost, allow moderate hypertension
    if 0.4 <= alertness < 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Coffee and work

    # Optimize work condition to include a broader range for alertness
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Re-evaluate beer usage for mild tension relief
    if 0.4 <= hypertension < 0.6 and intoxication < 0.3:
        return 2  # Beer and work

    # Default work approach
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)