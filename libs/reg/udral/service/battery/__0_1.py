# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/battery/_.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.512554 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.battery._
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
class __0_1:
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
    def __init__(self) -> None:
        """
        reg.udral.service.battery._.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
            'Bad serialization of reg.udral.service.battery._.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> __0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        self = __0_1(
                )
        _des_.pad_to_alignment(8)
        assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
            'Bad deserialization of reg.udral.service.battery._.0.1'
        assert isinstance(self, __0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'reg.udral.service.battery._.0.1({_o_0_})'

    _EXTENT_BYTES_ = 0

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8fDd$L0{@j*|8E>e6?bS#(n|`BLQ{zV9a5+qaF)12LMlQcu}uh0UCVY66^d4~J99UKcXzfkvu9tWRP+ZBkyfHomj8}FhR>Uw'
        'J?}ZTP*1kJw=?s;e%|N3@!zlhr@gfnKJEMULO4+*sgqXoLVwA#LMCZ$%Gx;XW!JvFEel=ZQ5-F5*}dxSf8D+4*4yu<x~in@)LQ%Y'
        'p|?%$8!K10yqQ+KgowLV&XPu0UL;U6*SSnG?!B~&B<<Sk>0DZ;O+})v{W(6r>UP(5ul%$7x@&Kw*lcyyc<H+5U3+`<J<S%qk{7g3'
        '$lA)B!`AL)`@M9kPo+p}V|}Vcx7XfEooQ??u~5jg=3aH}HTqNNtZU!ehsUS;^!62uzw)cDy{Zh^|D9T6V{R&MO#y@DDQvGe9`Dvo'
        'R_Hv1gH1ttQ^7q?J;LC+_6@x5+Bbve5D<OGQ}n)TCu#C9*-R(}o$n6FH^m)Hv$FE(aNuQoH5DfB{_@|OYimbJJBA;xBy%OVo<(V_'
        'G?n(o>T1S@FtbPJ_TZqEUo_fE!MtI?e5aVHg1o6I3Ud+!G}+%|?%l_e31f$!J^s_q))BkxbM*QC4*M1#>`&OiqoW=6*FS#w910|W'
        'G+V^%TyWqFKebvoox4O9u+HjS`$cjXjvcwP{hLXWY(9Jl$<A}%xXVqs9GQm~p8RSPLXjRo4!hj96}o@n$*&$JA5A8oX0%%(5!@po'
        '#iCD%w$2afU^%Z?CRyW<zNxWHI<HIaDPy!*R-&=ILJZ9`yr|8Iw5*S7!jAC9;I&<*cLJa>A)TI8QQ{ehHki<SRvD<s-3H^8U?ta;'
        'mlbJ9U~uhGsk|r_8$sECvFLO#7K&VsT9t%0j>vGKE9o4I)wJ|%-AQ>t;6OyMC^;C;-QSp;D4i>~N=)U>!PcJ`W};cpU-L{C+H2Y4'
        '_yIe7wzIPjABFswohaF({>-Rln4uN^#v&`EtOJnbs-M`xXR<`4GPiJEmUy#(VOV5*LWzY{F$HkfHD$1D5CwvDIzyU;<hj@LK8+5H'
        'L)p{btvHZG2aX=?Z9o1zy72$4(PdrqFS!sp2FCHJ^b1y7<KZpdxgK<MAmHOfI~g3Hbla%}NKUj@L0@HT2^prAmIrqt)aDX-LGNIH'
        'AY7huQrySOTOPEGOkJ?hQ^In|Pj%UpF<@M<ys<V|48+j}usU=@jnFPv+|Ez{RYCcp)tD>5H^h|~ZfEbwqbEDt344s-nm($lsRJ~F'
        'z8C_Ewk)PgjjpNdLPMm|GxcC@3XjmT?JZVGAj}@KsWm0zd9DQvMKlC2X$PQL$Z<5t8nDH&6iLwcjJzJI)il0td;|!BcII9T>Fa@m'
        'Ii3~3E0q%(9d{_A8ma=oK<pBwiT2QYhx+58tq<mGFhv{SA1WxKAXhR!c8rJsGEt~7gGx()gL1hNHSI>x1~g1qjnNJoLka-Zr_*s&'
        'g}k^x+2jqxRK|xOqcux$zN!{+dBhy6WqOV~HYU1aJuBqgA?7%&Oj8I3jKW%^2vue!X$y7L8^o7D8N+GhYg0`jibxTB%hqKwOTdYZ'
        'oWLL<XO@dt04R4h<+{KCbRW(Gb+B*_wO9>xj+}$o2V74<3$BL{X&k|78PlO(5M^5l6JjY1BD9-Sa>j$$C65iJ2S7#c3QW+G_tK7V'
        'K$8%po50wk4iKFjhW(Ka3W>ptU|lwa*C^*R4V)n3G%X;$rf~>xjCn>SiO9{Gb2CP;r*EpjH#kpCNDj>&9O$5?N-*hj3S0L3a}e@H'
        '!x2kj!I2UK@j=azH4Jkws@KKmMhk{HmOFAxPN&r6lBF!Wlz_saSm2BcRE0yuxUq9@N}W@4gDFP=emz>p)=<$*O&;2D9HDq=8YGB3'
        '3`0#H%GkFtoEBV{)M|(9FEjlVVVF4LYdt0EnQM7MNvERgPoqOtgxbs1VDCML?k&YVU}-G>w@d*Q$Y(Ed5{Mncvga!$Nh1{%OKyNO'
        '@M4B(n!vxR6348Tb7F}>JymTMs2Vc}ArwM~F?litjTs6((N1&#Fbf?7C>iK(Ko{zXzK(lA!ghK+!@$$q4BU!<?Ksn7p2=~7a6}EV'
        'APhv|ea)|G+K8+Xjn`#t$pIF^gq~-Jp%Dx1dOkjmG6Q}?;e-lWgx0q$U5%U4(3g<PJlN`DA_IX|4qYSS6<RqFAy}GNq((pDL}NJ1'
        '<CdYv(L^{2NaIC_>rl&9jvQQ#&pB)kLvt+njg|BkAtr=1LP8ueCqferXcjdT1_5|nJZbh!6Ke%Eq>OMQc#iC%qFIh5;nf2nr(kxG'
        ';Kr3^1#V6s4%gC5`?QeN%q!f6{Q2))d-JjO&%*aZe2q8H_KnokUCS;L;ud9QkQ-dLK9QxtrI)PuG~m(L@f9~mLl>R;sQvyv%}>?r'
        'wN2_bw7S<61-FaytB^3~MI*a^ck8=r-?$8y-MSal?Oty(xLfK9H(h$*r}S_w1#)qhq|=jBp4Pky_u)OX!>q~FMBPv~)jR6e^G@A<'
        '(W!S|syln?J@vzNbyxjJ{aF1(y|0-1sk)~=P(M>Yr(303f2r=PUqCjMWaUZEom9koy-gK5EB?@}wY%&;0<{gJ%N#pye^&JuhNmEr'
        'nY62y{u`rkce@NupecLuN_J|my|X_EqGQPx);^&n-1o2igKoe-NP*-^pt8q;{sq^6sgj^WZK_|7g8%Lo1{F@%l8ds~zSSoYEYdy4'
        'iQn}ieoq-;$jFMQ_YQb9lLsI%uP=kdam*ABjAdQ_CZuNz3)}eJd4UAStg9zTo^-Uxu*hCtq@&6I0Fx|}7?%+M00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)