import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Ensure health thresholds are maintained, prioritize safety
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 5:
        return 3  # Sleep if any major condition threatens health

    # Use coffee strategically when slightly tired but safe to do so
    if alertness < 0.55 and hypertension <= 0.6 and intoxication <= 0.25:
        return 1  # Drink coffee and work if it can safely boost alertness

    # Prefer just working when conditions are comfortable
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work in optimal conditions

    # Less priority for beer, focusing on reducing intoxication
    if hypertension < 0.6 and intoxication < 0.35 and time_since_slept < 4:
        return 2  # Drink beer if hypertensive is manageable but still low risk

    # Default to sleep if unsure or conditions are ambiguous
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)