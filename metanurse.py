import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if any serious health issue is detected
    if alertness < 0.4 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 10:
        return 3

    # Use coffee strategically to maintain alertness while keeping health in check
    if alertness < 0.55 and hypertension < 0.05 and intoxication < 0.02 and time_since_slept < 6:
        return 1

    # Allow work if condition is consistently healthy and productive
    if alertness >= 0.65 and hypertension <= 0.08 and intoxication <= 0.02:
        return 0

    # Use beer cautiously when productivity is extremely low and safe
    if work_done < 0.1 and alertness > 0.55 and hypertension < 0.04 and intoxication < 0.01:
        return 2

    # Default action to work if none of the above are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)