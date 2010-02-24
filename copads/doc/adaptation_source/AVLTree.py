class AVLTree: 
    def __init__(self, data): 
        self.data = data 
        self.set_childs(None, None) 
        
    def set_childs(self, left, right): 
        self.left = left 
        self.right = right 
        
    def balance(self): 
        lheight = 0 
        if self.left: 
            lheight = self.left.height() 
        rheight = 0 
        if self.right: 
            rheight = self.right.height() 
        return lheight - rheight 
        
    def height(self): 
        lheight = 0 
        if self.left: 
            lheight = self.left.height() 
        rheight = 0 
        if self.right: 
            rheight = self.right.height() 
        return 1 + max(lheight, rheight) 
    
    def rotate_left(self): 
        self.data, self.right.data = self.right.data, self.data 
        old_left = self.left 
        self.set_childs(self.right, self.right.right) 
        self.left.set_childs(old_left, self.left.left) 
        
    def rotate_right(self): 
        self.data, self.left.data = self.left.data, self.data 
        old_right = self.right 
        self.set_childs(self.left.left, self.left) 
        self.right.set_childs(self.right.right, old_right) 
        
    def rotate_left_right(self): 
        self.left.rotate_left() 
        self.rotate_right() 
        
    def rotate_right_left(self): 
        self.right.rotate_right() 
        self.rotate_left() 
        
    def do_balance(self): 
        bal = self.balance() 
        if bal > 1: 
            if self.left.balance() > 0: 
                self.rotate_right() 
            else: 
                self.rotate_left_right() 
        elif bal < -1: 
            if self.right.balance() < 0: 
                self.rotate_left() 
            else: 
                self.rotate_right_left() 
                
    def insert(self, data): 
        if data <= self.data: 
            if not self.left: 
                self.left = Node(data) 
            else: 
                self.left.insert(data) 
        else: 
            if not self.right: 
                self.right = Node(data) 
            else: 
                self.right.insert(data) 
        self.do_balance() 
        
    def print_tree(self, indent = 0): 
        print " " * indent + str(self.data) 
        if self.left: self.left.print_tree(indent + 2) 
        if self.right: self.right.print_tree(indent + 2) 