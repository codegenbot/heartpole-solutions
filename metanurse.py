import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if severely lacking, or after long wake duration
    if alertness < 0.4 or time_since_slept > 7 or hypertension > 0.6:
        return 3  # Sleep

    # Work without additional substances if generally healthy
    if alertness > 0.6 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work safely

    # Use coffee if alertness and health permits
    if 0.5 <= alertness <= 0.6 and hypertension < 0.5 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Use beer sparingly when slightly tired and health metrics allow
    if 0.4 <= alertness < 0.5 and intoxication < 0.1 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default to sleep to recover if no other safe productive actions are viable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)