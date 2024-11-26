import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for more realistic alertness thresholds and resets
    if (
        alertness < 0.6  # Increase alertness threshold for sleep
        or time_since_slept >= 5  # Sleep more frequently
        or intoxication > 0.08  # Slightly stricter intoxication limit for sleep
        or hypertension > 0.07  # Slightly stricter hypertension limit
    ):
        return 3  # Sleep to recover

    # Control coffee intake relative to hypertension
    if alertness < 0.7 and hypertension < 0.06:
        return 1  # Coffee to boost alertness, with balanced hypertension

    # Further restrict beer consumption to safe conditions
    if alertness > 0.85 and intoxication < 0.02 and hypertension < 0.008:
        return 2  # Reward with beer in optimal state

    return 0  # Default to work when conditions are generally stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)