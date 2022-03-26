import multiprocessing
import time


def counter(n):
    while True:
        n.value += 1


def readcounter(n, interval):
    while True:
        time.sleep(interval) #delay function
        print('value in process 2', n.value)



if __name__ == '__main__':
    num = multiprocessing.Value('d', 0.0)
    
    print('Value before the process starts: {} '.format(num.value))
    
    
    p1 = multiprocessing.Process(target = counter, args = (num,))
    p1.start()
    

    delay = 5 #in seconds, so that not all time we have a print
    p2 = multiprocessing.Process(target = readcounter, args = (num, delay))
    p2.start()


