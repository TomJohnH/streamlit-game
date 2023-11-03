import streamlit as st
from streamlit_extras.stoggle import stoggle
import game_config
import game_def
import time
import random
import os
from PIL import Image

###############################################
#
#               intro Scene [0]
#
################################################


def introScene(): #[0]
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
                 보물찾기에 온 걸 환영해🥳🥳🥳 :) 각 스테이지마다 퀘스트가 있거덩 잘 따라가보렴ㅎㅎ \
                 글구 노래도 심심풀이삼아 틀어봐 ㅋㅋㅋㅋ \
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
#               sheep Scene [1]
#
################################################


def sheepScene(): #[1]
    # possible actions
    directions = ["isfj", "help"]
    st.title('지령1: 테퍼로 가시오')
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["sheepScene"])
        st.write("<이 아이는 커서 교회벤을 모는 멋진 언니가 되여>")
    with col2:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
                예절중시부모 + Green + Withhhhhhh + 임티 사용 필수 + 쿵야를 좋아하는 + 100명 있어도 안싸울 조합에 드는 + F 중에 가장 T + 칼답주는 \
                그런 MBTI라고 할 수 있져 근데 솔지키 I가 맞는지 의문이 듭니다. 크레이지 서머 레이디가 아닌 그냥 크레이지 처치 레이디라 하자구~~ 바쁘다 바뻐 현대 사회 ㅎㅎㅎㅎ</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("/home/ubuntu/streamlit-game/audio/school.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

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
#               cave Scene [2]
#
################################################


def caveScene(): #[2]

    # possible actions
    directions = ["26", "help"]
    st.title('지령2: 예린이 [졸업사진 찍었던 곳]으로 가시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["caveScene"])
        st.write("<테퍼에서 찍은 마지막 사진>") #"<로라야 저 J좀 K로 바꿔주렴 거슬리는구나>")
    with col2:
        # need to change
        if st.session_state["scenes_counter"]["cave_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
                저 때 너희들과 함께라서 너무 행벅했다야, 글구 그렇게 주인공처럼 사진을 찍혀 본 게 첨이었어ㅓㅓ\
                글구 우리 할무이, 어무이 잘 챙겨줘서 너어무 고맙다야ㅑㅑㅑㅑㅑ\
                울엄마가 너 칭찬 짜앙 마니 했옹~~~~ 너 증말 착하다고!!! \
                아ㅏ 저 때 사진을 보니께 또 저 때로 돌아가고 싶구마이\
                </p></div>',
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
#               po Scene [3]
#
################################################


def poScene(): # [3]혜미

    # possible actions
    directions = ["1997", "help"]
    ## 혜미언니 찾기
    st.title('지령3: [사랑토비 집게 한 사람] 찾으시오 (인증샷**)')
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
            다음에 다시 피츠버그에 가게 되는 날 유들이랑 같이 또 쉔리팍에서 인생샷을 건져보오\
            아마 저기 너랑 둘이 갔을 때 너가 아들 4명을 낳을 것 같다고 얘기했던거 같은디 ...\
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
#               dragon SCENE [4]
#
################################################


def dragonScene(): #[4]

    # possible actions
    directions = ["1980", "help"]

    # main_image
    st.title('지령4: 타이푸드를 먹었던 [책상 밑]을 살펴보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["dragonScene"])
        st.write("<혜미언니와 은성씌>")

    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>\
            저 때까지만 해도 저 주일이 우리 넷이 함께하는 마지막 주일인줄 알았던... 허허\
            너 붙잡고 교회에서 한 번 엉엉 운 게,, 지금 생각하면 웃픈 상황이 됬구마이\
            인생이 참 계획대로 흘러가진 않어ㅓㅓㅓㅓ\
            막판에 크레이지 나날들을 보냈지ㅣㅣ 다같이 조온잼😍 </p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/shivers.mp3", "rb")
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
    # caption below input
    st.caption("4자리 숫자: 사실 난 한동안 이거 또 못 외워서 위키에다 검색을 했다는.....")

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
#               southpath Scene [5]
#
################################################


def southpathScene(): #[5]

    scene_identifier = "southpath"
    st.title('지령5: 이 층에서 당신의 대학 선배를 찾으시오 (인증샷**)')
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
            덕분에 가봐야 할 한국 맛집도 늘어가는 중이구여\n \
            그래서 로라야 한국 언제와? 유동이한테 물어봐봐 나 파워 제이여\n \
            여기엔 돈룩업이라는 새로운 형식의 인생네컷이 생겼걸랑, 그거 찍어야재 \
            아니 글구 우리 매년 지금 만날 계획있자너 그거 또 정리 계속 업뎃해야되ㅣㅣ \
            만년 재택이었음 좋겠다 ㅜㅜㅜ \
            skrrrrrrrr한 프로필 감사여</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("audio/cant.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

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
            st.info("다시 한 번 쓸 기회 드림. 어렵다면 help를 치고 아래에 나오는 답을 볼 기회를 드려여")
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
    directions = ["1", "help"]
    st.title('지령6: 2층으로 올라가며 [기둥]을 잘 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["elfScene"])
        st.write("<담당하는 색이 생겨버렸져>")
    with col2:

        scene_prompt = """아니 우리 커플템 짱 많은거 같아. 벌써 몇 개여ㅕㅕㅕ진짜 태어나서 첨으로 이렇게 우정탬들 소장마니 해본 거 처음이여 
        여하튼 몬가 그 추억탬들 하나하나 저 때 뭐하고 놀았는 지 기억나서 좋은 듯 ㅋㅋㅋㅋㅋㅋㅋ
        이거 퀴즈 만들면서 다시 한 번 보게 됨 ㅋㅋㅋ 참고로 너가 준 대왕 핑크 토끼는 내 책상에 딱 올라가 있엉~~
        특히 나에게 꾀나 충격을 주었던 은지가 팔찌 주기 전 있었던 자동차 사태 :(
        은지야 스미마센
        그 운전자석 차문은 잘 있니? 허허;;
        여하튼 너가 준 작은 토끼는 내 회사 사원증에 달려있당~~~
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/missing.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("숫자만 입력해~~ 저 사진이랑 관련된 거 고르면 틀린 답이지롱!")

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
#               library SCENE [7]
#
################################################


def libraryScene(): #[7]

    scene_identifier = "library"

    # possible actions
    directions = ["전준모", "help"]
    st.title('지령7: 밀리스 앞 [의자밑]을 샅샅이 뒤져 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("<이 때는 너보다 작았구나 너의 동생 ㅋ>")
    with col2:

        scene_prompt = """너는 참 좋은 누나인거 같구, 준모도 좋은 동생인거 같구, 둘이 좋은 남매인거 같어\
        둘다 증말 짱 착해ㅋㅋㅋ 서로 라이딩 해주는 거 보면 진짜 부럽소!!   
        로라랑 준모랑 있을 때 무서운 버전의 로라볼 수 있음!! 어렸을 땐 업어주기도 했구마이, 좋은 누나인겨  
        여하튼 외동인 나로써는 경험해보지 못한 관계라 붸리 흥미로움
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/airplane.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한국이름이요 그럼 전씨이겄죠, 세글자 풀네임으로 써주세요~")

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
    st.title('지령8: 두달 전 26살이 된 친구를 찾으시오 (인증샷**)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<97 첫째 26짤 기념 생일 + 그 전 날은 워더 졸업식 행벅한 이틀>")
    with col2:

        scene_prompt = """저 기간에 먹은 모든 음식들이 맛났고, 다시 한 번 졸업식 때 라이딩부터 시작해서 축하와 사진들 고맙소 \
        내 증말 이 은혜 잊지 않으리오, 글구 쪼매 기둘리면 그대들의 졸업식들이 또 있구만요 \
        그날들을 위해 전 오늘 또 열시미 일합니다 허허 \
        로라도 오늘도 행벅하게 마무리 잘 하시구요 \
        카톡 방에서 계속 시험 있고 또 일하고, 올 한 해 막바지도 마니 또 달리시네요 \
        으으으 힘들지만 유는 할 수 있어, 왠지 알어? 로라니께!!!! \
        할 수 있즤ㅣ~~~~\
        로라여서 할 수 있는겨! 내 말 알줴 ㅎㅎㅎㅎ
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/exo.mp3", "rb")
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
    st.title('지령9: [화장실 옆 게시판]을 두 눈 부릅뜨고 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<로라랑 한국에서 더더더더 친해지기 시작쓰😍>")
    with col2:

        scene_prompt = """로라 덕분쓰 우리 4명 모였다 ㅋㅋㅋ 한국에 너 놀러왔을 때만 해도 이렇게 친해질 줄은 꿈에도 몰랐어~~
        너가 그 때만 해도 되게 열정적으로 너랑 또래 97인 유정이라는 친구가 있다는 거 막 얘기했을 때, 
        솔직히 그렇게 큰 기대를 안했거든 ㅜㅜㅜ
        CMU 다니면서 1년 동안 친한 칭구를 못 만든 상황이었어서 ㅜㅜㅜ
        그른데 증말 너어무 감사허다ㅏㅏㅏㅏㅏ
        유는 증말 연결고리야, 고로 너는 I가 아니라 E여!! 유노?
        """

        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/hype.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한글로 입력 부탁, 내가 저 사진에서 입고 있는 윗도리의 색은 뭐다?")

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
    st.title('지령10: 목도리 한 여자를 찾으시오 (인증샷**)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<덕분에들 저길 막판에 또갔다야>")
    with col2:

        scene_prompt = """로라야ㅑㅑㅑㅑㅑ 증말 너 덕분에 인생 처음으로 영유아부 쌤도 해보고,
        미디어팀도 해보고, 또 부동산지기도 막판에 하고,,
        피츠버그 있는 동안 그냥 다 외면하려고 했던 교회 사역을 너가 다시 마주보게 했고,
        학교 공부 따라가는 거 힘들다는 핑계로 썬데이 크리스천이 되어갔는디,,
        유 덕분에 섬김의 자리로 나아갔다야
        아리가또
        초큼 더 긴 편지는 한국 오는 유동이 손에 쥐어줄께
        글구 유어 비데이 프레젠또도 함께
        우리들의 커플템이 하나 더 생길거여~~
        부디 모두가 좋아하길 🙏🙏
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
    st.caption("한글로 입력 부탁, 우리의 아지트가 된 그 곳")

    directions_container.text_input(
        "현재 너가 있는 건물의 이름은?",
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


def step12():
    scene_identifier = "step12Scene"
    # possible actions
    directions = ["duquesne", "help"]
    st.title('지령11: 3층 올라가는 [계단 레일] 잘 보시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<눈물의 아이스크림>")
    with col2:
        scene_prompt = """
        요거는 내가 안 넣을 수가 없었엉~~~ 저 때 이후로 나 너네 앞에서 우는 게 겁나 편해졌엉ㅋㅋㅋ
        한 번 우니까 편하데? 정말 서러울 때 옆에 있어줘서 단거 먹고 마이 진정됬다야ㅑㅑ
        엄마 아닌 다른 사람 앞에서 여태껏 울어본 적이 없는디 ㅜㅜㅜ 그 때 진짜 친밀도가 겁나 높아진겨,,, 증말 어휴 이제 취직이란 단어도 
        지겹구마이, 한국에서 직장이 있는 게 이젠 감사할 뿐이고, 
        저 맘적으로 어려운 시기에 옆에서 계속 응원해주고, 지지해주고, 기도해줘서 고맙다이
        붸리붸리 아리가또 🫶🫶
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
    st.caption("영어로 입력 부탁(대소문자상관없음), ㅎㅎ 이거 스펠링 웰케 복잡하니, 처음에 미국 갔을 때, 듀케스네로 읽음")

    directions_container.text_input(
        "현재 재학중인 학교 이름은?",
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
        if scene_action.lower() == "duquesne":
            st.session_state.place = "step13Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("자 눈 크게 뜨고 철자를 확인해봐-나 구글링해서 가져온거라 정확함✌️✌️, 듀케스네만 영어로")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step13():
    scene_identifier = "step13Scene"
    # possible actions
    directions = ["파파이스", "help"]
    st.title('지령12: [치폴레 먹었던 책상]을 찾으시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<버지니아 만찬: 은성이 배고프게 만들기>")
    with col2:
        scene_prompt = """
        아니 왜 그 때서야 우리 간걸까, 버지니아
        그 좋은 데를 ㅋㅋㅋㅋ (물론 나는 편하게 갔지만, 유들 덕분에 졸기도 하고)
        버지니아 좋더라구! 턱히 Hmart! 저 음식들 저렇게 마니 시켜서 한국에선 먹지 못해ㅜㅜㅜ
        그냥 저런 푸드 코트들은 있지만 같이 갈 칭구가 없다규 ㅜㅜ
        우리 다같이 언젠가 한국이나 미국에 있을 때 가부자!
        글구 그거 알어? 지금 아무말 대잔치 같고, 의식의 흐름대로 흘러가는 거 같지만,
        다 요즘에 하고 싶었던 말들을 다 적는겨
        또, 그거 알아? 나 미국 취업은 언제나 도전할겨 ㅋㅋㅋㅋ 훗훗 오늘의 TMI!!
        내가 여기서 좀만 더 경력 쌓는다 ㅋㅋ 나의 도전은 계속된다 ㅋㅋㅋㅋ
        """

        if True: #st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            # audio_file = open("audio/shivers.mp3", "rb")
            # audio_bytes = audio_file.read()
            # st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption("한글로 입력 부탁-왜냐 요거 또 스펠링 확인해야될거 같거덩 (아름다운 한글사랑)-믕지가 이 질문을 싫어합니다 ㅋ")

    directions_container.text_input(
        "당신이 가장 좋아하는 치킨 브랜드는? (피츠버그에서)",
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
        if scene_action.lower() == "파파이스":
            st.session_state.place = "step14Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("자자자 루이지애나 출신인거 같던데 이 치킨?")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step14():
    scene_identifier = "step14Scene"
    # possible actions
    directions = ["psalm 121:6", "help"]
    st.title('지령13: 여기서 그림 그리던 아이를 찾으시오 (인증샷**)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<휴식을 취하고 있는 로라-장소 협찬 KCCP 지하>")
    with col2:
        scene_prompt = """
        영유아부라는 좋은 곳을 소개시켜준 로라쓰랑 보낸 추억중
        영유아부를 빼 놓을 수 없지!!
        저건 VBS 마지막 날 끝나고, 지하에서 휴식을 취하며 쉬고 있는 로라여~
        많은 아가들이 등반하고, 이사가고 그랬쟈ㅑㅑ
        한국에서도 영유아반 선생님 하고 싶다만, 여기 지원자가 많은 지 연락이 안 온다 ㅜㅜ
        경쟁이 치열한가벼 ㅜ 아가들이랑 놀고 싶은데 ㅜ
        요즘 영유아반 쌤들은 어떠니~~ 재밌는 일 없남? 소윤이 보고 싶구마이 ㅜㅜ
        나 미국에 혹시 가게 되면 소윤이가 나를 알아볼까? ㅋㅋ
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
    st.caption("아멘-영어와 숫자의 조합 예시) Matthew 1:1")

    directions_container.text_input(
        "당신의 (현) 카톡 상태메세지는?",
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
        if scene_action.lower() == "psalm 121:6":
            st.session_state.place = "step15Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("자 띄어쓰기가 들어간 어려운 답변이지-너의 카톡에 있는 그대로 입력 부탁")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step15():
    scene_identifier = "step15Scene"
    # possible actions
    directions = ["160", "help"]
    st.title('지령14: [은지한테 PPT 가르쳐준 곳]으로 가시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<우리 침 흘린 날>")
    with col2:
        scene_prompt = """
        난 놀이공원을 간다면 로라야 너랑 꼭 같이 가야 되는 거 알지 ㅋㅋㅋㅋㅋ
        저 때 난 미국의 놀이공원 수준을 경험하고, 아,, 난 맞지 않는구나를 느꼈고,
        한국와서도 에버랜드를 회사동기들이랑 한 번 갔단 말야 - 토했어....
        후후 나랑 놀이공원 능력치 비슷한 로라를 찾습니다~
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
    st.caption("숫자만여, 단위는 cm야~ 왜냐, 전 inch가 아직도 어렵거든여 + 저랑 차이가 별로 안나시져~후후 나 한국와서 키큼 후후")

    directions_container.text_input(
        "당신의 키는? ",
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
        if scene_action.lower() == "160":
            st.session_state.place = "step16Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("이건 뭐 무슨 힌트를 딱히 줘야 할 지도 모르겠다 ㅋㅋㅋ 맞춰랏!!!")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step16():
    scene_identifier = "step16Scene"
    # possible actions
    directions = ["31", "help"]
    st.title('지령15: 이 층에서 흰색 애플워치 스트랩 찬 사람을 찾으시오 (인증샷**)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<낭만이 가득한 그 곳: Butterwood>")
    with col2:
        scene_prompt = """
        여기 또 말하자면 끝도 없지, 근데 그거 알아, 나 갑자기 여기 이름 기억 안나서
        구글맵 킴. 우리 엄마 닮아가나봐.. 여튼 저기서 헤쳐 모여 하면서 점점 더 많은 얘기들을 나눴던 것 같다야~
        갑자기 저기 케잌이 먹고 싶구만, 진짜 한국 디저트 천국이지만, 저런 케잌은 아직 못 찾음 ㅜㅜ
        피츠버그에서 차를 마셨던 유일한 카페구마이, 늦게까지 열어서 진짜 수다 마니 떨었는디
        또 가자!! 부디 없어지지 말고, 오래오래 흥하길 ㅋㅋㅋ
        저 아늑한 느낌이 그립구마이!!
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
    st.caption("이건 유동이가 생각해낸 이과적 문제-계산기 써도 됨-근데 이거 새로고침하면 맨 처음문제부터 다시 풀어야될수도..-스미마센")

    directions_container.text_input(
        "당신의 생년월일을 다 더하면?",
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
        if scene_action.lower() == "31":
            st.session_state.place = "step17Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("1+9+9+7+1+1+3 구몬수학 1번 문항")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step17():
    scene_identifier = "step17Scene"
    # possible actions
    directions = ["콜라", "help"]
    st.title('지령16: 한 층 더 올라가서 [초록색 의자]를 찾으시오')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<듀케스네 앞에서...>")
    with col2:
        scene_prompt = """
        자자자자자자자 듀케스네 참 이쁘더라, 널찍하고~ 건물들이 다 이뻤어~~ 그리고 야경이 턱히!!!
        저기서 찍은 릴스 존잼이었지~~
        저 때 듀케스네 앞에서 본 뛰어댕기는 다람쥐, 너네가 나 생파 몰래하려고 속닥거리던 거, 
        피스타치오 피자, 너네가 차려준 짱맛 아점상-히야
        아니 이래서 동네 칭구가 짱이야
        그리고 듀케스네 후디 정말 잘 입는 중이야, 모두에게 이건 듀케인이라 읽는 거라며 알려주고 있지 :)
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
    st.caption("이건 믕지 출제-우리 모두 너의 최애 음료는 물이 1번이라 생각해, 그거 다음으로 좋아하는 건?")

    directions_container.text_input(
        "당신의 최애 음료는?",
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
        if scene_action.lower() == "콜라":
            st.session_state.place = "step18Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("땡! 힌트는 검정 탄산-한국어로 답변 부탁해요")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")

def step18():
    scene_identifier = "step18Scene"
    # possible actions
    directions = ["honda civic", "help"]
    st.title('지령17: 마지막 한 명 더 있지롱 (인증샷**)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<소고기와 돼지고기가 만난 날>")
    with col2:
        scene_prompt = """
        이번 여름에 진짜 동산 아웃팅 짱 많이 했다야ㅑㅑㅑ 계획을 짜는 게 서투른 나는 신나게 유들을 
        따라당겼제 ㅎㅎ 한국에서도 저런 캠핑 가고 싶다야, 근데 준비부터가 머리아퍼ㅓ
        한국 놀러 오면 고기파티하러가자ㅏ🍖 🍖 🍖 
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
    st.caption("차회사 모델명(숫자는 필요없음) (eg. nissan altima)")

    directions_container.text_input(
        "당신의 차 종은?",
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
        if scene_action.lower() == "honda civic":
            st.session_state.place = "step19Scene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("땡! 힌트는 혼다 씨빅을 영어로 하면?")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


def step19():
    scene_identifier = "step19Scene"
    # possible actions
    directions = ["mango dragonfruit refreshers", "mango dragonfruit refresher", "help"]
    st.title('지령18: [4층 화장실]을 일단 가. 그리고 두둥 이제 나한테 전활 걸어~~ 난 한예린이라고 해 (뭐 카톡전화나 페탐이나 다 가능)')
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier])
        st.write("<귀요미 로라>")
    with col2:
        scene_prompt = """
        이 노란 옷을 입은 귀여운 꼬마는 후에 멋진 약사가 되어 교회에서 다양한 곳곳에 투입되어 섬김이를 하게 됩니다.
        교회에서 일손이 필요한 곳엔 항상 가서 돕고 있지요~ 로라로라
        오늘 하루도 홧팅하시게나~ 이 스텝까지 오느라 고생 많았다야, 내가 개발 능력치가 좀 만 더 높았더라면 막 중간에 신기한 효과도 넣고
        그랬을 턴디, 지금 상황에선 이게 최선이구마이
        하여튼 오늘 잼나게 놀아라~~~ 
        준비 마니 하고 있는 거 같아ㅏ~~~유후~~~~
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
    st.caption("이 메뉴 한국에는 없다?! 영어로 입력 바래요~ 로라는 카페인 프리~")

    directions_container.text_input(
        "당신이 가장 좋아하는 스벅 메뉴는?",
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
        if scene_action.lower() == "mango dragonfruit refreshers" or scene_action.lower() == "mango dragonfruit refresher":
            st.session_state.place = "last"
            game_def.temp_clear() 
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("땡! 내가 파파고에 번역을 부탁했더니 망고 드레곤프루트 리프레셔라 하네 ㅋ 저게 한국어인가 ㅋ")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


def last():

    scene_identifier = "last"
    st.image(game_config.image_source[scene_identifier])

    # c1,c2,c3 = st.columns(3)
    # random.seed()
    # vpth = "/home/ubuntu/streamlit-game/images/nuki/"
    # img = os.listdir("/home/ubuntu/streamlit-game/images/nuki")
    # GameHelpImg1, GameHelpImg2, GameHelpImg3 =  random.sample(img, 3)
    # c1.image(Image.open(vpth +GameHelpImg1).resize((550, 550)))
    # c2.image(Image.open(vpth +GameHelpImg2).resize((550, 550)))
    # c3.image(Image.open(vpth +GameHelpImg3).resize((550, 550)))

    author_dtl = "<strong>Happy Playing: 😎 Yerin Han: yerinhan97@gmail.com</strong>"
    st.markdown(author_dtl, unsafe_allow_html=True)