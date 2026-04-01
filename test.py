import pandas as pd
dict_vendas = {
    'id': [1,2,3],
    'valor': [2,4.5,7.6]
}
print(dict_vendas)

df = pd.DataFrame(dict_vendas)
print(df) #--