# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/pressure/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.706406 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.pressure.Scalar
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
                 pascal:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.pressure.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param pascal:    saturated float32 pascal
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._pascal:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.pascal = pascal if pascal is not None else 0.0  # type: ignore

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
    def pascal(self) -> float:
        """
        saturated float32 pascal
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pascal

    @pascal.setter
    def pascal(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._pascal = x
        else:
            raise ValueError(f'pascal: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.pascal):
            if self.pascal > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.pascal < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.pascal)
        else:
            _ser_.add_aligned_f32(self.pascal)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.pressure.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "pascal"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            pascal=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.pressure.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'pascal=%s' % self.pascal,
        ])
        return f'uavcan.si.sample.pressure.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZEqdL6~1=j_r!^D5<&uDLTO^RxeFK^TqqPU3ZX+T5lLFBFImm*j_-`TyR)5{wSAE)!H1$4t<;sWmG}w#1bzZi'
        '5%3ZI0qQT{TYAp!?7i0^v1C7I=jEI;XU=)f_>-gmSv=mUe~M?bL1d!X^9|RM#qwho#N6{km1N3D%d6t}Evxg;=9=FgWW2gxt$tel'
        'vsx*p{FEgyPja>!veYxuGc3tqcc!^9u->~BvY6?rnDuwLHd3XP=oB-5a`OF(PSDP0)u&al;4^Er406j&^><MI7`KM2s$%Mz<Z(1|'
        'XWoyPWxhop#bh%mrizQsJ1Z0LXOM<Mt5kl>quVfGEI3?=88O#-B94J|anfyHew-hfmWi}-7yMYhlN#AidGvm2d7taUL0a$wY5ka|'
        'eJd)u0bYj8SU*t_c=>d3=4Pu1w|Sc|cLS#|H2<nTs)|!S_?SjaN8^eP@&JyukjPLg!$XxuRdLjhR9J2OZ?e<5EjUT@B;cB;Z8EmX'
        '5G$A^g6(pWF=Kc{j7&pLj7m6R8cb-W2PA>d)DoG(`g*1H=258|2c=5OK1{Djk9$|@RTy9rFvC}gG$i8N5@JF!uDdMDVi__EckU5X'
        '6Xsf@p5Yd>lp8(|7exY2H2+5qcLUqEwMs_X&G7naWh4Q|xV}OR=k=mcfnJlrL1o&9QN1hSY_%)0wmuK10OxjDoOATjDw6VD3={m>'
        'j@4e{-*A5YY8OI6_GAQp@{oa#ug%XB(j{wm*RLLqEG%b%$}L%2+gK+9&a}Bg_Jj-tPC;3ucHoh>$<<eConw2!?;LVRlRcHk5f}ms'
        'gyd<;L#QLBWjttHfJ7kDnxVH4HrNK<;*G3>RV!3(a8+#{rlTBG5C+yjG2fREuhc>wlTb?|jn^DzGlpD{VR!TG9$871CD-0vC6Eaz'
        '#8QL3kZDMYJi~asN`e6tDO$|fAXcotW4I{b0<U)bc6(JMLHGNx*a#NKc*B@({g`*_<&BALJ_=OAVW7!TJG=)-ipv($0%M?YHie5J'
        '5JcluPzZ~~?50YwOzg1k#Im^Hq>FSzJSU!~9jqsDxhb8QJ3ZR_@Xx(UtQMF4!nJzXbe(T-Zy1f8RPCi+RZRP}LsjuiOA36yraDZm'
        'aY~r|sLoFoxBiIrVh)ZR;;4c7Yfi>G@6d_Qz%vu%0WX%vc+d|94a4FoR>V2+vgqbOC=myvP)<Cm4vIy8TkiA7$BXi1RP~A_->6)N'
        '942D!XAJ0~m_dkTP!)4Gfz|hK;^=*#r->JUID|qPpUfmIgnYDG#o!~~hup$56z8)%fCBb4@8>bv9WgB&X1XC*(1S6niVKe<S??w9'
        'MGu2kS){dPUoZpCAr1JhP^$yDjQ{qU!bb}PEnwCF4=4?+fWgN6h2myVxOPwJoo-zjX3S=NcePQ-7%L7{8Yob4-f%%p1tUA~A!J`b'
        'twD5E0z?-%!<e^$0!_eDEgRRhxC?8P?wX8;a$An&J2Z+N?ja`!F@)$+n=c~@heO+kzpLWdJJNnof8XN6WG;^QDuXurI3;F~1Pbm4'
        'qI!cT%8}!TP?gLoJ!(bMekgzjD)G1C#7!0<NB&}wU^v^$V`$rhhiAq5zpE9xQJMf6de&&D=xiRqITM*;djo;(qcDRl4zdN6(h1zx'
        'De0ucBZ!kFJ?g%v5GP7H?Z#)^_^iV@H$IOzUD5@&{uttHNsl8QE$O0Le*$r#q$l0{65>=zpKyAX5uYgODa4Z{J&m|n(ldz1O8O+?'
        'd`Zu`{ZBc&=bWAMPS4ZM-ZO~jOL_tETuGlre5#}b@oY&iB0gEt=Mc}7^jC<dOZq(GsgnL0ak-?IoL`p_mrA<g{98plQPSTyKYxpO'
        'yrfs0zg>4;&-wiV;#^5zbpF4DI8)L!caE1`JYI3<sqghjNw2zdz3Sq-;m-HF=HBUR4qtcpdxvj0eAD3{9KPl7y2CAp!r{Kddk(*F'
        '_@%?I9DeQa2Zuj7{JFs!vlC7@+X^eKu+a+FTVbmeL@VsK!o61bq7}Yug|AxS>sI)o6@F@kpPi7yD-SvY^b@3bHx?klL+6>Zqj%?O'
        '(ZL2bd~L#maPAtkRD0+R2_1|;2U`=D?}6fk_2Ds-<MZ*2&zCymKMx)}aLuH)G!5@Icz=T#@g4LQ@fPa(RxF7h#rL^*=Rj=s#Jl3X'
        '6>(j>Fa9W~_(0qcy<*ZpADC`l^3Vp_w|rHcXkPP&nOxjDK>gy5*lIZ9uj1~IO2VOZcZ^<6L$}8El|GWEin)fSpflh<0*}<@iyb-v'
        'XN;k>C-9qs-EVp@&>!O|0zAbHF4}@cTcbrgNLjxa#_RF^4}m&)Cm9U@00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
