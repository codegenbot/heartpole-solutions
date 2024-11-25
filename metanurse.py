import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always sleep if alertness is really low, or fatigue is high
    if alertness < 0.4 or time_since_slept >= 7.0:
        return 3
    
    # Avoid beer if not absolutely necessary; prioritize work over intoxication
    if work_done < 0.05 and intoxication <= 0.02 and alertness < 0.4:
        return 2

    # Use coffee when mild alertness drop and hypertension is safe
    if alertness < 0.65 and hypertension < 0.035 and intoxication <= 0.03:
        return 1

    # Work only if all factors are reasonably safe
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.025:
        return 0

    # Default to work if unclear, ensuring it's safe enough
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)