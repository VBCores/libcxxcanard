# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/length/WideScalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.498807 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.WideScalar
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
class WideScalar_1_0:
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
                 meter:     None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.si.sample.length.WideScalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float64 meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.meter = meter if meter is not None else 0.0  # type: ignore

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
    def meter(self) -> float:
        """
        saturated float64 meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._meter = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.meter)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.si.sample.length.WideScalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> WideScalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_f64()
        self = WideScalar_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.si.sample.length.WideScalar.1.0'
        assert isinstance(self, WideScalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % self.meter,
        ])
        return f'uavcan.si.sample.length.WideScalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 15

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{_KVZI2wq5#Brd-u=qi#@Jxm4zceN?*Ip9E+iy|L&l`>VsUn`Ab8X>)3@Eandzas=WZ7%Qv4yv7mdV7o=E%zegZ!M'
        '2?Y5_{sH0__*+sn)3bYL?9W;0?y2pUs_N>hr+WW>@L%^1cj`~^d^U_s6nnnmTC!Mv#)6o8eyEa68EJV{9Nw@x4{fgbtzpKi2i5Yu'
        '>TlIjG3BQ$f%ywL+YVXk8R;38WUxEtY2OO(LmBanki|?_#jL;0wUH{VM5mbfi<2Kzbb@w1ukKaFg3qkgGRQ4A)hD3-3670cRmIdb'
        '$>V73(7Ycp%Y2JoipgeBOcm#ye^w^k+Zd*y&?=Rm@#q!|7z-{}Vn)oho`^$WT^w`U7oX%urez|n+y*}uZ>L7~Qy#sWTHfb+f0!2h'
        'Kw7^ENk!Md%a9rCCn^FjpDj+^Y!%@)Zyn}t;1q`DAJqp{al!{5(}?M4ucF;NfTJxWGStfOP^D2-9P}d<R(F1$>~wAkPSQLHxF%|o'
        '>{(@q70eRBwmHd|F+3thrXeRrC7dt~CN$GSlEBy05}CsKdZqQ|QK=gTrAo^_OfN}~dzb4~7+?}G!<UIPB;uPAVnQ;myDZCM88QoZ'
        '?h#ZI=31kk(H69n8$J&gMFLJV|1^iYf$f`GC1dSobbYlll7M4eUnYk0dQqrAugTz`GVQ~t-j;B-+7($_pNCU`bK5M=IeKXoN%=O0'
        '3I1)yYNzpUG{1VK3n3vpkjmg!$iT<f=jRFOl9juwSN2C1ma{<RmaMF-t&$;U+FT|(LWTmTpfFN9^vIj!%B!``J$u3L9CAmK9hJus'
        '7y=7~<Y~%7ZVb~h9yTsOA`ofK$Xf^-Yy)rcMpnV96)HElsx}YPQ4T5y18bm|4<y7ZwUEao)Y3@fHHTS`As1xWU4OGjmQrQOwYQfE'
        'WI_tD)L<`U8j>Q<FkY{bU<gHu7Be=C6|3(UE(+Mds~x}9UKL5u{XQ%<g2gf3Fs55S=G}UEV`7t!1C?+XXmZq!?g5hGlEt*Z7-*bL'
        ';bI5`(RdXU!jWQjU8Ptic2sv_QJizqdAcSph!<!F>q%T{N@wPFkM`dGuvdxY;^IeKt4B@O`3Cof(b!7WPU=;~v|l?^70<P#zy}#5'
        '9Fo~SN|^ni&QBJ%{)p9L4vrk+sDb%wPR2U#(238%GZW+iFBbRkpdSnyj>S_fi8JCA(anKSA`V8OoOo327DxO|IpC3x7v;;S>J`U*'
        'qjDW`n25QbF`$cL1|gO~Rm|N4ULV}V(FZ_J6E6aB2!%vGnMqg(`DnF@!ACxT+`=;yXR|zj0`@iU=P}wHGc6oux*=H5gE6a$bB`ri'
        '?`7{L4}(@&q_ss~FaypZ4fw85t6jK^Z+lJQqXmK%Fl&GZlm=G7U}OG5aWg1fyQB10x2_Dc$7X$ZwNc0zEA~|yC{S_Ua6wH4V>|Fg'
        '$i9GDgXpRRh%R!5F>eC}nt-KRHm+-N8`db@H5m`(rreY7&?vUJhnyV55Tc81zKkgx4s9R(UKNMllJ>p&`vxB+b8)~|SyhlHDKWz&'
        'P;fsG)f+rfjvU{Is$^E_aVwhkLjg2UiN6*{Z?XtE@)wH)!`WUQL)#ucIxAMcsFvtjX#!~IS)-w%vv~mLOk|4f4FonoVFp_qWD6>#'
        '6S%Ka(n*I05GPA|(0!jmoG9tE8=rCGvkvFn_&nltNf+GuLx{5_J&bs;q(|KPqlgP7J?7?*BTkj{DW_)<@u`xYKs;8`lZZ!3dJ6GS'
        'NuNfXFX?Hw{~2fZjI(pr>3P=Kdk*nzNzWmkDe3cw&y<uPo-XNm#HUMo0r6Bxe}#Cmq%R<zDCw^e7fX84`E?2LcuAL>f6ItROZpq<'
        '=Wh`Ym-Mppx9iU9Ilo^-oGa-|&i|JYXG*%_&hd(i$E)r<^}QY_=@oab*Iazp-1&aj+&g{U;qM*(!QmSY|LE{f4zD`A?(mL7;c(#a'
        'zQZpae&z6Mhu=8-(cw=HA2xVncESm#TVbgc)>`3uE8J-X(F%iBxZet2w!&Af@O3ME(+WSf!cVR6&<Q!b@}M(7KS7FjV*wI8be=go'
        'es?Yx9c*Bu*Csp&=dM9Zwfo+X(7~=k2U`)B?t|il_2Ds-<MZ*2f8Oi-zdjHDTYp^hs!ukRaOfCtD)9rfGI14M|6Uvy{}KPr#ap{#'
        'y(iul?<|Sy;$87)LB)IGhUgWO2HMVa^V0zY_rNU{$3GwTw+^wfix$Lfai<}rkHy^)cZDPA?jAln3C{!Um+51Pv6yRk5n2)c@_4K^'
        'Uu@9{IAjcOi3I*qu=`yP2Ksx5@hT7_H@Ij3iw5IGTgZ{W7{+|?{s-=>-~)^e000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
