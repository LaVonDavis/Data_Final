import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default='browser'

df = pd.read_csv('cost_of_living_us.csv')

dm = pd.DataFrame(df.sort_values(by=['taxes']))


count = 1

while count < 14:
    print(dm['areaname'][dm.index[-count]])
    count = count + 1
