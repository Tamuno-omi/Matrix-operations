class Matrix:
    """ Matrix class for calculcating various matrix operations
    
    Attributes
    height(int) : number of rows in matrix
    width(int)  : number of columns in matrix
    data(list)  : list containing matrix
    """
    def __init__(self,rows,columns):
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
