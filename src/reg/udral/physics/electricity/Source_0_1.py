# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/electricity/Source.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.549899 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.electricity.Source
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.electricity
import uavcan.si.unit.energy

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Source_0_1:
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
                 power:       None | reg.udral.physics.electricity.Power_0_1 = None,
                 energy:      None | uavcan.si.unit.energy.Scalar_1_0 = None,
                 full_energy: None | uavcan.si.unit.energy.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.electricity.Source.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param power:       reg.udral.physics.electricity.Power.0.1 power
        :param energy:      uavcan.si.unit.energy.Scalar.1.0 energy
        :param full_energy: uavcan.si.unit.energy.Scalar.1.0 full_energy
        """
        self._power:       reg.udral.physics.electricity.Power_0_1
        self._energy:      uavcan.si.unit.energy.Scalar_1_0
        self._full_energy: uavcan.si.unit.energy.Scalar_1_0

        if power is None:
            self.power = reg.udral.physics.electricity.Power_0_1()
        elif isinstance(power, reg.udral.physics.electricity.Power_0_1):
            self.power = power
        else:
            raise ValueError(f'power: expected reg.udral.physics.electricity.Power_0_1 '
                             f'got {type(power).__name__}')

        if energy is None:
            self.energy = uavcan.si.unit.energy.Scalar_1_0()
        elif isinstance(energy, uavcan.si.unit.energy.Scalar_1_0):
            self.energy = energy
        else:
            raise ValueError(f'energy: expected uavcan.si.unit.energy.Scalar_1_0 '
                             f'got {type(energy).__name__}')

        if full_energy is None:
            self.full_energy = uavcan.si.unit.energy.Scalar_1_0()
        elif isinstance(full_energy, uavcan.si.unit.energy.Scalar_1_0):
            self.full_energy = full_energy
        else:
            raise ValueError(f'full_energy: expected uavcan.si.unit.energy.Scalar_1_0 '
                             f'got {type(full_energy).__name__}')

    @property
    def power(self) -> reg.udral.physics.electricity.Power_0_1:
        """
        reg.udral.physics.electricity.Power.0.1 power
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power

    @power.setter
    def power(self, x: reg.udral.physics.electricity.Power_0_1) -> None:
        if isinstance(x, reg.udral.physics.electricity.Power_0_1):
            self._power = x
        else:
            raise ValueError(f'power: expected reg.udral.physics.electricity.Power_0_1 got {type(x).__name__}')

    @property
    def energy(self) -> uavcan.si.unit.energy.Scalar_1_0:
        """
        uavcan.si.unit.energy.Scalar.1.0 energy
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._energy

    @energy.setter
    def energy(self, x: uavcan.si.unit.energy.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.energy.Scalar_1_0):
            self._energy = x
        else:
            raise ValueError(f'energy: expected uavcan.si.unit.energy.Scalar_1_0 got {type(x).__name__}')

    @property
    def full_energy(self) -> uavcan.si.unit.energy.Scalar_1_0:
        """
        uavcan.si.unit.energy.Scalar.1.0 full_energy
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._full_energy

    @full_energy.setter
    def full_energy(self, x: uavcan.si.unit.energy.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.energy.Scalar_1_0):
            self._full_energy = x
        else:
            raise ValueError(f'full_energy: expected uavcan.si.unit.energy.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.power._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.energy._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.full_energy._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
            'Bad serialization of reg.udral.physics.electricity.Source.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Source_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "power"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.electricity.Power_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "energy"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.energy.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "full_energy"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.energy.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Source_0_1(
            power=_f0_,
            energy=_f1_,
            full_energy=_f2_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
            'Bad deserialization of reg.udral.physics.electricity.Source.0.1'
        assert isinstance(self, Source_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'power=%s' % self.power,
            'energy=%s' % self.energy,
            'full_energy=%s' % self.full_energy,
        ])
        return f'reg.udral.physics.electricity.Source.0.1({_o_0_})'

    _EXTENT_BYTES_ = 16

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{^vFTaO$^6&}Z4uRRWlEpw5$h!RBBEUbGIA;nxJI~z8RCfTgKCK#cpQ`22Dr*L&wQ&l~?gNWn^fnwAmMs6hDka*w)'
        'A)a_b;(<qmqWmNCRdx5w?5@WKDXg?RJ=Im`@}2K|r}o~N-+k_4FZ@(rE@r7sRTNucBv<lhe56DaCps&%l}^;vr}mvG6IU8>dsc}0'
        'VZHHw{a!t&*5aIJc>jVClc-D$S5ZMTD-#<DB@$<3BHb+7*QH6Y?OZ$+#!8*n)T`FtZl534!`|@Juj=>f>O#yN4vk7DZ2b-#tO#ws'
        'tFG2|q)_Q1q<)-o$7AQ?q-UB%TC2YL<OuilfiN|#)A=qIdKUiaVr$^?lBp{tpC&wytc=QBy1AV=DUA`ii}n+)cx&y{u-92z7+aNA'
        'VPqzqoFc9BJ4$nR6zvP~NV-^weB!7cGNhVt>*7qONcDy4vwPife=OR@yEpwSkMA$*TXps6*gBr4+@#BfK7gH!PmoEOddFkK6NkE3'
        ')N7}GhK*le>Mj2~dh{p&b*nB%z~n5?3Sn^kOq}YZu6kJJ)#asf#-mw7miKCUnZ9C?O)3f_67ED=->;sF$MR65aiNWiWm@l6mtq@u'
        'gBMD~1xKvay8lpeggE!W&BHyv`ViQh+JbM=o{Y~F5*rhpJEIkn5Qk2foa6BeMLAL^6u3|-?{~o!WP7%$D-2i|IOA(uR~L_0x2~RV'
        '>KnZjy%_l_*3N@_IVNrqrQhSrI+bAjeY!^91STT|`&YW6FTlq}cl>)@J^PAuZ-npr_}Z4gIvwkxuGlIgc9xAal0zhKicEu2zHo1$'
        'D%@$aAko=4A&G{ex2xy(c$&(5a$*zx*uUK^71Ep?e+vs!u1ZmVSPzEmfgPc(i^fnrJXem8ZYFcjPdxBL|FG^k3dC`Gc+MZ|J+NS%'
        'I4pP`Bw)83*-;?UdIz&d4l9pqz%LzZz^PV_PsG#vj;^#%8$(84qlmUXpcm;IPp0-6Z@vwO)3-q1pVQRRcka`7cj<d{eLy$p722j('
        '>HD-puhC6<y;^TWs%hxSLA!wn^cLL;0niWV&K&7?=1;tNnRdX^*yBkP1WWjpOX!hWf^6<A#3+1>1Ip<0R8d~82(&tlCV+YdN%Vcy'
        'h$19-Nfztsxgd-n`b!I{hivY=e5%)bb(?9!Zfr9pbHTcUtng>pPfMOV$dRxSdrjmZky5iw=18!yR!Sd$Fs!XMvvQI%wCogLKnTW*'
        'LgD1M`+df)GT-W6*XG;DIBwb4=q%Vf=Gm4wJ!83W2in|aPKQm<)07QFG>JADhX;%^PwS1S@$vfjsHyI>w2RZyS)s;_7m+spIcrp^'
        'Gd+Uj2{YShGVKC}m0V1?Pa>+H#)CUcUHF-8oqLJQAKT8=`KFuU!;j0yTKmyS8U^;yFNF20*RgtivD$4uy4+H2t!U=twdzl|wd0D('
        '+>aF3z!P3Z{T0=cd0U7MueMk+zY8Xy47)8rtE$|dYpp!C)SXSgGZ?K`NXQqD&v5W_GW$O%$l6bIsl*Wp`8)mXDH3wF3F(tokmYL5'
        'U0l1vPWO5@7{;K*6~a33U*K;B;xXMc2G4Yfn&4Y=3X9w^V8}*-VT>y-v#uwWswH#ZHH$uXFd6l46B;7pGk+Gh0FkHuCHg*`bgkQj'
        'xS5D85?ncAgE6$G=`JXP?=O*scEGK4vn8O>{;sgesLW&v0o!E4B}>c-gKO^D2!Gi?(4dseQ<((6xT2=gHom>QAwDI7D78o!;m5mZ'
        'ae#b;Y=UX8TSgxS;4C7>1dUs`zU~`f;KPg?lBRBBgB7Z5^hM-TX>^_ehtO7ISj!U_=|Bl^!r4te^}^}by5<Y^8ofcyLWeAZMrd6r'
        'Q^pZg6VKMwa0+erLlSudwYPf`<&bg4WggtN_I+k;eL4<|!H<-A{-A}>lic<P%LrU;J~p;G$Ne3+3c2ySq25vf4QGPVZ8GW6_Uen<'
        '89PAarEN-O{I$_~!W>}>XCuSCl=uRH!`f{2ozKlJ%5#85OntDO7<YB=AYHH=9I&zosI`SYswIC#16^23&x_*6pIi%Zd<aW(vGks1'
        'fF1KGWs@*YkzpSQa@M?Ss*%nI5JNeHIWmPXV9^!+ZqEk$`sNc`2#piuv%OCInJ&@4=r8mU{d?7wf__6E(gXS}F31g8Pu?1;f81z-'
        '2RdzLx)}ihm7`;P&}M=#OEc2*q&H6%I<z?`^@cvUT5yY@A(dw^_E_p_-rOkyh4@rUbc2%I`aNPihG&2RmbLR9|5>3ap#`%8!mvkd'
        'R&4w)qx%odwm+^K%m4k(->;a-^v`C1zl+s(PY&>7%kAcSSiN_0^U-BLAEN&NWbrHBA`k!o'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
