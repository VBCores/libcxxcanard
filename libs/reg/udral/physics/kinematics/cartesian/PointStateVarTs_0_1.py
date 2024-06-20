# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PointStateVarTs.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.685486 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PointStateVarTs
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
import uavcan.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointStateVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.cartesian.PointStateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.cartesian.PointStateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.PointStateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.PointStateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 '
                             f'got {type(value).__name__}')

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
    def value(self) -> reg.udral.physics.kinematics.cartesian.PointStateVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.PointStateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.PointStateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.PointStateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 536 <= (_ser_.current_bit_length - _base_offset_) <= 536, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> PointStateVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.PointStateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointStateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 536 <= (_des_.consumed_bit_length - _base_offset_) <= 536, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1'
        assert isinstance(self, PointStateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 67

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`ut?~fD58OQf*pU-y~&UYNd0YaAK0)}vg@GB&3S_mn<bi)PlE2pN3y|#y&HS1kxe;jv_A~i2sL9|jWWh<e+>pT8|'
        'O1!D$7nO?CsJ~uRw9N~oz9{Oeyr@(vRZ5>(f5+!r?gAv0s;YYue#X1AGqbbv`99CgtoeTC$3K}>qQBtj_Hx5*nB|Jg978va_w|~|'
        '%9Xm^YTK^iu`t+p-gErA=R54ea+`%8hkHK^KL|^~aK+MFbpDvb7Rr9Z(amz3FS|zFEnhJ#*3vzZtm}@)Ttm0YXKlms&U?DYF6qt%'
        'Hw<!>MdrAMZG~J3MlK=!ai}TU&=128!(c;2_dLg_`BXyq4pq5MWBa+nVEDAb%*IM1$0`lo(<`26IZyQt^5I~YuP@fAO`g$W<@3u{'
        'ojbN=yw4gJ=z#0#t#-&q_^39dDWWAjPqp&`F5kRfJKB!XGCX6E+Ohef<r)hXYrJlGY=JqeyKY0JW_T5oSqmNywd2&vy6$?FmffIM'
        '?g+M?l?92*%BSeu8F7lbX6OguxiFZjP#dj=?lcAqy6)HL);6?^x?{VnZd;8o$W$73J)HkrN>MIwrdoch#vIkYtPbRIRgdeQ%JoI2'
        'wsqHK4b?TQI#XS{#Z=v)DjeNeR$KJd@>Ij3{83J?JSGaoaVpeyj0HMfGRmyHKguOKSgq+U+p8L`+F+MyWHi(^b7u5*+cfGlNNlUD'
        'iel=%<A`$lmx!8tmyOYbQfo|g*n2)b8@l|mW4BgHcl(boDokxr!<e&Qbs38?)om)*ZPSe!)&d=M77e<$s3}HN`xxB?HEvNieI{Dz'
        '*{a1BMK{sMWz)XeYhVBT(PJ~zCF)h9LG5I9o!a>F*qEx$sE6J?dTe#iQg*#&`<{B}(D9?{GSeM*zj~D$buLb|>B)J^W%Z<b>_}AR'
        'z_rwFpT>@(UbTI*K^0LAs_I)7t25Wt9m8DiHGu|#YIttHwbX5N8MRhCk)u?r$8FygxuWXnbi=12RGn(0g4vQm{bhMHj@7zjxQ1Kq'
        '-OMSI#)46wIdyVQEm^jwo_=kwN+ZFdzI3QQBAW(<-xmG#qFP%fNJWipec812=o!<4B84bN4Zk2CmD&=`U!cq`*G*GAVKLkmOg0l`'
        '?^SV`t#nk2(ShC=_4?0&2E`sv3=7c*jyP-4gHfpy-Ev4EYzlIxY)fF`^||Al`A(#EX~+39d|FckPkc`goso-k+T5FO&4qk#u=~5r'
        'vEx-o<Bgu1=#49uebp+5LADY#C=8yGqQI8gG~k4ot&)V?xoCXqrfd&C8jR8{*TqpGho_P5OW?WCt@$+;Y#z|TN^QBPyW%cNd>cQ^'
        'XM7Tr2BS&|C)NnB2b(IFjV0EohzC_M8sS_pQE_eGsWUoZvPxSgxd=vtF^yUnjGiT}Upgy}eoXQ-bby3|+d|w^ZG$q>c=R0Gq&Bi8'
        '8e8HXg6(a;MgUhx{e4r^yP~voGufWNQaPf}!eHl`B3pi;e6TD!E%bz}ZLV<LrN#*vr~uUPIz5bE&Go<+HK?KnF=|K$Y==}qbha43'
        '1h-D$dRJ}d%1lItJ5Xoz?4n9(#CUuaX;gr1`aLa(q+q2U`ofI`POMSy+AR{g1}YZgwq{dFq*79iBNi7akL}F3ZB{of8w2B=9K{t@'
        '7Mff$sf%{Y@v<V}bkkn^dl=+jHM}>X@8?;6FbC<1-3|kFy+YjOR?Vj8L%n*2wQPvvn?$AV+0Ke9%2w)}WFX|<3&zjt4WW?_Wa7Fw'
        'JLj7wxq<jue)LCSNju(gYvj<|y%It#=hx^yTZSdv8zuB5kr)v!jz)_pR2vf4DIF~Zn-(_J(K7fxEbLH6%i{P5j^|)UaePeJY)9LG'
        '{CQz>9c`nqnU1yz`NxIb(9sGwKOyXJN1H@Bn}wb1Xj8%#I@%UtH+8hF!sa{L6T*&lv?8v567_CFJ=;;v4%GLQu-iM@PGProw5NrA'
        'vZJZO7CYK5VV~$|&j`D<qdhC^mX0<p>{Lg4PT0*IZ8zGrN7#vuRzmys3OnA>_Mx563%jwS?MHiOaKB}=`+%^c9ql06|AMe19qkbA'
        '<1qT;2<|6(uIY|;4EOaS`u8~Q@1@>z*ItJG8tm6$UxEDw>^EUgz|O+X!*bXq*lVyiU~j_Sg1rrU2lgK9{hmFO8$zNe6D65AE)%md'
        'F)tHbCYEI4noQh~iJLNUOD1m1#2uNqClmLP@F~h8&p`e}NIZ_!gus*M8TD4;&b@&m99Tcv90*&Fe3?+Y7s(=~jzzKqWgmE)vLC(J'
        '{f|@Z17)sRqzv9&qwG@%SMJGP`7M(CORP@PbohbbeIRz<zRn!Nar9-1tWOKa*;Ct-;?U~AePe~0OhmhwQS1mtPgAtxt;$8g#R&>7'
        '4)HzL=$W_l1!|-(BKuc9`cV0A{oVgO`a@hn>O4wwj<#MmyyZ|!^NW1Gr{-_-cLzj&@*Hb3&sf`aq$*d$r8-|2a0Dkh(U3N^E^pC4'
        'Yh9&RVoINa(koE<bWG{fQ2G><ei%xxK<USz^kY!^Jd|FEDSaMFpMuioq4a4eeE~|JgVHNd`Uxog7?eH@r7uG1C!zFtD18=6uR!Uy'
        '$CQ2oN}q?)k3i{DQ2J>oy$Yq@0i`cO>8GId1t@(UN}q$$XQ1>7lzs+EzYj{k2TDH;rQZdm-wCDP4y7+b>9;`XC!zG?Q2IQSeiTZd'
        'h0>>?^a_;zAe6oUrJsk=&&HI#1f?%R>2px}E|k6trSC%NyHe@9Qt7)=>AO<tyHe@9Qt7)=>AO<tyHe@9Qt7)=>AO<tyHe@9Qt7)='
        '>AO<tyB(i@f`pX!;TEH?nWUZn#;@u8#0O!sIix83Gnc=5ou8WHukmk}_$+^&e}`-Q4St5t1u2&z?~D*Qil#Bc52gl0Zgud?&tDhC'
        'uMKitrkW{H?G+K8C5R@7CWx*e+MC4>BKilx%Dwdv4bl|Zgu!qW+la|@FS-eXv6c9SX4d@(Ck!@4F%CidLJZqr-zk|(t=qOkQz#v)'
        'DZ1Jg7e$jy^42tcd>G+gLU=-WLij@nADCGD9jSltfA-_|0^)c6FaFAzyPwOTnSZWj*W|A`Ow{$hG;@@sY^%fKf((nRL}c|bh#ZO$'
        'IUFN08(RR$#fTgRk$DiAjS;y4L}o$cP;3Dt4<d6QG7}?m3y7Qqk>emT4<biFWEMoGV?^!*kvl--HV|0^ky}CJ6o{OREr4tSk$Dg~'
        '1|oAHG7BOzATkvr@&Je|gUA^WxgSJ64<h%0$h{!41S0o<$lW0FIS@GwBA*43&w$8XAW{X9MG%<-kyQ{`1(8({Sp|_*5LpG0RS;PP'
        'kyQ{`l|)u0kyS}#RT5d1L{=q{RY_!35?Pf*Rwa>DNn}+LS(QXqC6QH0WK|Mbl|)uoh}=}S7j>G1TXk0P9ZxKMy!3VyD!+T^9aX*9'
        '7W+hwvA{jm6WJC_CVXOVQ%7E@lB;!$C9&wwgxfAPzm*~nc(?g8GR@QU;jiPtn|FxR<{!n!pTx(X#mA@g5lqNMjy0V1Lu2e!6X-3c'
        'Y)h=lTWc=Aib=RweRY^6_BYq`=YQ$>^P$9_C;mL~=fa;i&l1$kB_7VGL%bzE9-WAEjEJEa5ekUNfrwO$h!lv(frxaBhysXEKtviu'
        '<UqtYh)98me2j>VAR+}KCP73lwxKWyB1U6G6hTA*MC3q(0wSIQ5nDmTIEcuBh#?R$4I*}eh$4uX1QB@<k&O}YJc!s0B6fj@9U$Tf'
        '5HSfNHiC#8h)Bma6pnz1gCJr*h$w-G>6kxNKtvHloCOgFK|}#WTmunHAcBL4c@Qxh+fXP;B8rlT9EhOt2PC4@Y(F*MPw{?gsh_&m'
        'Pu=LJZuV2R`l;Lf)SZ6nUO#nTrh0rtshXVrC3qxwBzQc42cpkh^nzRT`dNHRxU$!D^b5DIqE}VS-aAZ}m}!gMl*0piW2rCR8+$so'
        'k+p~-$`9YhT65N_4$N9Vnpm~{Gr09bv)J^b&0^!5J8CkEO=hvlEOzxQwh+x&D>SvM;H}HSMdXDHO)BrF6=nUco~9`#o-Hx)%t;9d'
        'gThzZ=E)2!0w=I0uqLo3i@*ty36cL3i@+z}E=4}|K+m7<6|2Etb}{&O!vB6o{<nE@m_B}=dA#-DV8cL+9|l_nqkQtqhvGZA@4Z2@'
        '1Km-jAMd?vywbq(*qb%+W;2s7l^ea^2&gW8WTTs^>(`=pkLm8#n;@L8>n1foga+XwFGn|jk%B%oe@UtJ7M$(Oz=Ct4REbjk-z!z~'
        '(+n1zlMR?;118ykNnS5XXh>*?y<W7kbkmz$BL4g<g`WIQ)5%gmc`yBCUPjou>en1=y*{}8JY(uguIT4!4d&^F>Hg=#!=I;CmX?wY'
        'reuRD*<gBLgQ=+v%NG>x3PA2Y4j@Vlkjy$hQUM?%F+lPFBm+Q{7$BLLj~oUd3ILe|Ad>)ODh9|f0LcT8EdV3~Knegv0U+ZsKqdi5'
        '27o*n^O4g4qzFLr07L;GPXUlg05SqVN&sXh0GR?HV=+MX0Fa#kWD5Yv$A0m65P*~bhzdZ80HgpwasWgDAV&d68G!7G0U~{534ojc'
        'APNAP1t3KL(g7fC0CE<990VW*0CG<Paz_GkTl&ab(nsEuKJte2k=LY;T#`PLOCLEeedO!|zj!Q3A6b+>GAE(9+lS(AABwxHUP?%i'
        'NRUX77+Pmfq8B#uU-OCPPe&-y`t9QfjK$dhwDZ+oVtur*kXQPX!s9e4JTB<wpUjajd_OCFVKGJE(}z6OSA_Tp(J$qH17BGDGo?rX'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
