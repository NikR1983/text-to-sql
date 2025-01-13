import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
countries = ['Brasil', 'Japan', 'United States', 'Colombia', 'Spain', 'China', 'Australia', 'France', 'Germany', 'Belgium', 'South Korea', 'Poland', 'United Kingdom']
users = [892, 144, 1321, 1, 242, 2000, 109, 298, 257, 64, 320, 17, 233]

# Plotting
plt.figure(figsize=(10, 8))
plt.bar(countries, users, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Number of Users')
plt.title('Number of Users by Country via Facebook')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot()
