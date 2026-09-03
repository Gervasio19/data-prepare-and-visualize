import pandas as pd
dates = pd.Series(pd.to_datetime([
'2023‐01‐01', '2023‐02‐15', '2023‐03‐30'
]))
df_feats = pd.DataFrame({
'date': dates,
'year': dates.dt.year,
'month': dates.dt.month,
'day_name': dates.dt.day_name(),
'dayofweek': dates.dt.dayofweek, # Mon=0
'quarter': dates.dt.quarter
})
print(df_feats)
