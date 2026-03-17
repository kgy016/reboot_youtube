import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="유튜브 알고리즘 세탁기", page_icon="🧼")

# CSS로 버튼 디자인 살짝 수정
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧼 유튜브 알고리즘 세탁기")
st.write("망가진 유튜브 알고리즘, 클릭 몇 번으로 '새 계정'처럼 깨끗하게 청소하세요.")

# --- Step 1 ---
st.header("Step 1. 시청 기록 삭제")
st.info("알고리즘의 근거가 되는 과거의 시청/검색 기록을 모두 지워야 합니다.")

# 링크 버튼 (새 창으로 열림)
st.link_button("🚀 구글 기록 삭제 페이지 바로가기", "https://myactivity.google.com/product/youtube")
st.caption("※ 접속 후 [삭제] -> [모든 데이터 삭제]를 선택하세요.")

st.divider()

# --- Step 2 ---
st.header("Step 2. 알고리즘 정화 (데이터 덮어쓰기)")
st.write("기록을 지운 직후가 가장 중요합니다! 아래의 '청정 키워드' 영상을 2~3개만 끝까지 시청하여 알고리즘을 다시 길들여주세요.")

clean_links = {
    "🌿 고화질 자연 풍경 (추천)": "https://www.youtube.com/results?search_query=nature+4k+relaxing",
    "🎹 집중용 클래식 음악": "https://www.youtube.com/results?search_query=classical+music+for+studying",
    "☕ 조용한 카페 ASMR": "https://www.youtube.com/results?search_query=cafe+asmr+ambience",
    "🪐 우주 과학 다큐멘터리": "https://www.youtube.com/results?search_query=universe+documentary+4k",
    "🍎 EBS 지식채널 e": "https://www.youtube.com/results?search_query=지식채널e",
    "🐾 귀여운 동물 영상": "https://www.youtube.com/results?search_query=cute+animal+videos"
}

# 2열로 버튼 배치
cols = st.columns(2)
for i, (name, url) in enumerate(clean_links.items()):
    with cols[i % 2]:
        st.link_button(name, url)

st.divider()

# --- Step 3 ---
st.header("Step 3. 재오염 방지 꿀팁")
with st.expander("다시는 알고리즘이 망가지지 않는 방법"):
    st.write("""
    1. **시크릿 모드 활용:** 아이들에게 폰을 빌려주거나, 평소 내 취향이 아닌 영상을 볼 땐 꼭 '시크릿 모드'를 켜세요.
    2. **관심 없음 적극 활용:** 추천 피드에 이상한 영상이 뜨면 즉시 [관심 없음] 혹은 [채널 추천 안 함]을 누르세요.
    3. **구독 목록 정리:** 아무리 기록을 지워도 구독 중인 채널이 문제라면 추천 피드는 바뀌지 않습니다. 안 보는 채널은 과감히 구독 취소!
    """)

st.success("이제 유튜브 앱을 다시 실행해 보세요. 훨씬 쾌적해진 피드를 만나실 수 있습니다!")
