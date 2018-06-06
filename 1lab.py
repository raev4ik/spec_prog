import requests
import datetime
import pandas as pd


def save_data(var, years_1, years_2):
    list = ["Cherkasy", "Chernihiv", "Chernovtsi", "Crimea", "Dnipropetrovsk", "Donetsk", "Ivano - Frankivsk", "Kharkiv", "Kherson",
         "Khmelnytskyy", "Kiev", "Kiev_City", "Kirovohrad", "Luhansk", "Lviv", "Mykolayiv", "Odessa", "Poltava", "Rivne", "Sevastopol", "Sumy",
         "Ternopil", "Transcarpathia", "Vinnytsya", "Volyn", "Zaporizhzhya", "Zhytomyr"]
    for i in range(1,var):
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={count}&year1={years_first}&year2={years_second}&type=Mean".format(count = i, years_first = years_1, years_second = years_2)
        print(url)
        res = requests.get(url)
        rdata = res.text
        #print(rdata)
        today = datetime.datetime.today()
        with open(list[i-1]+today.strftime("__%Y-%m-%d-%H-%M-%S")+".csv",'w') as fd:
            fd.writelines(rdata)

save_data(28,1981,2018)


data = pd.read_csv("D:\SPECPROG\Cherkasy____2018-03-08-17-45-34.csv",index_col=False, header=1,names=['year','weak','smn','smt','vci','tci','vhi'])
f = pd.DataFrame(data.year.str.split(' ',2).tolist(),columns = ['y','w','s'])
data = pd.concat([f,data], axis=1)
data = data.drop(['year','tci','vhi'],axis =1)
data = data.rename(columns={'y':'YEAR','w':'WEAK','s':'SMN','weak':'SMT','smn':'VCI','smt':'TCI','vci':'VHI'})
data.drop(data.tail(1).index,inplace=True)
data = data.replace('\,','',regex=True).astype(float)
data



def save_data2(var2, years_11, years_22):
    list2 = ["Cherkasy", "Chernihiv", "Chernovtsi", "Crimea", "Dnipropetrovsk", "Donetsk", "Ivano - Frankivsk", "Kharkiv", "Kherson",
         "Khmelnytskyy", "Kiev", "Kiev_City", "Kirovohrad", "Luhansk", "Lviv", "Mykolayiv", "Odessa", "Poltava", "Rivne", "Sevastopol", "Sumy",
         "Ternopil", "Transcarpathia", "Vinnytsya", "Volyn", "Zaporizhzhya", "Zhytomyr"]
    for i in range(1,var2):
        url2 = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={count}&year1={years_first}&year2={years_second}&type=VHI_Parea".format(count = i, years_first = years_11, years_second = years_22)
        print(url2)
        res2 = requests.get(url2)
        rdata2 = res2.text
        #print(rdata)
        today2 = datetime.datetime.today()
        with open(list2[i-1]+today2.strftime("____Numbers___%Y-%m-%d-%H-%M-%S")+".csv",'w') as fd2:
            fd2.writelines(rdata2)

save_data2(28,1981,2018)


data2 = pd.read_csv("D:/SPECPROG/Cherkasy____Numbers___2018-03-08-23-03-14.csv", sep = r"\s+" ,index_col=False, header=1,names=['year','weak','0','5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100'])
data2.drop(data2.tail(1).index,inplace=True)
data2=data2.replace('\,','',regex=True).astype(float)
data2
union = pd.concat([data,data2], axis=1)
union = union.drop(['year','weak'],axis =1)
#union[union.YEAR==2012]['VHI']
print(union[union.YEAR==2012]['VHI'].max())
print(union[union.YEAR==2012]['VHI'].min())