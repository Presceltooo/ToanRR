# Thuật toán sinh tất cả các hoán vị của n phần tử
def generate_permutations(n):
    # Tạo một danh sách chứa các số từ 1 đến n
    elements = list(range(1, n + 1))
    
    # Khởi tạo một danh sách kết quả rỗng
    result = []
    
    # Gọi hàm đệ quy để sinh hoán vị
    generate_permutations_recursive(elements, 0, result)
    
    return result

def generate_permutations_recursive(elements, current_index, result):
    if current_index == len(elements) - 1:
        # Nếu đã đến cuối danh sách, thêm một hoán vị mới vào danh sách kết quả
        result.append(elements.copy())
        return
    
    for i in range(current_index, len(elements)):
        # Hoán đổi phần tử hiện tại với mỗi phần tử sau nó
        elements[current_index], elements[i] = elements[i], elements[current_index]
        
        # Gọi đệ quy để tiếp tục sinh hoán vị với các phần tử còn lại
        generate_permutations_recursive(elements, current_index + 1, result)
        
        # Hoàn tác hoán đổi để quay lại trạng thái trước đó
        elements[current_index], elements[i] = elements[i], elements[current_index]

# Ví dụ với n = 5
n_value = 5
permutations = generate_permutations(n_value)

print(f"Permutations of {n_value} elements:")
for permutation in permutations:
    print(permutation)
