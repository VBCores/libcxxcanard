# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/primitive/scalar/Integer32.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.016515 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer32
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
class Integer32_1_0:
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
                 value: None | int | _np_.int32 = None) -> None:
        """
        uavcan.primitive.scalar.Integer32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int32 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int32 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -2147483648 <= x <= 2147483647:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-2147483648, 2147483647]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i32(max(min(self.value, 2147483647), -2147483648))
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.primitive.scalar.Integer32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Integer32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i32()
        self = Integer32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.primitive.scalar.Integer32.1.0'
        assert isinstance(self, Integer32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{?YWO=}cE5Z#z;5)(g&30^$7@gVUsM*RVTiXdy^V#J#?-P7exLr-_pAIq)~FbBmzgF?#R;NP@*H_66G<}%e&)vsQ?'
        'SMzo0_n*bi^vU<#L<XrV7Qid6)fX-_RIIkGvq43`eDfgsRLA7u!^8oe;G-iv#GTw_hPRa8PJC2zQ#r3%71ao;P;<?F^~OXPf`9fD'
        '^C}yG56T*BI(g;eX?%kHg?{Hd9${W*JVviXiV*M<UPbG?2y^$f0xjos)|ljxvsgG@b^V+o=8Xe2G$2no{yW(^6Dl$dW*8gn_XxV?'
        'A+pv=z-BAo9h||GYt>82?UfXb)A@$)F>kRDxslw<i$Fh;Xu7#O;yO|PB_?f+xr0gYym?`ICMGjs53%Vr8-dtJa2{$NLE>?~#XhSs'
        'Nan1MOiA3&8!Xu5YoLS%<~a4rE9Iq?z<hl`K8^?F>j}-a@R)ixwitKKDJrb3iQa1R2*we-;S}C;NoZ9w55uHO-?_E{^YYAag1(^V'
        '^2~J1cg}6Eo>aS4u>oUIWs@~L5Iqkj7GFlH20U)In+GI@&;<PO%(b~{R2VOxG2eKh;@j!@fR3lW<wa&4=H68xVbTgqQxTIrXf5qT'
        'q$Pak!1HMR-2G)%H;Oi^d7f_%xRlBa|0`-<mF#}fH1gzfmJntp|HPes?^h7C{%!_@{naFB+*X;gSQPMa30BH-k<{h(8iTRpX8MQh'
        'ClN#v)n9r7HZrmU000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
