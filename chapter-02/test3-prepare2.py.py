#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import tsemodule5 as tm5


# In[3]:


shasta=tm5.stock("شستا",standard=True)


# In[7]:


sh1=shasta.iloc[:10]
sh1


# In[8]:


khesapa=tm5.stock("خساپا",standard=True)
kh1=khesapa.iloc[:10]


# In[10]:


sh1['daily_return'] =sh1['Close'].pct_change(1)
kh1['daily_return'] =kh1['Close'].pct_change(1)


# In[12]:


display(sh1 , kh1)


# In[13]:


sh1_CV = sh1['daily_return'].std()/sh1['daily_return'].mean()
print('sh1 CV:\n',sh1_CV,sep='')


# In[14]:


kh1_CV = kh1['daily_return'].std()/kh1['daily_return'].mean()
print('kh1 CV:\n',kh1_CV,sep='')


# In[15]:


sh1['daily_return']


# In[16]:


stock = pd.DataFrame(np.concatenate([sh1['daily_return'].dropna().values.reshape(-1,1),kh1['daily_return'].dropna().values.reshape(-1,1)],axis=1))
stock.columns = ['sh1','kh1']
Covariance=stock.cov()
variance=sh1['daily_return'].var()
display(Covariance , variance)


# In[17]:


Beta=Covariance/variance
Beta


# # anothor stock

# In[18]:


import pandas as pd
import yfinance as yf
import statsmodels.api as sm


# In[19]:


RISKY_ASSET = 'AMZN'
MARKET_BENCHMARK = '^GSPC'
START_DATE = '2020-01-01'
END_DATE = '2020-05-09'


# In[20]:


df = yf.download([RISKY_ASSET, MARKET_BENCHMARK],
start=START_DATE,
end=END_DATE,
adjusted=True,
progress=False)


# In[21]:


X = df['Adj Close'].rename(columns={RISKY_ASSET: 'asset',MARKET_BENCHMARK: 'market'}).resample('M').last().pct_change().dropna()


# In[22]:


X


# In[27]:


covariance = X.cov().iloc[:5]
covariance


# In[28]:


X.iloc[:5]


# In[29]:


benchmark_variance = X.market.var()
benchmark_variance


# In[30]:


beta = covariance / benchmark_variance
beta


# In[62]:


shasta['Close']


# In[63]:


np.set_printoptions(precision=2)
sh1[sh1<1.4]=1.4
sh1[sh1>3.03]=3.03
np.set_printoptions(threshold=20)
sh1


# # tamrin _2 
# 

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
url = "C:/Users/Ateeq/Downloads/S_Saipa.csv"
saipa= np.genfromtxt(url,delimiter=',', names=True)
CLOSE=saipa["CLOSE"][::-1]
max_price = np.max(CLOSE)
argmax=np.argmax(CLOSE)
min_price = np.min(CLOSE)
mean_price = np.mean(CLOSE)
print("Max Price =",max_price)
print("index of max price=",argmax)
print("Min Price =",min_price)
print("Mean Price =",mean_price)


plt.plot(CLOSE, label="saipa")
plt.legend()
plt.show()


# In[ ]:





# In[11]:


import matplotlib.pyplot as plt 
import numpy as np
url = 'C:/Users/Ateeq/Downloads/S_Saipa.csv'
barekat = np.genfromtxt(url,delimiter=',', names=True)
max_price = np.max(barekat["CLOSE"])
min_price = np.min(barekat["CLOSE"])
mean_price = np.mean(barekat["CLOSE"])
print("Max Price = {p:0.0f}".format(p=max_price))
print("Min Price = {p:0.0f}".format(p=min_price))
print("Mean Price = {p:0.2f}".format(p=mean_price))
low_prices = []
dates = []
for price in barekat:  
    if price["CLOSE"] < mean_price:        
        low_prices.append(price["CLOSE"])        
        dates.append(price["DTYYYYMMDD"])
