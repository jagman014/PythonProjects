# graphlib expects the graph to be a dictionary type
from graphlib import TopologicalSorter

# nodes need to be sets, else it will iterate over the string
dependencies = {
    'realpython-reader':{
        'feedparser',
        'html2text'
    },
    'feedparser':{
        'sgmllib3k'
    },
}

sorter = TopologicalSorter(dependencies)

print(list(sorter.static_order()))
