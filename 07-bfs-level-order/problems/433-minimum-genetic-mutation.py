from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Finds the minimum number of mutations from startGene to endGene.
        Uses BFS to find the shortest path in an unweighted gene-bank graph.
        
        Time Complexity: O(B * L * 4) -> O(B), where B = bank size, L = gene length (8)
        Space Complexity: O(B) -> for the queue, visited set, and bank set
        """
        # If endGene is not valid (not in bank), it's impossible to reach
        if endGene not in bank:
            return -1
        
        bank_set = set(bank)
        allowed_chars = ['A', 'T', 'C', 'G']
        
        queue = deque([startGene])
        visited = {startGene}
        
        mutation_count = 0
        
        while queue:
            mutation_count += 1
            # Process current level (all genes at mutation_count - 1 distance)
            level_size = len(queue)
            
            for _ in range(level_size):
                gene = queue.popleft()
                
                # Generate all possible 1-character mutations
                for i in range(len(gene)):
                    gene_list = list(gene)
                    for char in allowed_chars:
                        if char != gene[i]:
                            gene_list[i] = char
                            mutated_gene = "".join(gene_list)
                            
                            if mutated_gene == endGene:
                                return mutation_count
                            
                            # If the mutation is valid and hasn't been visited
                            if mutated_gene in bank_set and mutated_gene not in visited:
                                queue.append(mutated_gene)
                                visited.add(mutated_gene)
        
        return -1
