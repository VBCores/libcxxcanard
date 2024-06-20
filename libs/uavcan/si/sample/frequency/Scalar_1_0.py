# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/frequency/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.635560 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.frequency.Scalar
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
                 hertz:     None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.frequency.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param hertz:     saturated float32 hertz
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._hertz:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.hertz = hertz if hertz is not None else 0.0  # type: ignore

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
    def hertz(self) -> float:
        """
        saturated float32 hertz
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._hertz

    @hertz.setter
    def hertz(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._hertz = x
        else:
            raise ValueError(f'hertz: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.hertz):
            if self.hertz > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.hertz < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.hertz)
        else:
            _ser_.add_aligned_f32(self.hertz)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.frequency.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "hertz"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            hertz=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.frequency.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'hertz=%s' % self.hertz,
        ])
        return f'uavcan.si.sample.frequency.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZEqdL6~1=j_au&S5<&uDLLsr++yx8{E-fu!l!gwuL^z>VU$UCr9p4#wcV{~@Yx_p3R6Z2N)k<9{i^NahC-4)H'
        'sM>y{{{ZzD@GU)OclO@vkXW*xv-5J!nKS1+XZ+XWUo4*N)IY_G*&s4e?D>Xk$zpk*1u^&hP$ii%((<Y}xn*@8+FbKHgN#=XtJTk{'
        'zf>#5l%KK$<}c@LFJ!4_q-R)?!R{T+|D5wQ9C%wHi<z#9S$~gfBUM_7PBHVTlOI-ef_6TyKC6lapINJAkXvr5KY{kA_%&Qr6;n4P'
        'kE4-4^M1rE^DR0lCYwPqHFVF)gnL_qG!$B;@;;C5z<{yfaV2KNT<eKA0oKK7w|)6(eq>rE(#k#XWBG1sWIyH6hpFX#u8&4(!4IVM'
        'W1jY{sOScG88T!2L`C4`^ToN_ts>m!ZNl6woWjujt@@-Y&iLSC8ZjM>D>}>rINCxYL#+%CRT@>raX(UFwf(=zPUnu`B+Zk6Yod0@'
        '*eXM;V3r8B$4SPF;Sn)14LLC?;e=^0p_v|#1U^$sWD4u+mDZa_rEVOQDlPjky&^sCU8`4NfJwj%UnSCzi0?><3CXzbvMh^b$SmBs'
        'M^H_eYmIt_ThLN&_&i(`2{@_q$5`0Dqg67}Zid%aD<cUw#`QH~IIkCl3iO%`4l2_=jOslJXRBS2we@*81vt0I;+&(GR*{tNVVL00'
        'POSDD|AzDH*SioBvM(d>lZOm^e0zSLkS<xfw|@O-WMMfARBp-I+QvE=aHh>QvM*#Pa0==owF8g5N3OqF>m1t)e&>)on(V7Qj=&ID'
        'AS6#y9&%%tmhqr*0TO{oYlhxJ*kBuYi#M_kR;^IE!Bw?+n2vH#K^RyA#r!}*yiyB!OhPS<G+uL<%@}e)hTYBgdSoS4mfZMYl|Uw>'
        '5K9gALZ%@p@(knk76}GWq-Zf?gIKZpj^Uz!47}R$JMC4G1l{k$Vk1}_;|*iF^<&<xmp3MM_$W{bhk+(X?eHETDXv;f3ygur*%U5@'
        'KoE^rK_Q$fW;a!eWnzbQCziz}Ctao+;wAAi?O;8Lt4-<5-0jic$G_`UVzs#Pd#=^vrt5rzd&6k#rfNU+s$$x&9jb~KT2kN#86+H%'
        '*%3;Z{iM!M7PtP0^<oZ=9O9^f`5R8gI`7bl&%rYj<N+_1$9T{W1`WmHDOSV<@rLN;KqwIhqfkyfst$`&{*FB0k&hSU%c$xVOTJOL'
        '4mnK3+|L-$MKOaA%b+UeZUe0!+{V#|Ku;5|0&xh1JU*F8SP1!OwTi(<egL_JXDBXac>o3MYu?Xev^!#2ILvfIu%HKHRuz|?NV4AR'
        '-fJEPt+GgK%f4U+oI@J$U7=Qoa2enBn!-m51TA3J01qe)tboDB{DtCXP`Gwq>D_K!8D`98eRs7{$QUb*R2nEyao%u2O$8%6@F8Sh'
        'K&?S^RRTm8Im4K@fdWmyQY{<TwYUdsl<u00hjK@b<vTQrUG5<#2Qh@`N}Deu3Wr16$G@xM#QV~IRDW;rVKNuTe3exNd72V4NCE}-'
        '15v%j6XnS9W2j1Il^(UCX+IP|1C{t=v3Q$B$dNx<BpA;2@)+9o;PF|p{*P*fZj>f~hMqMVDmt47aLz=g*xo>32Pn*7i-T-IrE~)K'
        'bxJzv@EGD`NsqhlDa47APP_3LH$Lld&W+C_PM37Stv`V{Thfz=$4h$3tzSf3DCuc8zl1nd(r28WWyEJndIs@yNzWplD(N}I6D55X'
        'alWMI-TvpC-3!jnMW^R^XYU2XizU5;c%h^(B0g7Af_T29ml2;W=}U;`O8OJTvn72Q@k~iyL0m5B73bGg#HEt1IR91=7fbq6=jYE5'
        'PnPtW^SA5H>p8z)MVu??YtH}I5ob!e=Fahki^rSpJoUXEE9rH2uD4u#H{AJt-rPHV+u<)9{?g$)4u9qF*ACxxc+=swL*eki;RA<X'
        'I{eDv*ABmN_?^S=9sbbZt=S1DoNtAdR@i8To2{_j3ZfMbTH!$}eAx<LwZhk}@J%ax*9zaa!VgZ!;gtuS0s0A2yc-LU;Gy%(+0nam'
        'wdi028@@K-K{$5<TB<$rhJ+4Apo6W6s}DeN!us%-$?^I4&fk|h<3EocJ#x*YwlpQUw)eq`_&2l`@h+<Rmsk@275~Y_`-ft)Cq59r'
        'SrIqIhvK(_ijTxC(JLkmw1Mg7C0}9Ja&P&nSZrSNN10q~9ijnoS8O*N@dt5lNG0J=x;I8IXQ5kT`%0h4Q^j0EQ_vakAAu)o^TjTm'
        'fHTI>+7tLq!R|kMFwh_4DFQsj4KCV-McboAyGU6-8piAK{tweJ#v&RG000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)