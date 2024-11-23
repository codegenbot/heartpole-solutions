import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.5:
        return 3  # Sleep if heavily stressed or intoxicated
    if time_since_slept > 12 or alertness < 0.25:
        return 3  # Sleep if significantly sleep-deprived or very low alertness
    if alertness < 0.5 and hypertension < 0.5:
        return 1  # Drink coffee to boost alertness if safe
    if work_done < 0.8 and alertness >= 0.4:
        return 0  # Continue working if work done is unsatisfactory and alertness is sufficient
    if alertness < 0.6 and time_elapsed < 16:
        return 1  # Boost alertness with coffee if work capability might be affected soon
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)