# display bar chart of all values that appear in dataframe column
!pip install pandas
!pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
df['created'].dt.hour.value_counts(sort=False).plot.bar()
