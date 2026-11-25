
import streamlit as st

st.set_page_config(
    page_title="RIGHTS LAB | 기본권 알아보기",
    page_icon="◈",
    layout="wide"
)

# -----------------------------
# 1. 디자인 CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #18264a 0%, transparent 40%),
        radial-gradient(ellipse at 90% 35%, #20143e 0%, transparent 35%),
        #090d18;
    color: #f3f5ff;
    font-family: 'Pretendard', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}

h1, h2, h3, p, label, li {
    color: #f3f5ff !important;
    font-family: 'Pretendard', sans-serif !important;
}

.hero {
    background: linear-gradient(120deg, #17274b, #222044);
    border: 1px solid #35446c;
    border-radius: 24px;
    padding: 42px 38px;
    margin-bottom: 32px;
    position: relative;
}

.tag {
    color: #8daaff;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 3px;
}

.hero-title {
    font-size: 43px;
    font-weight: 900;
    line-height: 1.3;
    margin-top: 17px;
    color: white;
}

.hero-desc {
    color: #b5bfd9;
    font-size: 16px;
    margin-top: 12px;
}

.section-label {
    color: #8ea9ff;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 35px;
    margin-bottom: 12px;
}

.info-card {
    background: #141d30;
    border: 1px solid #293653;
    border-radius: 17px;
    padding: 23px;
    margin: 12px 0;
}

.info-title {
    font-size: 23px;
    font-weight: 800;
    color: #9db5ff;
    margin-bottom: 12px;
}

.info-text {
    color: #d2daed;
    font-size: 16px;
    line-height: 1.9;
}

.history-card {
    background: #141d30;
    border-left: 3px solid #788fff;
    border-radius: 0 13px 13px 0;
    padding: 18px 22px;
    margin: 13px 0;
}

.history-year {
    color: #91a9ff;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1px;
}

.history-name {
    color: #ffffff;
    font-size: 19px;
    font-weight: 800;
    margin: 7px 0;
}

.history-desc {
    color: #b9c4dc;
    font-size: 14px;
    line-height: 1.8;
}

div.stButton > button {
    background: linear-gradient(110deg, #4776ff, #8258f5);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 13px 18px;
    font-weight: 800;
    min-height: 48px;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: linear-gradient(110deg, #668cff, #a07bff);
    border: none;
    transform: translateY(-2px);
}

div[data-baseweb="select"] > div {
    background-color: #182238;
    border: 1px solid #394a6d;
    border-radius: 12px;
    color: white;
}

hr {
    border-color: #28344e;
}

.footer {
    color: #697995;
    font-size: 12px;
    text-align: center;
    margin-top: 60px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# 2. 기본권 리스트
# -----------------------------
rights = ["자유권", "사회권", "청구권",
          "참정권", "평등권", "인권"]


# -----------------------------
# 3. 기본권 설명 함수
# -----------------------------
def show_right(right):

    if right == "자유권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">01 / 자유권</div>
        <div class="info-text">
        <b>뜻</b><br>
        국가의 간섭을 받지 않고 자유롭게 생활할 수 있는 권리입니다.<br><br>
        <b>특징</b><br>
        • 국가의 부당한 간섭을 받지 않을 권리입니다.<br>
        • 신체의 자유, 표현의 자유, 종교의 자유 등이 있습니다.
        </div></div>
        """, unsafe_allow_html=True)

    elif right == "사회권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">02 / 사회권</div>
        <div class="info-text">
        <b>뜻</b><br>
        인간다운 생활을 할 수 있도록 국가에 요구할 수 있는 권리입니다.<br><br>
        <b>특징</b><br>
        • 인간다운 생활을 보장받을 권리입니다.<br>
        • 교육을 받을 권리, 근로의 권리, 사회보장권 등이 있습니다.
        </div></div>
        """, unsafe_allow_html=True)

    elif right == "청구권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">03 / 청구권</div>
        <div class="info-text">
        <b>뜻</b><br>
        국가에 특정한 행위를 요구할 수 있는 권리입니다.<br><br>
        <b>특징</b><br>
        • 국가에 권리 구제를 요구할 수 있습니다.<br>
        • 재판청구권, 청원권, 국가배상청구권 등이 있습니다.
        </div></div>
        """, unsafe_allow_html=True)

    elif right == "참정권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">04 / 참정권</div>
        <div class="info-text">
        <b>뜻</b><br>
        국민이 국가의 정치에 참여할 수 있는 권리입니다.<br><br>
        <b>특징</b><br>
        • 국민이 정치적 의사 결정에 참여할 수 있습니다.<br>
        • 선거권, 공무담임권, 국민투표권 등이 있습니다.
        </div></div>
        """, unsafe_allow_html=True)

    elif right == "평등권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">05 / 평등권</div>
        <div class="info-text">
        <b>뜻</b><br>
        합리적인 이유 없이 차별받지 않고 동등하게 대우받을 권리입니다.<br><br>
        <b>특징</b><br>
        • 성별, 종교, 사회적 신분 등에 따른 부당한 차별을 금지합니다.<br>
        • 모든 국민은 법 앞에 평등합니다.
        </div></div>
        """, unsafe_allow_html=True)

    elif right == "인권":
        st.markdown("""
        <div class="info-card">
        <div class="info-title">06 / 인권</div>
        <div class="info-text">
        <b>뜻</b><br>
        인간이라면 누구나 태어나면서부터 가지는 기본적인 권리입니다.<br><br>
        <b>특징</b><br>
        • 인간이라면 누구나 누릴 수 있습니다.<br>
        • 인간의 존엄성과 자유, 평등을 보장합니다.<br>
        • 국가나 다른 사람에 의해 함부로 침해받아서는 안 됩니다.
        </div></div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-label">HISTORY OF HUMAN RIGHTS</div>
        <h2>인권의 발전 과정</h2>
        <p style="color:#9baac8">
        오늘날의 인권이 만들어지기까지의 역사적 흐름
        </p>
        """, unsafe_allow_html=True)

        history = [
            ("1215", "마그나 카르타",
             "영국에서 왕의 권력을 제한하고 법에 따른 통치의 발전에 영향을 준 문서입니다."),

            ("1688", "명예혁명",
             "영국에서 의회의 권한이 강화되고 왕권이 제한되었습니다. 이후 1689년 권리장전으로 의회의 권리와 국민의 자유가 더욱 보장되었습니다."),

            ("1776", "미국 독립혁명",
             "미국 독립선언을 통해 모든 인간의 평등과 생명, 자유, 행복 추구의 권리가 강조되었습니다."),

            ("1789", "인간과 시민의 권리 선언",
             "프랑스 혁명 당시 발표되었습니다. 자유와 평등, 국민 주권, 재산권 등 인간의 기본적인 권리를 선언했습니다."),

            ("19세기 후반~20세기 초반", "여성 참정권 운동",
             "여성들이 투표하고 정치에 참여할 권리를 요구한 운동입니다. 뉴질랜드는 1893년 여성의 의회 선거 투표권을 법적으로 인정했습니다."),

            ("1919", "바이마르 헌법",
             "독일에서 제정된 헌법으로 노동권과 사회보장 등 사회권을 규정하여 현대 복지국가 발전에 영향을 주었습니다."),

            ("1948", "세계 인권 선언",
             "UN이 채택했습니다. 모든 인간이 자유와 평등, 존엄성을 누려야 한다는 보편적인 인권 원칙을 담았습니다.")
        ]

        # for 반복문을 이용한 역사 출력
        for year, name, desc in history:
            st.markdown(f"""
            <div class="history-card">
                <div class="history-year">{year}</div>
                <div class="history-name">{name}</div>
                <div class="history-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

        st.success("인권은 역사 속에서 자유와 평등을 넘어 사회적 권리까지 확대되어 왔습니다.")

    else:
        st.warning("올바른 기본권을 선택해주세요.")


# -----------------------------
# 4. 웹사이트 메인 화면
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="tag">RIGHTS LAB / 2026</div>
    <div class="hero-title">
        기본권을<br>알아봅시다.
    </div>
    <div class="hero-desc">
        EVERYONE HAS RIGHTS.<br>
        우리가 누려야 할 권리, 지금 알아보세요.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# 5. 기본권 선택 화면
# -----------------------------
if "show_result" not in st.session_state:
    st.session_state.show_result = False

if "selected_right" not in st.session_state:
    st.session_state.selected_right = "자유권"


if not st.session_state.show_result:

    st.markdown("""
    <div class="section-label">EXPLORE YOUR RIGHTS</div>
    <h2>어떤 권리가 궁금한가요?</h2>
    <p style="color:#9baac8">
    6가지 기본권 중 하나를 선택해 보세요.
    </p>
    """, unsafe_allow_html=True)

    # 리스트와 for 반복문 사용
    cols = st.columns(3)

    for i, right in enumerate(rights):
        with cols[i % 3]:
            if st.button(right + "  →", key="right_" + right,
                         use_container_width=True):
                st.session_state.selected_right = right

    st.markdown("<br>", unsafe_allow_html=True)

    selected_right = st.selectbox(
        "선택한 기본권",
        rights,
        index=rights.index(st.session_state.selected_right)
    )

    if st.button("알아보기  →", use_container_width=True):
        st.session_state.selected_right = selected_right
        st.session_state.show_result = True
        st.rerun()


# -----------------------------
# 6. 결과 화면
# -----------------------------
else:

    st.markdown("""
    <div class="section-label">YOUR SELECTED RIGHT</div>
    """, unsafe_allow_html=True)

    st.title(st.session_state.selected_right)

    show_right(st.session_state.selected_right)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← 다른 기본권 알아보기",
                 use_container_width=True):
        st.session_state.show_result = False
        st.rerun()


# -----------------------------
# 7. 하단 문구
# -----------------------------
st.markdown("""
<div class="footer">
    RIGHTS LAB · KNOW YOUR RIGHTS · PROTECT YOUR RIGHTS
</div>
""", unsafe_allow_html=True)

