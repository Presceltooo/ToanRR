# Thuật toán sinh dãy nhị phân dài n
def generate_binary_sequence(n):
    if n <= 0:
        return []

    result = []
    generate_binary_sequence_recursive(n, "", result)
    return result

def generate_binary_sequence_recursive(n, current, result):
    if n == 0:
        result.append(current)
        return
    generate_binary_sequence_recursive(n - 1, current + "0", result)
    generate_binary_sequence_recursive(n - 1, current + "1", result)

# Ví dụ với n = 5
n_value = 5
binary_sequences = generate_binary_sequence(n_value)

print(f"Binary sequences of length {n_value}:")
for sequence in binary_sequences:
    print(sequence)