# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/Point.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.572329 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.Point
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.length

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Point_0_1:
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
                 latitude:  None | int | float | _np_.float64 = None,
                 longitude: None | int | float | _np_.float64 = None,
                 altitude:  None | uavcan.si.unit.length.WideScalar_1_0 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.Point.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param latitude:  saturated float64 latitude
        :param longitude: saturated float64 longitude
        :param altitude:  uavcan.si.unit.length.WideScalar.1.0 altitude
        """
        self._latitude:  float
        self._longitude: float
        self._altitude:  uavcan.si.unit.length.WideScalar_1_0

        self.latitude = latitude if latitude is not None else 0.0  # type: ignore

        self.longitude = longitude if longitude is not None else 0.0  # type: ignore

        if altitude is None:
            self.altitude = uavcan.si.unit.length.WideScalar_1_0()
        elif isinstance(altitude, uavcan.si.unit.length.WideScalar_1_0):
            self.altitude = altitude
        else:
            raise ValueError(f'altitude: expected uavcan.si.unit.length.WideScalar_1_0 '
                             f'got {type(altitude).__name__}')

    @property
    def latitude(self) -> float:
        """
        saturated float64 latitude
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._latitude

    @latitude.setter
    def latitude(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._latitude = float(x)  # Range check not required

    @property
    def longitude(self) -> float:
        """
        saturated float64 longitude
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._longitude

    @longitude.setter
    def longitude(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._longitude = float(x)  # Range check not required

    @property
    def altitude(self) -> uavcan.si.unit.length.WideScalar_1_0:
        """
        uavcan.si.unit.length.WideScalar.1.0 altitude
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._altitude

    @altitude.setter
    def altitude(self, x: uavcan.si.unit.length.WideScalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.length.WideScalar_1_0):
            self._altitude = x
        else:
            raise ValueError(f'altitude: expected uavcan.si.unit.length.WideScalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.latitude)
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.longitude)
        _ser_.pad_to_alignment(8)
        self.altitude._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 192 <= (_ser_.current_bit_length - _base_offset_) <= 192, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.Point.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Point_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "latitude"
        _f0_ = _des_.fetch_aligned_f64()
        # Temporary _f1_ holds the value of "longitude"
        _f1_ = _des_.fetch_aligned_f64()
        # Temporary _f2_ holds the value of "altitude"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.length.WideScalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Point_0_1(
            latitude=_f0_,
            longitude=_f1_,
            altitude=_f2_)
        _des_.pad_to_alignment(8)
        assert 192 <= (_des_.consumed_bit_length - _base_offset_) <= 192, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.Point.0.1'
        assert isinstance(self, Point_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'latitude=%s' % self.latitude,
            'longitude=%s' % self.longitude,
            'altitude=%s' % self.altitude,
        ])
        return f'reg.udral.physics.kinematics.geodetic.Point.0.1({_o_0_})'

    _EXTENT_BYTES_ = 24

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{_)kTW{4y5I!f#$(=yRg*$Oe3rV4d^a}Js+5n|pl12mpYL%L`y~(cXV;g&&o**H?L#t3(>Pp#4`~-dikMxbVs&D*)'
        'iv9!M+8KMD!=+Il+aBrYo81}D&dlz9JGZ-j9viF`zkDKI^HV>tos=bl2I3}l17<s3)QqE4NT%~`i!#YPnI-J<TFmr@p1PxN>B+p|'
        'gtQ6zqX}EFGe4n$9rLwRc&YuZ2w9U#6jxZ}Gmz|sNQ6@7z0N92QW1rk*Ych#M&8h*M(RK4J31e5sFaCtGs#lD1nX=O;ii?&8|MWJ'
        '{B~shj!z|ZB!;`y=W!yMLW)(e=sO=oR6d{Ffa4131T0*UT$34a>Csd=O-M%b(R_TN`W!#AXF)fID$L`1eM#q|PAX~W)5L$)(K`5P'
        '(v?ui%*Tb76Y5FGKZUxSH!}G6@lNgE`aS)#_!XORNoOu^<h=pxWEpUm<3}FE`gKBmLBl09*ilxDkMMCL?IAOKFF(j9*15$G{kM|o'
        '3!-qP%!VJ?Dv=H&HF7JXs~!#QRM;8pnqBUreO35u(W3!PH1FYkq)uvhcKP6v{-4#O(PWY(Sc@7=(0t^X+vm7z<rTlB`5AsHg-hYH'
        'IAI=@%-47GA!k{%nD4|<A|2uD`Fz+(qb%_lC<5lh6pnn}gAfQ8j{5>IN^1dUH{goZkHdlD5mHD;EWpr<LYYJXoG;dbph61bzBqFO'
        ';W@xDS%B-duQpto?s9v;K?)AKaEoBlT(*3qy-oJCeZoc>&=POwh{I_L@g*#j$P25&WBM*X!e`)!y8(DUT(L&`_JW~&ajf&fPldc#'
        'j2B^O_#^LhqFCqFR!-8jrW-+85Xl^CM!-pU^S_K)LS>Y+S*Y9bxBzD3-{jjDsPBt#<s~ETp>{qCAkDQGwcufu1{u>o=}9u9QWy9)'
        'E*)voo4Jr~Q-nxxAkY>HJxFp;YxGU(_+3qr4uhSDbw#?&xPjQENVmZrqwh8PJ~Qq&`T@i~MF!1y8{(iMLx{bKY&Y{e%=g2H+Z5S}'
        '*ssV4Vvi!D#%|2`A4eQjWEbL2MRp_ZP-G9{kRp4{I{S>D{bs!bh~0`DH2x+KI~1|Z`mZ2PDDo=eK}8NB9#G^p#QloAj<`>e!-#to'
        'IfA%Hkx9heicBHyQsfQ9aYc?Ijwy1?#QP@Vh$6O$`#9pTA}37z(}>#@dCTPSwyDQECZBf^2NZeF<n_L(?@5#2DO0c0CeIHL8;X2r'
        '^8E<0Q<0BN-e*ibXH5PV%5y`m8RQ0A2G<SVGkD+N1A~tYJ~sHo;L{T4dh15mT?vzwaIz9ERKm4N;FZv-g!M|eR|)qk;Xx%ls)Wat'
        '@T3x+8X<%CnYCgX7EOtnb5pl`2WcQTUk-Uz-~;b5%VqLA#zISSW(5(jjn!l{v{FW`fUUB?nw(p_IAuXIP?#(iCNVZcR<vA9(NMB5'
        'q_&0ph&_c>tz=O*f*~4#6B`(s@lWv1ALhgSIG^Ib@#&1u-sNZK`8j@Jl7G&>;Dle~b9_GU1kQxssOZd)hRfbe=l$*O45+s1&vZUi'
        'bZEen(`}~YSAZ4sUp_NNR?!neZBAQNQ*g}Md{K`TNmjAj{g)x^DDhchiPZ9Vlwy@43zqhHnRp8ng$3|YRgL*`XD#T9n#MsYZnDB}'
        'K-Z$o)C@jLtELp4vl|%{6?~(ES(?D(1+O|r3&q0*P4lb#tAY{v62HDloNQCN{tTIp%|;=<apB*xa^6>xGQ1twp8kWk-^)e+*ve9r'
        '`k>-x9+Enowg_5=82&dv_v<`NylBT#G`bB&x7$V`Qu@o&v^0JQvkzZ3etsIyy8RcT%=26z3;+N'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
