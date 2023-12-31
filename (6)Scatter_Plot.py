import plotly.io as pio
import pandas as pd
import plotly.express as px
pio.renderers.default='browser'

df = pd.read_csv('cost_of_living_us.csv')
df.dropna()
fig = px.scatter(df, x='total_cost', y='transportation_cost', color='state')
fig.show()
