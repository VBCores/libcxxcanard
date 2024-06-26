# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/file/409.Write.1.1.dsdl
#
# Generated at:  2024-06-20 11:16:15.142601 UTC
# Is deprecated: no
# Fixed port ID: 409
# Full name:     uavcan.file.Write
# Version:       1.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.file
import uavcan.primitive

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Write_1_1:
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
        def __init__(self,
                     offset: None | int | _np_.uint64 = None,
                     path:   None | uavcan.file.Path_2_0 = None,
                     data:   None | uavcan.primitive.Unstructured_1_0 = None) -> None:
            """
            uavcan.file.Write.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param offset: truncated uint40 offset
            :param path:   uavcan.file.Path.2.0 path
            :param data:   uavcan.primitive.Unstructured.1.0 data
            """
            self._offset: int
            self._path:   uavcan.file.Path_2_0
            self._data:   uavcan.primitive.Unstructured_1_0

            self.offset = offset if offset is not None else 0  # type: ignore

            if path is None:
                self.path = uavcan.file.Path_2_0()
            elif isinstance(path, uavcan.file.Path_2_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 '
                                 f'got {type(path).__name__}')

            if data is None:
                self.data = uavcan.primitive.Unstructured_1_0()
            elif isinstance(data, uavcan.primitive.Unstructured_1_0):
                self.data = data
            else:
                raise ValueError(f'data: expected uavcan.primitive.Unstructured_1_0 '
                                 f'got {type(data).__name__}')

        @property
        def offset(self) -> int:
            """
            truncated uint40 offset
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._offset

        @offset.setter
        def offset(self, x: int | _np_.uint64) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 1099511627775:
                self._offset = x
            else:
                raise ValueError(f'offset: value {x} is not in [0, 1099511627775]')

        @property
        def path(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 path
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._path

        @path.setter
        def path(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._path = x
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        @property
        def data(self) -> uavcan.primitive.Unstructured_1_0:
            """
            uavcan.primitive.Unstructured.1.0 data
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._data

        @data.setter
        def data(self, x: uavcan.primitive.Unstructured_1_0) -> None:
            if isinstance(x, uavcan.primitive.Unstructured_1_0):
                self._data = x
            else:
                raise ValueError(f'data: expected uavcan.primitive.Unstructured_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_unsigned(self.offset, 40)
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.data._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 4152, \
                'Bad serialization of uavcan.file.Write.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Write_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "offset"
            _f0_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f1_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "data"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.primitive.Unstructured_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Write_1_1.Request(
                offset=_f0_,
                path=_f1_,
                data=_f2_)
            _des_.pad_to_alignment(8)
            assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 4152, \
                'Bad deserialization of uavcan.file.Write.Request.1.1'
            assert isinstance(self, Write_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'offset=%s' % self.offset,
                'path=%s' % self.path,
                'data=%s' % self.data,
            ])
            return f'uavcan.file.Write.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 409
        _EXTENT_BYTES_ = 600

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{`t?U2Gdyb|&YSmhFVGV@KI+l8NKk^sd4vS!bjCZRO2wR@<B7RTb|>4=tz>d8IqfXvoeCZ7Dzi1w|Kf!FH$3ETBFV'
            '5KwfXr^1hV)T17aqCoYiM?Lyc=*#w;`4LHp)So4}*`;kk<h|#7=euXlTuS%zoO$K<?~Z1oKaE#wa}}>*7fT*@Ez`EXGAC_bES0M>'
            'wW??NJZzl*8Mmz&d|A0OSL5Ng;f-&?ufsw^D_M@i-B4s2=Rfz|dfBhLyxl}CIpz#PyjVByl})EOWg+$#E@BnO_}|vK=ZB44=^l4I'
            'tLhMt{+s0Ww;{{2>~F(w!p7N>>HDrVS@*dY{tcpbp}cJsHq=ioZdaN-`brhkH%mT|>*ii_X_3}Fw7B?d$Frs#Uiqct^J(t3FY0V*'
            '((+3-ccy(2G6FA~o?n`&R(L30Y+N2qfyk}+3C;mc(Te^)919!ImptEeDyCa$1$t1Q6nzb?IyL2S%!*Q~RLfx_6XNitII!p!dh)8T'
            'k#EiDsEGjLoOp&wEJHaH&taaLevOy9WXyHVxv=rVZ%iD;k<TJ3w`jC|$>&Sl<}=*!;}nXQ669A{PP{5!V;NeQxVliEY@ESt)XcKw'
            '&xP!djSI>0N>g+}I(okz`zfVK+Y1}lQl`z+AZdT+`>=8Dr<Nb{{T$yWOdE2kS_>OSHxO@bX0mEqnAnTJXR4S7AB*i*HSU^z)om^9'
            'vaqm##4j3`KB+oo)8|e{Q(7)ry4<1CMEhrN*KON$=XP0YrF*7b=i%?d0?P&7r1)i$hR@LJg)!5a=3~6ZeXAR#FH1A#EG88l?nHy)'
            'ixex$-;CviEJH8Q47T)!PBmG#O*Ca$GR*`YRx6*anND<*-L6k^BvQufP=QQN@D@WMaF&p<*pymSVAsTTe0#Bx!<0}7Z>OC~v;Cre'
            '7+q9!J@fg`M{kYYy7Q~C$X|TXcsac|$iw9x5ox>ma$`}ZO*=(LpEFagS*B5}kld%qYr3P}qCH|PjCjuM$E6Q$jh8<A`R!la8A-^9'
            'dJ;i=#s1iY;*E<fdroO`F5bon@=Gx&T;Ygs#MgD)2`U`dK;=;hA2go9Dxc+*QmyLxC94wNZai1=s&%)_OLUu-qAWIa`es{`SUaP*'
            '!_G!G@3(k`vv1*TFRHX(N;L}&%T>pBt2Qo~&-&b@l;E9QpTq(#xqKS0EXHl_Y?vD@-W3ps0^-(9;Kg@}gGEYt=+pLdu_R0nxwv#Y'
            '<9=|@D)aDxxHkU3*-Yj(Zppl25L~hEmO&_nH-}?02GKUSQ^vilVpxvx>pPzg6^%QB8&$`iGqAX=is5ktrouHW&+u_>s_NdyozC!V'
            '(-X#(x2_PZXF1aZ9E}xl@P^^?Dct!DzZ!YD)v9k)EKDsz%^3w6v#aH(FpTPyabH+vK_M!9%EEoxn4F9JXgS=yQS2Mzm>evp7#CS{'
            '&nWQXbkVp{EMhoZz2Q)d#2@$L=sn(cScjB?f@%ArTAvmOjDcp%IioD-CZ)AUE34Dz9mc}D;U4Cas?#VC2zPMRWnQ`QL7!o~Y21oa'
            'SF2iR<V@2V%{a4|CeyGj=Sv!kbB!VGm<mTq_bqfZn^`S(2W(~wQKOL*xH*%ccSH`wu=pgt8$NB@nw}jsD-{g0YfHk}zr;`PT09-H'
            'T)llO>AHh-`aF9%`8?a+2#WX_oc>Tzi9g)3%@4O0jGM`;_d4J9A3-K7K5m)IZ-3@=Uh(aC=&xuyZ{26}?R)lLC$CC`-)Tq2Tx7O$'
            'QAqbyCMDnH=sT`S3Ye0NsoP^rW=g=c_`O80^|m>tGA&@a#P7_mIi@2E*0=4CBl!MoM>}?g^#$x)JeQ+b=eydmv+P{Jo@v9yQ5<`A'
            'Pak%kJrl5e5+h*G?Q6}R#f-BHyCUHXj$b^GKYNZ{2-x$nt%CFC$oJBLec46!e84Vu<bbm{_rjsD*d=y3VEt*Pk;{vR_Gd4!{(yb2'
            'D<`zT`InA_%U)#P3)uJD@`baA_wteP*h}pD0efXnzG#IuuRc)>_A+}VV8(WCiS=twjL2SPM!>GbIL2Q5Df;Wj5|6#ct_19A8nfj('
            'P?p{}wixVnb~Rwv_PsLbVW2hIUO(2@><xA;V1;y@$u+xi>@nDNRtVS+4!lnEK>Ht_2oH9H{UBfi&1-uVF$=BN_stWF%YMiP0#-a!'
            '9?%PY-a1iE>`hh-*kH2`3UMX8ed1B^*N4G?y>sY{peOqM=v4Tzx7j-ZySck!1`vBNt(tdFjSKq`yBV+_A1P<(jlS=lDp&R{`*FaA'
            '+N*1j>g)Ye=fU1%Ljn8X$hkuV^#Aaw@MiC`4+8d4_d2|ZF@~rXKYnWb*oW++fc@l&@{1^l@fS~Z4eVp~lYkBHs#&`FBkAaH`}lbK'
            '_((J}8qbO5+{DgVHXg9q-SZ-`sHHXwtv2(Wt=Me97GpcISio8QaTk3GXf=eMBWOF0{sKMFc6qn$B3dtXvtQ|Mzl<IaJNc~b@3Vql'
            't2_PH5AL^yo{w66HxKW-j@}!o|JKp{Hxc16Vn8mNfZ*?^hsN1zMe5&ygwO;A`Rvi~3VY&VID!NtdpOjgL!crB0*1lt!LUb;jE%Gi'
            '9)`1fM;Je*2uPKJz-YE}9C0FXkbWErCbF&3W=|y=E{Xy|ElV*MT4KWd35CU#?T)<IF)|WLf<th!@s|%AAE_o3VClG7tUM75Ttq?y'
            '9zHpjwPWXk%S-6M>QNZ2p9&*fctQ#u9gNrJQ{#mxX{81m9oTLC|6_+4O9;Ya;#e2)4_T0rAfrG=gG`R)ASXdifh`qs8p}gog1iEG'
            'jrBvn1pNy1Yp|s=0}Kfa1q_W9pddj(fr7>cVNilW1qL-X1Va)GDKMn5VHlQRSb<@UjlhTmBMOXYY!pT%7*$|YW8*L`!MFnB8k>L#'
            '2__Vn(3k)rflxqbtOhj+Y6{deHVd;7%qlReVQS|km{(w4!`v=Nu%N(#hRF>i2owl3%<iHDiwZ1inBFA`mK0dhFu%(ZEGw|AVS*n@'
            '@KAw=8fJJ!f)xc;G)(cT1gi?HYMA3S3Dy)?(=f@8BzUC2BMq~>F2TA2>l)jD4GA_B*w8S=n-Xj)u&H5=A4~99fyWwNg)IrTFrOL~'
            'LPmy+3K^YBAtyr)ldMxQ<YmaKkk_dk`eo=>p<kzhFk~=PFmx)3f(!)}3OW_VpbUd54C+)CLoy7hFr-sq49hUA!mv)IF(Si=3L`od'
            '$EXaWDvat>9^*2Mt1zxpc}&PKp~8et)gfdMDhQqGqb5U5g_=(FGb_Wa3bQ&^G0e*_ufn{JbqotKEU2)cV<kf%L!d&SV=cp?42vo('
            '>R8RNB*T&lOFGswEX%O0!m^GP4G(2_sKP@XYZ_K$SW#g`$Et=^8CF$T)v>N&O@=iU)^x0FcqGFk6&~qW+psRfmJI7Etm|0Yupz^S'
            '3L83BH*CtVsluj?^$m|@c&x%>9q+^-)r|9^0{QQfxRIkn?Vh-C3gSjS&O=Y!I011ZkE2m`k5$|-_B${+0dd1<zYc%0;)c-_r2cHg'
            '4O;V6L@u;n-#=?{gK|<xE1@TD><~BFE2bxI99G<jcNsc3&G*EOClEK{Po<u?aT?-Ab4P3yH)wRYeSAC~A5Lm~x403@5*eIH{o2Ki'
            'bbc>!Bb7EXiA}DHxIq>R(d_=>M!W6);znoty~T~aeY%Sq2lMMJZXC{cx41DMU5f?u&L3Ueh>n$;JQky?u{X|a8`4%PZlp+bQk<iM'
            'n(R^W3SIH&+&5Y3e&WV1)S*M5?jvsO!X7yiHl52R@H@qgT@l8QDZ&nMV^<t;B5~;KGz!%!ZfvFEMzaPZmEqW<wH$<QrQ$|<44R>k'
            '3&+05-3P>5skqUMypU}TP6x32mg0U#`FqA+K0y4%Y&(S`i5q*eSa~8AhZZ;X<g#|`Tn->^?8#{TR2X#>H}>SU`P6uke6USzqcgj$'
            'c6QN5Lej><(__~zZfqsuMys>|ISq2TRNIgeZ9{{6juZ|OHzJWkd7APD%;G<ZL=L61yg{-?qHy%&jXza+Bi1&y<b%r_$s;Rj{J38H'
            '%!(;~`*nEt@3NVU_)kwPJP;3Vi+>RRSP=gtekTI)&*ERiw<2tuX?c$AQtJaO#kX6Z!4m)aKwN8lbjva7EjC8EYTLY=KI1ew=W}ns'
            'pof+Q4A;DGOj?fV&KcH>InBF0uCuiLYDN5e@<h&ePN?ZUh0+shdO}T4sObqcrz6zRac57c=?OIl7iyXn(-UfrBGgdsdO}T4sQIo6'
            'HSGriIXV;AJ`l*^@33mu1A(V`8j${f$KGi`?=+y>X~0&t{Xjr(9tbGZX(c%i;B+2P5O0Xf;y*;;?tjt2z#r;e4+g~V8y9X4zMr(d'
            'dK>??oCPe1YvW%_nM^ckSWeWu!{swod>6HM>btYu+QjgLY1>B4Hp@KfLP9-axZ`_tVi0vDp*~B-b)tGb#)?O69`_50d!<~bb{y9Y'
            '(~oB3o>PWb<7Er|$)c|XE1tey?CbkNaL2fhG^y)I+{0ubW?@@MBJD5Y@*1bsH1?cPCbm%nm88>5+<1iOQ4<$rWmfK)PC060(xg&%'
            'e2e^eU&I{UDJm}1puS`__qjb+G$K0WbwA3SM;*nSa%7&GRd(<rIteGfO{wZ|!!|ukhBd<n`XYv{dBLwFkDm1vZ)Td<r>#_IBwAIR'
            'G(J=F=LV8KHTNwHNDakIyQNDFzKrwV=ewrkP4TE_&Xna?p5T=<+s)-wqy8&&IMlMffmXnHdA?hZ8dk-PbhuZyqstYSK(tEo*uK{B'
            'BKJQ}>f9jZ$t+u&rWB~XN_u2f5EcANd&r1?i~q;*pr}Bh*;;1XddK+P2HuUa$1u(e<#&7R7>{poaaNoY`M7o3Wl<1+IP^_^_rK9('
            '`=-A8KlrYpm#BG@<A<<%p>erXNqXtICBe-Ke%sj+%{XFv8lzi#nsKR1dz#yrgw+dC)301>)2}FXG`Z1Xl3a`b2i;+%5kOD?00'
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
        def __init__(self,
                     error: None | uavcan.file.Error_1_0 = None) -> None:
            """
            uavcan.file.Write.Response.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            """
            self._error: uavcan.file.Error_1_0

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

        @property
        def error(self) -> uavcan.file.Error_1_0:
            """
            uavcan.file.Error.1.0 error
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error

        @error.setter
        def error(self, x: uavcan.file.Error_1_0) -> None:
            if isinstance(x, uavcan.file.Error_1_0):
                self._error = x
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
                'Bad serialization of uavcan.file.Write.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Write_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f3_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Write_1_1.Response(
                error=_f3_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Write.Response.1.1'
            assert isinstance(self, Write_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Write.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 409
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@j(-D@0G6i;f?Y}zKK#>QfmjtI5II!Q$g`cl$lBg-T+%VyK+L%H0Ux!H4dc4oM9CuR#ui>NJJFwk36@S}b_h#*)L'
            '@xcdMLGhomp1ZTzY|;(7yX@}W`|&%!bI&=yGuIB@{%35c{ZgmWR+xp6O)@4pjrdjSN6aQc(oB<#OQzNMB8zwvhhe>yGJQ**y{_NU'
            'XVf9W<CqBzLu!0giae0HV7s@BkeD_R;>nzD1T?nSIbvTHh-KGUmL_qAizTwbM8=cYAdOz?jBjaY*ctvnU)Smgp;8L&=aOamir$ZM'
            'cav5lOPodF4v)hmq>>V8$iZka35V6OURq@#5_IM$OrYT*V;GKI!EMJo+fVFgHx=e~_y*dYT8lH@h*?;PC2KIT`!<dcpGy+4xFJD1'
            'lgKKdnIz35L{`tJ>FPF+Ic6{5+KO4in;3du*R*<^WRk`q6=5&Xjoe39MmA`aBZGq^OaiTjG|o<`(gI#Fo{?P=Z~~s~j7~d~@Ekl3'
            '=L&=ao}<Br8H{TO>*;NO*=8zOX2P<|+ft26oTJe;I?SoDbwL9&o8kIWXWVwd1hb|yAB~;=FD~P2uH$-_T~e;qyjq(U%)zT2BXD8m'
            '!Gl5I#$2yXmb^80@nI<Ez#vGainkvpXJjA`=NA^rtE*(O>{iPCXpIkocC>;>m0EeB?$zEvFm<6~Gy9x{CBd30R<0!&4QJjqm1iZf'
            'MXi)duq04vr3sH^X2}F+LoQe#6VcMU$s8ZZwTgRbez~$p@O!On*vysf2C^|_W*I@ScxJ_kv@p+jXsss#nJ`OI(O|OJm9;WtzK6y1'
            'AS@=9D$8Y3_dK#ZUwf_G=Y~%Xbi>|Sop?)RwK~7h5A3OdZph^0>RPqx)#`nNe|iUvsi_|MBYvxpRD=2goPw9(MOcE1;DH0LLmenw'
            'fj40tB&6^zT!jzeJ=g-3qxggjt2m&T4f>{<AnSaSg(OXcBs|ovI!3Z27Xc$C0L0{nR-@)8;=Wd6RqO_vRWo}FrEGWxr3MnC?FUkh'
            '8-pa4B8jl**`{Q|h=Mwq=6=KjB3L7jjNKg-Ms+w;h%e$8gIZ0r1=v1s&)P<Hv^0`8MSx~VMzB~K+1=m)(>F1tW?Yt;yf$F=VQeOO'
            'B&}o}bGRpetR!Wktx>j7Mn6Kcr?*9IM?w);?)|UT(TiLzxBsuQu70XVNRn!0?FW*zntp;lBl8v3Ot3{5>t34%c9)*s834x)1$Wh>'
            'RT_poZalOJele?V9z|5N_O8O*NBWF2xt00YKhpw1JEh!5Kbt%@?F9#P(+oyUi@^xsF{fmX4Q*xEd{EVC-0rn*?za;c+XySVAZBFl'
            'Q@D+W{(|WYKE4T`xbP`_b_PC&FW^hK17E?{@C|&c9(!r_l}=ATkMC~m;JX{`#Qq+BC>Z|;KXo1ZwLAJ5emAt?9+t>`{QQAC|LhWi'
            'BiN89O(TZs|3wG>?y-%Yn{34Pw{mS*O=ATV4>E!P$|3#~4+J|^YGIY0b%ss1Eo!wd`Mc^k_El3!ao_N&u_C&dwAwsD{MHjO3nR7*'
            '>WLbS8?44sCi#B3@>UVaSv=5-RoZG_(mfaMqkrb+y5VhKA<H_8cls=vqxQeUn@8CR3IG5'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Write.1.1()'


    _FIXED_PORT_ID_ = 409
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{`t?U2Gdyb|#0z8CvlVZO4uh=V#)0Z90}|C7W!NpWT(#mRG{{kyKfBwCEP}h`iDrEj46kNLvaTR4K3v8D+b(4Y$?q'
        'LtzvsAaq|0^hGZPgrY_D=(nmsAN1&_!jD2<(sO2p<WM9fQI_OpS8;qr-h0k>zI*POd#QWOGcW)8e?AYn|CQd#&t>dPHkq=yW$0Ps'
        '3w<KXlc{uWCZDs70xy?dy3MWoMw*Y!<$3w*^5w6}UzQW4V=0UOX_4E7RDt?MsC4WG&l)qRlBt(eQif@A%N4m@u!`wI(b@zSO_}-('
        'ntHXU-%smia?(H!pIeBP9QCY}OR>~_ZrMi8Bp~&!|N84P3$ySq%3mSRlwK%U#ze8e?ed=>YKy5=rOKt~O@n7MH69(Qj9$>a8MRW+'
        'TQo`IK1!UvW7@`)$uomyflqO(eo`-`CX7NV%gw2RC^G_2>*%hTTn63sX6fum1&Gv=*KrJJh-UQj@@TpAa>_2~W=6L%L7<1l32~yN'
        '<R&L=j$V;dnOwSD3YD?@HP5hkLmc&AohZeF9v#sUK%5k(nZ!cmGjSIERMRV+YvD1=(&x&hSMKWAi#@koDt*+uIVgCR&v3I66q=9x'
        '4vUEk;vx&t#Kh%=;za2PdLyr=jlx`+eN#H+PcJn|3({0O;pxe#iL6~NU92#zxdurWHoq^Ij{e9fczkc;Tc2qulFH@FC9M^RJvTFv'
        '%Npp|)4*qP=!XIZ+i;#+dLd^8Lpv=D3?Ol<bmn@_OzQ=1HWj7mlBC5=3Qd$hF;vWEb!)CcQc2y{vqfJ1WjVoOjy)lUd^h|NYP~Y5'
        'n^Sz0=Xt?sMd@d$8GRO=iV8n*JH<~cSg!wO471Ea^a90TLoKNklf|r#qAX0JA;-pO<+FL+bRV*z;si$`0@uNSP)tk*1jP)F5;6vx'
        'oOc84is-_(ouwGMghIILb_&h<MeTJL6;+Si?jPwJ?Hd~&b@jzhOK(&b2YFcBCL(nYUu@L%w4SY?qt1~@OHWfTMo8?Y|C*ktYqUp<'
        'mR+9Kc3e83Z#;FYf9S_!13nq?g>OOpIs2vt#Y?9HdroR%&fCTaGA}+94}>j#A^xI>J3)ry94I_8<%gx?80E7(lgj6;LdwXLhe{_?'
        'cCKipd5Rv>l<UQkN<Xs31jfz??!>e1!}~R^aQGTN_9937rIa^NFr70CRxXQE=CcKEkxTGNE>2(o<0d_YD~on(I~)2&@pc8oA%o@8'
        'F#=D%pX^SO%gY7Yeom)^ZX*|q9%tJ-0?H4?mGS=#heAWRCG(6%aLJB7jZidu4*O;_qOEZ=jeA)}GfeHy*v+1#HYT{1GqZCV2Dg#X'
        'Y>vPbxSC;W1st2qSr2fh)9kEn3+?>1^8{-f<`e<DeF^NmtXX^#cYdvqbG58ouApTMbS*;7X$k7f=F)CpXt_!4fiTj7Ol0_^f%~*J'
        'G3V;hbhvdn*)ht|IT%hJF0$sfmf*>$q;@`;L~}TM%_JMXKJLfvdwlFL4#@=xJzEgD;*>yOG&G~nX=y<ZDb3xTS&_~=w1rQ@ee@+o'
        'r<NcPZsM%dJahSz4o$nN^?9z#=L{4wr)ZA4=UH@<u4N7LXVmBU8ck+BDjX?2Fi=sic{SM@u;wj9b$cqnwGkh^DRNo#ivjOxV0By5'
        'i4i@MK{E|o5{?ez>7Dn6%Pdx`-%48UAkEIRH~jOgx)CJt46b~r$asfaxOTV&Fh2HQeb)T3?}JcS{3tLMubw&0XMEf1x=Y)6aG#CW'
        '@7cQlDnt0qc4YKLsOpPEWnX2I|1;wL#5qY0ll{JEwU0%Z>@dZ9FVSnYZj42l;;@*nccfvAsmOwLRQ0h3-@nvUjvZkg4m;|N#mLsN'
        'mU8SRcGO|V>u|9b`%Y}B!;Z1z4vYIX9CmVBX?6lV&Q3L0!V&C0y(4{glAUtc%bu)^<3~yN%#L;0Y4)<i&Nk(Mqd4|TTUhK2JL|B{'
        'il>pwt8MGES6HXRUTet-C2;)Qu5j6_>@|nIUgs|yMZ7n5jmOTh*B$oemV8kPW!`!&8|)4Cro*(VZ;AEW&yC35Vw%IwdpO!w{K@(|'
        'dt#5h&CWaQLd9la9mq@H*)tpL9d^NC7q?v*)X-2GWiRciZT1~@(P4?oJpDDhyyrI9C6;j5yE~pIYM}g;ec{0_vv(cVRa@H&h?xkk'
        '@6~;?%dW64hb7zc18SkpwSDEpuCk=Vx@&Qe@FL;8eYc9gK6E?m{kA=VnyB~P1L4QsWA8icgT{#ILhSBJ)O>hgT-bNn2M+t*u6%~t'
        'sQb}@a%CT~?>VfeKDxRozCJ#19_%C5<FHS5?K?z3{ZC&AZ}u_!#9^Pcj>8YoMi0f}_g@%4_9^?!VLx~-{~`)v{P2a&fqkF-z+t@&'
        'F-xmIQ0eWh?;o%4A8<!TyfIN5ySI6ijXP|%aa{Nk`HIX!P-ecl6q|L}q9;cZ3pk1&cTp#SQaz|SfU@JLFHi$zml|akQTkCU`Q_H~'
        'OQ`X<na=9=I?JfFvRQ9!=X$HC`6Q_Ow0+$*)LyUXZ|q+GDIz>W42Xq&5d8hLZJdoDQs*WlgeEYEhj)jU*b)!T5hQ5g_E3A;Kt&1!'
        '4Bg?KVGryY8)*?d^oF;#Fuq3?kSZC0k#KW6Vqfeaea{r!3kR*u9*8xZ6d8nkm~1WtY{L9LnZ=nkT3&2w843Bu!P#H?OFOoYRDBBY'
        'Xs=l;KNky}giiz>KR=h%J?Dbc^Xb6KZWyf{2qT=hPYRywjMvi_#tU5%qz3Cv*lqm(V}~B|3BohtSQIlZM+iv}k|Cr(D8^zClOQI;'
        'MigQSi$h$3xD0WHbwZ~EoicPPu%R*yGzl~rG=(J~Awfchgu=R^TY_#Gx)s&~JreZD(4(+k=#`*XhF*mYz<>k;G7Kne1V$tnkzqt('
        '<1jA4xD4Y8y9f6qxF^Fsg$WQ62pNRJ@{pGxFGF5ovoI^ctPHaXx^`ZIc^T#v^zDKK3o<My=v+qvM+Qeh?=DKPD8r(H?tLV|BN-kk'
        '=-(v?mSk8`(7}%-cr3$X1wFhh!Lkg?3c7ejf)yE76!h_`1gkQvD(K`V5<HRNiGp5UlVDATHHEFix&-SotSji^rxHAs;i-Z?ekQ>)'
        '8J;P)3L6q^pg$D~gir)RQ3$CN3b6>p(8($VLp%cUD8y9?ht3FeMxj%sfY2hKML|<3BoYxwL?NM4P;^J2I||(@g+)&UdZN&yQegB('
        'pf?J=Duu>C1O}oopi*#*L|`NeBPxZ*cm&3yFs@Q~+>5}yDBM#iIz$9S6og9gk&i$=3VD^{XEp+}QJ7URieWwi^HG>rF^*v&0t-=C'
        'P%)ChiGULYN5xo%#Rx1$VNu0shDQ;26op4B#xpEMU?~bqDn>Lsj=<w6JXSHLVL1ZJQCL<ns$nGpD^XZcF|J`X0;^G2RWY*RNd%rm'
        ';fac|4QmnDh`?GD)>MpbSdYMZ6xLOYZg?7jr%`ySVtm812t13zGZmjir;;;{3j^ZcrsPJ9F0~Jn8wZfwh<koGOm6H$awCqtu6Oq|'
        'xuI=$VX_a&4Xu71es7Z-S}h^<2b0{OIbT5JME&~yK_@rJCy7cV940q5B{%9L<}kU@ZgRuhW$5BGewf^Nj^u`SDjg;_4kEcx+Yy7w'
        '4eIT!?;rR2d;J)1Om28-i4cxd^y-rvmGP~T8<o^X$d`$=NN$kCf;+l>a-&{$`{YJ*`K^;1TkEt=ZtP62d2*vY-Nxj`yt@_)s2$&Z'
        'a>Kn=uJKrOS7U3O**c_+N^+xuL^s7Tx~K{77BA5fkM4c_scx6tXh7|019h9^Mg#W1uCVD|)`#Dm+-R^czDE`|B{v%Eh<&j`cc-qY'
        'U~*%llH91ppqpjbb8CT%(2YuRqjC)zB9jYyKFP)l;*Cmjqh@&_95hZBu-k^>c31gZ+F#m%{l#!Sg<T~#wq&vVTrAp7ZfwbAb<er%'
        'Ai1$6qqPHJ)HJ!VC9kJ1j2ER3s?^q-v)ia==WZmF+E{pT?CO&n8-8*lnA(7t0<l;nw;}nt4F%#c%5YF}!%cF?FEYIWv-rP6Ne;Pr'
        'dV|s$eum>Pz47~+-tcl88<Cx-H~g=xM7^);dEZ&l#b16|o?ZxtLgJro@mCMUUk{02ioZ#SuSHq>TKui}JFzH!Q#um(9^0AV7g&<-'
        '1;2wO{{Er3Qu?gV)QSNaEuG6|dAjl)r-``&x4Sg@(o&aZ=?}CC!_=)g&6v@rc&o4L{A2aizlbIO8#&*)M9ty1P!1C{hl!fQM9pEM'
        '=3o*vblrKFs5wm3>^xCZi<rYi&2ADk<h#Q}&0(VE+nT7UzYvJgoj~<MAcnugMq6G8yvW;t%D;C!ybU<K4QO>6uo14m5KwCu0y0%v'
        '@$UmT-3KJZyW*VqCvkQ9Kj~uNcg2<$1LC)(Qy+AH?3ccJ5B~)20v5!T@h_!N$Q{%S(=Fa%@tGXHbIUt*j8#jUXtvO^SuLN{)7-5>'
        'LN#KzS+MEGz^zI`b(XYCMD>z~<@IK{S1-h?m2!#7aa_{$f;;NfoYL$(PaCLD5*-07Z}?KOqvLbIP3-~Fq^cuc4U;a9Mb<zPmHHwU'
        '&vPnGlbzGj#MUjK;#ZpS3Xc#yD&m5y^vr$TOuJ=FYE+75!5}@};W9^cvWgScsD4?N7kG9qskwAW>w)Vzn<|Q#X;-`=mf6IQ==hv?'
        'l~T^+T2{Bw8O99n>Tnqb{epjeKib9@yyj_QUn!+RJ?^YLr}3G5VXn)sQ}e(;gH%vV&jza0;7iZ{9R*7_?Md#|%$YPy!xlVK@pf%`'
        'Ik)}_T@D52*A)cxrdP0vZow+AkPf$tS$Da-5O8Nn8r8M-Cb|86Qu6{S&nFoynv$UMDwQj%gfQ@LrG||72k&1TcMAg&wbC+G=}rC9'
        'zrv@{)9A&Ko_M3irhe}M7jbb?obgJhofB8Z@7jLIr~eB@st@(_f8)E7nxf)OW}yr#r%Gp28NZgEl@eUf;E&BE(X?Hbr_oxKrx}-8'
        'l&2X&C#;-ui+;s|MZa9v(cpTMLATb}@f5~YK4;q8r?2|fIsz4aUTaqK&(kVb9Nn}O(8-`;zh&jDhVnmw+IE{N`&5g4)m`5<tqoQu'
        'E)BCLHNisLlozXmICf`<4Gn)jl<FTHt(H3rpusoav;%i!Xm~7jbNJ5CjV8pTc93F&!>u^sXUcYF*mwPU|LxnU8~sCr{mp0{YX|M<'
        'AR-Np_Fo?x9{mY|m3}yw<jF2Pl?t?daym%#%r$@aGx5N2%U-$LrhAszn<`(G>&cvHYiff-cl&M)-bi74r=Qq-)bHNByZa`Uf1_=e'
        '>T-F7&L*kK7H*^k-I~JlAy6o76N|I$usD8m@K%3nY<M_zt8etj{Y^Z4t}PD_-x*5{-%Q;e>AT(x?De)hMDck0&dA8{=vdRmzZfW>'
        '=kA=-SMgKL^kr(^rzT0wr__8z%?)aLsR3#RskuwdC^ac+{+Jqr8cvN(O^%vBqh^+xpHuS{Hd}uBI_~Zx&9X4p>Pp^?y5}Vw@p@hH'
        'yXxV){XyAKGc1sYVe#fWD(zR?+vx)7rr*-k-p0n>@tK2bvNgTwUm;#2r2v!Zw@AX@pk4FN!Dc#)3i$bdS|ZT>JLT{*K<h(pKD@;t'
        '_bA+QNlrGLVCC8;gxUcVLs8W)n%hv~Zu%Te9QR<WdiDi=ftda`a_YZQ^B>gwdo_;XH{tCZ{Luf1QJhHrAHC7q+xb@j00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
