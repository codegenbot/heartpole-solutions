import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep for health recovery when needed
    if alertness < 0.5 or time_since_slept > 8 or hypertension > 0.3 or intoxication > 0.3:
        return 3  # Sleep to recover

    # Use coffee carefully to improve alertness with stricter health checks
    if alertness < 0.7 and hypertension <= 0.25 and intoxication <= 0.25:
        return 1  # Drink coffee to boost alertness

    # Pure work is only okay with ideal alertness and low health risks
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Work

    # Allow beer if both hypertension and intoxication are below safe bounds
    if hypertension <= 0.25 and intoxication <= 0.15:
        return 2  # Drink beer to relax

    # Default to working if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)