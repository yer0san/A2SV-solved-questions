class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        holder = defaultdict(int)

        for domain in cpdomains:
            cleaned = domain.split()
            visited = int(cleaned[0])
            holder[cleaned[1]] += visited
            for i, l in enumerate(cleaned[1]):
                if l == ".":
                    holder[cleaned[1][i+1:]] += visited
        res = [f"{val} {dom}" for dom, val in holder.items()]
        return res
