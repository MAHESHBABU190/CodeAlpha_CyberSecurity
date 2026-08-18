from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {proto}")

print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=process_packet, timeout=15)