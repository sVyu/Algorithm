import pandas as pd
num = pd.Series([2, 6, 7, 8, 9, 9, 11])

interpolation = "lower"
print(num.quantile(.25)) #25%(Q1) 값
#print(num.describe()) #데이터 요약 