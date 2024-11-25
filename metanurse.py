import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health check for immediate sleep need
    if alertness < 0.3 or hypertension > 0.1 or intoxication > 0.08 or time_since_slept >= 5:
        return 3
    
    # Prioritize reducing hypertension through rest if mild
    if 0.3 <= alertness < 0.5 and hypertension > 0.05 and time_since_slept >= 3:
        return 3
    
    # Manage alertness with coffee if safe
    if alertness < 0.65 and hypertension < 0.05 and intoxication < 0.02:
        return 1
    
    # Optimize productivity with stable conditions
    if alertness >= 0.65 and hypertension < 0.03 and intoxication < 0.01:
        return 0
    
    # Consume beer only when very low in alert and work done, within safe intoxication
    if work_done < 0.03 and intoxication <= 0.01 and alertness < 0.35:
        return 2

    # Default to working if conditions aren't critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)