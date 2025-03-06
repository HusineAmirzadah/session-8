test = {
  'name': 'test_ses08_solution_lecture_graph_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> adj_list = lecture_graph()
          >>> adj_list['d']['e']
          2
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
