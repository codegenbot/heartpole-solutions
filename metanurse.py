import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if health indicators suggest degradation
    if hypertension >= 0.25 or intoxication >= 0.06 or alertness <= 0.6 or time_since_slept > 5:
        return 3
    
    # Consider coffee if alertness is below optimal, but health indicators are safe
    if alertness < 0.7 and hypertension < 0.1:
        return 1
    
    # Consider beer if light relaxation might be beneficial
    if intoxication < 0.04 and hypertension < 0.15 and alertness > 0.75:
        return 2
    
    # Default to just working if all conditions are optimal for productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)