class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # take the current value of our node (self.value)
        # compare that to the value we want to insert

        # if new value is less than current value
        if value < self.value: 
            
            # if self.left is None then set the left child with the new node to new value
            if self.left is None:
                self.left = BSTNode(value)
            
            #  else self.left is already taken by another node
            # then make that node call insert
            else:
                self.left.insert(value)
        
        # if new value is >= self.vale
        if value >= self.value: 

            # if self.right is None then set the right child with the new node to new value
            if self.right is None:
                self.right = BSTNode(value) 
         
            # else self.right is already taken by another node
            # then make that node call insert
            else:
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        # initalize a variable found to False
        found = False

        # if current value is greater than target 
        if self.value >= target:
            # check the left subtree

            # if you cannot go left then return false
            # if left is None then return False
            if self.left == None:
                return False

            found = self.left.contains(target)
        
        # if current value less than target 
        if self.value < target:
            # check the right subtree

            # if you cannot go right then return false
            # if right is None then return False

            if self.right == None:
                return False 

            found = self.right.contains(target)
        
        return found

