import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping when alertness is too low or if time without sleep is too high
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # Sleep

    # Use coffee strategically to boost alertness without high hypertension
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Prefer just working if conditions are optimal
    if alertness >= 0.6 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0  # Just work

    # Default to work while monitoring health
    if hypertension > 0.4 or intoxication > 0.3:
        return 3  # Sleep to reset

    # Use beer when not a critical impairment, balancing relaxation and alertness
    if intoxication <= 0.5 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 0  # Safe default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)