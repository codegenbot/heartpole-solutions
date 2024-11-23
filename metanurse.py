import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if there's a significant health risk
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep to offset health issues

    # Sleep if awake too long or alertness critically low
    if time_since_slept > 16 or alertness < 0.2:
        return 3

    # Drink coffee if low alertness and early in the day
    if alertness < 0.5 and time_elapsed < 8:
        return 1

    # Moderate intoxication and less than 50% work done, take a break with beer
    if intoxication <= 0.3 and work_done < 0.5 and time_elapsed < 12:
        return 2

    # Work if health is good, alertness okay, and work is incomplete
    if (
        alertness >= 0.5
        and hypertension <= 0.3
        and intoxication <= 0.2
        and work_done < 0.9
    ):
        return 0

    # Always rest if alertness is too low later in the day
    if alertness < 0.4 and time_elapsed > 12:
        return 3

    # Default action: Work if capable, otherwise rest
    return 0 if alertness > 0.6 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)