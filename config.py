#cav = [[-0.75, 0.0, 0, True]]
#cav = [[0.0, 0.75, 4.71238898038469, True]]
# 2 CAV 1 CIS settings, simulation
#cav = [[-0.75, 0.0, 0, True],
#       [0.0, 0.75, 4.71238898038469, True]]
# cis = [[-0.75, 0.75, -45, True]]
# 4 CAV 2 CIS settings, simulation
# cav = [[-0.75, 0.0, 270, True],
#        [0.0, 0.75, 0, True],
#        [-1.5, 0.0, 270, True],
#        [0.0, 1.5, 0, True]]
# cis = [[-0.75, 0.75, -45, True],
#        [0.75, -0.75, 135, True]]
# 2 CAV 1 CIS settings, real
# cav = [[-0.75, 0.0, 270, False],
#        [0.0, 0.75, 0, False]]
# cis = [[-0.75, 0.75, -45, False]]
# 4 CAV 2 CIS settings, real
# cav = [[-0.75, 0.0, 0, True],
#        [0.0, 0.75, 4.71238898038469, True],
#        [-1.5, 0.0, 0, True],
#        [0.0, 1.5, 4.71238898038469, True]]
# # cis = [[-0.75, 0.75, -45, False],
# #        [0.75, -0.75, 135, False]]
# rsu_ip = '127.0.0.1' #'127.0.0.1'
# interval = 0.125
# offset_interval = 0.0
# fallthrough_delay = 0.100
# init_time = 10.0 # Seconds to wait for the system to initialize before starting
# map = 0
# map_length = 1.0
# simulation = True
# debug = True
# unit_test = True
# unit_test_config = [[0,0,0],
#                     [0,0,1],
#                     [1,1,0],
#                     [1,1,1],
#                     [2,2,0],
#                     [2,2,1]]


# # Working 2 CAV Real
# cav = [[-0.75, 0.0, 0, False],
#        [-1.5, 0.0, 0, False]]
# #       [0.0, 0.75, 4.71238898038469, False]]
# cis = [[-0.75, 0.75, -45, False]]
# rsu_ip = '192.168.0.103' #'127.0.0.1'
# interval = 0.125
# offset_interval = 0.0
# fallthrough_delay = 0.100
# init_time = 10.0 # Seconds to wait for the system to initialize before starting
# map = 0
# map_length = 0.5
# simulation = False
# debug = True
# unit_test = False
# unit_test_config = None

# Working 2 CAV simulation
cav = [[-0.75, 0.0, 0, True],
        [-1.5, 0.0, 0, False]]
#       [0.0, 0.75, 4.71238898038469, True]]
cis = [[-0.75, 0.75, -45, True]]
rsu_ip = '127.0.0.1'
interval = 0.125
offset_interval = 0.0
fallthrough_delay = 0.100
init_time = 10.0 # Seconds to wait for the system to initialize before starting
map = 0
map_length = 0.5
simulation = True
debug = True
data_collect_mode = False
unit_test = False
unit_test_config = None