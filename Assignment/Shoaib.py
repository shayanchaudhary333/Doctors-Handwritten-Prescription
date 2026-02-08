# Kia Milestones Professional Bar Graph
import matplotlib.pyplot as plt

# Decades
decades = ["1940s-50s", "1970s-80s", "1990s", "2000s", "2010s", "2020s"]

# Impact Score (subjective scale)
impact = [3, 4, 6, 7, 8, 10]

# Key milestones for annotation
milestones = [
    "Founded as Kyungsung Precision Industry\nBicycle parts & Kia Industries",
    "Small cars production\nCollaborations with Mazda & Ford",
    "Asian Financial Crisis\nAcquired by Hyundai",
    "Design-driven brand\nSportage, Optima, Sorento",
    "Global rebranding\n'Movement That Inspires'\n180+ countries",
    "EV entry\nKia EV6\nEuropean Car of the Year 2022"
]

# Professional color palette (muted blues/teals/grey)
colors = ["#2E86AB", "#6C7A89", "#3AAFA9", "#A2D5AB", "#F6F5AE", "#F28C28"]

# Create bar graph
plt.figure(figsize=(14,7))
bars = plt.bar(decades, impact, color=colors, edgecolor='black', alpha=0.9)

# Add milestone labels on top of each bar
for bar, milestone in zip(bars, milestones):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, milestone, 
             ha='center', va='bottom', fontsize=10, rotation=0, wrap=True)

# Titles and labels
plt.title("Kia Milestones Over Decades", fontsize=18, fontweight='bold', color="#222222")
plt.ylabel("Impact / Significance (1-10)", fontsize=12)
plt.ylim(0, 12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Professional light grey background
plt.gca().set_facecolor("#FAFAFA")
plt.tight_layout()

plt.show()
