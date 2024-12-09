import streamlit as st

def intro_page():
    '''
    Intro 페이지 구성
    
    실험 설명, 개인정보 수집, 다음 페이지로 이동
    필수 정보를 모두 수집했을 경우에만 다음 페이지로 이동
    
    Args: None
        
    Returns: None
        
    '''
    # 제목
    st.title("🌟 Personalized Reading Assistant 🌟")
    st.divider()  # 구분선

    # 실험 설명
    intro_explanation_block()
    
    # 개인정보 수집
    personal_information_block()

    # 제출
    submitted = st.button("제출 및 다음 세션으로 진행 ➡️")
    if submitted:
        # 필수 항목 검증
        user = st.session_state["personal_information"]
        if user["name"] and user["age"] and user["gender"] and user["english_level"] and user["education_level"]:
            # 성공 및 페이지 이동
            st.success("정보가 성공적으로 제출되었습니다. 다음 세션으로 이동합니다.")
            st.session_state["page"] = "reading"
        else:
            # 오류 메시지 출력
            st.error("모든 필수 항목을 입력해주세요.")
        st.rerun()

def intro_explanation_block():
    '''
    개요 설명 블록
    
    주어진 텍스트 출력
    
    Args: None
        
    Returns: None
        
    '''
    st.markdown(
        """
        ##### 📚 더 나은 읽기 경험을 위해 도움을 줄 수 있는 정보를 입력해 주세요!

        📖 이 앱은 독서 효율을 높이고, 읽고 있는 내용을 더 잘 이해하고 기억할 수 있도록 돕습니다. \n
        🧠 당신의 독서 여정을 더욱 풍요롭고 유익하게 만들어주는 개인화된 피드백과 추천을 제공합니다.

        📈 이제, 당신의 독서를 더욱 스마트하게 즐길 수 있습니다!
        """,
        unsafe_allow_html=True
    )



def personal_information_block():
    '''    
    개인 정보 수집 블록

    개인 정보 수집 후 st.session_state["personal_information"]에 저장
    이름, 나이, 성별, 최종 학력, 관련 경험 또는 친숙한 분야, 추가 정보
    
    Args: None
        
    Returns: None
        
    '''
    # 개인정보 수집
    container = st.container(border=True)
    user_name = container.text_input("*이름:", placeholder="예: 홍길동")
    user_age = container.number_input("*나이:", min_value=10, max_value=100, value=20)
    user_gender = container.radio("*성별:", ["남성", "여성", "기타"], horizontal=True)
    english_level = container.radio("*영어 실력:", ["상", "중", "하"], horizontal=True)
    education_level = container.selectbox(
        "*최종 학력:",
        ["고등학교 졸업", "대학교 졸업", "대학원 석사 졸업", "대학원 박사 졸업"], index=1
    )
    familiar_fields = container.multiselect(
        "관련 경험 또는 친숙한 분야:",
        ["음식과 음료", "공연 예술", "비즈니스와 경제", "정치와 정부", "생물학", "화학", "컴퓨팅", "지구와 환경", "수학", "의학과 건강", "물리학", "공학", "기술"]
    )
    additional_info = container.text_area("추가 정보:", value ="나는 현재 건축학 석사 과정을 밟고 있으며, 연구 분야는 건설 기술 및 건설 관리야. 특히 건설 분야에서의 컴퓨팅에 관심을 가지고 있어.", placeholder="본인의 특기 사항이나 취미 등을 입력해주세요.")

    # session_state에 저장
    st.session_state["personal_information"] = {
        "name": user_name,
        "age": user_age,
        "gender": user_gender,
        "english_level": english_level,
        "education_level": education_level,
        "familiar_fields": familiar_fields,
        "additional_info": additional_info
    }
    