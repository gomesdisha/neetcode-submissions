class Solution:

    def encode(self, strs: List[str]) -> str:
        enco = ""

        """for s in strs:
            enco.append(str(len(s)))
            enco.append("#")
            enco.append(s)

        return "".join(enco)"""
        for s in strs:
            enco += str(len(s))+"#"+s
        return enco


    def decode(self, s: str) -> List[str]:
        deco = []
        i = 0
        # lets say: s = 3#dis4#shey

        while i < len(s):
            j = i

            while s[j]!="#":
                j += 1

            length = int(s[i:j]) #takes size of word, 
            deco.append(str(s[j+1:length+j+1]))#after # to end of word

            i=length+j+1
        return deco


        
