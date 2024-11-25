import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when either alertness is low or health signals are problematic
    if alertness < 0.4 or hypertension > 0.1 or intoxication > 0.08 or time_since_slept >= 4:
        return 3

    # Carefully use coffee when alertness is moderate and health conditions are stable
    if 0.4 <= alertness < 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Choose to work only when in very good conditions
    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    # Resort to beer minimally and only for strategic benefit when conditions match
    if work_done < 0.1 and intoxication <= 0.02 and alertness < 0.35:
        return 2

    # Default to working if no specific conditions met for other actions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)