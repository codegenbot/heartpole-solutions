import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health issues
    if alertness < 0.4 or hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept > 6:
        return 3  # Must sleep

    # Work directly if all health indicators are optimal
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work
    
    # Drink coffee to boost alertness if hypertension and intoxication are low
    if alertness < 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Prioritize sleep if actions have been taken for several steps 
    if time_elapsed % 5 == 0:
        return 3  # Sleep periodically

    # Use beer if intoxication and alertness are not critically low
    return 2 if alertness < 0.7 and intoxication < 0.3 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)