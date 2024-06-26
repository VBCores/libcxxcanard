# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/StateVarTs.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.624027 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.StateVarTs
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
import uavcan.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class StateVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.geodetic.StateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.StateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.geodetic.StateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.geodetic.StateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.geodetic.StateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.geodetic.StateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.StateVar_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.geodetic.StateVar_0_1:
        """
        reg.udral.physics.kinematics.geodetic.StateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.geodetic.StateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.StateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.StateVar_0_1 got {type(x).__name__}')

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
        assert 1240 <= (_ser_.current_bit_length - _base_offset_) <= 1240, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.StateVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> StateVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.geodetic.StateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = StateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 1240 <= (_des_.consumed_bit_length - _base_offset_) <= 1240, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.StateVarTs.0.1'
        assert isinstance(self, StateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.geodetic.StateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 155

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`uuTZ|jmdB@4+WoNk*#l1<?>Nb)Ui7W3?vJ}~>6Sq{PI7(?LTT6D<b}Vw19PJE6a+sOnYS(Q58o5+11}y<k00C(W'
        '_oekqfjsJwMS;Raf;K>2^wzvp=u^-Fg^E6;-<kQJA@}T3Ua3Y}!?VEh9M0vOGne1@Kj%B&47>3k|MCwb-k)={y;-wrjY8Q{O<if|'
        '?<uPdwNS1a&9-6bw(2^2ZrEn0YIjWa=4M-UKXez~cfaT6okY2%G->@=Q(Y@`YNpaCw6#r3uUdsWdP{98Hp{N5Mopz$;fAf)>YIvr'
        '({dfDysny-ZnRu2;*7tE{D*ESQi}e_ecyE^%ZhEA`fA5kE%#ljY(z7Itz0MZs;)L_gXX2mHN{rSHfyss<}cI|&asZNUR7EJTW_j`'
        '8=I}FW*RO1J+*d|7Ff2@Y`faHHc^U}BCI7^nrhdw*nMVHJKCn+)NOs8+A;G+%hK0cYVDgXTU}GlttV}=ysF#fhT2-QHMew;T3J;r'
        'yWFIc<Z6eUeapNcwp-yct-Hon(W#04(0$!?X3NyZR!uQ$!v%fNS*1gpZ0c3hu+*y2s<}?QTr;Zf%D;_8A~!WvZgrZgswo?{<)N)C'
        '+13<W)|7QsZY!3h)?`a>RaMzCnyRdrRE4RSn{t!Bwrp8%(e~b!b|J+I#d0dtF!eQBo!1L$VbR-)onU!YvD5`wx8$07o9>C4+*Zvc'
        'rQL4mRk}TlRzYUPR6C~0$_aL1HFYdCMHfn5Rb^BCZilW7?S9)dnuF4<;PQEe$xUjQYA(u_s(Kq$4Jy}a(}C)(HCk$}>vU{hQ*^KP'
        '6deUMZe3|~RMtw{kX!0HJ5BU)yJ6h*+ZU|A@Zu7k68WxPqjsuQh1&RXDkaNH^0`|VUfg<SX>(=O=-BePa~Chjo2p`3i}GDfuWD>n'
        'o35O_S&%QuFMio8b7)^`cZcpBQ@(3-8a1kjYLMkltEE;|%Ti3evFSH~ZUkAkt)R7Z+GsawExRHYs8(AuIu_f?tDaWZI#h(LP;FGO'
        'x}nqgYT0xj%T-gibgSSW%;g5%3wm|w@}=u?zGc|*t5+6ex)WM-E={Vhs+e?BblU8Ey(F)05~QrgwzAnU6z>|-g(BNf@EU%TUn;rD'
        'n!iRHTbj~nuq(`Nx3z}4<ZbR(aa$dnsHRE_{Cm_6t^?f^r)+jxuybItwJo|ZGMz-L;1UQKN4jjZ7$$bWoi?K#LGD=TqIO(6QHn60'
        'v{ODh<8NFqUH{g%ue;iUbMkG~G{maC`;D#}I~#Xe#@$xIb&_STL9TO{8wGWvO*b4fW?M{x^tyL{Dh=Kq?SeBwhg@Y#nK^tF`M?Ce'
        '?pmvzRn?gpvV-N-P2b|OqsVLX+IelMLk6X$Ql*5GT5~^eGUeO)hFUAL3su%@?saFXY#AN1s?v&vT5c<3E}U_eH1t*1nOG((zp>1g'
        'en{pidWH;#W-zlp*4Al5x*u)RXiyu~4Z643F*pa?omB$3Om@H1VD%0xEgekKH?UL=J7=zQWJe=gc%g8%z)qTLGqW~R))b2x$IL(('
        'pt>K>#rWBEAADAW%xYkF4cP(1B&)zqHoJcbZiT?L?;7TvC65eis7~+Nd6m)~V{2PTqXLXZ$F~KZDHzm4Uo?G9Bi88b8ci~EHB`**'
        '+f{=~A}htMvB%;%ZDW{AR$Hy=xAmd>orL0!T3|MLwLz!oB)?w<CY%o17Qeer`fIxVn)m&N8r;lItZcMhM;=v(wb@)X==#uEy{0w|'
        '7{_lBm5Obc11U<Ds~VXBSNo2$cUh@18@X*GO<`-VcNz_n0dcK%;m_QB>0-}XB|&fdCAcN2vr5O=)LTs6D5Gq!%s7)cx?5PGr6}7k'
        '(kqQ2jj?pBSBm3%f~C=3DT(FdSS}%*!15GJlfBX;wokKE>Xr7eG~O#^u>D?^PWDP!te;|OqF0(mIWsJs?v-X)n(dY5SeogT_OUeG'
        'EA3}#s#nTk{{yIZ9`zhVIfqc+VU`~3m5#7<zE?WR(gVGc%+g%1bd06@d!^$n-PbEU$I`i8=>$t>d!;Y2bf#B2iFTc0=~S<jNBb67'
        'y0=$4jdniI(mlP>BHFuz<1L`wXIMJXE1gCAUtsBYuXGN_aUSR6%QznIy2g5?7jaxK;rw32@%@f}-AgYc{R+~rB7Ftv?;`y@q(!7x'
        'k**-skZvHohx9(ukC8q=`U%p9NFO16?5EeHC^9*o$@9!bp1I01D?Fp|%m&Zg<C*(B^D)mn;F(W&<{{5K;+e<Dbf}j{%0PO;OgxsY'
        'G6PS_Ghq+<oeNHc30TnE9O||fp01Pa_hHeS7W%M5r7rERRMLp2DD?F13*BXj&+oQG>i;~k$V1M=tJFoYxAe)WM^L05!8z^JJ-Sd$'
        'WsN$A9o8Lx<xk#^{9pY&{*CvC&VYBPNTjuB*@7dzV=6UWX}!DkhWU?ehot@I|F`3qXc(=vPdkvo#g{Q)v-CoTu1vv~y27_f=5JJ$'
        '2EQ$b#%rIm^O0z()U%><q5X4bRndyybL&&lNTfbVAC~sD546kIwJX{;^4eAHo7(SdCG9osns(h8v#5U-XQzbvTo?yBGlSEzwTGqM'
        '_<&WQy`io6+Wn4pE0FkVkXsuP_96+pc8BS?)}YhZr2p1P^^OYa9fx|yq25tJy`xa?IMjOr>K%uAr=i{w)H@FKjzGQlK)q8??{TPi'
        '9O@l~de1_=r=i|isCNeHorZd+pxzSHI|=oUL%qkK-VvzxQK<J3sP|#0_aUhFL8$jU)cXL`I|udN5B1&$^`3)z&qBRtpx)C^?<uHv'
        '7V5nh>Yagl?}2)!q27~F?-bN~0_rV6y~m;6NvL-M>K%uA$DrP0Q12+zI|B7CLcNPn?;_N@2=y*Py^B!qBGkJG^)5oai%{<()Vs*l'
        'yU5kM$kn^Z)w{^myU5kM$kn^Z)w{^myU5kM$kn^Z)w{^myU5kM$kn^Z)w|g1Xg^1WOSYsm28P(aqO&nTl{p0LyQ=EDNE!w)=#3#|'
        'OI75Cx~?|l{IwgeEqDV3w#jX8lQz>VHh5->XvC_vT1r7?gEBUBlzC0em9XwRHK-6a%vG78$ZP+l{kk3{L!te5y~~V7j6OOejD`~<'
        '9d(_Ar=)BU=xeF#qy}nA13j*%u9NW;mCVQsf+2DK?i<)h_Pm7DuX$PK^0X)i27b{yT7D3|&&V*@sGUYvRgHQ8E#^a@s%fzAoq-Kn'
        ';cdYNbvP~8zkY@L6IcNj4eGpd8_Fj0uXtP0ZWeb_vclExcIfO<*{p!eib>;V5*gN7)f?Uw+)p!ww}wVQbC-=48)3J097;J8{z!@j'
        'ugq8Z<kIRtrYq!qso$sEsO@(!#L>_YhlV&b#LN(H!$Y+g8(m_f`vf*b7eh>NF^r9HF-TxzTyQZ=f{ih-Aqi|u2rh;U*pR@+7}%Hw'
        '8+!y7Lkw)>z{V`t$byYD*pR?RTwvoc*q8?!`vn)n6xhgsjY+T}fsF*%7y}!p!A2fzoCF&uz{YW~A%l%0VB-+jm<Jm<u(1zp%z}++'
        'u#p8D8L*KC8!50MfsG{Ch=YwWfer3r$b*d>*pR?R7i@IFMi*>!!A2Ksbiqa!Y;-vrUCu_Av(e>jbU7Pc&PJEB(dBG(IU8NhMwheE'
        '<!p308(q#um$T93Y;-vrUB(9QvWGN;G<@M{s2`+Gmah(d;-UWp9wGt{W8fhI9%2FyG4L=39unXo0v=M}Aq5`N0uS5)odyqM;2{kj'
        'V&EYQ9whJ(0S{B)Aq5^{;2{SdrolrRJR}7k4hjzFDe#a6598or3_P3w4>EW-1RiqWVHP}O!9yB6NZ=t39wOjj2|Szz52wJx3Gi?X'
        'JRAWJ2f;%QJj{WIY4ETYJfy+H1b9e-hnT>_S@4hr4=do|s^EamgNGb=kibJ9JoLdsA3XFq4}H!<pYzb?JoGsaea=Il^U&u!^f?cG'
        '&O@K`(C0k#IS+l#L!a}|=REW|5B*_v2x$mu_`=h`9Xi~J0VnK^e(0luA6j973xz-EC~R8X+jpcJ+BrBPddW1EP1l)yl}*|E^SqbX'
        'qOBoAd&+7<WpOr$Wg7Uj<zb)p)D}PUu#cJfCzQ5Q)$L8U6yMqJ@f~OSb+xV9`p$F3W92(+*R6gDx#yj~u%{XJG{c@Iw<Ynr8=LQK'
        'naqjBBayljd(vc1eTMmNXX(R9cy`5gW(Jn!S!QzTKcNc4p<oDT2&e$)q+#kLrpl1s`*SJv?=xf`)tijhAH+t_qtw68X#D~E_#ylF'
        '5&QUK2Japg)UeZh$xpnPLeuc8^+HYAOa_bAknd`$sbcoS52R%IRin1)&w9v;$tHrlm|{PIP2AR>Z3?DIUQVs}^GYmS(X_Qi`7Qok'
        'RV;f^ew%--d4Y_(o(b9A+(rFQqeG@A9A|{%j4%8+qdpmj7wTFusx{fi?!`DFh;c$7A^{>IBLX2M5RnEE34w?Vh{%A5EQpAJh=dRb'
        'IVXtmEQpXm#C{Nw1`$yZF$*G60uekAG6NzKAVLNaIS`Qr5fX@qfQVxtVje`y2!W6Z5U~g%P6}c?4<cqkL<U4iAYu$eoC6U{AR-SU'
        'o&ym_K*RwMF$*I0f`}A|NC-s8LLj6BB9=kKSrCy05%)pFJrJ=0A~X=O0wS(%3xv#bB66Gv2}IBx2_(Fn7UVX9+`S-oKgfL?<Q@dM'
        'PlDXTAonQ9J?1%|4lfrtr9wDDI6^oCIM8iP_|KY%4yt-DhAvsY{vqqX4!lFzA@9(&U;T!AgX;Hbv(ns-oxb{C4odqgf3vMFpDbKH'
        '*OnQn%h9Lk*hPhoU1UVZj>q#Sg^t~%5YL|+5s1P&c6)?){s>4-g4B%Av6~delxZQJe+r}~LFzn6&4SdV5Qs7-bnIdvRR*a!A)a3X'
        'sS%L+97sI`Qs+Qw2BeM)9lO&Y^#n*gB8(}gL24SLCWUzZ^B}bVQWrq#36Odeq|SrXIgpwaI(AouF=a&vM3F&i1f<>vsrNwY21wOF'
        '>Ix_I>b7|PJSR2BJ9ZKWbvXcaIRJGz0ChP4bvXcaIRJGz0ChP4bvXcaIRJGz0Cjl?)J)Y_S4^FS1eQCdO~kJJk_JR?wArJNroN`x'
        'vdvbnHB>%+8|=YC;Y@wQd#G^R-#h;EQT`zB-C(H~dnV`EfN=rqguT7z>KgvgQ(?h*ew-cq3x=frvx;o_4ppxpeGBQ^qm~Q%KEL#I'
        'f8M~=cg3^a|0wm=*6)Loo43x%JN-3Jn@TP9wouH<;5bq2mhbYX{!yW~&QY;jb_=2~>wlgg%loT(IvI)7|03}$o`Wo&vDm?R@aa+8'
        'Pdh;G#JvG}H0*PQeXg+2wL_n){x=CeUhj<&9`w<A<_8x=JS3r`BRbEM0v?kB9x31<0gsf>(Mbr-^Yn-Z7n8t467ZN79$ZWa9UbmG'
        'PXUj4;2{YSw<+Ku3mu(^fXAfZJf8<1Y2dLW;4vdSxVQ*BWZ*FiJS5<8Uclq9;K3Rf9$YK{j}yRSUg+pZg7aJ!9$ah#kFx?En(*MF'
        'BzUks+U7j3Y>T*+c}FM0>9`oskq_v|1$0Q9j?!c9#d^fOSP!`u>l5z9dceI{A9F9(eU3$MY<Qd=LJ>j{Lg7Qf=Y8AW^Q@!eN6tL)'
        'A=WB?M5S=^u5Q`8f7*8OX^P!tnPRBRy4o;U^hn`NwQ3vY`6q<BJi#Ba%V-tfKM~uVe<C(2B&DJ?>Hpci6QX@e3ie47yb}q*K8fCm'
        'N!X_(>{C>*PifdE3HB*2cqisypQd4-_6qiCLhw$+gg)&N*r!8+eagW;?Sp-qg?*Y9>{ABzDGmFSf_;);pOUaoaoDFZ!8>sV_Nf5-'
        'v;_OK2>bLr?9*x3rv<@2oq~Nj3H$UV!8`FB?9*}Br(>{BGVD_h_DO<$stDeR3hYw__NfB<RDpe}z&=%ApDM6V6>gs@+w4<?+ouY*'
        'PZd7xRN>Q36+Z1$;nPkPZksCHHdVN7s&Ly>;kK#5ZBvEYrV5{Sstin1)_cIX+@^oL9BMc`<?qL740>~Xm*FWAw*{_~g*AAl@RVEQ'
        'LvzF-tRbu+tUj#C2B|kw{{`pxYhG67$np2D4MIZ-qh6YDYJ0G1r=ghTP{~8%5E_Tit#O$0-<2{-%Kus-nSM#yrIcqyqu|#6fmHb^'
        'MEsHzig?Ir$mupt$AK18@hg}7{6NP2sW$H&And`9QDL8Xb;CCG77gha1~2@mFEPenV}16$6ZCOLdb-&rXCiP3xK74%3hWfG`pPxK'
        'o93ccDKdMtYt3&N^+3*Fk*&7E-=j*+-=SCXSx;E~EF3L_h9)#LLx!gQw^I0Aa~NSAMp%c>HHS2WH0=Cba~Lxk#*BtBqo2>1(SQ7G'
        'Vn&}3`?<T&&;M2Y=QBltrd9?+<=~ISZ0@ksPx8$(*24CH(7YE6x^TwwLN|9Rb46Cf!MRt{4ojaLADX9%yf#opJM26dz86z85Wm8P'
        '?>}X^OR1*}7M-R+zca;S1b!>gq6a1h(V}7ZD(qf`-K%;j#lu6hED|m|_7p_KK81*+@NR{OK!hX^5fg}r3ht=A!n+kX5fKovPaq;D'
        'L{IM(h~O_|odyw6p-&S55z`<dCb*+gAmTWPm=oTua6%v=4I&~S;uwh72O=f~B2EhLR+tu|r_T%SsAB>VdxaOW^53;M3nKC$LIx2z'
        'p-;ozQ4t|}`Yedp01;OOB0dt{txyqO$SQLpBAkfFoQOx9h=-hrPdE_|I1wLnBJOh{?r|bEI1w5rVucfNb=&V+<T(*J-jT^}2@MT_'
        '2!RNJ7!1K}Kkjn)JtJRXvl$QT|1wGaxv!2t%hN(r{C8e<n!EY>4ONxB4ZL5gs;Rc3H!Su`cI>qy?5C~RPkDJiQD^(_6A{M}Rn_|J'
        '=Wu3|gE^cqfIJK!4+F>%Kwf_k^d>)w6BhKbdo1Dt7SR#U;>AZ`5fxtVpBXW^$)Ckb3a|H<1S}>6EGB?OMtByFzurFwEHWd;SBHhk'
        '&BMa8coATc1Qr?L_5NHuC19~%z#;=Ijtjq%#<7rq#c^OU2`uu0hm1dqcUXA6|01x+0gE`WSOgXagz?omVRBOzu*d@oO_<!=02UIk'
        'SOyjkglF+`;`pk&?e+c<j>Y3`;(4Eor?%}^(j@L3YwzG4I~#b%vfMjX`ZdSm7aWV9ax6ZI5BDfTC_*SW6vH>jPLmw?Rh)m)rt1Hm'
        'rvAn+p1yB2Gx(wE--dflD+g1T7quq+(`~N({5r|PzfN*lc*qEN7!OtjXoxG=DJlF9UoQ4--g^K5'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
