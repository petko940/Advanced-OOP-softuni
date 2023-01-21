matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]

primary_diagonal = [matrix[x][x] for x in range(len(matrix))]
secondary_diagonal = [matrix[x][len(matrix) - 1 - x] for x in range(len(matrix))]

print(f"""Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}
Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}""")
