##Session 5!
import numpy as np 

if __name__ == "__main__": 
    T= np.linspace(0,2*np.pi,num=1000)
    U= np.sin(T)
    U= np.sin(90*np.pi/180)
    print("THIS IS X! (0..2pi with 1000 entries)\n")
    print(T)
    print("THIS IS SIN(X)!\n")
    print(U)
    print("This makes sense since sin of x can only complete once before 2 pi.")
