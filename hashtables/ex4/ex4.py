# create a dict
# sort the list of items from positive to negative
# goes through sorted list
# checks if item is in dict
# if no then add item as a key with value of None
# if its in there then do nothing
# once it comes to


def has_negatives(a):
    # num_dict = {}
    # a.sort(reverse=True)
    # print(a)
    # for n in a:
    #     if n == 0:
    #         continue
    #     if n > 0:
    #         if num_dict.get(n):
    #             continue
    #         else:
    #             num_dict[n] = None
    #     else:
    #         print('called')
    #         if num_dict.get(abs(n)):
    #             print('called again')
    #             num_dict[n] = n
    # print(num_dict)
    # # return result
    pass


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
