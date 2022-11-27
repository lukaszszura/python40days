import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("THis is my Todo App.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")



