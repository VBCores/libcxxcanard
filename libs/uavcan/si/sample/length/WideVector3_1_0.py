# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/length/WideVector3.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.504662 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.WideVector3
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
class WideVector3_1_0:
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
                 meter:     None | _NDArray_[_np_.float64] | list[float] = None) -> None:
        """
        uavcan.si.sample.length.WideVector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float64[3] meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     _NDArray_[_np_.float64]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float64)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float64 and meter.ndim == 1 and meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float64).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float64  # type: ignore
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
    def meter(self) -> _NDArray_[_np_.float64]:
        """
        saturated float64[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _NDArray_[_np_.float64] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float64 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float64).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float64  # type: ignore
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter) == 3, 'self.meter: saturated float64[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 248 <= (_ser_.current_bit_length - _base_offset_) <= 248, \
            'Bad serialization of uavcan.si.sample.length.WideVector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> WideVector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float64, 3)
        assert len(_f1_) == 3, 'saturated float64[3]'
        self = WideVector3_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 248 <= (_des_.consumed_bit_length - _base_offset_) <= 248, \
            'Bad deserialization of uavcan.si.sample.length.WideVector3.1.0'
        assert isinstance(self, WideVector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.length.WideVector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 31

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{_KVOK%*<5nfW_TcRG6WLc8smhDJnq8;0mDKk!#NT$KaX=^R$VGDV9&@<EAZg6IL(%nOH4H$?HF~nei44?_%pWvV1'
        'V~z$A*g5)~laWKtyd_n$J-bVpI%fg$tL;Zsbyf9Oy?;FX*BkS#`cu4|^&%6+o^QC8ES8_LAm*MQsw7iJT3!`L?^~URHrM<?FXPqI'
        'YUy$HS+!V9_$f<Z{?(jqg)H@q^bAWf*d6n<YlZi*jQB@9v`SyAifMm~Ya>-!iB>W7k&~ZRbd0t>uO3&$oX@P)GRQ4A)$c+7b37ZY'
        's)~tq$>V6~(X1aa%Y2J&it+xSm?$ne2dzxFcfXg0LaS7M%A*G`U@Z7ti77GDcp{E~b#dHnUwED$nU;yPatr)ec$ga5O?mWwYI&FI'
        '{c)P}18Mz!Oe(qxUWUwAKT#2Qd7(ISw^4-Kyfv7+gHsrqKUMdt;*<|QrV-Q8sG{9GfTPVNGStfOP^D2-9QGp>R*(KY-fBG%oTPaY'
        'a81+(8ChkB70eRBwm8X{F+3thrXeRrC7dt~CN$GMlEBy05}CsKdZqPdQK=gTrAo^#OfO20dspjK7+?}G!<UFOB;p$qVnQ;m+bqjs'
        '88Qnw_Xw&9bFER&U<+Ex4WETXk$@A;|Byp&VEcwv$xyo)q_0*+5^#*`tHf|#FA5dtH5nXKrd=4-TN2JzyCQ4rvv3M<Zi~e^M=z}+'
        'Dc`~{!M}}IZTI~f%&%N;LrBOr)H3)LGVt-8*;zu`Wcibo>-!@M%UPguOO}^cS4fXDZLX4SAwz*va5GZd^T;i7{jFN($X@U}huYC('
        'Tjg;ChQI<Ld7AQ&8^g4Wdwmz65Qwy9;4Op=wt=^pkrl9Ng~|=Cs?Ec6l!FSwz#1s#I}+lRTBu_ZYH6hL`iEJIp%!G=Uc1#Hi>b0?'
        '{k<gum5@R#HP{Q8hN8$bjMv*F=)omLiy7<1iq$!WL;)Rmwc`((RFMST@4{juSR7-9vD~^bZ`aHFCN}smPzi^DevR5e9-t_$SS$;S'
        'fyUVs5<?(}#;f2W%oo#ZD#dGJ2lq}ah>K3TL|4Tt;x*dB`y{UPug=uN4()vSai<bX#pT~{t)4Yq*Bj&wqp_K)?bNG^NxyceDqd<x'
        'f$wBca7bqRC}H|uU7sv&{1Gd~3>-PcQ3LbqPR4uQqGO+fXC}x4UM!68pda-5B#Wn56z9Y>(awQTA`V93I`OF5E$00Vxx*tL6XnaO'
        '>J%q@qjDW`n25QbF`$cL3L%z3Rm|K4V&A!oqfddJ#$E^F5DJ-mJd>~x>d|TygO7X%Y75U$oX_$AF0ik8H;>WokZIvClYN2(Js7j9'
        'xOgDRdT)Afco?+GBCRd>f*EiQX~1_Ewc3Sb{Jqn^_-KKk1*{t20i}TzFxXhXaJd;=T)VCGX1l%_X2fQlyV@vJj1~KC8Yob4-sggv'
        '3Wj#zi;!IbcMYPe5+J(B8OFK|6lemLYS_5Gi(9Zp>9)yuC^zIty+fne<Q{Tz5JQMAH}x{4a5%Jm_Ip(vc~{yG>hJgYpqPt8zRIeC'
        'JWq+~C4qwcKveJWL^*Q&5N;)d?mKKnlYS_G1}gEp;@DjlAxHjTkzhF6$>SK>z_YVr<uBDDT`f%j4L$2?sOWSaz&R6{VtWID?VvD)'
        'Ee@&$mC`ZX*DC3_!$XMUB|YrEPauw!bkdDax$$X-Gj4nqak8XyZv7F&>5?8rJY3RwxBeL7TuG0+`4fl}B|Yi%EFhjN=_$nHB|VKe'
        'U(z#(M@sqv;%rIJy8SOYyXTyp^G?qNXYVD%^Ci8Ac&?-`BfeNtf_S#1mk?hl=_`n5O8P3|>5{&Nc&em7LR={6W#`uw#1kc5bp9<N'
        '9xLgOou5BJJX+GL&fm5>ujl-J9dV|lZ#e(oM4T$=vOC8$7mv5xdFs3#D(Q81uD4x$SKax3+Rr<E$KlT${@mdWhre+6ONTcd-gfxN'
        'p>Vk4@QK4O9DeEWD~De@{LbO`4)^+aXL`&DXB%O$5mp=Fb|XA$1kngPjqs!qzG#Fm8{w-)__`6kYlQC`Vb2LUyz-zkKtDl>cVht('
        'JanEJJA8L86)kLF!`J5d=e&BgW<7Wdt|Qg=`Qa80?SE<>^?A(kedgZ47mAs6=+AcFDrko{p&c%ZD^I}7gmvL%l;d0U#-AUz{$HQH'
        '|JEPZ34u>$;FX-QP}*Ka4~d83QJ;T)D?S;asgw73#;rV<?8f~~+{#3Egt~5)brNFwH<7?!`dQUblM(;u3{o_aaA<vy9`P;oWN{M>'
        'ej`qZ|A>F);@w@b))DWCUoDE;;(hUJLB$8+j_4HQ2Kwh@|3?rA?xkLw8u=l#zX^)_yJ+Iz<Anoh^vI{-p@W@2J&@utY{>A?RPi^|'
        'f!chrNyq9KtU?S{F$VR~#lN`0(LEU58;))wz5ies<K+Dhzr0YMNDcr1'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)