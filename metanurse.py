import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate high-risk conditions - prioritize sleep
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.1 or time_since_slept > 16:
        return 3
    
    # Address moderate alertness problems with coffee, but avoid increasing hypertension
    if alertness < 0.3 and hypertension <= 0.4:
        return 1
    
    # Avoid using beer if intoxication is moderate, but utilize it slightly differently
    if alertness < 0.4 and intoxication <= 0.1:
        return 2
    
    # Optimal condition to work directly
    if alertness >= 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0
    
    # If none of the above, consider recuperation options
    if time_since_slept > 12:
        return 3

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)