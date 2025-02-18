# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/primitive/scalar/Natural32.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.029125 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Natural32
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
class Natural32_1_0:
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
                 value: None | int | _np_.uint32 = None) -> None:
        """
        uavcan.primitive.scalar.Natural32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint32 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint32 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 4294967295]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u32(max(min(self.value, 4294967295), 0))
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.primitive.scalar.Natural32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Natural32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u32()
        self = Natural32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.primitive.scalar.Natural32.1.0'
        assert isinstance(self, Natural32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Natural32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{?YWO=}cE5Z#z;5)(g&30^$7@gVUse*FMJMUXY?V$_>7-P7exLr-_pAIq)~FbBmzgF?z5;lH#xn`C1obD8R?s@JdH'
        'tNFV0`_E$M_{n$OR0gRl7Qid6)fX-_RIIkGvq43`e0?waRLA7u{nP;-;e!L*$DQ0|hPRa8PJCQ*Q#r3%71bE3P;<?FHQ?05_0uPq'
        'SJ@bRP}X46$txdE;v?)Y^gG}20P{NIF?uCZgn*y$GFoRvn7gkOXgQ~|#w3rN#lrEj_A`o@H$Rx5Mh4_-6JZ4Y-`UogP?2dcqu5}-'
        'N8mLNk+oI=He31j@D!-DRWB&FTT(Po=NrDmyv0J~MshFD1N}&%>E`a3>qHEen6x$K4kp3#=DGQqn9ii#$EMe81Y#q>d8l~=iHG?H'
        '`>ZA)nX^7JC2^29Sg^_0KnV@Zak?w7l$TZl^VK0aIT@C(M>N~QL%O@M#kwm_QDJRO^j4EgFp1y|r|^zTLaUm27$sfqovRx#FV8F|'
        '=yQrL&uqth>&*D-arLMwMqn(eY_f(2qUXWH;>=jpfQQX?bC1Ljnt<=0`ZiaM3gg8y=4;PYd~<x>qvMHhd68L%xpx^zn6|>wRK#Q#'
        'T1#6IX${{x@H|>ScYm4HjiTLZp5>cEE~PS~|B9NIB|Au(MxI{G62i>npSaWS{R)D905=1|{%R65ZmUdLEDHFf1S@5^Nb1tP#$e*O'
        'IsQimNd%EZ^%sb>f>N{t000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
