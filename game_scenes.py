import streamlit as st
from streamlit_extras.stoggle import stoggle
import game_config
import game_def
import time
import random
import os

###############################################
#
#               intro Scene
#
################################################


def introScene():
    # possible actions
    directions = ["20231103","help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["introScene"])
        st.write("<Now u r finally too old for LEO>")
    with col2:
        # scene text
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{st.session_state.player_name},\
                 보물찾기에 온걸 환영해🥳🥳🥳 :)각 스테이지마다 퀘스트가 있거덩 잘 따라가보렴ㅎㅎ \
                 HAPPY B-DAY </p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("audio/happy-bday.mp3", "rb") ## happy b-day
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    #st.caption(game_config.caption_below_input)
    directions_container.text_input(
        "오늘 날짜는?",
        key="introSceneActions",
        on_change=game_def.clear,
        args=["introSceneActions"],
    )
    st.info('예시처럼 입력해줘: 20230101')
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
        if scene_action.lower() == "20231103":
            #st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = (
                "sheepScene"  # we are moving our character to other scene
            )
            game_def.temp_clear()  # we are clearing text input
            st.experimental_rerun()  # rerun is streamlit specific and rerund the app

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("로라야 틀렸어ㅓㅓㅓ 좀만 더 생각해보렴 후후")
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
    directions = ["isfj", "help"]
    st.title('지령1: 테퍼로 가서 하람언니를 찾아랏')
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["sheepScene"])
        st.write("<이 아이는 커서 교회벤을 모는 멋진 언니가 되여>")
    with col2:
        st.markdown(
            f'<div class="fantasy-container" style="min-height:258.17px"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" \
            class="image"><p>예절중시부모 + Green + Withhhhhhh + 임티 사용 필수 + 쿵야를 좋아하는 + 100명 있어도 안싸울 조합에 드는 + F 중에 가장 T + 칼답주는 \
            그런 MBTI라고 할 수 있져 근데 솔지키 I가 맞는지 의문이 듭니다. 크레이지 서머 레이디 ❤️ </p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("/home/ubuntu/streamlit-game/audio/school.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    # for some reason we have here lenghty interaciton with sheep

    directions_container = st.empty()

    # caption below input
    st.caption("대소문자 상관없어영~~")

    # clearing text_input was suprisingly hard to figure out
    directions_container.text_input(
        "당신의 MBTI는?",
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

        if scene_action.lower() == "isfj":
            st.session_state.place = "caveScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("이걸 틀릴리는 없지 후후, 혹시라도 틀렸다면........")
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
    directions = ["26", "help"]
    st.title('지령2: 타이푸드 먹었던 책상밑을 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["caveScene"])
        st.write("<로라야 저 J좀 K로 바꿔주렴 거슬리는구나>")
    with col2:
        # scene text
        # conditional if you have already seen the scene
        if st.session_state["scenes_counter"]["cave_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
                저 때는 바야흐로 카니발. 로라 바빠서 함께하지 못해 아쉬웠어ㅜㅜ \
                저 때 날씨 차암 좋았는디~~\
                허지만 갈 수 있는 기회는 많으니께\
                난 또 이상한 포즈를 취하고 있고ㅎㅎㅎ 믕지 유동이 잘 나온 사진으로 골라봤엉</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/sun.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="/home/ubuntu/laura/streamlit-game/images/Laura/IMG_2961-removebg-preview.png" class="image"><p>You are back at the cave.</p></div>',
                unsafe_allow_html=True,
            )

    directions_container = st.empty()

    # caption below input
    st.caption("숫자만 입력부탁해요")
    if st.session_state["scenes_counter"]["trip_counter"] == 0:
        pass
        ##st.success("You feel exhausted and lose -5HP")
        # st.session_state.health = st.session_state.health - 5
        # st.session_state["scenes_counter"]["trip_counter"] = 1

    directions_container.text_input(
        "당신은 오늘부로 몇 살이 되었나요?",
        key="caveSceneActions",
        on_change=game_def.clear,
        args=["caveSceneActions"],
    )
    st.info('우리들의 세계에 온 걸 환영해, 막내야')
    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- back ---
        # ------------
        if scene_action.lower() == "26":
            st.session_state["scenes_counter"]["cave_counter"] += 1
            st.session_state.place = "poScene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Too old for Leo는 뭐다?")
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
    directions = ["1997", "help"]
    st.title('지령3: 안경쓴 노란 의자에 앉아있는 사람을 찾으시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["poScene"])
        st.write("<추억의 쉔리 팍>")
    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="/home/ubuntu/laura/streamlit-game/images/Laura/IMG_2961-removebg-preview.png" class="image"><p>\
            저 때가 나의 첫 쉔리 팍이었어, 워더 퍼스트 쉔리파크 익스피리언스 위드 유 가이즈 호호호호호호홓\
            저 뒤로 저기 진짜 자주 간 거 같구마이,, 그치만 저기서 김밥을 먹는 걸 못했어ㅓㅓㅓㅓㅓ 오노우 \
            유어 페이보릿 음악들 선별함 들어보33 천천히 계속 들어보소</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/kitsch.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("때는 바야흐로 IMF 시절이었지 (엠즤의 시작이랄까). 응답하라 시리즈의 시작이기도 하고 허허")

    directions_container.text_input(
        "그래서 너가 태어난 연도가 언제라고?",
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
        if scene_action.lower() == "1997":
            st.session_state.place = "dragonScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- RIGHT OR BACK ---
        # --- BUY ---
        # ------------

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("숫자 4개, 우리 톡방에 있는 숫자 4개 유노롸잇?")
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
    directions = ["1980", "help"]

    # main_image
    st.title('지령4: 2층 밀리스 의자 밑을 샅샅이 뒤져 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["dragonScene"])
        st.write("")

    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
            저 때까지만 해도 저 주일이 우리 넷이 함께하는 마지막 주일인줄 알았던 허허\
            인생이 참 계획대로 흘러가진 않어ㅓㅓㅓㅓ\
            막판에 크레이지 나날들을 보냈지ㅣㅣ 다같이 조온잼😍 </p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/kitsch.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")
    
    directions_container = st.empty()
    directions_container.text_input(
        "KCCP 건물 비밀번호는?",
        key="dragonSceneActions",  # potentially dynamic key based on function name?
        on_change=game_def.clear,
        args=[
            "dragonSceneActions"
        ],  # potentially dynamic key based on function name?
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')

        if scene_action.lower() == "1980":
            st.session_state.place = "southpathScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("TMI: KCCP 생일이랑 내 생일 같음 (연도제욐ㅋㅋㅋ)")
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
    st.title('지령5: 게시판으로 가시오')
    # possible actions
    directions = ["sung_is_mandugook", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["southpathScene"])
        st.write("<Skrrrrrrrrrrrrrrr>")
    with col2:
        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
            우리 넷 중에 가장 인스타 짤들을 많이 보유한 로라로라\n \
            덕분에 가봐야할 한국 맛집도 늘어가는 중이구여\n \
            그래서 로라야 한국 언제와? 유동이한테 물어봐봐 나 파워 제이여\n \
            skrrrrrrrr한 프로필 감사여</p></div>',
            unsafe_allow_html=True,
        )
        # audio_file = open("audio/south.mp3", "rb")
        # audio_bytes = audio_file.read()
        # st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("요거요거 철자 확인 잘 부탁드려여")

    directions_container.text_input(
        "로라 저 캐릭터 인스타계정 아이디?",
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

        if scene_action.lower() == "sung_is_mandugook":
            st.session_state.place = "elfScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("다시한번 쓸 기회 드림 ")
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
    directions = ["1", "2", "3", "help"]
    st.title('지령6: 머리 땋고 있는 사람을 찾으시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["elfScene"])
        st.write("<담당하는 색이 생겨버렸져>")
    with col2:

        scene_prompt = """아니 우리 커플템 짱 많은거 같아. 벌써 몇 개여ㅕㅕㅕ진짜 태어나서 첨으로 이렇게 우정탬들 소장마니 해본 거 처음이여 
        여하튼 몬가 그 추억탬들 하나하나 저 때 뭐하고 놀았는 지 기억나서 좋은 듯 ㅋㅋㅋㅋㅋㅋㅋ
        이거 퀴즈 만들면서 다시 한 번 보게 됨 ㅋㅋㅋ 참고로 너가 준 핑크 대왕 핑크 인형은 내 책상에 딱 올라가 있엉~~
        특히 나에게 꾀나 충격을 주었던 은지가 팔찌 주기 전 있었던 자동차 사태 
        은지야 스미마센
        그 운전자석 차문은 잘 있니? 허허;;
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/shivers.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("숫자만 입력해~~ 저 사진은 답과 관련이 없어")

    directions_container.text_input(
        "9779의 첫 우정템은? 1. 시애틀에서 사온 열쇠고리 2. 은지의 깜짝 팔찌 선물 3. 유동이의 열쇠 다는 목걸이 4. 은성이의 핑꾸 토끼",
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
        if scene_action.lower() == "1":
            st.session_state.place = "libraryScene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("그럴 수 있어, 다시 생각해 봐..... (사실 나도 가물가물한데 사진 보면서 기억남 ㅋ)")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               library SCENE
#
################################################


def libraryScene():

    scene_identifier = "library"

    # possible actions
    directions = ["전준모", "help"]
    st.title('지령7: 3층 올라가는 계단을 한 번 구석 구석 살펴보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("이 때는 너보다 작았구나 너의 동생 ㅋ")
    with col2:

        scene_prompt = """
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            # audio_file = open("audio/shivers.mp3", "rb")
            # audio_bytes = audio_file.read()
            # st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한국이름이요 그럼 전씨이겄죠")

    directions_container.text_input(
        "당신의 동생 이름은?",
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
        if scene_action.lower() == "전준모":
            st.session_state.place = "step9Scene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("ㅎㅎㅎㅎㅎㅎㅎㅎ 이건 솔직히 알아야되지만 허허 엄빠 찬스 가능 ")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               step 9
#
################################################


def step9():

    scene_identifier = "step9Scene"

    # possible actions
    directions = ["exo", "help"]
    st.title('지령8: 치폴레 먹었던 책상을 함 찾아보시오!')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("믕지 26짤 + 그 전날 워더 졸업식 행벅한 이틀")
    with col2:

        scene_prompt = """아니 우리 커플템 짱 많은거 같아. 벌써 몇 개여ㅕㅕㅕ진짜 태어나서 첨으로 이렇게 우정탬들 소장마니 해본 거 처음이여\
        여하튼 몬가 그 추억탬들 하나하나 저 때 뭐하고 놀았는 지 기억나서 좋은 듯 ㅋㅋㅋㅋㅋㅋㅋ
        특히 나에게 꾀나 충격을 주었던 은지가 팔찌 주기 전 있었던 자동차 사태
        은지야 스미마센
        그 운전자석 차문은 잘 있니? 허허
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/shivers.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("당근빠따 영문으로 답은 입력해야지ㅣ")

    directions_container.text_input(
        "당신의 예전 최애 아이돌은?",
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
        if scene_action.lower() == "exo":
            st.session_state.place = "step10Scene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("너가 엑소엘이었다는 걸 알았을 때, 내적 친밀감 더커짐 ㅋㅋ")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

###############################################
#
#               step 10
#
################################################


def step10():

    scene_identifier = "step10Scene"

    # possible actions
    directions = ["핑크", "help"]
    st.title('지령10: 유정이를 찾아봐')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("Elf sorceress")
    with col2:

        scene_prompt = """아니 우리 커플템 짱 많은거 같아. 벌써 몇 개여ㅕㅕㅕ진짜 태어나서 첨으로 이렇게 우정탬들 소장마니 해본 거 처음이여\
        여하튼 몬가 그 추억탬들 하나하나 저 때 뭐하고 놀았는 지 기억나서 좋은 듯 ㅋㅋㅋㅋㅋㅋㅋ
        특히 나에게 꾀나 충격을 주었던 은지가 팔찌 주기 전 있었던 자동차 사태
        은지야 스미마센
        그 운전자석 차문은 잘 있니? 허허
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/shivers.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한글로 입력 부탁")

    directions_container.text_input(
        "당신의 최애 색은?",
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
        if scene_action.lower() == "핑크":
            st.session_state.place = "step11Scene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("핑꾸 아님, pink아님, 그럼 뭐다?")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step11():

    scene_identifier = "step11Scene"

    # possible actions
    directions = ["테퍼", "help"]
    st.title('지령10: 한예린한테 전화를 거시오 (페탐이던 카톡전화던 다 받아드림)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("Elf sorceress")
    with col2:

        scene_prompt = """아니 우리 커플템 짱 많은거 같아. 벌써 몇 개여ㅕㅕㅕ진짜 태어나서 첨으로 이렇게 우정탬들 소장마니 해본 거 처음이여\
        여하튼 몬가 그 추억탬들 하나하나 저 때 뭐하고 놀았는 지 기억나서 좋은 듯 ㅋㅋㅋㅋㅋㅋㅋ
        특히 나에게 꾀나 충격을 주었던 은지가 팔찌 주기 전 있었던 자동차 사태
        은지야 스미마센
        그 운전자석 차문은 잘 있니? 허허
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/shivers.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한글로 입력 부탁")

    directions_container.text_input(
        "현재 위치함 건물의 이름은?",
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
        if scene_action.lower() == "테퍼":
            st.session_state.place = "step12Scene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("영어로는 Tepper허지만 ㅐ인지 ㅔ인지 헷갈릴 수 있으므로 ㅔ 인거 알려드림")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

# author_dtl = "<strong>Happy Playing: 😎 Yerin Han: yerinhan97@gmail.com</strong>"
# st.markdown(author_dtl, unsafe_allow_html=True)


# author_dtl = "<strong>Happy Playing: 😎 Yerin Han: yerinhan97@gmail.com</strong>"
# st.markdown(author_dtl, unsafe_allow_html=True)