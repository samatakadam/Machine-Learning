def calculate_quartiles(data):
    
    data.sort()
    n = len(data)
    Q1 = data[n // 4]
    Q3 = data[3 * n // 4]
    IQR = Q3 - Q1
    return Q1, Q3, IQR

def get_bounds(Q1, Q3, IQR):
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

def detect_outliers(data):
   
    Q1, Q3, IQR = calculate_quartiles(data)
    lower, upper = get_bounds(Q1, Q3, IQR)
    return [x for x in data if x < lower or x > upper]

def main():
    salary = [25000, 27000, 29000, 31000, 50000, 100000]
    outliers = detect_outliers(salary)
    print("Outliers in Salary:", outliers)


if __name__=="__main__":
    main()