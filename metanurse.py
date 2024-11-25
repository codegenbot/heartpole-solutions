import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if critical conditions are met
    if alertness < 0.2 or hypertension > 0.85 or intoxication > 0.6 or time_since_slept > 14:
        return 3  # Need sleep

    # If conditions are productive, just work
    if alertness > 0.9 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee to boost alertness effectively without impacting health
    if 0.4 <= alertness < 0.8 and hypertension < 0.65 and intoxication < 0.15:
        return 1  # Coffee and work

    # Avoid using beer due to health risks; it's often a poor strategy
    if alertness < 0.4 and hypertension < 0.45 and intoxication < 0.15:
        return 2  # Beer and work

    # If none apply, default to sleep to maintain recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)