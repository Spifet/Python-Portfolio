import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:

    st.image("images/photo.png", width=320)

with col2:
    st.title("Jei Cohen")
    content = """
    Hi, I am Jei! I am a Full Stack developer. I graduated in 2022 with a diploma of Full Stack Developer from 
    ITC Academy and an enthusiastic Bsc. Computer Science distant student from UoPeople University in the 
    California, USA with a focus on backend languages and technologies. I have worked as a PS Engineer - Tier 3 Support 
    for an international LIMS company assisting large-scale business clients get bugs that affected dozens of thousands 
    of people tracked down in very limited time constraints. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv("data.csv", sep=",")

print(df.columns.tolist())
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")  # alternative is st.write("[Source Code](https://...)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")  # alternative is st.write("[Source Code](https://...)")

