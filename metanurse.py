import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for safer health states
    if hypertension > 0.25 or intoxication > 0.08 or time_since_slept > 7:
        return 3  # Sleep

    # Sleep when alertness is low
    if alertness < 0.55:
        return 3  # Sleep

    # Encourage sleep cyclically if approaching 1000 steps or significant work done
    if time_elapsed > 900 and time_since_slept >= 5:
        return 3  # Sleep

    # Use coffee to optimize productivity if alertness is moderately low
    if alertness < 0.6 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Restrict beer to control hypertension cautiously
    if hypertension > 0.2 and intoxication <= 0.01:
        return 2  # Drink beer and work

    # Default to work if all metrics are safe
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)