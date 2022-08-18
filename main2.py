echo "# Morg" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/morganclauss/Morg.git
git push -u origin main



import streamlit as st

st.title('Our First Streamlit App')
st.subheader('Introducting Streamlit in Automate Everything with Python')
st.write('''This is our first Web App.
Enjoy it!
''')