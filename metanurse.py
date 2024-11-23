import sys

for line in sys.stdin:
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = map(float, line.split())

    # Immediate rest if any major health issue is detected
    if intoxication > 0.15 or hypertension > 0.3 or time_since_slept > 8:
        print(3)  # sleep
    # Use coffee sparingly to maintain alertness without impacting health
    elif alertness < 0.55 and hypertension < 0.25:
        print(1)  # drink coffee and work
    # Proceed with work only when all conditions are stable
    elif alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.05:
        print(0)  # just work
    else:
        print(3)  # default to sleep to improve safety