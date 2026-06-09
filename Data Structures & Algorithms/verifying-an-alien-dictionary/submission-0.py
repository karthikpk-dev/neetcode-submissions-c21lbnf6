class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map={}

        for i in range(len(order)):
            map[order[i]]=i+1


        def compare(word1,word2):
            
            min_len=min(len(word1),len(word2))
            i=0
            while i<min_len:
                if map[word1[i]] < map[word2[i]]:
                    return True
                if map[word1[i]]>map[word2[i]]:
                    return False
                i+=1
            if len(word1)>len(word2):
                return False
            return True

        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]

            if not compare(word1,word2):
                return False
        return True
        
