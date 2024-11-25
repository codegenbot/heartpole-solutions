import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize rest when necessary
    if alertness <= 0.6 or hypertension > 0.3 or intoxication > 0.15 or time_since_slept >= 8:
        return 3  # Sleep to recover crucial metrics
    
    # Coffee can be used when alertness is moderately low but not dangerous 
    if alertness < 0.75 and hypertension < 0.2 and intoxication < 0.1 and time_since_slept < 6:
        return 1  # Drink coffee to boost alertness safely
    
    # Avoid beer unless it's very safe to do so, as it affects intoxication
    if alertness > 0.9 and intoxication <= 0.05 and hypertension < 0.1:
        return 2  # Beer only when in optimal alert states
    
    return 0  # Just work if conditions are under reasonable control

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)