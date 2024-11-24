import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when alertness is severely low or health is compromised
    if (
        alertness < 0.4
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 6
    ):
        return 3

    # Drink coffee if alertness is moderate, but avoid if health risks are visible
    if (
        alertness < 0.6
        and hypertension <= 0.5
        and intoxication < 0.25
        and time_since_slept <= 5
    ):
        return 1

    # Work if alertness and health indicators are excellent
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0

    # Default to sleep if none are suitable to improve alertness safely
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)