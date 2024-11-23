import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate high-risk conditions - prioritize sleep
    if hypertension > 0.7 or intoxication > 0.7 or alertness < 0.2 or time_since_slept > 18:
        return 3
    
    # Use coffee more liberally under moderate conditions
    if alertness < 0.5 and hypertension < 0.5:
        return 1
    
    # Balance beer use carefully
    if alertness < 0.6 and intoxication < 0.2:
        return 2
    
    # Optimize default working state
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0
    
    # If none of the above, consider other recuperation options
    if time_since_slept > 12:
        return 3

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)