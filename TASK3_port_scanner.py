import socket

def port_scanner(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except:
            print(f"[ERROR] Port {port}")

if __name__ == "__main__":
    target_ip = input("Enter target IP (e.g., 127.0.0.1): ")
    ports = [21, 22, 23, 80, 443]
    port_scanner(target_ip, ports)
