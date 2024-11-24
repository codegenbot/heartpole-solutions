import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust sleep criteria for better health management
    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 7:
        return 3  # Sleep
    # Lower thresholds for coffee if health permits
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.25:
        return 1  # Drink coffee and work
    # Safe conditions to just work
    if alertness >= 0.8 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work
    # Consider beer more cautiously
    return 2  # Drink beer and work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)