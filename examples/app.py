# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Sample data creation
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': np.random.randint(100, 1000, size=12)
}
df = pd.DataFrame(data)

# Streamlit app
st.title('Monthly Sales Visualization')

# Display the dataframe
st.header('Sales Data')
st.write(df)

# Plotting the sales data
st.header('Sales Chart')
st.line_chart(df.set_index('Month'))
