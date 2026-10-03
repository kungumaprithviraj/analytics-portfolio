TITLE = 'Black Friday Sales Reporting'
GROUP = 'category'
VALUE = 'revenue_inr'
from pathlib import Path
import pandas as pd
import streamlit as st
st.set_page_config(page_title=TITLE, layout="wide")
st.title(TITLE)
st.caption("Synthetic demonstration data • Portfolio project by Kunguma Prithviraj Manmadhan")
df = pd.read_csv(Path(__file__).parent / "data/sample.csv")
selected = st.sidebar.multiselect("Filter " + GROUP, sorted(df[GROUP].unique()), default=sorted(df[GROUP].unique()))
df = df[df[GROUP].isin(selected)]
if df.empty:
    st.info("Select at least one category to view results.")
    st.stop()
a,b,c=st.columns(3)
a.metric('Net revenue (INR)',f"{df.revenue_inr.sum():,.0f}")
b.metric('Profit (INR)',f"{df.profit_inr.sum():,.0f}")
c.metric('Average order value (INR)',f"{df.revenue_inr.mean():,.0f}")
st.subheader("Breakdown by " + GROUP)
summary = df.groupby(GROUP).agg(records=(GROUP,"size"), total=(VALUE,"sum"), average=(VALUE,"mean"))
st.bar_chart(summary["total"])
st.dataframe(summary.round(2), use_container_width=True)
st.subheader("Explore source records")
st.dataframe(df, use_container_width=True)
st.download_button("Download filtered data",df.to_csv(index=False),"filtered.csv","text/csv")
