import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Add rectangles and text for different states in the alert flow
# InfluxDB to Grafana
ax.add_patch(patches.FancyArrow(0.2, 0.8, 0.3, 0, width=0.02, color="black", head_width=0.05))
ax.text(0.05, 0.8, "InfluxDB", fontsize=12, ha='center', bbox=dict(facecolor="lightblue", edgecolor="black"))

ax.add_patch(patches.FancyArrow(0.5, 0.8, 0.2, 0, width=0.02, color="black", head_width=0.05))
ax.text(0.4, 0.8, "Grafana\nAlert Engine", fontsize=12, ha='center', bbox=dict(facecolor="lightgreen", edgecolor="black"))

# Threshold comparison and states
ax.add_patch(patches.FancyArrow(0.7, 0.8, 0.2, -0.3, width=0.02, color="black", head_width=0.05))
ax.text(0.9, 0.5, "Threshold Comparison", fontsize=12, ha='center', bbox=dict(facecolor="orange", edgecolor="black"))

# Add alert state transitions
ax.add_patch(patches.Rectangle((0.3, 0.4), 0.4, 0.1, edgecolor="black", facecolor="white"))
ax.text(0.5, 0.45, "OK\n(Metric within range)", ha="center", fontsize=10)

ax.add_patch(patches.Rectangle((0.3, 0.3), 0.4, 0.1, edgecolor="black", facecolor="yellow"))
ax.text(0.5, 0.35, "Pending\n(Breach detected)", ha="center", fontsize=10)

ax.add_patch(patches.Rectangle((0.3, 0.2), 0.4, 0.1, edgecolor="black", facecolor="red"))
ax.text(0.5, 0.25, "Alerting\n(Threshold sustained)", ha="center", fontsize=10)

# Arrows between states
ax.add_patch(patches.FancyArrow(0.5, 0.5, 0, -0.1, width=0.01, color="black", head_width=0.03))
ax.add_patch(patches.FancyArrow(0.5, 0.4, 0, -0.1, width=0.01, color="black", head_width=0.03))

# Notification flow
ax.add_patch(patches.FancyArrow(0.7, 0.2, 0.2, -0.1, width=0.02, color="black", head_width=0.05))
ax.text(0.9, 0.1, "Notification Triggered\n(Slack, Email, etc.)", fontsize=10, ha='center', bbox=dict(facecolor="lightcoral", edgecolor="black"))

# Hide axes
ax.axis('off')

plt.title("Alert Flow Logic", fontsize=16)
plt.show()
