def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize immediate health issues
    if hypertension > 0.025 or intoxication > 0.12:
        return 3  # Sleep to address early health warnings

    # Consider sleep necessity at lower alertness
    if time_since_slept >= 6 or alertness < 0.5:
        return 3  # Sleep for better recovery

    # Use coffee to enhance productivity when alertness is moderate
    if 0.5 <= alertness < 0.7 and hypertension < 0.025:
        return 1  # Coffee and work to boost alertness

    # Work conditions when alertness is high and intoxication is low
    if alertness >= 0.7 and intoxication < 0.08:
        return 0  # Work safely without coffee

    # Fallback to working cautiously
    return 0

import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)