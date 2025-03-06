test = {
  'name': 'test_ses08_solution_dijkstra_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> graph = gs.Digraph(lecture_graph())
          >>> dists, prev_nodes = dijkstra(graph, 'a')
          >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
          [None, 'd', 'b', 'a']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses08 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
