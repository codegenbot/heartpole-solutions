import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is too low or potential health issues
    if (
        alertness <= 0.6
        or hypertension > 0.3
        or intoxication > 0.15
        or time_since_slept >= 7
    ):
        return 3  # Sleep to improve health and reset

    # Use coffee carefully to avoid increasing hypertension
    if (
        alertness < 0.75
        and hypertension < 0.25
        and intoxication < 0.12
        and time_since_slept < 6
    ):
        return 1  # Drink coffee if alertness boost needed without hypertension risk

    # Opt for pure work when conditions are reasonably optimal
    if alertness >= 0.75 and hypertension <= 0.2 and intoxication <= 0.08:
        return 0  # Just work in reasonably good conditions

    # Consider beer if there's a need for stress relief and it's very safe
    if (
        alertness > 0.85
        and intoxication <= 0.05
        and hypertension <= 0.1
        and time_since_slept < 5
    ):
        return 2  # Drink beer if stress relief is safe

    return 0  # Default to working to maintain productivity

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)