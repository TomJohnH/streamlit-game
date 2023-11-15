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
    directions = ["left", "right", "south", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["introScene"])
        st.write("Enchanted forest")
    with col2:
        # scene text
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>Welcome, {st.session_state.player_name}, to a distant and unexplored exoplanet. Your spacecraft has crash-landed, into an enchanted forest and you find yourself in a world of unknown wonders and dangers. May fortune be on your side as you embark on this journey.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>You are back at the enchanted alien forest.</p></div>',
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
        if scene_action.lower() == "south":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "southpathScene"
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
#               Unicorn Scene
#
################################################


def sheepScene():

    # possible actions
    directions = ["left", "right", "back", "pet", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["sheepScene"])
        st.write("Magical sheep")
    with col2:
        st.markdown(
            f'<div class="fantasy-container" style="min-height:258.17px"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>As you traverse the alien landscape, you encounter a majestic creature with a shimmering horn – a unicorn native to this extraterrestrial realm. The air is filled with an otherworldly glow, and the unicorn seems to emit a magical aura. Do you approach and try to communicate with this mythical being?</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/sheep.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

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
        # ---PET THE Unicorn ---
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
                    "Unicorn goes: Super Saiyan mode and gives you "
                    + str(random_gold)
                    + " coins"
                )
                st.session_state.gold = st.session_state.gold + random_gold

            # --- Sheep becomes angrier ---
            st.session_state.sheep_anger = st.session_state.sheep_anger + 1

            if st.session_state.sheep_anger > 2 and st.session_state.sheep_anger < 6:
                st.success("Unicorn is becoming a little bit anoyed ")

            # --- too much pets ---
            if st.session_state.sheep_anger == 5:
                st.success(
                    "Unicorn had enough of pets and bites your arm off. You lose 50 HP!"
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
                    'Unicorn whisper through telepathy: "Violence is not an answer, but it could be if you don\'t stop"'
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

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["caveScene"])
        st.write("Dark cave")
    with col2:
        # scene text
        # conditional if you have already seen the scene
        if st.session_state["scenes_counter"]["cave_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>After hours of traversing the alien landscape, you come upon the entrance of a cavernous structure made of extraterrestrial rock. According to the records in your astronaut guide, this cave is known as 'The Echoing Abyss.' It is said that those who dare to explore its depths might uncover the secrets of this mysterious exoplanet. A strange luminescence emanates from the cavern, casting an otherworldly glow. The air within shivers with an unknown energy. Your spacesuit's sensors flicker with erratic readings, indicating the presence of undiscovered elements. Do you have the courage to step into the unknown and explore the depths of The Echoing Abyss?</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/cave.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>You are back at the cave.</p></div>',
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
#               Astro Scene
#
################################################


def poScene():

    # possible actions
    directions = ["left", "right", "back", "buy", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["poScene"])
        st.write("Product manager's hideout")
    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>In the dim light of the alien world, you come across a disheveled figure wearing a high-tech exosuit. This individual was once a skilled intergalactic explorer, tirelessly working to uncover the secrets of the cosmos. However, a catastrophic malfunction in their advanced navigation system stranded them on this uncharted exoplanet. The stranded explorer, once adept at discovering new frontiers, now survives by trading rare extraterrestrial artifacts. Among their collection, a peculiar energy weapon catches your eye. The explorer, with a grim determination, mentions that this advanced weapon is the key to securing passage through the hazardous terrains of this alien world. They propose a trade - the weapon in exchange for a vital resource needed for spacecraft repairs, 30 Golds. As you listen to the offer, the eerie sounds of unknown creatures echo in the distance. Will you accept the deal and risk the unknown dangers, or explore other options on this enigmatic exoplanet?</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/po.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

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

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["dragonScene"])
        st.write("Dragon's lair")

    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>Oh no! PM was wrong about going left! It\'s a Neural Network, AI, Deep Learning, Cloud Generated Dragonoid Monster! (NNADLBDGD)</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/dragon.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    # without a sword you will die
    if st.session_state.sword == 0:
        st.success(
            "Dragonoid uses matrix multiplication and you get hit in the head by loose neuron. You don't have anything to defend yourself."
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
            "Equipped with advanced alien weaponry you bought back then, you face a menacing Alien Monster. It roars with otherworldly echoes, and its alien physiology makes it a formidable opponent. Do you stand your ground and fight, or attempt to evade its powerful attacks?"
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
                        "Your tensor matrix manipulation skills are better than dragonoid Alien. Who would have guessed that these algebra classes would be useful after all?"
                    )
                    damage = random.randint(5, 10)
                    st.success("Dragon loses " + str(damage) + " HP")

                    st.session_state["dragon_hp"] = st.session_state[
                        "dragon_hp"
                    ] - random.randint(0, damage)

                    damage = random.randint(0, 8)
                    st.success(
                        "Dragonoid hits you back and you lose " + str(damage) + " HP"
                    )

                    st.session_state["health"] = st.session_state["health"] - damage
                    if st.session_state["dragon_hp"] <= 0:
                        st.session_state.dragon_alive = 0
                        st.success("DRAGONOID IS DEAD or at least to you are safe for now")
                else:
                    st.success("Dragonoid Alien is defeated")

            if scene_action.lower() == "up":
                if st.session_state.dragon_alive == 1:
                    st.success("Dragonoid Alien is still alive. Fight or flight!")
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
#               southpath Scene
#
################################################


