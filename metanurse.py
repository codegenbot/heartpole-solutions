import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep more strictly if alertness, time_since_slept, or general stress factors are critical
    if alertness < 0.3 or time_since_slept > 6 or hypertension >= 0.15 or time_elapsed > 5:
        return 3
    
    # Use coffee with less strict criteria to maintain alertness if there are no significant health risks
    if alertness < 0.5 and hypertension < 0.08 and intoxication < 0.05:
        return 1
    
    # Encourage working if all indicators support productivity with minimal risk
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.03:
        return 0
    
    # In scenarios not warranting coffee or sleep, lean towards working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)