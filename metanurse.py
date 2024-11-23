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

    # Strict health caution with adjusted thresholds
    if hypertension > 0.35 or intoxication > 0.2 or time_since_slept > 8:
        print(3)  # sleep
    elif alertness < 0.5 and hypertension < 0.2 and time_since_slept <= 8:
        print(1)  # drink coffee and work
    elif alertness >= 0.7 and hypertension < 0.2 and intoxication < 0.1:
        print(0)  # just work
    elif 0.15 <= intoxication < 0.2:
        print(2)  # drink beer and work
    else:
        print(3)  # fallback to sleep for uncertain situations