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

    # rusult: [('154.157.157.156', 1531), ('82.146.232.163', 1505), ('194.78.107.33', 1494), ('226.247.119.128', 1494), ('21.143.243.182', 1479)]
    
