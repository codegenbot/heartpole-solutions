import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any critical health level is reached
    if alertness < 0.5 or hypertension >= 0.6 or intoxication >= 0.5 or time_since_slept > 8:
        return 3  # Must sleep

    # Just work if alertness is fairly high and health is stable
    if alertness > 0.7 and hypertension <= 0.3 and intoxication < 0.3:
        return 0  # Just work

    # Use coffee to boost alertness if moderately tired and health is ok
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Use beer sparingly when needing relaxation without much health risk
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.3:
        return 2  # Drink beer and work

    return 3  # Default to rest by sleeping if unsure or in danger

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)