class Matrix:
    """ Matrix class for calculcating various matrix operations
    
    Attributes
    height(int) : number of rows in matrix
    width(int)  : number of columns in matrix
    data(list)  : list containing matrix
    """
    def __init__(self,rows = 2,columns =3):
        self.data = [[0 for x in range(columns)] for y in range(rows)]
        self.rows = rows
        self.columns = columns
        self.dimensions = (self.rows, self.columns)
    
    def get_height(self):
        """returns the matrix's height (number of rows)""" 
        return self.rows
    
    def get_width(self):
        """returns the matrix's width (number of columns)"""
        return self.columns
    
    def addMatrix(self,x,y):
        """ Matrix object for addition of two matrices
    
        Arguments
        x : first matrix
        y : second matrix
    
        Returns
        sum: addition of two matrices
        """
        if(len(x) == len(y) and len(x[0]) == len(y[0])):
            sum = [[0 for j in range(0,len(x[0]))] for i in range(0,len(x))]
            for i in range(0, len(x)):
                for j in range(0, len(x[0])):
                    sum[i][j] = x[i][j] + y[i][j]
            return sum

        else:
            error = "Matrices of different order"
            return error
    def showMatrix(self,x):
        """ Matrix object for displaying a Matrix
    
        Attributes
        x : matrix
    
        Returns
        x : prints out matrix
        """
        if isinstance(x, str) == False: #checking if return value is a string
            for i in range(0, len(x)):
                for j in range(0, len(x[0])):
                    print(x[i][j], end = ' ')

                print('\n')
        else:
            print(x)
            
    def subMatrix(self,x,y):
        """ Matrix object for subtraction of two matrices
    
        Arguments
        x : first matrix
        y : second matrix
    
        Returns
        sum: result of the subtraction of two matrices
        """
        if(len(x) == len(y) and len(x[0]) == len(y[0])):
            sum = [[0 for j in range(0,len(x[0]))] for i in range(0,len(x))]
            for i in range(0, len(x)):
                for j in range(0, len(x[0])):
                    sum[i][j] = x[i][j] - y[i][j]
            return sum

        else:
            error = "Matrices of different order"
            return error
     
    def multiplyMatrix(self,x, y):
        """ Matrix object for multiplication of two matrices
    
        Arguments
        x : first matrix
        y : second matrix
    
        Returns
        mult: result of the multiplication of two matrices
        """
        if(isinstance(x,(int, float)) == False):
            if(len(x[1]) == len(y)):
                mult = [[0 for j in range(len(y[0]))] for i in range(len(x))]
                for p in range(0, len(mult)):
                    for q in range(0, len(mult[0])):
                        for i in range(0, len(x[0])):
                            mult[p][q] += x[p][i]*y[i][q]
                return mult

            else:
                error = "Invalid Order of Matrices"
                return error
        else:
            for i in range(len(y)):
                for j in range(len(y[0])):
                    y[i][j] = x*y[i][j]
            return y   
        
    def inverseMatrix(self,x):
        """ Matrix object invert a matrix
    
        Arguments
        x : matrix
    
        Returns
        inv: inverse of matrix
        """
        det = detMatrix(x)
        inv = multiplyMatrix(1/det,adjMatrix(x))
        return inv        
#TODO : implement detMatrix() method
#TODO : implement cofactor() method
#TODO : implement adjMatrix() method

    def detMatrix(x):
        if(len(x) != len(x[0])):
            error = "Matrix is not square"
            return error
        det = 0
        order = len(x)

        if(order == 2):
            det = x[0][0]*x[1][1] - x[0][1]*x[1][0]
            return det
        else: #optimization required
            for j in range(0, len(x[0])):
                det += ((-1)**j)*x[0][j]*detMatrix(cofactor(x,0,j)) #Recursive call
            return det
    #extracting Co-factors and adjoint of addMatrix
    def cofactor(x,r,c):
        if(len(x) != len(x[0])):
            error = "Matrix is not square"
            return error
        order = len(x)
        cof = [[0 for x in range(0,order-1)] for y in range(0,order-1)]
        a , b = 0, 0
        for i in range(0,len(x)):
            if(i == r):
                continue
            b = 0
            for j in range(0, len(x[0])):
                if(j == c):
                    continue
                cof[a][b] = x[i][j]
                b = b + 1
            a = a +1
        return cof

    def adjMatrix(x):
        if(len(x) != len(x[0])):
            error = "Matrix is not square"
            return error
        adj = [[0 for a in range(0,len(x))] for b in range(0,len(x))]
        for i in range(0,len(x)):
            for j in range(0,len(x)):
                adj[i][j] = ((-1)**(i+j))*detMatrix(cofactor(x,i,j))
        adj = transposeMatrix(adj)
        return adj