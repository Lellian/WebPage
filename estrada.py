import streamlit as st

st.set_page_config(page_title="Lellian's website", page_icon=":tada:", layout="wide")

#-------------------------------------------------------#divider

st.header("welcome to Lellian's website")

column1, column2, column3 = st.columns(3)

with column1:
    st.write("Autobiography")
    st.write("Hi, My name is Lellian C. Estrada. 19 years old Computer Engineering student. How can i help you today?")
with column2:
    st.write("Say Anything")
with column3:
    st.write("say")

st.write("contact me:")

st.markdown("""

    <form action="https://formsubmit.co/lellianestrada2@gmail.com" method="POST">
            <input type="text" name="name" placeholder="your name" required>
            <input type="email" name="email" placeholder="your email" required>
            <textarea name="message" placeholder="your message"></textarea>
            <button type="submit">send</button>
    </forms>
            

""",unsafe_allow_html=True)