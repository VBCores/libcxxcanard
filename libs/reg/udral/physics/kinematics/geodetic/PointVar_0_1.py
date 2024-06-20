# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PointVar.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.592708 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.PointVar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.geodetic

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointVar_0_1:
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
                 value:          None | reg.udral.physics.kinematics.geodetic.Point_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.PointVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.geodetic.Point.0.1 value
        :param covariance_urt: saturated float16[6] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.geodetic.Point_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.geodetic.Point_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.geodetic.Point_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.Point_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.geodetic.Point_0_1:
        """
        reg.udral.physics.kinematics.geodetic.Point.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.geodetic.Point_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.Point_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.Point_0_1 got {type(x).__name__}')

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
        assert 288 <= (_ser_.current_bit_length - _base_offset_) <= 288, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.PointVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> PointVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f1_) == 6, 'saturated float16[6]'
        self = PointVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 288 <= (_des_.consumed_bit_length - _base_offset_) <= 288, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.PointVar.0.1'
        assert isinstance(self, PointVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.geodetic.PointVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 36

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`vVTW=f36$fx$M2ezliMm*3Bw1cNj!oZIc6y1E-kdsd9E|0vw&NNIob`}9(yYDQWp<Y`6(GR+p@mZ{&;`5&@)7b8'
        '^0<A=H%JO3ZQh!PqCnsLmd=p>A!XW1n!dC}B)~pH?s9f!xWBW5!*J}6hL-95MTgqkrf=H1;WN*ow)Gxu*i1K?ZmaG3R=|>I-}S)j'
        'G=q-EZfv(%@+dj+AbCHjM+L*7Epc4;*rwhwJ!<Q1zU^C0U%zKLtVILa++?oFL`z?HEho51y(B6bTg>w<*GYIL8o!D5ql9Eg_IJsH'
        'B$_m65O`Lj6EHuyEiSdoAO~k9QQ?xsY;!ocvSHGI8i5=!&-LHrh3M3G7;D1E`Ggu1uZVH*Dmt3mZA5L)YFUA`B}O!H$#!Y*<dRJq'
        '4J$Bg=4=K$As56bo74}Cmbh%fm!pMs^>O(z{h~OwCJ)J_`E7D7iRKMIppHpBb7w~nML#XN=~zL>lo#IcXfqH?>WihmgtqA8_YX4v'
        't-r@#_x^foc`fNQ#5Ym0#hUjAJZ6|~Q;hX(kD3;BZp#w}E6rEXI!rF`Bm5XY{*c%CssF9XOxUio*`Ezx-EAVnyHM-UttNGJ-_kqc'
        'ThsgBqy8JqWY?S27DjrvUY2Ckt@nSn9)%VQm?zgFBi^9V+z!x2W4oU?-cR@&{8e9|Fj?DUO&TyW`5>AyHmoi)jkfCrhGiyKqZz|@'
        'J6@BC12!|-RNV5>xD2+{5V!lf$Wz^Q`R*e@EW0XhDDKL{lxth!#HQ;6o@<Nyi*?1I94eYi?M}nCnuf>*9a~;^m@NdFV*l$A9r&Vy'
        'G5HmVH-Rmh8-7jtIsL3I(?AkPopT1Kz8Ig!oIvJ<Evw0r5BMs-EN=0JEqXqtvc^!aI58M~okW#iTEUgx>+9kr@<)_6+;$RayLIAk'
        'w;HaPmKezzYq=sPN%_BOGmi$YH_Spsqsc9iEcr$>y-rQjayFkjiQkh)uXb!P&F#^nqK7SNcUba=q)slxenX`6cE6*9lsXMD-InFZ'
        '1ScA_D;wi7$%(a=eUq&GTqY(t#Jr5zn2h0dLB_F|6cNX9yoBQucwNTvNf{?%Qo-weGFD<TC1WWj(|Es%&(FxXFDA1xmSZv}<9JNw'
        'ao&FPzaZm$Ob*C68<U!h)tEdd<5Wx*ah)afvyAH<l(86-74&yV##~G^T>r3)hhlO>#+8^nFXO?O9F=i7CNIdi6q92zF2>}zjL*fS'
        'E@LewCuBSjlan$o#N?EW`(tt%<2@teTugL~dsW7nn4HD<&&fC)lNT|MA7DLxi23|T#>trc81s4w>w6yadl~EX3g-C}84EG_Ddzh#'
        '8S^puIp+Nftmg&H|8oDnA-51YVi)lt;)jSIA%2Yb3F2pnUm-s3$F))xjhbrIRpY#BTvm-+s=-yGs~Qhg<3rW>NHsoIjZakLGu8M?'
        'H6EkU5zlAVZBwVW&%t{QztMjVQacztIfB<L`G9XSt-*r(j5%7snP$5p+h{FD9nEJ{v)LB2wffriD<?Fu8R(s|(L1Frw=J5x(R+(J'
        '0dpLxYcfB|J%y&Oq|t^eUdoe1C%VYcjK3+(>wJ;F#Lw|R^OrlEe88_<<!gMs&VS9X@$38se~aIY@*-!7?N)COCDU+!7nMZi;XX>F'
        'TD6l(qN(0qO619N!%WHF5m_<%(;GNR>+Lkf+PtEvO~Gkx@I*b`o1_}MUcMoQ?RqBjG|ShT-1X%uxth3illLdy6$g4}h<v10<Lc|L'
        'X<}d0LI=L}9_#gM(`~ndH4`86)mB$_&fe{aMHPL^4lYtpJiNqHU5-{Pp4^}%+~AE~M&yk1LE>x;T6{+`-G9+_<TK8BW>$_S`bk+l'
        'JLHb{TYCFP|Dylg?aX)k#{-q0`4-8FyY0T%GIYhi?Y$(tmxRA>Ntl1CGVfD7m@jRF!bbQFHgY32^01MEjogTh9Bh<eV;nY0urUc6'
        'IoK$T*qDHg9BfR%MhP}@urUi8`(UF48+q8M!NxpnRAHk68ztBn8?kW^HWp#y0Bp>|#tdvs!Nw$PlwhL(8#&lG2^)3TI0hR>VdDsF'
        'Xt1#Y8_Te<2pcunSb&Xr*qDWlDr`)_Mg=y?uu+1IB5aJoMsCE$dDy7KMh!Mfuo1#W2pb`6gs>69MhF`rY=p{2sBDDFMyPCr%0{Sc'
        'gvv&!Y=p{2sBDDFMyPCr%0{Scgvv&!Y=p{2C~a)X4g8*lJq>#rgafPpXh;Qy^cyf_Mlj@nAp;Eg5e#`?$N@tE7&5?628J>)R7Nlq'
        'fT02mIbf&&Lmn8az)%8)3^2?9Lm3$Iz)%B*SzxFDLvaMd5-=<P!wfJ~fMFaMa=>sD7&Ks528J3i%mYIe7%IR}0){bQ$N<9`U^od3'
        '$ARG}FdPPk6<}Bbh8i&J2ZmW-m<EOlFiZeL5g76#7|sGi6&P*-!)0JN4-9o+r~yL>7*b$JfguHkRAERJhE!ol6^2w{NEL=uVMrB*'
        'RAERJhE!ol6^2w{NEL=uVMrB*RAESWJ{tBk>}mMkYe4y?&@Y6_BJa*(f3&pAFIJvMx07i8k}Pre3%sw&x1Ri&XrIAs){<4^{_j`A'
        'l7Dqa$$#z3uT{xiRu5>KHmzVgA;o7`B{rhjYpl%z>)A!&oN-Tn^vT*mHSSIGKDi^v-}w&Yvm@jSBjk%9Uj+Hm2>AlYS3tfvLVgnD'
        'iy)r``6|d)K)wX>V<Y7EgZwPWPlJ2~<R?JB2=e(6@+%;}4DyR0Ujz9Cke>(nS&*-S{1nJnK)wv}C6F(I{20jRM#!&%ybkhbK>jqy'
        'p91-lAb$en>mYv|<d1>;3m|_K<evxmBOrem<TXX$&XB-V)7_%tCU=_5=y-v!aBDi7$-LeB4d|U0Z<pU{i@WWNXKnI83*?ELHdA%E'
        ';b&z9&$GJy`kbl=?mTY!n#ndShnbqkWT8;jFkOvmf#^|Sv1A3*rjD#^dTwX4Uk&uztZ8jn%pBAfR|lm<z5IIL*`QpwTLn^8AGJ4w'
        '|FG;hsIuPuJeSGvnY-unnatfUM0>YVEB~B-!T-Yl%D;?e)Q{)SsH5`B|9%zn+v<jY8x#r$&v^dn)lTE?-^Dn4Tj4b=%e(SFbx7?B'
        'o;o1!4*g%TGP9s+AOHX'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
