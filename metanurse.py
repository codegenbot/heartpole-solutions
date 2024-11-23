import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to prevent critical health issues
    if (
        alertness < 0.4
        or hypertension > 0.6
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3  # Sleep more often to recover

    # Use coffee to boost alertness if conditions are safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Coffee boost safely

    # Work under reasonable conditions
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Optimal work conditions

    # Default action to work if no conditions for sleep or coffee are hit
    return 0  

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)