import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize recovery when any health indicator is critical
    if hypertension > 0.4 or intoxication > 0.3:
        return 3  # Sleep

    # Manage alertness spikes; prefer sleeping it off rather than relying heavily on coffee
    if alertness < 0.5:
        if hypertension <= 0.2 and intoxication <= 0.15:
            return 1  # Drink coffee and work
        return 3  # Sleep

    # Allow coffee only if hypertension and intoxication are manageable
    if 0.5 <= alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Encourage regular breaks after long periods of work or sleep if needed
    if time_since_slept > 6:
        return 3  # Sleep

    # Default to working in safe conditions
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)