import streamlit as st
from webui_pages.utils import *

def display_link(c1, c2, link_name, link_url):
    with c1:
        st.write(f'{link_name}')
    with c2:
        st.write(f'[{link_url}]({link_url})')

def link_base_page(api: ApiRequest):

    st.text('Stable Diffusion 链接：')
    col1, col2 = st.columns([0.3, 0.7])
    display_link(col1,col2,'stablediffusionweb', 'https://stablediffusionweb.com/')
    display_link(col1,col2,'huggingface spaces', 'https://huggingface.co/spaces?sort=trending&search=stable')
    display_link(col1,col2,'prodia sdxl', 'https://huggingface.co/spaces/prodia/sdxl-stable-diffusion-xl')
    display_link(col1,col2,'prodia fast', 'https://huggingface.co/spaces/prodia/fast-stable-diffusion')

    pass
