import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if there are significant health issues or hasn't slept recently
    if hypertension > 0.4 or intoxication > 0.25:
        return 3  # sleep due to health concerns
    if time_since_slept > 6:
        return 3  # sleep due to long time without sleep

    # Boost alertness when it's low during working hours
    if alertness < 0.5:
        if time_elapsed < 10:
            return 1  # drink coffee to stay alert during work hours
        else:
            return 3  # sleep if it's already late

    # Regular work if conditions are moderate
    if work_done < 0.7:
        return 0  # work if productivity is still needed

    # Default action for steady work with sufficient alertness
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)