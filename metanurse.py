import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health issues that demand immediate rest
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 8:
        return 3  # Sleep

    # If health is stable, consider productivity improvements
    if work_done < time_elapsed * 0.7:
        if alertness < 0.5:
            return 1  # Drink coffee and work
        elif alertness < 0.3 and intoxication < 0.2:
            return 2  # Drink beer and work

    # Optimal conditions for pure work, prioritize health
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.15:
        return 0  # Just work

    # Default to sleep if no other action is preferable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)