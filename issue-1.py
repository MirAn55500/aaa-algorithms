import pandas as pd
import numpy as np

names = pd.read_csv('simple_english_wiki_pages.csv')
links = pd.read_csv('simple_english_wiki_pagelinks.csv')

df = links.groupby('pl_from').apply(lambda x: x['pl_to'].to_list())
df = df.apply(lambda x: np.array(x).astype(np.int64))
df.head(3)

graph = {i: j for i, j in zip(df.index, df.values)}

visited = set()
start = int(names.page_id[names.page_title == 'Analytics'].to_list()[0])
end = int(names.page_id[names.page_title == 'Algorithm'].to_list()[0])
print(start, end)
queue = [[start]]
found_path = None

while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        neighbors = graph.get(node, [])
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

            if neighbor == end:
                found_path = new_path
                break

        visited.add(node)

    if found_path:
        break

if found_path:
    print(found_path)
    print(len(found_path) - 1)
    print(names.page_title[names.page_id == found_path[-2]].to_list()[0])
else:
    print('No way!')
