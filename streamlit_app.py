import streamlit as st
from streamlit_extras.stoggle import stoggle  # check https://extras.streamlit.app/
from streamlit_extras.metric_cards import style_metric_cards

import time
import random

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
if "forest_trip" not in st.session_state:
    st.session_state["forest_trip"] = 0
if "sword" not in st.session_state:
    st.session_state["sword"] = 0
if "dragon_alive" not in st.session_state:
    st.session_state["dragon_alive"] = 1
if "dragon_hp" not in st.session_state:
    st.session_state["dragon_hp"] = 20
if "temp" not in st.session_state:
    st.session_state["temp"] = ""


def restart_session():

    st.session_state["health"] = 100
    st.session_state["mana"] = 80
    st.session_state["gold"] = 5
    st.session_state["place"] = "introScene"
    st.session_state["sheep_anger"] = 0
    st.session_state["forest_trip"] = 0
    st.session_state["sword"] = 0
    st.session_state["dragon_alive"] = 1
    st.session_state["dragon_hp"] = 20


# this little function helps us to clear text input by storing variable in temp
def clear(ss_variable):
    st.session_state["temp"] = st.session_state[ss_variable]
    st.session_state[ss_variable] = ""


# before changing scene you have to clear out the temp
def temp_clear():
    st.session_state["temp"] = ""


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
    st.caption("Use mouse or [Tab] to focus on input field")
    # st.session_state
    scene_action = directions_container.text_input(
        "What to do?", key="introSceneActions"
    )
    if scene_action.lower() in directions:
        if scene_action.lower() == "left":
            st.session_state.place = "sheepScene"
            temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "right":
            st.session_state.place = "caveScene"
            temp_clear()
            st.experimental_rerun()

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

    # for some reason we have here lenghty interaciton with sheep

    directions_container = st.empty()

    # scene_action = directions_container.text_input(
    #     "What to do?", key="sheepSceneActions", on_change=clear
    # )

    # clearing text_input was suprisingly hard to figure out
    directions_container.text_input(
        "What to do?",
        key="sheepSceneActions",
        on_change=clear,
        args=["sheepSceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.write("There is nothing there")
        # --- BACK OR RIGHT ---
        # ---------------------
        if scene_action.lower() == "back" or scene_action.lower() == "right":
            st.session_state.place = "introScene"
            temp_clear()
            st.experimental_rerun()
        # ---PET THE SHEEP ---
        # ---------------------
        if scene_action.lower() == "pet":
            # progress bar for petting sheep
            my_bar = st.empty()
            my_bar.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            my_bar.empty()

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
#               cave Scene
#
################################################


def caveScene():

    # if st.session_state.previous_place != "introScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["up", "back"]

    # main_image
    st.image(
        "https://images.unsplash.com/photo-1621622658048-f9f0dbd11c46?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
    )

    # scene text
    st.subheader(
        "After walking for 2 hours in the forest you encounter dark cave. They say that If you stare into the abyss, the abyss stares back at you. Something shiny seems to flicker in the cave. Are you afraid of the dark?"
    )

    if st.session_state["forest_trip"] == 0:
        st.write("You feel exhausted  and lose -5HP")
        st.session_state.health = st.session_state.health - 5
        st.session_state["forest_trip"] = 1

    directions_container = st.empty()

    # st.session_state
    # scene_action = directions_container.text_input(
    #     "What to do?", key="caveSceneActions"
    # )

    directions_container.text_input(
        "What to do?",
        key="caveSceneActions",
        on_change=clear,
        args=["caveSceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        if scene_action.lower() == "back":
            st.session_state.place = "introScene"
            temp_clear()
            st.experimental_rerun()

        if scene_action.lower() == "up":
            st.session_state.place = "poScene"
            temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right intput")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               poScene
#
################################################


def poScene():

    # if st.session_state.previous_place != "introScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["left", "right", "back", "buy"]

    # main_image
    st.image(
        "https://images.unsplash.com/photo-1527043604258-3f1c4fcce3f1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
    )

    # scene text
    st.subheader(
        'In the dark you see young man. "I used to be a product manager" - he says. "But then I put comments in the Jira, clicked something and I did not save." - he mubles. "Now I sell swords...30 gold seems to be a good price! Ah...remeber that if you go right you will meet dragon! Left will lead you to the exit." '
    )

    directions_container = st.empty()

    # # st.session_state
    # scene_action = directions_container.text_input(
    #     "What to do?", key="poSceneActions"
    # )  # potentially dynamic key based on function name?

    directions_container.text_input(
        "What to do?",
        key="poSceneActions",  # potentially dynamic key based on function name?
        on_change=clear,
        args=["poSceneActions"],  # potentially dynamic key based on function name?
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        if scene_action.lower() == "left":
            st.session_state.place = "dragonScene"
            temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "right" or scene_action.lower() == "back":
            st.session_state.place = "caveScene"
            temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "buy":
            my_bar = st.empty()
            my_bar.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            my_bar.empty()
            if st.session_state["gold"] >= 30:
                st.write("Acquired sword")
                st.session_state["gold"] = st.session_state["gold"] - 30
                st.session_state["sword"] = 1
            else:
                st.write("You don't have money")

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right intput")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               dragon SCENE
#
################################################


def dragonScene():

    # if st.session_state.previous_place != "introScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["fight", "up", "back"]

    # main_image

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        st.image("https://i.ibb.co/nfY7Qph/output.jpg")

    with col3:
        st.write("")

    # scene text
    st.subheader(
        "Oh no! It's a Neural Network AI Deep Learning Big Data Generated Dragon! (NNADLBDGD)"
    )

    if st.session_state.sword == 0:
        st.write(
            "Dragon uses matrix multiplication and you get hit in the head by lose neuron. You don't have anything to defend yourself."
        )
        st.write(
            "Unfortunatelly this is were your adventure ends. But could you have done something differently?"
        )
        if st.button("Restart"):
            restart_session()
            st.session_state.place = "introScene"
            temp_clear()
            st.experimental_rerun()
    else:

        st.write(
            "Fortunatelly you have a sword so you can defend yourself from the dragon! Do you wanna fight it?"
        )
        directions_container = st.empty()

        # # st.session_state
        # scene_action = directions_container.text_input(
        #     "What to do?", key="dragonSceneActions"
        # )

        directions_container.text_input(
            "What to do?",
            key="dragonSceneActions",  # potentially dynamic key based on function name?
            on_change=clear,
            args=[
                "dragonSceneActions"
            ],  # potentially dynamic key based on function name?
        )

        scene_action = st.session_state["temp"]

        if scene_action.lower() in directions:
            if scene_action.lower() == "fight":
                my_bar = st.empty()
                my_bar.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                my_bar.empty()
                if st.session_state.dragon_alive == 1:

                    st.write(
                        "Your matrix multiplication skills are better than dragons. Who would know that that algebra classess will come usefull afterall."
                    )
                    damage = random.randint(5, 10)
                    st.write("Dragon loses " + str(damage) + " HP")

                    st.session_state["dragon_hp"] = st.session_state[
                        "dragon_hp"
                    ] - random.randint(0, damage)

                    damage = random.randint(0, 8)
                    st.write("Dragon hits you back and you lose " + str(damage) + " HP")

                    st.session_state["health"] = st.session_state["health"] - damage
                    if st.session_state["dragon_hp"] <= 0:
                        st.session_state.dragon_alive = 0
                        st.write("DRAGON IS DEAD or at least for you")
                else:
                    st.write("DRAGON IS DEAD or at least for you")

            if scene_action.lower() == "up":
                if st.session_state.dragon_alive == 1:
                    st.write("Dragon is still alive. Fight or flight!")
                else:
                    st.session_state.place = "libraryScene"
                    temp_clear()
                    st.experimental_rerun()

            if scene_action.lower() == "back":
                st.session_state.place = "poScene"
                temp_clear()
                st.experimental_rerun()

        else:
            # what should happen if wrong action is selected
            if scene_action != "":
                st.info("Please provide right intput")
                dir = f'Potential actions: {", ".join(directions)}'
                stoggle("Help", dir)
                st.write("")


###############################################
#
#               library SCENE
#
################################################


def libraryScene():

    # if st.session_state.previous_place != "introScene":
    #     st.session_state.last_direction = ""

    # delete welcome
    welcome.empty()

    # possible actions
    directions = ["left", "right"]

    # main_image
    st.image(
        "https://images.unsplash.com/photo-1600431521340-491eca880813?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80"
    )

    # scene text
    st.snow()
    st.title("Congratulations " + st.session_state.player_name + "!")
    st.subheader(
        "You enter Dragon Valut, but instead of gold you found...streamlit documentation library!"
    )
    st.subheader(
        "All the power is now in your hands. Would you make the documenation available for others? Or keep it tight and make the most sick app in the world? You feel amazed about the opportunites you will have using streamlit."
    )
    st.subheader(
        "One man once said that with great power comes great responsibility (he was talking to the spider but whatever)"
    )
    st.subheader("Use your new power wisely.")
    st.success("Thank you for playing SteamlitLand Adventure RPG!")
    st.info("If you liked the game you can like ❤️ the community post and share it 🙂 ")
    st.caption("alpha version")

    # directions_container = st.empty()

    # # st.session_state
    # scene_action = directions_container.text_input(
    #     "What to do?", key="librarySceneActions"
    # )

    # if scene_action.lower() in directions:
    #     if scene_action.lower() == "left":
    #         st.session_state.place = "sheepScene"
    #         temp_clear()
    #         st.experimental_rerun()
    #     if scene_action.lower() == "right":
    #         st.session_state.place = "caveScene"
    #         temp_clear()
    #         st.experimental_rerun()

    # else:
    #     # what should happen if wrong action is selected
    #     if scene_action != "":
    #         st.info("Please provide right intput")
    #         dir = f'Potential actions: {", ".join(directions)}'
    #         stoggle("Help", dir)
    #         st.write("")


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

    elif st.session_state.place == "caveScene":
        caveScene()

    elif st.session_state.place == "poScene":
        poScene()
    elif st.session_state.place == "dragonScene":
        dragonScene()
    elif st.session_state.place == "libraryScene":
        libraryScene()

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Health", value=st.session_state.health, delta=0)
    col2.metric(label="Mana", value=st.session_state.mana, delta=0)
    col3.metric(label="Gold", value=st.session_state.gold, delta=0)
    style_metric_cards(
        background_color="#black", border_color="#2b2410", border_left_color="#2b2410"
    )
    if st.session_state["sword"] == 1:
        st.write("🗡️ sword equipped")

hide_streamlit_style = """
            <style>
          
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# MainMenu {visibility: hidden;}
