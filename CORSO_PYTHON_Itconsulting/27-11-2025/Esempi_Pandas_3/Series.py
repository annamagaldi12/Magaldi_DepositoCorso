import pandas as pd

#1  pd.to_datetime() = Converte un indice o una colonna in formato datetime, permettendo di sfruttare tutte le funzionalità di time series DI python
#esempio: colonna “date” in stringhe → datetime
df=[]
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(df['date'])


#2  Dataframe.resample():
#Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati, specificando l’intervallo desiderato (‘D’=day, ‘M’=month, ‘H’=hour, …).
# partendo da un DataFrame con indice DatetimeIndex:
df=[]
df_daily = df.resample('D').mean()      # media giornaliera
df_monthly = df.resample('M').sum()     # somma mensile


#3. Series.shift(): “Sposta” i valori lungo l’asse temporale di un numero di periodi, utile per calcolare differenze ritardate, tassi di crescita, ecc.
#aggiunge una colonna con il valore del giorno precedente
df=[]
df['prev_day'] = df['value'].shift(1)
# tasso di variazione giornaliero
df['daily_return'] = df['value'].pct_change()  
# equivalente a shift + calcolo %

#4. Series.rolling(): Calcola statistiche mobili su una finestra temporale scorrevole.
# finestra mobile di 7 giorni: media e deviazione standard
df=[]
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7']  = df['value'].rolling(window=7).std()