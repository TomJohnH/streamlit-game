import streamlit as st
from streamlit_extras.stoggle import stoggle
import game_config
import game_def
import time
import random

###############################################
#
#               intro Scene
#
################################################


def introScene():

    # possible actions
    directions = ["left", "right", "help"]

    # main_image
    st.image(game_config.image_source["introScene"])

    # scene text
    if st.session_state["scenes_counter"]["intro_counter"] == 0:
        st.markdown(
            f'<div class="fantasy-container"><p>Welcome, {st.session_state.player_name},  to a fantastical realm of mystery and wonder. The path that brought you here has been long and winding - the decisions you\'ve made throughout your life have led you here. Now is the time to choose your path with caution and care, for the fate of this realm is in your hands. From the mystical fields of the west, to the dark caves of the east, this world awaits your exploration. But beware, for dangerous creatures and ancient magic lurk around every corner. May fortune be on your side as you embark on this journey.</p></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="fantasy-container"><p>You are back at the fork in the forest road.</p></div>',
            unsafe_allow_html=True,
        )

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    # input container
    # there are a few things going on here:
    # 1. we take user input
    # 2. we trigger callback which copies input to temp. callback is called with argument that is passed to clear function
    # 3. text input is cleared
    directions_container.text_input(
        "What to do?",
        key="introSceneActions",
        on_change=game_def.clear,
        args=["introSceneActions"],
    )

    # this is probably redundancy
    scene_action = st.session_state["temp"]

    # this part is responsible for reactions on inputs
    # after we gather information about scene action we then trigger reaction
    # there are standard reactions like reaction to help and scene spcecific reactions
    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = (
                "sheepScene"  # we are moving our character to other scene
            )
            game_def.temp_clear()  # we are claring text input
            st.experimental_rerun()  # rerun is streamlit specific and rerund the app
        # --- RIGHT ---
        # ------------
        if scene_action.lower() == "right":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "caveScene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               sheep Scene
#
################################################


