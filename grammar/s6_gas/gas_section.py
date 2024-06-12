from yargy import or_
from gram_utils import sep_rule

from pipelines import GAS_HEADER
from single_gas import SINGLE_GAS
from gas_mix import GAS_MIX


GAS_SECTION = sep_rule(
    GAS_HEADER, or_(SINGLE_GAS, GAS_MIX)
)