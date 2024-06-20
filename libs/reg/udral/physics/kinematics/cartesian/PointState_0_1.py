# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PointState.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.676242 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PointState
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian
import uavcan.si.unit.velocity

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointState_0_1:
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
                 position: None | reg.udral.physics.kinematics.cartesian.Point_0_1 = None,
                 velocity: None | uavcan.si.unit.velocity.Vector3_1_0 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PointState.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param position: reg.udral.physics.kinematics.cartesian.Point.0.1 position
        :param velocity: uavcan.si.unit.velocity.Vector3.1.0 velocity
        """
        self._position: reg.udral.physics.kinematics.cartesian.Point_0_1
        self._velocity: uavcan.si.unit.velocity.Vector3_1_0

        if position is None:
            self.position = reg.udral.physics.kinematics.cartesian.Point_0_1()
        elif isinstance(position, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self.position = position
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.cartesian.Point_0_1 '
                             f'got {type(position).__name__}')

        if velocity is None:
            self.velocity = uavcan.si.unit.velocity.Vector3_1_0()
        elif isinstance(velocity, uavcan.si.unit.velocity.Vector3_1_0):
            self.velocity = velocity
        else:
            raise ValueError(f'velocity: expected uavcan.si.unit.velocity.Vector3_1_0 '
                             f'got {type(velocity).__name__}')

    @property
    def position(self) -> reg.udral.physics.kinematics.cartesian.Point_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Point.0.1 position
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._position

    @position.setter
    def position(self, x: reg.udral.physics.kinematics.cartesian.Point_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self._position = x
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.cartesian.Point_0_1 got {type(x).__name__}')

    @property
    def velocity(self) -> uavcan.si.unit.velocity.Vector3_1_0:
        """
        uavcan.si.unit.velocity.Vector3.1.0 velocity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity

    @velocity.setter
    def velocity(self, x: uavcan.si.unit.velocity.Vector3_1_0) -> None:
        if isinstance(x, uavcan.si.unit.velocity.Vector3_1_0):
            self._velocity = x
        else:
            raise ValueError(f'velocity: expected uavcan.si.unit.velocity.Vector3_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.position._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.velocity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 288 <= (_ser_.current_bit_length - _base_offset_) <= 288, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PointState.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> PointState_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "position"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "velocity"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.velocity.Vector3_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointState_0_1(
            position=_f0_,
            velocity=_f1_)
        _des_.pad_to_alignment(8)
        assert 288 <= (_des_.consumed_bit_length - _base_offset_) <= 288, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PointState.0.1'
        assert isinstance(self, PointState_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'position=%s' % self.position,
            'velocity=%s' % self.velocity,
        ])
        return f'reg.udral.physics.kinematics.cartesian.PointState.0.1({_o_0_})'

    _EXTENT_BYTES_ = 36

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`upTW{RP6~}jVS*>K**3FJ;yEg4OvaHCo-Q4WNZrwUiT}-VCcH;OYAZN*uhYFV@NUop_U?6^IAqNCHfTuvdK$E=n'
        'DX3Glg?o4VQlLNqe}wcK_^myMdq!HVB{X@;LnJ`_A999ghMfJKbA}%b{Ng{;mGZARmbCrM4{awCX~4taeclL#?RarBiL)RVy4ZU&'
        'Pg`EzO2u34MCb?l^gVr7&lZDD#GBB5J{5QDmY?#_PGma^yv%+th(wd;XnH)&MHcYLUW$V#znOFNS$9@NngwyBWu+LpMfL;DDy;f5'
        'eNPvA9G>TC&}hNU`dt`phk0)F(#7CHAVPn0ej|?0bME9gY1!AgC<lxAuQFXNhvcxClpK9m%Q12^+2!(hi?4ccOBUFzD9G(lM0av&'
        'zZ3Z4mhkd8eW~N8$|}$LDGu-OWNFIVx|muB)`b7#(&P8>($+=T>xfV^MU;1*bEnsoq(L*tgH`A;yb#7b-|A(L(+F~>Gi}YTz^n6k'
        'mOIVZhgUaO99%ND<8Ag;XuFP0xL!ZiH(-)Zmh;Hxso(8r9sD%;9e5)x9|vAextGH_XR!VYWP^_n?^V98zo-8#|H}2fp<9h&7#=*~'
        'UXZsn>n{eJMhKIgG4FKq+2Hl&z2~|Z{Xvj-R_Z34(%UWiojB2jwUd*q-E72R;OS!Wx@g9*V)$Nul8BVUFK2U&YK|uZ_<hSai-{W|'
        '5qYqEzdq+Zn7jND^xMDK3PYZ@dpm)zRUWp4{<)rIS5(%3Cm(Q{L8RFuH24}CL%9B}kfT>t#jX{_`bhgp2S^7|`xL9u`4DQqVs$zn'
        'rt=Z%w+D4lu~BN@i#np%KGOZDql%4D`#ANVpzD+5XNt}bkpF|IV~Rb8T32kE?*A6*xMGLM|6%HX1a(@mZ=+5qc9i@bL#-)h(f!9!'
        '4=Z*8^`K(UlfRSH{{_?`#b#(;r%+ESHj8R0b{h4FVskX!i>OnI&C`6(kRO}oeHL{<v2!&3dDJtCeFt?;v6oO!DfTjr^9t&5#a=}{'
        's@Q8Z-wQO}Mbra|y-v^h2I_vrF44G`QHK@#E<N}6=>1%w@vottQ|va)SEAllYz_6AV(X|E6#EEuR<TcM+=ui$k5L~f_Js5c(x)B0'
        'UayidZH!rCTrkEpW85}|G{%}S){XIzF+MfMLt{KP#uH<FVT`9_v><eewS-4yUZQIa1O>wVU{mBG)j*0L1GW_i9K4w9N?1;#-N}u2'
        'wfwa_kwJX*MUn~+a-Xm77yF!L4C+o2r@0gOda)RHvbdFc0vbZ$Bpjk=F@zEZ4Tzjekc!uq@ah8~ym}VKmNDkuz9fK-UL56V970$X'
        'YcR8jgLyb<H6W@uknMnB7<V%pLP)E1G8Q<<z`+1!Ex1T=yO`?AT=seUoQ;u7=NRcH9mzA8V2UXRa?EPr34LEal%LDX@=6(9<W;#q'
        '$*l}ROWgN^=*}~d3R-^%g+S72)~pUM_igq_-h%&kc4N+N%=xCp9Qj#qpy_03qzgif{LNjx@>;c0k%uz*+xzl&i}LsK53}-*@=x;5'
        '@-OnQ@^3{y;0~2=S>9p<=@huS7}+dwA)IU!xw_a_mbrlV`Ax{>KLO}s?yBi!d2yTqqYy<hD_*v^mEcWQ5Lp=%OTyOMv;Xf6>tFK8'
        'F5bI%@8Z1$?|QkzE;qp?;oI&lkM-;=S49}({>1+OJ4-o3)@eCU)>&rBbMj^R%DQ}2Ui@%;%WkN9CnPVy9%5Un8Ci?vCS$47;b!MI'
        'Sw7g?%mv8ZuK;<q2lBxl$ZG_7jUcc0Kt4#2j}qjy9?16)<TZl4N|28c<f8<6ogg3Rf&2hLK0%Q0C&)($@?nC!Mv(XSKz@`UKSGcn'
        'BFLu+@`D8V6hS^gkdG1M`v~$;f_#J^uM^}of_#7=@9Tm5EJ1D)<Yx%-d4l{!f_#o3KTVL&66B`{@)?5s1%mt}LH;~Jeu5xBPLNv!'
        '`7}XZC&*ob+$G3eg4`v@U4q;t$X$ZmCCFWZ+%=H926ERx?i$El1G#G;cMasOf!sBay9RRCK<*mIT?4smAa@Pqu7TV&kh`0ZkCmGR'
        '2Z~=Pm!VMix1{r<eU-|}uOO%Il+op5`FHt`qHeI)#n`rmd6~0!D#AAs@yh2|KA2p*i|H<=yO>fg-T<tFr$9VsS3X8w##h!6(@(%|'
        '?SSdZMQB`k9S?8d;SwG$!=aem{OrA5mHo@Nq_8%Mb1TDsT{ZT+#i8U*pimILmB&^tdERMm#D06;3Np(Vt8w7t#Wc>#Z--ErFUM)K'
        'wCxcXAQf;f=HYH(ndih?vqX5oasaNOl*h)-zP_v8x0X}h{1OFz_lEz#)i}a09nrQQGVv2De#eA?@VoxDQR>a^D7CR;ke@BK8Y?rf'
        '6e5F$>sD3X!h>ltcRbU8OKkrSiDw&b^cVmD'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)