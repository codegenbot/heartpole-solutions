import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # More stringent conditions for immediate sleep
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    # Rest if alertness is low, could also boost productivity after rest
    if alertness < 0.6:
        return 3  # Sleep

    # Use coffee when alertness is moderately low but still manage health
    if 0.6 <= alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Resort to beer only under specific conditions
    if alertness < 0.62 and 0.1 < intoxication <= 0.13:
        return 2  # Drink beer and work

    # Default action when conditions are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)