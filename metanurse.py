import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with more balanced conditions
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.3 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee wisely when alertness is moderate but low-risk
    if 0.4 <= alertness < 0.6 and hypertension <= 0.6 and intoxication <= 0.2:
        return 1  # Coffee and work

    # Choose to work when conditions are favorable
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Avoid beer; keep default action if no specific conditions are met
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)