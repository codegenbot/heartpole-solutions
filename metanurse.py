import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health by sleeping if critical
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 6:
        return 3  # Sleep

    # Conditions to counteract low alertness or early signs of intoxication
    if alertness < 0.4 and time_since_slept <= 5:
        return 1  # Drink coffee and work
    
    if intoxication > 0.2 and time_since_slept <= 5:
        return 3  # Sleep to manage intoxication
        
    # Work efficiently with good alertness and low health risks
    if alertness >= 0.65 and intoxication <= 0.2 and hypertension <= 0.25:
        return 0  # Just Work

    # Default to coffee and work during moderate alertness to enhance productivity
    if alertness < 0.65 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Default action if health conditions are not optimal
    return 2  # Drink beer and work, assumes beer slightly reduces stress for a short term gain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)