import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical levels are reached
    if alertness < 0.4 or hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept > 8:
        return 3  # Must sleep

    # Optimize work based on alertness and stable health
    if alertness > 0.8 and hypertension <= 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee to boost alertness when appropriate
    if alertness < 0.8 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Use beer sparingly and only under conditions of slight relaxation
    return 2 if alertness < 0.6 and intoxication < 0.3 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)