import os
import pandas as pd
import matplotlib.pyplot as plt

def parse_log(logfile, title):
    df = pd.read_csv(logfile, sep=' ', header=None,
                     names=["timestamp", "throughput", "rtt", "loss"], usecols=[0, 1, 2, 3])
    df["time"] = range(len(df))
    
    # Throughput
    df.plot(x="time", y="throughput", title=f"{title} - Throughput")
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (Mbps)")
    plt.grid(True)
    plt.savefig(f"results/throughput_{title.lower().replace(' ', '_')}.png")
    plt.clf()

    # RTT
    df.plot(x="time", y="rtt", title=f"{title} - RTT")
    plt.xlabel("Time (s)")
    plt.ylabel("RTT (ms)")
    plt.grid(True)
    plt.savefig(f"results/rtt_{title.lower().replace(' ', '_')}.png")
    plt.clf()

    # Loss
    df.plot(x="time", y="loss", title=f"{title} - Loss")
    plt.xlabel("Time (s)")
    plt.ylabel("Loss Rate")
    plt.grid(True)
    plt.savefig(f"results/loss_{title.lower().replace(' ', '_')}.png")
    plt.clf()

parse_log("logs/bbr_low_latency.log", "BBR Low Latency")
