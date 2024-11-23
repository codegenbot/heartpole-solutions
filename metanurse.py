import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep over potential health issues like moderate alertness concerns
    if hypertension > 0.25 or intoxication > 0.15:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.65:
        return 3  # Sleep

    # Use coffee only if alertness is slightly low, ensuring other health factors are stable
    if 0.65 <= alertness < 0.8 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Encourage sleep more frequently if enough time has passed since last sleep
    if time_since_slept > 3:
        return 3  # Sleep

    # Default to working only when all conditions are optimal
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)