# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/common/Readiness.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.525987 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.common.Readiness
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Readiness_0_1:
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
    SLEEP:   int = 0
    STANDBY: int = 2
    ENGAGED: int = 3

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        reg.udral.service.common.Readiness.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint2 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint2 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 3:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 3]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 2)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of reg.udral.service.common.Readiness.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Readiness_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(2)
        self = Readiness_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of reg.udral.service.common.Readiness.0.1'
        assert isinstance(self, Readiness_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'reg.udral.service.common.Readiness.0.1({_o_0_})'

    _EXTENT_BYTES_ = 1

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{^vGU2h#n8Fri|cDGOzQdOdWIzXu$Y;W5OBqVy{q)v$38p{q1T)=8}cg~q<W_PwTv*-9kMxqxWMOq1@EPn!tpTvLR'
        'd1rUem+jD8uu`1$?9BW9JnuXH%Nzgv*PV^<H1Ail+~qn>oUn>(^_-_##7Sm~$~fgk+kE%T+dA{L6;EcBXkWJXzG?s5?liZOk{9^?'
        'Q!B=Com;MB$e5^1#5i4;GCmbNSEX>SZMKt%uuhq>l^f00m;L+8_Gshi#^2g++UBi<dv8@*d*RwYLi{y`&3CoUt%pkJd|^<O<lOVb'
        'la<#UudFJRR}<{G`@7PqaVhf0r59siSG{{HNtI8uD92v5N1G6yap#l5<f4`DH1D1ag6LTM0N=i#Pw?o*U)$5Rc_(q6mpQljvY;1r'
        'DsMHnCS2FB;Eg0VS=(&1Sbe+Meqc&E<L5@myYk)s?FUDj@;&*ZqYV-+-|yv|eSUa&(#oIw{@<G$8&9NQ+LYscFKode$qQyitWc#Y'
        'xMr1^3d=I+sEf)Y`f&u)RmQcR?Xki*&s?3lne(D>j9bCnRQXJboT<_q<{>`lV-y26m7)x56CqWm1yhby+&;s0xZP>PyBUq*=xia^'
        'OYT{2SZPRIRT=A-BzHzTX=<G_Zw2-$&p6B}nfSU^h?^)qd3E;W;P|uqe~6>#U|}{Z_>5WF2<v%Rr+6a$j2EWvPI^@c27ko4>Qp-|'
        'MAbR9Gcpz*cu{Gw*X<;csbHlLIo$CkN{#8xnMzphRXJw8cJkZST~wUVP$dx5%9>2%K##izYoAI*u`1WXxz`<<JAz;$FNh(jWSQWO'
        'L<Vq?z=<OG1clC<iuS@nKQ;Cl;~A<_`B?;5qWU!8M{XM^utRVPMA7ZR(@a#p%L#(vB*}rZ1QpVY1duSwiSofCH9}nHux15*@G<2c'
        '+A;w&<czQn!zeDioDFptv_nzZIUTpn?W9M+j|ZfR^9oTS&sK1{eafj^xgKyK_nS9ImP|u2<NL$@eNHE*txExr53WJcF9!T<^;JX&'
        '`q_;RL37-sf?Pld@>wVskc16cDvc#PEz%!K2Px%Lxu|Djb7A9^!t6rqXjiXuwbqw{4iI^jsVYRhT-LarVE|Z?OcyrgV#I6hd$~d3'
        'YEAX35MtHaJ0h0?Quk3!z=zVPiAqDg*Rvs$gknnHR5=kN`10dE3-Xsoo39n_!{bK>j}AYhaBqRIo)U%hYgYgO@dX?UiZH4VK!nL)'
        'A`vVa)n&*z>)k93HWJHqhj<B~WRg>5fd3sL>f%>XMM&H#N$epssKykLsG-wh+el0SLvUyg^dMIqLn3>ADtbEX{UK~dE2(yDhhh#$'
        '<j@(62O*r9LM-zxnMK@~tI-GqO5}xX4hjZ=1pGnKj)=$c9uaM7fcKEKx&*I>@E`>F6l8vnibbsXpChB?H~_eVH?O@xBu(w$bYFa8'
        '(o-(nM|;&csfXzA(WWW*Uovz@5z&4th}4myfv=?C+RG4x+AS6Q(}UCF$H$M>OX}vLq(pOfX(~w4SvPS|X)$?6?#iFbPvx)VLwUbO'
        'zs?2d18$4FebKy~jMTZv6S5^yd3)U4Nt~%|Ch$Rv1n`n=vqk@DmA1{BCzy85PiXZey8n%j(4D2B@n*A9*od5aYc$wKoTH+MjhY`;'
        'bqcH`Alh1!-o^X@TDpm4%qU?nf`C36;Jt1*YMbxRc{Khw{v;+2Y(0$*cN57SETr@&!?_m#&3|rp9A)PO+<_fnsa@YHI?RHD`b2~r'
        '@(EX(r%Ho0hD3yn_LQ=et(|#^P`f%H1|R5yx`X5sL73BMNvMi)*_c5$Bz%Pe?>GnmbfJT@u{P;^4(X5+M~4^-XG>+-$61G|1M8@)'
        'DJpduil%loO)G<E#0smSfLkfgo>3rpmIW|VN2d^scyCcCQg1nizkrYdTXV#%hj#(WlxQ=I6ucAwNr$ORCUoWn-g20A5TkU4Rtb%P'
        'TBKNphV?0pIaD<BF2S`k#OIKjcQC{vmA<QZCVm~gLIj<L9o@i=Xd|*=Jt(G5LDOm!F}AzE^z35cf;|{wZ`sAtxBa!}6$^13GkUJA'
        'iA##v{JCIj&*g=Pe*S6c-{P69Z@#<`4MH!Lh3~H0@~VZaMO?76J{cF^ZUJHXzZvsdu^djWrgZl;PG2g9%g_H7cSSMx_2MG-?UY=t'
        'If@?BSQchrw2=wj1i+M`SrHKJe7?tE$}KKxmV=JUx<~;6U?vdIwbhK4u1&VaX_)h)fyIaeCfq7Rjj!+U*d*2J)v0gc80@QByU<rL'
        '$Ixs}1ce^$jK#pQ(%CV+`-~`>D5z^hUB|b5M;Q2nW+W1~KLk1DPC*)aYB%%;YAw;`Ed@dcSHh(J3H#0Sy{Nk+glkSGpufb?4RPfj'
        '6UcIHA|MUjD2Hj@FW+Xay0XM{B~CS(=ZC|cU~zXwC-m#Tx6OC%EB|@;{Y=a+&dtrlRBgkq6XIq?Y7j8A+Al<5)bkLz--dzS*u~!f'
        'ZYLS8Yk4cbYQA^EbGp-9+9VBqJ+8Gz<*a{|`+skDjyC_{(q<bCJxFMew(AsrVqV27z3_8-*`mKKV2&XBBf1Mwhr*n2jNXV@DE=?a'
        '$N#If5dZ)'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
