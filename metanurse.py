import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if there's a risk to health from lack of alertness or excess stress
    if alertness < 0.5 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 8:
        return 3  # Sleep to mitigate risk

    # Safely use coffee to boost alertness only if stress and intoxication are low
    if alertness < 0.7 and hypertension < 0.6 and intoxication <= 0.15:
        return 1  # Coffee and work

    # If already alert with safe health levels, focus on work
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.25:
        return 0  # Just work

    # Use beer tactically to reduce hypertension while keeping intoxication in check
    if 0.15 < intoxication < 0.3 and hypertension < 0.6:
        return 2  # Drink beer and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)