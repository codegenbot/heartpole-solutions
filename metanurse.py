import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health conditions
    if hypertension > 0.15 or intoxication > 0.15:
        return 3  # Sleep to reduce health risks

    # Address sleep deprivation more aggressively
    if time_since_slept >= 7:
        return 3  # Sleep is a priority

    # Opt for coffee to boost alertness under healthy conditions
    if alertness < 0.6 and hypertension < 0.1 and intoxication < 0.1:
        return 1  # Coffee to improve alertness safely

    # Maintain productivity without additional stimulation
    if alertness < 0.8:
        return 0  # Just work

    # Allow beer when productivity is high but only if both health indicators are very low
    if work_done > 15 and alertness > 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 2  # Minor risk for high productivity

    # If no other actions are optimal, rest for recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)