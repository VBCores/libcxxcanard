# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/energy/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.513844 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.energy.Scalar
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
                 joule:     None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.energy.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param joule:     saturated float32 joule
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._joule:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.joule = joule if joule is not None else 0.0  # type: ignore

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
    def joule(self) -> float:
        """
        saturated float32 joule
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._joule

    @joule.setter
    def joule(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._joule = x
        else:
            raise ValueError(f'joule: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.joule):
            if self.joule > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.joule < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.joule)
        else:
            _ser_.add_aligned_f32(self.joule)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.energy.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "joule"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            joule=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.energy.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'joule=%s' % self.joule,
        ])
        return f'uavcan.si.sample.energy.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?Ya>u%k~5k8Ww%aMFjWIK+XIO{aErPhZ@l*m!jrcI*2b-MA15!tQKi-{$<I=dCgWp|g7PJjZ<j|NsjAOy?;d4xPd'
        '9w9)Bwm;K12>Jy1=gyGJbB-Kafb<RbGBZ0f`_1Yv$N%0v*{Oeu7qekxqS*5d*OJBZ6BfkW^Fx(n%1Fzr;^daqd1!OZ?+!CwJ*-wg'
        't^QoC6f=Ix5}3c7v%Qd|o{^qmNd~)l%JpFAZG|jmx+>=VJ+6&ZX(c+v+^?Pdu%c76^I7$2RV@0<S}lXza#Q^QR6oV3(W<JLxhZ)Z'
        'jh$KWBW9Uz(L*ua42qfJiu29NgnL`VG!$B;@)I82g#ly1-Ac@fZtICS0oKJCw|)6(eq>rE(#k#XWBFcc<RInI2dU))u8)Rj(GR5c'
        'W1bGIsOScG88T!2L`C4`^Tqi)ts>m!ZNl7boWjujwfeX!&ideE8ZjMBDmu&qIND+&L#+%CRT@>raX(UFwf(>8PUo)RB+Zk6Yod0@'
        '#41CqV3r8B$4SPF;Sn)14LLC?;e=^0p_v|%1U^$sWD4u+mDXE8rEVOQDlG>vy&^sCU9VSRfJwj%UnSCzi0?><3CXzbu`G*a$SmaC'
        'Bd8|KwMIRoEodn>d;t<g0!}plQx3U-?K@f}W9?>?zFHYcz%j0`6T^AEC{&==WN=WK4q#O8NjO{Wima_Kz$w7FJr?I2y|jv?d=J9}'
        'e|BQE-}pD0U%%0VkdS>DfuB5N;Nx2h3xxE@+Wqw#M<WZ%S)g)D*48%G$&fQ`u9JNsLxEFpDN;N1$h+jm8@0}fz2J8awWG<t%Hs$O'
        'fdxYHH02>ThG`iO8yBDuh_q(pErboWfw!2Eb+BrM$_=in&BJt*g9^gH8Yt!m65^FwsACdpX{7O*!)(S-3o`6&zS}1&sj}qe`>O;h'
        'A%$3Kuop57MUiJ1uQy3BgiDGRGd7GBt8)yA0w(Zk$M3eOA_=-bfW=0zIK~WPxea38tCu$>cKA3@35S8EM(rpMP!!iJmIcN@<7^6v'
        'ArM64Rd5kb74w@a#cN_m_f9N}%TBsNH^fWgW!k~}B(61AXYO8~_CNYfzY?p()!%Zh9yeXr8{`e6v74&>)T@eFzjml9UT8^yA7oH)'
        'NM=VUVgBQ~K3UxQBi4&9967{M1M@eXjQ6}lr#=JEOpph>Sf1cPKNvRril<l+7sczMmjj_h9E`$s;!$;2obq?%0grr4lrN*IUo81X'
        '<vQdr5pzFdKo`XvLM(%-=-vTNKe&UV4}qShUIF3|3Q2rAldur#(P|ZgkNf~?3(rto%JKj%u&?<bkJ0X!Y2h%l4Z(sQj2Se8Cz7o9'
        'n)j-QL8~m%+OjX00q2kge0Nc+LrBIy`pv~h3j{4-)c_AD4Xl8{#`=ZJ&EVqNeWiDM_02F7HtXEgMxkP?IC9fKfr|5n3u-DD+kp=u'
        '2LkRIL{}w1bdfWRbsH$q1T59EaeWu}V2#o}lkrgQ$ccJ~MzPC1<m4cR5M6ESWlZ64X#4ngRh)QF+7IjREj}vd;+U_psvu8OVunee'
        'AU_b*+dNT@96y3v$*j`jRy6B}0%)KTzb{VTVG(lV_ZA6;v;91Vwmp1&R;+(st<a6q1klj4MngsC^8n77$Q0Wf2<!lbIc#xIEvS@E'
        ';l55uryU+coG$5c_dSC+Rnl2EKIg{g9d_OL0^)2*7v1_3i1Q^qiFmxEr`-C}h>ImX<K~wTXG;2v)3c2DOi9loo+;@$#8V|bk9eY_'
        '&mu0A^n%;}oU?n;*}3HOJn!tifOx5-mk}?P^hLzyN=gtfl=KSXvn72A@q9^tfOxK?FC(5U=?@W?OM2D$bq#T;q$|$9Rm9UJ{gLzY'
        '$A~9OdfoZkbLaJ(->)EcOZuww|24$9lCHUPyzb)hhC5H4*JCBU;m-A@i|>Xz-%pyn)3+S{)Zxz@zU}bm4u9eB9f!9ZZaWkX4;(&l'
        '_=UqS9e(BTYlq)B{MO-j4c?xga>9jHSZRfgR=Cv)+pQp4;h+^Bw89sy@MSA})e2v?!Z)q(Z7Y1|gdARZ&>5hgAjP|}00|yCPuGs$'
        'ovTF$8`$Wz2@k^VO=zk1$Qu$m7=aG9CaygI#R(h0V<yMv<J*5*>P-GTdi2OOliJeEAK^Ix%T~p|p|yy2P}RT0lK8LqPcGg&6q|kV'
        'zWC*exFtRizY<h@C~k{>F>Rm?%r?(>5SoX4Rh({~@<(Z0Y#pL@aZhYF1o1m@f5ao<NV-44E$5(BWA93zNK!?&;V5Ve_+P*iwfSO~'
        'PQd|V=<5mmreOD<eHa)_kQ4!u;szIO!=ml+qFv;x?+s&ay#E6YBtVc94FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
