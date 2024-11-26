import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Address immediate health risks
    if hypertension > 0.02 or intoxication > 0.08:
        return 3  # Prioritize health, sleep
    
    # Prioritize sleep for severe sleep deprivation or low alertness
    if time_since_slept >= 5 or alertness < 0.4:
        return 3  # Enhance alertness with sleep
    
    # Use coffee when moderate alertness and health is stable
    if 0.4 <= alertness < 0.8 and hypertension < 0.015 and intoxication < 0.05:
        return 1  # Boost with coffee
    
    # Opt for beer to stabilize when marginally intoxicated but not severely so
    if intoxication > 0.02 and hypertension < 0.015:
        return 2  # Sedate slightly
    
    # Optimal conditions to work
    return 0  # just work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)