import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate need for sleep if health risk indicators are above a critical threshold
    if hypertension > 0.05 or intoxication > 0.1 or time_since_slept > 8:
        return 3
    
    # Use coffee to boost alertness but avoid if health risk is notable
    if alertness < 0.6 and hypertension < 0.03 and intoxication < 0.05:
        return 1
    
    # Prioritize work if conditions are optimal or near optimal
    if alertness >= 0.75 and hypertension < 0.04 and intoxication < 0.05:
        return 0
    
    # Resort to sleep if no optimal work or coffee conditions
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)