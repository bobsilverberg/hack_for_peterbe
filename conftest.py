def pytest_addoption(parser):
    parser.addoption(
        '--minutes',
        action='store',
        default='10',
        type='int',
        help='Number of minutes to stay on the page')
