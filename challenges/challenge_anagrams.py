def is_anagram(first_string, second_string):
    return sort(first_string.lower()) == sort(second_string.lower())


def merge(merge, left_sort, right_sort):
    to_the_left, to_the_right = 0, 0

    while to_the_left < len(left_sort) and to_the_right < len(right_sort):

        if left_sort[to_the_left] <= right_sort[to_the_right]:
            merge[to_the_left + to_the_right] = left_sort[to_the_left]

            to_the_left += 1
        else:
            merge[to_the_left + to_the_right] = right_sort[to_the_right]

            to_the_right += 1

    for to_the_left in range(to_the_left, len(left_sort)):
        merge[to_the_left + to_the_right] = left_sort[to_the_left]

    for to_the_right in range(to_the_right, len(right_sort)):
        merge[to_the_left + to_the_right] = right_sort[to_the_right]

    return "".join(merge)


def sort(string):
    if len(list(string)) <= 1:
        return list(string)

    left_sort = sort(list(string)[:(len(list(string)) // 2)])
    right_sort = sort(list(string)[(len(list(string)) // 2):])

    return merge(list(string).copy(), left_sort, right_sort)
