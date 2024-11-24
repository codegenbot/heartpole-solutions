import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health issue is high
    if hypertension > 0.6 or intoxication > 0.35 or time_since_slept > 8:
        return 3  # Sleep
    # If alertness is low, consider coffee if health permits
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work
    # Safe conditions to just work
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    # As a last resort, consider beer if slight alertness drop
    return 2  # Drink beer and work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)