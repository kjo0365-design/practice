import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 설정
st.set_page_config(page_title="2024 폭염 장기화 대응 정책 실효성 분석", layout="wide")

# 사이드바 네비게이션
st.sidebar.title("보고서 목차")
menu = st.sidebar.radio(
    "메뉴를 선택하세요:",
    ["1. 서론", "2. 기상 요인 분석", "3. 정책 실효성 검증", "4. 결론 및 정책 제언"]
)

if menu == "1. 서론":
    st.header("제 1 장. 서론 [cite: 2]")
    st.markdown("""
    현대 사회에서 기후변화는 더 이상 미래의 위협이 아닌 현재의 직접적인 재난입니다[cite: 4].
    본 보고서는 가상의 2024년 8월 전국 단위 데이터를 기반으로 폭염과 노인 온열질환 간의 상관관계를 명확히 규명하고, 현재 시행 중인 주요 폭염 대응 정책들의 실질적인 효과를 검증하는 데 목적이 있습니다[cite: 14].
    
    * **핵심 타겟**: 생리적 체온 조절 기능이 약화되어 치명적인 온열질환 위험이 높은 65세 이상 노인 인구[cite: 6, 7].
    * **폭염의 특성**: 폭염은 노출 빈도와 강도가 주거 형태 및 사회적 연결망에 따라 극명하게 갈리는 '불평등한 재난'입니다[cite: 11].
    """)

elif menu == "2. 기상 요인 분석":
    st.header("제 2 장. 환경 기상 요인과 온열질환 발생 분석 [cite: 17]")
    st.markdown("""
    단순한 기온 상승뿐만 아니라, 높은 습도가 결합된 '일 최고 체감온도'의 상승 추이를 분석했습니다[cite: 20].
    특히 전국 평균 체감온도가 폭염 경보 기준인 **35도에 도달한 시점**을 기점으로 환자 발생 수가 기하급수적으로 폭증하는 임계점(Tipping Point) 패턴이 확인되었습니다[cite: 25].
    """)
    
    # 임계점 시뮬레이션 데이터 및 그래프
    np.random.seed(42)
    days = np.arange(1, 32)
    heat_index = np.linspace(30, 38, 31) + np.random.normal(0, 0.5, 31)
    er_visits = np.where(heat_index >= 35, (heat_index - 34)**3 * 10 + np.random.normal(0, 5, 31), heat_index * 2 + np.random.normal(0, 2, 31))
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax2 = ax1.twinx()
    
    ax1.plot(days, heat_index, 'r-', label="Heat Index (C)")
    ax2.bar(days, er_visits, alpha=0.5, label="ER Visits")
    
    ax1.set_xlabel("August (Days)")
    ax1.set_ylabel("Heat Index", color='r')
    ax2.set_ylabel("Elderly ER Visits", color='b')
    ax1.axhline(35, color='black', linestyle='--', label="Tipping Point (35C)")
    
    st.pyplot(fig)

elif menu == "3. 정책 실효성 검증":
    st.header("제 4 장. 폭염 대응 정책 실효성 분석 [cite: 36]")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. 방문 케어 서비스 예방 효과 [cite: 37]")
        st.markdown("방문 케어 서비스 수혜율이 높은 '우수 그룹'이 '취약 그룹'에 비해 일평균 응급실 방문 수가 유의미하게 낮게 나타났습니다[cite: 42].")
        
        # 박스플롯 시뮬레이션 데이터 
        care_low = np.random.normal(40, 20, 100)
        care_high = np.random.normal(25, 10, 100)
        care_data = pd.DataFrame({
            'ER Visits': np.concatenate([care_low, care_high]),
            'Group': ['Low (Vulnerable)']*100 + ['High (Excellent)']*100
        })
        
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.boxplot(x='Group', y='ER Visits', data=care_data, palette="Set2", ax=ax1)
        ax1.set_title("Elderly ER Visits by Care Service Rate")
        st.pyplot(fig1)

    with col2:
        st.subheader("2. 무더위 쉼터 접근성에 따른 실효성 [cite: 44]")
        st.markdown("도보 접근 시간이 15분을 초과하는 지역부터 쉼터 이용률이 바닥으로 수렴하며 온열질환자가 급증하는 역의 상관관계가 확인됩니다[cite: 50, 51].")
        
        # 산점도 시뮬레이션 데이터 [cite: 48]
        dist = np.random.uniform(5, 25, 20)
        utilization = 20 - 0.6 * dist + np.random.normal(0, 1, 20)
        er_visits_scatter = 300 + 30 * dist + np.random.normal(0, 50, 20)
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax3 = ax2.twinx()
        sns.regplot(x=dist, y=utilization, ax=ax2, color="blue", label="Shelter Util")
        sns.regplot(x=dist, y=er_visits_scatter, ax=ax3, color="red", label="ER Visits")
        ax2.set_xlabel("Shelter Dist (mins)")
        ax2.set_ylabel("Shelter Utilization", color="blue")
        ax3.set_ylabel("ER Visits", color="red")
        st.pyplot(fig2)

elif menu == "4. 결론 및 정책 제언":
    st.header("제 5 장. 결론 및 데이터 기반 맞춤형 정책 제언 [cite: 53]")
    st.markdown("폭염은 사회적 재난이며, 피해 저감을 위해 다음 3대 핵심 정책을 제언합니다[cite: 55, 56].")
    
    st.info("""
    **1. 대형 거점 위주에서 '초근거리 마이크로 무더위 쉼터'로 패러다임 전환 [cite: 57]**
    - 노인 인구 밀집 구역 500m(도보 10분 이내)의 카페, 약국 등을 쉼터로 지정하여 이동 중 2차 피해 차단[cite: 59, 60].
    
    **2. 폭염 경보 시 '핀셋형 긴급 방문 돌봄망' 가동 의무화 [cite: 61]**
    - 경보 3일 이상 지속 시 집배원, 배달 종사자 등을 활용한 다중 감시망 구축[cite: 62, 63].
    
    **3. 체감온도 연동형 '스마트 야간 무더위 쉼터 및 에너지 바우처' 도입 [cite: 64]**
    - 24시간 수면 특화형 야간 무더위 쉼터 운영[cite: 66].
    - 체감온도 35도 초과 시 즉각 보전해주는 '폭염 핀셋 에너지 바우처' 제도 도입[cite: 67].
    """)

st.sidebar.markdown("---")
st.sidebar.caption("본 대시보드는 가상의 시뮬레이션 데이터를 바탕으로 제작되었습니다[cite: 72].")
