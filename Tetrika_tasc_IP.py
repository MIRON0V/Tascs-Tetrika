# Файл состоит из строк вида: <host>\t<ip>\t<page>\n, где host — корневой домен, ip — IP-адрес, page — «хвост» ссылки.
# Необходимо вывести 5 IP-адресов, которые встречаются в файле чаще других.

from collections import Counter

pullIP = []

with open('C:/Users/russi/Downloads/pull_ip .txt', 'r') as inf:
    for line in inf:
        line = line.strip().split("\t")[1]
        #print(typeline)
        pullIP.append(line)

    def most_common(list):
        data = Counter(list)
        return data.most_common(5)
    
    print(most_common(pullIP))
