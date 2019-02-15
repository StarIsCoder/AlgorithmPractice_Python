#   Given a string containing digits from 2-9 inclusive,
#   return all possible letter combinations that the number could represent
#
#   A mapping of digit to letters (just like on the telephone buttons) is given below.
#   Note that 1 does not map to any letters.
#
#   Input: "23"
#
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


def letterCombinations(digits):
    # Solution 1 start
    # mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    #            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # if len(digits) == 0:
    #     return []
    # if len(digits) == 1:
    #     return list(mapping[digits[0]])
    # prev = letterCombinations(digits[:-1])
    # print(prev)
    # add = mapping[digits[-1]]
    # return [s + c for s in prev for c in add]
    # Solution 1 end

    # Solution 2 start
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output
    # Solution 2 end


str = '234'
tmp = letterCombinations(str)
print(tmp)
