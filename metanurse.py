import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if any health risk parameters exceed safe thresholds
    if hypertension > 0.35 or intoxication > 0.20 or time_since_slept > 9:
        return 3  # Sleep

    # Sleep if alertness is critically low regardless of other factors
    if alertness < 0.5:
        return 3  # Sleep

    # Consider drinking coffee if moderately low alertness and safe health parameters
    if 0.5 <= alertness < 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to working if everything is within safe limits and alertness is sufficient
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)