import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if critical conditions are met
    if (
        alertness < 0.4
        or hypertension > 0.75
        or intoxication > 0.5
        or time_since_slept > 12
    ):
        return 3  # Need sleep

    # If conditions are productive, just work
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.05:
        return 0  # Just work

    # Use coffee to boost alertness effectively without impacting health
    if 0.4 <= alertness < 0.75 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Coffee and work

    # Consider light work with beer if productivity can be boosted with less severe consequences
    if alertness < 0.4 and 0.05 < intoxication <= 0.3 and hypertension < 0.55:
        return 2  # Beer and work

    # Default to sleep to maintain recovery if no productive strategy is found
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)