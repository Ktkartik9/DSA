# Problem: Majority Element

# Method: Boyer-Moore Voting Algorithm


# Logic: 
      """Maintain a candidate and a count
      Traverse the array; if the count is zero
      pick the current element as the new candidate
      Increment the count if the element matches the candidateotherwise decrement
      The remaining candidate is the majority element"""

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
