# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.2.dsdl
#
# Generated at:  2024-06-20 11:16:15.178261 UTC
# Is deprecated: yes
# Fixed port ID: 435
# Full name:     uavcan.node.ExecuteCommand
# Version:       1.2
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
class ExecuteCommand_1_2:
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
            uavcan.node.ExecuteCommand.Request.1.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param command:   saturated uint16 command
            :param parameter: saturated uint8[<=255] parameter
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Request.1.2 is deprecated', DeprecationWarning)

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
                'Bad serialization of uavcan.node.ExecuteCommand.Request.1.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_2.Request:
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
            self = ExecuteCommand_1_2.Request(
                command=_f0_,
                parameter=_f1_)
            _des_.pad_to_alignment(8)
            assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Request.1.2'
            assert isinstance(self, ExecuteCommand_1_2.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'command=%s' % self.command,
                'parameter=%s' % repr(bytes(self.parameter))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Request.1.2({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 300

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@j+TW=&s8MVVE>+Ma5!;(!<2q_jwY{?!(0tB&Akk=k3mg9@Y-Yg-BIyK!jQ^odlb-Jr<PozkRBEmj2B9KOTKs@lk'
            'Qyvfx2#~l3B#@Ah_yPP4?u7GIb@yC$mh7&y@=SMKzRUT}cdF*qQ{Va1N9XLn;-O?1W?|IwGm$DDsh4>-5-mT_gG6V_h_bkALquwT'
            'kKy4k5#?Lu@@wTQ<x+8nui{vwrJO77IxuM-m^>AeLvHtDKEM(ea()!>xE1SAwAv>k$c<Rng8`4jR!6*)i_Db8f`25^OzD_bJpD}d'
            '`K@w$e*3mJ%Gb)`tj~=}RTq=9@&zn^1KXQXWpVqa5>YrZ$n!&PxNpeH8%<AA@>U&T#JS6Hruwl6w_+puBAxW^tlw3}k3`%zvfN(8'
            ';sMW$KY){^{77+rzg~!@wbt=&hhD*>xv!O-viPu{8AO1m;rK$=@~-rX(}4?5S)B4i9hAl24yv&%NyTa?dJ1N-YE;H}Di}A+NWqLw'
            'nC{t+DUbVtE!CsDBGSjpE$<l-hdRv|Qo`Ij%!dgnPlqe)$i7|85)r7L3PyXV*e=@D#^?b{cxtBhfjg;Dai8^440u_jy4h^Ta+%~&'
            '#A0n&o(ZNx5gQCZ+8OWaBf%bf^zqL>-YOA}dtJcg{lx<}$atFaVOiYw498PEdD@0@jh;@X>@HtKVt}0-1mpwN${*WakPpdE$WJ2r'
            '#Tn!=;ej&4a{ImFLseq@9zkj5ypM0sQ$pSBQ+_wf%HrYL(ot$*w3+^17I$7!#@Ty-ua%|62Yj8B1-sEA*>KR+kpeEx?TCR!91MzO'
            'FA*s>IvuakKq?e~{8Dl6x{d>GL_BjSIZY!|5mRYl{N1~G6af&|jl9D@;!!TjZ<b5j3vXs!xmE>Z1GDby5EMEh5k}p}q^tgbpCGiD'
            '@U(p>_v*E5{01sUiO>fO+xh$H;xyG%9&wt#Jx^oj-rQbre{+<bI7xVH*<v^E3Rv_U((?Sy+=6^z)(pupjP^pEodJwNQHFTz;o>iA'
            'ECY7{!Odfq<w+7LRFBaX>lJ=m>=0jiIvt?w@Ez5G(Wp&h<I7Z5k8Ggd@@Pt3^P@rtbyEdKVx9#WTLSTDRJAh8D@>dOBC(}q?5+_C'
            '8Q;F>F}BLq_jY#Hb~pS>?I*W({e!*D!z*i@wtsnlW9_g_^>eORK=Nth24E<rF%T~{;73UAuGj0d4-VHlhZLAsJEE(#;}=Wf-mW%e'
            'E}YNwV3t<{K4dzzf5^KOG_Q!H@X7K7(TPq&M3@50uL>r5JrS6TOtku~71rYca5JRgKs+!~JXlu)@{OmI@CmkF=-ANnsCE)_&h%2O'
            'gQqCTh0W?S-tWBk-uC<(C|ZjH`F=6Er;f?~-j#O8-`m`zsC?x><_76Ij+?+-WW7Aamz41!fQ{@}RV3FH3>`I7peL4t>LNQQ(Z?8z'
            'q@#ISisr#p2ESmte5rCm9_{@1maKj7|06;^{N?X?b90wOzhd-E_slVMkUT+qgi)!sw&xikuIk-A1*Yu?ZjnDiHxhhRWEQ+tGq}*y'
            '&V>rfw(mIfkLoJWvEeGtTo|~Kb%Dj=cw~_paC8>hn_eS^6zxd!kYY7-){7Lv!Sx(lps3c^c+Pk;UU4*11!9IrdtJMV1GFtdZHbF2'
            'IXmWwvoh5YT&>)6+feCyBP&{-cR9hFRM>jOCp&r+u9b0<mt4HXvO|d=UZwaSOJO0T3?ZXIjSWDRGw%jDYq71K^8zzNfnEn@8q`ay'
            'j5C<q6d_H;S5bF@9v}-kt~2S0G}V--P-Lvu5EW!lfABLSSAq#Y?Kn&QY{?b!rL_$oL~__>s@K$s<;OflyD`zw)A4GUo1x`V4#o{3'
            '1{|TLc@suupbW6t5mtvmHl|>GFbK@b<Ba#<AFYsSI05B>NI>9BVH(qTlp^Uv%)#7aK6Fv3asgSQb6^%4Bz1gO&!nYm?y`}p!Adw<'
            '@$xvLQR7QFeFZNDB(W-NVF%X_V70}ya+5ODMFsRKeYKrkK}a3}f5k%*j-?7Db|C3gjYg5VHsz8NvV+U(>+ORBYdMvhigRK2(r|DJ'
            'H=f0fAcjsUMNC@=Vp?dknUU@cqCBjtDs{SD)GJL!(P9hD5Uhrbjv3-vba3MgasEO+W<6|HM;e8#;v;?arVAK5B?4=P(Qu4g>9t4E'
            't=1=;^dM@6Y$=HZMJ^S+s{cr0mLMl-=&Bx_-6et!42)EteKfEwId*-Y#sMej0ffyw162Wb-WBPxI7Y0n!e!CLC!7g6^f|i_9U$0}'
            '^ML5{0zJ4ul{bEjdP)F@U3k6h!GWE<jrKIrx7hwoxjA#yncl*=Eeke4LHA?zGU1JaG|(A@zz}d4R4q^PBg<G#71QP_1+uVKRA(}y'
            'Az)hCVOA^hma4L{BEyaX6EuS)`YO?LLZO9OU^*x7DZ)IfOUqSB>=u!#FIV{yR}t^32qM3>n^L!<0$>oO0;-SbC}O>%twwN%#Z~P%'
            'k9sN{SZl1*5pG0Ar!Zkpx(z$h;EMB_NuDJv%PC~37<5HwdmGf2t#)(?9vJ|nFRPM-yQ$`Z6z<g5v<LWmETU)`Eg*Jwliw@eaRbL$'
            't5Y)bI7R>+CN20-PGCO_JW|{}MGmMD&xT5c->&dx!H^7#G!n$K>ijshx!qeF5#{%Yd0cc?QxQ?AjB&n4{x)5s;qMmP1Xjffr|hrP'
            'U1o~+dq_Af7KhVDz#-CS^lbuyD_%p(HYhWF8}(2Zu~t<eJj(QSRicOs2a^z^sy9vaIh{2ESDH>-lTrxB9jbshsxm77gio}dCU%fo'
            '+!EMQmZM!%8KCs7Zf(>`rcxtyXc|0^X)n@e%fPjF0~oo}kfBrsl|rIsN5tzSH-lPYU`p!O&AtIdRwEqhQ<5W^DgFDOThhPx*7|pI'
            'ZT)bs^DLcY+V&jtZpXExItq_i5z$lqyb^m>e^*RdpFkjKcpjNLQyE*LO0N$zl_UUrY~-Szn#X}iN#259YBe`@^2zGipsBuyMXCZv'
            'l-N>ajRc7R?u=M37&|vjhvwh66q@sOXxcmN&Xeuk^=F~Y_Vy_@-(I)PVq9VkARnn$N6<*bs^kReEMhEEA7d)J2>YAW*=Ho4-SN-X'
            'Kb~KI1{wvWR;37z<4r6$<?6p~$<>EySK%NEcE8;@*g80D?;biedO+u(_1os=CQdUrkl3rtQK3|9o;nJx`Fj#Iqf?E&8gW|Dv2{ZC'
            'nCKgrV}q7?^)Uyc_ei5mslI3f6kCh!TCr_!^G13OmQf{Mw-n>K(bSm(3`UA{7ku5^64+J*@Ob0r57JijQCTR{Cd@K}Q#ms%8;Akb'
            'z{F0(Be5V_<tf<rDcA`DS+V`qi>(Kg_sG_gz0p8DxT87x?FyTeuXe=PeM{X;=uC;D*^}>6AD)$pV&arFakn7iEKkSew{?{WhmsmL'
            'ji<?Xs6`e(Vn$+O<h<9UAP`knXuvd1|9ML|U954swE=K$Z9YrDd}98lfSJf)R^_C+Kpm2V6j86yJBZQhsym4x_q~W`(q<lv+?NJn'
            '@<f9M%*gAjt*{1n-4|j`7yLDO*Y~wmvl=^IHF2|V>Z@ux{*SpsM<bVFC~~VcWsVmWbI|3q#l5jj%iX~@ZL6xWG547R9ZV)Sz|(m$'
            'os)lz<wO+c#(qlhyF>Rg1?A>b^1KvsNe-lvugIbNx_n)JOMXLsSH3NOAipnvDBsD8vwkS(G(;`7yjFbB@2L|J`lJAS6_&fjJw5^n'
            '*7m7+`qVtj;xzq<RJSb7?CVUO?9<b?%B5od(`9i=YWkhzwnUY5^>4*NSuBVXV4g0tiU*Rs3uWM^qMzH=KKdaeD~mgvF2gz$2#o&h'
            'W1pM;o#ivFM_Y7#RvP;4;hZmd2Fr-d{7Q_M*U$xiv^4>=N*mO8tC*SDYXNizs)GrY3kcc#(`j+)M~arWMr?E4MIn)$P8>a4WU3{A'
            'R1#$U9GrlncN_??&`qq9r2w+~?EqOvqQ4+7x<o%QaTk5}J`d@*dfgo~-j2p?x~W@q>pgn<=jPM+74_nqS+`g~*zCIH_Iyrv&5QDR'
            '{C@$1=wex3ayQWT%jb6%7e<f&y1kIkc<%0@<ym>BT$J~a5$6Fv1?asF*u4$Ny(8q0Zx)*JC)eapcjeFI&zIyc<S*r~<gev#<ZtD>'
            '@^|w0lz90EBw7BkIPDX*VpHzCc&0cHJiDLxQeO(vbJzXM!N6FLJI0zB?eQp%M~qGWKyX-ny0Wt}KlA!uKDUebym*G<Q(xF;Hc&RI'
            '^zzjiFKKG)f5PFa6xSR800'
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
            uavcan.node.ExecuteCommand.Response.1.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param status: saturated uint8 status
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Response.1.2 is deprecated', DeprecationWarning)

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
                'Bad serialization of uavcan.node.ExecuteCommand.Response.1.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> ExecuteCommand_1_2.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "status"
            _f2_ = _des_.fetch_aligned_u8()
            self = ExecuteCommand_1_2.Response(
                status=_f2_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Response.1.2'
            assert isinstance(self, ExecuteCommand_1_2.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'status=%s' % self.status,
            ])
            return f'uavcan.node.ExecuteCommand.Response.1.2({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@*>?{5@E7;gDdt_2h<;18m#K?(5TMA5{A59GLBwK;li?ye@7kjd=s+j}SM?JP61rH4U51sk0NVu!>}#6*ezrtj=t'
            '+v`aa>V3J{otbx@_j#Xr-hFuJ`OE2v;%CoggILE&m1$6dC*nR26R5IC_A{x40cVfTK_dDzjJtyj+@`zq$USfu?GzJf3d-SxJ>D@Y'
            'k4&y$_maab<$VfqKIdx@Pphenq1sr7C^t}-{XS3QY8!MWQ%$QXYz>qaGW8*kd@~$xy5?l_z!Ue#*`tgbqeMu%wYyF6_W-}W%Gty7'
            '0+M(K(F}{Z;mmlLdu`8@PgktbirJM^i(U%xLTaD~YIk}^SttxkAnh4+%?bsNxHha$Svq{zo>|@s<hNDpG`HxdD5HtTuI=n8rVUZR'
            'RXiGKBM))LPSKRfwX=s<EF)*%>mmdSbe@<%t_G%fx|@SGRYx0UZKX~uQaH1X58uJF!_f!L3ZBFB_)!`BjZU}LUFopSO1<9bbR1r='
            'LC0`KH4dZ-psY|F=sb!*>(x9-29658#*>^_d4G#HSkDNOFVim8Ds67)9Z$BP;1xT)s(9qzQc9Ki;kclpIr)Uh&><na^t!<3YYR75'
            '+6@o<T3zNz9Hi0&+Na<X@a)8(h4T62hQtg(w7o3!)bR)*CSZ7Vh!DRdo$Uk4=^>QXQkT_Mx?eA~7rt%Gc|_;uAQg0SoI_w_knre^'
            'FB#7bN<|_oGT(jjf&HBP*6`#TwK-N_T3oEPies;KcQiq#N9Fwrgf5c4lgfLk=cXVk&ob$&JqF|8eqfv$fw5d`*A^SyM%x3q?t%Ct'
            '63;@$6?uRG6_5iA>CZJy+!F?iN@++S8i70p>d<~bofrY-hlNDG@_?dTDM$;E7}&Z(-jIS=Ldj7EiX=RgKNYE5MFhSY*x~;pmxUIw'
            ')T-TNjdpvfpljZvlXP|=j6h={ROD+=-am+m8gjFMr$L_5l`F|w<su=&4P;bgHV$rT2OQYh5#waxpmb#q@?$)MRlJPX@ft2*13S2c'
            'xA7MCFv7do&&lFqpgSIMFP07a23r;D5HqhHCSupJCz+PHihw2(U>PR^vq$`2B0^`Um#K-YFZ;KfWSEnmke{LSE#W{WXkjE%qhvys'
            '0P7?XZyEM%mWPRmn1WuO_;YtGo4jMHY$X)O*N#?ye)Ws-mhx%!v#K{JXS~bKGUS?&`RaS8UlS3y4I+NRn`@X*&<k6JwqwJz(u_Yl'
            'd+dfVH;d;EY#XgT$YkbhuvZX0=!cRrA}EW{mqQ0wDk?73XhV%qP_x2K`{pu_W0Cg$vk3q2vn?`Yt_I_?c;%_P*sMI$A@$O%j6i)U'
            '4=K;SNPUZ<0blonBfd=$zaIaLH*%g9?Y5PNg`j8fC?3NTc#`@oiR3Z~q(S1iMZ)L<-g_PK;9vvqx9~gs{v!T>5AhNHh(F=a_!yty'
            'FTOPRE0qC%BP_o9)VUTPPTDi1xbk~LF$5mdU(u~cE>=Jn>%-=x@1f=OviP(l;CFmJ!qaJLiC($sD+#yLCEuhA|1p6tMmP+J!(E}?'
            'Zu7JUZOFigy{dPo<n{_}crjKF!uVGU|EB!#<pZMMzn^%f@gJfa^l<XeS4{e?)qerp9U!c*2><{'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.ExecuteCommand.1.2()'


    _FIXED_PORT_ID_ = 435
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{_KY+ix6K8Mo71Hj}n-nkKChm5$PzP3<i-KvhBk$6hCvySBUDw4?$}&d!|mnPhfmn2YT#0;Ls&AdN)T4m=g9PdxBc'
        '1WyQ%pxh;RK>P<h!aH}$?>pzr?CfTp#7Kxr9na33%Xj&GzwbNW<of<^Tzqsw{+B%*_MO=A>Q>AnmwE0htmE;zWe2@5h~0$e*^vz%'
        'ZMimY_d}k)mCwAIe=(oV?y(~N`IN_rmC$oBk=?V%J-3G`&hW^Cmh1aGl0!C<D7BL`8d>as<+C2PI+L<3oB4G=aCp73!|gQT3qh~P'
        'e5c-0+vQo!+Tu~{20pEL=tX`1R=zU1vhOSTs}R^?NfNmoOpf!<VfkHjEJx+pfhCuF&Oji;a#+HYYP(GjBhuF0!ieLS{Mg;}xwGsi'
        'e3M7R+8wbvZen@d-%LclGKIx$2D|m3WG+6Com?*#qG|O7ylc`cXf*M9-paH4tvG=NSmaa}x{-Fo(d>||%#&yPEhn(^>@OR7tQkgp'
        '&f#4bVwrkWY_f=(EHM+o%_IoTpet`9=5KOyx)|NzUa&n=H(unv6GX8Imze4u=0k*tMg3WGOTL|pLvFiW*B<QQ`f|}ukR(CR3|W+n'
        '>;rY8#Pv7LZiE4^@F*xZ8?#(2nCF>(keF%AP1oUmf&p;5$vVLnH_tx(%*URo=P<`9WpMFOc6t|&M-l7i*#j>!JjIjer77p>=_tCn'
        '$9vdGqubOgKeAF2kBVtA1M6pp;m45KZqm<J-p}sSj<LD~rLprKUzsF_s@eOkju+?I<AtOH*FxxI^mm@!ecnx!yc_tbCC%=#f-uj_'
        '-4==ay-wh{z{T+<?**_!f?!z-dBl<+s>Y}-Tm*nv%uXx>zReQuj~z-%)5wVX6j~U6bT#!n0OF>R2dypUr9A(7KD|<VBkqVLZH#5i'
        'dZ0y6Xz`FI?rtJovwCa?rp1I8<U`Re){^$?xjsUKZZNF**F)JMimB9NG=F81#!kGkQd56ZgdN`rnJ?L5HSKUnbOml<&54@mjGH04'
        '7)E;`&JF{{ps0j+?8)r+^JWb00D{ZMW}Jqh=OTKNKw@3vw{EuaqZ>p$gdKh(IxrfsnMnJZZd{Bkp<g#>N)hveKyZRG3KD^N5@_Z$'
        'h$lc)yUEO~$#-lX%Fs&Wt{wszzdml5=A5~()@;tNE?Vas7nWD8jkTrrOY^OUb!mNZzTKesc`&QN`LuBfFa%Qt#8V~sVUnZ8dacGr'
        'd%o2s!(4CiP7o-5ktA-c1__A^<>R0?POBd4n?WT1kam<+Tp}slNuD4&2_gp;Cd0C8+~nOZx07=wuW#08%`UTnn?4N(;(?Lup&}aK'
        'Z#*T353zNvB~8z~LP^Xy+>Njfo+2b`OZpz~oA1BBGWit*t;9j^b~ZUy*kpa}rAEtITUsKkyu2aO1n%4ROT(NqyJ>_Uk;!ZuGMd}2'
        'Cb<qbk$Gbm^kk->I#13CgKdn3(~&$SMKk-F3B4e@*wRXfFEszXCutwLH6p~5pZS(CF>#)6YDSNPZn8}oBn^=sAygDd+0&R1r*n7L'
        '1=F@TlgJ;S8xFq4V+mfJ49=9Xb4Ej1<{gFpL0s8^pD@>tl^IwfiU9NZ_CO-H$B<cQZ+Z<IlC`~nIb^H8k{)FY){{9$1}LJ{PYfk|'
        'QjNG+6+B}!TI<MF6rg1g29mfalH+X_Dk-DDgQ{9hwGD;7F_5Be7?(oKiMWhc+{w`cbIn#oo>uneGYTb~c$MtGEx3e`n-DTe)JOwp'
        'pBcOOtZpuMl@^%kaO65LQ?FQJw#r~?Q<ya3R}pud9>5EMUwG2sQ52A)93GoR4WS`}_=BD?sbUZ5DaT3bH>Xt~pPyf}KqT#k>2}LF'
        'k^GoONH>YsHv)goNt3?hQ3l3!Pz)$SjndMLZi31Hn{8or2qbL^)(3+?tkjQL7y8i(aR4PydB74Va7HkVY0Qh@^giZb?l$Wyt7u=K'
        'ED2Iz7Bxtu_^y~qOBdWFEmeS(a5QVAzDJ{~OR4$_TJ)&I(%8ZdDjz^<iECF)iV+tY=-PdSoE=U`9sqyVfD^WbYYXf^rIQ|wAX8~d'
        'Ima<KE-frHHa4W>6mG7ca=BLk1xIjWNZfE@=!jfo1`>jp=16bGRCn55>J(9>j|se3Y1oPqTS$grHF&flh#}Fz5+#Vz7v*Ez#b$-2'
        '5!kN36<oXH0LD%s$C{4UuW&29HpseqeZol>MNQwF4n0nmi+ES(A3@Awr&JoMs7Gd3j-UgBNmZYG)RQUMS9zbt0Vl`-gv~StRRMO!'
        'OG0_ELadNNc~RNN84Ee&Ik^xWAk1l{0nz6fdT@p!uX>ES$N|I-w4O1bKyz)eF-r7xbN!Cg9J}gRZK2$<1RJ0bZ2Imigf}u$FNjeH'
        '^Z|#SPI-cDNyaLpm^ODKAPZ}Gg(qVg0;Z)M#-$=-T8EV^GUO;QK{-euuM$0nWLk&?rc>oTS(wE|XsIai)gr>(6mx8gxgP7d9*X=z'
        'ZgO4IwShr|3aH+rqlnawwi>`466@Ge8g<>MC#8|44p$>$I)!n0(k<DM25ZhMCmE8kB&U$1yw~B5%x$Q)WV9noFfRc>HiZsJs2c^$'
        '7F?bB%Jcwzx4GxdAO-kJZqj?!*e>BXZgp~I>iaOD!lVQr!U^n$fm<$9PvHYf#N(l&@!R3XI2e*(UH}KNSf3w9HkW(zEu#D`F^{tD'
        'T*N&Jl?vw@q;HuuO8%~!OTa4MVdVYUBFl{Meisg>#e8Q}2q;AL8T}f9;H**7vNXzA-3B>SS*)%Dgn4mrQ<S*Gg}q^jQPd};^%<Qt'
        'Y!#ZSxTZ?MsVby_IEXR||Bwx(p3-(GwU{KZ={QBY&>kT7%`Gn$m5i=N3e%K$uGC&spUnW*#x5{Yr=f&gW$Oxwk{uDRD!ENmOD33-'
        '@^!hdjUuZo9EwwtBASu<_g{Oee@_(k@6!B2d#!buPBIO7j(M-8Qc_`sCu9-PbvIL8?8*9DGi7lCK}o|>FDX0~o6{8O#eqhb1YnQF'
        'lowM|-{ujOx1g7znyZ|A;$k*vYLojsa&1MF*pkO(3E~0VF|nRqIX8`(=AU~q&B?+vjb@{Dp|QGf8MWEkI@#vU1(__WB~}mRBjsuj'
        'H4?EZDM57>F;-F>W3*g^{Uv?&85Gaz_$T8Z&u=~h4UAG$r7(`-O)NN~>Oc0R>cfSqP!IvT-e_$sZ?qe$ZB>nK&^c&f-^9ewX$A)p'
        '*~%OQie~djQE0*6!>AdYYGi9f)ryL(L+WE9Z(xozT5J@@92C7<0m78xi#9;8)y-8|Y|C!mpq_(d6p1%2WwJC0C^Op_3>O6*@O9ZG'
        'kf{jZF{<Yes;%hOl~ATlOvwzY${8bBkM}4BhIS$z@j1~di@?4YAtwlAR_0g3ml}}YJsC@~qk(u(M|0%cS#!92l_M(smLi$ZnG#2{'
        '3%7|6Lzaqs=#(|oTi|}2MwRkgs!D`IPIbz}Q~KKpc<eus42p??@<!<bn`^JofKi<OeNQ-@DsZ~I2yiYhT_#|Da`KLV8H#?aeWDwv'
        'eJUZj*DdQE*l2D}oy6e#uE$~_Jr73S6bZ~^@DdG}kru5jrvP`67kowy{(`)VeyvVcmE%=uH~FS$Rnzgmq7EI6l#5Z3%UV;Uc%hkt'
        'n$r^ZiA-9m2VbTw9b*;sO$9oLOlp9q({R)$f2;U}XU8j_60A;NeWoDad{CSgSH+x&gfCtbUlN(PA-*Zz6z_<)#dpNF#rMU#X?DbN'
        'IGu(l#pXA%d#$d!!ySt%0Lyjq)$EuBLxQy}N}d)a&pbOse>}I7XNT8=*xgyDr*Gxc+2m7swqFGFon&9==G6L^#X+9c_zo~n4Xx~S'
        'n08PZSP|b$WojRM$cXdopsLHT4jBTYKXUe?qu*IRTz|Sw?Xx_gZx6>U!D2{8WM=7NJimb~@ZIGhpy}G6z?)`fQ?><=9ViZls$4)w'
        '`kzjVBOfX1#yqjjO^re#yC78baL#n=97v^tY%>KXAm|kb0xZ;tRb?rFtiBz<>u~gQ;?v5}3q!r=qwCC}<LXU4XuKVaTTxS2sp~y>'
        '`iJta+M=F%Bkp81m`$#muS}-YYn~De|93Em8q4B>>OemzSaYg2c>KqeS~}*r>O+euaZH>LCrOCYfS(WO-2m*~2ISu5;s<vMP4UAU'
        ';zz6E$Kof`;-}(0@iXyr@eA=w@hkCb@f&iy_${0)ewQ7x2wQ%VH?JJdP6E&B6JKNrPW9YPpE*o0)+ZEWjkR{widBo5!ygDP>$}f3'
        'XD7$D|HYM6*yqY&vQN>lkENlcRq5sRF)!tpgL|!_E2YIhq<1sK-TLlm_Q)+iMXKrfz!|5;uy?J>-Ulfar!f^!r`oD9Mzvz`VN4b4'
        '@+(&Fc1zt$b;+d-OLt3XNpnM$R;E1QsH%t(HgT<NWel_2%EWCF&)EHz=9izp)S|v{c5XptRti5=mB}s$k^zsYTBQo!rlew*!{phA'
        'PNU9<D3f~;<%AYxb**j9Uus`mYc0RrSR{!aS>!&o${bZ(%bJ3CCdHXJ(%-#CcHXy_o$u2-Q<qXFV%qj>d#J@#DNaf0Yd-b-gGd>w'
        'prsKp?%InO_gBPNpKr}K8|_Am1o@QwW>kEGs<hA5sa2OrgN7t>ziQ?dACQNI+P@c}rYb_onwbQ;(5{rh>KqV^R8P_@A+<e|(H_X4'
        '1Q-$Qz<&dm<yBZ|b^dv)(Q2(pb1ji{mEOIo6lF6?h7FhJ)-;iwVW01W%2?DLkj0HHH5(P~V5N4DWPJ4~>a(jy=yHNC$LR7fT~5<w'
        'hAxlM<t$yEqRVr1d6q60=(0eU7wFQ&<qnBEo7g4UjZatd>uiyCYRFQfY3J%;>|K(b(&t#I#bc%H&z2ICu>V&RTz#2D{!{b%r1<my'
        'Fh8w)=oaY-d+(l}-kBVqo&eiZyXT&<DW^vN5JZzuu2rx8bBL=4$QDPlT2v;kVvzRHm&v-X(dDajdA+oA^LvxGwDi}gN=Q5P{{X>n'
        'f8kRk000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)