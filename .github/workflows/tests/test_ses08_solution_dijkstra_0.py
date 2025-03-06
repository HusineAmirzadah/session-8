test = {
  'name': 'test_ses08_solution_dijkstra_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> graph = gs.Digraph(lecture_graph())
          >>> dists, prev_nodes = dijkstra(graph, 'a')
          >>> [dists['b'], dists['e'], dists['c'], dists['d']]
          [1, 7, 3, 5]
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
