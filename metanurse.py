import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if critical health indicators are too high
    if hypertension > 0.3 or intoxication > 0.2:
        return 3

    # Consider sleep if very low alertness or prolonged wakefulness
    if time_since_slept > 6 or alertness < 0.25:
        return 3

    # Use coffee more cautiously, only when alertness is low, early, and safe
    if alertness < 0.35 and time_elapsed < 5 and hypertension < 0.15:
        return 1

    # Allow beer only when intoxication is negligible and other metrics favor it
    if intoxication <= 0.05 and alertness < 0.4 and work_done < 0.4 and time_elapsed < 7:
        return 2

    # Work primarily when alertness is adequate and health metrics are stable
    if alertness >= 0.35 and hypertension <= 0.15 and intoxication <= 0.05 and work_done < 0.8:
        return 0

    # Use sleep as a recovery option in late hours with low alertness
    if alertness < 0.3 and time_elapsed > 7:
        return 3

    # Default to working if moderate alertness is achieved, else prioritize sleep
    return 0 if alertness >= 0.3 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)