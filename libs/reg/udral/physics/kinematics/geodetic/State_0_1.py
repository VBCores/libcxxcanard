# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/State.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.610205 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.State
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
import reg.udral.physics.kinematics.geodetic

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
                 pose:  None | reg.udral.physics.kinematics.geodetic.Pose_0_1 = None,
                 twist: None | reg.udral.physics.kinematics.cartesian.Twist_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.State.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param pose:  reg.udral.physics.kinematics.geodetic.Pose.0.1 pose
        :param twist: reg.udral.physics.kinematics.cartesian.Twist.0.1 twist
        """
        self._pose:  reg.udral.physics.kinematics.geodetic.Pose_0_1
        self._twist: reg.udral.physics.kinematics.cartesian.Twist_0_1

        if pose is None:
            self.pose = reg.udral.physics.kinematics.geodetic.Pose_0_1()
        elif isinstance(pose, reg.udral.physics.kinematics.geodetic.Pose_0_1):
            self.pose = pose
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.geodetic.Pose_0_1 '
                             f'got {type(pose).__name__}')

        if twist is None:
            self.twist = reg.udral.physics.kinematics.cartesian.Twist_0_1()
        elif isinstance(twist, reg.udral.physics.kinematics.cartesian.Twist_0_1):
            self.twist = twist
        else:
            raise ValueError(f'twist: expected reg.udral.physics.kinematics.cartesian.Twist_0_1 '
                             f'got {type(twist).__name__}')

    @property
    def pose(self) -> reg.udral.physics.kinematics.geodetic.Pose_0_1:
        """
        reg.udral.physics.kinematics.geodetic.Pose.0.1 pose
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pose

    @pose.setter
    def pose(self, x: reg.udral.physics.kinematics.geodetic.Pose_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.Pose_0_1):
            self._pose = x
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.geodetic.Pose_0_1 got {type(x).__name__}')

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
            'Bad serialization of reg.udral.physics.kinematics.geodetic.State.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> State_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "pose"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.Pose_0_1._deserialize_(_des_)
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
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.State.0.1'
        assert isinstance(self, State_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'pose=%s' % self.pose,
            'twist=%s' % self.twist,
        ])
        return f'reg.udral.physics.kinematics.geodetic.State.0.1({_o_0_})'

    _EXTENT_BYTES_ = 64

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`utU2ogg8OLSGl4)B}<d-C>lO{}>CU)W|X|uIyx31}$W!YG#Zj*IsyH2E}V;`y%sgjgq7wg7cbVvsRBTx<qurJV$'
        '&`a&EyV=cvp}Q&uv}<-T3<ZWE-CK7K`9G4wSa}%=Y(;6nejdIZo^#0G|2#YoX>arw<?m*qAAetGqv<q_YRw_Gt{M94THPSkTEl90'
        'EJt@q=x@8=+TDiRwaLYe4hi257p{bFg!6vBW@>G={isb=tKFup8PyKmaP)>#eN{I}TXVU)N~|VfUiE^j@zSK)8nGSSGDDj2$6kQ{'
        'cBo{Ok)MWFLVvQRxvs6(yDo9USJ-)m)Udx-=;zPs#Aps`Hc@M8u2yq-b!j$UN%Q`ZyQ}E3<*>uX=(wm7EwXCRGRm3RRN~RQEm1e!'
        '+Z8#ijU8KW>#n}W+BkmJur&APD==BB>u${;=Bi6W<uq$|Lv!3(o1HeK2mPJP;&6Ug^=Y<kiErYa{bu-l=+D+1S2LTM-P~NzRaQ=0'
        'TQzmJ+vF!+v9*TFE|SA8-dXspjGtY}{I7m)d=~vgeffOYt+Oj38LZFa3Xj&BR)f{`Wm{|Nn)wRfVQ}#d!CO#H(<8J>k6)!H=*j=D'
        '#*7=5xf-{IK02%+gS$}fYHJP6tU7wN%dT2AzK+%J>rHZ@p&6PT-+CiTM%;Q|u>Q!miA!wW7a6uf^Jg|mM6JFN>(Cn^eU^U5VNf(l'
        '$0iM?HqG!Yzf@b%*GaS1v23@dH^cM(RL!xvc7w1D2B~#4cFX%?+!%VD-R=y3eSMj)eVZXRa-7{z)Z#jq?dWXBhGn|8Ww85;tg}j)'
        '8gqAdx^+Wu)R-D{4SwE%{xE0?@#SF!IIMtCeu>yhz~;{kE>rcP>WM0sfzai2&eW*pu=?4=bh$39=?xOTMIWWh>=v&ZtmH#NH3syu'
        '9o^(|=oi1KyU#?+7uX{7!_U>MPUy?S3UM~tb&EBN)ntjZEv8AF{AWAF)?CXTs8FHSpgNOZYWmxkwPsT{S8v&gI(+N-uECnQk=)8k'
        'SksIy34b2WE2jge&IXB2Tu`V;-8yS-TQ|ADF-KeH&KMUt*4MmjWrQD>36v~sj@ywy8O3s*+tENNz>Z<Ngze*4p1}4=ZpQ<qh~;hE'
        '76YZktrRHRvA&Gsr?}k~DAU|d1j-DzV}UY@{dS=Io!rg_$}VoF1Es=kIZ*E7wiGCHIL~gBvj^w9pW8y9>_vI|xXlKNjPvj3c3+?z'
        ';C64IJizV!fpU=BJ%REdx4Q%75Vv!Ia+uru0%e}tN}w!oyDLzRaJw^5j&i#rP!>_&W8BUJN)`1!&h1p7oIw2_;&ywWJdAdnM1On*'
        '?fELVlY#OG+Vv><_Y~Uq82amRwDW7+<^$#HXzvr;<^ts#X!n!o&(moCx%j?OF2PdRb=a%0*I?g)eHZpU*!N+t!`_JPk~9LRBAj{Q'
        'oD$AC;an0970$YFt_tUxaNZHlyTW--IPVMRx^Qm5>9X;etamgsikz^n?$qOPP&3^A$l;#R`2gP_a-F!B2{C1t64|hr+Q@C9nX*GP'
        '*&u7gkmr{!JhLFPU?AFMCEBIK!xq_EiB@T*OH5O%%3L3LOd*Ri$y(iFi+m?mNR=rxq0e#VAE5{6lk_qA2l`Z(UU-XMJWszzFU`{z'
        '=}Yuw`UCn3{h^;@n#lsVD2C!P97j>1KQV}-nAD0$D)dWHEX8#4p@CA;6{d>*ufC0)<S1}uee<|1f`Uc4KcX&1jTCjSPF!Tww(KUc'
        'W!;e*l*N9mmn@l`x<TWHud@x&9!!r!Z=C<u8JWdJZ4}_>ual@;L));r=reYhBO+&BIC-thI+c~p3wT<y+2F-SbzWQ6c|1T1=_+kS'
        'ib&hE(-+Qe-|K7=(;ZJ+CLiO>Emheck42e{9Xy7<Lur4DPx|SwJvZX*KN9*(f2@qKyX_||WboMUl~jaN5&p7?F#SL%?=5%`hqK`^'
        'HoV)gkxj6X0~=Yekxj6X1sf9B7y}y;*q8(xS+F4`*cb;JS+G$88xq*af{kggu?=iUU?T@MDqv$4Y?Q%95o}0cV>H3W{a|AbZ0rIX'
        'vtVNiY?Q#pB-oI^MjmWr!Nw7=F%LElfsKP;;{e!@!Ny*&u?K9-fsG2-*a<df!NxS$D1(g>*eHUH39uo7jRM#h1smA}8>hg=JlLp!'
        '4GC;`V8a6&9@y}}h6gr0u;GCXPq5($Hax+GC)n@=8=hdp6Kr^b4NtJ)2{t^zh9}tY1RI`U!xL<Hf(=iw;c+&8%met8hLnbs2FAf_'
        '@zBs?F!XK%LnZ-37BFN0LoNYB4lrZ^Lmn_>0K)`em;emL1Ppn=Py`HFz)%DXIlxc`3=&|-0EQ{RFaa2HfT02yrU63{FccCn>;?=w'
        '0mBqvC<2Btz>ozD2LXc&81?{$3SgK83}wJj1Pl^j7zGR&z;FyO903f60mDJSupcn&1q{0ZLj^GG01VTBVLM<b0)}zGPyh_M1Pmtt'
        'Lm4n!0u1K>!zsWp4;U(dK>`dtz|aE>J;2ZtF!TfrJpn^cz|a#g^aKn&0Ygu~&=WB91Pna^Lr=ia6EO4y3_SruPr%R<F!VML4Ji#N'
        '4PSa1#Pp4ry9oI_?~wWaeTn&g&0IA|^|`Lb=cA)zhfeqVyN4vxY+Kt1{n@j8t~{P8eu}TUIp4IcMhw#C)6sEiZIC;VH|GwfZko^E'
        'JeSX>CA5y#(A|wt8Qpri!}O=0CmrJIThBIUYp?P{Z=RHpgQ)+~Ff$D^(=bzL$>`<vjn|<g8lRDEHFKFv>(ALt#u+jlOKVi6nxBsp'
        'CG=+onsRe)Dw=Vn%XgTsZ2gm+Dt!V>(M-`ypgC#TIvYl{O(T7rGiiOuk(q1#hLidc^M@r)=!f(p`bYXPz3y-0FRW~p5&7jy#I|JH'
        'iqFGS5IpnX@b_@!%aqsz`3>TTv_{=(Zp3*FS+jYDM_)BbQ@*Ub^p<_&G*Uki^7zE1IAP?-re(WyQGQV@6U}iK<(I@_)4FWlORnQi'
        '*@?fTPZH^qMEWElo+MfZ(~fAKY3cL`_4uE=A9OQ`K{uZuA`c=mAYvpj=t>}>2qN+cB1#~l1R}~HA_F4wAfgB&b|ePfSr8$Ch+QC}'
        '2qH#6#4L!IND#3LM3g{89z@6>q5>kyAVLBW84$4_M9hJR84ytf5qS`?2qF$82HiOjF$*F}AVLBWSrG9sh&To!=0U^*AYw0wxDQ0k'
        'f{5)PVgf|u6GX@$;uMIGK*TbLH~}KcAmSQ`xC$cHK?DU6mq5fhLBuIR#JnJ)B8ZSc1iK@FMC8%Fx8C=z_PuL;@14H)Zr^*a@4esm'
        'uJ^qg!i(vMy#BOP3P%b@3P%DC@#NTvUV$Dy1GRYD_nsT#-InUb%ev#<<-63$S*<m~B23-gsJ=iNu4SLR&8$}I6Ba4Q3$4HM0Q#OM'
        'rdpq}!<5{XL22u=LFw6CwA+x`CzZvY>OI7tBZ>GkDJTU9N&$i*CF0L~LQo0`L79Z06d))g5R@_mr3gWhASk1W_;UvYWg3FAJs~LL'
        '5R?K0C6^GCy%3Z=5R^FxN(F+l6M`}eL79f2lp!c32ucxxG66x6ASeY0$|wXSn}|P;Lr|&^lw%N-MF`4K2+9!%%0fa=4nt55K~Nrq'
        'pd5stJODvC072OgL6IRS6$pw1K~W(nDg;G^pr{ZO6@sEdP*ezt3PDjJD5?+?RS1eI1Vt5sqKf!a74fGk;!jn?pQ?yIRS|!xBK}lG'
        '{HcogQx);2D&kL7#Gk5&Kh=STl%sdHYaRCMkcMS8Z<>jEBhQ|1OZhv_L`gygLca_h_^)Q7D)~(_Q7NV=rYWW|rUiqI+gkK(#eruc'
        'R~E?0x|x_1st)@C<?yW;sji{fwR8+m#UT}kFRVCB#UGvx8^qND8^k}k^B`VM%0bxj*irW|eE%aIzEeU|LT@E>3~2H3`^;0ZKN!HZ'
        'I{z3Y`k;ru*D);BGf&oCTQ}Kb{KDYtoz}-ZL@)3^zvi6(DSzi=lt12o^bh?~^zgq`Uh0V@D@sVQnrO1Euj<XXHZ0yac}8|RT7$?<'
        'vZC|U(-twv=axBYy_w2NDl4h1Y?77MY5~ckG?|(vQ`2N>`f5Q+LrO#9CFQ&ur*$^JxAd=37D`RE{yxS+#ea|9)q6{&=syB&6(Iip'
        'tZqB*vG}v>eqsr4E=5se6c0wTRnaR=U3-NGjnSr#p_#;uzsrukt&T%Uhiz(DtVrGDr8paoOWLw)Yo@be+3olhsTJF5M<vGpbp!D+'
        'KG}{wsNVe5chn91wJN7W8v2Sp2v;}lD$fsM*M-kBc>P^&5WH?qX44POvvK^lVjN$}WZ5S6M{MdJlia|sZuLLGGM>5{N&o-'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
