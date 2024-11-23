import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if any health risk parameters exceed safe thresholds
    if hypertension > 0.4 or intoxication > 0.25 or time_since_slept > 10:
        return 3  # Sleep

    # Sleep if alertness is critically low regardless of other factors
    if alertness < 0.4:
        return 3  # Sleep

    # Consider drinking coffee if moderately low alertness and safe health parameters
    if 0.4 <= alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Consider slight intoxication alleviation when alertness is sufficient and productivity benefits
    if intoxication > 0.2 and alertness >= 0.8:
        return 2  # Drink beer and work

    # Default to working if everything is within safe limits
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)