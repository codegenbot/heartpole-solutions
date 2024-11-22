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

    # Prioritize sleep for poor health conditions
    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 12:
        print(3)  # sleep
    # Use coffee to boost alertness only if recent sleep is not too lacking
    elif alertness < 0.5 and time_since_slept < 10:
        print(1)  # drink coffee and work
    # Safe to work if health parameters are within a comfortable threshold
    elif alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.2:
        print(0)  # just work
    else:
        print(3)  # fallback to sleep if unsure