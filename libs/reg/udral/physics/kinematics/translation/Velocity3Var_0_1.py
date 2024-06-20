# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/translation/Velocity3Var.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.666556 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.translation.Velocity3Var
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_
import uavcan.si.sample.velocity

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Velocity3Var_0_1:
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
                 value:          None | uavcan.si.sample.velocity.Vector3_1_0 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.translation.Velocity3Var.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          uavcan.si.sample.velocity.Vector3.1.0 value
        :param covariance_urt: saturated float16[6] covariance_urt
        """
        _warnings_.warn('Data type reg.udral.physics.kinematics.translation.Velocity3Var.0.1 is deprecated', DeprecationWarning)

        self._value:          uavcan.si.sample.velocity.Vector3_1_0
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = uavcan.si.sample.velocity.Vector3_1_0()
        elif isinstance(value, uavcan.si.sample.velocity.Vector3_1_0):
            self.value = value
        else:
            raise ValueError(f'value: expected uavcan.si.sample.velocity.Vector3_1_0 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 6')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 6

    @property
    def value(self) -> uavcan.si.sample.velocity.Vector3_1_0:
        """
        uavcan.si.sample.velocity.Vector3.1.0 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: uavcan.si.sample.velocity.Vector3_1_0) -> None:
        if isinstance(x, uavcan.si.sample.velocity.Vector3_1_0):
            self._value = x
        else:
            raise ValueError(f'value: expected uavcan.si.sample.velocity.Vector3_1_0 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 6')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 6, 'self.covariance_urt: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 248 <= (_ser_.current_bit_length - _base_offset_) <= 248, \
            'Bad serialization of reg.udral.physics.kinematics.translation.Velocity3Var.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Velocity3Var_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.sample.velocity.Vector3_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f1_) == 6, 'saturated float16[6]'
        self = Velocity3Var_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 248 <= (_des_.consumed_bit_length - _base_offset_) <= 248, \
            'Bad deserialization of reg.udral.physics.kinematics.translation.Velocity3Var.0.1'
        assert isinstance(self, Velocity3Var_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.translation.Velocity3Var.0.1({_o_0_})'

    _EXTENT_BYTES_ = 31

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{@Ly>u(ju6~8w4&BI_`fhL(yO6&wL7-Hg*rY$8wv;)TFRn&-VW_QPT#@<(EX0LrCRcb!8f@r0##8%=@$e)luAyU6a'
        'Egveil_E8YRH@&}H+s(Q?7i2-u4)N>=g!QY_ndR)x4ZxN^>nNH%U?~qfeu2))m%vy%1@XVa>w<PC{469yv+CBHY)Q?rudz1%FD;)'
        '+^6Ml%GrFxjadZyi;B0MEKn?TQqk4Y*Uq|(dBhBoMzL6jKqs+tkB5mbP4~h*rpkQW?Qo@Gy%eo{?4G3`m$XHPeqVlC=2I>+MoBL-'
        'T$c|(;tsm@PL=t{RmsDkuj8Z}FvDDfii_cTQH<oTWvt_~*wNC_EJ}e%$EpT8`X*5qN--uT=n!q8CSngr7t{9hnQa&u8FA-!H}-`}'
        'V)+RV?!baJ!25qO+R30)$w(U60fT1l##**x9{fBuyv^0t5KOtAG;YY_wh<*=0&{()jT<Ean0qQeveGcZ&zvi;cLTS;$3wp>Z<YBW'
        '7j%pRrh-96k1`KTn~J2b63zW24$6GD8zg>t|J&hK>yF?g&LWR1lB|+}Q<@mT3=youNy@b50nsw{InhbP2~!|KG1Vmz{EQ8eF`TbX'
        '8fOxj+I3)>DA|VXS?O@+Omzw!OgyIf9Fdv?d=)Y*ASqY#EKNh{*9k_Djh`une0ratq)hWk2o&)+QT*c!VgsMAswC=j*S+vn%t!=^'
        'adn1h&Z|Ry0(^A}hRV1NtEwZxwn`OQNuLBOK)DVJGmcuCgv7jqZi4?-!(^k@ueZN=aUNVkHe>*La-V^YmnJ6(nJ4EzT)eo|vv8bw'
        'NoL6T^Gl1Q%bC(=$cB)<z%9t&7;=|fCKunTcn*9EdS{S3ifklV7=R#<Ku8wH+~-;|CBts50we;FM)$M@x4~ziEk<M!q#BWA8c$W?'
        'VLQlx1z{i!81qdD{)!FcG4YkuQaiOVS3<}I>Ca!eyi8`}#E`4+&5^1sq=^D~K2wksS&II8n|NKg?I<y2-7sNQj3H1^X`D*&J58ua'
        'gzC59uof%~F~XQ`?U2t`$7>O*yzi)p!$O^-rWXfDiq{RM1^PhYZVZ7T;6&||a1r+9<5!XxuZij1J17CCEj34%#2exaZQ*?qXX~po'
        'c6XUB-~82bDHih6zve1=QFN7W5I6M3dYo*;PMMFol|p6ya#IxeW(o<1RdGv67{68JCkq>W#Jl+fnC#=KhW)FS?$y#;rS>w9=Q9HZ'
        ')%Ch{{YER!iId_Tv6w+Y2{;Ia>%@cdQNGVzm76?pF;K1y%H{lktCLLm95zDkrVPqOK86rVugoV_pl58Z;Ob*2PeW&+aEJt(#BeI%'
        'AmpP_NeDXfO~@^@AwQ939$a7-x=0qH+<wUhV@B%&3w+RLW&X;xMb=qx&N=9`(qLJeaRt+$9F_ssUexjt1mjQ3^~FaC1SMeBKpjXF'
        'R0VW4<}X}s1{c?CBx-%Wx*2*vW)-_iC}fNgTW%UKNW!eH1yw2N%Yh$4wgucZ@NN=8p$n{F%v&!3PEe(qYFypL4xCBUyiU0<SLHyy'
        'L!(&d4%TEZ1Q(rd@}*zG!D#d1?=s)>Gik0@zi;ziGUvP8BrS8Y6BFHyyaeI{UcJGi#1_Y!a4Q+~$$l#ub$tP4pcFyAe}x5DBfoP<'
        'NZeh{!VucPi@W08Ka{g{sn8xw25HTqq~n<fc1AMB_67voL}CnE9ApbJr9=2#tDwUccOecJbhrIIf;d#rQM*27*T*eR*!4-o(SlCd'
        '^Lr4-3%VC^cR}~r^ZOB}3Oa4~4<L>d^q}Q4gLtr@hY+U=dKhtEL60ErDd<te$$}oU-@jz#9=CE%SU%sg@?J(fQP5Wqj~Db+#Fq+6'
        '5RVn~HN>L@J&Aavpx;M4T+ma9hYI=w#F>JgwtBsec%Y!OR=+vK{RMr)>iH((-h!U7`p#Q>9jo_Q#EF8Qv-&R}jurI0wc~>I$6MB('
        'MZ{eNy=d)v+xmCO+V{gc?(~wycP#$MqRk8XV~anr_*0A5EZ(;$EN)tSXz_`~&n<po@k@(OEq-J1S&cWwhb(cdA!Zw5sUfa4#Qla4'
        '4YAn}4;$i1Lww#4Uo^y*4e_)gzG;YOmdIergU$f`1WUYK^RU1}=b145xpN_JVFT+=n<sV{pOs==m<6w5sjut9Wn9`iYVLJ;$Z<Zi'
        '!}O_q;wtoKv*i@DLjvvak~sSiw2W9ACZh~z(f2<)&>H-E{`|S^OmM#^U}{YnPTwWnB_4>6>U!Xd)q%2c@D@+Gk=qxaVRs!rl_D7^'
        'C8VgFV(3RAgMXdDT4C>gCcawk`EEMm(34zX?%JtWEQr5A-xSwSi9d_u;y>bPCVufq&}DI5+?*9F;+Nu<xGnC8yW(Cxtf9w^)(;A3'
        'am|yW%%|<6Vr!ccA3Q<<+Z(*zqXwOD7)BB7&GEKH7#)c<7}_2_m$v2B7Mc!KUReUKETLB#XXwfq;#;n9`w476*=Ac~N#1$i`f{Y6'
        'Woicwyqx}OslSPT^fG4JW{mh+yno~G&zrOm|D>ba`{rMk`ZpZd8uIDyguIFP7VY-=Ne2dB25%ELQwFcf<qu}7@Sm+iKlkDJ2jp&w'
        '?+bW}2$<UNILwwfnbwbih6B74U~?0P#X3{gjt;e2;=tOQ0BgtKKS-H}+oept3uYd8vsQ0s9HZ*jbD2-}-_P(09(X~Q`QgDgG-T7l'
        '3;C3Pd>y`JiZt0*PbqzMoynUXjzqkfMrHlDfZ3yd<-_={Gp`z2z}EglIfJ|0e<t7d88q=Kq09d}gV)Bv8`Y1sDWG=9(X}D;Uz4W2'
        'JgWk@b`tjL1bqe@&w3lZyxh8s0eAij3zG1A?+^e0'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
