import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep for low alertness or extended hours without sleep
    if alertness < 0.45 or time_since_slept > 5:
        return 3

    # Immediate sleep for concerning health indicators
    if hypertension >= 0.1 or intoxication > 0.08:
        return 3

    # Coffee if moderate alertness is needed without health risks
    if alertness < 0.65 and hypertension < 0.08 and intoxication <= 0.02:
        return 1
    
    # Permit work at higher alertness with safe health parameters
    if alertness >= 0.55 and hypertension <= 0.07 and intoxication <= 0.01:
        return 0

    # Use beer carefully when alertness is average and work_done is minimal
    if alertness > 0.5 and work_done < 0.04:
        return 2

    # Fall back to safe, productive action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)