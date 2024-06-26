# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/optics/HighColor.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.745426 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.optics.HighColor
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class HighColor_0_1:
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
    MAX_RED:   int = 31
    MAX_GREEN: int = 63
    MAX_BLUE:  int = 31

    def __init__(self,
                 red:   None | int | _np_.uint8 = None,
                 green: None | int | _np_.uint8 = None,
                 blue:  None | int | _np_.uint8 = None) -> None:
        """
        reg.udral.physics.optics.HighColor.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param red:   saturated uint5 red
        :param green: saturated uint6 green
        :param blue:  saturated uint5 blue
        """
        self._red:   int
        self._green: int
        self._blue:  int

        self.red = red if red is not None else 0  # type: ignore

        self.green = green if green is not None else 0  # type: ignore

        self.blue = blue if blue is not None else 0  # type: ignore

    @property
    def red(self) -> int:
        """
        saturated uint5 red
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._red

    @red.setter
    def red(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 31:
            self._red = x
        else:
            raise ValueError(f'red: value {x} is not in [0, 31]')

    @property
    def green(self) -> int:
        """
        saturated uint6 green
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._green

    @green.setter
    def green(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 63:
            self._green = x
        else:
            raise ValueError(f'green: value {x} is not in [0, 63]')

    @property
    def blue(self) -> int:
        """
        saturated uint5 blue
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._blue

    @blue.setter
    def blue(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 31:
            self._blue = x
        else:
            raise ValueError(f'blue: value {x} is not in [0, 31]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.red, 31), 0), 5)
        _ser_.add_unaligned_unsigned(max(min(self.green, 63), 0), 6)
        _ser_.add_unaligned_unsigned(max(min(self.blue, 31), 0), 5)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of reg.udral.physics.optics.HighColor.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> HighColor_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "red"
        _f0_ = _des_.fetch_aligned_unsigned(5)
        # Temporary _f1_ holds the value of "green"
        _f1_ = _des_.fetch_unaligned_unsigned(6)
        # Temporary _f2_ holds the value of "blue"
        _f2_ = _des_.fetch_unaligned_unsigned(5)
        self = HighColor_0_1(
            red=_f0_,
            green=_f1_,
            blue=_f2_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of reg.udral.physics.optics.HighColor.0.1'
        assert isinstance(self, HighColor_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'red=%s' % self.red,
            'green=%s' % self.green,
            'blue=%s' % self.blue,
        ])
        return f'reg.udral.physics.optics.HighColor.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{?|oYi}Gi6isM0j}4TRluCdgZYx0|l3A*z1y!Jmgrr5AglJ1qzaYyqbF;QGV~=c4vI|0@A3%y~)I!W(;rDSp`^YBg'
        'sw=I=W8Zu3!{?s)ed^!;W+tkiTPnJ#NwbI=(1K;+7Zzs_(M08iGQxs)?>w=(Ol+y)$8G`s)UQ1EzxicXqmt!#eoI3;DpSp}sNh{A'
        '5)-MyhR0*k=9?;0+PhhL1lkBCJ)dwhKlRtAzB$pH{L?@8Zk{r0wTMd##{Z1)V-g!$c~{#Okfmn{)oIEsqc&tY&b`ng7gijh#o|+G'
        'L|a1oy|mB<eZIPR8VgG^kZsF-vxeXaGnVEm1<$X$8~X#G;1+G-*={%r75(8`-d(50GMO@+jsl&OF|WBR8dC43XsQzLCOqyf^rG@b'
        'extwopgGMy<e%`Ro=dH*0kC;D`K>YLwNdk_I4fabebvowDjCwT!}`X%&g_2sjJCGEtGwMbJz@dMeLUzVbP5e7T;I8F&bFAvJ(dkZ'
        '@O3wLpji@j4W4iJ*P%sA;nG{)#27JpQ|WUdp+~K)t-UHGzRthw2jE{fAHD(UTxqibX=CT<)&S_MG6uIe!aN#xd#n!LgkR&I@!Ncr'
        'FY~*+!8iFszQZ4v$c+@R2??`!k0<UbJrEs8X`!^GBK3Rj8a1la3E)8nv|xDiZYDf35qmeckCWBe54)$xw8;i?fvYe|ZxsR!6D6%y'
        '8TJf17If&T`=}`6Oe7R%t;|B)Gp=KEkx*@%hiV8zq}~{MH{BaV@7^1ZV)R9HCki*|ZJ_BQ<;-A)8l(-QawHP)C;aBKza}RpDhDDY'
        'u^h;N&g9PhHDolow|0N+9%((=AO}k4%#!7bqC^;SEK<-UErD1?q>^i;6v2oj6`%neJY<cqU7`*ua9-w266nH8ROi+f=0T$YGCCHA'
        'qJUJeNa=PXyfs20w8E*^w-HPOGf1!i6rzZvqTwoGBv(=;Tw`NNhEA3w7$OD|MmU3%lt##QuQa@I5?Z-hKjxsJ+KhE@l1TMXQVItG'
        'rGhY19p->o{oH#+Re~w8iv}ykexTx@Io6Mx59)O?iuVm!Mg?f}2aSAAs?IfrJjb0dzl{N1S4e~04T2G8c$c3JCh<&H@aF8rckkZb'
        '5O$|}e*(kFcUPz?yd&d4OgE1eG7YJ*3%Nqw4E_9}0L?54`A{FHX~G4nFF$ne?z1$-US2Zd1<!}8L-#(aP?#C{T1Yq7LqsM9{U7nv'
        'uR-hdB;eO^mYCIEnPp6OFUH~PFa2_}_R7TgQ7U?w`{raBV}ElYgVy7Mb;4pM=snI`NUt80kICx0wTE)@Vgzj((ZIy~Rdb&IjsJh}'
        'pfY+HfG=;qxR6QDcL9wSMtx_?%iBTeqW=K`?9{)(2LJ#'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
