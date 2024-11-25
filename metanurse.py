import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strongly prioritize sleep when signs of fatigue or health risks appear
    if hypertension > 0.2 or intoxication > 0.15 or alertness < 0.5 or time_since_slept > 5:
        return 3
    
    # Use coffee to stay alert, provided it doesn't negatively impact health
    if alertness < 0.7 and hypertension <= 0.15 and intoxication < 0.1:
        return 1
    
    # Work if conditions are within optimal health and alertness levels
    if alertness >= 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0
    
    # Default fallback to working without beer to maintain balanced health
    return 0

# Main loop to process each observation set
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)