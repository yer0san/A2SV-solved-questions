class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        holder = defaultdict(list)

        for path in paths:
            cleaned = path.split()
            root = cleaned[0]

            for f in cleaned[1:]:
                file_name = []
                content = ""
                for i, l in enumerate(f):
                    if l == "(":
                        content = f[i+1:len(f)-1]
                        break
                    file_name.append(l)
                file_name = "".join(file_name)
                holder[content].append(root+"/"+file_name)
        
        res = [lis for lis in holder.values() if len(lis) > 1]
        return res
