import streamlit as st
import pandas as pd
from datetime import date
from app.src.components.auth import authenticate_user, authorize_user

authenticate_user()

if authorize_user():
    st.title("Hello :red[streamlit] :100: :the_horns:")

    st.header("Header :anchor:")
    st.subheader("Sub Header :taurus:")
    st.text("This is a trial of text")

    st.markdown(""" ### h3 tag :moon: :sunglasses: :cool: """)

    df = pd.DataFrame.from_dict(
        {
            "name": ["Yoda", "John Wick", "Pikachu"],
            "country": ["Star", "USA", "Japan"],
            "dob": [
                date.today().strftime("%B %d, %Y"),
                date(2002, 5, 5),
                date(1992, 12, 12),
            ],
        }
    )

    st.write(df)
