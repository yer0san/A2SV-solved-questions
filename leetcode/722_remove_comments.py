class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_comment = False
        holder = []
        for line in source:

            if not in_comment and len(line) == 1:
                holder.append(line[0])
            i = 1
            while i < len(line):

                if not in_comment and line[i] == '*' and line[i-1] == '/':
                    i += 2
                    in_comment = True

                if not in_comment and line[i] == '/' and line[i-1] == '/':
                    break
                elif not in_comment:

                    holder.append(line[i-1])
                    if i+1 == len(line):
                        holder.append(line[i])
                    i += 1
                    continue
                
                if in_comment:
                    if line[i] == '/' and line[i-1] == '*':
                        in_comment = False
                        i += 1
                        if len(line[i::]) == 1:
                            holder.append(line[i])
                            break
                        
                    i += 1
                    
            if not in_comment:
                if (len(holder) == 1 and holder[0] == "") or len(holder) == 0:
                    continue
                res.append("".join(holder))
                holder.clear()
        return res
