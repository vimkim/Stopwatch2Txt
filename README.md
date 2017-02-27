# Stopwatch2Txt
A simple stopwatch application that writes timestamp to txt file (usage example: OBS streaming).

## How to use?

1. Replace (manually) the first line of 'secs.txt' with your preferred starting seconds (in integer form). To initialize the stopwatch, this should be '0'.
However, if you want a very specific starting point such as '01:05:12', type '3912' (= 1*3600+ 5*60 + 12).
2. Run the python code 'stopwatch.py' by typing the followind command inside the terminal:


    python3 stopwatch.py

3. That's it! If you check the 'stopwatch.txt' file, you will see that the file is constantly being updated. You can use this whereever you want. e.g. OBS text source


