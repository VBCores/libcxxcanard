# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/State.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.711067 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.State
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

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class State_0_1:
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
                 pose:  None | reg.udral.physics.kinematics.cartesian.Pose_0_1 = None,
                 twist: None | reg.udral.physics.kinematics.cartesian.Twist_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.State.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param pose:  reg.udral.physics.kinematics.cartesian.Pose.0.1 pose
        :param twist: reg.udral.physics.kinematics.cartesian.Twist.0.1 twist
        """
        self._pose:  reg.udral.physics.kinematics.cartesian.Pose_0_1
        self._twist: reg.udral.physics.kinematics.cartesian.Twist_0_1

        if pose is None:
            self.pose = reg.udral.physics.kinematics.cartesian.Pose_0_1()
        elif isinstance(pose, reg.udral.physics.kinematics.cartesian.Pose_0_1):
            self.pose = pose
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.cartesian.Pose_0_1 '
                             f'got {type(pose).__name__}')

        if twist is None:
            self.twist = reg.udral.physics.kinematics.cartesian.Twist_0_1()
        elif isinstance(twist, reg.udral.physics.kinematics.cartesian.Twist_0_1):
            self.twist = twist
        else:
            raise ValueError(f'twist: expected reg.udral.physics.kinematics.cartesian.Twist_0_1 '
                             f'got {type(twist).__name__}')

    @property
    def pose(self) -> reg.udral.physics.kinematics.cartesian.Pose_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Pose.0.1 pose
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pose

    @pose.setter
    def pose(self, x: reg.udral.physics.kinematics.cartesian.Pose_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Pose_0_1):
            self._pose = x
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.cartesian.Pose_0_1 got {type(x).__name__}')

    @property
    def twist(self) -> reg.udral.physics.kinematics.cartesian.Twist_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Twist.0.1 twist
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._twist

    @twist.setter
    def twist(self, x: reg.udral.physics.kinematics.cartesian.Twist_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Twist_0_1):
            self._twist = x
        else:
            raise ValueError(f'twist: expected reg.udral.physics.kinematics.cartesian.Twist_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.pose._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.twist._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 512 <= (_ser_.current_bit_length - _base_offset_) <= 512, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.State.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> State_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "pose"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Pose_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "twist"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.Twist_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = State_0_1(
            pose=_f0_,
            twist=_f1_)
        _des_.pad_to_alignment(8)
        assert 512 <= (_des_.consumed_bit_length - _base_offset_) <= 512, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.State.0.1'
        assert isinstance(self, State_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'pose=%s' % self.pose,
            'twist=%s' % self.twist,
        ])
        return f'reg.udral.physics.kinematics.cartesian.State.0.1({_o_0_})'

    _EXTENT_BYTES_ = 64

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`us+mGB<9mi+qw%$uNvztw_-K2?gX)?J@E-iE^O`9}n6yzjLo2o=YsqGnib3C0Hk8Dr6TT#h<0Hu{tE!9Atka(+v'
        'fG0#>swNenQtp)y6#|LJ{0Vu3-?6`EX4lyv+k%8pJ<`taXZ!g0*q+b#_dA#Mi{Jg`$z1#ic6OHy*J#yL*K{nsWxb}?TV_pd*zK<E'
        'TAmpN8?Jaxui^C^^Tp+^8NCx7cq4i}ss<&sqqph!VaL2)>lu#Ts&(12Yc<^3D^|yB>mGL-y5pIyrFUvqJe^l3sW(i=wd_vBa>3|J'
        '@ZX7)oHFw5=#40tP<799ta^{mi>}dyhBUEXDhf*HEVE?{nl`Q)x~HoiZ!gOyJ6S0>w9b}Zwp}`Jl#Pitu}NwNtDvGyE2=!a?kcU0'
        'cVC@rR=KOE-)PV&u2t)GEU(rwJJ&r{`?_VAFPRO`b{<XY8Bucg*Ar|T@~|97Uyg#=bJmh+T!?Et&3CPSr5jYUWwy<Zmpr;*PrmC|'
        'ZOgN6P>Hc~EnD|i*D|5jEl*9F9Vw^iZ8UV(Q`@#dPxVBw<+3=PpH@3V$1d_i{3r0O=mlz|>Uw&|&>drCMK`IQwtk(SNYCIGUUc+^'
        'M?W2xep2V)Qyp);k^5hL?)@|V#P9cos8<ih=*GKx!}69Rr4SU=dW#ynPdwAXz0u?K(%Vrm`HbZyZ|Vwd;^_tj)$T@tJggFTxm~wg'
        'RwD{FT{PP^y)ph=p6i;9PQRSNJ1VOUW)U*%LNN1!*)=_D?Q(hb6>2+sp2}^!)N8eLXE|Mn>bjw~dS>)?R8>xeZk_JDsJ5+6q}=9?'
        'zQmnT{{DL{o!6?2@S?d;$-@?4i?Ahb^Py74_9(Z7P?4}bhV5~bo8Yz-Dw8<Af!py=nS$NO?PRD_aC{o&XRv=0>Y2s%X4Joh+e)Zx'
        '<yH!nIh_9xx6`3AkNUTv{B~~VLgis@XF_EM>f6a}IaFkvzl+;#p|YFXEupdp_3cIZN4Omgm3?T}es1@MN|jqVR1R>vJyZ_jdWX23'
        '4VA-a?-A5fL%WZ1TMU(Bxc+f&kA%tzZV!gaqulNfmB(<MFLApoRKCpZj!=0V?Onk2zQXP1P<aCP`BiQ=hRTz;?n!RPLggvk_tSVj'
        'r*QrA+#U;+t7tFd_G+jsaeF>gZgRU2Dz~_;hRVCR?t8eOkGQ=ZDxbpMg}s;9i_!?3IpI`=vml)F!nrCOCY&YV+!W3&;k+xH_k{D2'
        'a6T2zUE$n=(<A9Jm%4f<4t3a9=b(_>m)fRhIuVg#*o1A4ghLNDt%!kYeL0D=uSe_ycF-k#HO#JKHYl7L(VM}Py2wRc?b?o~T1Ip!'
        'm{wi8=QK<@&@$DoPU;zqa?`Tvq?{Dqtfk9*?>j{J$WgjBvw0-XcP%Q|usfb(w@6maC2CnmCwE)7S0`0bDcTXkblpLKB}pqM5sNBt'
        'se&SpTC@|o9n7wXT(#r1V>PZ^k;j#Olgf0L8tCwlLow!t)i9$s*==@*J<HC=>cSLu3BfHEq072qSe@(lDHR=kj&h4`ayU{Xdbrn='
        '+w5ifQ!~xUH0O(^Iqdzk&?Hfs(?t@)K72iDK0T7lvE45F#hdJxm)Nh^udD21_8azF_B-}__J^QAxKnZ+r?*@|k_0yj#s?`b$w@!S'
        'je@B-%_YQ-4<KiMA)teUXGAHvVcQNdN-E;Y_M)uIU4D{mb!3;4C9@W-&Hmr}-e1{2GQ2aqGrU*fEyexyxL+L;zGmNYXR2?hcdk>1'
        '?)je11ATn%(4Hl$!8^_#gZH>1vjz4fJ9(2m#ZJF9y{b2~vM0pOD#f*_z5?$hD)2nJniTj(@|%or?3&^e<o>^bJfDKR0Lb%zJfDI*'
        '56C4zJ_^VsKt2J;^MG7RK|Th^^MHH`kV}9(56EW#`368P0rCPMp9AExfV=|8Cjq$x$crh+9|q*}fP5<;p9SR8fP4y&PXKZWke2{?'
        '9*`dd<W)ev50LK#<hud649Ir?^6h|p9+1xg@-2XT7Ld;X@(LiI0_2l`d>oKVfV>RIi-0_zf_wpxR{{APAeR8S56FE$?gMfkko$n#'
        '2jo5=_XXs>fZP|5`vP)bK<*33eF3>IAom62zJS~pkoy91UqJ2)$bA91FCg~?<o*Ei;;T!`udNE<`|`P5^XC-DhedJrNA@T7Nl=PW'
        'r<8jD`|4yoj?=>u?|$%Y-r*^Oh`$+{8JZcI37QkOV^KF&UlD>$PH46H6OPP$GvuWHl>FWhQk$pgVDlONb%uYP<zLUzSFnMPNUxDr'
        'KM>bdedo<*><%9^=&U&=$VV&rkRbKN`KbGv@LyO7f0le_$@dpN`EJ&TYSSeiE}j};FY~YUhr?Vd9F|f<lt4rdM2w`up#&l(K}0D<'
        '#1x2_0udDukpmGW5HSfNHmAbjEQpXm#8wb72_i;7#4LyyPZ6;dL`;E*5{QsN#2kpIfCvdh<UqtO5HSxTHi3vq5K#gVhe5=?R5+Xm'
        '5wjp-3PeaCA`c=?fQTa?q6#ARfQTI+;vo<*3nDgxh;a~6N)aK0hy@TKfr!f>;uwgifQVZl;wFe#0uc;ETm=#51rZB^h^ioBP7oo1'
        '2>L|=iP&R(Z>jIy?0dKR-n)J8y}tKR-}|)h-R*n#gqP3}dvy^kGB`3gGB{Fjh(296UT!da&}O}B3|@TIa=mq~TSyNC-7s4=pQx@q'
        'c!|M(I1p5L&_GaO*g%j*38(fM63&rS!kJc(G8Ci?1(8w-XDOv1<&=U<Ktak-kP#?I1qw0=1(Bd2#Z<z%845B31=*NVkTEDo846NJ'
        'DaZ~e$aW~mJQQRO3bF+XG7ANnfr3<^AX89~NhruT6hwl8l%XI+C`dk)a2|z%)Sw_opdg2#AcvqJ2caMbQVOyk3bGFh@(2`UFBD`C'
        '6l6CPWET`fhJwsNK_n=M1_jZeAQ}`zgMw&K5Df~VK|wSqhz14Ggo0>7K{TNtnotl;B%GQ^I5m-QY9is(M8c_wgi{j<rzR3kO(dL}'
        'NH{f-aB3pq)I`Fm4Md|7&l;=Lhf`g%VRwvGgF>f^)N}l#@W4SKNnjrZl{IH**EuNkx5A2kVTNgjX@+TnX}Lv#T6YM}VE2XCl?8Hq'
        '!qa1>T(^y7dC}3^W-S_$0PMei)~46e9W@KunHpqj@c*L*(~fRXqCPBY?=4Z({#o&XQM;1nKWd((vpz$-{-Bt}>x|Hh(EA7-1zJ2{'
        'pFN%UgNUuy?VcA0?RdqdtS==?m{x~zxoR$Xj@6-#`T-u&F$?q~o|At}iE{Hhobw+SKhH$aRNTj3Yk}3ti#DItNmf)j)^*EBnnYQ~'
        'qi2(qRkC3&QVwFQm3gdt9;x|*d@dJnG=E6mu$iK-WeSriOr|g^6sCEogqfmj<}{l*&1O!sbp#m=84c+*`d%`JvvT>+9X_}^-F&}H'
        'N#KWt&y_XC|9ZPt*7)ahmg9OyY{xJixj(5SyS#joN{S>h&LE$V`COH(cMLghXl?vO$|K`_Np9)V8H4rxvb*ehW?S|gz2h$0PCH(B'
        'L@B4;juX)2AAgWFdv?4pUW0_JG_F0qkZifs0<&Q)T7&#`MNzprNM;ZG_p{mW=LgyB%BgJj{v`_R-xGoTVlGdI=t~^xpOZeoUw7?a'
        'kH6m0hdlrQ'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
