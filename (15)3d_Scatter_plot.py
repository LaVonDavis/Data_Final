import plotly.io as pio
import pandas as pd
import plotly.express as px
pio.renderers.default='browser'

df = pd.read_csv('clean_COL.csv')
fig = px.scatter_3d(df, x='childcare_cost', y='taxes', z='median_family_income', color='state')
fig.show()
