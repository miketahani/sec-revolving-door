# extract data from the POGO HTML-formatted database, create a force-graph structure for use with d3
from BeautifulSoup import BeautifulSoup as bs
import json

with open('pogo_database.html') as infile:
    raw_html = infile.read()

soup = bs(raw_html)
hdr = ["full_name", "fmr_office", "fmr_title", "new_employer", "resign_date", "statement_date"]
nodes, links = [], set()
flat_nodes = []
for row in soup.find("tbody").findAll("tr"):
    fields = [field.text for field in row.findAll("td")]
    entry = dict(zip(hdr, fields))
    full_name = entry["full_name"]
    new_employer = entry["new_employer"].replace("&amp;", "&")
    new_nodes = [
        {
            "name": full_name, 
            "type": "employee"
        },
        {
            "name": new_employer, 
            "type": "employer"
        }
    ]
    for node in new_nodes:
        if node not in nodes: 
            nodes.append(node)
            flat_nodes.append(node["name"])
    link = sorted([full_name, new_employer])
    links.add( tuple(link) )

graph = {"nodes": nodes, "links": []}
finished = []
for node in nodes:
    connections = [link for link in links if node["name"] in link]
    for connection in connections:
        src, target = connection
        if connection in finished: continue
        finished.append(connection)
        link = {
            "source": flat_nodes.index(src),
            "target": flat_nodes.index(target)
        }
        graph["links"].append(link)

with open("graph.json", "w") as outfile:
    outfile.write(json.dumps(graph))
