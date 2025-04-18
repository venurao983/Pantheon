# Pantheon Congestion Control Experiments

Welcome to the repository for running and analyzing congestion-control experiments using the Pantheon framework and Mahimahi network emulator.

This project is created to evaluate the performance of three congestion control algorithms—**BBR**, **Cubic**, and **Copa**—under different network conditions.

---

## 📦 Project Structure

```
Pantheon/
├── analysis/                
│   └── analyze_logs.py
│
├── logs/                    
│   └── copa_low_latency.log
│   └── bbr_low_latency.log
│   └── cubic_high_latency.log
│
├── scripts/               
│   └── run_copa_low_latency.sh
│   └── run_cubic_high_latency.sh
│   └── run_bbr_low_latency.sh
│
├── traces/                  
│   └── 50mbps.trace
│   └── 1mbps.trace
│
├── parse_logs.py            
├── setup_test.sh            
├── setup_guide/             
```

---

## ⚙️ Setup Instructions

Before running the experiments, please ensure the following:

### 1. 📥 Install Dependencies

- OS: Ubuntu 22.04 or any Linux distro
- Install Pantheon:
  ```bash
  git clone https://github.com/StanfordSNR/pantheon.git
  cd pantheon
  ./setup.py install
  ```
- Install Mahimahi:
  ```bash
  sudo apt install mahimahi
  ```

### 2. ✅ Test Installation

You can verify that Pantheon is installed correctly using:
```bash
bash setup_test.sh
```

---

## 🚀 Running Experiments

Use the bash scripts in the `scripts/` folder to simulate each CC algorithm:

```bash
bash scripts/run_bbr_low_latency.sh
bash scripts/run_cubic_high_latency.sh
bash scripts/run_copa_low_latency.sh
```

These scripts simulate different network conditions and generate logs in the `pantheon/experiments/` directory.

Copy the logs to the `logs/` folder and rename them as:
- `bbr_low_latency.log`
- `cubic_high_latency.log`
- `copa_low_latency.log`

---

## 📊 Analyzing Results

Run the following Python script to generate all required performance graphs:

```bash
python3 analysis/analyze_logs.py
```

It will generate:
- Throughput vs Time
- RTT vs Time
- Loss vs Time
- RTT vs Throughput scatter plot

All outputs will be saved in the `results/` folder.

---



