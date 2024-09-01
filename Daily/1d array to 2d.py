# <!-- 2022. Convert 1D Array Into 2D Array

# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible -->

class Solution:
    def construct2DArray(self, original, m, n):
        result = [[] for _ in range(m)]
        i = 0
        match m * n == len(original):
            case True:
                while i < m:
                    result[i] = original[i * n:(i * n + n)]
                    i += 1
            case _:
                return []
        return result

def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        original = json.loads(lines[i*3])
        m = int(lines[i*3 + 1])
        n = int(lines[i*3 + 2])
        
        result = Solution().construct2DArray(original, m, n)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
