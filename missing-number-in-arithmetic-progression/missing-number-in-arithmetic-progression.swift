class Solution {
    func missingNumber(_ arr: [Int]) -> Int {
        return (arr.first! + arr.last!) * (arr.count + 1) / 2 - arr.reduce(0, +)
    }
}

//         (arr.first! + arr.last!)*(arr.count+1)/2 - arr.reduce(0, +)

/// Hello
