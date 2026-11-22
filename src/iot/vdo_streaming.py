import subprocess as sub
import multiprocessing as mp


#subprocess.run("python real_time.py & python real_time_exit.py", shell=True)
def enter(q):
    sub.run(q)
def exit(w):
    sub.run(w)
if __name__=='__main__':
    # Run keyboard control and camera preview concurrently as separate processes.
    en = mp.Process(target=enter,args=(["python3","-m","src.iot.keyboard_control"],))
    ex = mp.Process(target=exit,args=(["python3","-m","src.vision.camera"],))
    en.start()
    ex.start()
    en.join()
    ex.join()