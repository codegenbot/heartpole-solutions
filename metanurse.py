import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Determine need for sleep by being more cautious with health metrics
    if alertness < 0.4 or hypertension > 0.75 or intoxication > 0.4 or time_since_slept > 10:
        return 3  # Need sleep

    # Adjusted conditions for productive work without stimulants
    if alertness > 0.8 and hypertension < 0.45 and intoxication < 0.1:
        return 0  # Just work

    # More conservative coffee use, considering hypertension
    if 0.5 <= alertness < 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 1  # Coffee and work

    # Avoid using beer as a solution barring extreme low thresholds
    return 3  # Default to sleep for better long-term recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)