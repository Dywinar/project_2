import pandas as pd
data = pd.read_csv('/content/Housing.csv')
data[data['price'] == data['price'].min()]['bedrooms'].min()
#Вопрос 1: 2
len(data[data['bedrooms'] <= data['bathrooms']])
#Вопрос 2: 15
data[data['guestroom'] == 'yes']['price'].min()
#Вопрос 3: 2450000
data_for_cena = data[((data['price'] >= 500000) | (data['price'] <= 200000))]
data_with_airconditioning = data_for_cena[data_for_cena['airconditioning']=='yes']
print(len(data_with_airconditioning))
#Вопрос 4: 172 дома ценой от 5.000.000 или до 2.000.000 денег могу похвастаться  кондиционированием воздуха 

#chast_with_airconditioning = len(data_with_airconditioning)/len(data_for_cena)*100
#print(chast_with_airconditioning)
#тут еще нашел процент с кондиционером