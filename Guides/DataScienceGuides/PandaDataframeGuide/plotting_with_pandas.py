import pandas as pd
import matplotlib.pyplot as plt
import os

#%%

temp = pd.read_csv(os.path.join(os.getcwd(), 'temp.csv'))
df = pd.read_csv(os.path.join(os.getcwd(), 'data_1.csv'))

# %%
# can use pd.DataFrame.plot()

temp.plot()
plt.show()

# %%
# can save figures by chaining methods

temp.plot().get_figure().savefig(os.path.join(os.getcwd(), 'temperatures.png'))

#%%
# can use all other matplotlib plot types

df.loc[:, ['py-score', 'total']].plot.hist(bins=5, alpha=0.4)
plt.show()
