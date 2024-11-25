import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health issues that demand immediate rest
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 8:
        return 3  # Sleep

    # Optimize productivity if health permits
    if work_done < time_elapsed * 0.6:
        if alertness < 0.4 and hypertension < 0.3 and intoxication < 0.2:
            return 1  # Drink coffee and work
        elif alertness < 0.3 and intoxication < 0.1:
            return 2  # Drink beer and work

    # Ideal conditions for pure work
    if alertness >= 0.5 and hypertension < 0.25 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleep if no other action is beneficial
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)