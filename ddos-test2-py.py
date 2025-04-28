import socket
import random
import time
import threading

def send_udp_packets(target_ip, target_port, duration, packet_size, delay):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = random._urandom(packet_size)
    end_time = time.time() + duration
    sent_packets = 0

    while time.time() < end_time:
        try:
            sock.sendto(message, (target_ip, target_port))
            sent_packets += 1
            time.sleep(delay)  # Paket gönderimi arasında kısa bir süre bekle
        except Exception as e:
            print(f"Error sending packet: {e}")
            break

    print(f"Thread finished: Sent {sent_packets} packets to {target_ip}:{target_port}")

def main():
    print("=== UDP Load Tester ===")

    target_ip = input("Enter target IP address: ").strip()
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("Invalid IP address format.")
        return

    try:
        target_port = int(input("Enter target port: ").strip())
        if not (1 <= target_port <= 65535):
            raise ValueError
    except ValueError:
        print("Port must be a number between 1 and 65535.")
        return

    try:
        packet_size = int(input("Enter packet size in bytes (e.g., 1024): ").strip())
        duration = int(input("Enter duration in seconds: ").strip())
        thread_count = int(input("Enter number of threads: ").strip())
        delay = float(input("Enter delay between packets in seconds (e.g., 0.01): ").strip())  # Paketler arası gecikme
    except ValueError:
        print("Packet size, duration, and thread count must be integers.")
        return

    print(f"\nStarting UDP load test to {target_ip}:{target_port}")
    print(f"Duration: {duration}s | Packet size: {packet_size} bytes | Threads: {thread_count} | Delay: {delay}s\n")

    threads = []

    for _ in range(thread_count):
        t = threading.Thread(target=send_udp_packets, args=(target_ip, target_port, duration, packet_size, delay))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\nLoad test complete.")

if __name__ == "__main__":
    main()
