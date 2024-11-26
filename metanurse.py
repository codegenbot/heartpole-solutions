import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is critically low or time without sleep is high
    if (
        alertness < 0.6
        or time_since_slept >= 5
        or hypertension > 0.05
        or intoxication > 0.05
    ):
        return 3  # Sleep to restore alertness and reduce health risks

    # Encourage coffee only when alertness is slightly low and no health risk from hypertension
    if alertness < 0.7 and hypertension < 0.03 and time_since_slept < 4:
        return 1  # Drink coffee to boost alertness safely

    # Moderate beer drinking, only when intoxication and hypertension are minimal risks
    if alertness > 0.85 and intoxication < 0.01 and hypertension < 0.01:
        return 2  # Beer is a rare treat under safe conditions

    # Just work under normal conditions
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)