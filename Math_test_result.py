# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Math_Test_Results_by_Grade')
df = pd.read_csv("2006_-_2011_NYS_Math_Test_Results_by_Grade_-_Citywide_-_by_Race-Ethnicity.csv")
st.dataframe(df.head())

st.subheader('Scatter plot of Year vs Mean scale score')
sns.scatterplot(data=df, x="Year", y="Mean Scale Score", hue="Number Tested")
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
st.pyplot()
