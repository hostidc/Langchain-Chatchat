import streamlit as st
from webui_pages.utils import *
from configs import (PROMPT_TEMPLATES,ROLE_ROOT_PATH)
import os
import time
import json


# 读取 JSON 文件
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        st.toast("JSON 文件格式错误！")
    return data

# 写入 JSON 文件
def write_json_file(data, file_path):
    try:
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        st.success("JSON 文件写入成功！")
    except:
        st.error("JSON 文件写入失败！")

def get_key_index(dictionary, key):
    for index, dict_key in enumerate(dictionary.keys()):
        if dict_key == key:
            return index
    return None

def role_base_page(api: ApiRequest):

    role_list = read_json_file(os.path.join(ROLE_ROOT_PATH, "prompt_llm_chat.json"))
    role_names = list(role_list.keys())
    # st.toast(role_names)

    selected_role_index = 0
    st.session_state["selected_role_info"] = ""

    def format_selected_role(role_name: str) -> str:
        return role_name

    selected_role = st.selectbox(
        "请选择或新建角色：",
        ["新建角色"] + role_names,
        format_func=format_selected_role,
        index=selected_role_index
    )

    if selected_role == "新建角色":
        with st.form("新建角色"):

            role_name = st.text_input(
                "角色名称",
                placeholder="角色名称",
                key="role_name",
            )
            role_info = st.text_area(
                "角色Prompt",
                placeholder="角色Prompt",
                key="role_info",
                height=200, 
                max_chars=3000,
            )
            submit_create_role = st.form_submit_button(
                "新建",
                use_container_width=True,
            )

        if submit_create_role:
            if not role_name or not role_name.strip():
                st.error("角色名称不能为空！")
            elif role_name in role_list:
                st.error(f"名为 {role_name} 的角色已经存在！")
            elif not role_info or not role_info.strip():
                st.error("角色Prompt不能为空！")
            else:
                data = {role_name: role_info}
                role_list.update(data)
                write_json_file(role_list, os.path.join(ROLE_ROOT_PATH, "prompt_llm_chat.json"))

            role_list = read_json_file(os.path.join(ROLE_ROOT_PATH, "prompt_llm_chat.json"))
            role_names = list(role_list.keys())
            # st.toast(get_key_index(role_list,role_name))
            # selected_role_index = get_key_index(role_list,role_name)
            PROMPT_TEMPLATES["llm_chat"] = role_list
            st.toast(f"角色{role_name}创建完成！")
            time.sleep(1)
            st.experimental_rerun()

    elif selected_role:
        # st.toast(selected_role)
        # st.toast(role_list[selected_role])
        st.session_state["selected_role_name"] = selected_role
        st.session_state["selected_role_info"] = role_list[selected_role]

        with st.form("编辑角色"):

            role_name = st.text_input(
                "角色名称",
                placeholder="角色名称",
                value=st.session_state["selected_role_name"],
                key="role_name",
            )
            role_info = st.text_area(
                "角色Prompt",
                placeholder="角色Prompt",
                value=st.session_state["selected_role_info"],
                height=200, 
                max_chars=3000,
                key="role_info",
            )
            submit_edit_role = st.form_submit_button(
                "编辑",
                use_container_width=True,
            )
            
        if submit_edit_role:
            if not role_name or not role_name.strip():
                st.error("角色名称不能为空！")
            elif not role_info or not role_info.strip():
                st.error("角色Prompt不能为空！")
            else:
                data = {role_name: role_info}
                role_list.update(data)
                write_json_file(role_list, os.path.join(ROLE_ROOT_PATH, "prompt_llm_chat.json"))

            role_list = read_json_file(os.path.join(ROLE_ROOT_PATH, "prompt_llm_chat.json"))
            role_names = list(role_list.keys())
            # st.toast(get_key_index(role_list,role_name))
            # selected_role_index = get_key_index(role_list,role_name)
            PROMPT_TEMPLATES["llm_chat"] = role_list
            st.toast(f"角色{role_name}创建完成！")
            time.sleep(1)
            st.experimental_rerun()
