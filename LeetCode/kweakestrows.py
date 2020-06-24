class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sorting = []
        for i in range(len(mat)):
            x = mat[i]
            strength = i
            for j in range(len(x)):
                strength += 1000 * x[j]
            sorting.append( (i, strength) )
        sorting.sort(key=lambda s: s[1])
        return [i[0] for i in sorting[0:k]]
        