import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if hypertensive, intoxicated, or too long without sleep
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept > 8:
        return 3
    # Use coffee if alertness is low and health parameters are fine
    if alertness < 0.5 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1
    # Work without enhancements when parameters and alertness are in good states
    if alertness >= 0.5 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0
    # Drink beer in relaxation mode if some work is already done and within safe health limits
    if 5 < work_done <= 10 and alertness > 0.5 and intoxication <= 0.1 and hypertension <= 0.15:
        return 2
    # Otherwise, sleep for recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)