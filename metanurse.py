import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep only when needed
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Sleep

    if alertness < 0.4:
        return 3  # Sleep

    # Adjust coffee strategy with lower alertness
    if alertness < 0.65 and hypertension <= 0.2 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Tackle moderate intoxication directly with work
    if intoxication > 0.15 and hypertension <= 0.25:
        return 0  # Just work

    # High alertness and low intoxication — work without aid
    if alertness >= 0.7 and intoxication <= 0.1:
        return 0  # Just work

    return 3  # Default: Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)