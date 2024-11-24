import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical sleep necessity: prioritize health risks
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Sleep

    # High alertness and low health risks: maximize productivity
    if alertness >= 0.8 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness: use coffee to boost
    if 0.5 <= alertness < 0.8 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Extended working without rest leads to accumulated stress and intoxication
    if time_since_slept > 7:
        return 3  # Sleep

    # If stressed or toxic, reduce the load by choosing a balanced action
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep

    return 0  # Default work if no strong indicators for rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)