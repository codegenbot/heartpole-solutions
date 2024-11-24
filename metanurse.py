import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if any health issue is significant
    if hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept >= 4:
        return 3

    # Evaluate productivity level vs time spent
    if work_done < 0.75 * time_elapsed:
        if alertness < 0.7 and hypertension < 0.5:
            return 1  # Drink coffee and work

    # Optimal working conditions without needing additional stimuli
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work

    # If no specific condition is met, default to sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)