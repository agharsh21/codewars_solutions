def find_outlier(integers):
    evenlist= [n for n in integers if n%2==0]
    oddlist = [n for n in integers if n%2!=0]
    if len(oddlist)== 1:
        return oddlist[0]
    else:
        return evenlist[0]