#!/bin/bash

# ==========================================
# Ephemeral Port Exhaustion Monitor
# Using netstat
# ==========================================

THRESHOLD=80

echo "========================================="
echo "EPHEMERAL PORT UTILIZATION REPORT"
echo "Host : $(hostname)"
echo "Date : $(date)"
echo "========================================="

# Get ephemeral port range
read LOW HIGH < /proc/sys/net/ipv4/ip_local_port_range

TOTAL_PORTS=$((HIGH - LOW + 1))

echo
echo "[ Port Range ]"
echo "Ephemeral Port Range : $LOW - $HIGH"
echo "Total Available Ports: $TOTAL_PORTS"

# Count used ephemeral ports
USED_PORTS=$(netstat -tan 2>/dev/null | awk -v low=$LOW -v high=$HIGH '
NR > 2 {
    split($4,a,":")
    port=a[length(a)]

    if (port ~ /^[0-9]+$/ && port >= low && port <= high)
        count++
}
END {
    print count+0
}')

# Count TIME_WAIT sockets
TIME_WAIT=$(netstat -tan 2>/dev/null | grep TIME_WAIT | wc -l)

# Usage %
USAGE=$((USED_PORTS * 100 / TOTAL_PORTS))

echo
echo "[ Current Usage ]"
echo "Used Ephemeral Ports : $USED_PORTS"
echo "TIME_WAIT Sockets    : $TIME_WAIT"
echo "Usage Percentage     : ${USAGE}%"

echo
echo "[ Status ]"

if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "WARNING: Ephemeral port utilization above ${THRESHOLD}%"
else
    echo "OK: Usage within safe limits"
fi

echo
echo "[ Top Connection States ]"

netstat -tan 2>/dev/null | \
awk 'NR>2 {print $6}' | \
sort | uniq -c | sort -rn

echo
echo "[ Top Remote Connections ]"

netstat -tan 2>/dev/null | \
awk 'NR>2 {print $5}' | \
cut -d: -f1 | \
sort | uniq -c | sort -rn | head

echo
echo "========================================="