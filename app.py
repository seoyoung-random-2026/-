
import streamlit as st

# 1. 기본권 리스트
rights = ["자유권", "사회권", "청구권", "참정권", "평등권", "인권"]


# 2. 기본권 설명 함수
def show_right(right):

    if right == "자유권":
        st.title("자유권")
        st.subheader("뜻")
        st.write("국가의 간섭을 받지 않고 자유롭게 생활할 수 있는 권리입니다.")
        st.subheader("특징")
        st.write("- 국가의 부당한 간섭을 받지 않을 권리입니다.")
        st.write("- 신체의 자유, 표현의 자유, 종교의 자유 등이 있습니다.")

    elif right == "사회권":
        st.title("사회권")
        st.subheader("뜻")
        st.write("인간다운 생활을 할 수 있도록 국가에 요구할 수 있는 권리입니다.")
        st.subheader("특징")
        st.write("- 인간다운 생활을 보장받을 권리입니다.")
        st.write("- 교육을 받을 권리, 근로의 권리, 사회보장권 등이 있습니다.")

    elif right == "청구권":
        st.title("청구권")
        st.subheader("뜻")
        st.write("국가에 특정한 행위를 요구할 수 있는 권리입니다.")
        st.subheader("특징")
        st.write("- 국가에 권리 구제를 요구할 수 있습니다.")
        st.write("- 재판청구권, 청원권, 국가배상청구권 등이 있습니다.")

    elif right == "참정권":
        st.title("참정권")
        st.subheader("뜻")
        st.write("국가의 정치에 참여할 수 있는 권리입니다.")
        st.subheader("특징")
        st.write("- 국민이 정치적 의사 결정에 참여할 수 있습니다.")
        st.write("- 선거권, 공무담임권, 국민투표권 등이 있습니다.")

    elif right == "평등권":
        st.title("평등권")
        st.subheader("뜻")
        st.write("합리적인 이유 없이 차별받지 않고 동등하게 대우받을 권리입니다.")
        st.subheader("특징")
        st.write("- 성별, 종교, 사회적 신분 등에 따른 부당한 차별을 금지합니다.")
        st.write("- 모든 국민은 법 앞에 평등합니다.")

    elif right == "인권":
        st.title("인권")
        st.subheader("뜻")
        st.write("인간이라면 누구나 태어나면서부터 가지는 기본적인 권리입니다.")

        st.subheader("특징")
        st.write("- 인간이라면 누구나 누릴 수 있습니다.")
        st.write("- 인간의 존엄성과 자유, 평등을 보장합니다.")
        st.write("- 국가나 다른 사람에 의해 함부로 침해받아서는 안 됩니다.")

        # 인권의 발전 과정
        st.subheader("📜 인권의 발전 과정")

        st.write("① 마그나 카르타 (1215년)")
        st.write("영국에서 왕의 권력을 제한하고 법에 따른 통치의 발전에 영향을 준 문서입니다.")

        st.write("② 명예혁명 (1688년)")
        st.write("영국에서 의회의 권한이 강화되고 왕권이 제한되었습니다. 이후 권리장전(1689년)을 통해 의회의 권리와 국민의 자유가 더욱 보장되었습니다.")

        st.write("③ 미국 독립혁명 (1776년)")
        st.write("미국 독립선언을 통해 모든 인간은 평등하게 태어났으며 생명, 자유, 행복 추구의 권리를 가진다는 생각이 강조되었습니다.")

        st.write("④ 인간과 시민의 권리 선언 (1789년)")
        st.write("프랑스 혁명 당시 발표되었습니다. 자유와 평등, 국민 주권, 재산권 등 인간의 기본적인 권리를 선언했습니다.")

        st.write("⑤ 여성 참정권 운동 (19세기 후반~20세기 초반)")
        st.write("여성들이 남성과 동등하게 투표하고 정치에 참여할 권리를 요구한 운동입니다. 뉴질랜드는 1893년 여성의 의회 선거 투표권을 법적으로 인정한 최초의 자치국이 되었습니다.")

        st.write("⑥ 바이마르 헌법 (1919년)")
        st.write("독일에서 제정된 헌법으로 노동권, 사회보장 등 사회권을 헌법에 규정하여 현대 복지국가 발전에 영향을 주었습니다.")

        st.write("⑦ 세계 인권 선언 (1948년)")
        st.write("국제연합(UN)이 채택했습니다. 모든 인간이 자유와 평등, 존엄성을 누려야 한다는 내용을 담았습니다.")

        st.success("인권은 오랜 역사 속에서 자유와 평등을 넘어 사회적 권리까지 확대되어 왔습니다.")

    else:
        st.write("올바른 기본권을 선택해주세요.")


# 3. 웹사이트 제목
st.title("📚 기본권을 알아봅시다!")
st.write("우리의 소중한 기본권에 대해 알아보아요!")

st.divider()


# 4. 기본권 목록 출력
st.subheader("어떤 기본권을 알아보고 싶나요?")

# for 반복문
for right in rights:
    st.write("✔️ " + right)


# 5. 기본권 선택 메뉴
selected_right = st.selectbox(
    "기본권 선택하기",
    rights
)


# 6. 알아보기 버튼
if "show_result" not in st.session_state:
    st.session_state.show_result = False

if st.button("알아보기"):
    st.session_state.show_result = True


# 7. 선택한 기본권 설명 출력
if st.session_state.show_result:

    st.divider()

    st.success("선택한 기본권을 알아봅시다!")

    show_right(selected_right)

    st.divider()

    # 8. 다른 기본권 알아보기 버튼
    if st.button("다른 기본권 알아보기"):
        st.session_state.show_result = False
        st.rerun()
