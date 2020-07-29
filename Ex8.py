def Count (Year, Month, Day):
    Months_List = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
        Months_List[1] = 29
    count = sum(Months_List[:Month-1])
    count += Day
    return count
