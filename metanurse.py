import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if near-critical health indicators are present
    if alertness < 0.5 or hypertension >= 0.6 or intoxication >= 0.4 or time_since_slept > 6:
        return 3  # Must sleep

    # Work directly if all health indicators are optimal
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work
    
    # Prioritize coffee under lower health risk and moderate alertness
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Use beer as last resort if relaxed and health is stable
    return 2 if alertness < 0.6 and intoxication < 0.2 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)