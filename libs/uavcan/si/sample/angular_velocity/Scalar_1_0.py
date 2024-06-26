# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/angular_velocity/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.571889 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_velocity.Scalar
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
                 timestamp:         None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 radian_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.angular_velocity.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:         uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second: saturated float32 radian_per_second
        """
        self._timestamp:         uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.radian_per_second = radian_per_second if radian_per_second is not None else 0.0  # type: ignore

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
    def radian_per_second(self) -> float:
        """
        saturated float32 radian_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second

    @radian_per_second.setter
    def radian_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second = x
        else:
            raise ValueError(f'radian_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.radian_per_second):
            if self.radian_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.angular_velocity.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            radian_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.angular_velocity.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second=%s' % self.radian_per_second,
        ])
        return f'uavcan.si.sample.angular_velocity.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZEqdL6~1=j_q-V=AtVqclqT10?g9n}mzEYVN<)WSBAm2VU$UCr9p4#wcV{~@Yx^QqDj$mCYNf7}t;A2@C-4)H'
        'S`|Lhe}MW6_?DitJA3bSNG#dU*?BqV%$akZGyd!Gf3BYF)IY_G*)TFu?D>Xk$zu5l3u5m1p-M7kq~%p{a?9#Gw7KSYhZ(OPR;!;@'
        'f2q2~jGwXu=DRuD3t8$J=^2(}u$!fWJZ9S8<FN{*9eP_KgYT-ChaqjGN-NPR=6>tshZUWoozJRIt76G#)@m8#mYeENVB{(8jaF5~'
        '%uUJTXzbRaA2G{(i@u8KW>Cx&SDcqtCfwT^rlHU(m7nnFE({n8j#pw%EVQ186JTAOaobm(=0~PwBCXs5KUVIgMh;RQeUMr{;QDB='
        'mi$0kKj!Jcii&Q4mmxFOPgDe6K3|-_(<;Jk-X_f5#wiTV->Q$R;;auorV-Q8q@u$-fTJxXGStfOP^D2-9QPv?R@?uZ?sV=7PSQLH'
        'xF%|cOsq1*3TBC5dz@s<7#<NL(~uLR5>A)~6PoEEN#HZJM5eI5UTM8WRO-e-snT))(_QIt?|Quo155&D_$rZxM0`g=Oi0Fck7Zdb'
        'LuTR5J%Vb&Tx--b+JcsH!x!PANWh8af6n1<VEc|%$ymD?U0<z?B;Xj=*NNf0UKA?OYce>fOb0Nk_avOHc170K7vU7(+#ZW_j$T?t'
        'Qoe^_f<HU4+Hd?D&9C3+K}g8HjKEJGGVt-O#YIATWbOX?jiZr;<t$LSC2MON>tx88HrL6%kfFdSD325hg1k#^yix0%*b9E=kUN^}'
        't2~at5Lh52Pg5RpW0;oluyFwrfk<mc-a^=58+eO1vJO_QP`SZXwRxD1a!^4SSOdlUKtjAy3wcaJEsZo@bC}H-azTc@&3F5xn<`6g'
        'zQ0N!6H<t!274jXkQ8}_@p_X4Lnu<Tn6Y83SbfKEQNRga?fBjHsz`$F4`8toEROMpG2I3+@72p26FYnysD#5nlcRQY50DhsET#p<'
        'K;vu*7egS3#;c$ZP8IW;D#bFfqq-9-;<A&j&<*jDc$s#vp2W4Lbms2$Y5$|&^((PjT>U-Q>T%O`zQMg=G<H+9pL$g>>(>rd#S1Md'
        '@PiBz4$15YCCq<Z=O>F>f5dvR07njS)WG~rCu5y==+tN6nF;cM7b_Dy=m*1wY4H?YaZ$W3dN~kE#K9<(6OXFH;*`H54|wF`MfozS'
        '`o*$uRIWn~6EXKQ26R!(A;dDMiiJDC?gw{p^dZpG)GI(7LLr?`XA%}dK3c6}@R1)tZs8e<OIaR30sERGy@TB`)52k98-fKr7_+Ll'
        '{6v!VUh`h{Fld!UT3hi2GvFN3fbR;mI)uykSHCHIv_Q}TW)1Lw(!dHBY|LLMZU%*G_m$r5)s<l;Y}R*I8-<Lq;z*@|0u|>C7t~ZR'
        'wgVqR4g}O1L{}w1bdfWRc^fFu1T59Eab1ghutw>g$#^Jt<V3zhquAvha&izuh_1HzGNy1iw0-=$Do(s7?T7XE79S;Zam-g)RgkAC'
        'F~cNKa6b^$+dNT@96y4pWLD{ME1LB~0W?sFKNhF&un0Nw2a5#5*?t~F+a5kXE7t!}b?HWF0%+)2qoJbnc>w23WQy$#1a^SJ9JV;f'
        '7F0^7a9^jS(+-azPM7q!`<_9ZD(S2npL65$4j0_`BI0aGm)!aji1Q^qiFmxEr`-C}h)X3s<K~wUXG;2v)3bv3Oi9loo+;@$#8V|b'
        'k9eY_&mu0C^n%;}oU?n;*}3HOJn!tifOx5-mk}?P^hLzyN=gtfl=KSXvn72A@q9^tgm|u`FC(5U>5matN_y4#bq#U3q+RFVD&pyq'
        '{>1tDQ^b=cz3%+&x$}C??^h5PO8Tnv|24$9lCHUPyzb)hhC5Gvug6My!=39*7vBwczMnPsPTz9)bBDih__o7eI{cNxcO2ewxb09l'
        'JaG8H;pYy&aQLOeuN;2s@H>a!H+Xw~$_W=*q1y@@t#GRqwp&58!a*xMXob&P;fq%IvK78+g>PHoyH@z#2|2v-pff-}L5g={0TMiP'
        'o&`I8cdiy4Y+$3;COiliZbD17N8XUo!3cD)HF50$C{EY_9y2*UAK(7_a%b}A(W6JMnbek+HH#!meW+sJJrc#L_!`=bcn8(~M=Xo~'
        'if?l9-l5p+i}%H^yW*DkK>S8f@u9da`o*+?mN45q?yKU=<Inr5INdz(kCMCCIz&6-p4e_^;}7Egh+V>wbbo?z&Ormmj+Q==x{8H{'
        'xu99#{{~Og=8IiA1;>t|+b8gwg57`jVPG&pT?D9$8(g#vi?+v$c9F$?FpM|m{U5qxz<M+d000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
