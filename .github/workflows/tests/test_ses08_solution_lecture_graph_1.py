test = {
  'name': 'test_ses08_solution_lecture_graph_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> adj_list = lecture_graph()
          >>> 'd' in adj_list['e']
          False
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
