from block import *
from interactable import *

level1_blocks = [
    "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
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
    "W - - - - - - - - - - - Ḷ - - - - - - - - - - - - - - - - R - - - - - - - - - - - - - - T T T T T T T - - - - W W W - - - - - W",
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

level1_interactables = [
    "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
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
    "W - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 4 - - - - 5 - - - - - - - - - - - - - - - - - - - - W",
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

level2_blocks = [
    "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
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

level2_interactables = [
    "W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W",
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

all_levels = [[level1_blocks, level1_interactables], [level2_blocks, level2_interactables]]
blocks = []
interactables = []


def build_level(self, index):
    self.blocks = []
    self.interactables = []
    x = 0
    y = 0
    for row in all_levels[index][0]:
        for char in row:
            if char == "W":
                blocks.append(Block(0, x, y))
            elif char == "T":
                blocks.append(Block(0, x, y, height=.5))
            elif char == "B":
                blocks.append(Block(0, x, y + .5, height=.5))

            elif char == "R":
                blocks.append(Block(1, x, y))
            elif char == "L":
                blocks.append(Block(2, x, y))
            elif char == "Ṙ":
                blocks.append(Block(1, x, y))
                blocks.append(Block(3, x + 1.001, y + .01, height=.0001, width=.0001))
            elif char == "Ḷ":
                blocks.append(Block(2, x, y))
                blocks.append(Block(3, x, y + .01, height=.0001, width=.0001))

            elif char == "b":
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "a":
                blocks.append(Block(0, x, y, width=.5))
                blocks.append(Block(2, x + .5, y))
            elif char == "c":
                blocks.append(Block(0, x, y + .7, height=.3))
                blocks.append(Block(1, x, y))

            # Position Flow F
            # Position Current C

            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0

    x = 0
    y = 0
    for row in all_levels[index][1]:
        for char in row:
            if char == "w":
                interactables.append(Fluid(0, x, y))
            elif char == "e":
                interactables.append(Fluid(1, x, y))
            elif char == "a":
                interactables.append(Fluid(2, x, y))

            elif char == "1":
                interactables.append(Button(1, x, y))
            elif char == "2":
                interactables.append(Door(1, x + .25, y, height=2.5, target_height=2.5))
            elif char == "3":
                interactables.append(Door(1, x + .25, y - .5, height=2.5, target_height=-2.5))
            elif char == "4":
                interactables.append(Button(2, x, y))
            elif char == "5":
                interactables.append(Door(2, x, y + .5, height=.5, width=2.5, target_height=-2))
            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0


def update(dt):
    # Knöpfe und Türen updaten
    for inter in interactables:
        if inter.__class__ == Button or inter.__class__ == Door:
            inter.update(dt)


def render(self, window):

    # Alle Interactables rendern
    for inter in interactables:
        pygame.draw.rect(window, inter.color, (inter.rect.x, inter.rect.y, inter.rect.width, inter.rect.height))

    # Alle Blöcke des Levels rendern
    for block in self.blocks:

        # Rechteckige Blöcke
        if block.typ == 0:  # Wand
            pygame.draw.rect(window, block.color, (block.rect.x, block.rect.y, block.rect.width, block.rect.height))

        # Rampen in Form von Polygonen anhand des Rechtecks
        elif block.typ == 1:  # RampeR
            pygame.draw.polygon(window, block.color, (
                (block.rect.x, block.rect.y + block.rect.height - 1),
                (block.rect.x + block.rect.width - 1, block.rect.y),
                (block.rect.x + block.rect.width - 1, block.rect.y + block.rect.height - 1)))

        elif block.typ == 2:  # RampeL
            pygame.draw.polygon(window, block.color, (
                (block.rect.x + block.rect.width - 1, block.rect.y + block.rect.height - 1),
                (block.rect.x, block.rect.y),
                (block.rect.x, block.rect.y + block.rect.height - 1)))
