import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards
import time
import random
import game_scenes
from PIL import Image
import os

# additional components from https://extras.streamlit.app/

# -------------- app config ---------------

st.set_page_config(page_title="Laura's 보물찾기", page_icon="🌻")

# define external css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


###############################################
#
#
#           VARIABLES DEFINITION
#
#
################################################

# variable responsible for checking if player provided his name and game can be started
start = False

# set session states
# this is streamlit specific. For more contex please check streamlit documenation

if "health" not in st.session_state:
    st.session_state["health"] = 100
if "mana" not in st.session_state:
    st.session_state["mana"] = 80
if "gold" not in st.session_state:
    st.session_state["gold"] = 5
if "place" not in st.session_state:
    st.session_state["place"] = "introScene"
if "sheep_anger" not in st.session_state:
    st.session_state["sheep_anger"] = 0
if "sword" not in st.session_state:
    st.session_state["sword"] = 0
if "dragon_alive" not in st.session_state:
    st.session_state["dragon_alive"] = 1
if "dragon_hp" not in st.session_state:
    st.session_state["dragon_hp"] = 20
if "temp" not in st.session_state:
    st.session_state["temp"] = ""
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if "scenes_counter" not in st.session_state:
    st.session_state["scenes_counter"] = {
        "intro_counter": 0,
        "cave_counter": 0,
        "trip_counter": 0,
        "elf_counter": 0,
    }


###############################################
#
#
#               GAME ENGINE
#
#
################################################

# ---------------- CSS ----------------

local_css("style.css")

# ---------------FX--------------------
def ReduceGapFromPageTop(wch_section = 'main page'):
    if wch_section == 'main page':
        st.markdown(" <style> div[class^='block-container'] { padding-top: 3rem; } </style> ", unsafe_allow_html=True)  # reduce gap from page top
    
    elif wch_section == 'sidebar':
        st.markdown(" <style> div[class^='st-emotion-cache-10oheav'] { padding-top: 0rem; } </style> ", unsafe_allow_html=True)
horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line
# ----------------- game start --------

# ViewHelpf
ReduceGapFromPageTop()

############

welcome = st.empty()




#main_text_container = st.empty()
#main_text_container.caption("Create your own adventure visit [GitHub](https://github.com/TomJohnH/streamlit-dungeon)")
#dsfd
with welcome.container():
    first = st.empty()
    first.title("🐮로라의 보물찾기🕹️")
#st.set_page_config(page_title = "PixMatch", page_icon="🕹️", layout = "wide", initial_sidebar_state = "expanded")
# hero base statistics
    hlp_dtl = f"""<span style="font-size: 26px;">
    <ol>
    <li style="font-size:15px";>각 퀘스트에 맞게 사진 조각 혹은 사람들을 찾아간다.</li>
    <li style="font-size:15px";>퀴즈를 풀어야 그 다음 스테이지 미션이 주어져요</li>
    <li style="font-size:15px";>각 스테이지에 사람이 있을 경우, 인증샷을 찍는다.</li>
    <li style="font-size:15px";>마지막 스테이지까지 가보숑~~~~</li>
    <li style="font-size:15px";>답을 정 모르겠으면 help를 입력 -> 밑에 답이 나오지롱~~~</li>
    <li style="font-size:15px";>퀘스트 수행하면서 찾아야 되는 사람들은 모두 KCCP 사람들입니당~~</li>
    <li style="font-size:15px";>단,, 새로고침을 하면 처음으로 가지고, 뒤로 가기는 안되요 (제가 기술이 딸려서,,)-스미마센</li>
    <li style="font-size:15px";>허지만, 첫 페이지로 돌아간다 하더라도 당황하지 말고, 첫 문제부터 천천히 푸심 되여👌🏻👌🏻</li>
    </ol></span>""" 

    sc1, sc2 = st.columns(2)
    # random.seed()
    # vpth = "/home/ubuntu/streamlit-game/images/nuki/"
    # img = os.listdir("/home/ubuntu/streamlit-game/images/nuki")
    # GameHelpImg = vpth + random.choice(img)
    GameHelpImg = Image.open("/home/ubuntu/streamlit-game/images/Untitled.png").resize((550, 550))
    sc2.image(GameHelpImg, use_column_width='auto')

    sc1.subheader('규칙')
    sc1.markdown(horizontal_bar, True)
    sc1.markdown(hlp_dtl, unsafe_allow_html=True)
    st.markdown(horizontal_bar, True)

    player_name_container = st.empty()
    player_name_container.text_input(
        "자! 게임을 시작하기 전, 너의 이름을 적어줘!", key="player_name"
    )




