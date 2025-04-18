# Run Cubic over high-latency, low-bandwidth network

cd pantheon
./run.py --schemes cubic \
         --uplink-trace ../traces/1mbps.trace \
         --downlink-trace ../traces/1mbps.trace \
         --runtime 60 \
         --extra-mm-args "--latency 200"
