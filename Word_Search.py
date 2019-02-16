class Solution:
    
    def found_word(self, word, index, board, size, pos):
        
        #base case
        #search went out of "bounds", some char of the word cannot be found on the board
        if not(pos[0] in range(size[0])) or not(pos[1] in range(size[1])):
            return False 
        
        if board[pos[0]][pos[1]] == '*':
            return False
        
        #current char not found
        if board[pos[0]][pos[1]] != word[index]:
            return False
        
        #current char found in the postion, recur and check for other chars in the word
       
        if index in range(len(word)-1):
            up    = self.found_word(word, index+1, board, size, (pos[0]-1, pos[1]))
            down  = self.found_word(word, index+1, board, size, (pos[0]+1, pos[1]))
            left  = self.found_word(word, index+1, board, size, (pos[0], pos[1]-1))
            right = self.found_word(word, index+1, board, size, (pos[0], pos[1]+1))
            
            return (up or down or right or left)
            
        #this was perhaps the last char
        return True
        
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        
        found = []
        
        m,n = len(board), len(board[0])
        
        for w in words:
            for i in range(m):
                for j in range(n):
                    if self.found_word(w, 0, board, (m,n), (i,j)):
                        found.append(w)
        found = set(found)
        return list(found)
        
