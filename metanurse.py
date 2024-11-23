import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health risks are high
    if hypertension > 0.4 or intoxication > 0.25:
        return 3
    
    # Insist on sleeping on low alertness or prolonged wakefulness
    if alertness < 0.3 or time_since_slept > 14:
        return 3
    
    # Limit coffee consumption to early hours and moderately low alertness
    if alertness < 0.5 and time_elapsed <= 6 and hypertension < 0.3:
        return 1
    
    # Consider a minor break with beer only if productivity is beneficial
    if intoxication <= 0.2 and work_done < 0.4 and time_elapsed < 10:
        return 2
    
    # Work more freely if alertness and health metrics are good
    if alertness >= 0.6 and hypertension <= 0.2 and intoxication <= 0.1 and work_done < 0.9:
        return 0
    
    # Default to sleep to promote recovery for any staying health precautions beyond alertness
    if alertness < 0.4 and time_elapsed > 10:
        return 3
    
    # Default decision based on capability and recovery
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)