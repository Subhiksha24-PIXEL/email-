# -----------------------------------------
# Streamlit-based Project Management Dashboard
# -----------------------------------------
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -----------------------------------------
# Mock Project Data (could be from DB or Excel)
# -----------------------------------------
def load_data():
    data = {
        "Task": ["Design UI", "Set up Backend", "API Integration", "Testing", "Deployment"],
        "Owner": ["Alice", "Bob", "Charlie", "Dana", "Eli"],
        "Start Date": pd.to_datetime(["2025-06-01", "2025-06-02", "2025-06-04", "2025-06-07", "2025-06-10"]),
        "End Date": pd.to_datetime(["2025-06-03", "2025-06-06", "2025-06-08", "2025-06-10", "2025-06-12"]),
        "Progress (%)": [100, 70, 30, 0, 0],
        "Risk": ["Low", "Medium", "High", "Medium", "Low"]
    }
    return pd.DataFrame(data)

# -----------------------------------------
# Risk Color Mapping
# -----------------------------------------
def get_risk_color(risk):
    return {
        "Low": "green",
        "Medium": "orange",
        "High": "red"
    }.get(risk, "gray")

# -----------------------------------------
# Main Dashboard UI
# -----------------------------------------
def main():
    st.set_page_config(page_title="Project Health Dashboard", layout="wide")
    st.title("📊 Project Performance & Risk Dashboard")
    df = load_data()

    # ---- Project Progress Overview ----
    st.subheader("Overall Project Progress")
    avg_progress = int(df["Progress (%)"].mean())
    st.metric(label="Avg Completion", value=f"{avg_progress}%", delta=f"{avg_progress - 50}%")

    # ---- Gantt View / Timeline ----
    st.subheader("Timeline View")
    gantt_df = df.copy()
    gantt_df["Duration"] = gantt_df["End Date"] - gantt_df["Start Date"]
    fig = px.timeline(gantt_df, x_start="Start Date", x_end="End Date", y="Task",
                      color="Owner", text="Progress (%)", title="Task Schedule")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

    # ---- Risk Overview ----
    st.subheader("Risk Breakdown")
    risk_counts = df["Risk"].value_counts().reset_index()
    risk_counts.columns = ["Risk Level", "Count"]
    fig2 = px.pie(risk_counts, names="Risk Level", values="Count",
                  color="Risk Level",
                  color_discrete_map={"Low": "green", "Medium": "orange", "High": "red"})
    st.plotly_chart(fig2, use_container_width=True)

    # ---- Communication Status (Placeholder) ----
    st.subheader("Team Communication Snapshot")
    st.info("🛠️ Coming Soon: Integration with Slack / Email / Logs for visibility.")

    # ---- Raw Table View ----
    st.subheader("Detailed Task Table")
    colorized_df = df.copy()
    colorized_df["Risk Color"] = colorized_df["Risk"].apply(get_risk_color)
    st.dataframe(df.style.applymap(
        lambda val: "background-color: lightcoral" if isinstance(val, int) and val < 50 else ""
    ))

if __name__ == "__main__":
    main()
