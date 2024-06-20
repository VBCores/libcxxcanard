# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/length/Vector3.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.492571 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.Vector3
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Vector3_1_0:
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter:     None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.length.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float32[3] meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float32 and meter.ndim == 1 and meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float32).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float32  # type: ignore
            assert self._meter.ndim == 1
            assert len(self._meter) == 3

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def meter(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float32  # type: ignore
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter) == 3, 'self.meter: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.length.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.length.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.length.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaTW{RP6<*2K-Lfsqb{yNW$7yOyt(QsU$Wha#jiW$yGV#XnB{g~pJ0wRt1CbndW+-U`1ZW-_SOtL)Fbnu6<R|10'
        '6bR6w$zz`T6!am_d2`R<4tH0MEWrK_=W=dy<~y^0J^YV<&bR8n;$qf|OcZ;*;aaj-e$0ZHdw!^rOc`l;Rm|VDIuC8G`MqAot4G!H'
        'r`0FbQZeDDEP?rpIol3d>KW-7mSnIy=4sao??WD1rLR@Rw7<=@kt(f3tC;%G$&V^JMq8g%pH{`3&#cul$SpV3pFsCByc(>kiir)$'
        '<7nv3tRFGUe2XrM@&2HgC@wkYtW3Cfx0i-Ot5kl>qkAx5EcjcADKXP{B94G{aolZRe3l=XmWi}-8~j+jpBmXsdGu~-d6(<`IhykW'
        'Y5jgaD!K+<hRj$$Q4x4~zBqlmQH0yPb(p(_Q<$2+Rd=f5qz^u(5!2DAqP;wT(B={uYGrt+(x@s9`;iK(2mc#yweAT{(mV;cCTf$6'
        'tTMz3W{F_ioMg-x9uXtckQ1X4PM8K0n&}=%;4`&Erm((VX}wug>c&B-(y|NFOVZ=s)p`{sm;}u5Wg-oU_@;!Mkc{g#%d%L8%)*&_'
        '1l5GO)~IK&1uf-<&%!~GfD_IClEc}+_D!vlp>{JkzFHYcz%j0`62p1DC{&==WDuxKyD+M^CB#;{B5Uij5Cu55&ElM+msXLKZ)2L^'
        'zs*?f^!*#muU>CMO303kz)v1B@bQh=Swh-m<)hW>`!fs6S)g)DR#w(lNslvau96)gLxEFpD^lC@$PIG+wOZ%MUhq4I+R<c3<#7at'
        'zycw8n(~kv!?cWheHWk*h_q(lEu;;$fwy=ft6<d%l^a}Dn}_Kr2Ni^YHBiiVCFCo$P{$<H(n#a=gISNE7G&67ztJH}sj_6_on-=*'
        'kU}ms*bAA4qR2DM*Xtzc!6ikD8SBN0)n^O`1ytbGj^AsJiX`ZM7Zw}A;uudD%dH#pcD=lBVv`ROm2ep7*Qgzw0~Ey-i)Dd1&^VjI'
        '!4OEI@hZ3oM~mromEtwAgL@|y#RVr_qHE$s@e*y}eG*stS7+*ehju>rU8fSu#pT~~t)4br*BhK0W@9T=JE>O{lYZ?`RlLxU0^iM`'
        ';E>GrQNr|{x;|Ol_#;+}83;MVQ3LZEPR4uQqGO+dXC}x4UM!CApda-51dCBDiL>IGXy-sE5eK7iop@C36-WI|xyvIT56YKO)hQNy'
        'qjDW`n25QbF`$cL3L%z3Rm|K5Qs2FeqmO`|#$E>E5DHm*Jd>~x>d|TygO7X{Y71j1&SiN37ueUlo5yH($g~j5WS?L`59X{YE*wa*'
        '-mBg#9wx1_NNbC}U<RB+8t~mkt@hwB{?+MUe6&E&0#*(1fYQJUm~5<HxZDgbuH8|3t6kp=Gh(woyV@vJj1~KC8Yob4-sggv3Wj#z'
        'L&&axy9U`+2@qZ63}f8}3N!&rHEdkp#cf!lblYS+l$&y--l0)!aSu5;h#^Inn|c{iI0S8<{;rB6Z%g}r{e71Yin%!CtE?)>vy_-#'
        '5-2zy$m%VgC`XPTz^!D^eTS`R(hmjDKqdZI9J|dT<j5Z_5)5ZMc^pF<czRZ>eqJrnwbBI8(6hdVicaSN#F@wx+ZzaM7lkQoaZoL&'
        'l#b!PR!PSl9zq;1>0$RhfjCyuNjE;_#-|<5xba!U$&${w^+yn=OFEBuxTHtj`eTT5B|Yxu7Z4{(dcx^hL_AT_lZeMldJ6GqNlzml'
        'Dd}^Fvn4&__CN3Jo^^K4IX&l{y%!MAmGlDQ*^*vFe7>Xv@k~iCAwE~q7ZFdF^e2d?O8OGw$&&sQaj~SAonKcF7fQP1{98smR??q2'
        'KYxxmU(&12-?od_bAG>!I8)MBod2&PPL*`U#c|E$<24sgeXfT}dfmnKy36mHi|-fxbEj`O{H4QRIegRMuO0rz;ad)GI(*<zINWvk'
        '(BWf;UpV~I;a3j7b@-jbANqJ}ddvxD8eyps)*9hvBRpsX(FnVZ@URgcH^LW<@MR->)d=4<!gr1EgA;Oi<w0kFeu5P5#sVaG=sYua'
        '`0iXTTG+sbug!DMc=c+{dhiz9K&tQa!wnqT|J0oKdCc*B=H9^Pi<u4R&vxG`Xom#a;flEO5WGxS7hXm=zD3{s`$B8<@5z%Vt~0^?'
        'o`F|u#zJX(6+I;GiwAu^_=EUpgf>px;TgB`VDcIFw{R;H-4QAwWu26m{#hjOFa4xysKSVUcLph&NI0}2NSF8;dZc&@4gN<gi0{QW'
        'xp;d|tarpa;<roUrg&GpC#ZN|+!CE)+(18@?EfGE!M&V|<L*bv{)Qy(?xFgFLkkDeXt<}~(Scn!J&<lOWyrSB;PCg%f!chrMaSy+'
        '*C75ijK2<B{FfUXeGH?Ihof6awLcoh9C`l-aAy%}&<y|p'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)