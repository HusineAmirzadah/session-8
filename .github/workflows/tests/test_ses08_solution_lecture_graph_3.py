test = {
  'name': 'test_ses08_solution_lecture_graph_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> adj_list = lecture_graph()
          >>> [len(adj_list[n]) for n in 'abcde']
          [2, 2, 2, 1, 0]
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