def sheepScene():

    # possible actions
    directions = ["left", "right", "back", "pet", "help"]

    # scene image
    st.image(game_config.image_source["sheepScene"])

    st.markdown(
        f'<div class="fantasy-container"><p>You see a sheep grazing in a grassy meadow. A gentle mist hangs in the air, and a mystical glow surrounds the area. As you approach the sheep, you notice a magical aura emanating from it. Go on, try to pet it.</p></div>',
        unsafe_allow_html=True,
    )

    # for some reason we have here lenghty interaciton with sheep

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    # clearing text_input was suprisingly hard to figure out
    directions_container.text_input(
        "What to do?",
        key="sheepSceneActions",
        on_change=game_def.clear,
        args=["sheepSceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.write("There is nothing there")
        # --- BACK OR RIGHT ---
        # ---------------------
        if scene_action.lower() == "back" or scene_action.lower() == "right":
            st.session_state.place = "introScene"
            game_def.temp_clear()
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
            random_gold = random.randint(4, 8)

            if st.session_state.sheep_anger < 5:

                st.success(
                    "Sheep goes: streeeeaaamlit and gives you "
                    + str(random_gold)
                    + " coins"
                )
                st.session_state.gold = st.session_state.gold + random_gold

            # --- Sheep becomes angrier ---
            st.session_state.sheep_anger = st.session_state.sheep_anger + 1

            if st.session_state.sheep_anger > 2 and st.session_state.sheep_anger < 6:
                st.success("Sheep is becoming a little bit anoyed ")

            # --- too much pets ---
            if st.session_state.sheep_anger == 5:
                st.success(
                    "Sheep has enough of pets and bites your arm off. You lose 50 HP!"
                )
                st.session_state.health = st.session_state.health - 50
            if st.session_state.sheep_anger > 5 and st.session_state.sheep_anger < 10:
                random_number_of_dots = random.randint(3, 20)
                annoyed_sheep = (
                    "".join("." for i in range(random_number_of_dots)) + "no"
                )
                st.success(annoyed_sheep)
            if st.session_state.sheep_anger >= 10:
                st.success(
                    'Sheep states in an unusually low, human voice: "Violence is not an answer, but it could be if you don\'t stop"'
                )

    else:

        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               cave Scene
#
################################################


def caveScene():

    # possible actions
    directions = ["up", "back", "help"]

    # main_image
    st.image(game_config.image_source["caveScene"])

    # scene text
    # conditional if you have already seen the scene
    if st.session_state["scenes_counter"]["cave_counter"] == 0:
        st.markdown(
            f'<div class="fantasy-container"><p>After walking for 2 hours through the enchanted forest, you stumble across a mysterious cave. Legends say that if you stare into the abyss, the abyss will stare back at you. A faint glimmer of light seems to be emanating from the depths of the cave. An eerie chill runs down your spine as you walk closer, but you can\'t help but be curious of the unknown. Are you brave enough to enter the depths of this mysterious cave, despite the fear of the unknown darkness?</p></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="fantasy-container"><p>You are back at the cave.</p></div>',
            unsafe_allow_html=True,
        )

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    if st.session_state["scenes_counter"]["trip_counter"] == 0:
        st.success("You feel exhausted and lose -5HP")
        st.session_state.health = st.session_state.health - 5
        st.session_state["scenes_counter"]["trip_counter"] = 1

    directions_container.text_input(
        "What to do?",
        key="caveSceneActions",
        on_change=game_def.clear,
        args=["caveSceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- back ---
        # ------------
        if scene_action.lower() == "back":
            st.session_state["scenes_counter"]["cave_counter"] += 1
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "up":
            st.session_state["scenes_counter"]["cave_counter"] += 1
            st.session_state.place = "poScene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               po Scene
#
################################################


def poScene():

    # possible actions
    directions = ["left", "right", "back", "buy", "help"]

    # main_image
    st.image(game_config.image_source["poScene"])

    # scene text
    st.markdown(
        f'<div class="fantasy-container"><p>In the dark, you see a young man. He was once a renowned product manager, who worked diligently to make the world a better place. But one day, he was attempting to add comments to Jira, when suddenly, something went wrong and his work didn\'t save. As a result, he was cursed to sell swords in a mystical land, far away from his home. He mutters that the price of 30 gold feels right, and then he offers a warning - if you go right, you will meet a dangerous dragon. He reminds you to keep left if you want to find the exit.</p></div>',
        unsafe_allow_html=True,
    )

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key="poSceneActions",  # potentially dynamic key based on function name?
        on_change=game_def.clear,
        args=["poSceneActions"],  # potentially dynamic key based on function name?
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.session_state.place = "dragonScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- RIGHT OR BACK ---
        # ------------
        if scene_action.lower() == "right" or scene_action.lower() == "back":
            st.session_state.place = "caveScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- BUY ---
        # ------------
        if scene_action.lower() == "buy":
            my_bar = st.empty()
            my_bar.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            my_bar.empty()
            if st.session_state["gold"] >= 30:
                st.success("Acquired sword")
                st.session_state["gold"] = st.session_state["gold"] - 30
                st.session_state["sword"] = 1
            else:
                st.success("You don't have enough money")

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               dragon SCENE
#
################################################


def dragonScene():

    # possible actions
    directions = ["fight", "up", "back", "help"]

    # main_image

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        st.image(game_config.image_source["dragonScene"])

    with col3:
        st.write("")

    # scene text
    st.markdown(
        f'<div class="fantasy-container"><p>Oh no! PM was wrong about going left! It\'s a Neural Network AI Deep Learning Big Data Generated Dragon! (NNADLBDGD)</p></div>',
        unsafe_allow_html=True,
    )

    # without a sword you will die
    if st.session_state.sword == 0:
        st.success(
            "Dragon uses matrix multiplication and you get hit in the head by loose neuron. You don't have anything to defend yourself."
        )
        st.success(
            "Unfortunatelly this is where your adventure ends. But could you have done something differently?"
        )
        if st.button("Restart"):
            game_def.restart_session()
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:

        st.success(
            "Fortunatelly you have a sword so you can defend yourself from the dragon! Do you wanna fight it?"
        )
        directions_container = st.empty()
        st.caption(
            'Use mouse or [Tab] to focus on input field. To check potential actions, type "help".'
        )

        # # st.session_state
        # scene_action = directions_container.text_input(
        #     "What to do?", key="dragonSceneActions"
        # )

        directions_container.text_input(
            "What to do?",
            key="dragonSceneActions",  # potentially dynamic key based on function name?
            on_change=game_def.clear,
            args=[
                "dragonSceneActions"
            ],  # potentially dynamic key based on function name?
        )

        scene_action = st.session_state["temp"]

        if scene_action.lower() in directions:
            if scene_action.lower() == "help":
                st.info(f'Potential actions: {", ".join(directions)}')
            if scene_action.lower() == "fight":
                my_bar = st.empty()
                my_bar.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                my_bar.empty()
                if st.session_state.dragon_alive == 1:

                    st.success(
                        "Your matrix multiplication skills are better than dragons. Who would have guessed that these algebra classes would be useful after all?"
                    )
                    damage = random.randint(5, 10)
                    st.success("Dragon loses " + str(damage) + " HP")

                    st.session_state["dragon_hp"] = st.session_state[
                        "dragon_hp"
                    ] - random.randint(0, damage)

                    damage = random.randint(0, 8)
                    st.success(
                        "Dragon hits you back and you lose " + str(damage) + " HP"
                    )

                    st.session_state["health"] = st.session_state["health"] - damage
                    if st.session_state["dragon_hp"] <= 0:
                        st.session_state.dragon_alive = 0
                        st.success("DRAGON IS DEAD or at least to you")
                else:
                    st.success("DRAGON IS DEAD or at least to you")

            if scene_action.lower() == "up":
                if st.session_state.dragon_alive == 1:
                    st.success("Dragon is still alive. Fight or flight!")
                else:
                    st.session_state.place = "libraryScene"
                    game_def.temp_clear()
                    st.experimental_rerun()

            if scene_action.lower() == "back":
                st.session_state.place = "poScene"
                game_def.temp_clear()
                st.experimental_rerun()

        else:
            # what should happen if wrong action is selected
            if scene_action != "":
                st.info("Please provide right input")
                dir = f'Potential actions: {", ".join(directions)}'
                stoggle("Help", dir)
                st.write("")


###############################################
#
#               library SCENE
#
################################################


def libraryScene():

    # possible actions
    directions = ["left", "right"]

    # main_image
    st.image(game_config.image_source["libraryScene"])

    # scene text
    st.snow()
    st.title("Congratulations " + st.session_state.player_name + "!")

    st.markdown(
        f'<div class="fantasy-container"><p>You enter the dragon vault, but instead of gold, you find a Streamlit documentation library!<br><br>All the power is now in your hands. Would you make the documentation available for others? Or keep it only for yourself and make the sickest app in the world? The possibilities offered by Streamlit amaze you.<br><br>One man once said that with great power comes great responsibility (he was talking to a spider, but whatever).<br><br>Use your new power wisely.</div>',
        unsafe_allow_html=True,
    )
    st.success("Thank you for playing SteamlitLand Adventure RPG!")
    st.info("If you liked the game you can like ❤️ the community post and share it 🙂")
    st.info("Credits: Created by @TomJohn")
    st.info("Top players: knight @Courtland_Goldengate")
    st.caption("beta version")