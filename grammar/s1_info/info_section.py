from gram_utils import sep_rule

from pipelines import INFO_HEADER
from basic_rules import TEXT, FEATURE_LIST

from facts import NonTerm


INFO_SECTION = sep_rule(
    INFO_HEADER.interpretation(NonTerm.name), 
    TEXT.interpretation(NonTerm.successors).repeatable(), 
    FEATURE_LIST
).interpretation(NonTerm)


if __name__ == "__main__":
    from parse import parse

    parse('', INFO_SECTION, True)