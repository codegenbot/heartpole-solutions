import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Ensure health thresholds are maintained
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 4:
        return 3  # Sleep if any major condition threatens health

    # Use coffee sparingly and strategically
    if alertness < 0.55 and hypertension <= 0.55 and intoxication <= 0.3:
        return 1  # Drink coffee and work if it helps significantly with alertness

    # Prefer uninterrupted work when conditions are safe
    if alertness >= 0.6 and hypertension <= 0.55 and intoxication <= 0.2:
        return 0  # Just work in optimal conditions

    # Drink beer with more restraint due to health risks
    if hypertension < 0.6 and intoxication < 0.45:
        return 2  # Drink beer only when stress is manageable

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)