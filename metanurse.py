import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for any notable health issues
    if hypertension > 0.5 or intoxication > 0.3:
        return 3
    
    # Opt to sleep if time awake is lengthy or alertness is very low
    if time_since_slept > 12 or alertness < 0.4:
        return 3
    
    # Use coffee with caution, optimize time and workload conditions
    if alertness < 0.65 and time_elapsed < 8 and work_done < 0.5:
        return 1
    
    # Prefer work if all conditions suggest safe operation
    if alertness >= 0.55 and hypertension <= 0.2 and intoxication <= 0.15:
        return 0
    
    # Prioritize sleep in afternoon if alertness is waning
    if time_elapsed >= 14 and alertness < 0.5:
        return 3

    # Review work condition, default as needed
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)