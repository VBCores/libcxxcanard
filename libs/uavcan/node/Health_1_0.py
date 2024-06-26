# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/Health.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.244031 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Health
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Health_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    NOMINAL:  int = 0
    ADVISORY: int = 1
    CAUTION:  int = 2
    WARNING:  int = 3

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.node.Health.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint2 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint2 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 3:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 3]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 3), 0), 2)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.node.Health.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Health_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(2)
        self = Health_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Health.1.0'
        assert isinstance(self, Health_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Health.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{@j&ZEssO6i&Of%`(_DI!yuu^Tdl<joz#+>_a~hIu%0Nv}(KYA|cE7+BY`%+E=!3(jXzR4@|0L38b3ez~AIJFKt>V'
        'XqBQmv3<_-Jm;Lpzux@wgL-ZB=O30sYN<@HWkwJwekQ483C?s;YAYNI{>>w2s?1e}9S=(u&cf=;@Jm?n3s{i?_TQ>VKO-tpnzH08'
        'Mx^7x*Kwa2E3^u{=9gYf)@PwJ*Qvb<FN430iE~Dzm18#i0O76ya(*iKg&n~py#Ua_lsJN2M0MTu(uhJh(T5Yu&y^KD#b{eO)??-}'
        'o7*@Q4ojwb0KYR2!82kVE`U_v_x*!|X`py5*@nHnxCM-AzlFo#?_=wTqQubIK&Ms87yLq>$O;hL#8hX&*8=={$Je*Dig(;O2)@i8'
        'Ojd7q=J`APeg1G9VX3>n*Y37<1ApY79CL<7^-)YYBrM7+l{wH?s2(bfE}4--w4!t&6p^b*@QZkY;Jv9z?4&fz#-d!(sD4OdAR?!j'
        '_+x)7H)Isv!v4-=JtE$jdj-^O3J^d1KL+*Ivls27{lo7fg}+)TGmtVP5|zY28#!jsAkxtld~#%n>M^7Za+k<5mFWt~XBb5U0Y5mA'
        '6Ct5F;Usa0YG#qr4s>9BxY3CBZI#-gb*w<S(FFp1a&3yJ7E!~PO*o4TbncoH1v{71CP1Gj6CL;_^zLgAUfOOwKW^`LBj5h<f3YAx'
        '&ai+UiY1-FC=?u`tY-*?^RXeLE})YYaXCg$*|@injI|{H3V;5!;D6IP?6$jKM)==fhHtAppJ2~n03|SxQ_ZIMD;4JtIXz`ELMec>'
        'iY%tbuR^?W0g?IT8H>Q_aBMdbD&qI}D*uRY@u&P5|D1RE*A)yfWl;2tI7Y*%zk_pe!YD4aaahpM_4lyVmB|=vNQO%iZE7k0lOhfN'
        ')&bbv$wB<}4D4X83FFFj^tbs^z`;x_XS9S7U?)(yI3oVtvPz}MuwlJQ#=IAX1hcX@_C<&joiX^kV{c5>lP5_W!r-EBEMrbApfR9q'
        '^sc_hSUBa6z7=z|S}V0K4&03Rd=vzfjG~U}oS=3-8k3l2Dz`;NC7mdt2615fFl;awE8q@&=$e^b#oR!fpU@<=UHzmHD>X?2{^Tl)'
        'EZ3E!Fe15RfMzsP;~hOt4I!*sn;ooi(r81M6RakU9WA9E*sTUa+_}<jHJgLMAdzH{WZEbuWx{CH%yQFoAa-;8)8@uzvc9>oapgu%'
        'NYc~&Cb()<fH=D%HN*^?1*3vATeL5%HbcBEOa}Ea&DJ*F_-qttZ9OSz4w%MG`!srUDxqi}PYv?I#Gxwg>i6K^_(Hhd(f1>E?%@6g'
        ')@AVMx*&E~q#8N~%D%@64UbezzYn?*r_IG<w1_h<;Hl%Kzk5I^1x5dHh*xp9TS;Ixyt>OD{~lI4^MBYBUgB~bA$00h3Ou1cu#5|G'
        '5*JJHkpq1q{ziNlh#EcCU2sj9!{l!hy1a-k2mk;'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
