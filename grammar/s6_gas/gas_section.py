from yargy import or_

from ..gram_utils import sep_rule
from ..pipelines import GAS_HEADER
from .single_gas import SINGLE_GAS
from .gas_mix import GAS_MIX

from ..facts import NonTerm


GAS_SECTION = sep_rule(
    GAS_HEADER.interpretation(NonTerm.name), 
    or_(SINGLE_GAS, GAS_MIX).interpretation(NonTerm.successors)
).interpretation(NonTerm)