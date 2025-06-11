import preswald
from preswald import connect, get_df, table, text, plotly
import plotly.express as px

# Load dataset
connect()
df = get_df("BigThree")

# Cast necessary columns
df["TotalChapters"] = df["TotalChapters"].astype(int)
df["TotalEpisodes"] = df["TotalEpisodes"].astype(int)

# Filter manually (pandas way instead of SQL)
filtered_df = df[df["TotalChapters"] > 20]

# UI Table
text("# Big Three Anime Arc Explorer")
table(filtered_df, title="Arcs with More Than 20 Chapters")

# Visualization
fig = px.scatter(
    df,
    x="TotalEpisodes",
    y="TotalChapters",
    color="Anime",
    title="Canon vs Total Episodes by Arc"
)
plotly(fig)
