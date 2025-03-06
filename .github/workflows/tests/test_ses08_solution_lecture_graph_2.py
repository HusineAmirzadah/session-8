test = {
  'name': 'test_ses08_solution_lecture_graph_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> adj_list = lecture_graph()
          >>> [adj_list[n][m] for n in 'abcde' for m in 'abcde' if m in adj_list[n]]
          [1, 5, 2, 5, 2, 6, 2]
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
