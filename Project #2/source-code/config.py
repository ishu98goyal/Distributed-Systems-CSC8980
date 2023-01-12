NUM_NODE = 7
INIT_PORT = 3000
NODE_PORT = [(INIT_PORT + i) for i in xrange(NUM_NODE)]
RECV_BUFFER = 4096
REQUEST_SETS = [{1: None, 2: None, 3: None}, {1: None, 4: None, 5: None}, {1: None, 6: None, 7: None}, {2: None, 4: None, 6: None}, {2: None, 5: None, 7: None}, {3: None, 4: None, 7: None}, {3: None, 5: None, 6: None}]
