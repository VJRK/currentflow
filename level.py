from barriers import Barrier
from interactables import *

level1_barriers =         ["W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - C - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - W W W W W W W W W W W W W W W W W W W W W W W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W W W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - R W W W W W W W W W W W W W - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - W W W W W a b b b b c W W - - - - W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - B - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - F - - - - - - - - - - - - - - - B W W - - - - - - - - - - - - W",
                           "W - - - - - - - - Ṙ Ṙ Ṙ - - - - - - - - - - Ḷ - - - - - - - R W W W W W a b b b b c W W a b c W W W W - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - L - - - - - - - - - - - - - - - - R - - - - - - - - - - - - - - T T T T T T T - - - - W W W - - - - - W",
                           "W - - - - - - - - - - - - L - - - - - - - - Ḷ - - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - L - - - - - W W W - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - L - - - - - - - - - - R - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - W",
                           "W - - - - - - - - Ṙ - - - - - - - - - - - - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - Ṙ Ṙ Ṙ - - - - R W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - Ḷ - - - - - Ṙ - - - - - - - - - - - - - R W - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - W",
                           "W - - T L - - - - W W W - - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - T L - - - - - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - T L - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - - - - W",
                           "W - - - - - W W W - - - W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - W W - W W W - - W W W - - - W W W - - - - W W W - - - - - W W W W W W W - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W"]

level1_interactables =    ["W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - C - - - - - - 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - W W W W W W W W W W W W W W W W W W W W W W W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 2 - 3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W W W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 4 - - - - 5 - - - 6 - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - R W W W W W W W W W W W W W - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - W W W W W a a a a a a W W - - - - W - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - B - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - F - - - - - - - - - - - - - - - B W W - - - - - - - - - - - - W",
                           "W - - - - - - - - Ṙ Ṙ Ṙ - - - - - - - - - - Ḷ - - - - - - - R W W W W W w w w w w w W W e e e W W W W - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - L - - - - - - - - - - - - - - C - R - - - - - - - - - - - - - - T T T T T T T - - - - W W W - - - - - W",
                           "W - - - - - - - - - - - - L - - - - - - - - Ḷ - - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - L - - - - - W W W - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - L - - - - - - - - - - R - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - W",
                           "W - - - - - - - - Ṙ - - - - - - - - - - - - - - - R - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - Ṙ Ṙ Ṙ - - - - R W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - Ḷ - - - - - Ṙ - - - - - - - - - - - - - R W - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - W",
                           "W - - T L - - - - W W W W - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - T L - - - - - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - T L - - - - - - - R W W W - - - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - - - - W",
                           "W - - - - - W W W - - - W W W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W W W - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - W W - W W W - - W W W - - - W W W - - - - W W W - - - - - W W W W W W W - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W"]

level2_barriers =         ["W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - F - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - C - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W"]

level2_interactables =    ["W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - F - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - C - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - W",
                           "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W"]

all_levels = [[level1_barriers, level1_interactables], [level2_barriers, level2_interactables]]


def assemble_level(index):
    Barrier.instances = []
    Barrier.ramps = []
    Fluid.instances = []
    Door.instances = []
    Button.instances = []
    x = 0
    y = 0
    for row in all_levels[index][0]:
        for char in row:
            if char == "W":
                Barrier("Wall", x, y)
            elif char == "T":
                Barrier("Wall", x, y, height=.5)
            elif char == "B":
                Barrier("Wall", x, y+.5, height=.5)

            elif char == "R":
                Barrier("RampR", x, y)
            elif char == "L":
                Barrier("RampL", x, y)
            elif char == "Ṙ":
                Barrier("RampR", x, y)
                Barrier("Point", x+1.001, y+.01, height=.0001, width=.0001)
            elif char == "Ḷ":
                Barrier("RampL", x, y)
                Barrier("Point", x, y+.01, height=.0001, width=.0001)

            elif char == "b":
                Barrier("Wall", x, y+.7, height=.3)
            elif char == "a":
                Barrier("Wall", x, y, width=.5)
                Barrier("RampL", x+.5, y)
            elif char == "c":
                Barrier("Wall", x, y+.7, height=.3)
                Barrier("RampR", x, y)

            # F
            # C
            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0

    x = 0
    y = 0
    for row in all_levels[index][1]:
        for char in row:
            if char == "e":
                Fluid("electricity", x, y)
            elif char == "w":
                Fluid("water", x, y)
            elif char == "a":
                Fluid("acid", x, y)

            elif char == "1":
                Button(1, x, y)
            elif char == "2":
                Door(1, x+.25, y, height=2, target_height=3)
            elif char == "3":
                Door(1, x+.25, y, height=2, target_height=-3)
            elif char == "4":
                Button(2, x, y)
            elif char == "5":
                Door(2, x, y+.5, height=.5, width=2.5, target_height=-2)
            elif char == "6":
                Button(2, x, y)
            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0


def render(window):
    Barrier.render(window)
