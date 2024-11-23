import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High priority sleep for severe health issues
    if hypertension > 0.35 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep or drink coffee based on alertness
    if alertness < 0.6:
        if alertness < 0.45:
            return 3  # Sleep
        elif hypertension <= 0.2 and intoxication <= 0.1:
            return 1  # Drink coffee and work
    
    # Default to working when factors are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)