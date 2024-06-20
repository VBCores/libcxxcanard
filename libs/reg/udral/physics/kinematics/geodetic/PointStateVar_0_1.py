# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PointStateVar.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.580700 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.PointStateVar
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
import reg.udral.physics.kinematics.translation

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointStateVar_0_1:
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
                 position: None | reg.udral.physics.kinematics.geodetic.PointVar_0_1 = None,
                 velocity: None | reg.udral.physics.kinematics.translation.Velocity3Var_0_2 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.PointStateVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param position: reg.udral.physics.kinematics.geodetic.PointVar.0.1 position
        :param velocity: reg.udral.physics.kinematics.translation.Velocity3Var.0.2 velocity
        """
        self._position: reg.udral.physics.kinematics.geodetic.PointVar_0_1
        self._velocity: reg.udral.physics.kinematics.translation.Velocity3Var_0_2

        if position is None:
            self.position = reg.udral.physics.kinematics.geodetic.PointVar_0_1()
        elif isinstance(position, reg.udral.physics.kinematics.geodetic.PointVar_0_1):
            self.position = position
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.geodetic.PointVar_0_1 '
                             f'got {type(position).__name__}')

        if velocity is None:
            self.velocity = reg.udral.physics.kinematics.translation.Velocity3Var_0_2()
        elif isinstance(velocity, reg.udral.physics.kinematics.translation.Velocity3Var_0_2):
            self.velocity = velocity
        else:
            raise ValueError(f'velocity: expected reg.udral.physics.kinematics.translation.Velocity3Var_0_2 '
                             f'got {type(velocity).__name__}')

    @property
    def position(self) -> reg.udral.physics.kinematics.geodetic.PointVar_0_1:
        """
        reg.udral.physics.kinematics.geodetic.PointVar.0.1 position
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._position

    @position.setter
    def position(self, x: reg.udral.physics.kinematics.geodetic.PointVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.PointVar_0_1):
            self._position = x
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.geodetic.PointVar_0_1 got {type(x).__name__}')

    @property
    def velocity(self) -> reg.udral.physics.kinematics.translation.Velocity3Var_0_2:
        """
        reg.udral.physics.kinematics.translation.Velocity3Var.0.2 velocity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity

    @velocity.setter
    def velocity(self, x: reg.udral.physics.kinematics.translation.Velocity3Var_0_2) -> None:
        if isinstance(x, reg.udral.physics.kinematics.translation.Velocity3Var_0_2):
            self._velocity = x
        else:
            raise ValueError(f'velocity: expected reg.udral.physics.kinematics.translation.Velocity3Var_0_2 got {type(x).__name__}')

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
        assert 480 <= (_ser_.current_bit_length - _base_offset_) <= 480, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.PointStateVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> PointStateVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "position"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.PointVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "velocity"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.translation.Velocity3Var_0_2._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointStateVar_0_1(
            position=_f0_,
            velocity=_f1_)
        _des_.pad_to_alignment(8)
        assert 480 <= (_des_.consumed_bit_length - _base_offset_) <= 480, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.PointStateVar.0.1'
        assert isinstance(self, PointStateVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'position=%s' % self.position,
            'velocity=%s' % self.velocity,
        ])
        return f'reg.udral.physics.kinematics.geodetic.PointStateVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 60

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`vY+i%;}9S3k(vSitoZTS*MjdNjAH&t#*n)H%(m!`KY1?$wS+s<2>l9Y7pLzN;`l5*{0ZJCD-$wpuV$^m`Y^Uyz`'
        'kJ?-Rgub-{+ARYH6a$7W+e>$j_&t)$#BMSa*oHD_`#Tb;Ba-6hcMgAK>J9(q@YAX8AOBEmtM1f|isBGk*9`q_t!j{pQnQ*Z%h6pD'
        '`V%Xz-LAQ9o4mZ$BH;(&v1{QwVcE|rrq*Q3&)H<X(yrT@QEAaFN3S`RH*}LUHJ3NniB%`8Rav%l(_L{jm%OUkp`TYai0$Z>8Pb$L'
        '@+#UNgmOwA`bBsx^v4y=b#1-cc8L>SW#6~MmiE>P{p>}Z81?=ZjwyA`)fAU+Hcdxw(yU*(hYjZ2N=N9Z*eqILn?j4|Yj&X56Zg>T'
        'Ze8xQpDkN&>aM=Q_H*>2VQKF6Ut?UU>aJoCbKRw(e1YwIO><nO$-XwEi~jtw_&EPq<r%hYi7(;@{QdBy(4SKrS2OFHT_5b|I_syY'
        't(&^ruJbQmv$dMbekh0ifEUqbef;uT>c92p*4N!X-DCMu*sii)B5$x`9&PZjQnzYsTd&w!UDwR3e1-mxcNDE-@&$UFR_N*L^b9@s'
        'zqK=?hGnitdqW@FX-E2Jq14tkYMNPb^h%rkYL)1Bto%f;la-ogh_iV}PKi_R|Lk~Vo5UqHKNczWhUU)>qzR?E73HLNLi!?o-eD-}'
        'q-B#DOFH%NhCivS>6@gkv@F|I^m=&NpH>{JZPy4}U=XFHu~Xh3;la?W>~vpdDR6U{zxx3rHguYuP}Jf%FWu7FiZ#o0ZOdTi7ujSR'
        'WooRs&}vr=y{52i&^Gw@_Hz(JlZ$>H)`7!180J3_dlT6F+5XQ|d8l%x!qY(La-FjZ)f~2cHZfhE7dG@732)HH=rTLSs|M@&sK^?9'
        'y=+A{{yOvvPwVar-PbGZCGv-#QLI+zOFMPqY&EME+by;wOQdPBoW$k7*dn&(T6RAR<&+xLSqi46KeepY>$<sq+e*~oOE0$#wwqh='
        'rL2by&1jSG*I`+{5I9vfP_&|sLOI{AvfXX!CQopzp>6WU2v2hCSo6N+A^y2kAg2*CJPrl&FkWYQ91i3h;s}=Kv3wM-$FO{y$I(D8'
        ';PnKLg+QL<F(1fNc)y6xPxCkt$TK{S1@bJ9BY`}J_4c6uc^>Bic`uJMfn4IT7|8eWI2p+M@I4FYXFtC00FSvqK8XGf@t6)|3EzL1'
        '$3ua9gvWz{d_Ru|0(p_g{ek=dj|+i(l*fI6{2-6_1#+3kQXn7Wac>|W=W#xePw==WkWXTJPw_Y#$Q5k&X&$Eo`3$!IAs(j!`7HM1'
        '9FE7s*q=vu91rA2v0snj_@2l9J&xn`1orcLJZ1y=``F(f@R$kYA7a0s#PPg<{l65QH}WbXMchQZj`$(sM~ELIeuDTZ;!VU`QC!Lo'
        'p-~czvS^$ajZ31jDjHNYHbvvQXnZIdABo1tqVb7nd@33@MdKD4Z8koW&6Z|%XHR&q>Qtj~P&3@#$l*S#^8vm_q$+XWBE*zjN+iQ#'
        '*+yy-&6FIXNe0;<hE!f!dEuDECIj77*1D^-__Rf`*1B(Lrb|pyt4KUQ@;QYhzDd%m7JJE8Vx3f2h9>mK-29{T2z`=1PX9okYSWb)'
        '^ySO+6}nocKczpTSLkc>Dt+D0u$;*zaosr-Ps7nHD)h(t^C*^T#Y`&nC%bbgmM0(TXG*%pvZDX{A7Le_JBek-<_Sqm3QkJB5%pwu'
        'C&ji`#$INdZP|5VOS&V~sO9jZWJ&C+Yc$&NO}3!B2Fpj{Xk32oS&7Yyn&`mM-zMFD4Q<P6<Cw9JIbs&gJ11|p*+FG}^A4WTY&LkY'
        'QJrrsJ9vD87SeUv=w?LPq^(}!Z1-BNfn>Vp8O!8joO#Er?2krCnT;KM9{mly{XP29f9|yAR<!)*B0tl2<so*qy~m~u9{cxNl7y2a'
        '{9Q}J^fQrpZ{tB6Zo^|Xyj^UhV>U9dk%o<Q%tjhE@~|-i8+q6mhmACB<YP8QVIvJ2ldzG8jWle`z{Uh@<Y6NN8ztD7gN-6=6ksC{'
        '8^bXh2Vi3#Z0v=NIoOznjY-%ThmAaJWMLx>8^>Xz3>!ybV-Yrvz=i}H2VrABZ0v)L5^T)F#vE+Sz(x@^CSjuh8)LAMhm9O;48uk`'
        'X5&0;lwqR;8+q99V8eqA4>mm5@L<D(4G%UvVZ#$PJYmBVHaua&6E-|y!xJ_<VZ#$PJYmBVHaua&6E-|y!xJ_<VZ-A#-sKbcL_?w>'
        '(ZC$M84V2`hM}_yhExng8W>W*kcnZ)07DuWvcQl6hB06m1BOBjLlzhcz>o%p0x)ENp$H6lU`PSOG%$<-Lk1X1z%T<01z^a<Ff0JW'
        'JTOcHLjf2@fFTVGi@+cO!+u~W0mB?H6oH`t40&J}28I+coC1d9!0;e2ECRz}U^oa23&2nUhCRSA0}NBZPymKeV8{VOCWhe*Fcg7d'
        '6&Nl7!+BsR149WI^1#pmh7K@vfT1HWbOeTuz|avGIs!vSVCV=89f6@EFmwclj=<0n7&-z&M_}j(3>|@?BQSIZhlWH$qTxHQ0p*))'
        'R0!oo-oawOzp%r7Fx%F)LVxZeFL6f&-lzCm+iw$1D8wL5UPX@XiuFtW#etIl(&t}`k~^;+Xf3U#yIY~0yK_~-^k-foE#m5TE()iW'
        'H~2@l*A9w7cQ@aYRYqRD2l7KP^4S>q9LVQDJ|82W1^EKV=VIi?K|TlaLm*!S`2xu2L4G(!eh<jcfczB57eIa#<Z~dOiIG1D^7}!4'
        'AIO(LejeoKKz;_~iy%J<@&%9|1Nl72=RkfK<kK<or$N2~@~1%lB*>ot`Qspe4CKoo{~*X81^EX+ei7vF2l*o)e;DK?kS~FJ9^_S!'
        'S3zC{c@^YUkXJ!o1$h<ZRghN&c~y{C1$kAFR|R=hkXHqHRghN&c~y{C1$kAFR|R=hkXHqHRghN&d9_b|vSw{)47FJ!O51js{ne?V'
        'RO(9ip4aPVua3RaV!BS*`Z{$bm#?^P5K)Khf0kD)ZGAJUM~VvQ;BwuO>SRqfNnNrDFO2e<ttDxa%X(zVLFW};Lo<0L*S6a0QT5Yl'
        'k($1ylX|a~db(Fit&BYv<&|D}bf=1|sJ2SayZ>RCwO3Vce34G2=)T5lnN+IrC2Q|gTBcvnFX<oYpXg10THMyZL*1Az-+k5fo9d)r'
        '^$MfOoF<vmeCOvhjlVIT-7DTDX^49KKX)%86B7}?Rgj7mfYLD$>DaA;OiV-(B2o~Mi4}mRAR-MBg_wv5h)6@kOzc*{0z}L}#Ar-J'
        '2_lLRk%x#BL>z#Kd5D;b6@Z2yVi6(^LPQB7W+0*f5xJO%6A*C}A`U~ueu&r$5i<}m5xZ58fr#@E@i0W3fryh3QHF@c*pQ!sh!R9B'
        'L&O<~C_=<_h}eV(3K6RiaS0;MLqu7KC<zgHh+yX*NOW75dac!7i}qTZz1H<!>%(5_qh9OdUh9)y>(gHAX0LTiv?3qfR__ux;gRr2'
        'c-+QAJklU$v$tIq4?F|+$gWRfy0&IIM)yv6<yB%>{L1#+z+;~2-5>Kj6nnsK16{DbYV4}_+%C`8HU7-T!01KeFMQ_Ozxb90pSPRd'
        '_6*$M^KXs6vX9A`JI+!Y|LFJruV}UHSKLx^#hqMnCs*9tuegidOKXK)RVxmuS!NxHMdKHkjqxnIu>9?CD&_2SVX07+YJOg1fzU4^'
        '4{U#c^X@J$8^2>;)vJXkOcSOF(_L%fyNswil(VA|G<SC+Xi~FIXeKo8xn}J@b*0=LR!>Jm>ao|)UX|{xa@{ZSw)qeo4)X#pZ*641'
        'xytL056tmHf6w47pAE`q<4+5}`2xE-&}>Nz;?i5XO9wWpGWKGX|D6k74cFZ0X<qh^)_bH^GbE>7<u}y$9_@62Fz^>U!f&n4+?dUF'
        'rwl_$UP|&(l9za1YIs?cnv+{E$*q^<)=TnmRiYu$5PP_)U$Kd<DKXpp6)(U{H|9s!RMQ{6s|O0^xBZU|?)10O7FGz6`fEvRmMztZ'
        'tLcXGZO#PinSSwT@GcVl>@ph^zY>Gu(&v29=lw;!&%_t-Lsj`VyVMntEJ6SP'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)