if st.session_state.player_name != "":
    player_name_container.empty()
    welcome.empty()
    
    start = True
    st.empty()
# START THE GAME

if start:

    # delete welcome
    welcome.empty()
    st.empty()
    if st.session_state.place == "introScene":
        game_scenes.introScene()
    elif st.session_state.place == "sheepScene":
        game_scenes.sheepScene()
    elif st.session_state.place == "southpathScene":
        game_scenes.southpathScene()
    elif st.session_state.place == "elfScene":
        game_scenes.elfScene()
    elif st.session_state.place == "caveScene":
        game_scenes.caveScene()
    elif st.session_state.place == "poScene":
        game_scenes.poScene()
    elif st.session_state.place == "dragonScene":
        game_scenes.dragonScene()
    elif st.session_state.place == "libraryScene":
        game_scenes.libraryScene()
    elif st.session_state.place == "step9Scene":
        game_scenes.step9()
    elif st.session_state.place == "step10Scene":
        game_scenes.step10()
    elif st.session_state.place == "step11Scene":
        game_scenes.step11()
    elif st.session_state.place == "step12Scene":
        game_scenes.step12()
    elif st.session_state.place == "step13Scene":
        game_scenes.step13()
    elif st.session_state.place == "step14Scene":
        game_scenes.step14()
    elif st.session_state.place == "step15Scene":
        game_scenes.step15()
    elif st.session_state.place == "step16Scene":
        game_scenes.step16()
    elif st.session_state.place == "step17Scene":
        game_scenes.step17()
    elif st.session_state.place == "step18Scene":
        game_scenes.step18()
    elif st.session_state.place == "step19Scene":
        game_scenes.step19()
    elif st.session_state.place == "step20Scene":
        game_scenes.step20()
    elif st.session_state.place == "step21Scene":
        game_scenes.step21()
    elif st.session_state.place == "last":
        game_scenes.last()
    # player stats

    c1,c2,c3 = st.columns(3)
    random.seed()
    vpth = "/home/ubuntu/streamlit-game/images/nuki/"
    img = os.listdir("/home/ubuntu/streamlit-game/images/nuki")
    GameHelpImg1, GameHelpImg2, GameHelpImg3 =  random.sample(img, 3)
    c1.image(Image.open(vpth +GameHelpImg1).resize((550, 550)))
    c2.image(Image.open(vpth +GameHelpImg2).resize((550, 550)))
    c3.image(Image.open(vpth +GameHelpImg3).resize((550, 550)))



# this part of the code focuses input on text window
# please note that counter is required - for streamlit specific it does not work without it

components.html(
    f"""
        <div>some hidden container</div>
        <p>{st.session_state.counter}</p>
        <script>
            var input = window.parent.document.querySelectorAll("input[type=text]");
            for (var i = 0; i < input.length; ++i) {{
                input[i].focus();
            }}
    </script>
    """,
    height=0,
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# MainMenu {visibility: hidden;}

# ------------ footer  ---------------------------

# st.markdown(
#     f"""
#     <div class="bpad" id="bpad">
#     <a href="https://www.buymeacoffee.com/tomjohn" style="color: grey; text-decoration:none;">
#     <div class="coffee_btn" >
#     <img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/coffe.png" style="max-width:20px;margin-right:10px;">
#     Buy me a coffee</a></div></div>""",
#     unsafe_allow_html=True,
# )
