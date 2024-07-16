# network-traceroute

This project contains a script to visualize network topology using IP addresses and their corresponding Autonomous System (AS) numbers. The script uses the Graphviz library for visualization and the IPInfo API to fetch AS information for given IP addresses.

## Requirements
```sh
pip install requests graphviz
```
mac
```sh
brew install graphviz
```

## Usate
```sh
traceroute csgate.princeton.edu
```

```sh
python network_topology.py
```

## Notes
Ensure you have internet access to fetch AS information using the IPInfo API.
The IP addresses in the ips list should be replaced with actual IP addresses obtained from a traceroute or other network diagnostic tool.
