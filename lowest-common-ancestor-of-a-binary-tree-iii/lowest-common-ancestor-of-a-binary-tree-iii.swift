/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var left: Node?
 *     public var right: Node?
 *     public var parent: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *         self.parent = nil
 *     }
 * }
 */

class Solution {
    func lowestCommonAncestor(_ p: Node?,_ q: Node?) -> Node? {
        
        var seen: Set<Int> = []
        var a:Node? = p
        var b:Node? = q
        
        while a != nil {
            seen.insert(a?.val ?? 0)
            a = a?.parent
        }
        
        while b != nil {
            if seen.contains(b?.val ?? 0) {
                return b
            }
            b = b?.parent
        }
        
        return a
    }
}