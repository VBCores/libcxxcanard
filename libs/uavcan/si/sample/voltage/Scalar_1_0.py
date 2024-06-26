# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/voltage/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.563438 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.voltage.Scalar
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
class Scalar_1_0:
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
                 volt:      None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.voltage.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param volt:      saturated float32 volt
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._volt:      float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.volt = volt if volt is not None else 0.0  # type: ignore

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
    def volt(self) -> float:
        """
        saturated float32 volt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._volt

    @volt.setter
    def volt(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._volt = x
        else:
            raise ValueError(f'volt: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.volt):
            if self.volt > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.volt < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.volt)
        else:
            _ser_.add_aligned_f32(self.volt)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.voltage.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "volt"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            volt=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.voltage.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'volt=%s' % self.volt,
        ])
        return f'uavcan.si.sample.voltage.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?Ya>u%k~5k8W2J@QSF?KpN~uhZ0)S|27+B1cV|Hi-h)>Bc8UY_~!$CYI#t>_Q}$-CZ8(1Srt_XkZltO290TN5~`O'
        '5dySm`!jumpihv0?hLs+I&y3Q(l^}8%<RnUH>*F-{JndkQ~wl~vr%NC*z*n7lEv~<7R221LzQI8NXx6@#9gcN(B_)o8)dwDRIPnh'
        '{i#|lX8n{UFn>8`!;qz(k)B~m2D^tUwrs$?yCI92u8IYJ$hDCwtwg7o|Fx4JRdkAWKCeEjiY1>}t7VW|ZmK_k?q_&4UR4#dHzkjw'
        'LvOl%#4PhIx+tcbK`~ogan4zpfIp)&6k4V7Qy$%e0b{}6O3aJJ))R3Ytc%lb`^vNY$h1tPl|%4j<$h}9Am!1AspSK%kH%=p52W>D'
        'o(`<2=q7j>GGqNjMd0O&#ko7JBHZR}!Q5?}!qEJs`lKq(_~2t2F&#}RI>-Y!+EOAztqc!U8db%NAE~g~{@-+`b5C%R=1IUcQ9EQ}'
        'l_6FzO9UHok}+d=M2t*BPK-)8VH!+mrbi@!&(so`!uoop^}49kje}C9<p8EvrN_PN^(qW737Fw)L>dzD9SJcZ8P`3QWw8vIg`9f?'
        ')r7g$sAs$dE#-!HAyFjYMDsu9kQ>;(qg8UK-Hg*$D<cUw#`Se#IIkCl3iO%`4l2_DjOw9;v(>K1+IkmG0nQCsoOATjDw6Uch6(=c'
        '#A>hcZ#=(oqX!`&dolt)dC0)Wx4T_JdSv~<#*L$qh2<<zxh3oCn;T@rnKswSo{*uyDYzA>9eLzEa^uZf=fqy{JBQlQWKZRB1ctx@'
        'A$gkekQ>9aj7N<NPzXd?Gxiq32HU_}%*X~<wL;|vSJmcWI?6!>VPFju^L+{NN-fke3AHrRc+Fw9VyFcf_O{;ZlhssNa`S^V0+o<L'
        'EH&5*nTDdsGmO_;BpAUZMT;35#fsHAhC~4sc(vpA+EkGQ-5<bWBUl_`hOyiRG4IvO8xuSHFi;7Hfu=_7I1f-1*DRI=#z5n23W*^Q'
        'MB`O(5l$8hTPnqCV#oJRtcXiax<WU_%i<N<!TThxHCJc;exLR~{!PCUYsJ;ya;=^;UDq4r4WqG}s=d^!iaEb_s48A+NrCTYP;f|Q'
        'M<`+8le#`x-1;LnibXhbh@%GPZ#o(8d52DY4xX7H4|uUM!GnG<Y6uoju_`WzH$*Q7LWwvSh3mwl>YzC3@5p@~`IsnQMpeI9_KnJQ'
        '$YCPpe#U?<ig|=s234_m2S|PY4vszodYXC_h(jo3@###$La0ZpRSZ7zeW)!wLvb<71GvDx=7T&&yN65*hnZ^#7W81us^Zd9N!EMa'
        'd(Fe3RTgP&#TU$gb4UZeyQtLxB;z0b=HjCTf)=o9fCrQYR={9m{levDaB=OP(!0I-W|#?^b?$1TP%%~<xoMz4#d*U8H5DA%fe#@E'
        '0`3|_S0zAnku!{S8z|5OEY-4ceHVwYM(Li(cqn(|M7=|!*ySE_au7p^uD11ZNa1j3`{Z|39DiThkLvHcd|b@MF<)g>L7t_=jFLb>'
        'ejuv1d7>OSehjygS)~tK(VQO&pn*#KzBqM<MaYrgTO=6H_VXCp_UOr3vGKQRm2Q?MfQFtm8Y;Sw2XM|rrr6#<VEZV{V~c}oL8WvG'
        '_jO7-?eG}lbV+C2_blR6N$1@7yc=I|xah{ah;t=fa_f&HE|l~H;!H_Ty7i|Jmr8ot%`YR)mh?HNX9e-OlAb|4UDC6NCrf$`@pws}'
        'N9>mLyxaeRvwOkWx#;w~=<L0Oc(J6H5HFPUGU5v*C5Y!sdIj<MlD>?1uB1OeJX_LN5YLqKhlndBz3TkBhPYhPRp;Lt;;EAU$octW'
        '#1kdG?)>e!^LozjR}mLW`kM3qb;S9SuDf%*;o|Y8J5Qb0V<o-e&h?gy@1{H7Pnx{bw;le};m;ht<M8JWf8p?5hqoMVI}{H09X@pU'
        'g~Kl$e&z6Mhu=8-*5P*z-d>n;!ueKMZH3KNxYY{Vtsq)qzZD*~!WXUZWh;Eu3SYOvH?8n(D}3jK9A0_Q8K9pa#k;Wp2_8DnqCI?f'
        't`!|@VB^;&JO~$WLQAzr-jLA22z0P@aqS@}PS^k*GdVsV-}&ouXY%Lq<HxR<)Rt!O6%IzkzoD~;cTv;7#IpFW_)jk0KM-4e@qzf|'
        's<<US6u%Nwd?ap*elcyJ3(PgocxVUiAzu}zny36x8W(pDP`$V>wi|-@op><jk#H<MnBbPP(5kU_rB5ZPVzJ>UXbbpXz*DvPVwX<A'
        '0b}Uv3H+vD_n&<j7)+290g~bd7j46$?ZZX8$XDMR#@u-S2Y{@II~5H800'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
