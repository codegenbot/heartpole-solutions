import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping for health risks or poor alertness
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.5 or time_since_slept >= 6:
        return 3
    
    # Restrict coffee usage, balance between productivity and alertness
    if alertness < 0.5 and hypertension <= 0.15 and intoxication < 0.05 and time_since_slept < 6:
        return 1

    # Allow safe work when alertness is sufficient
    if alertness >= 0.5 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0
    
    # Minimize beer use, only under less hypertension and lower work done
    if alertness >= 0.6 and hypertension < 0.1 and intoxication < 0.05 and work_done < 0.4:
        return 2

    # Default fallback to working if none of the conditions are strictly met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)