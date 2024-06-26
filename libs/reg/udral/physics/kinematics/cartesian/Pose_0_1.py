# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/Pose.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.695576 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.Pose
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
import uavcan.si.unit.angle

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Pose_0_1:
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
                 position:    None | reg.udral.physics.kinematics.cartesian.Point_0_1 = None,
                 orientation: None | uavcan.si.unit.angle.Quaternion_1_0 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.Pose.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param position:    reg.udral.physics.kinematics.cartesian.Point.0.1 position
        :param orientation: uavcan.si.unit.angle.Quaternion.1.0 orientation
        """
        self._position:    reg.udral.physics.kinematics.cartesian.Point_0_1
        self._orientation: uavcan.si.unit.angle.Quaternion_1_0

        if position is None:
            self.position = reg.udral.physics.kinematics.cartesian.Point_0_1()
        elif isinstance(position, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self.position = position
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.cartesian.Point_0_1 '
                             f'got {type(position).__name__}')

        if orientation is None:
            self.orientation = uavcan.si.unit.angle.Quaternion_1_0()
        elif isinstance(orientation, uavcan.si.unit.angle.Quaternion_1_0):
            self.orientation = orientation
        else:
            raise ValueError(f'orientation: expected uavcan.si.unit.angle.Quaternion_1_0 '
                             f'got {type(orientation).__name__}')

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
    def orientation(self) -> uavcan.si.unit.angle.Quaternion_1_0:
        """
        uavcan.si.unit.angle.Quaternion.1.0 orientation
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._orientation

    @orientation.setter
    def orientation(self, x: uavcan.si.unit.angle.Quaternion_1_0) -> None:
        if isinstance(x, uavcan.si.unit.angle.Quaternion_1_0):
            self._orientation = x
        else:
            raise ValueError(f'orientation: expected uavcan.si.unit.angle.Quaternion_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.position._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.orientation._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 320 <= (_ser_.current_bit_length - _base_offset_) <= 320, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.Pose.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Pose_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "position"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "orientation"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.angle.Quaternion_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Pose_0_1(
            position=_f0_,
            orientation=_f1_)
        _des_.pad_to_alignment(8)
        assert 320 <= (_des_.consumed_bit_length - _base_offset_) <= 320, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.Pose.0.1'
        assert isinstance(self, Pose_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'position=%s' % self.position,
            'orientation=%s' % self.orientation,
        ])
        return f'reg.udral.physics.kinematics.cartesian.Pose.0.1({_o_0_})'

    _EXTENT_BYTES_ = 40

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`upTW=Ic7RSfqu|2-x8^i$u153={kOo375Fqg`k(a0z$AN_K618fk3s;+-?p9wMPb8$~A(25Xr6ej+K0!8b`-B!&'
        'yDRq2?#oImt;9#*Bk;C+&de!a20PieeTXf&|EIgEPF;F_=Tvo8`r4W*wEpsgVbh5n&$43?x!iL<=QU4Qc0Fi>LF^_%=fhW%D6J=H'
        'BtB|}Lf_NJZtGjRn)lc~Z$SAgkyx}+C*qzJ%4Y1=W9z2tiv~~7tn(-lvCDmHA&8-N*<Kb=>;}G;g}m<?+4nRnu&yulZJiI=JV_$A'
        'mO?ZADfF|=2-j-qyl2i8p0hr(0o&mTw-X$$EVduYp8WX#JW$t9wCt1pW>9kIQ!Piy(ZmLqhf=;=hbFOWrM{b3p70kFX?@~4;+m)@'
        'L3Fz9r;8Py_ml72W@b^un>wGIb614(i<ZZq;-k&WKWqz6G=!hD=egZ7g^}BE6L%SE^v`(#Pd0lQv}<l+w}-9SEG%7}$BEqt99X)U'
        'e9wYuj?Ju#P<9!M@O^!uufQPfIN`p-BWI(dRq)f`i?AZ8gB{<9cs+sl9K-vcBO83&y<PZ!{XP3n>#y~GujsUv_rt_PUU!qGX5D$o'
        'u6Z!nX|ty5bA#ngI`4Hp^fNbUzp1NmORJlA+d-)F%63lTW}_B(Ze8aSmqjChH-_u-K`0^)znt}V)N9wJ3%_sqUOs+Bgd%abu2-~g'
        '!r0~eP;b|K>UlhBc2)vk%iK$a{z_Nbtcq(e^OD_gea#-B!B^1e!}p(h9KEtGtXfd4NZL(WBJDvfD%MN)eW=}vmFd2p?gyyeAZm|d'
        'LsUMDI-uAH=`PeE#YU-ojOvfm^9k}ZN%y<S{~pv)#a=)yD>g;#Uql^KY%lrWNA>rkPAT>h>bPPD$lpQKUd1ZZ{t)Uu#SWwHQS2w='
        '?+Dd@8MRNbX&Tp2)FX;jQ7eiaL*1{~4E6U4>ZD@FX}qtJAB)C)0=1;rN$UR;>Z^*qhB~9zY1E^Ny-xkSfqF=>H&G8L_7;uz4E1*w'
        'b+=+~(>%|i?o#YL^?L!eU$J*+-tW@-%u@fCP){m$oyIFsuPe5KdP%WW)H8~GgIZPWJL>lV&F3-dBgLMOJ|%tD*30ECGNz1CHO3iZ'
        'Tr$RWV@PAH7-Q8K-x%XNV>~d%V`Drq##3WFBO`^-C00W2xAGD_t05>5?t2;{5s?N`oB*&bK;Yo{#D;`r*P89DcuUJ)%fm6mS4V`A'
        'sPjZP`c6J#-@u@5he4FsuA}GkF*^>@s4k$u6L!cUdggs7o?C;+2}#pkS-_|Ffbgyp(6<aQ>lQ;7D%Jx(i2@J8s#t-M`5erBVOoQz'
        'VnenAhN0i}YzQH(x1F)TK@1K`n6=;`#qE4@L*}whStl)wTspx>KVeHA!vG^pIgn$P-MY|s<OBIoUXZh`=prx5IZAG=Ahf_8$MqMV'
        'i&RkhbJz%k?PAT!u(%(yNAeo{f3g#Ec4E$tE#}Dkoq?vErI9WOG4eOJ^wL{hg@W80%irFSznho8mw%|rKgvJJKg++!zskSm-GDpn'
        'gj?HNj3Dg|uFeP6x3~~a);761A8BoK0r6AokjsAp(D}?oQ>#)Bf(RIeC=yqK8x>v&u~EhKD=}=Agr&D;|KDrYzvPo0ym#>4!Fv<l'
        '<<{A{bqH<|zUA5SV8_{#`-^a(`!MC0=v!^KJz2_WvX05)WSw9Yc~ZVE-&mDz%CmRJHl2nxo`mFiR@$0sM%Fx3cwa8GD_m{=CR-Ex'
        'm}LNY_C1gnJ0R~S$cqGdu><lVL0%@v`v~$fK|V;37YXum2ju+(d66I=A;`-Fd66I=C&-5h@-ji*O^{C!<dX#XC_z3%ke3PaQU~NO'
        '5#)Ob@)rp5NrHTgARi&f2MO{rLEb}<7YXtig1kzQPZQ)v2=c=Od4(W9K#=bz$oCTDQv~@Qf_#!7A1BC13Gxwwe25?)Ajr!Ec`rd;'
        'BFKv!ke?yQs|5KJL0%@vGlD!L$TNaGBgiv?JR`_6f;=;jX9n`jK%N=MGXr^MAkPfsnSnerkY@(+%s`$Q$TI_ZW+2ZD<e7myGmvNN'
        'ke5DNX@0&bg&!yu3QNC&Jic8PmyhM&<v;SC7V5C&UWa}2X1tZBx7&EHCEuloxMeW;cL&WKG<VQ!qd6EvE*xX|h7>H2(CX5+h|Jj1'
        'Dw6t3u+wcwT{;VeOK;=l9A3`j<pNytVf@a$#kTqfaou!w-hDCf@uPvi<u^h6T8W<o;Vh1y$hU<5y^Zj%ZNBCG`Lwn)4bu}b6kML|'
        'lGpHJicE{=3UKAD{{kbw?BqEZ000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
