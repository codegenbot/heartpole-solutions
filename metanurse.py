import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk
    if hypertension > 0.02 or intoxication > 0.02:
        return 3

    # Sleep if alertness too low or slept too long ago
    if alertness < 0.7 or time_since_slept > 4:
        return 3

    # Drink coffee if alertness is moderate and no immediate risk
    if 0.7 <= alertness < 0.85 and hypertension < 0.015 and intoxication < 0.01:
        return 1

    # Drink beer if relaxation needed and intoxication is low
    if intoxication < 0.01 and time_elapsed > 10 and work_done < 5:
        return 2

    # Just work if alertness is high
    if alertness >= 0.85:
        return 0

    # Default to just work if no other conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)