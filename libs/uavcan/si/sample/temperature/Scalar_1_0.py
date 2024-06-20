# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/temperature/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.537979 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.temperature.Scalar
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
                 kelvin:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.temperature.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param kelvin:    saturated float32 kelvin
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._kelvin:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.kelvin = kelvin if kelvin is not None else 0.0  # type: ignore

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
    def kelvin(self) -> float:
        """
        saturated float32 kelvin
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kelvin

    @kelvin.setter
    def kelvin(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kelvin = x
        else:
            raise ValueError(f'kelvin: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.kelvin):
            if self.kelvin > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kelvin < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kelvin)
        else:
            _ser_.add_aligned_f32(self.kelvin)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.temperature.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "kelvin"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            kelvin=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.temperature.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'kelvin=%s' % self.kelvin,
        ])
        return f'uavcan.si.sample.temperature.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZEqdL6~1=j_q-V=AtVqcKoh&oUBKYr($WG(A#}(kB1vmOo7L>@_|C|?JKLGrYhR>F<wH?it;9;%O8f+V0zUz%'
        'RojpBA0U1K-_mn-XYaiZi6#3vJ1^&)Ip@rC#(zEfkJHCH^-uA9HjGRZd%odXvRHn`f|z@LsFF+>X?ax~zio9M+FbKH!;DuCs<qFn'
        'zf`NmjGwXu=3mU&AY`d$q-R)?!EVcwjBAElyxSp*nXZa?f55eoDy>APnESnxA5?UTcD|@SuZks~S*vA`TW+d9f&M3WHd<8`GuI`L'
        'qp?See#9*EExIYDn?W&CTyhRtnSejTG!$B;@-rUYfdON|=Ss|ph1L^s46KV&Zu`oU{K&LSq?H5kW94pYWIyH62dU+Kt`Em)$q%IU'
        'W1jY{sOTnm88T!2L`C4`v&Gq4ts>m!ZNc14oWjujt@^ksPW#|v8ZjMBDmusmINDMoL#+%CRT@>rQ9n{)wf)0%r*lVelIBUkHBmcc'
        'VwE9QFiQj*aFQ`&ctng$Lr#oJIAI!0Xr_lGfzQ+unZo*drS%q3sT&8SO3OY>uS$=5SL;<6U=lFH*N8ME;yV&zLZB47EX!gUG7CBP'
        '2&xHltx?Zt3tGwzUxY-FfD_ICoI`G4`;J!0Si2deuU1A9aE$A##Bg3O3Ki%z85~rmeHhgP31_Qak+t<jI0ZO2U~$gTORGrA2N)*!'
        'vlFYm#=p`0#<eblgzU)({Ny16AKzSDB&18$?`>Q=99dY-0+m~`zP`CZhMZ}0mFx)_3Y>zQk=mh0-XYgsuXRrB1;2Bs9ZmLB9!FpZ'
        'ED(~XDG#|ZOv`xKxB!Jfq%|XNA#AV>yv2-cfK@A0Zg5p?9;TxlR1gN%Kr!E!5U<oi9g|Q?BaPP_W-EqTkYRW0ogP_Dl_l5TTO&{j'
        'Da2BPy^v`riaf)3y+MK@TvD`{v0<!OonuH8(1BMwey2?pNzna1EH;A0F=iOctsnDly}U88!^eS2I1Ds3YDam1qPSwQEHDNdXH!TF'
        'fgl>Mf{SpXnBP(<UK2aIcVb0cbkZfdDP9mS(GK1xaizIBb9Z~R_t77El~^k-f5NqT)O1~MkT;CRZmRZDuPSE!+M%j=t|bM&pFzPP'
        'nH{2p`H$=RWO3_{*eDj@$RUmzn7{61yyqP{^#yolf;`~G$^;Mk!LT7&JjJRwFJ2Sf90(=iU=*$skE(;>guf&AdE{fFd>K`}V%aw;'
        '*CB_AnEM$6x+vxlVi{D$!Yv^7{aZNt0O)DzWgrfrkjbYr2@9bftyVGk$oHYP@C?O;EDzuU`<nOj810Uk77jDp5G?4ym{rBa$C9k~'
        's`rYAL8~m%+KMlj0q2kge0Nc+14za{d(Fj13j{4-)c_AD4Xl8{#`=ZJ&EVqNJ*9WM_02F7HtXEgMxkP?ICRrMfr|5n3u-DD+kp=u'
        '`vUG7L{}w1bdfWRbsH$q1T59EaeWsDutw>w$#^Jt<V3wgquAvha&izuh%UGFGNy1iw0-ouDvrG??T7XEZ9XdI;)t)Zsvu8NVunee'
        'AU_b*n><mD96zd?u+rmJH0y@~XrK~*EKc5H5pv{D772#4y*!4tJ$!UlY<yX*(#_HY(9p9+Lq+HF0M41n6x$mJY#)U=Y;jO6sFY6O'
        'zD`M}9UeiPF6mMCJ%cz^(pfh?=f>w9F1YbU#MzQAx%I~o=SzAV@n}g;xb-Iymr8od%`YR)l=La5X9e-8lAcC9RnjwvCrWx2@mNWp'
        'MqDiEIk*2AXZO6bbHV9(*4cXw@j^*2BAzel^N7!slpvlf=_SOcOZo!h*^<79c&4N;A)YSj&k$EidfEAP1#!8gtIoeQ#FHicx%2ZE'
        'h{sEM)%n|X=k=W5FC#9L^cCm-tB7+YU3cer&Bfz&cb+=0M@o9lo$C!3-%WSEUp9HCZ#w*y!(Tgm%i(Vv{?_5!4sSTzb|@U~JG}4k'
        'D~De@{Knz84!?8wy~7_Hyg5JRgmbO1+6tSkaHAErTS2tKek<H>g|AxS>sI)t6~1kS?^@yeR`}5gIlS_qGeAE<ig#lH5<GOC1v`Fs'
        't`!|@V58S2JO~%ALrb-X-jLA22z0P@apgWJPFNovGdVsV-}?J<XY%La!-uY!)Rty<c|3q?Db~b)ptp#(QP;o4viP6)Z!X?F5L-R*'
        'o_K#%+z=m#-w7%{6gNe$m^RP{W}C-6Jj^Ga^Hp)OdC(swb8-6sO^CZ<yP=6s#k~=mgd^$R1jC$xhK(I8eJoWK3k_32bHM)v9;?k4'
        'yL1YU8AEqZ;5P-k|LVa&e}bwAP!%`0Xd4!7j~DGCYyD&xGvxgr*A^&39}NHi'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)