def southpathScene():

    scene_identifier = "southpath"

    # possible actions
    directions = ["north", "south", "back", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("South path")
    with col2:

        scene_prompt = ""As you traverse the southern region of this alien world, you find yourself amidst a forest unlike any seen on Earth. 
        The air hums with the energy of a highly evolved civilization of ethereal beings. 
        Tall, crystalline structures rise like beacons, emanating a soft glow that bathes the area in an otherworldly light.
        The ground beneath your feet is a mosaic of responsive panels, adjusting to your every step with a gentle hum. 
        The rustling leaves and chirping creatures are not of the natural world but rather manifestations of the energy that permeates this realm. 
        Every movement seems to be observed by unseen entities, and the occasional pulse of energy sends shivers down your spine.
        You realize that you have entered the domain of an advanced civilization of spirits, 
        beings who have transcended the boundaries of the physical and embraced a form of existence beyond our understanding. 
        The forest holds secrets of their wisdom and power, and you are determined to uncover the mysteries that lie within. Will you boldly step forward into the heart of this advanced spirit civilization, 
        or tread cautiously, aware that your every action might be under the scrutiny of these ethereal beings?
        """

        # scene text
        # conditional if you have already seen the scene

        st.markdown(
            f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/south.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key=scene_identifier + "SceneActions",
        on_change=game_def.clear,
        args=[scene_identifier + "SceneActions"],
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
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "north":
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "south":
            st.session_state.place = "elfScene"
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
#               elf Scene
#
################################################


def elfScene():

    scene_identifier = "elf"

    # possible actions
    directions = ["north", "back", "help", "accept"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("Elf sorceress")
    with col2:

        scene_prompt = """As you traverse the fantastical land, you come across a celestial being unlike any you've encountered before. 
        A blonde-haired elf goddess, poised and graceful, stands before you. 
        Her eyes, a mesmerizing shade of violet, seem to penetrate into the depths of your soul.
        Her movements are as fluid and enchanting as a cosmic dance, and with a wave of her hand, she manipulates the energies around her. 
        It's evident that her power transcends the natural order of the universe. 
        Her voice, a harmonious blend of music and authority, resonates with ancient wisdom and knowledge that surpasses mortal understanding.
        
        The elf goddess reveals that she has been observing your journey and senses a destiny of cosmic proportions awaiting you. 
        With a benevolent smile, she offers her assistance. You can feel the cosmic magic emanating from her, a force that could prove invaluable in the challenges that lie ahead. 
        Will you accept the guidance and cosmic power of this ethereal being as you continue your interstellar journey?.
        """

        # scene text
        # conditional if you have already seen the scene
        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/elf1.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://github.com/Mattral/streamlit-Adventure/tree/main/images/cat.gif" class="image"><p>Sorcerres says: "We should go back."</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/elf2.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key=scene_identifier + "SceneActions",
        on_change=game_def.clear,
        args=[scene_identifier + "SceneActions"],
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
            st.session_state.place = "southpathScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "north":
            st.session_state.place = "southpathScene"
            game_def.temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "accept":
            st.info("Elf sorceress joined the party")
            st.session_state["scenes_counter"]["elf_counter"] += 1
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
        f'<div class="fantasy-container"><p>You enter the heart of the alien vault, and to your surprise, there's no hoard of gold but an advanced extraterrestrial technology repository – from a distant galaxy!<br><br> The power to harness and wield this cosmic knowledge is now in your hands. Do you choose to share this intergalactic repo for the benefit of others or keep it closely guarded, using its potential to create the most extraordinary applications the universe has ever seen? <br> As you contemplate, you recall the wisdom echoed through the cosmos, 'With great power comes great responsibility.' Though originally spoken to a spider, the words hold true for you now. The possibilities presented by Goddess's cosmic capabilities both amaze and humble you.<br> <br> The fate of this otherworldly knowledge is yours to decide. Will you be a beacon of sharing and collaboration, or will you embark on a solo journey to create the most awe-inspiring app in the vastness of the cosmic expanse?</div>',
        unsafe_allow_html=True,7
    )
    st.success("Thank you for taking your time!")
    st.info("If you liked the game you can check our repo and share it 🙂")
    st.caption("beta version")
