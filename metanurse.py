import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health issues that demand immediate rest
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 8:
        return 3  # Sleep

    # Prioritize health: ensure blood pressure and intoxication are managed
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep

    # Consider productivity
    if work_done < time_elapsed * 0.7:
        if alertness < 0.5:
            return 1  # Drink coffee and work
        elif alertness > 0.5 and intoxication < 0.1:
            return 0  # Just work

    # Default to working if no other specific action needed
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)