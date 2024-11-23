import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.65 or intoxication > 0.5 or alertness < 0.2 or time_since_slept > 16:
        return 3  # Critical health state, sleep is necessary
    
    if alertness < 0.4 or time_since_slept > 12:  
        return 3  # Proactively manage sleep to maintain alertness
    
    if alertness < 0.65 and hypertension <= 0.4:
        return 1  # Coffee to boost alertness safely
    
    if alertness > 0.8 and hypertension <= 0.3 and intoxication < 0.2:
        return 2  # Relax with beer when alert and hypertensive state is calm 
    
    return 0  # Work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)