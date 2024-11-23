import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Prioritize health by sleeping if stressed or intoxicated
    if time_since_slept > 16:
        return 3  # Ensure sleep if significantly sleep-deprived
    if alertness < 0.3:
        if time_since_slept >= 12 or time_elapsed >= 10:
            return 3  # Sleep if alertness is very low and hasn't slept in a while
        return 1  # Otherwise, try boosting alertness with coffee if possible
    if work_done < 0.7 and alertness >= 0.5:
        return 0  # Just work if productivity isn't satisfactory but alertness is decent
    if alertness < 0.7 and time_elapsed < 12:
        return 1  # Boost alertness with coffee before it's too late
    return 0  # Default: just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)