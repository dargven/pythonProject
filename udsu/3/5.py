##Дана строка с латинскими и русскими буквами. Преобразовать в ней все строчные буквы в прописные, а прописные – в строчные.
a = 'asdsadadADSDASDAfasfsdfasdjADKAhdФЫЫВФЫЛВФыфвыфвыфДЫАЛОФЫДАОДЛфылстчстофвтл'
stroch = ''
high = ''
for i in range(len(a)):
    if a[i].isupper():
        stroch += a[i]
    else:
        high += a[i]
itog = stroch.lower()+high.upper()
print(itog)