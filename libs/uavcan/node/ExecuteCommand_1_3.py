# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.3.dsdl
#
# Generated at:  2024-06-20 11:16:15.165413 UTC
# Is deprecated: no
# Fixed port ID: 435
# Full name:     uavcan.node.ExecuteCommand
# Version:       1.3
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

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ExecuteCommand_1_3:
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
        COMMAND_IDENTIFY:                int = 65529

        def __init__(self,
                     command:   None | int | _np_.uint16 = None,
                     parameter: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.node.ExecuteCommand.Request.1.3
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param command:   saturated uint16 command
            :param parameter: saturated uint8[<=255] parameter
            """
            self._command:   int
            self._parameter: _NDArray_[_np_.uint8]

            self.command = command if command is not None else 0  # type: ignore

            if parameter is None:
                self.parameter = _np_.array([], _np_.uint8)
            else:
                parameter = parameter.encode() if isinstance(parameter, str) else parameter  # Implicit string encoding
                if isinstance(parameter, (bytes, bytearray)) and len(parameter) <= 255:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._parameter = _np_.frombuffer(parameter, _np_.uint8)  # type: ignore
                elif isinstance(parameter, _np_.ndarray) and parameter.dtype == _np_.uint8 and parameter.ndim == 1 and parameter.size <= 255:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._parameter = parameter
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    parameter = _np_.array(parameter, _np_.uint8).flatten()
                    if not parameter.size <= 255:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'parameter: invalid array length: not {parameter.size} <= 255')
                    self._parameter = parameter
                assert isinstance(self._parameter, _np_.ndarray)
                assert self._parameter.dtype == _np_.uint8  # type: ignore
                assert self._parameter.ndim == 1
                assert len(self._parameter) <= 255

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
            saturated uint8[<=255] parameter
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
            if isinstance(x, (bytes, bytearray)) and len(x) <= 255:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._parameter = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 255:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._parameter = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 255:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'parameter: invalid array length: not {x.size} <= 255')
                self._parameter = x
            assert isinstance(self._parameter, _np_.ndarray)
            assert self._parameter.dtype == _np_.uint8  # type: ignore
            assert self._parameter.ndim == 1
            assert len(self._parameter) <= 255

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.command, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.parameter) <= 255, 'self.parameter: saturated uint8[<=255]'
            _ser_.add_aligned_u8(len(self.parameter))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.parameter)
            _ser_.pad_to_alignment(8)
            assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
                'Bad serialization of uavcan.node.ExecuteCommand.Request.1.3'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_3.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "command"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "parameter"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 255:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 255, 'saturated uint8[<=255]'
            self = ExecuteCommand_1_3.Request(
                command=_f0_,
                parameter=_f1_)
            _des_.pad_to_alignment(8)
            assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Request.1.3'
            assert isinstance(self, ExecuteCommand_1_3.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'command=%s' % self.command,
                'parameter=%s' % repr(bytes(self.parameter))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Request.1.3({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 300

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@j+YmX#V8J>ZKovj5KTv;%P99M;zWTuUxV%!8XJJSP`VJ_*JWkn#x>8jIxj$2))s5&(>O+o@8A|z!*DZ>Zj2S50U'
            '55^BhO}wLtCMG8S0RM(}@p;dws=jQm>~6A|?y7TnFVFkD&pG|_sqg&hBXjm&@nA9xvoLD;nMf6n)Qh|uiIyMeL83EdL|NRqAtE)v'
            '$MA5Ni1Mv+`IYjea;do8S8*)TQqC239+)%_OrDC#A-DN4A7F_KIX?<`+=_K5TI~}N<VLLP!GOnMt0P{>MP|xk!9NmdrgTgzo_?zO'
            '{8qU=zkTa#<tt@z*5}5gs*A~4`5czNj_u8;vbb$ii6|Ty<oO{t+&5(9^`<8&d8>{v;@sspQ~g+kTd@&+kxqJd*6%9gM<VVUS#B?4'
            '@qlN>AHc~{ez-WlUoS+{TI+bXL$Bb`+}FxZS$xRP3?jhOaD1WH^RD!Y(}4?5S)B4i9hAl24yv&%NyTa?dJ1N-YE;H}Di}A+NWqLw'
            'nC{t+DUbVtE!CsDBGSjpE$=B2hdRv|Qo`Ij%!dgnPlqe)$i7|85)r7L3PyXV*e=@D#^?b{cxtBhfjg;Dai8^440utby4h^Ta+%~&'
            '#A0n&o(ZNx5gQCZ+8OWaBf%c|%%h)wv{fP;_qc$|`-=Oolkqg=!?L*dDUPRj@}v#r8a<s%*`2<K!~i=v2*~@Zl|Q<@ARm+;m!ClN'
            'i!;b$!UJW7<@S5U2dl*RJ%ZBAc^})Jr-ZuMr~Gb|mBmA~rK8lsXfyr2Ebh3ZjI;LuUn@(CTYa6B1-srN*>KR+kpeEx?TCR!91MzO'
            'FA*s>IvuakKq?e~{8Dkxx{d>GL_BjSIZY!|5mRYl{9U_w6af&|jJ(}H;!!TjZ<b5j3vXs!xmE>Z1GDb!5EMEh5k_6lq^tgbpCGiD'
            '@T7ex_v*E5{01sUiO>fO+xh$H;xyG%9&wt#Jx^oj-rQbre{+<bI7xVH*<v^E3Rv_E((>%i+=6^=)(pupjP^pEodJwNQHFTzq2e!V'
            'ECY7{!Odfq<w+7LRFBaX>lJ=m>=0jiIvt?w@Ez5G(Wp&h<I7Z5k8Ggd@@Pt3^P@rtbyEdKVx9#WTLSTDRJAh8D@>dOBC(}q?5+_C'
            '8Q;F>F}BLq_jY#Hb~pS>?Z>xv{e!*D!z*i@wtsnlW9_g_^>eORK=Nth24E<rF%T~{;73UAs@LnZ4-VHlhZLBXJEE(#;}=Wf-mW%e'
            'E}YNwV3t<{K4dzzf5^KOG_Q!H@X7K7(TPq&M3@50uL>r5JrS6TOtku~71rYca5JRgKs+!~JWy8y@{OmI@CmkF=-ANnsCE)_&h%2O'
            'gQqCTh0W?S-tWBk-uC=!C|ZjH`F=6EyN=2J-j#O8-`m`zsC?x><_76Ij+?+-WW7Aamz41!fQ{@}RV3FH3>`I7peL4t>LNQQ(Z?8z'
            'q@#ISisr#p2ESmte4%ne9_{@1rmTJ7|06;^^yTk)b90wOzhd-E_slVMkUT+qgi)!sw&xikuIk-A1*Yu?ZjnDiHxhhRWEQ+tGq}*y'
            '&V>rfw(mIfkLoJWvEeGtTo|~Kb%Dj=cw~_paC8>hn_eS^6zxd!kYY7-){7Lv!Sx(lps3c^c+Pk;UU4*11!9IrdtJMV1GFtdZHbF2'
            'IXmWwvoh5YT&>)6+feCyBP&{-cR9hFRM>jOCp&r+u9b0<mt4HXvO|d=UZwaSOJO0T3?ZXIjSWDRGw(V%Yq71K^8zzNfnEn@8q`ay'
            'j5C<q6d_H;S5bF@9v}-kt~2S0G}V--P-Lvu5EW!lfABLSSAq#Y?Kn&QY{?b!rL_$oL~__>s@K$s<;OflyD`zw)A4GUo1x`V4#o{3'
            '1{|TLc@suupbW6t5mtvmHl|>GFbK@b<Ba#<AFYsSI05B>NI>9BVH(qTlp^Uv%)#7aK6Fv3asgSQb6^%4Bz1gO&!nYm?y`}p!Adw<'
            '@$xvLQR7QFeFZNDB(W-NVF%X_V70}ya+5ODMFsRKeYKrkK}a3}f5k%*j-?7Db|C3gjYg5VHsz8NvV+U(>+ORBYdMvhigRK2(r|DJ'
            'H=f0fAcjsUMNC@=Vp?dknUU@cqCBjtDs{SD)GJL!(P9hD5Uhrbjv3-vba3MgasEO+W<6|HM;e8#;v;?ah6@-wB?4=P(Qu4g>9t4E'
            't=1=;^dM@6Y$=HZMJ^S+s{cr0mLMl-=&Bx_-6et!42)EteKfEwId*-Y#sMej0ffyw162Wb-WBPxI7Y0n!e!CLC!7g6^f|i_9U$0}'
            '^ML5{0zJ4ul{bEjdO`q*U3k6h!GWE<jrKIrx7hv-xjA#yncl*=Eeke4LHA?zBH@jKG|(A@zz}d4R4q^PBg<G#71QP_1+uVKRA(}y'
            'Az)hCVOA^hma4L{BEyaX6EuS)`YO?LLZO9OU^*x7DZ)IfOUqSB>=u!#FIV{yR}t^32qM3>n^L!<0$>oO0;-SbC}O>%twwN%#Z~P%'
            'k9sN{SZl1*5pG0Ar!Zkpx(z$h;EMB_NuDJv%PC~37<5HwdmGf2t#)(?9vJ|nFRPM-yQ$`Z6z<g5v<LWmETU)`Eg*Jwliw@eaRbL$'
            't5Y)bI7R>+CN20-PGCO_JW|{}MGmMD&xT5c->&dx!H^7#G!n$K>ijshx!qeF5#{%Yd0cc?QxQ?AjB&n4{x)5s;qMmP1Xjffr|hrP'
            'U1o~+dq_Af7KhVDz#-CS^lbuyD_%p(HYhWF8}(2Zu~t<eJj(PnRicOs2a^z^sy9vaIh{2ESDH>-lTrxB9jbshsxm77gio}dCU%fo'
            '+!EMQmZM!%8KCs7Zf(>`rcxtyXc|0^X)n@e%fPjF9T>UOkfBrsl|rIsN5tzSH-lPYU`p!O&AtIdRwEqhQ<5W^DgFDOo6^7c)cSXG'
            'ZT)bs^E91g+V&jtZpXExItmY45z$lqyb^m>e^*RdpFkjKcpjNLQyE*LO0N$zl_UUrY~-Szn#X}iN#259YBe`@^2zGipsBuyMXCZv'
            'l-N>ajRc7R?u=M37&|vjhvwfm6`J#PXxcmN&g1Rf^{1iD_Vy_@-(I)PVq9VkARnn$N6<*bs^kReEMhEEA7d)J2>YAW*=Ho4-SN-X'
            'Kb~KE1{wvWR;37z<4r6$<?6p~%GC#JSK%NEcE8;@*g80D?;biedO+u(^;_oVCQdUrkl3rtQK3|9o;nJx`Fj#Iqf?E&8gW|Dv2{ZC'
            'nCKgrV}q7?^)Uyc_ei5mslI3f6kCh!TCr_!^G13OmQf{MvlQdG(bSm(3`UA{7ku5^64+J*@Ob0r57JijQCTR{Cd@K}Q#ms%8;Akb'
            'z{F0(Be5V_<tf<r3D^k&S+V`qi>(Kg_sG_gz0p8DxT87x?FyTeuXe=PeM{X;=uC;D+2ik1AD)$pV&arFakn7iEKkSew{?{WhmsmL'
            'ji<?Xs6`e(Y(`>Y<h<9UAP`knXuvd1|9Mk5U954swE=K$Z9YxFd~E)PfSJf)R^_C+Kpm2V6j86yJBZQhsym4x_q~W`(q<lv+?NJn'
            '@<f9M%*gAjt*{1n-4|j`7yLDO*Y~wmvl=^IHF2|V>Z@ux{*SpsM<bVFC~~VcWsVmWbI|3q#l5jj%iX~@ZL6xWG547R9ZV)Sz|(m$'
            'os)lz<wO+c#(qlhyF>Rg1?A?G^1KvsNe-lvFUg_&x_niBOMXLsSH3NOAipnvDBsD8vwkS(G(;`7e53e)-%}?d^hp8uDlB)4yL|)_'
            'tnE|t^r?B4#cBEzscu=E+1Hsm*{7#(l}p9^r^@1#)bu;aEr}}W>fefkvRDu&z&u@O756837s|j-ML)N#ee^>{Ru;EAU50fi5E%X0'
            'M?N?GJIkkAkF@CetTgo7!#Q8_43-g@`IQ(iUq=`C(bfdeDs52Xtzu?ouLaN@s17DnE+Ay{Pp8GHA1PYi8nMka7llN2I&t)Hk*Ssd'
            'Qb~~Yb8rHR-f<wnLN~EamIBD`w*zDyiT;AT=o0<d#9j1V`#hxM>NR)Jcsm-m>85Vct@r5ZpPNtPSJaDdX5C@|VYBO&+w(cyH809%'
            '@&7ptqKjpD$=yKTC!gI}To^t6>-IuE<GH(smS^Q1a#7w*Mw|!y6rlGiVD~m4_l}T1zENn(pS&S|x+{Msf4(GtA%7`<C4Vh{BY!L3'
            'mA{j}r^L%YAj$HN#c7|g6`OMB`7_0N;Mx7em-<qWp1bB}4hF`0)G^k~Xpcv6JYsC}2ZF=u)0Lf-`I*=M@|j)4=lL@fpZdZ+vw^Zv'
            'rI#<ycu7-R{{zu+Un|!f000'
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
                     status: None | int | _np_.uint8 = None,
                     output: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.node.ExecuteCommand.Response.1.3
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param status: saturated uint8 status
            :param output: saturated uint8[<=46] output
            """
            self._status: int
            self._output: _NDArray_[_np_.uint8]

            self.status = status if status is not None else 0  # type: ignore

            if output is None:
                self.output = _np_.array([], _np_.uint8)
            else:
                output = output.encode() if isinstance(output, str) else output  # Implicit string encoding
                if isinstance(output, (bytes, bytearray)) and len(output) <= 46:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._output = _np_.frombuffer(output, _np_.uint8)  # type: ignore
                elif isinstance(output, _np_.ndarray) and output.dtype == _np_.uint8 and output.ndim == 1 and output.size <= 46:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._output = output
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    output = _np_.array(output, _np_.uint8).flatten()
                    if not output.size <= 46:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'output: invalid array length: not {output.size} <= 46')
                    self._output = output
                assert isinstance(self._output, _np_.ndarray)
                assert self._output.dtype == _np_.uint8  # type: ignore
                assert self._output.ndim == 1
                assert len(self._output) <= 46

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

        @property
        def output(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=46] output
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .output.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._output

        @output.setter
        def output(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 46:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._output = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 46:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._output = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 46:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'output: invalid array length: not {x.size} <= 46')
                self._output = x
            assert isinstance(self._output, _np_.ndarray)
            assert self._output.dtype == _np_.uint8  # type: ignore
            assert self._output.ndim == 1
            assert len(self._output) <= 46

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u8(max(min(self.status, 255), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.output) <= 46, 'self.output: saturated uint8[<=46]'
            _ser_.add_aligned_u8(len(self.output))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.output)
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 384, \
                'Bad serialization of uavcan.node.ExecuteCommand.Response.1.3'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_3.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "status"
            _f2_ = _des_.fetch_aligned_u8()
            # Temporary _f3_ holds the value of "output"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len1_ = _des_.fetch_aligned_u8()
            assert _len1_ >= 0
            if _len1_ > 46:
                raise _des_.FormatError(f'Variable array length prefix {_len1_} > 46')
            _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len1_)
            assert len(_f3_) <= 46, 'saturated uint8[<=46]'
            self = ExecuteCommand_1_3.Response(
                status=_f2_,
                output=_f3_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 384, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Response.1.3'
            assert isinstance(self, ExecuteCommand_1_3.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'status=%s' % self.status,
                'output=%s' % repr(bytes(self.output))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Response.1.3({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@*>TWcgm6wbK2*>Nwr8h5>+wyZ8I$f&HMASkoBXqe3;OeQK`XllAoa*FNgZmX)Z89`9Q8?>lws}H{DgHQY5lc?bR'
            '0{Y}X@VEG#?wL#yC*T^GOi%TxQ{VaOJD1lEe)RFNsq!zsD;<P3j2gZrqgA9|QN4&7evtIj#A-)HeteE1-N$3t9i&uTF7A81c(pj2'
            'Py0HK$rL=5A76DQ3tVPsx5*(tR(-fQovF=0#f>-#sWHDrLFQ;S>GxF}HacX}B(|`s`<rB}PGWI+_?hAJ<)T$<9eAsFy~vOH$~mKZ'
            '*lmlK;C~<R+g3$>XhBmHju9R4L*<n31m=F*QzPN(O<2sV#a3^`6fVY&HpuJ_@2KC?&W|YGa9p(Na2_b@{63;A_}2W?%E*yyYs})^'
            'lDtAhQ*RcXBEQME4iqR8?sW7{*5f1jG+w#P7WqLxOoAf6t;^&YvRUN3WZiS+ua`5ju2Epa$qEwRlHa}$C&s8jk>C7`!YWoSl!rBC'
            'b$3w5eTt}0v8zbp+lQX-Y}NTLKF#+4Uw$njO;w=XplCJn8;8*Sbs>A=zPnpB3Ax&R(C<Zv?92%1ICy||dw&=CvGdwhcvtarh%`Uo'
            'Cuxy;`#G_LelLkMsGC`$egYmG<g}cUQ7$n%WgM`EMEJ@4<ZKcL%27PgRDu>uL$Qbt_Sd(wC{kwdFUx6vQ$-mS?-yrV^$%>1n?o|@'
            'u<PcIiZ`f3DLK6#q>FxEZGl>BxKJ+g^2k@oUth-%kvza`DXry)MRi%EWPhtBwo@Op>eY7!VbWHr;xeDwS&x9|1zgLEOItO5Y0?f>'
            'Fq5-HiAm<t%oTj*xiht?sb)OzsuhS(IWI`EDD-;dWtP^ns9I!YONoj~dOCtmJeR;U-lTySl2baO(9`jHV)`Z7jU#K&tHp-cvlNH0'
            'Ez5)T@DEB42x;Wmlmfl315c9pelOA&3Enn!fLCR@c!}})q%10tNZ5Kk6<owQo`QiP)sHli*@I_PuEr6`sZk1!PqbWy6p_M_j<xkl'
            'U3=6|5l0qBWUU86AujEr!3Y)nCWzTw(w54coXP7Dl=$BkEfREMLV@P%R=dsa+N!_0Hak1Nx(d2;Z`CQ|#IM15Wz`Hln*{*?fa+)f'
            'S>$(&5&(!$ALNdAm9ToJBv?fw4A^t+x>13wA`9ya!{@RtwQ6r6P0O3-|B85_xp-l%GcSlApDn426DPbHC&)zyAz5uCkj#N*8j42D'
            'dQ!(!z=RB3=9h;Ec@stdDxjPkLTN8|{pMQt>E+Ji^Ye3p==2=Lay4N_BEd-XfcmL2$B7vhg*_)<b2TU5I6V1$bIzY#URr9l%VW=V'
            '#|4_UwdFxe67<D5xfBaGB~e+LCUVVtU>vv_7&q;JvC`}`m*%_k9Rc!Wsc{?;2@9z*XvmI?B-)UE<Zb9((vHiUvZ(&S4#;~z9lRP)'
            'Cw736$5J9s37{Y|D5IrF9F6*!Ob1?=P{k3dA|yQ2Jua!T0)dl(9r{0VS!{!)cJqQi-{~xubS((Fq^!tt=CBm7RDv?`C<HYaEl`$F'
            '36OFXS?efhs5xE|l#%TPH$4VN`OJ<f#_tWP5lKMa%cq$5EcaRSt32Sh`3?S%-{VjD6aIof=P&t6hM6NI<hit|uy{AW4n22^LSGc*'
            '>#%6&H~2QmOh9-Mk)J9|6!~HKigXV>Yz0%@){3lNMyIJgfB}OOnbEFEH4IUrok=2;1=@m4q-<cK$a<)CzM&0t7@Rwvp-?}jtJw~I'
            '<o;m&@VQ6!&Ug<s&NZY+6;8&U86WKd$V34$rAYlQ-U0bj1wY1*SF}B`t7l%nqQX$e8~^H+cssURsJ1RjcOI|)wf(fWm15#dE5DdA'
            'vtduf2Q9H|fPB8{lqb+BU#pFm|8CW@3F}qA<fD9yPw))_;uLOE<0jw0Eq;O<yh8ldf4yn``d$8}&EN8OXZd^nfq&$m_-Fowf92o!'
            'cj1x$0B8IsTEAQsdJM4Sry!4NS~otE3h}jf9P^L~k5-v5k?ox<?qtl{J;-#2PtUd<oH(WM3+-)sMstNNc`8Yjm!C~|DO(%=0O6@}'
            'lA#O$00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.ExecuteCommand.1.3()'


    _FIXED_PORT_ID_ = 435
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{_ig-H#+!b)T`<yR&8R&SGqkR}NQeWM*Ne1DN0_b`r)jJ?o)8AN2Iv*aFJ8t8UM&-Ri1J)vcasqeLcBkS&!I3s-mo'
        'i6<U-Kt}L{0EzDp2_6vt0WV1K4hbaYckaDaUESNWyF(NymR!?aeLv2}@0{~H_wLJQ{^K`~F6jS?cO_##^TU>#i8SD0@DlHbqUCz='
        'Fp0B3iL$u&K%}F<6TNXF%Gb*)pDF*jTq)k_rsAJ+kttWvd$~}&byI}F5L5i=k!Rf?ibSf19H=z+RG!W(c8?qJA-1}l^O47+Ruuc9'
        ')jk$puEa(>9P-F-b<K8VvE+_Kngwx0E1rASetx~|EOzexZ21`o>~f{jppVH}`AIB)f{yj5vbbj}5TQR2$Z>tHxKZt-=}Ai31|y8P'
        '|5}s<hmr8NBP9++I<4KkZa+|ND566p%g!<u_c-h}gp#HFtKz}^Y9X4|+Q4r+^b<5%__wlK7H@Ym1q<-hZ!Yvo-j^4ObDl9zS)6hG'
        '*ei?QAK0-hNyVBk1_8ukc2vfADi~KxNx@W{uy~+9raU?nY^56A7h!yKrR6*;B0o+u2A44N8|FiVl&9lWHqyVYWr^^DLEugH2qL{`'
        'KUOLpvV^B<W*?}NsvtUKgA@Z^5@}p-HfOm^@-SpktXQ527Wg7k7y!33-j7FuJ@&!JKm2&BggG8E2A2;Pmrn3_n(}d3yyIDpw|Mi6'
        'Hsw0Kokh0@#SlALbThm1Bb_DrZn+|_!1~2`_%Y#LpvGnA&Ejp=G46n%G<V*koken}nSI9Xhgn%XT1h%_EreFH-^=1HPX)@zdw{Q2'
        '(&BD6PRfFvv`97{_Tw-BF7DqE!x(l@2$sD>q+G>mGe$ibAOPfM@xVqLd0dHT?od*iMy4X7(8Bl&yLlJ_5I2oH>yCJsi}K&gmCn*@'
        'Szm5hV{BvAJGumgu1JImP7>*cJLJbOEhc<Szm&adEp5MH5Fte91BUJV;aqW!Vk!?g&F?JI*oD_ROXhEmuoK4#k94-!&HDlpy$HAP'
        'orNXYpEpAeFpTy>oSg@Zk)jmkvG*0fTxS__2M}DpW?7yjVSwmSvBtW^Z;SQtWe}%BgdM&kIxrfsskD7rkX0jV=(il2QpNlv5d64~'
        '0wpm|1C6a9@x+MgKwVj7;@A_34lSj34H3xr_ID0rYiwh0XJ>tP(|xLab$i!6*xTwox87~L*Y-Epdu@uJcNR-<K5bkB48ha@@p27*'
        'nB+pWUblVFTkrPBFfVsSKaNd)(MjCdjTMOt<+FG=PpcsxvpCg%NIR-30VOGX(s_c?Nu2tyFd3HL5KIgP!c$K$(K>9cvH|yin=uUs'
        ';(?Lk;VK&7Z@eXkPi5<+t~NanD<v`K{2;|Tc#Du++OnVV`_7whb{0R2pw&1S-p(c$E1T@^J=gBKds|y%l@|_VuHe3-s5Z<KY>=n;'
        'k}~djkdYk)Hp%q`L*>l^q$idm)rERa5+7kKoQ~qDQ#AK(Fz5x@<;W@_KfUumr;_&JTO&fg@8e%|78afohc=^U@jx9>1<4bXM+lY1'
        'TJ}66#M#<C2#{&Jf@|bY&<zLQ5Sa$AEe4nC*tu+>tm}?J|0J%wI8r=_GGhj=WEEhMIGRWl3^^(b?M*+!hGgw9=04eKY@`Q`!Fsyp'
        '=m15uM#?e5t7gPyhVabMXs@qVF@V-V80*AEk(?dz#7LROAyl<$nr$fborx4J$GMhZPAYV~;*%adG1qES<P~FYamAoSP+lebA4#Dh'
        '6evPQjT&tL>oeyBpS9Tbz-WP)zCf)*W*SyYtTr>4*%T&C#dXA;pcn8$995olM4HCrC|_i(;t&=xh(G9=kt*Jlo_d^4{cObq@>A=Z'
        'E)q$v&4NK4CptgoDawrs$4(rr`MDbFJj#)AeUJf@P}96NW1zqcu-OQ!Lm+KaWPM~1h?PefA3#4^A&a2|m<KEYf-{3@Oygk+r;jlQ'
        'bC3AgSjGARv?R`fS#Xfl<hyDnEnVd<ZK(>Zgrij_k3t&NT*~k(XfY&;WwC`FOg(_q8rOlDlp!uG(5?F_Is1Z;JOTcy11B8Gz?0a4'
        'sFNLyATwpkILBuP*ETlV2M1bm3b!E2h2ATMf-|^rG;RcC=#*T<Vhuq|^R+iK;+<ZY`&CrgHbGP?O<Pf83&jvw4IXU>;%IbmWdt$$'
        'f<9&gY*twsfgMDn_{JRvFm_4=*7U=1Be&Ae4q4Z(PdFKX)Qs6m5(=_hDh9UxNXjf;PSnsuJu16#1T_qdSf741)FnAGb)UuoC#V60'
        '%{)V@0_>dUr14@Su|f*tMPna-F62<>^g`4?uoa^LrO(Us;xa{EvyFOM0Em5PeZ_$SJA0e$*+k!B`*)<~+*Rjl3+1*o*Z_t2FbZBG'
        'ypfTHaRwqV1{{XA<Vil#8LN(B+B`^sEUXn)p3G<nGA->euM{~eHmo$s(4&wE>Om59mC|!UriEC@bcWuOg?UzmmWh(cEFyzLxyDC4'
        '2zfsULGmlP$#pw{2Mi)qkm^HfMYMLb)dcR4*v5|0Xb_}BEsdr+!i>nM3lqB2t+OKywmGk!<miN@a|%f+hJE4d+6K0zqa9U(hYA2W'
        'lr|)xZW?n>3e)w~<pKI0i7>o^5)c`=N$*wXsD|Ub)ybK86v2Q7lNx*oCuBbi90lCGg%79@&xeY|Z(lg`U`T?6F&xA*+ds~1uJ;xr'
        'O8EoIJjS|fsR$`l8adw~ee0@G=kFHV0#?N_C-1LTRc0pd58!ZGEb?cCfI`I2=-U(oSDiX7YopB7ZBj#x#acE%c$mdEMM*%pa5xPy'
        'ih5OBpHr{lnb0)knwWy$RLBBx5@i(r37;xGwe3K)xK3azS&njHJwWbT+up30jAbL0X=*$-xEJxWE5NmL0*p*Iq{vmCWk^))DDfJ~'
        '&A^rzG9}gPdS4GDt0oRrmt+#n4FCP_Q}N#iD*n5*zR}z3K2M!YTlX>F@0yZSS>ZjJL=1w%+>$-bzip<hIuKAAo`<UPRK`{)(yNBX'
        'QUYX;&0JJd^T-n^(OaaKip@1TpRAgVG<7H<kp`Ygl-N>aH3bO)?u@dY*XWyOP4lNyndZUDH0_;s_iB50<9Tqiy?wIH=Qeb)Xi}^p'
        '=p)tY5FClJDk(uci!zp~+88SrVSmf^J`?h6+CLrtcz<&bG%-rWN?{z6H?iQ1s((C{s_&{)g@Op!{dV_Y`=Hm}?HM+DKz-20T?-3S'
        '-3%HMeUv!~6r0UclR~TfJ&l@4SEG+c3|BPSI-zq+)D6thM$4S4%>n5h#RyZ1FWLaX)?&MwZ0pm!37>;x6p1%2#dxk_s>~h+!$ol)'
        '`MN$O(4`3Aahm-HaVz>5XeiSrOlJnea^^@j6hn%Eshuc~M1s;PPmz6}hMY(stGd2Ak=B6x9_m=qCmM(c)0(5+uCi(Rsz)@=TdHD0'
        'JtbPRtG9^{M^i;H)n!ecEr=+~(+2(4s#3xsr}}l_sr~K8B8%RmCS+owyi>ct6V@v<U>2wUbt;@LS2*3?1UR?1o+n`b!{QwQGm+!W'
        '`otcfj)_8wa8UCd*l2CdbYk%RAmo|Uo<~MLlnQ2YM2!Z_$g86*zXEqv7a~pv{8jR<&TDP4YP46i-SjWjQ8l&y4RxqBGA;%q*IZNP'
        '_`zllI-J(HSGs7KGx)k}*%)i6&kX1wGO2+)ohP$C`Ok(=L~(!PD#7iK%{2x2=DqTgye`*dDkJ%?@?T^jUy+}epOasbUyxssUzXpH'
        'Z{)?jt}mz?q7qxaTHNOjf@9&k!~opDFL#TJE)0pR?Nae{sd$#fIr<X@{jxZ}A7{bwKD~XtTqzd+x-8DfnC?mLN`jJ({xvx$izRUk'
        '%+rBZaVg3BU<Pg~4s%`FCl?u6S)4Vz4C{~~F#1D}{mtw>%LiJIwdnY)RCM=nzbknL$tan*mW-FLpbC6#dkScl8&r6+nVIQh0aOQy'
        'gDI8^2x<RQw>Wc2(Q?))+uU?eNXafvOnP{N1uX%j5+OUxkrNQ~CI<p6bP{W5DS&M54&Ze-`tRjOjH5TE&Y~~ubD!GPo6ex|>ttNV'
        'Ox>kZ@5$R=)t{P2)XT4B{bC7b)9aR<#hlKXmnFyleGH<5WqH+{K)+M+o#my;>tA=4@;UF#Ika4s7v%%;K@#E;;1>aUuK;#m0OZ~f'
        '@|$-GP5G@?<+pd`cjR|h<oD$F<qzZ!<&Wf#<xk{K<<H3R^5<}}{6%rjC2U2i+<EbQ@gVSQuJ}?{3gUA&U2`yGtS3#znrrQ*6`K}g'
        '(-#EK+fSd^SzVla{4ZbJg?(N;Pxh$}>@#gBZB_d5<vBm<n}hq@>Qu^#f6nga$hX)}7m7!2c@=4<mlJ0^G$(s6HM93wD#dw51nQxl'
        'IT$0ZSY3=6vOax_B|l(4eQ5rok9S(~Z)bk`OKiV%g6*;VeA9OpVBTc$7Plso%a!BB+h4An1>sL}MfL1a)U)+y%*-3xo;C_SRRR4{'
        '@~US~s{S0&kCZqP#Ke_p<EG9eu4TerW@aL4CKi2Q=ZRocpSgLu`mdt)fid_(A0`<G>bnXMV3atjU76_wbjOB#DEKhcxeO~ubj&;d'
        'CdU$!Q0T*t$z6^ZCW`u1eUu@NsmBYbgPoiNYO;6~WI{t_cstbHM-=wjfol)e2z~6puyCe(VMCya+fiB8r(V+qv9oX+jxu+@t@Z6^'
        'u65}Op?G3L>q?p05O{rHMpn(Ju^~@;#6P@xm~NBl;KH8~W$`qkJYYrH-RrsQ*LqLyb+=z=Z<0ihY>J3%>6<=G(@!c%xsq{euSjQh'
        'zUwqQzs>GU2ilgi(YBBErcOf}eGDmmBckh}I5mc<D%gw|cb`U#w>QMtU+=E(w0rF?3G$B`l+|@*<EF(Na9Bn?IlBf;H0S=+zcrW^'
        '>da|`T5brX+ba_2YOm2TnU*o0A==t337wFu+2gVaTbvQ>p1%Yx+q<yR?)o!syW8E<=Gr3Z8rM7~cJ;ZX4jZA5IC7;g5h6sbF%}&p'
        'X&&rp&1Qu=+n|}cZePEE)OY<}dc2<=7wPd~dVG)`AEC#S^!O+}w&>BL$38tiMUNNgA?e}MBc(@##~oJtV&Mda^sE0R8`AaV*OmmK'
        'CUhpO=K3YbXNtu#mF&fvdC<&zQ!=if$Gp1w8mnEbZS`brq5aw}er1jSC)U3HY0}`gq}uQP5BXE){kNb`#;hmMr!Oter%#BLhfd~3'
        'b1Bgh{X-?2`AVyLljvN(hiq}7SW0VRRSmM<dV{R{ReF4#9$%~Nyz}+NTUz>6VzGI@^=JLvn<n!n000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
