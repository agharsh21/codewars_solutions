def expanded_form(num):
    listss = []
    power = 0
    while num > 0:
        if num % 10 != 0:
            listss.append(num % 10 * (10 ** power))
        num = num // 10
        power += 1
    listss.sort(reverse=True)
    for n in range(len(listss)):
        listss[n] = str(listss[n])
    return " + ".join(listss)
