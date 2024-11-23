import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate sleep for high risks to health
    if hypertension > 0.25 or intoxication > 0.1 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.7:
        return 3  # Sleep

    # Use coffee to safely maintain alertness
    if 0.7 <= alertness < 0.8 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Avoid using beer; work instead of increasing intoxication
    if 0.65 <= alertness < 0.7 and intoxication <= 0.05:
        return 0  # Just work

    # Default to working when conditions are safe and optimized
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)