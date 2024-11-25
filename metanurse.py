import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping more aggressively for health
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.5 or time_since_slept > 5:
        return 3
    
    # Allow moderate use of coffee to increase productivity
    if alertness < 0.6 and hypertension <= 0.1 and intoxication < 0.05 and time_since_slept < 5:
        return 1

    # Tighten restrictions on beer due to health impacts
    if alertness > 0.7 and hypertension < 0.08 and intoxication < 0.02 and work_done < 0.2:
        return 2

    # Default to working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)