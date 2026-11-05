#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>

void analyze_packet(unsigned char *buffer, int size) {
    struct iphdr *iph = (struct iphdr *)buffer;
    if (iph->protocol != 6) return;

    unsigned short iph_len = iph->ihl * 4;
    struct tcphdr *tcph = (struct tcphdr *)(buffer + iph_len);

    struct in_addr src, dst;
    src.s_addr = iph->saddr;
    dst.s_addr = iph->daddr;

    printf("[RAW PACKET CAPTURED] %s:%d -> %s:%d | TTL: %d | Flags: ",
           inet_ntoa(src), ntohs(tcph->source),
           inet_ntoa(dst), ntohs(tcph->dest), iph->ttl);

    if (tcph->syn) printf("SYN ");
    if (tcph->ack) printf("ACK ");
    if (tcph->fin) printf("FIN ");
    if (tcph->rst) printf("RST ");
    printf("| Length: %d bytes\n", size);
}

int main() {
    int raw_sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (raw_sock < 0) {
        perror("Socket creation failed (Must run as root/sudo)");
        return 1;
    }

    printf("=== AKV Elite System: Raw Socket TCP Analyzer Active ===\n");
    unsigned char buffer[65536];

    for (int i = 0; i < 5; i++) {
        int data_size = recvfrom(raw_sock, buffer, 65536, 0, NULL, NULL);
        if (data_size > 0) analyze_packet(buffer, data_size);
    }

    close(raw_sock);
    return 0;
}
