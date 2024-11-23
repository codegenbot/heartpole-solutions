import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health risks are detected
    if hypertension > 0.2 or intoxication > 0.15 or time_since_slept > 4:
        return 3  # Sleep

    # Use coffee to boost alertness while keeping health safe
    if alertness < 0.6 and hypertension <= 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # High alertness and low intoxication is ideal for working
    if alertness >= 0.55 and intoxication <= 0.1:
        return 0  # Just work

    # Default to sleep if none of the above conditions apply
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)