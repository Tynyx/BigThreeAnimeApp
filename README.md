# Big Three Anime Arc Explorer

This Preswald-powered app analyzes arcs from the **Big Three** anime: One Piece, Naruto, and Bleach. It allows users to interact with structured anime arc data and visualize trends based on total chapters and episodes.

## 🚀 Features

- ✅ Interactive table of anime arcs
- ✅ Filtered view showing arcs with more than 20 manga chapters
- ✅ Scatter plot comparing Total Episodes vs. Total Chapters
- ✅ Color-coded by anime title
- ✅ Custom branding, logo, and favicon

## 📊 Technologies Used

- Python
- Preswald platform
- Plotly for visualizations
- Pandas for data filtering

## 🗂 Dataset Fields

- `Arc`: Arc title
- `TotalChapters`: Number of manga chapters
- `TotalEpisodes`: Number of anime episodes
- `Manga%` / `Anime%`: Percentage of coverage
- `Anime`: One Piece, Naruto, or Bleach

## 📝 How to Run

To run this project in Preswald:
1. Upload the dataset (`BigThree.csv`) to your project
2. Register it in the `Config` under `[data.BigThree]`
3. Set `entrypoint = "Script"`
4. Save and publish

---

📁 This repo contains:
- `Script`: Main Python logic
- `Config`: Preswald configuration
- `data/BigThree.csv`: Arc dataset
- `images/`: Custom logo and favicon

---

## ✅ Built as part of a coding assessment
