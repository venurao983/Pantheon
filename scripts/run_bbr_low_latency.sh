cd pantheon
./run.py --schemes bbr \
         --uplink-trace ../traces/50mbps.trace \
         --downlink-trace ../traces/50mbps.trace \
         --runtime 60 \
         --extra-mm-args "--latency 10"
