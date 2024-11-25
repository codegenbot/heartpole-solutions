import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Encourage sleep if alertness is low, intoxication is high, or prolonged wakefulness
    if alertness < 0.5 or intoxication > 0.1 or time_since_slept >= 5:
        return 3
    
    # Controlled use of coffee when necessary, ensuring low hypertension
    if alertness < 0.6 and hypertension < 0.025 and intoxication <= 0.02:
        return 1
    
    # Safe zone for work with heightened health checks
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Avoid beer to maintain productivity and health
    return 0

# Main loop
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)