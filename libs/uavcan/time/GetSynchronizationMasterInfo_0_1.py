# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/time/510.GetSynchronizationMasterInfo.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:15.434742 UTC
# Is deprecated: no
# Fixed port ID: 510
# Full name:     uavcan.time.GetSynchronizationMasterInfo
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class GetSynchronizationMasterInfo_0_1:
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
        def __init__(self) -> None:
            """
            uavcan.time.GetSynchronizationMasterInfo.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> GetSynchronizationMasterInfo_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = GetSynchronizationMasterInfo_0_1.Request(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{?wf-)|f>5WbX<q?Z<`N>fCE8jwmNMcWjqPe@2@s8DoG8YO^usVwjA<i^x%FShrRLyFWsfKtg4m15rc@Ax+u?_S_8'
            'Z5kyx`^NLleBb<dKL6K03%&Ly+^)x^D^<oFSSghJP2>tPUYM#jPI`#p>UW@IMaS}oaSib_uDyuIaWyP(sWsS$y>NBk+otf1h1n<X'
            'axE%?*l5J45IXa+g6w<n`(s_8HJYM%Y4o;m9_*GrFxejb+JN&hEb$RoN5+J|_|xQk8V9|>+#m5p49i@2Z)M(iaPesj*Qf40A9s<D'
            ')4LLC3xyy8@nv|AAIKvpd2OucvWz?78h56#1&~1juZ71L7So54c?_3#Nrt1{^zA7zn!6jrJeox6QZ4CWVYIhKQNnOUB($L8t-8sT'
            'EVzYXqf%U63NN@PZCnfsofw3Z<cMMI{=JR2i?Wg3%Tke|k9&zI3P*Wb&^}ddBnyZqVV;+!h(CXHsn>f%(v6umB`}Y|Gf{ZQ1pTrU'
            'k-6DGtZE~zGh>-_tPpi-0cH-8pVY(T>6!x9`wmT`O1jiZJ;J8vlLWH<7R506FF-ycNI>4O+M1E1EF`h8RToX<rt$0$Wr1huQ2441'
            '-PlA*jalQMBrgg9OoKl(_F2~NKhXvJPvSo>G!FDSlb&+d+IW@&eJS*iFerCrIu0a+0;0-{hE5za6Ch#PMr)!>Y&0`uvy3dITW{Y@'
            '$9+8#F;Z|I&(vUrZxJ78Caap-qLYE-ZS_k+r5ed}2TT0u&qCSgQfU9Sf^}JqnNW&3r2l<VtxdpD>(68>)S(!=j9QN8idyi_+0f_G'
            'a|L?nkvhqrzsGRpq4ba2`#xPKa~<B{rjCJK1meb3Zipzg>NZqnlJ%2T3S*}iNI{yF5jVp7yP_;frq>?f{bb!~loED)-bx4~p&E#P'
            '#??XZmCI>s)E!V9EHydNt)!-vkq+W09Ts_IN*c=K-RE#r3*9c3ohEmAlVcy3@d|!`*PceaejM?}OI+E(oA~i6-oj7tQ~V5XBg4<}'
            '3;Z%oBi=c|uW*%c)A(y2x1Z026<Rsn%CsCol=P8iKVGzKYnvX^*pOmBQa(cs<(Bp^1UtJ=m#4Ij14axAYK24zB0df)yJtYjE!!m9'
            'b~4e{oclekjt{x>f*Q+~(?BQ0dkxpy7<d=Io>KnCrqOA0>Nl1!T<$7JLrWWY6~E~qzD?y|RE`;_n|o<a_MiqYFY1S9U70q>VH#`c'
            'Ra=_}JNS^~#m!@??xf`Sh$;teV*L9J#^jp)3lUZFPx1x;00'
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
                     error_variance: None | int | float | _np_.float32 = None,
                     time_system:    None | uavcan.time.TimeSystem_0_1 = None,
                     tai_info:       None | uavcan.time.TAIInfo_0_1 = None) -> None:
            """
            uavcan.time.GetSynchronizationMasterInfo.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error_variance: saturated float32 error_variance
            :param time_system:    uavcan.time.TimeSystem.0.1 time_system
            :param tai_info:       uavcan.time.TAIInfo.0.1 tai_info
            """
            self._error_variance: float
            self._time_system:    uavcan.time.TimeSystem_0_1
            self._tai_info:       uavcan.time.TAIInfo_0_1

            self.error_variance = error_variance if error_variance is not None else 0.0  # type: ignore

            if time_system is None:
                self.time_system = uavcan.time.TimeSystem_0_1()
            elif isinstance(time_system, uavcan.time.TimeSystem_0_1):
                self.time_system = time_system
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 '
                                 f'got {type(time_system).__name__}')

            if tai_info is None:
                self.tai_info = uavcan.time.TAIInfo_0_1()
            elif isinstance(tai_info, uavcan.time.TAIInfo_0_1):
                self.tai_info = tai_info
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 '
                                 f'got {type(tai_info).__name__}')

        @property
        def error_variance(self) -> float:
            """
            saturated float32 error_variance
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error_variance

        @error_variance.setter
        def error_variance(self, x: int | float | _np_.float32) -> None:
            """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
            x = float(x)
            in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
            if in_range or not _np_.isfinite(x):
                self._error_variance = x
            else:
                raise ValueError(f'error_variance: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

        @property
        def time_system(self) -> uavcan.time.TimeSystem_0_1:
            """
            uavcan.time.TimeSystem.0.1 time_system
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._time_system

        @time_system.setter
        def time_system(self, x: uavcan.time.TimeSystem_0_1) -> None:
            if isinstance(x, uavcan.time.TimeSystem_0_1):
                self._time_system = x
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 got {type(x).__name__}')

        @property
        def tai_info(self) -> uavcan.time.TAIInfo_0_1:
            """
            uavcan.time.TAIInfo.0.1 tai_info
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._tai_info

        @tai_info.setter
        def tai_info(self, x: uavcan.time.TAIInfo_0_1) -> None:
            if isinstance(x, uavcan.time.TAIInfo_0_1):
                self._tai_info = x
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            if _np_.isfinite(self.error_variance):
                if self.error_variance > 340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
                elif self.error_variance < -340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
                else:
                    _ser_.add_aligned_f32(self.error_variance)
            else:
                _ser_.add_aligned_f32(self.error_variance)
            _ser_.pad_to_alignment(8)
            self.time_system._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.tai_info._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> GetSynchronizationMasterInfo_0_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "error_variance"
            _f0_ = _des_.fetch_aligned_f32()
            # Temporary _f1_ holds the value of "time_system"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.time.TimeSystem_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "tai_info"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.time.TAIInfo_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = GetSynchronizationMasterInfo_0_1.Response(
                error_variance=_f0_,
                time_system=_f1_,
                tai_info=_f2_)
            _des_.pad_to_alignment(8)
            assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error_variance=%s' % self.error_variance,
                'time_system=%s' % self.time_system,
                'tai_info=%s' % self.tai_info,
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 192

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{^vG-EUk+72mXJ<8JyXw;>gR4h2zH-Q29#`LKfua-Fzc9Iq|gp;b|OHGA*u&fvRuZfE9tvsDpo5zxRzP3f)rzylA6'
            '2cCG~i6?jhi9Y~|zkolZoHKKGch<2JieTkr@1B`CbLM>f&TsB}CqMo5*_!<n&t;=n$4L-srUXsIJG7gyAdKW7lUf*77LQ$Ji5S3R'
            'yf?~N`APZW`{fVIh2r5*q$yJ+uN9B&8kI*TS8R65Lt#n>pkgtn2N6vJBL*yZm6_d98gV64*v$x;Zc=TSYNtIJ>@c0lRKuFN@PH`|'
            'qqxDT?^VyAlpD2;6F)8AFN@P5HAabUZkR4_!fwYLWiqQQ9$FVHiKq6}!<ZTx8Z`R2<(b06ivyVP$a*5FnLXm^uq#ZMu(WS@xj{f>'
            '1g8lHGG--zwm7prUXIIxH5l8(Aw0)V%AK-!I@E@yF;%gz=tIymp#4;sJjRWCibm)u4Srd#o<YaYpQ`zv&p-d%I%lWMyS!dJ&XkfW'
            'JfLu#Gy*jz!&pY;8y6m^)xNJ;B-8k<*3J4goJGd78bqXIJlG(zM+|2K0|!%*oDsz`sUR6hcLYO1lYxz1P~XEJZVo)qB#}dyWh99>'
            'P5X@W6l2MV47o^{Rq7VvWR<6>Nc%y39V}tD=pakbke)Z~1x@5IB~c=yeO#g^DFmAgh2eyfS3A4A4ZDWToC)W%TN#UtGf1S7VpOv_'
            '1wEpl(gaQwu?)RRVg|bjsVJmXK-$iRY8L28q&5wA@X1+y-F+p81PrFJNJh>WR0WQ#;}F<6lz9T)W3W@k(wL=&z_vK??Htn1jAop^'
            '&sYYoAsjMfNEIXWfQkfD6HJM~%OkSTrSWupgek7;J?C7v=ZgW^LO;wNMX^2=DT`;0<E)F7%t)7ltKmqg90*tvU{*cj(w?8?r>duV'
            'amKIiJ@{{T1bYuk{wRNZT&?^ms8Db9v&H<46is1qJ2kA&)J$3NuWp>=&+)HqoWLUC-?(iP`XOs#$s0utZJ96T)}SPye9Uy=S-vu('
            ';_KtZPj7B@w)VC<?X_^X-C4U9zOuEohq~CNOr?QLik!!_Kv#98G(r8)5azXeQmn@mb3Ubp#FFXs1v5@{7jXrtyANSvG}A!|c<Ib9'
            'zA^?H$Q#8p;@S+%%<WiIq{;YH{58I?QB}6?!f96Tci0E_R@-p4H~xB}Rzv@)v{Fe{4MZ~{7^ZI#ZcL`HoIlUfU?}!Q#$rJOsru*f'
            '*ZG-+p<5W@LacR{p5XjJR%H%AhJk$2Hp|j{(1rAaOol~DIzWL+Nx&CSD9*==E0>$+nv3wa*KA&~e{T}79Q3cY9f%C+2z}lYw_ufU'
            'nc^uQ>!lnD4h64n?^?rxx=TXs;*)DO86p%lP6Md9O?glR4ad0oko9N+Kpc%@EI&MxGa?qfYGqKLs03RfQHaj73LJY7eZ&~ZPc#dZ'
            'YXSD85oknz=!qUfY@-Dy<375w8d?IOS(b>%`XBNKl3-(+4JW=xHaxw$y?wpCwz}8e>V&)7*VfwW?KMpO%d68Z&S?NK(VJ9(H3V(X'
            ')BO~oHv>!n2MKnUF;7g5Va2@Hmc#DIF#t5`+x!w==dbWRzRlm_Z|2ZC0RaJcp;+SbcJX*<9UP(uLlKvq;;B%}Tty595*B6@8e?$^'
            'zY@`frnn7$yS0tdPoNQ>I1deuOQahQWCA8)J}Q|&J+WIhk>T;nS>A;MhX8$fg8NPh0JPSJ9gu+@bU|6nPr)o`28#h!ZE3J;&xf39'
            'un6OaeBnSqf4vPJ{pFtLJO+u%l=bekWX6M<19)Q_u%HZ1vN?k?*YGqpVp~eg45iu+>TSRmnqr>8Du*<&*G{W>em}*Q-%a3T-yB2E'
            'lw*L|=J4;bc=Q!vuG`<cY=WxAgQ3jIf*hwrj|N={ZUw(=vVp8v-ByNYm&#|15m+0S{Jr9dZC6-#P2xYn(N3NuRE-Xg^4C5p7dB4b'
            '(Osa2nbS~i%;jA;C-f+I#0Po{A5I|$gCL{*b%a`)S_aw4yS8fT#c2#jsH<kxC~o?(i*kj*h4u<zK=`n9hfUbd+J6=aX-{BdaZLA|'
            'pXr{fZKT2XY@O30ulq%Qb_z@(;4u0l*I{lV>;wNgS*u|JR;Thn3{GH%jHMRu5Or?sty$`2i{28T3IG~_wiX%RVM+#dpYILmXx#ds'
            'BS7I#v^wZOy<-@;2mfo-9VJ2_1WF_f;9yr+N(9@=F18n<WH;BwZLEP*N~p7{zKMeieXMb22z3hJKVnoh5O=lc&QQ`S_*0Ya*CVe('
            'a}Qk?f|eu3BuhzSYXI@{8dbphKxGUZGpW*HhI65XG6h2*n_M$EU;()*ZBN16ley6%W=<8HZryg5DuNBd;Q=?WO$sW9B+zScYXDcN'
            'V#rMh?l}moA9v@#27U|ZHD*dVVc}2-wDL;5PT+GD=?s3}JxWn^mAHvh&rLq>p1aq_s{Jlakpi?p?PAkO@?;`e^ye(0q~%L4pk&FH'
            'TtvwQUvdd07k$ZPlw9&9%P6_*OIA>_>`9iJC|U6=TwVl8%eQ$MZEh|4612J1@+D|t%eQ$McW?PNui#!S-{uv&*CkKSirwq7FR^<q'
            '`x5j|YsJ@t-dOT&UO{gx`F>u(voB5k+-f%MswH1y=UkZRX*Czoo~4Vv1W&qj$y>E(_qtrKuUbCTYPOn<Dqr!n!T8F9T)8537Bp-v'
            '0co_gG{zLnKO98FQfy#3XAYUD5Faeg9>s{}99Vwn!18K)ef`?bHM|FansBq-xv?7pox?uxr%6Wd9l`p%3o=yCVf38vPbgpJNMVIN'
            '>;T)w|C*Hw?Gw^NylnnHBypyHkRx3Jz7B76Hac6ccfd9LJF^>jcM`^9RQg-~8~%I#JN`%hhn)9r^L~eOzQ4c|KHw>rJmYV3#dYyy'
            ')#+w=6(0hJdLw-Rn-!i6xEZnB46w5YS5<9^G+y`|Lk5tZzM0S@b17gwBW>;+d-rJo)6#O>p0vAl>@xP>Ux{q8jB{0Ukxg>L0xMSx'
            'f&K@8+#U<mfS9;<1M{FU?!PF++YhuiiLX(##bFHn%QjzLf>Ir);A8;Ty+p3t(dJ~d{<>`r&tKnte%v9(9AJ8j@~Tc>`63OkzBbB$'
            '#?IVS#+hpyn!-0e(v`=MvlNQ}(!8I@E-druFy5dTgI+aztI|N>(>^GPg^r-R)BgYGay8=by0rcg|6oEye>Qpgg-1W@KtK6M$U6C*'
            'jVJlX@b6bJ<`K&|<X^(_xJHq#MkdD>F7R6o9Foy4bad+!xKtg8_^!8UmVr%flR*VU_+rQ13jE?A_|`{eE+-NGs#1K3pW&bKfd7qu'
            'cF$6L@#13h-Y;bj)#!&72=3#t4?H^m%$iK`mX{uRFDM>y*8&I^zQ(<ewtu)y|9RX@KT^bx6oE*QNu>CXnMUaXNEfEk@#I6|KfB4x'
            'AYHzD@~qh906z^B{z*sO&p;49`(i=ifA?GsR~clusVO&W4;N?P*6iNLs}SFMz?Xf0?cq8BTz}cMx+A0H`|vJ*`GNb=4z{ixAmv6J'
            'cct5R7p}h?^8MT$>xerY{xMjM-r1N#dF_t2Zn7T5L2|?(E)D(-?eb|}rWgPK'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.time.GetSynchronizationMasterInfo.0.1()'


    _FIXED_PORT_ID_ = 510
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{^vH&2t<_6<;O(kT)N8%85x4QfUGtN_o9rt!zs&P=z8(W+UqZNlpTZnVQ*YsoS2Np3H~jO~pk*0cEEK2<73#ffO7#'
        'aN)oO4iqOY9H|^RP#kjNz#jnN_qu0hXZ2;9z?QU{>5td%y?*cae%*Ta&`+IbYx<Ku7xdl8^_o`1Luq^RZQJp9)9R{TpduObEPZ5+'
        'hg-7C*ZTp_?q)B&m)*+7(#Ncjzm@PPwqj}*we+z|+><>_afe49v83<wP!Cy)!=xK0;SOPkE#K~8sa9fdb#1>H%N}oD=J8tJ?}||Q'
        '&?=V7U$mo`haG=IHCN5zSvqQM@i0Os$v^sP{(LuEs4a~AAbSt$TXr0W(n(?-W!JLwWaZs*`ex-@G|uHg$h$TS$nK<%TO0BwcdbB$'
        'u_fJXDSg6<R1$VMIy`O#b}X{=DE;xIlcmR2;I5l1)Or^djhxNWLqd^J4+RnfyULG4<w0S76Gr$p9-j#k$CF)nax?L0UCXs&TRSw$'
        '(j&$hkVEds(wEMUw+?nnt2y4J&CKF#l?)Yj1U*CU$F#e&huQ7)kmagw_WIKg)oOEaU7z{N<t!F<%<OI)F&jUOR%FreLae7(YA_Wt'
        '8L_S%P^d7qLGz@)Ni(CQD;o7ksKj&e5|H;G8^d!2n)MFWP|kIZIa{0r#fk-?+LF*h!iunGR<j+I#B5v0t|-*O@;$wD5|U9~pCu7@'
        'F$+s@=JR-4g*Te@`m*2U10%{=LPgwfFd0L4-&ZknI2vt#6EdK?r;H77gvVhjQ$9D&Q9}!mtT6F?m<(%trqCBM^te$&kE^b`dnH)p'
        '@tyKiz(YIM5@&oSdjZ12xB>3f{v$`x9!YxVA?(9%$lb(uZ9hI}!;DsaW_uos1itI=npPk}=nrXYd)szDY9iz;$3qCdP=JFYW6R_I'
        'W-Jg%@y_=wee`7+U(xStc+K-Veb`b#ma_eXME#zlU?@U$k@r-t^|E$_3abFph0okfoKKIh*scpV?HVL5QtwjYd3M;}*$W9<wwLhi'
        '$Jy9I?SsexY6M15wlJDFFt;atKn6Y7H|gQ1)l)8#l4jQ}elxIr4J=EE6FG?^j*AoG3GtLTbuAN5-^#>i?}%rX#OK6wV}gm#i|54`'
        '#23Yv#0%m@F-F-aPTv*{aRzcJ{rxywe0L;01;{aw8CrtdF8*jR-4B$5kOm`d;IXUFXVd3y$B+3Y4~Oyek&3Ug1qKVc2n8|;Nd1lU'
        ')Jh?UrZs2Lw@6(;&5`dDbUbNAv5mkA-KwD5u)8V7^%~-wn5=mIsafR{a{7C2VS3E$Ad(gcJSM(oM9k85Fl@(=sL!lYo~-hK$8x`T'
        'xM8-bg$Y$zqaWzKnO_o@;a>6eTiD%v%f&0$IUePmAMVjfQ-S&+j{@aKJTGfUbIt1F(fsLnI{pAv$_UGfSQ*=IYs;FHrHAJwN3@sb'
        ')(2IAHt*QHr|fuWzs0KyOuQz(xlp6s6K~$eoSwbu%Q(TVrpGoyLTD(0>NB4|WAgh?)T*CPKKVq~%+-wIJAIsop$d^WP!o8XiN@>a'
        'P&3|$I7*rO?e?|$91UQ_fCk}k(b+J#m7|MJK7bWf10bN&H;`uFsaapA7c&MA04TMMQ78)rGTBDRIk0{JoMz$>4$ngqe$xhUk|G<G'
        'VJ`w*w|&<2R98do03->FWh_uBE-$UE8SLgmHqm(GK5CUwNc!CnrGeL})FJ(B4_0+~pwZUlSWPMfE03D2V|2(zNh&W<+%SfhwpL|t'
        'hH9HZVcV5n-zY<(;K(|4LC<YnRZ&VnRJiW~MT*MwR)R>1`$JB@!FfPcSs;tIsaV)sw)Aw#hAZIZJ{xmvchKLbu#4&&#<^zAmzqo$'
        '(_vG<S8NIF88XLc=Y}d^jty7CBwqnmZLdiI^<EyT->W3jscIsv<7-WqA<CAM1%K07Q<=S1hWsIf{2SuUJ33kq8-N#$v_`9aCmjVM'
        '5s1ZuEZI5v{bKTyi_1&P>&r`>S!=DcG&^U#yu7?lviPDx^+v38^D-&P8IDqMv%aHCmb5A48>r95Ybe;R;*tMiTm-Y((-6UVgA>mP'
        'P;SL+`fLFU2nj$C)tVu^A6?bh0@j$DBWA^q7V>=6sP~I|S^4n#Ooy`gPb0M&RgKWkMY5R~8`WjB17Bt$j)Ump*|XelZp#}o;I6cr'
        'D%?CvZ)b-lT4tg}6Df^N<iYE`AP)*+y$F@a@SUXRAhHmom=r356-WXPPCyPA=Z;TLw$8N1@w47)UDQ9{V$dA&XF3KSh@-&Snx7*j'
        'b^WUdFXY-(QmNtc%9>WJSvT>OGbv(0MVDc{gPqG6EChif$7VbNnp6OK8S0>IGD^5|BcIu<mm;AnQNNr8V-&b8BltjIl3EZRN$BHu'
        'A(8wMm2zUH4_|OHtrO*1qargqD5;?i9P#TxG>kk*G(0)8vT~&}JG0(dUb5C!=4Lzdomq<c$(g|tXCmN}+$h7}uteyd_&0n)RS<WS'
        '=UDPx${Zgk!-*k{iJyy~iC>9dir<Rgh(CzmCkJq*^yB~yhEFx(^d0E<!}W?f99ys1Gg77u!lF|XUc$_h@6s+%TTYI5ogO;z{gU>g'
        '_+)#tqOX)sRgQ9q_|6=$PBFhQDlX#}RHS4e*qKL2e=EwNu#sM?8ap`pKyQj*T}*jdOJ^VSys;lPpB%#GnGW%p`vm5CHO`(M<c0+('
        'AflZ_RuXp!iatJ6tI>|-R#ox{7R1|}`#R+)@UO1V>cXz$PM6m_1{+9tot$s;P~q@bVG}*OU%)Ov31zvIYND6q7Lj}ayJ*x+!KGY8'
        '!IgAKcBC%2SXMcNa4b|#f-|FDI09u+2+aJT&&<6+w6AjUw$umKKDTkaM(Rh>86rG`Lu{_ny<qwZ3X5fc5U3}M5+16!JXOxwAvgs@'
        'x?nI~9u7kloitQF6hSl@Jlf(-c1dYiqu9d%J)&c~76t3(HNfRN*kJmYDh>8;;AF-;NvG-!;!HR#BQ~+QXRxu=eK!tl&|m4&S-d1P'
        'n7AEE((+=x&hWWJrIbGJ>?J5Cs@G`fney|_nS(xB>?^iURj3WI<1N#YcxB6Yb<6~{w5u)WsAZzsa-LewRa-7l%lT@{B(+?qwoFmW'
        'WVL0QTBa&3Q!Q$lu4p(lj+S;+=PA;;Jzi}go!jkd3u)M{>O4iOx2rl&(^~DS&eM9W3l%xjdacQ7i(YH0+Cu(mPgmuTHzuk&Pm?z$'
        's(zj(+b0HoZns)`)<m^Mk2zP$X}88npNaF;7P55WLS@#tUTd;mpV1|`-D<ZQdA!msWkINkr{%mtgNDu}@D`m*1*TB^Q70i*$a|Xh'
        'B#6Y2@ImA3UPXD-faPrimX|v7^K+|n#6cm(TI?)cU9-R_s1E$DjOg_}h)3o4h3wgho+SlB`f|fda_r$-R5t$C#7IU}PPBs>oV*85'
        '8LA&_PnW>g*43qjrRCR_;2QDa@B+16+~aTJui|6zckxg0j{|wfiM-P7K{{UdAEIJKmf<+g^d&8@a{~vVNOL(lY#5RTkRF_SBNmtt'
        '(4J8`cJ`&;4N#Lv73C>1#CMJJ|DKiWU@2lX5;7=bLj$Y8*&0B99mrjwO%V{2)^1Q7G>ZC5jZ$9_ZzwvXM;eD|>%Xew<up>Y2*I+0'
        '=AC9&bZ@Kdt-q#=!}C|xo-Zmy!2t$DzLIs(#Rn;P_1S&^-Zw;+i^$alEu{MdWzu6?aG#O@VZP}p2h(=k8~dE2Rt*#TC=Qjs2_deG'
        'x~T5<=KqJ^KLD|;SBd2b5X%!giRCEqFR6K4BlTyxaYD!WU03epl>9<|=Ut6vVC8|PnFA4B8yFg0O%8oQtpXF11b=xd{zQCN{6*Zo'
        'ei+A4@lkT0H>V%o%N2t*#|+~{Pe0wrUH6oQdl}rzO81IC>x;#OF|>{iT8qIun*U`6PoZ^c_u%2?{Hpm@d3^}q-4!2wN>45?){cmk'
        '3g9wxld|vqZq-i*+}-x_r(ofa2VBfz?foxi*^#|3W)Zz(_j~I)xNNPQPDUZ&X#O8dT``7^J$=fKu)M6*-Nwn+J8<sx%k*`HzFxtX'
        '@$}-qM-KG$9lGyNoaTQ3fvG*bZ5;pr'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
