# def isSorted(arr, start=-1, end=-1):
#     if (start == -1):
#         for i, elem in enumerate(arr[1:]):
#             if (arr[i] > elem):
#                 return False
#         return True
#     else:
#         if ((end == len(arr) - 1 or arr[end] < arr[end + 1])
#                 and (start == 0 or arr[start] > arr[start - 1])):
#             return True
#         else:
#             return False


# def almostSorted(arr):
#     inds = list()
#     increasing = True
#     buffer = list()
#     for i, elem in enumerate(arr[1:]):
#         if (len(inds) > 2):
#             print("no")
#             return
#         if (increasing):
#             if (elem < arr[i]):
#                 increasing = False
#                 buffer.append(i)
#                 if (i == len(arr[1:]) - 1):
#                     buffer.append(i + 1)
#                     inds.append(buffer)
#                     break
#         else:

#             if(elem > arr[i]):
#                 increasing = True
#                 buffer.append(i)
#                 inds.append(buffer)
#                 buffer = list()
#                 # if (len(inds) > 2 or
#                 #         (len(inds) == 2 and
#                 #          (inds[0][1] - inds[0][0] > 1 or
#                 #           inds[1][1] - inds[1][0] > 1))):
#                 #     print("no")
#             else:
#                 if (i == len(arr[1:]) - 1):
#                     buffer.append(i + 1)
#                     inds.append(buffer)
#                     break

#     if (len(inds) == 0):
#         print("no")
#         return
#     if (len(inds) == 1):
#         start = 0 if inds[0][0] == 0 else inds[0][0] - 1
#         end = len(arr) - \
#             1 if inds[0][1] == len(arr) - 1 else inds[0][1] + 1
#         if (inds[0][1] - inds[0][0] == 1):
#             temp = arr[inds[0][0]]
#             arr[inds[0][0]] = arr[inds[0][1]]
#             arr[inds[0][1]] = temp
#             if (isSorted(arr[start:end + 1])):
#                 print("yes")
#                 print("swap", inds[0][0] + 1, inds[0][1] + 1)
#                 return
#         else:
#             # arr[inds[0][0]:inds[0][1]] = arr[inds[0][0]:inds[0][1]][::-1]
#             temp = arr[inds[0][0]]
#             arr[inds[0][0]] = arr[inds[0][1]]
#             arr[inds[0][1]] = temp
#             if (isSorted(arr, inds[0][0], inds[0][1])):
#                 print("yes")
#                 if (inds[0][1] - inds[0][0] == 2):
#                     print("swap", inds[0][0] + 1, inds[0][1] + 1)
#                     return
#                 print("reverse", inds[0][0] + 1, inds[0][1] + 1)
#                 return
#             else:
#                 print("no")
#             return

#     if (len(inds) == 2):
#         if (inds[0][1] - inds[0][0] == 1 and
#                 inds[1][1] - inds[1][0] == 1):
#             if (inds[1][1] == len(arr) - 1):
#                 inds[1][0] += 1
#             temp = arr[inds[0][0]]
#             arr[inds[0][0]] = arr[inds[1][1]]
#             arr[inds[1][1]] = temp
#             for ind in inds:
#                 start = 0 if ind[0] == 0 else ind[0] - 1
#                 end = len(arr) - \
#                     1 if ind[1] == len(arr) - 1 else ind[1] + 1
#                 if (not isSorted(arr[start:end + 1])):
#                     print("no")
#                     return
#             else:
#                 print("yes")
#                 print("swap", inds[0][0] + 1, inds[1][1] + 1)
#                 return
#     print("no")
#     return

# print([i for i in range(0)])

# # for the LIS
# r = upto
# l = startAt
# while (r - l > 1):
#     m = l + (r - l)//2
#     if (arr[m] >= elem):
#         r = m
#     else:
#         l = m
# return r - 1

# mid = math.ceil((upto + startAt) / 2)

# if (upto - startAt <= 1):
#     return startAt

# elif (elem >= arr[mid]):
#     return binarySearch(arr, mid, upto, elem)
# else:
#     return binarySearch(arr, startAt, mid - 1, elem)