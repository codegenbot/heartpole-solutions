import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health levels are exceeded
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 12:
        return 3
    
    # Encourage sleep if alertness is low and haven't slept recently
    if alertness < 0.6 and time_since_slept > 8:
        return 3

    # Encourage coffee to boost alertness moderately
    if alertness < 0.7 and hypertension <= 0.3 and intoxication < 0.2:
        return 1
    
    # Default to working if all health metrics are optimal
    if alertness >= 0.8 and hypertension <= 0.25 and intoxication < 0.1:
        return 0
    
    # Encourage more sleep if workload is high and alertness is low
    if work_done > 0.8 and alertness < 0.75:
        return 3

    # As a fallback, work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)