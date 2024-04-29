import os
import streamlit as st
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

API_KEY = os.environ.get('API_KEY')

st.set_page_config(page_title="Prueba chat Arthropic",
                   page_icon="💬")

st.header("Prueba chat Arthropic, no usar en prod 🤖", divider='rainbow')

with st.container(border=True):

    response_range = st.radio("Largo de la respuesta",
                              horizontal=True,
                              options=['corta', 'mediana', 'larga'])

    if response_range == 'corta':
        tokens = 306
    elif response_range == 'mediana':
        tokens = 612
    elif response_range == 'larga':
        tokens = 1024

    client = Anthropic(api_key=API_KEY)

    messages = st.container()

    if prompt := st.chat_input("Pregunta"):
        messages.chat_message("user").write(prompt)
        response = client.messages.create(max_tokens=tokens,
                                          messages=[{"role": "user",
                                                     "content": prompt,
                                                     }],
                                          model="claude-3-opus-20240229",)
        messages.chat_message("assistant").write(response.content[0].text)

        print(response.content[0])
