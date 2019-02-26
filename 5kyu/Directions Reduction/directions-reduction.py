def dirReduc(arr):
    n = 0
    while n < len(arr) - 1:
        if (arr[n] == "NORTH" and arr[n + 1] == "SOUTH") or (arr[n] == "SOUTH" and arr[n + 1] == "NORTH") or (
                arr[n] == "EAST" and arr[n + 1] == "WEST") or (arr[n] == "WEST" and arr[n + 1] == "EAST"):
            del arr[n + 1]
            del arr[n]
            n = 0
        else:
            n = n + 1
    return arr
