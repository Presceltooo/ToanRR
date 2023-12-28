import random
# Define the matrix size
n = 5
coefficient = 4

random.seed(coefficient)
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]
for i in range(n):
    matrix[i][i] = 0

# Print the matrix
print("Cost Matrix:")
for row in matrix:
    print(row)

# thuật toán sử dụng
def traveling_salesman(matrix):
    n = len(matrix)
    cities = list(range(n))

    def dfs(node, visited, path, cost, bound):
        nonlocal min_cost, min_path

        if len(visited) == n:
            # Nếu đã duyệt hết các thành phố
            cost += matrix[node][path[0]]  # Quay về thành phố xuất phát
            if cost < min_cost:
                min_cost = cost
                min_path = path[:]
            return

        # Duyệt qua tất cả các thành phố chưa thăm
        for next_node in cities:
            if next_node not in visited:
                new_bound = bound - matrix[node][path[-1]] - min(matrix[next_node])
                if cost + matrix[node][next_node] + new_bound < min_cost:
                    # Nếu chi phí hiện tại và ước lượng tối ưu có thể cắt nhánh
                    dfs(next_node, visited + [next_node], path + [next_node], cost + matrix[node][next_node], new_bound)

    min_cost = float('inf')
    min_path = []
    start_node = 0
    dfs(start_node, [start_node], [start_node], 0, sum(matrix[start_node]) - matrix[start_node][start_node])

    print("\nOptimal Tour:")
    print(min_path + [start_node])
    print("Optimal Cost:", min_cost)

traveling_salesman(matrix)
