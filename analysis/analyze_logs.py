import pandas as pd
import matplotlib.pyplot as plt
import os

LOG_FILES = {
    "BBR Low Latency": "logs/bbr_low_latency.log",
    "Cubic High Latency": "logs/cubic_high_latency.log",
    "Copa Low Latency": "logs/copa_low_latency.log"
}

summary = []

def process_log(name, path):
    df = pd.read_csv(path, sep=' ', header=None, names=["timestamp", "throughput", "rtt", "loss"], usecols=[0,1,2,3])
    df["time"] = range(len(df))

    # Plot throughput
    df.plot(x="time", y="throughput", title=f"{name} - Throughput")
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (Mbps)")
    plt.grid(True)
    plt.savefig(f"results/throughput_{name.lower().replace(' ', '_')}.png")
    plt.clf()

    # loss
    df.plot(x="time", y="loss", title=f"{name} - Loss")
    plt.xlabel("Time (s)")
    plt.ylabel("Loss Rate")
    plt.grid(True)
    plt.savefig(f"results/loss_{name.lower().replace(' ', '_')}.png")
    plt.clf()

    # RTT
    df.plot(x="time", y="rtt", title=f"{name} - RTT")
    plt.xlabel("Time (s)")
    plt.ylabel("RTT (ms)")
    plt.grid(True)
    plt.savefig(f"results/rtt_{name.lower().replace(' ', '_')}.png")
    plt.clf()

    # stats
    summary.append({
        "name": name,
        "avg_rtt": df["rtt"].mean(),
        "rtt_95": df["rtt"].quantile(0.95),
        "avg_throughput": df["throughput"].mean()
    })

for name, path in LOG_FILES.items():
    if os.path.exists(path):
        process_log(name, path)

# Scatter plot RTT vs Throughput
df_summary = pd.DataFrame(summary)
plt.scatter(df_summary["avg_rtt"], df_summary["avg_throughput"])
for i, row in df_summary.iterrows():
    plt.text(row["avg_rtt"]+1, row["avg_throughput"], row["name"], fontsize=8)
plt.title("RTT vs Throughput")
plt.xlabel("Average RTT (ms)")
plt.ylabel("Average Throughput (Mbps)")
plt.grid(True)
plt.savefig("results/rtt_vs_throughput.png")
