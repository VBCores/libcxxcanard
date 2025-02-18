# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector6.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.454533 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector6
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
class Vector6_0_1:
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
        reg.udral.service.actuator.common.sp.Vector6.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[6] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 6')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 6

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 6')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 6, 'self.value: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector6.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector6_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f0_) == 6, 'saturated float16[6]'
        self = Vector6_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector6.0.1'
        assert isinstance(self, Vector6_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector6.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8fDd$L0{?wfZEqYk5Wb{&Ytz7$K={Ci-UnVng_aiy1Og#JA%bo%JuWmzh2VJClN(d7z4CgaJEThV1E`TKQ7PvC@lRm9duehd'
        '$4RI4dS;%Pd1jvdZRxK&E1l-&Z<Z5L36-!4tmI1m$}<HC%S}<5N;(LB<10|IpriPHQbITlZ$A!?!nR*wQfsgQJAPx&**bT%g;|$n'
        'rg=dS?^qZmwXj?zl;&9GkZ^M6&e()96-Fmjne0PO7as+`#*V>O(&&i2x<5UihP0C|{1F}pzs|UGR%W$>DjbA)O+0f7etAcN66cj&'
        'V}d)*TrAhWHYeO#J_-Ki9XSSZ7xc*C7x8Mg#|;Jw3eau}Hm8=-Mh@jMd0gF5hPzpmb(TrTRFfp6U8*nVm1Bhw5b&no8k~j4u;ez`'
        '`q30Q`8^D&NLD$n1-IfN&=bNb_()4vi<tPx679rgMI7%;&xFzc`=3bcFw~j9N{LIJOE(GWieF-xBIh^HdOF9Z_T2OD!C(JUx|XRu'
        'dYyLXuP{>v-<t<gO^VDYnFqhwhr$qJv95b1*tj4U7cNIhL&Q(~OG7BZ$;<r~*+Z%wKPSHzcWb4%ojmVESjSw|5dI9?Y4>TBQRhpn'
        'kUFG?@xaINup0TV6{mo7A$oS6R>UZbORk%h+^w@1ir4&d3rDfSP$M0plKagIYs#`oD~3k_2e?(y#08WVa!$euC;kO?6xWQE#yTcN'
        '*!4G9WonxP85FRR(>(oZd?=aGEC(dd@gUxwQqK$TQf@R+Y>TBN$J}UVjiN!r*n!nt#XYYx;+c^esVmBRE&>|z6}l#&G%_WCsZa^v'
        'Osd3MD^|);(LlRX!6xq|?<aAz!NpbFWXLP3*G5g8p`74%IK&U|!-jtR7(Z=?)lO-^g^+smpHY(aGx{2otvRG?#Pyx@5L5c!C7659'
        '27v2$9lLnrAmA3qy(!6f{{;7U@dtdcjX&Z~cz{16!$ahlVU7X;k8l)=#$TEOY2uMB?LxoP^;<Nd_RD7(0vGgXBu;wVyiW@-(jdOo'
        '4n|;S#Eh?}J$wV-N*AIu@zxV6a8Bp1+%`IHfWCC)qZs4H6O;6n+s3b3h;QO5_GoEmpk5tvJ%az!#R_}aY<9o1ND&vo)*1y6wH-{U'
        '^T=(wHeL9JWT>LGN7mjY))<`p3m1>3*i{Aq00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
