
# Pantheon test to verify the installation

cd pantheon
./run.py --schemes cubic,bbr \
         --uplink-trace mahimahi/traces/50mbps.trace \
         --downlink-trace mahimahi/traces/50mbps.trace \
         --runtime 60
