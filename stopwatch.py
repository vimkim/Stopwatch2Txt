import time

def stopwatch(seconds):
    start = time.time()
    time.clock()    
    count_file = open("secs.txt","r")
    lines = count_file.readlines()
    count_file.close()
    elapsed_init = int(lines[0])
    while (True):
        elapsed = time.time() - start + elapsed_init
        m, s = divmod(elapsed, 60)
        h, m = divmod(m, 60)
        print("%02d:%02d:%02d" % (h,m,s))
        print("loop cycle time: %f, seconds count: %d" % (time.clock() , elapsed))
        text_file = open("stopwatch.txt","w")
        text_file.write("%02d:%02d:%02d\n" % (h,m,s))
        text_file.close()
        count_file = open("secs.txt","w") 
        count_file.write(str(int(elapsed)))
        count_file.close()
        time.sleep(1)  


stopwatch(20)
