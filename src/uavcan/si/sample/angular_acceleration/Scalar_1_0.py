# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/angular_acceleration/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.587326 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_acceleration.Scalar
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
                 timestamp:                    None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 radian_per_second_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.angular_acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second_per_second: saturated float32 radian_per_second_per_second
        """
        self._timestamp:                    uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second_per_second: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.radian_per_second_per_second = radian_per_second_per_second if radian_per_second_per_second is not None else 0.0  # type: ignore

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
    def radian_per_second_per_second(self) -> float:
        """
        saturated float32 radian_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second_per_second

    @radian_per_second_per_second.setter
    def radian_per_second_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second_per_second = x
        else:
            raise ValueError(f'radian_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.radian_per_second_per_second):
            if self.radian_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.angular_acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second_per_second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            radian_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.angular_acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second_per_second=%s' % self.radian_per_second_per_second,
        ])
        return f'uavcan.si.sample.angular_acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZEqdL6~1=j_q-V=AtWJ8C{66vcL9TgOQ8jf($FE72q&%8m#k)Y$9G2F-Pz8}+P+AY%7>!3T8WjimG}w#1bzZi'
        'E9gi14^V#r-_mn-XYaiZi6#3vJ1^&)Idjf)#(z8h&$mu?>Yw6;Y!I0!_I$&&WU>5&1u^&hP$ii%((<Y}xn*@8+FbLygN#=XtCdfy'
        'zgEk|l%KK$=2vsJ7qZkd(lac{U^h$qdCauW!jQ*YGb>f<ZG{ZRs$$mP<J!PTB|62-@0|Rwq7$_9S@mgEEcnb?ErZ;0Q~enXJ;lZ0'
        's;Zc}DR~@?T$}eJW|?o%UoqJXimBqN^VG_Ods~Av6k4V76CT}#0b{}WO3aA4))R38tcx>l`_j|=$h1tPm3!dF(!JEke#)Z{Qp@{X'
        '9}U=oA4u!RJndUi(GBo2WXAf5ionau#rZp}BHZR}!rX0~!qEJ^`nW32`ru<4F&&L7I?Mw&+Cm~jtqc!U8db${KT=_}{lCdh=dR!+'
        '&69v@qISsGDnqPbmI$`TNyd!f5iv3iIWa2XglRCLnI4b?K2u9%3hV2Y)|*GAZXA><E&DLNEIsb6)~hhUBw&WG5NSxncO=AwWL$Sy'
        'mc=q`GJ>F*FxMLO47Z@A-0*q0C=zg@`CoFl8`!?1RWj0UhSygsBMCUh^(rx(*NZ|0dQAogm1!SF^`3;Y)vn0e`aGNhoZDk@&e2P&'
        'NXqvxOz>wXR{M>A!};|aT?h%;ml62MLk2#+IX_QGm#p1izi~9Ou$%=dw`6T?W1S2*(`J?I3mFQWf)YvXz$5RH8?V<o$M%BXIpmHe'
        '`zntkFa#C|$<vgF+!&^1JZM~iL?F_dp|=n=*aqI>jjV%JD^zZ9Rc#)oqa0Ka2G&3^Kadcw)IuJUP)j3?*BoXuhFp+gck|sISx%KD'
        'H{V|&kO?WoQiHvaX-JAZ!+5<xf&mmMTFlrWR;<2bxG3NSuXg-ydsQSs_xrHe2o}e9!<cUUn0M>tjfovT3RJ>jpvh4?yaz~%>lV`j'
        'W1w+1g^M8&MB`OZ2&anKO_gGq*kRp?C2_?`SLud$QM^PuSWn`5Q#v#EdbIb^?|YS4DX#s2YxTJ4I^W>lFdDn5+E2ZznD%Rjs^a;U'
        '6!<{~35R5Mgc4>yuJe<{tv_PDn1dsSIBH=2rjxPGJ9OeR@XQ2xz>B3Z9`u7j!?t*eWpPowCb~HgO2ok^loOAt!{U^`BM*4w<3;&0'
        's(QtuZ&a>B4iho=GX``~%pk-vsEWBe!0-omaP%S2)5Oa_96}+bPi7JpLOxopV(^h4KyKj~ic47@Kmq%jBgKQ=5!1q9rW=9<Js7j9'
        'xbj4j^<MQ}@i1tWMOs_(1vB6r(tz&@wK{~$_*btfe6&E&0%i^HfYQJU7;Ma6C~gLYYxkAj?belH#%$JiR~v<lvEoRjfdUoh4Hwi@'
        'FtP(5LiPpJ8bntmKy;BajCmU<&;%^ivT<FDd$307uE}^PcjQ>UL!;Q`9&&OJLx`@m`7)w#IJABIyDCn+C+&yz_ZA-}b8*a9Syhmy'
        'DKUd2P;fsG)!RH#jvPPAun8+YYDLq2D1Zhk@u%YS9Tp)+{%Db4INQr(XxoFwXT|#G)iT{EO#lr&Ycy1JHV@#OiA=G*fxr$>n86kY'
        '*@8;x1n%pUbkgB5#L1E#ci&Tp6D6H?<1=o2*5RBRpGTZ7>4IB-0&%vaClQaA^psnF8gZedXWaZE;#5hWae9^zpDF2C#4{y5hj^-_'
        '=Mhho^jXCDl3sB8pL2FEIy;w~p3BbO^N5#9dIj-fNnb#GuA~I<LP@V8K3mck5zm+OCy3`t`V!*VlKvENsifDOU)K>AOS<g*TR}Ws'
        '(w{j$e~x&vq^r)~t~;;i{C*j6uB5Lx|6fI%De0O!$7?Pgue<Zq_j;_PH{7}2aPi%6=lex-@AOTFzjXMP!?zv&%HgjazT@zg!)=Gc'
        ';eo>k4!>~trNgfre(mr(hu=H=p~2g;6Hd6$3d^mq(F(U(VY?MXD;%`KgI4&W6~1hRuUg^jR`{+JzHfyeoRGsS4>|+%6Qp=I79hbx'
        '=b5vkcjrpc!3H*bZNh_a?k2QUd*lrX9gIK+TNBqGfZ~Mp;W3lr^YQI}EOy3!9zA;Gnn`WxvSyKFsSj1`H}p3qf^qRJbR6*xTKGmR'
        'ivNoL<l?<UvDp*vi{C7ZTjB%pTS3K#;<o4&lLorObo17SSLu^p`&DtedG8<Pda-qgw!}TL-LS|X#r+}KghT267y+GwevS<;eIk<;'
        'a}AL}@4$Z*o~X?iyL1Ag5JU4%;5P-k|L(y+e~ifpFc~+vXd4!7j~4ABsr_geFVOox$-LZ5M-2b~'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
