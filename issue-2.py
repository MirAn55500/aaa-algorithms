import pandas as pd
import numpy as np

names = pd.read_csv('simple_english_wiki_pages.csv')
links = pd.read_csv('simple_english_wiki_pagelinks.csv')

df = links.groupby('pl_from').apply(lambda x: x['pl_to'].to_list())
df = df.apply(lambda x: np.array(x).astype(np.int64))
df.head(3)

graph = {i: j for i, j in zip(df.index, df.values)}


def get_length(id):
    return names.page_title[names.page_id == id].to_list()[0]


start = int(names.page_id[names.page_title == 'Analytics'].to_list()[0])
end = int(names.page_id[names.page_title == 'Algorithm'].to_list()[0])
distances = {node: '' for node in graph}
min_len = np.inf
found_path = None

for _ in range(2):
    visited = set()
    queue = [[start]]
    while visited != set(graph.keys()):
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if len(distances[node]) > min_len:
                    break
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor not in distances:
                    continue
                elif len(distances[neighbor]) == 0:
                    add_len = get_length(neighbor)
                    distances[neighbor] = distances[node] + add_len
                else:
                    old = distances[neighbor]
                    new = distances[node] + get_length(neighbor)
                    distances[neighbor] = min(old, new, key=lambda x: len(x))

                if neighbor == end:
                    if len(distances[end]) < min_len:
                        print(new_path, len(distances[end]))
                        min_len = len(distances[end])
                        found_path = new_path
                    break

            visited.add(node)

if found_path:
    print(found_path)
    print(len(distances[end]))
    print(names.page_title[names.page_id == found_path[-2]].to_list()[0])
else:
    print('No way!')
