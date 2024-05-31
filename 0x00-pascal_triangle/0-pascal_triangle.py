#pascal triangle 

def pascal(n):
    row = [1]
    for x in range(n):
        row.append(int(row[x] * (n-x) / (x+1)))
    return row
    

def pascal_triangle(n):
    if n <= 0:
        return []
    return [pascal(nth) for nth in range(n)]
