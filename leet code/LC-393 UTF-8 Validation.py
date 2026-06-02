class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        binary = []

        for k in data:
            binary.append(format(k, '08b'))
      
        i = 0
        while i < len(binary):
            string = binary[i]

            j = 0
            cnt = 0

            while j < 8 and string[j] == '1':
                cnt += 1
                j += 1
            
            if cnt == 0:
                i += 1
                continue
            
            if cnt == 1 or cnt > 4:
                return False
            
            if i + cnt > len(binary):
                return False
                
            valid = True
            for r in range(i + 1, i + cnt):
                if binary[r][:2] != '10':
                    valid = False
                
            if not valid:
                return False
            
            i += cnt    
        else:
            return True

