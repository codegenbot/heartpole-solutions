import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate sleep for high risks to health
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness falls too low or it has been too long since last rest
    if alertness < 0.6:
        return 3  # Sleep

    # Use coffee to maintain or slightly boost alertness safely
    if 0.6 <= alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Allow beer only as a last resort to maintain minimal productivity
    if alertness < 0.65 and 0.1 < intoxication <= 0.15:
        return 2  # Drink beer and work

    # Default to working when conditions are safe and optimized
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)