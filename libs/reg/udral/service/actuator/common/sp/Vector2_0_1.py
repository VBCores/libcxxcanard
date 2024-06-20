# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector2.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.440446 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector2
# Version:       0.1
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
class Vector2_0_1:
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
                 value: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.service.actuator.common.sp.Vector2.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[2] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(2, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 2:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 2:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 2')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 2

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[2] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 2:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 2:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 2')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 2

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 2, 'self.value: saturated float16[2]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector2.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector2_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 2)
        assert len(_f0_) == 2, 'saturated float16[2]'
        self = Vector2_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector2.0.1'
        assert isinstance(self, Vector2_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector2.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8fDd$L0{?wfU2hyU6y2oxYSYjyf$+dX_koXq(DXw>Dgq(3r4e+x>9V1z1O(SJzS-;6;~9B8(JoRY`cTwJmZ%i-|M(|xJu_*t'
        'CEJx&<FT*Lz4zR6=8uKH?=5xepSw~_L@89nN-&Zu`8!V(L@dp-A}^%{@7BHpB{N!zpC$$PBmdcR|IBZ?B__27<FVt`cC4vVTN#)R'
        'S!9}L1o4G|QB(=TRYYkHWC{_daBg!GQKl@{QCUR0kkZBt?^f6Wm{R6CU@z~s>mwg`;<-QlbMICex7Ns{vQYXxKdXt?LEbHHNl@aX'
        'vI|Ub%b5-3x({buH-=BVdv8mQLEHyDvUn?OP4~FQKtTrDwqP@ADNNu{9#F*jEtPXSjk3xTX_=~%__#~;rM$E(%LRD6;x-1y*Tc2w'
        '4xRPGQQ+i-A5xL5v|I~r#A%?Hgp=`+mbMZh@xCG2iOZ5W-fGu`(f{Y)K<v<0i91h;3!X|l@$tM{V2PsOPmX&!!KU`?oA2ITye)0R'
        ')DFG2-MMotFTCr`0x2h1k}H{dx88>=C&ofu4+=0rAg2YFqNE|>SMJ>*6kz4qar5jc)sEj%+@<YGDQ+fj1`*Z)R~7ib{AS#JRVLK='
        '0?VZKaW5?RI4qU}|CQo&A)X77omV9>3gd$7T9VsU60YI}x7fhZU6E5G9io!E^;0rs$)qvEGmit@C~4vX3Ii!8WBEh(4%-hhV?}N('
        'lfrMi%dE^RlL8$mU<Idny5;atGND-x$e!at*gc}2=dMz2%!AqH3rT@#uC2)x4I0K4jOHrnyh?~?MsB38DDR00XvpVin~YN1lmJ?z'
        '62P%liM7V8l%u49c3Z<n*P`oD7_GNKit7w{N%flGiDQ&Q{1JzE1HY{4$D8<dGpuGx11^NrqyLSPPQRhALD3xhc!jvW7xyrx|9yga'
        '@Ol8aiWjkqm-jqwaNKE0#)pTvyN!?V=S}<tf5kog4H-U0jtQnH5O5zyp=f+k7f2HiY-#KJovz!U2{m6n!w|TjM{RNP<N8Aqz(|Am'
        'L0cGsnKCneMCE;qpT={+n)vxkDsV>U@88LFP=G#D^1+Nj@x&y3<u>td1Mz*3Vvj^S1@*y@>k+)o7fbAEt?Yg$nBz3qO6>rmwu3Qs'
        '9=MHHTEW*OL)jAF@11cPE=T_XqVYT>RR#b6'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
