import streamlit as st
from webui_pages.utils import *
from streamlit_option_menu import option_menu
from webui_pages import *
import os
from configs import VERSION
from server.utils import api_address


api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    st.set_page_config(
        "数智人Chatm - 基于AI技术 轻松创建对话机器人",
        os.path.join("img", "chatchat_icon_blue_square_v2.png"),
        initial_sidebar_state="expanded",
        # menu_items={
        #     'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
        #     'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
        #     'About': f"""欢迎使用 Langchain-Chatchat WebUI {VERSION}！"""
        # }
    )

    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        "知识库管理": {
            "icon": "hdd-stack",
            "func": knowledge_base_page,
        },
        "角色设置": {
            "icon": "person",
            "func": role_base_page,
        },
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img",
                "logo-long-chatchat-trans-v2.png"
            ),
            use_column_width=True
        )
        st.caption(
            f"""<p align="right">基于大语言模型构建知识问答系统 </p>""",
            unsafe_allow_html=True,
        )
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
        )

    if selected_page in pages:
        pages[selected_page]["func"](api)
