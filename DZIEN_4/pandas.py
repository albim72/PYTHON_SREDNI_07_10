import pandas as pd

data = {
    'jabłka':[3,2,1,0,9,2],
    'gruszki':[2,1,0,0,3,1],
    'śliwki':[1,0.4,0,0.7,2.2,1.2]
}

pr = pd.DataFrame(data)
print(pr)


pr = pd.DataFrame(data,index=['Jan','Nadia','Olga','Leon','Anna','Marek'])
print(pr)

pr.to_csv('newf.csv')
print(pr.info())

ndf = pd.read_csv('newf.csv')
print(ndf)
