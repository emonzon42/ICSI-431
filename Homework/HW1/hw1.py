'''
Eli M.
ICSI 431
9.20.20
HW 1
'''
import numpy as np
import matplotlib.pyplot as pp

#https://www.youtube.com/watch?v=I_biaTE2_YA
#* Load data from online repo

def main():
    #a)
    data = load('Homework/HW1/cloud.data.txt')
    center(data) 

    #b)
    cov = np.cov(data) #* covar(data) 
    #print(cov)
    #print(np.cov(data))
    
    #c) 
    eigvals, eigmat = np.linalg.eig(cov)
    
    #d)
    r = find_r(eigvals)
    print(r)

    #e)
    xvals = np.arange(0,1024)
    print(xvals)
    for i in [0,1]:
        yvals = eigmat[i,:len(xvals)]
        pp.plot(xvals,yvals)
    pp.xlabel('Dimensions')
    pp.ylabel('Magnitude of Components')
    pp.show()
    saveComp(eigmat[:,:2])

    '''#f)
    A = [np.transpose(eigmat[r]*data[i] for i in np.arange(0,len(data[0])-1))]
    xvals = eigmat[:r,r]
    for i in np.arange(i,r):
        yvals = eigmat[i,r]

    pp.plot(xvals,yvals,'o')
    '''

    

def load(fn):
    return np.loadtxt(fn,skiprows=53,max_rows=1024)

def center(data):
    mu =  np.mean(data,axis=0)
    data -= mu

def covar(Z): #! Doesn't work as intended yet
    return 1/len(Z) * np.dot(np.transpose(Z),Z)
    'covar'

def find_r(eigvals, alpha=None):
    if alpha is None:
        alpha = .9

    total_var = np.sum(eigvals)
    r = 0
    for eig in eigvals:
        r+=1
        if eig/total_var >= alpha:
            break

    return r

def saveComp(compon):
    with open('Components.txt','wt') as file:
        j = 0
        for i in [1,2]:
            for j in np.arange(0,len(compon)):
                file.write(str(compon[j,:i]))
                file.write(',')
            file.write('\n')
'''
def center(fn):
    'loads nd centers data'
    data = []
    useful = False
    with open(fn, "rt") as file:
        for line in file:
            if line == ';;; CLOUD COVER DB #1' or line.split(' ')[0] == ';;;':
                useful = not useful
                continue
            if useful and line != ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n':
                data.append(line[0:len(line)-1])
        #print (line.split(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')[0])
    print(data)
    file.close()
    return data
    '''

if __name__ == "__main__":
    main()