import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default='browser'

df = pd.read_csv('cost_of_living_us.csv')
fig = px.scatter(df, x='food_cost', y='taxes', size='childcare_cost', color='isMetro')

fig.show()
