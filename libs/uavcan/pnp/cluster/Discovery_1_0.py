# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/pnp/cluster/8164.Discovery.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.352070 UTC
# Is deprecated: no
# Fixed port ID: 8164
# Full name:     uavcan.pnp.cluster.Discovery
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Discovery_1_0:
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
    BROADCASTING_PERIOD: int = 1
    MAX_CLUSTER_SIZE:    int = 5

    def __init__(self,
                 configured_cluster_size: None | int | _np_.uint8 = None,
                 known_nodes:             None | _NDArray_[_np_.object_] | list[uavcan.node.ID_1_0] = None) -> None:
        """
        uavcan.pnp.cluster.Discovery.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param configured_cluster_size: saturated uint3 configured_cluster_size
        :param known_nodes:             uavcan.node.ID.1.0[<=5] known_nodes
        """
        self._configured_cluster_size: int
        self._known_nodes:             _NDArray_[_np_.object_]

        self.configured_cluster_size = configured_cluster_size if configured_cluster_size is not None else 0  # type: ignore

        if known_nodes is None:
            self.known_nodes = _np_.array([], _np_.object_)
        else:
            if isinstance(known_nodes, _np_.ndarray) and known_nodes.dtype == _np_.object_ and known_nodes.ndim == 1 and known_nodes.size <= 5:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._known_nodes = known_nodes
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                known_nodes = _np_.array(known_nodes, _np_.object_).flatten()
                if not known_nodes.size <= 5:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'known_nodes: invalid array length: not {known_nodes.size} <= 5')
                self._known_nodes = known_nodes
            assert isinstance(self._known_nodes, _np_.ndarray)
            assert self._known_nodes.dtype == _np_.object_  # type: ignore
            assert self._known_nodes.ndim == 1
            assert len(self._known_nodes) <= 5

    @property
    def configured_cluster_size(self) -> int:
        """
        saturated uint3 configured_cluster_size
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._configured_cluster_size

    @configured_cluster_size.setter
    def configured_cluster_size(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 7:
            self._configured_cluster_size = x
        else:
            raise ValueError(f'configured_cluster_size: value {x} is not in [0, 7]')

    @property
    def known_nodes(self) -> _NDArray_[_np_.object_]:
        """
        uavcan.node.ID.1.0[<=5] known_nodes
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._known_nodes

    @known_nodes.setter
    def known_nodes(self, x: _NDArray_[_np_.object_] | list[uavcan.node.ID_1_0]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 5:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._known_nodes = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.object_).flatten()
            if not x.size <= 5:  # Length cannot be checked before casting and flattening
                raise ValueError(f'known_nodes: invalid array length: not {x.size} <= 5')
            self._known_nodes = x
        assert isinstance(self._known_nodes, _np_.ndarray)
        assert self._known_nodes.dtype == _np_.object_  # type: ignore
        assert self._known_nodes.ndim == 1
        assert len(self._known_nodes) <= 5

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.configured_cluster_size, 7), 0), 3)
        _ser_.skip_bits(5)
        _ser_.pad_to_alignment(8)
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.known_nodes) <= 5, 'self.known_nodes: uavcan.node.ID.1.0[<=5]'
        _ser_.add_aligned_u8(len(self.known_nodes))
        for _elem0_ in self.known_nodes:
            _ser_.pad_to_alignment(8)
            _elem0_._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.pnp.cluster.Discovery.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Discovery_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "configured_cluster_size"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        # Temporary _f1_ holds the value of ""
        _des_.skip_bits(5)
        # Temporary _f2_ holds the value of "known_nodes"
        _des_.pad_to_alignment(8)
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 5:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 5')
        _f2_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
        for _i0_ in range(_len0_):
            _des_.pad_to_alignment(8)
            _e0_ = uavcan.node.ID_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            _f2_[_i0_] = _e0_
        assert len(_f2_) <= 5, 'uavcan.node.ID.1.0[<=5]'
        _des_.pad_to_alignment(8)
        self = Discovery_1_0(
            configured_cluster_size=_f0_,
            known_nodes=_f2_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.pnp.cluster.Discovery.1.0'
        assert isinstance(self, Discovery_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'configured_cluster_size=%s' % self.configured_cluster_size,
            'known_nodes=%s' % _np_.array2string(self.known_nodes, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.pnp.cluster.Discovery.1.0({_o_0_})'

    _FIXED_PORT_ID_ = 8164
    _EXTENT_BYTES_ = 96

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8e-CtK0{^vHTW{RP72ef)rPb<US+XTrSK6}W^=*A=;>fPsSh4I_7|T{A#}HB&40k!Jq0A*|4p){8v}jP&unQJdYqrQw$WO>y'
        'U-O)&6ev)j=tEGT?|JMwGlzSzrMv{y!+yiVnc<ml&iTkQ`pu!g{NZ>;{l&Avt}Si1Y)T$Fmg~H*DlRXZRlgqi(usHy4=i!lsYBC#'
        'v>Wi`O>*}0<X1^4?lv9I<6$B)@xXc%HmXr0<egperf1b*im8URUA4S&;05KX+mI0t%S(=|`rAC*P2z$HC>`I!xq2Q``%S{KEb}t?'
        'Jc;{ED~dv=(ulZBp1{Nhc-`!k#QD1pckPxdMbow-%Z$*!gN6qouG86u9wVQ4(%JO5z3fGNlZTz_>N6`&WV+njj6}k6FnQIIky-a`'
        'o`~b|=xRC<4lCb=dn<SgR+RZ&vX;b0O&M99ZH0FGM6VkaQH;l`zE^WLflJ#Yu1x8?0G|$-wqH%+okxNjUZY;&q2bpI%XR&#75Skw'
        '9M6d09*r_AX|(1te0@`L&j$93kAx$QZOd(dNx&RNh3osUVTM%=eJOG3w&}|W_%{;wuUfY4c$=O4it%`2e^R%7$A&F_4A4%Zm|=N|'
        '>&+x$UR;5xk2PnSJYaXj(1K_gdu)LfEcX>{i)iiKo&l4)yw1HyZ@1{7nTzot1)>MrQC?n3M86nJqf8umlC+!<lhm4FLt<9UiBqrC'
        '_T&|3<g*ozv_+;_+12q5t6LJcB!r30gOCG#+)iG{gJ#Xyfn5#!FfxIZ2k{Y8`i-#4;fBl2z=9x%dk|cwlEl5Mkbyg^Xng~#%3gvH'
        '5I*KpSKvTL*xV@eT_Bh5z<zrcG$(^b#dWG?$Tu4<KDQP2GKstO@?jn%0P<>iseGk;xr}Tl5k}^SDJ%(|gvcJyzwK0c@><Nte_P@;'
        '$Kwzb29CW5Ba0Y_b!*3|H|iKlj!gjtkp&CKK=YzB?iv_&?k)t55rvi~kp#oFb}<$o<0xsk{&R@hNLZe6<?4a~K0x$6w{|5>Uh_j0'
        'lFjk5TwLQd9OLWQ4S3b5IlwpQhw5JUVG_ry`DIL>iVGafr@__AJXmP-_H`2Xf8<0u#Ma@Gf-BCMevrh*L6gYcdc}tg047&>-G|Uc'
        'UmgZL#2jiD&#G`Be}okuri6N@lc?d{2MyP?!riy;!VEeR|Cp56(4MS-iUxY3gcTYUSZ>|%5;lYlYX=)WC{Pd;I5*4UxXd2wBFrIX'
        '_t+u2&eL@_;-Nj(gV?pl3Ut30v1gAJ5xe(TA7Xxw^;7==#M~Ymq;ZF7z9AZaMElK#2}cNz5*{NQB^)ChCp=C#K{!b`ML113LpV!l'
        '5S}1BNjOJ%itseyJmDF_65(0GbA;y!FA!cNEE8TLyi9n7@G9X?2;U=opYR&t2ZRfR*9mVB{*>@0;m-(vPWU0=Ey8<*8-#*zhwv5Q'
        '7ldCDent2-;kSg}5q__6rI4k@c-knXjfJ#vFKuk34Usl>(#ET_@kQGBGHra7Hoi_9-=>Z4(#H4HXuvy~?*t$m_-R45imX7Q^uo(K'
        'u&Pe9o3MO5oThUP-*5B+X}t>y@GdyPviKI)Z-h_96a7B>OjO&__SkLTL*4iG&3}9*ra!1Ge$EJ2PvN6q1<2)&sm9hUZ<DWqphnI?'
        'V)9hycpe7W;8e&mLb6p6VWy`UyKly4;O*D-R@N&U%V8FG>+7zj0yOVo&iAI49LuvF@La2b>d(6Ix=&wY|2*quMbd{1D>OACqvq>|'
        'yZxjV&GFd(aOYF=Zz)KI^|Jvs$PPEP1m`Y-b+D-_85q|Cwt=R;prrtPQk}v1yICI_Vn;}EutyQ+U`I)N(5qh6XP8td1MLDSQARO<'
        '{l`d?uzxo`gN>3pVV@#gA7c}wQ`!%B1{){E$|x>|*a(iAX|VxMMNej1Y=E!mi9w!_qGgz&*<iDzZD>(!uo+T0v?w;%H0d2$6d!Dg'
        'ln*VMkx9}(v>a0YPmmg-1vwdF$4M9UJVUsev*~pYJEK`S*P3@;vvNMQ<k@NDh163&>6GUFVrt2;Ipl>DRX_Wr-i=GCCCg6eJ-nRm'
        'k3mX{cafFL$jj9hQ)rnX^+n5ovP_c>Ywpl8MT(4;K4qCCZPsj}Wr9>1ExpQeob)>7<uWpJy~PY##z@08GiVtlHP_6b<rwL@W(F-s'
        'N#Qj!Xc-}`*UX@0m{eaggO($t|B4xQd9NY9Njuz99acdUxkLdefPifLUj-!J6cC;6KO`Vol}xIK5|9F>4hcwBr8g#hUx$Dw86W{E'
        'p!mSXfmo1$6i7g{G|}9{o$`|kNEh_L^f-)^?kgZUb=?aAHPRH2E;UC#jv3Q_=9EuIu+Mn9iu6+k`wqYpMlnQ`fanzrYH^s<e)Onb'
        '!)Tf6@S`apS-9?lQR5h(Gx{kghvRGlgLt;Z#yC5UA!}&MI0=Yi0=yVQ%Sr7A`gT-%HrL`~7=&!RDIje^c3Lws2NvK1ElNO6!Z^hT'
        'T9kmCP~IXV<0K%4lJAy);FC+h$~dO&xs;WXTHg!_NSCq<fMvQVAZWogPmzG&bssygSt+NMB0Gn?kbod7C3Y5hAprqaScwGWj2h9S'
        'c~Jr~Pu?kBlz^O8yp%LAN<dDLzls+nAag1TN}88zEnZ5Rmk(OJlr%33EnZ5Rnd_<l$jbsUb0f73D$5KBNXp9sGIKMv^ef9035aF}'
        'Et4c53&f3L=ED{<3!0f*O=j3aDj+!Eo|<HXzN(;7?tAL_&pi{XMG5tC{Op0Q8zr7vV7b<IasfqOqzXPYCavdGEh`1qjLp6mpq#6^'
        '4O<nG2lO$VNOHGE2NnhR6vN||sO_-gtuMM}bwBda+QY@A+l%XumLGg<uHIQ&ez=6b@BC77D7Wn=`rM?>rL;Ej<iu~dHXfZ+Lf^9S'
        '5QxL&Zs+n0SX+d{91qHLsM??yjvRHgV))QAY-a*Vu<2-w+hzDDjHlCL6Fy)=crttgcAQle*3?HPl>h13iXZpZLaT~asCWx^sjZLH'
        'vM=G|758YXk<DcGVI-#+(Z^9kD~lWE?fajsKf1GKt}lOj2kE$rl|Q%#MLqD^w$k+IscLziAK~#+WI3KL!&PDbe#e25@V9=Q`T*_U'
        'LK{-3=^z(((4*60bSs2g;_B85fURx(`91!;grA1^__esV^6y!(Ebf=Yig+L%idFFou_o5zT;K(GQli~T;<1G**WPO#J$4>`h>h1`'
        'eq*{Tlj+!GXf~wY)_s;NF<5JkXB*tA3ca6aWb2G%)#a8%vf9omu&6K=13V$Q<3*vvr8=yzIgsVba<RDRwQ)*8CL=#+kM^kDM@t&g'
        '_dP@>G6X;?hW3xM&a*=OOukd)fjT>}g1`m0ZWzx6hpTpXLSE$%c6bof<gw`obPx48BDfi0qU(fKB4DT#z>{T{N4!{a%DikqwN+{p'
        'inGQ|<A4Luvlnn}`mmCC*w+UrykK6ng_yFcW-6lp&*i%`z>Yj?IMt^vZtlgDw9aGHn)-$Npdw)eQM+%=Cz`F6?Vq~azp%#paXs5B'
        '#2i+L&sbI!dO7$`%i(vL_~ro^+WY09U+ZJ8(CYLI4~X71|3h~k0_$h*cJ4H5jTe2QUku^FX-SNVbC96hX<Gj1+}-*U_WCpayn&x)'
        'f^Pj4uHqgO&pbiXS2DSH)U@ee6rm}&Wdpojw;P~ofB%7sy`BGd4vo%g{6EzCFHli?r)*CvZ}16;N<W;XVoZ~3z+GdXyEwS~KfM^`'
        '378oG00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)