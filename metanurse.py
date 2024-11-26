import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health by introducing stricter health checks
    if hypertension >= 0.015 or intoxication >= 0.08:
        return 3  # sleep if nearing risky health conditions
    
    # Adjust alertness to prioritize more frequent rest
    if alertness < 0.75 or time_since_slept >= 6:
        return 3  # sleep if alertness is moderate or needs more frequent rest
    
    # Alertness enhancement through coffee should be carefully balanced
    if alertness < 0.85 and hypertension < 0.01 and intoxication < 0.03:
        return 1  # drink coffee and work only if metrics are very safe for productivity gain
    
    return 0  # default to work if alertness is adequate and all metrics are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)