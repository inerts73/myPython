import copy

# P(n,k) for nums where n is len(nums)
nums = [1,2,3]
k = len(nums)
basket = [None]*k
results = []

def add_basket_to_results(members, basket_len):
    if basket_len == 0:
        basket_copy = copy.deepcopy(basket)
        if basket_copy not in results:
            results.append(basket_copy)
        return

    for i in range(len(members)):
        basket[basket_len - 1] = members[i]
        members_copy = copy.deepcopy(members)
        members_copy.pop(i)
        add_basket_to_results(members_copy, basket_len - 1)


add_basket_to_results(nums, k)
print sorted(results)