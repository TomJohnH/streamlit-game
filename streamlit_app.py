import streamlit as st
from streamlit_extras.stoggle import stoggle  # check https://extras.streamlit.app/
from streamlit_extras.metric_cards import style_metric_cards

###############################################
#
#
#               VARIABLES DEFINITION
#
#
################################################


start = False

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


###############################################
#
#
#               SCENES DEFINITION
#
#
################################################

###############################################
#
#               intro SCENE
#
################################################


def introScene():

    # if st.session_state.previous_place != "introScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["left", "right"]

    # main_image
    st.image(
        "https://images.unsplash.com/photo-1429743305873-d4065c15f93e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1467&q=80"
    )

    # scene text
    st.subheader(
        "Welcome, "
        + st.session_state.player_name
        + ", to an unusual world of fantasy. All the decisions that you made until this point in your life led you to this moment. Choose your actions wisely!"
    )
    directions_container = st.empty()

    # st.session_state
    scene_action = directions_container.text_input(
        "What to do?", key="introSceneActions"
    )
    if scene_action.lower() in directions:
        if scene_action.lower() == "left":
            st.session_state.place = "sheepScene"
            st.experimental_rerun()
        if scene_action.lower() == "right":
            st.write("Large tree is blocking this way.")

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right intput")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               sheep Scene
#
################################################


def sheepScene():

    # if st.session_state.previous_place != "sheepScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["left", "right", "forward", "back", "pet"]

    # main_image
    st.image(
        "https://images.unsplash.com/photo-1484557985045-edf25e08da73?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1373&q=80"
    )

    st.subheader("You see a sheep. Go on, try to pet it.")

    # sheep gives you gold

    # scene text

    directions_container = st.empty()

    scene_action = directions_container.text_input(
        "What to do?", key="sheepSceneActions"
    )
    if scene_action.lower() in directions:
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.write("There is nothing there")
        # --- BACK OR RIGHT ---
        # ---------------------
        if scene_action.lower() == "back" or scene_action.lower() == "right":
            st.session_state.place = "introScene"
            st.experimental_rerun()
        # ---PET THE SHEEP ---
        # ---------------------
        if scene_action.lower() == "pet":
            # --- Sheep shares his wealth ---
            if st.session_state.sheep_anger < 5:
                st.write("Sheep goes: streeeeaaamlit and gives you 5 coins")
                st.session_state.gold = st.session_state.gold + 5
            # --- Sheep becomes angrier ---
            st.session_state.sheep_anger = st.session_state.sheep_anger + 1
            if st.session_state.sheep_anger > 2 and st.session_state.sheep_anger < 6:
                st.write("Sheep is becoming a little bit anoyed ")
            # --- too much pets ---
            if st.session_state.sheep_anger == 5:
                st.write(
                    "Sheep has enough of pets and bites your arm off. You lose 50 HP!"
                )
                st.session_state.health = st.session_state.health - 50
            if st.session_state.sheep_anger > 10:
                st.write(
                    'Sheep states in unusal low, human voice: "Violence is not an answer but it could be if you dont stop"'
                )

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right intput")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#
#               GAME ENGINE
#
#
################################################


welcome = st.empty()
welcome.title("Welcome adventurer")

# hero base statistics


player_name_container = st.empty()
player_name_container.text_input(
    "State your name and hit enter to start the game", key="player_name"
)


if st.session_state.player_name != "":
    player_name_container.empty()
    start = True
    # st.info(st.session_state.player_name)


# START THE GAME

if start:

    if st.session_state.place == "introScene":
        introScene()

    elif st.session_state.place == "sheepScene":
        sheepScene()

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Health", value=st.session_state.health, delta=0)
    col2.metric(label="Mana", value=st.session_state.mana, delta=0)
    col3.metric(label="Gold", value=st.session_state.gold, delta=0)
    style_metric_cards(
        background_color="#black", border_color="#2b2410", border_left_color="#2b2410"
    )

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
