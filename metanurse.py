import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Check for sleep when necessary
    if alertness < 0.5 or time_since_slept > 3:  # Slightly relaxed threshold to sleep sooner
        return 3  # Sleep to regain alertness

    # Reduce hypertension and intoxication risks
    if hypertension > 0.6 or intoxication > 0.3:
        return 3  # Rest to prevent health risks

    # Utilize coffee strategically without increasing health risks
    if alertness < 0.6 and hypertension <= 0.5 and intoxication <= 0.25:
        return 1  # Drink coffee and work if it's safe

    # Prioritize safe, uninterrupted work
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work in optimal safe conditions

    # Avoid using beer unless all parameters are favorable
    if hypertension <= 0.5 and intoxication <= 0.25:
        return 2  # Only if stress and intoxication are low

    return 3  # Default to sleep for precaution

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)