import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High-risk health indicators: prioritize sleep more aggressively
    if hypertension > 0.015 or intoxication > 0.04:
        return 3
    
    # Recommend sleep for lower alertness or if long time since sleep
    if alertness < 0.6 or time_since_slept > 2.5:
        return 3

    # Use coffee strategically to boost alertness without risking health
    if alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # Beer as last resort when in specific balanced condition
    if 0.6 <= alertness < 0.8 and 0.01 < hypertension <= 0.015 and intoxication < 0.03:
        return 2

    # Default action if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)