HIGH_prices = []
dates = []
for price in barekat:  
    if price["CLOSE"] > mean_price:        
        HIGH_prices.append(price["CLOSE"])        
        dates.append(price["DTYYYYMMDD"])
#print(low_prices)
print(len(low_prices))
print(len(HIGH_prices))
plt.plot(low_prices, label="barekat")
plt.legend()
plt.show()


# # next_execise

# In[13]:


#1
# Python program explaining
# irr() function

import numpy_financial as npf
'''
Question :
Investment = 500
Withdrawals at regular interval : 50, 31, 3, 11
'''

Solution = npf.irr([-500, 50, 31, 3, 11])

print("Solution - Internal Rate of Return : ", Solution)


# In[14]:


#2
# Python program explaining
# pmt() function

import numpy_financial as npf

'''
Question :

how much time would it take to pay-off a loan of
$10, 000 at 10 % annual rate of interest, if we had
$100 to pay each month ?
چقدر زمان برای پرداخت وام 10000 دلاری با نرخ بهره سالانه 10 درصد طول می کشد، اگر ما 100 دلار برای پرداخت هر ماه داشته باشیم؟
'''

# rate pmt pv
Solution = npf.nper(0.1 / 12, -100, 10000)

# Here fv = 0 ; Also Default value of fv = 0
print("Solution - No. of periods : % f months" %(Solution))


# In[18]:


'''
تمرین
یک شرکت در حال بررسی خرید تجهیزات جدید به قیمت 500،000 دلار می باشد.
مدیریت تخمین می زند که عمر این دستگاه 4 سال باشد. 
همچنین انتظار می رود که در پایان هر سال، جریان نقدی برابر با 160،000 دلار برای شرکت ایجاد کند. 
شرکت در نظر دارد در سال پنجم این دستگاه را به ارزش اسقاط 50،000 دلار بفروش برساند.
'''


# In[19]:


npf.irr([-500_000,160000,160000,160000,160000,50000])


# In[28]:


npf.npv(0.13,[-500_000,160000,160000,160000,160000,50000])


# # فرض کنید در یک پروژه ساختمانی سرمایه‌گذاری کرده‌اید. در سال مبدا یا سال صفر مبلغ 10 میلیارد تومن برای خرید زمین و مجوز هزینه کرده اید. در سال اول 8 میلیارد تومن بابت ساخت هزینه نموده اید و در سال دوم بابت فروش ساختمان 50 میلیارد تومن درآمد کسب کرده اید. حال با نرخ تنزیل 20 درصد ارزش فعلی جریانات 

# In[29]:


npf.npv(0.2,[-10_000_000_000,-8000_000_000,50000000000])


# # تمرین قیمت های بسته شدن سهام به این شکل است نمودار دایره ای و نمودار میله ای و خطی را همزمان با هم رسم کنید.

# In[31]:


import numpy as np
import matplotlib.pyplot as plt


# In[32]:


stocks=["femeli","AP","margham","haiweb","khodro","Dey"]


# In[34]:


Price_close=[4930,6500,9880,2987,1997,634]


# In[46]:


#Pie plot
plt.subplot(221)
my_explode=[0,0,0.2,0,0.1,0.3]
plt.pie(Price_close,labels=stocks,autopct="%1.0f%%",shadow=True,explode=my_explode,startangle=90)
plt.show()
#bar plot
plt.subplot(222)
plt.barh(stocks,Price_close)
plt.title("horizental bar")
plt.show()
#line plot
plt.subplot(212)
plt.plot(Price_close)
plt.show()


# In[64]:


# Python Program illustrating
# numpy.percentile() method

import numpy as np

# 1D array
#Price_close = [4930,6500,9880,2987,1997,634]
SHASTA=shasta["Close"]
print("arr : ", SHASTA)
print("50th percentile of SHASTA) : ",
np.percentile(SHASTA, 50))
print("25th percentile of SHASTA : ",
np.percentile(SHASTA, 25))
print("75th percentile of SHASTA : ",
np.percentile(SHASTA, 75))


# In[ ]:




