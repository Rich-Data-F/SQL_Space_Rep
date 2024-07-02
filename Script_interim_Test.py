row_1=[column_title_1,column_title_2,column_title_3]
row_2=[3,4,5]
row_3=[2,5,3]
row_4=[2,5,3]
nb_rows=4

data=dataframe()
for i in nb_rows:
    current_row=row_+i
    data=data.append(current_row)

data.head()