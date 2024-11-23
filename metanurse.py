import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health by managing hypertension and intoxication first
    if hypertension > 0.4 or intoxication > 0.2:
        return 3  # Sleep

    # Sleep if alertness is very low or substantial time has passed since last rest
    if alertness < 0.6 or time_since_slept > 12:
        return 3  # Sleep

    # Encourage coffee use to boost alertness during early stages of the day
    if alertness < 0.8 and time_elapsed < 10 and work_done < 0.5:
        return 1  # Drink coffee and work

    # Recommend sleep during later hours if alertness is not optimal
    if time_elapsed >= 14 and alertness < 0.7:
        return 3  # Sleep

    # Opt for work when conditions are optimal
    if alertness >= 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleep for any marginal deviations
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)