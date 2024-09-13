// # You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

// # For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

// # Return an array answer where answer[i] is the answer to the ith query.


function xorQueries(arr: number[], queries: number[][]): number[] {
    const ans = []
    const prefix = [0, arr[0]]

    for (let i = 1; i < arr.length; i++)
        prefix.push(prefix[i] ^ arr[i])

    for (const [left, right] of queries)
        ans.push(prefix[left] ^ prefix[right + 1])

    return ans
};