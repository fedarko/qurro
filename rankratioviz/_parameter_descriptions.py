# ----------------------------------------------------------------------------
# Copyright (c) 2018--, rankratioviz development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# ----------------------------------------------------------------------------

TABLE = (
    "A BIOM table describing the abundances of the ranked features in "
    "samples."
)

EXTREME_FEATURE_COUNT = (
    "If specified, rankratioviz will only use this many "
    '"extreme" features from either end of all of the rankings. '
    "This is useful when dealing with huge datasets (e.g. with "
    "BIOM tables exceeding 1 million entries), for which "
    "running rankratioviz normally might take a long amount of "
    "time or crash due to memory limits."
)