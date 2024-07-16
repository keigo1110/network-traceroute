from graphviz import Digraph
import requests

# IPアドレスからAS番号を取得する関数
def ip_to_as(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('org', 'AS info not found')

# トレースルートから得られたIPアドレスのリスト
ips = [
    'XXX.XXX.XX.X',
]

# IPアドレスに対応するAS番号の辞書を作成
as_numbers = {ip: ip_to_as(ip) for ip in ips}

# ネットワークトポロジーの描画
dot = Digraph(comment='Network Topology')
dot.node('PC', 'Your PC')

prev_as = 'PC'
for ip, asn in as_numbers.items():
    as_node = f'AS{asn.split()[0]}'  # AS番号だけを抽出
    dot.node(as_node, as_node)
    dot.edge(prev_as, as_node)
    dot.node(ip, ip)
    dot.edge(as_node, ip)
    prev_as = as_node

# 結果を表示
dot.render('network_topology.gv', view=True)
