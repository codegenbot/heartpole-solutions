import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep threshold adjustment for hypertension/intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if sleep deprived
    if time_since_slept > 4:
        return 3

    # Use coffee if it won't push hypertension too high
    if alertness < 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Choose work if conditions are satisfactory
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.03:
        return 0

    # Use beer if well-performing and at low risk
    if work_done > 20 and alertness > 0.7 and hypertension < 0.03 and intoxication < 0.01:
        return 2

    # Default to working to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)