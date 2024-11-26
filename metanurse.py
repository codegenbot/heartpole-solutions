import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health first
    if (
        time_since_slept >= 5.0
        or alertness < 0.3
        or hypertension > 0.08
        or intoxication > 0.06
    ):
        return 3  # Sleep to recover and reduce alertness issues

    # If health is not critical, improve alertness if it is moderately low
    if (
        0.3 <= alertness < 0.6
        and hypertension < 0.06
        and intoxication < 0.05
        and time_since_slept < 4.0
    ):
        return 1  # Drink coffee for slight alertness boost

    # Choose work when alert and demands on productivity are low
    if (
        alertness >= 0.65
        and hypertension < 0.04
        and intoxication < 0.03
        and work_done < 0.95
    ):
        return 0  # Just work when alertness is high

    # On initial low productivity but not severe health issues
    if (
        work_done < 0.2
        and intoxication <= 0.02
        and alertness < 0.5
        and time_since_slept < 3.0
    ):
        return 2  # Drink beer to boost mood/productivity without excessive risk

    # Default to just working if nothing is critical
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)