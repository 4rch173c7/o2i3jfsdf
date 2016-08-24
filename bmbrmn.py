# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import sys

def getData():
    data = ""
  
    for line in fileinput.input():
        data+=line

    return data
    
class BomberMan(object):
    
    def __init__(self):
        data = getData()
        setup = data.split('\n', 1)[0]
        self.initMatrix = data.split('\n')[1:]
        
        self.j, self.i, self.N = [int(i) for i in setup.split(' ')]
        self.N+=1
        
        self.matrix = self.convertMatrix(1)
        self.timeMatrix = self.convertMatrix(4)
        self.actionMatrix = self.updateActions()
    
    def convertMatrix(self, setVal):
        outputMatrix = [[0 for i in range(self.i)] for j in range(self.j)]
        j, i = 0, 0
        
        for line in self.initMatrix:
            for entry in line:
                if entry == '.':
                    outputMatrix[j][i] = 0
                else:
                    outputMatrix[j][i] = setVal
                i+=1
            j+=1
            i=0
            
        return outputMatrix
    
    def tickDown(self):
        tempMatrix = list(self.timeMatrix)
        j,i = 0,0
        
        for row in self.timeMatrix:
            for entry in row:
                if entry != 0:
                    tempMatrix[j][i] = entry-1
                i+=1
            j+=1
            i=0
            
        return tempMatrix
    
    def updateActions(self):
        """ Update the actions matrix
        
        Note: 
            t(1) = explode, t(2) = setbomb, t(3) = do nothing
        
        """
        tempMatrix = [["NAN" for i in range(self.i)] for j in range(self.j)]
        j,i = 0,0
        
        for row in self.timeMatrix:
            for entry in row:
                # do nothing (this is t=3)
                if entry == 4:
                    tempMatrix[j][i] = "SXP" # set to explode
                if entry == 3:
                    tempMatrix[j][i] = "WTG" # waiting phase
                if entry == 2:
                    tempMatrix[j][i] = "SET" # set empty bombs
                if entry == 1:
                    tempMatrix[j][i] = "EXP" # explode bombs
                i+=1
            j+=1
            i=0
        
        return tempMatrix
    
    def setBombs(self):
        j,i = 0,0
        
        for row in self.matrix:
            for entry in row:
                if entry == 0:
                    self.matrix[j][i] = 1
                    self.actionMatrix[j][i] = 'SXP'
                    self.timeMatrix[j][i] = 4
                i+=1
            j+=1
            i=0
            
    def checkSetBombs(self):
        setBombs = False
        
        for row in self.actionMatrix:
            for entry in row:
                if entry == 'SET':
                    setBombs = True
        
        return setBombs
    
    def explode(self):
        j,i = 0,0
        shrapnel = []

        for row in self.matrix:
            for entry in row:
                if entry == 1:
                    if self.actionMatrix[j][i] == 'EXP':
                        # explode above
                        if j > 0:
                            shrapnel.append((j-1, i))
                        # explode below
                        if j < self.j-1:
                            shrapnel.append((j+1, i))
                        # explode to left
                        if i > 0:
                            shrapnel.append((j, i-1))
                        if i < self.i-1:
                            shrapnel.append((j, i+1))
                        self.matrix[j][i] = 0
                        self.timeMatrix[j][i] = 0
                        self.actionMatrix[j][i] = 'NAN'
                i+=1
            j+=1
            i=0
        for item in shrapnel:
            self.matrix[item[0]][item[1]] = 0
            self.timeMatrix[item[0]][item[1]] = 0
            self.actionMatrix[item[0]][item[1]] = 'NAN'
    
    def checkSetExplode(self):
        setExplode = False
        
        for row in self.actionMatrix:
            for entry in row:
                if entry == 'EXP':
                    setExplode = True
                    
        return setExplode
    
    def executeActions(self):
        if self.checkSetExplode() == True:
            self.explode()
        
        if self.checkSetBombs() == True:
            self.setBombs()
    
    def printFinalMatrix(self):
        j,i =0,0
        
        line = ""
        
        for row in self.matrix:
            for entry in row:
                if entry == 0:
                    line+=('.')
                if entry == 1:
                    line+=('O')
            print line
            line = ""
    
    def start(self):
        while self.N != 0:
            # update actions
            self.actionMatrix = self.updateActions()
            
            # execute executable actions
            self.executeActions()
            
            # switch time down
            self.tickDown()
            
            self.N -=1
            
        self.printFinalMatrix() 

bomber = BomberMan()
bomber.start()
