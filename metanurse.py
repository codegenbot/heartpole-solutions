import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for health preservation and recovery
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Sleep

    # Ensure sufficient alertness for productivity
    if alertness < 0.5:
        return 3  # Sleep

    # Allow coffee to boost alertness when safe
    if 0.5 <= alertness < 0.8 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default working mode in safe conditions
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)