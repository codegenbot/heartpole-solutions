import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health indicators are present
    if alertness < 0.4 or hypertension > 0.7 or intoxication >= 0.5 or time_since_slept > 8:
        return 3  # Must sleep
    
    # Prioritize coffee if moderate alertness and manageable hypertension
    if 0.4 <= alertness < 0.6 and hypertension < 0.6 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Work directly if all health indicators reflect a good state
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Use beer only in low-stress, not-unwell situations
    if 0.5 <= alertness < 0.6 and intoxication < 0.3 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)