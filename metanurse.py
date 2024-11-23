import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on severe conditions and accumulated sleep deprivation
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3  # Sleep for better recovery and long-term productivity

    # Use coffee strategically to improve alertness when it doesn't dangerously increase hypertension
    if 0.3 <= alertness < 0.5 and hypertension < 0.2 and intoxication < 0.3:
        return 1  # Increase alertness without significant health risks

    # Work under favorable conditions with moderate controls on hypertension and intoxication
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Maximize productivity in a healthy state

    # Use beer in limited cases to manage mild hypertension when other factors aren't critical
    if 0.4 <= hypertension < 0.6 and intoxication < 0.4:
        return 2  # Lower stress without risking intoxication

    # Default to work under uncertain conditions to avoid negative health effects
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)