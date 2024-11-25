import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for health risks or poor alertness
    if hypertension > 0.25 or intoxication > 0.15 or alertness < 0.4 or time_since_slept > 6:
        return 3
    
    # If alertness is moderate but within safer hypertension and intoxication level, consider coffee
    if alertness < 0.6 and hypertension <= 0.2 and intoxication < 0.1 and time_since_slept <= 6:
        return 1
    
    # Opt for just work under balanced health conditions
    if alertness >= 0.6 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0
    
    # Consider minimum beer intake and its impacts thoughtfully
    if alertness >= 0.7 and hypertension < 0.15 and intoxication < 0.1 and work_done < 0.5:
        return 2
    
    # Default fallback to working if none of the conditions are strictly met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)