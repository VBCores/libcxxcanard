# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/primitive/scalar/Integer64.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.019707 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer64
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
class Integer64_1_0:
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
    def __init__(self,
                 value: None | int | _np_.int64 = None) -> None:
        """
        uavcan.primitive.scalar.Integer64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int64 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int64 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -9223372036854775808 <= x <= 9223372036854775807:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-9223372036854775808, 9223372036854775807]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i64(max(min(self.value, 9223372036854775807), -9223372036854775808))
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.primitive.scalar.Integer64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Integer64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i64()
        self = Integer64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.primitive.scalar.Integer64.1.0'
        assert isinstance(self, Integer64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{?YWO=}cE5Z#z;HYR=$6TEmZ@gVUsMi8$C6+za-#fUd)x~I#XhMw-GKbBn~U=E6b28EQr!M|yBHp#|F<}%e&)vsQ?'
        'SMzn@_n-OB$&>H9i40O#EPz*Bt1nz=s90@VXM>7>`R0D~sgB9Rhlv9`#z%*EfLpoC3~wpFnfR#YrgC1jDyk7wq2`+V>Wzso1pn+Q'
        '<|Q@)ACxuNbaL<GX?%?Rxqjz69%5c$JVviXiV*M<UPbG?2y^$f0xf5BmYL*{vsgG@b^V+o=GA>QG$2no{yW(U6Dl$dW*8gn?+|p&'
        'Lu9R$fX#ZoJ2-<W*Q%G4+bt;?r}GWpV_s(=awEBy7lD2x(R6cn#C4+n3ryM?a|e^)dF{gVOiZT29$>T4tOjBu!Fi~81c^ua7W=Hm'
        'Aepm1G9_^@ud-m1uYnR8nB&wd_sUBvf%*D?d>jwT*JGM(?lJXlY%%VdQ&d=66TQ{s5sV{v!zsMylF+JV9)?MmzB6qD=EbSu1bsoz'
        '#i{9-@0{CSJ*l><Vgtsa${K5UAbK85EWV6X4S3XSHV;S)p$YimnQJrEs4!kWW4`f1#kVKteL9}{mgkvum^ZEh36oY>nu?h0LThO!'
        'A}!%N2cAdkXYMbux>2-Q&GUSFz@=1X_+L@;s$}<)rjaL?vxG1;`6q7mcYXyy>+hyO*k4M5#%+};i$wt+m!Maci=-~Mml=#5Hz$9{'
        'UJ^khQT+vq)ReQb0{{R'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
