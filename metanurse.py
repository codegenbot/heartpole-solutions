import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health issue is significant
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep to mitigate health risks

    # If awake for over 12 hours or showing fatigue
    if time_since_slept > 12 or alertness < 0.4:
        return 3  # Sleep to recover alertness

    # Use coffee when alertness is moderate and some work progress is needed
    if alertness < 0.5 and work_done < 0.9:
        return 1  # Drink coffee and work for alertness boost

    # Default work if no threshold for concern
    return 0 if alertness >= 0.5 else 3  # Work if alert enough


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)