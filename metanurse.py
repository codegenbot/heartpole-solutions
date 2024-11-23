import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate high-risk conditions - prioritize sleep
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.1 or time_since_slept > 15:
        return 3
    
    # Use coffee to address low alertness, but watch for hypertension
    if alertness < 0.4 and hypertension <= 0.5:
        return 1
    
    # Avoid using beer unless intoxication is very low
    if alertness < 0.4 and intoxication < 0.05:
        return 2
    
    # Optimal condition to work directly
    if alertness >= 0.75 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0
    
    # If none of the above, consider recuperation options
    if time_since_slept > 14:
        return 3

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)