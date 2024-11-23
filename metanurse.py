import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate health risks prioritized
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    # Requirement to rest further if alertness falls below threshold
    if alertness < 0.5:
        return 3  # Sleep

    # Use coffee effectively while maintaining health
    if 0.5 <= alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Discourage beer use unless critically needed
    if alertness < 0.65 and intoxication <= 0.15:
        return 0  # Just work

    # Default safe productive state
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)