# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.200877 UTC
# Is deprecated: yes
# Fixed port ID: 435
# Full name:     uavcan.node.ExecuteCommand
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ExecuteCommand_1_0:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
        COMMAND_RESTART:                 int = 65535
        COMMAND_POWER_OFF:               int = 65534
        COMMAND_BEGIN_SOFTWARE_UPDATE:   int = 65533
        COMMAND_FACTORY_RESET:           int = 65532
        COMMAND_EMERGENCY_STOP:          int = 65531
        COMMAND_STORE_PERSISTENT_STATES: int = 65530

        def __init__(self,
                     command:   None | int | _np_.uint16 = None,
                     parameter: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.node.ExecuteCommand.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param command:   saturated uint16 command
            :param parameter: saturated uint8[<=112] parameter
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Request.1.0 is deprecated', DeprecationWarning)

            self._command:   int
            self._parameter: _NDArray_[_np_.uint8]

            self.command = command if command is not None else 0  # type: ignore

            if parameter is None:
                self.parameter = _np_.array([], _np_.uint8)
            else:
                parameter = parameter.encode() if isinstance(parameter, str) else parameter  # Implicit string encoding
                if isinstance(parameter, (bytes, bytearray)) and len(parameter) <= 112:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._parameter = _np_.frombuffer(parameter, _np_.uint8)  # type: ignore
                elif isinstance(parameter, _np_.ndarray) and parameter.dtype == _np_.uint8 and parameter.ndim == 1 and parameter.size <= 112:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._parameter = parameter
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    parameter = _np_.array(parameter, _np_.uint8).flatten()
                    if not parameter.size <= 112:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'parameter: invalid array length: not {parameter.size} <= 112')
                    self._parameter = parameter
                assert isinstance(self._parameter, _np_.ndarray)
                assert self._parameter.dtype == _np_.uint8  # type: ignore
                assert self._parameter.ndim == 1
                assert len(self._parameter) <= 112

        @property
        def command(self) -> int:
            """
            saturated uint16 command
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._command

        @command.setter
        def command(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._command = x
            else:
                raise ValueError(f'command: value {x} is not in [0, 65535]')

        @property
        def parameter(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=112] parameter
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .parameter.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._parameter

        @parameter.setter
        def parameter(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 112:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._parameter = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 112:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._parameter = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 112:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'parameter: invalid array length: not {x.size} <= 112')
                self._parameter = x
            assert isinstance(self._parameter, _np_.ndarray)
            assert self._parameter.dtype == _np_.uint8  # type: ignore
            assert self._parameter.ndim == 1
            assert len(self._parameter) <= 112

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.command, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.parameter) <= 112, 'self.parameter: saturated uint8[<=112]'
            _ser_.add_aligned_u8(len(self.parameter))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.parameter)
            _ser_.pad_to_alignment(8)
            assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 920, \
                'Bad serialization of uavcan.node.ExecuteCommand.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "command"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "parameter"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 112:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 112')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 112, 'saturated uint8[<=112]'
            self = ExecuteCommand_1_0.Request(
                command=_f0_,
                parameter=_f1_)
            _des_.pad_to_alignment(8)
            assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 920, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Request.1.0'
            assert isinstance(self, ExecuteCommand_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'command=%s' % self.command,
                'parameter=%s' % repr(bytes(self.parameter))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 300

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{`t>O>ErOwH7)4k!d@Y<JeK^CcbeTXVgd&C3b8jPEyOV6dSi!5=Khmz9yhK!#g5n4$1OIKLHB3ixyfCc*F|}WK%TD'
            'EYn?<0lLXD=qk$q1zrQZMYAZ-;PthA=iEzjW~5PUIktngHehOoJonu5^PO|gnR|J2*ROtdZb1A?PWbC)XgW1L<biEC_Pa*I;WfSK'
            'wS6zNBc3G(FLTFk!$)&*-RIeR*~rhcpJml#k8Zmz4>D^YIk*r7aWjeo-b=Duca1i%I2ju&O~b9Zp2=&|YrGjpe9CLL4cDyI`A=gW'
            'Mp-hbukawWJr_CdeKY_3UPcu<@XPGyS+ZX@qA0K%FgVQK0ruO-UQ%Vr?irgqW=9}RH;u^9Bb0Kx;eLSH+ABbD<PA5pmt1aMbtAsS'
            'gI?|S>kT{79qukgRz`<_dD93Zy$woc)?>-B`GOG+t4+Z(hL1p_fnQ|xEO|r^Bd~xGnB9yv;)bOqdz;ccS+Ywvy=IpDWg({}e!#~}'
            '-m*a~l2e7m2skk!5?P!?o=?1%_!t=O5+~Jyy1^Z9b)=@f$z9V6LIN%!@)?W=5dtGvA0;c|=~(FVrroleojGh*Fl~5I<h6-!1kt8>'
            'K%F46-6hfrfZ$yoc;#e$*oBtiIK=fL5{I1FCU+ws0JjsP;jM6T=7sa;&et+9$5Cl;YdAT+jmLw)SkID2-!$MZ-1(6(<s{zib=g6k'
            'JG>1uNeEcSbIwoDLF<I|lywTMpX>ua`bN`^)-&oS59f~2TL`7T<DR4nI#iC{r8k@~OHLP(c3cZWN1MNA$$?9DB;{Rzueqd2MfdzH'
            'A=@zt*V_%xu>luH7;k%EhX{gY&gX#<c|muKHZ2<h!1`fwbjov^M#SB|q^LAf2HeHa0{TO<vEu+BwovZTR}3fS*?(qLI+%tHYce;+'
            'Wf=8n9idR?K9B6}M7p83jWsYW4ET|_Y0VY9g#FsK3n79ZfQ;R&BzrNYV#mPoR6*K-l&bmPiuemjLQUze{NC>J9<9(_DcvK#tN3|u'
            '&ojE4?n&ujK5pNZXLK*fMYVD~+=1`=`_j>UR7>dr`D_s9I=C$z-A@ms^r0TUa2M_!`o=NzAblvML-`yjJ$y@QdWa6C^x-Wt!4tTD'
            '<hI7s!}Q^lJ|by%!Se$+_ULVorAO!^DLvL#26zh39^DZydXyeZ>2P6bkma!*kEf5);go)FTbY0Yo*%y>zVtEry_9~x$6oLh_&t8d'
            '{OED|{ggiOjq(B&(46>IbI`}>6DcL7ZBgnczcojCf|8V;lzhlH$&a%?byw!2PtubqJyp!v<p;FV(|2tS`V>8t($lx}42&Q^4YbeP'
            ')w$`@^mIzAg`T<3M(+9?^ch-B=?`vOPZ$C8&)yR`=m`BmN=G}sJq0|g-TocBXY<l$>1ax8JF)|ef-%qCQ<>-(t)+ClgM+F>!t?ih'
            'R{9(rPw5Lgwg`-bacAy}eDrzxLQ2nWMa(Gh9xqVy;(e2ao}p(`dhU*F2BTr@`THs>eUY9^=|nHO#t~mH-FG?Yc{-8Om+#nizyZcz'
            '_)g@eFVUA%`pWh=JPUJ7AQoT!&g7#P=qo9G?OWLwxB!nIey2LnSLtghy|@Ll;Qbidb-v~suK1NfP_O}&4zfX&4zVGX4zppE5=K;7'
            'WmT1qvvHM9unCo3WEWL>g<VnUJeybPHFiy<*V%QITFg?Z&wQ1xu{D+6WH(j1!8TNyvQ(w-v-ef{0sBCuAF>Zs`Vsp`r6048Rr(40'
            'M5UjyPgVLE`%I;uv(Huf1^Ys!U$QS%`W5?1rC+nJRW_iofeIT`*kFYXDQu|1h7~qkVMJl1!m0|ZR@k`0#w%<>VG|X0QDGM=?25v!'
            'RM@=2<}2))!md@=b%kB8FiT-ph4~8eD{M_+YZZ1=fnJMkC@fXj`wII&VIL~&BZYmeuul~Bslq-}*yjrSLSbJj>??(Rt)y{-L;v>^'
            'XoBBn8x`xFf13Vm5bN@L+@B4i#Q*mF8CIhM5Bjrv(w_<2-u3>B+$!hagZ_;4`r%);KO>!<`roEML!D0v?>^|yivCRE;6Z=Zzd!3m'
            '%!B@Hr~O%hu5pR42mRR{_GfZcdeEQUkNym8Ei0P5KeK)Vw|iPLY{-T;wPe_kP25IHh7H-;KW|I6QQ1*fh8t;?mhAJ5z-aRbH|b9&'
            'zn>&w6yWx3d7Ff>?>ja(N#u!*+<bGkMi${q%M02@MBqEIU7+>@9*NCEVuuA~xvyK(a7eMC-Pz?ey>g2;vS6IpMI}{x$@KzG>}X_^'
            '@U<rQ#lCSQW_28I6~4W!5i&-m<`|oty{uoFe*NmKzA!hl_|{~7T7P5y^5o()ZVn$w2B$n1CoXqStJZMW4((96vkN9URPd`$FDy>h'
            '7tt^`>%8H4a`RlAP|#+*2*m~EL$BRWtG2ODyg>Xx?E?PO*v1`r_#`&Laj)D9Ot3H-*0{k5Z?$+cx<GhssWwVlMl<q)btLCeEwkp5'
            '$BV6Az6N#<@mGnSqX>g_VS2+Ul!P(+S^@BZyCFQE$v?w$_K$y1<(FAK6FB(qTiN7rVUzi}x2Eg*+{_GG<v$jzI0E;rx}{+*kX9VP'
            'mw*_}Cdf!u?R*En!HMsI&<%%^*o|yQjPboyparK#aUjkg7|k05^a9zfKjlhTe`bH*k+hG0Ga{_h*M6-H3|!(%`EiBNYelPgJR<f@'
            '1KjEdo{&8b5pns!l$P!ATAdpL`5knFgKzLqfHyzsaI%b@lR1>dp$duqPFyuTH!^HDlx8p@s|YZcuXZG|+r|<A9_Gf!U_-RF;~6H}'
            'YF$dtgB9Q>4pfK$g=lpnO$r}%M;ubxP2NYNxrX2(0WE^i6T9*l$>FNuODO}-0abG~<un-jT1SeSroG|An1G9Tg-?RIW3JI|k*m_)'
            'd_<yz<Dmhx|Ek3WgzN~BQKCi|AorQJjn8W2YD;PXBTdfRU?;m>uo&&mU~*D0X~35u?l|56FL-X@NsR}AhmJCNNQwh8Ib<OIK+h0W'
            'Y4+$T=)}1OQk8*xY4WlTiDYq_*sU^7M1G8e08HqtYo0r1#?iXSqXuML)8wv9s6kws(T+lb@w)=tK_FpMH?$#xfLO5`8ZFQdIfNc4'
            'F;dgO5{A1O(=g0%0&w~|jDfMM#=5jh?h6uHUJRHu8eSmtT`>|_7r9GVssJnEXjF?`2dTPQ$-_gSMH|l#<=BE5<az*73tZcBPzZ66'
            '13h<NA!malk~_d3)xZg>mff^q20Ry(Q$vu+WlB27Bnxj$O-(N>2+1+rY&Yg&E)Nvkgd0uZhGT{f&_%=(5QJf-@MegIs+vx07Eu+*'
            'LutI=)N4h7Em#a8tAR(m1knUKj7SP1^$iR+Y{6uOr6I6wcg4GL+W`zS`5btf&U#mF#m5?2H|LKyX~hoERDFk|<pSQy*B=WrOEboE'
            'PcrIZWtWb?({KcjG>Kbnu_U{4-A6jW39JE#%{YWq1+dfJvZNQg5-Ug{y(sNt_Jtg*bAl0`jw4m60jAHBc;h5SUiTTnD;$8>0If$f'
            'P=L){p5C13Yh?bm)a=W(uePAvRRK1Dg16+_?;_sNNNq2KLSP->(9V}U%UBT^tBhit+ztR)z{@E-86pW}TAZQZQlwS$uo6Xvpn^<L'
            '5?QdWVtV$`v>+B_I(c>tEo_8EXvrvXB@@eDvc`-R!*+~@?bwiYa=FoU%x(e(AygpMJ9y4cXopjE;0_Y!u_HBV*+E-KBT5}EDMCDA'
            '$i*?vGCLx1p7Y8<nn+k8r=X;~-QcEJ+o0MK(GIJG;Y0wCB`Xg}P&e?5rp4uv#&UT8eOI~TjKC7$O1V+*QEjz^V?XZb%-D6ofD)4e'
            'd=O5M{eW=AHsoFK0WQS-p_1db!L@!cM8O;n9At#~;mA#si@Es<ru-IW9%<dNfIAo}T{&Mveals&%-=OK16bv226}(ASY<Zl{T4VJ'
            'nYrd>AwVIl&+uCh1V^<pEeoUc)vdFJN{iL<05P1<+Y%)<=E8O_#4zfk()tGW8ci9Rvbe@d!R%Hj2Vy76F#LU^XXz<z2c?!F5?D2i'
            'VY$dXfbJW+dby}%@@k|oO^N5O+6(Km5x}*!4UA+r6rrn{d4+_F9VT8`aucYQ2xLlJugiIxP-K;bL(wJ4M6;>>{o9V}-=jtSJ2N@8'
            'I9LBMb~4kVkNI6)E=h$Io)JYv%U+7}Vo%iHd8RBn5GZMk*og{Hg`|p+UNkg$NdVd7a?FdNvD@SUmbZ{zifXQ_^9hU5kfxTn%LBV9'
            '6D3T^!?FZ%0Nf#Fy=GV6wAnQOw<FUWD@-%Zrt7ay&rbaqYO}d{w9S7_iN&J3#A-wNh-<Y2H4<i3R08WP%ve#;#^iD#_Gj|mr&B!3'
            '_D{q=+~3**b&OI}rC=PHH-X_MRsXspRZkSEf`SmR^V9W(s|$<Mvx~ACUBEtQN*x&J>1LoI5$E(ffs$wQK&H?lfA^xM)76M`zp_@8'
            '+1kfL`mk=m7-6(fE7}|=dRIIMQ;aX10D`SXW<{|rj;eR+Igkt^aSJPA#F2+9a}$WcMP38)b@?lSSc(8VT6h0}wH1D}1(b0TA~J)l'
            'a{5Tt=536Do|!O@xE#}}5kU660&+qE85QfR<_Zna?~aHi@rwq;gKW)Vy&WaJ<*T6R`n{!COt7bf*6j6L#D^wIMc&h8_58NL-7pTi'
            '%5R}6CLDCCSuQ-KzfF&a?lV!RnCK|4l`d%V+$%`18K?i-g;Sm!>3SzaZ>-DrJrJ)?TgR+FSXJwPtUp?Rwf?faTNxNwR`7BNFZ=QG'
            '7+#Lz<te<JfJ>b0*G-PqIHve)BY8+~*=yX?aRt(CGn-8g>!BAz*3dC|>zKT=WH0`4>_(RCoA*L{Z65EwmsJzxxh&abdH52F>f0H<'
            'S0NUsEE(i$U~~LIB{}ZL4Op4<fG@>jY3aNr5@yLBSr-5wv>;HQJ@ew`msp;!jo0w!n=HZ?JC5j<5rSkGOnP1nW*d-&etWei0`s-0'
            '2*f-y5Yd)Gc0xb&R9TRpgx|1R+4KfTO`AltZ~37LgU$0LJTDNt#-V4$f?z2IOaka+3<4hUmq1w-K@iCoGXUz~{0ZxVbpC5S2mKGt'
            '8z#0(TMqcc(+=H?9C{UBDJbtQPl2OLlI~XkhSIQ+41(nZ>x?Qfo-P@(-iH700MTz|;l?F-=49A<o4sEtZ!gz@DIJXaJd(eLTKla7'
            '){u1=ML7n*{3C!;DWQ0@03cr;f$O(H@ba^8-B=!l>+JFv-X4cbb@_Sx_yS(e;N>h{Uc}2eyqw3&1YTZ(3&Lpm735=`UVat+CVO?n'
            's~ctP`o82C#E5(+E6^>DHOiLvQV6UT=jCeA*Mr@j>2?9>eWPPB|MV6cRr<cKVf|zltbKhSTDv%>6AH5nH{rvZeIDY_+W!MU-psLx'
            'HUIz'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
        STATUS_SUCCESS:        int = 0
        STATUS_FAILURE:        int = 1
        STATUS_NOT_AUTHORIZED: int = 2
        STATUS_BAD_COMMAND:    int = 3
        STATUS_BAD_PARAMETER:  int = 4
        STATUS_BAD_STATE:      int = 5
        STATUS_INTERNAL_ERROR: int = 6

        def __init__(self,
                     status: None | int | _np_.uint8 = None) -> None:
            """
            uavcan.node.ExecuteCommand.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param status: saturated uint8 status
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Response.1.0 is deprecated', DeprecationWarning)

            self._status: int

            self.status = status if status is not None else 0  # type: ignore

        @property
        def status(self) -> int:
            """
            saturated uint8 status
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._status

        @status.setter
        def status(self, x: int | _np_.uint8) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 255:
                self._status = x
            else:
                raise ValueError(f'status: value {x} is not in [0, 255]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u8(max(min(self.status, 255), 0))
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
                'Bad serialization of uavcan.node.ExecuteCommand.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "status"
            _f2_ = _des_.fetch_aligned_u8()
            self = ExecuteCommand_1_0.Response(
                status=_f2_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Response.1.0'
            assert isinstance(self, ExecuteCommand_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'status=%s' % self.status,
            ])
            return f'uavcan.node.ExecuteCommand.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@*>U2hXd6ixUDPWUJ^KtE8+R%sFN;HILLD)E4f<FrwT6WLBBDxuNr?v3w=_0BRg8)7P2XbX+nkwDEL^$AsKQU7M|'
            '>^h0#5{c9=p52+bbMCok&fP~xUc8zdD}MH3){k|ZRG9`Pcp@I~Fo7zIWG|Ci7;yIF93-Mg!?@GWz-_rJkKIFe*-kK#rl1^-*^_Of'
            '^2p>0_AWWfQr@EwGdW+6cv?+m4AsU4M7e>w?DcpWS6iSnnQB^9Ve6o@kf{%O?3=-O%Po#Cjy-jcojuODF-nBATe~|He;@EWtDHSL'
            'FCd9`5lyj}8_tY}x!?9o`E<oPt(aa-wdkf0FQf*#p!TMBoQ1-$1k$cSw^*Uz5!Z(GC`*U$+4C#gf&8{=o#vMO6lFB_#I>9~%d{a1'
            'xQd4ZZRR0P*$J95xpwvli)G~O`yGTpfzA^X$hE)}Pxo@rrs`<Jw5`;MMG9wj@Zr07VKDk|v4R(I20t!?pK5n%oz*sLuh#30cH7}4'
            '8?+5qRO3LZ0Llu*fzG1{v|h`Tr0=NU>paPcl@GRggN=+J`7-Tct<vI#-tlA`3eMWeHN_+UmQt$B55@%*i{np;3>^}(D{l&XzP4~{'
            'wbk&zuh(Us#6c=epnVEH0nbhhS}31SZb-}!L_5nuPaTgCVgiQO1_<#>(%Au^oEt!CE_YaMwe$6IYvJ3*oJTY>2dSWw;~WAbgM>$S'
            'eaU!kP%08xk@?<}4;|#>w+AQRtj)3d^3qbRSsZ(<v#SX@Ju2^4Aas%R-BjLBJvRkWd6r3E?GYG<4+7)t5R8>ttG3kWG+G|W4G+X0'
            'k$4s|uE+xnsDK<`K!2`j;=V9gR7yhv(GcVjP)7~|>husOKP)8jl?N2%N<mtP#K86y@`e<|5=xFTP$c1j{HaLgDkAXpz>fYOxhyn^'
            'rDp9GYqVO+1zqzVouso1VFVfrp(0<0^8P_g)R3D6JPq=cu3Smh8W#x}ZXlx~vr%vpyWqf14;d#5`=u*;ke}drtm0L?f!A>X8`#EW'
            'yo0x~ixJ+#UQQMl1Ksh6d$DZVQ*2FaK+L>)n224|o?%+%Dgv5FfMuKv%pUW9i3pvYT%jhivEtuukztO1N`8jYw}eBPpoNi4jgkpj'
            '0&I{(yk*!6Sso@LVhXx>;?Lc+Z1RqYvXxLAUprd;`L!=bTgqqE*{U}vXS~Z!Gvu0(`RaS8Ul$R$O(K5Gn`@X*&`aBfwrj(*(u_Vk'
            'd*Y@rw~FUB>=>;*%w*<luwM|}?}d^wA}CAHlLH4>E-Eh7a6^qyP_x1<`_>ANW07|Mvk3q2vrRH&uKJ_1IQz_9UaUOVA@$O%j6i)U'
            '4=K-{NPUZ<0pIY0W4=uhzaIaTH*%g9?Y5bRg`lVKIG(`Mc!v5ciR3B?q(S1iO~U8_-hUJEV1E-IH1Rw9{xbf6kMJ@6h(F=a_ynKg'
            'FTOPRE0qC%BP_o9)VY=(job62xbk~LF$5mdU(v0HE>=Jn>!ZbS-$TpmW${@_!0-5Ch^KSZ61{TM*Ai|gOTI}L{$m1P4sjR|hkHW3'
            ')8c6tT9APe`&I95$?Ys{csWuJ!uVGc|EB!#)kC7+zaM+9@gJfa^kDMO*G&4Y)qeq!x>zN!2><{'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.ExecuteCommand.1.0()'


    _FIXED_PORT_ID_ = 435
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{`thON<=Hb=x!i44V|W6hER#Q!10RG%N0oR-z<Qq9k*<A97Ku-OcP$qKpL1p6QzHUiNf%`m-MaMrZ^w)<6RuSZzQ)'
        '7!VKx(ZzraA1ojj89@M@0wE_IbrfJ9bO;hTcH+EO)!p;iS(3}2;+O<j+f)6j>is`e)i<{N<R`BUh=1`D-kK2@c0~)gZ|S!6wqCP&'
        'MXS3_&kd}QC-Lri?k`()zOd%;<lSWG`^oo`a{P$q^S_OF5NaXzn*;G96Wq3%FvRGF+@V>H!+ilVANo-}jQpO-wrh^wgr!bI`f^=&'
        'DvoRL%H%4qM<E|~n@!y@Dpk2$5|^}P?gy6Z;EX%pNT1(Ls6q#RkbEBy*7Pv+tr`ptlD~oJH=!|yO5*KP7PpNyLaJuyp)N_=Y`Etm'
        'wbn8~9Jt~H)}q6WX(!~1-0!Atw^p-4&F0QxXeM+JCa>$jw<Zvon2*PY=dy`#SY;gEF?<CS4ZM?7llY((gunsaH##R;k80+=cxPR*'
        'CyBRdhFeeK|C~=@iRbeXgEuTdi=<Ei(S1(zkc1{Dq3aR1As&6*S>&XgLD#tLt_)SwH@IWCen3DZM81RZfP%04Yr|w&yd4QVUbh-n'
        'y}gFzh)HX17`jd3>3-O=4v^!Ama|A2J^;MUeK%jM&vb#Q+ct6BkVF9|mcgA606^?Suer;doO$l-i)Skdu;Zv?xOqH2wu!`jUtde&'
        '$KKGP7kXY7tQ^DMUhU>KZ^BBcc9V4GleA=>GRx)=a6jG!a`g1N6|N=Jiyut|qcu>K`i^^&DkxAndYe|WgCu@3!?Z10KsxOGoy2=C'
        'TA{>u9)6~n#zoEbl9+5ZNwC(exwZv*ae(or3w#K{SY|!$>!Is++GyRhzyQpN_|UlP)b)@%eL<0Eg!H+CrUmf(W+K}Lh1dYOLtEDE'
        'h$lZv%Cyu9YUWhRjA<D4SQS;F$~_)ho1t`FYwD}OS{U$GqSIW+<`VpCS`L^9J^&cIQH*z@O+~hj<EetM11(xe{}#nxa1w<U-In%k'
        '&--YRZfnsU@^=BBcXqv_+v$!LEv4gjZFom_0$x<j$3qYN-rX0D?xJdo?vd|GxYi?^!qMGyPmAvDniqPZZ{JPF&`0Rr79C92Xwm(*'
        'gr@uGV2eJwVI_D2{ReJqJl#(pZP9}gb{o9kgJTcf_E>s=9&FLWeQ|)d@b0lK%|#E<!!3Fw<22y%jV+I-kI^G7dUR8q00Q10yQ6vO'
        'H|Wt8{bm=x;4RE|{Ep|N$LKd(^zobG3s3;_#9ggHkJHCnl;pfctiN^FGtwt0Y0(pM9&$7MarKk;WIg&VdZI;7WovfG0lD<;d$tBW'
        'Nl&%tled%%j359Fuut97wduF%lPy}#=uBlcbkEnIPtkIVK7HGC!U%vreP8gPL-gqu9d66^6wF!fl<&xWTbG`u!!26b5+7g`jCtn1'
        ';zUPirA0^EdQg^{@a%nGl|Dm9TlBdta|A}hxHAs~Kl&_vu0@~Us4>GZ_h_ayFFY_@=o$Kai@tbAJcH3N_Ur@2mA*h<Y|(Sw+BJ&$'
        '_0j{!gPx`5TJ+^R<{iuc<IjIBc+;2Y%PsoK=6d)%tZ@!?@zt*lKYE_N(xR{36@OtCnBzNND-HBj`dW)#*r2l@{Rql+zUt|Y*kuq9'
        'Y@k3(tW=<bY_LF&up<RZ7%9*)D;MY}8!gat>|B9fU>6GXGP_)$b8N0aud=HJdW~HxP?MPj>M^fCSJ`TT-e5Nhbe*jiXp6N9^gZ@o'
        'fxge)FVGLz2L<{e`>;SiVjmUg$L!+*{e*o|pr5i&3-mMgS%H4eJ}=NO*cS!*CHt~KzhYk%*nq+YimartQjrZRY_Q0VDC|g)5rvT='
        'D=VyAWTOfjEwXb8J6B{E6n3G=E-UPEk<BS=uE?$`>}ru+Q`og4GZkhQnWr$X$W|4$T4XmAsI}O-!deP@PhsyX>;r{;sIZR|_OZe~'
        'QP`&n`%Gb<E9?t}eW|dolvY&ZQ2$+nB3NhZMYHy2Q=gSEFTc<ASqU-zi?7cx8y$F9pWT=GOz`%e*JtEbKL0+{XQW#W|8MIv(ypoh'
        'V(K%b`IM0E!}=_%&!iqatk3$_XWbg}us+*reU@q0sMN2A_1PWPXEG{1tj``qeTKZ28BJQBnLmf_u96H3vLihu85U&cZlff_f^7BA'
        'w<KFHZmBB6gEVtryvx&ly~#s7q(2@1+ZYK#ACG7AZW2VEXItDLp(_q@)5F;cS%4o6*Kg_}f#1Y(0NV3;C=L&a6=ab4xo$<pA=!a;'
        '`;^yk^CRBSgmK~&m6WYT$Mrd}!l7ZpSL@sp=f<H})wbOg`1P_%$OsvqWo&F_Lc2J5X?jMRpPgEGbF4b4U74F0TbRVd;UjTr+;wo_'
        '{PeVJ9`87z9n4R5fhGI0`Kpui3uDy<WXz2!ueq)~JQp_<)EPHKbb<K5ZT6$8sjm^&7k`jCyfR_o2|PTBLvTDRcYOmmjEvQ<bHW=9'
        'UJuU`URkURlZIXoU4IS1d00uzh4^@O)XP_a&jIdAbX`R#RR!yHJ0lXt>}vQh5A+7`eky&2_v}x9qRJ1FY9jRDx3}WS{){Jcvu{pT'
        'wb`jD<jQyF%_s!%tvESj&XY#u!w;Y6^*Z24R;=^{zs8B@0@5{`lgJ4zTa5AC6@UeyhmkMtAL#Y#1n2_X&3{jcFn`bfXG_=~zqv-3'
        'r?37@9T>RC7t`wsf!hdI@Onh#89Ip7^Id^^6rjeX7gHLR%_~)|3(aq9HwgGT4}|ijHyuvowsRs?WpSxOYJc0V>aG*&mJ>)e=%JYz'
        'n8R1v7+Fny5fmQQ#@E0@<hJeV2J&i6V$c0$m`_}&5C#g?>V&F9KJ2u(K;Gu*L(yza%pw(97@;dp<<XLZ72T6q`mPP6rew-x(Dc<d'
        '78O;!;=vf73wwnp0o`WTa3{)T$!|U+wS?oP0p$OR$%P78A!<ghHG%=D%+yU}Rw2_3Nd=5FIBx=<tY$XFaHj{8ivml1z65s1u>+*w'
        'I+-L@?)xqZ%HRRXF36-R1NH}W21rW1i%tP2?lq9IG~|n86B;;@g-K#Hayt?JG4g$2p}nTM&WI6(Yr>D};BgIuJJO;0QO-sy3<%oq'
        'GRzJL37$HE1s(*@ikv`i0DU+^-~tgt6%{z4JH0v$!*tsRp|8Oh7`vjcNv@=_Ac5&dptE|-^`*bdM&i_&?-HEKloj=8SdAPTp*p9M'
        'mxq9gCf*-PbqiLI@c^(EdTq%;0oX;V=&ATJJZl^^xvluaDhOf4wCX0TfcJt@XfQGvrlfETGJj=!d~$wXV2<WyIT06Yxj<l#-l#%v'
        'IC^LwMMPYof-uYw(hTrYRo#w^%&O8ma6Fr-n~OrXAQ*yI1BrGZq6+QMLy3r_*Vmn(0gGjv2E(?TW%v4R8!)WoahTJv*E)PFzE+XD'
        '>HMfCjmQR=vS)MToX;C+{4vq9)FZt2B&{AIyA%Z8h9h{TNpv+uNOol0M>x<EhykdZQ2?$A)J}cVlv3<)tbm1-qU4X!SLGniiHY!b'
        '94Si*(0!i3juU8kop%H;b5O(@P(7pq0c>_+ve(g9$lPs_*>~2y)B<tSLfJqS+(pNF8}$vD)N}(#1lB+unrX;0^=09)ax2EgEgv)s'
        '=CU(M1_%P47FXyOiqvvyRwBs|P~Zu2AQR#$x@Qkr3uu9-lXusU!+MaJmb4N_PGVY%=7_$mTee=aYzw?jiZ_amS#{7sFcon1Hr}%n'
        ')ZtQXbq9=7+mRGCEWatR5vdNB5CL8><l-7<?i~?0^?CUqRX8l+QxH?$tZ_rcHpsSwwL_H9?GO}X(M(Me$n{;lZgP30F%J(w?+Ul='
        'AqWAE#2e`zR#$R$>^D0KGjbeYpwvmBd|*!C{Qz*;(q%8m00VJ<RY~=?#?^jmh=|!P2uKgo%aJ{ci?#VOy8H%u9?9JipWA3E9X?-0'
        'dh@7}`|k>w0$t^+I!b>yi!wcazX1Zr$sD5>2_OjbGyK)1g2QU=mIYJ#($<cll4F(BKy*8BH&}^<zOdP?VrcbY&V3zgjk+{VnOtM0'
        'V003cDq`Ep(EL5UEA-^NgH%fw4y+tR5H3;)p!i0nC$dZ?%|<fT<oeu^dtrVy1bVG*qDHbB3Q<(`G(*B*hmKdK+yt^E0-h4%b-r#L'
        'lB_&&$f_jiXnOMB|K3vmdnn6)r^dz?W~*;uB{M1Nn18Oykd$%ZDUn1pti>oz_C)@jddjQ<fs{s%>@bs5K+0(8SwWMg1mHa;BAyM6'
        'oI3Y0y#@D@Wpf>sPmqlUH?_ze?pt-~C}Bw+<SB>^${nEBt9R5*y{!4;mRNH*W6dO+tX`U&8Gj3Mv)MW1&5y@Lu;@&&nvgzXthOOX'
        'La&NMV4j5@E6mE66fe~MskHWKC(p9{6ZQ}N8*898Q?jfSm?QlrOxQ!}AGSp56B(&MAQ<f2WOaUeeqnNEL1v@#SO<+41_rvS87N4^'
        'J^i+!q~6?@E;RGs-CEPGYQ()?nJY?f?cpVTh#N3QFfCBCG6$00Wf#m8?F$zGW2=xEk!*{r>g{|EFhfh+Fcs0G(8b7H2VfA9TLXWc'
        '?-Gbm1j?g!)*qN#;iDx~85beKGsrBb4`xl?L>uT@3H^w}(XHw}c;Cx_CpeH{5nokDP=Io`g)NC44X_7UnnS!DCf(_)faut7$$|;i'
        'lu(*ox`lnHB30yFRaV#D0(XMQ??}G|spxP}s74-ma(Npr51gmMb~4c>Ud=^N=c!Z>pjS`-t3ywDe4yi-46U{%zxP0WecC)`eqoN7'
        'Uz)#L8c+rX%s(!v@MmcUHV3g8#O85qj$%{B<`gthyjwFkCgkYlll6G7*05H&p<xixEF+nT_iKS0f#cB7e{1N!lXxfov8`GX@0xQ1'
        'YjqBL-%ZM~@=OwMGhO@+rQlf!ep(^oQxcc>DzF{*RN`Y^RD<B8`Ft@F(WU*NNRY%kWNHBOAQJ)l`7<x{e#i1`Wwe4jI7x`#b{x=5'
        'Jpjzmp0qR{OxD2>{c^g?2-EPC*<$J(h^S1#L7^zR5-o61LUdTL^n3(TQO8i>H|$lRy}6#$(DTHqa41_bCs>R?EkW<38G=gUW}wWB'
        'z>eg%8KCVT|5wcmQvTyzcm4Ox=>}Fz8}9hS+cq4PLuc@-g1mR>G6*^c>HG>{uocwe5^zpTolqsh3nqi64*zQa^z#|$xFoNg95HqF'
        'UNP@pdJ`t4rKry<xglx}n)}T|=3zwT80hBjKq+_Rs(3V0K)zIg_AZrpX%yP^rDvg?S$Yn;Ux22(^ddf<#pWC~FJbdCHs`T<1)Eo~'
        'c?}xWq@^*O$2`4s5&p(IHB?zAOxU$u@nJ9%`DK=`nH)2f4PU1ah#9ZQn9)~=ox<sq0_py)<E`}Rui3ED_p1%_+6*xK+Ad^xc3US9'
        'oEMV9mpA&n6d!!-)w2DT6#bp)YO1*>ecBhFyy+KYa(L2~?$JK+v(y<scVLi-0!$5#F32q(%!0D-nPeI&K0f;Gt)|+G5%<cxmhJ=K'
        'lw@8e4Me2wGTvh-!l)vO^lqPu2QW7c{e9P)8k>IoN)>lJ<MZPpW}sEed_&at;O%*Uc^KxVbu16-Ihe@mvCcAjP*Jvm%ApjMnb`$x'
        '?8?IB+3NInCnpf2lM~#*O&~+2jUrm2`--62^V83jdR8uMW#vcHm2v+qO@(mTGYegtHyvpg5`Epl-E7yFjLN)S4;sa-pmDGRjk&Sv'
        '7@J&}tRf=c5vL*9=}O1Ou&l?@1fadu7I0f`Q)b`&btAQHD@YA?ASJRvMCj5&M}j9aT(>7L5Nz>qLoe*D?%UZ%4`SQzL|vw5fJ-xD'
        'uWOUl>a1Yb6k^x0D=l*%vCSgPhKq_U3dNqM!&g1YEUbGm{c-DpvR>qNbYv=-Pha|b^sax0%@4782b*`X`4Kih!{(>h{3AC1fXy$l'
        '`2{xrgw3z9`4?<{b3Yt?JkUSjZXPnx1$V~25(LXqPv~3v9)_>XKT7)F$*KNnPU|mn3V+iX3IES?ZRuaJSA&M#P?oMCvG*?u($Sj)'
        '!5hj=g5di~{~!p)adh(t*Eg`0@GIfe)g>tdI=_`&T0<u6i%WhU9y6e}SieH9{RcLGz~=WoqG7*M?pioMOmmm0R{38CCqbE@J^%m'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
