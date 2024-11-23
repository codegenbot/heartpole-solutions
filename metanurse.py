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

    # Prioritize sleep if health conditions are concerning
    if intoxication > 0.2 or hypertension > 0.4 or time_since_slept > 10:
        print(3)  # sleep
    # Use coffee to improve alertness judiciously
    elif alertness < 0.6 and time_since_slept < 8 and hypertension < 0.3:
        print(1)  # drink coffee and work
    # Safe to work if health parameters are okay
    elif alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.1:
        print(0)  # just work
    else:
        print(3)  # fallback to sleep if unsure