import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust thresholds to better prioritize health
    if hypertension > 0.25 or intoxication > 0.1 or alertness < 0.6 or time_since_slept > 5:
        return 3  # Sleep to recover and manage health risks.

    if alertness < 0.7 and hypertension < 0.2:
        return 1  # Use coffee to adequately increase alertness.

    if intoxication < 0.05 and hypertension < 0.15 and work_done < 0.3:
        return 2  # Relaxation (beer) only when health metrics are excellent.

    # Default to working only when productive metrics are balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)