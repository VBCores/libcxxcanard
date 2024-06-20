# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/common/Heartbeat.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.521038 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.common.Heartbeat
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.service.common
import uavcan.node

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Heartbeat_0_1:
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
    MAX_PUBLICATION_PERIOD: int = 1

    def __init__(self,
                 readiness: None | reg.udral.service.common.Readiness_0_1 = None,
                 health:    None | uavcan.node.Health_1_0 = None) -> None:
        """
        reg.udral.service.common.Heartbeat.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param readiness: reg.udral.service.common.Readiness.0.1 readiness
        :param health:    uavcan.node.Health.1.0 health
        """
        self._readiness: reg.udral.service.common.Readiness_0_1
        self._health:    uavcan.node.Health_1_0

        if readiness is None:
            self.readiness = reg.udral.service.common.Readiness_0_1()
        elif isinstance(readiness, reg.udral.service.common.Readiness_0_1):
            self.readiness = readiness
        else:
            raise ValueError(f'readiness: expected reg.udral.service.common.Readiness_0_1 '
                             f'got {type(readiness).__name__}')

        if health is None:
            self.health = uavcan.node.Health_1_0()
        elif isinstance(health, uavcan.node.Health_1_0):
            self.health = health
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 '
                             f'got {type(health).__name__}')

    @property
    def readiness(self) -> reg.udral.service.common.Readiness_0_1:
        """
        reg.udral.service.common.Readiness.0.1 readiness
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._readiness

    @readiness.setter
    def readiness(self, x: reg.udral.service.common.Readiness_0_1) -> None:
        if isinstance(x, reg.udral.service.common.Readiness_0_1):
            self._readiness = x
        else:
            raise ValueError(f'readiness: expected reg.udral.service.common.Readiness_0_1 got {type(x).__name__}')

    @property
    def health(self) -> uavcan.node.Health_1_0:
        """
        uavcan.node.Health.1.0 health
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._health

    @health.setter
    def health(self, x: uavcan.node.Health_1_0) -> None:
        if isinstance(x, uavcan.node.Health_1_0):
            self._health = x
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.readiness._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.health._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of reg.udral.service.common.Heartbeat.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Heartbeat_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "readiness"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.service.common.Readiness_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "health"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.node.Health_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Heartbeat_0_1(
            readiness=_f0_,
            health=_f1_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of reg.udral.service.common.Heartbeat.0.1'
        assert isinstance(self, Heartbeat_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'readiness=%s' % self.readiness,
            'health=%s' % self.health,
        ])
        return f'reg.udral.service.common.Heartbeat.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`t<OLHB?6_#Wy$(NV0fe;>{c?2XZjr_obKu8d>!OFE|m1MB<fJx6xUv<m#xODg2t4o=xkXPZVsfw$ZRPhhOCVPGY'
        'KY>j)R8qwvStN@Ti!5?Z&zbwu1H8y8nJV4Wn&~-x`t&*9dCV{G_`?dDa98noyBC=#_Ix9>;<0*<2eI({FiYB*QC5`2-J4eDq0P0p'
        '(rb(IqjLU(^8IqIIP9l9f#*+ZvE}8F=CKDnIw}+%yq#pJcR_G%1Ho-s%=#UnjmpweP82h5(fFgXInkW_UHL&--05>`wF+`8O!+pj'
        '-$$_itg<-#x)O0T5UAlt+;ZQdlya)NDGwhY--h6kN`*0{oRLRrQRH2)ygW+pAKy=qwpNL<ssn-?e={{|D;3ddYQ>h&qk6j250v#|'
        'k#1R8Hm5+$kQ?hKSp;G}T0FR3Gs4%r6?k?DAAxQre_L*p#r?jqJdL=Hh8f+=1K8W)4v%w?;0`~^!m^ks;qE=f>`Ip6JGL)`JTAXO'
        'qbHhE@=5u0a{`&mXNk||#q;OaOF4h-Pg4^USEOKZmToOtp%Vt2tYBG-B`Q@3k6AnG3e7@TBTw2E&e3at=qluK+*@EtW-K##V0y-i'
        '#4xS}GhJmvDI%s)n=uRQ-Fgglz`9bT?p{Yo6~=-o!`fV5hv~5GYBd;Vt(Mo=9PqW0TNY(3&2YJPJJWWEb0xHqSsq8sYOq13EaM<f'
        '%EY_50=<dU;;uHYEU%q=?I&KNu{;o)CA`NpP6X+>yN~*W<7Yg{^6E{i62V|UVn<a=n^=f;wW+yQrr`lk+Ob%uW+KZ#uvCZ$wqvtK'
        'kY&|-SzBmsRl3D!b=<ekE3Ft2!%_m2+SXYpBJe{q57J(h3U!r^sdJ%vslO3WCY%fC5SL`3;09SbH$a9Rg^uVJG&XDFT#(RqGku-$'
        '5Uf(!UIQEmtS<&f!EI--fUcF3fELXH>@*Z@Tb&6g!${-<n?+Z_b>RSz8J>x<ZbzyGdhI(POW=oZ;n~A#p#X1)7<wrPhI-*?ueL+C'
        'IxLh{oA%0L+9xk~toBr~(*`Z!&PM!nc7vn2^0@X3dA2yx(kL1jGdzEt#(iMgC`|wkvapXAov!_7hO7uZ=&8xdgZh3G2;2gwAnG}D'
        '0g%w{l+sM2KMjuGnGPH&N6Q6!&U7TSH)5ETiVe=9HAiiINa^52R)wnVw4M&HIDW$5z!G^HHz^V=p2wE>x&=pVik1QuE0VW`TXLSd'
        '2-XDtp<=L!b_~ngxL2PfdNCefR~g}f^5u(k3i6fa)NQHz{MsAKZ=64e>Yf3>x{44&_x5lA&@Z@Sf*J<v14jgr0f~f@sFkPg%o%Mn'
        '&0r#;T=f!9!BIlV(J}!44QSMO2SJ59xKWT;0M&ps2B3)?*3>YqCA#2-fT0n151dtnkZ^joD+ms0Kj@o{k)t+j4s{ML5y6^HcmRaW'
        'ED^)Fi((-*Myk~U07dYE)2tV$8KUFY3(W~{%UeL84Kna|cWQYGxbD;gDu}uO=JRMQVr>5roM^h`9Jq3Cp4$vGndJsHO~xlW1i7$%'
        '2-GpW8Q0ohz)4-ef5{*^iU!Wt0zn;)sKzTPcx<IpLT-i({_66^+UnXH<0f@zU{azuK9pbhL9fbP(6r{{!}5$=l;`BDa!vj?hj<+c'
        'fDhQVh{~JAJ$_5=h{#7-d=-^z#eKfXavchI5DOpNOP0k9l2`?0abz9xrk!=X`w>L{$t8%+GQ&h^s;yumoVnFm3}_>Ez@iY1ibvXc'
        '0KVb_(B?6&JIG`JmJY#f$aY)`0}MzTfO}OMQx?biIO?7BPI-udrNz|YxG%W@3Gw*-`n{XrG=HA1FiQ6UxN>%ImfTRNsC*VMhz`P?'
        'A@6V%^FYOb8udZA6D3F)I<2|BiD0-|Mg*_n1EYiF9f3X<Lr4OvNQZ@~*9H#TVBi%7fdd*B!P!=v1^qmv@*J;m9umynkXe$RW0!Tn'
        'eXy)9SZdc9O>T0`R_dK0DvYWEwiWR3Ix2#Pp>t-8=%|7gCyAVqTFoK(a~@LrR^Q{s)jM#?0AbUm6g(B+B$ZF?5}^{$;g*412Xqwl'
        'AXLJN4qBubc8x04W@t41D8XZsA)W)*sB%NNiKcJbJQOcC4q$<AgB(@r584LJy8CWnj1-uyHX4kbSRA@ez>OPhrPjS>H-?@qj$H@b'
        '@H~&<wXaR=TA1~(8*J>_eWQWD?+pD7uFm-6-8ULF(;LIgPmIfQ(2c!W++dq@7&pGz4N%j6O_<x#W&P&pk)F7Xw|5!C?(6H>?P1Jh'
        'FQ&o1*&=(d+-R&~TIO<K2qPV=1OO>rutG=F{rnyhQ?8*<(;VO^&65C}0DQ&)(7x6TAwAB*F-(Izzfq$YVnBy$m0{qc2oIB_8ZDhD'
        'ghOKA&ST@^D&#Skn<GF$j5e8ugkvPKL-uY%glL4IDiBo>UsFV=@dI-tWVcu=Ip9VCH;AcK((j-(g)pyC5wY8f%hXS?3-2v7sv^Oa'
        'ITZsc;;=#-sbd^ij%5V6LY2xvHgAWknY~ID4@=@8hT!>3T@wsyXNZJ${Qt7J>osLBy8kytzi=)N`B}Rx*nUh*F9|YG7=+qOBFWTy'
        'PIH%CLZ9hD4`A94p<Ihfsf&Bpd4x61u1T_sPuKD|2Fn?LD$oADoNG?qGC?s50o`#Zo3nWU`-FTIhB)9mIGDlS0^||Mv^k0IP26fu'
        '5j|A#Y2HEqA4YoUR&$!}&mf(=)tsg0N083mYBq@8N%StFcN4vb=)FXb61|V;F`~zb-cR%aq7M@N7SV@@ew*mSL?0pgDAC7=euwDe'
        'L>bX1h(1a5DWXpk{VvgGh(1enj_5qm=ZKylx<GW1s7G{(=t-idh@K{ThUoJ|&k}us==X@eNc8(eUn2T4(H{_fh3F57{)p(SL@yA%'
        'MpP2rA^IWFkBNRl^i!gr5&fL#mqfp+=%v|78az}F=IX(V_25E1xK<BjJ=m!SAJ&79>%k}W;M02WSv~l?9(-93zM?^1G_d-|oD4E!'
        'x)->r@^EoP4;p^+@;SKI@A3`x3y<Zz6Y|tcp%}*&CX^gie{ixnu}6P!zZ#WVbF|Rcm$Yk_FRiXEUxXKmlZeEw1Dj$N39wg}NeG?@'
        '?m|QII!C4I{CMGWTdj-P<#TVXZeHHN-bL}pWfp44W?d+Pnl}+x*mqssmb=;w(p{+XC>0*aC{mXsyG|X)P9e-_L8*{yQFrP9?lJX+'
        '(hBRq#%Pt^(pfTGr(<;st5ISeFS-s|tpzi_;mO--9;__Cd1dwT8t%7q<)B^g?V(*@v>xjvU_6Y(mgd+;aJ?It4|;NK5t2R<Rcn~V'
        '*oNYJihp~(52|)i{GX1BZ*o_7M0*w3wfuS7Zx2;FaZ>K;h8$E&%PT0>Kjh!#zvMr+CnhH*<iEEYK(?px=YIS-3O~7g>!!TACa=k#'
        '&B>q3x8*z1m%os_n65kwVl?_#S=?KB8I-Ok2gR#YSg0!Cvm8Jff<@P0r_>2hscX?Vf!S({`Zu6_+8Y#Hd2Cf1HcXj;!tROddq!gD'
        'X`MgRiOKvz1J$x;!$FHyTot8ar~=0SfQ7M(!&Xe`2)OF#0+4RKo?%<oyaaivw6<+tT3YIMyI#z@UYO}r#IYx$d?{?{B`bF9(y8Z{'
        'PM`5kojHAa?2Q)Z-d5IGin1`rcI-tJVD7n;h)D6J<*1_|>FfC`N{5gX=%wWq|MXeMXz`TSj#}7<au)JJDX+`4I`em>?Pn#u{^<R&'
        'Ttt3=DTw@4b5{Nu{(kfSgyVlc;mG9|V^McnQViWc63$it_o18r;HBkj{`#A*U0hvRMx6H7&u^?=#$In>T^EU}kGjW!L1lOOP<yK@'
        'XpCg!&Qui6W!ho4b{`rlFP<NCqg*Q(SYrirK&&Ao{ENJAJ4O`z>-M{deaQjXCj%MENQ&ZE|KsRr&#r>KztJ~@K6>xl?g1$cL>6#t'
        '=02@)ThDbsIG8xn1#-ycz9|m6L3M%F|B6#L1NW=@un~nQSAQWG)WAtrh5gj^_2>xj3jzGOw5lpL_bAr;J>B}HhzaFB`8X+zz^ufI'
        'x^7;;h|70%s$iYESH&B&%A#qDP_<Ophx3Ys$M&mxcfB}P=vIBau`<_ft@@U-fBQ@fefe^Iw68^8J5(b+u#%<Nolf^GHj5)wt*J$d'
        '-_iHvmhT2``NbOO1HWAfgAb0vgQNWi{rRJ}(Fwf&02nRn-cBF@00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)