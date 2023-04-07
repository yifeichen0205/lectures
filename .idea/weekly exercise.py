import pandas as pd

df = pd.DataFrame(
    {
        'col1':range(10),
        'col2':range(10,20)
    },
    index=list('acgfgidheb')
)
#result=df.loc[{'b','c','d','e'}],[col]
print(df)

df =pd.DataFrame(
    {
        'col1':range(0,20),
        'col2':range(20,40),
        'col3':range(40,60)
    }
)

rows = list(range(0,len(df),2))
result=df.iloc[rows,[1]]
print(result)
print(df)
