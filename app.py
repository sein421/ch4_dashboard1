import pandas as pd
import streamlit as st

st.set_page_config(page_title="공부 습관 대시보드", layout="wide")
st.title("📚 공부 습관 대시보드")

df = pd.read_csv("study.csv")

total_students = len(df)
avg_score = df["점수"].mean()
avg_study = df["공부시간"].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="👥 전체 학생 수", value=f"{total_students}명")
with col2:
    st.metric(label="💯 평균 점수", value=f"{avg_score:.1f}점")
with col3:
    st.metric(label="⏱️ 평균 공부시간", value=f"{avg_study:.1f}시간")

st.divider()

min_val = float(df["공부시간"].min())
max_val = float(df["공부시간"].max())

min_study_time = st.slider(
    label="🔍 최소 공부시간을 선택하세요",
    min_value=min_val,
    max_value=max_val,
    value=min_val,
    step=0.5,
)

filtered_df = df[df["공부시간"] >= min_study_time]
st.write(
    f"현재 **{min_study_time}시간 이상** 공부한 학생은 총 **{len(filtered_df)}명**입니다."
)

st.subheader("📈 공부시간과 점수의 관계 (산점도)")
st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

st.subheader("📊 학생별 점수 (막대 그래프)")
st.bar_chart(data=filtered_df, x="학생ID", y="점수")