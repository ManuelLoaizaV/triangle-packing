from enum import StrEnum


class GraphSubfamily(StrEnum):
    CONNECTED_CHAIN = "chain_"
    CATERPILLAR = "caterpillar_"
    DISTANCE_HEREDITARY = "distance_hereditary_"
    PTOLEMAIC = "ptolemaic_"
    INTERVAL = "interval_disconnected_"
    CONNECTED_INTERVAL = "interval_connected_"
    PERMUTATION = "perm"
    CONNECTED_PERMUTATION = "connected_perm"
    CONNECTED_PROPER_INTERVAL = "proper_"


class GraphFamily(StrEnum):
    CHAIN = "chain"
    CATERPILLAR = "caterpillar"
    DISTANCE_HEREDITARY = "distance_hereditary_graph"
    PTOLEMAIC = "Ptolemaic"
    INTERVAL = "interval"
    PERMUTATION = "permutation"
    PROPER_INTERVAL = "proper_interval"


class FileExtension(StrEnum):
    DAT = "dat"
    OUT = "out"
    TXT = "txt"
