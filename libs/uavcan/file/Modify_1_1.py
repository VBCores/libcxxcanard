# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/file/407.Modify.1.1.dsdl
#
# Generated at:  2024-06-20 11:16:15.094468 UTC
# Is deprecated: no
# Fixed port ID: 407
# Full name:     uavcan.file.Modify
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

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Modify_1_1:
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
                     preserve_source:       None | bool = None,
                     overwrite_destination: None | bool = None,
                     source:                None | uavcan.file.Path_2_0 = None,
                     destination:           None | uavcan.file.Path_2_0 = None) -> None:
            """
            uavcan.file.Modify.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param preserve_source:       saturated bool preserve_source
            :param overwrite_destination: saturated bool overwrite_destination
            :param source:                uavcan.file.Path.2.0 source
            :param destination:           uavcan.file.Path.2.0 destination
            """
            self._preserve_source:       bool
            self._overwrite_destination: bool
            self._source:                uavcan.file.Path_2_0
            self._destination:           uavcan.file.Path_2_0

            self.preserve_source = preserve_source if preserve_source is not None else False

            self.overwrite_destination = overwrite_destination if overwrite_destination is not None else False

            if source is None:
                self.source = uavcan.file.Path_2_0()
            elif isinstance(source, uavcan.file.Path_2_0):
                self.source = source
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 '
                                 f'got {type(source).__name__}')

            if destination is None:
                self.destination = uavcan.file.Path_2_0()
            elif isinstance(destination, uavcan.file.Path_2_0):
                self.destination = destination
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 '
                                 f'got {type(destination).__name__}')

        @property
        def preserve_source(self) -> bool:
            """
            saturated bool preserve_source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._preserve_source

        @preserve_source.setter
        def preserve_source(self, x: bool) -> None:
            self._preserve_source = bool(x)  # Cast to bool implements saturation

        @property
        def overwrite_destination(self) -> bool:
            """
            saturated bool overwrite_destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._overwrite_destination

        @overwrite_destination.setter
        def overwrite_destination(self, x: bool) -> None:
            self._overwrite_destination = bool(x)  # Cast to bool implements saturation

        @property
        def source(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._source

        @source.setter
        def source(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._source = x
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        @property
        def destination(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._destination

        @destination.setter
        def destination(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._destination = x
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_unaligned_bit(self.preserve_source)
            _ser_.add_unaligned_bit(self.overwrite_destination)
            _ser_.skip_bits(30)
            _ser_.pad_to_alignment(8)
            self.source._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.destination._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 4128, \
                'Bad serialization of uavcan.file.Modify.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Modify_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "preserve_source"
            _f0_ = _des_.fetch_unaligned_bit()
            # Temporary _f1_ holds the value of "overwrite_destination"
            _f1_ = _des_.fetch_unaligned_bit()
            # Temporary _f2_ holds the value of ""
            _des_.skip_bits(30)
            # Temporary _f3_ holds the value of "source"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f4_ holds the value of "destination"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Request(
                preserve_source=_f0_,
                overwrite_destination=_f1_,
                source=_f3_,
                destination=_f4_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 4128, \
                'Bad deserialization of uavcan.file.Modify.Request.1.1'
            assert isinstance(self, Modify_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'preserve_source=%s' % self.preserve_source,
                'overwrite_destination=%s' % self.overwrite_destination,
                'source=%s' % self.source,
                'destination=%s' % self.destination,
            ])
            return f'uavcan.file.Modify.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 600

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{_ie?Qa}M8NV~BeK{vh8k4lNA{`7wXUSO`gw)bcxM>a1<y_-9Q4lZ7-0s}X$a}ln-PyA*QbjBA(nu?{QWgmTQhDbC'
            'ACQm`6+)ta3V%TV0K}K_duI0T_Ri-bJ|K}O@_Oc(=k@pe=9#>C?#Cal)y$v#`FP}~e&D#NNE8p$L*5O9<9g8`j#8yXkzag81Zsd!'
            '|8NwG;&HL@R`EvB%9mXgh9W6sEx&kICz+?SM9hjj;f8zw70+gT=<(3$Dd_G*zUqyf1Mzw$QeET?cPNrnMImWgxnF)iF52~W{fEU{'
            'MZW5CtrOMFv`C9@L+u$pPo#?ciCrZEf9gon^||J*ChyKV9w!u~8bV_A<tPdS4`-uUb-PNtfe8Cr!aFGSc&gn&<cmUnD!;ZrRzSy`'
            'TiEN+79y$rpg1V<Pr9k*q0bY)s_0SHmCgK8oCvrx6mA-2i3cCfxqjpo`IldbSQu%Rh(R<IOiRJ6gv0Ko!e=^SUKEd*3R5k(&!QfK'
            'pbGm=0mWCX>+%`-T={jqU6;?x&&tnPyH}w!IZjYr*GDx}$hE1&jePrd&seK0GjXC)oo<euQJQr{FG_?&SjOI3eqo>cKFrS+Kt7W{'
            'yEyB^Ncq6Pef+3q8-89-$-x?YkuS`IvQmCE^UGCS?Q>*PUXV|=m)bP~j(iGWnV!p^I|DXJ!be5^^nH$1tlTkm*`d|h`d@TKAO<4T'
            '7Dp)g+PyGU{ZRO~LoNCunUO~b4V&t>vu=JKV2Qb>^r&cmlwT>U@AfE7rM}xU=RVV}6Kd?~b8a_Ci~Pnof+>CwjGq6!$S=ICw2k8~'
            'el0!9KjB7kk+ZXuq@zJM3KT%M)<J=hA1eB5u}HX%l4|37QlYr=8~N2+QRs0k!iAy~G)X2Rq`rmxrM)Z&crrRAx$F*kkcr}*qSbD^'
            'i^_kqOvZO`>gfX>_QipSg;r;|bmR{B2~vv#J&PbU)@AZHP$Bw|J|Ncl=Ssdpjhh7=qU}0~*4|Cg(&8lMp<$rCtSjJ1hH4BuwT3*d'
            '2+D`pCCvcgx!3^DqI4~9ASKl2x&r>W(ppI1==r;^?(ZDz9KLp7&P$bldR!d%0Y)H4W|*mQU^2~vNu#Lzd@tc1tpXv9-SV4gXNw5*'
            'pfG-Z??3s{?Cd;n@4UMA)x)oq&d48?7G&Q3XsSx&YZXFvyCX~Tr1A~<75RPnrhF{l$v~IBKnw&Azj%~C39O$8-;JY0yXg77{Hc=b'
            'Txws}WHDc%AA#xuJNvkQPE1ojMuqEJphOwbZL$<A2zpVdlPEyQ;zWytQi2Z8x&W}7h(0O{yHnanZk8=uKo1$j#YW1VFFM-}rM%F@'
            '(QB^cDSSz&&54i|xcHI0@!((eT5S(hNR&(T-rQlNg{32`4H&u2MCgI=eQ+_mcewka!w$ipQ5cLEz^#0i3MeMvGL;%`1$Q3fI$&wQ'
            'Q_0r1)=6y&_9Vq-t%b!6@NEy*B5^&PN+R3`zCvoDYQ$Q!7DS$<Xz>5BRGuUgzUV2C6YGxby+QX&vf(rj1d;<dS-tRDq^u>JzQfiX'
            '2j&pHxpT(n!S3dFv>k9rDQNLP%P8whD2AZ{A2Cl-lTz#^vW%ty*g`i9kxN1+YmpKWB5F_g8!t5(yUBKJ>f%U2DC|>=+-4SO;w(_%'
            '5v|!=!(?Dx5pd~P;UJ%8)j3<?G+WSWR>q2_JEiu8nhSX#@7Zp6Fhfn3%IoeFC1Lkl7;R#^U9=n7ER|FlWVyWaPu+AcVRLo%UM2}4'
            'e?t48m)GQ`Y{|dK7v*2&`<eXdBl)vE`E&VROa4OsQvOQ*TK-1<R{l=@K41IN_6y_5>kIfhLA?CK+d%h+%e7jEhblI0gV5=Q$43?7'
            'sA4j5*iIY=N~GhWU>X>wP|+`h70PYO0Qn>INjXN83XKxNW~C-L6a*}^%|!yF{#aqH3s-tQNC|%v1|z50Je&Y|TrgxFh#D9rktu@#'
            '8>%r-9u}cL3*qQ^30E*VKqyMHnCQr~NRzzGLSH1oh;UO09cFjTQ8Q}MCTN756UI4o5?Wjg;vgE?ZYzTg!3JqLB4Lda5)7<+AS^~x'
            '7Z!|NV+<L^Ed{E7Xy-f(;Hm1WfE-3!gV+Te2z_%0rcQGgs>BJ0U9mZD1pwzszf{~yqCtfLHqEz(olwJKUuxt{n@JMKwP<pNpph6{'
            ')ONUpb<BD_m89An4vihF2K%<^KBgmWhQcfc5zz|*3v_|8J3zv*O2sBrrw9<fu~ef{qCcACa-2WJG0x2<xC{ivCMiPQj2A`#V+Tsg'
            'cysFQm<Fv!##5S9&6un-9mYLT9cc|mr+`@;ClU7~L0Cq|g3{C^S_@2|Wok--^}%$3;g*SE(+W&ktb1q>q_)Sg=v$IWQA|N+u|H_S'
            'R!lhC#4L{$1d*upXbfm1L-QlJ4h92Nd0v!-8W`*#lC4|FH+b%DEIjmb<vn0&uMB%;YNrk2#<CMjaX%8a3CvJ$F)?W$+kO-P9mEW2'
            '0Xh3dVZDI&Cl3%DM6D<qoAZjr(@zNF=fbDQq&3CI`&6pdgmP_TSD_bVzKJTlY3xuHX4nZwMiXkWXvbwnM8(zzM-XK<<Mj=qnJDw*'
            'T%PB1YJwP`Qm3i_Sm;s3OS@<zZxK|sCgit8WVx|v&^aJ}R^>&m)j&*K&0?QiomV+uL!{oAw#_mZ=l?!yjO_vushJ<}ECL_FD5ed9'
            '!^dEDVMb<?dn)yl4DSLDlg3++l*L}1ai9Nb@-<!it`+m>0rUSSS$*r&>D~0_cHK-GbveYp@t|=^&c1AxAha|U8lRn8uAaR<Im;l#'
            's%PzlGq?OlE8N1|!y2ch=hsW|ZCbv3T6}KZj!$wGkN(T{v40KY&^E@Q_y7A5N&amz4#~gcbx5xYJmNYZT*<G2pzMEvC9cGMfFJWO'
            'c7~_a*X>hkA+oA<tmc!=zIDU$>-ElqrG+n9ne8D5A6zl7(MI((YBEQg|5&g|N1cBINIDmc_Y(jB'
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
            uavcan.file.Modify.Response.1.1
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
                'Bad serialization of uavcan.file.Modify.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Modify_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f5_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f5_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Response(
                error=_f5_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Modify.Response.1.1'
            assert isinstance(self, Modify_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Modify.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@j(-D@0G6yMawY|<vC#KuCEjtI5II%!1=_)^kjBg-T^%Vbmap<M3F+}(3^c4oM9CuR#ui>NJJFwk36@S}b_h#*)L'
            '@xcdMLGiDu=k9Dan|6clF1vg8e*Dhw+;h(F%(cU}OH-xpOPxwPVHQR<$(Z0Y;#a93F`EQQJ54e!nO4&)EaGh(hK)|j^euh%x_(!m'
            'QI8WI$4qD_sp$<V@<8T-?cXv^V%kQClR4cAXlyq*Vy`D5Z+2{tWoZ&;xLPJ#Ok_NX4b;Tt-uRYw#+<Pa^>wX|5GtkMelA(2ujqp~'
            '_cv)ZzRFn??h%<HA(fO!!wx2jNtjZ{26<J4NYI<3FoT9m#xNYag4>Swwx2l2ZYs?6@GZ1Ew;5-=6|=A!OV(my|8*Q8K9?k7aZ7@B'
            'W|37uGfCP>h^(Gf^YvXIbIe}GwRN+EH&OaPds;n7GD+i*if|C<M((34<6AV!k-=dSCV^HZjk9yAyo^_jXJnrQoPg(gqtnhTJP$9x'
            'xdP#k>u9iH0R!8^dS=&Oww(%=nXv5hw(L=fb2QpTheb8n6f`ii8LqGP#$6XoFg>05Xzap&ahcw%IW_n78mV}m>vd_tBD~r&0vFdG'
            'JQxLTvgS6(s=HZRc@)YyGzwC=>K??&86U~RrRC+y#s*ob)T)(Xw5CTvJ6c7gs#jTVxZaxxrY=@(W}maLBv?De(zOJm;leut%h*a{'
            'i&`m_U`e3TN)sN-%#sPthFq{fCZePFlQ}+;Yt`E2rM2n`!SBtAVY67VTgb+gnPn8g;+YjE(!xCBq18+TGGUgaqQzvfE9+#){2><e'
            'qp+A+t*%u_!*$8plJ{C=$PJ$y>4x3S260!(Mtx~{7}(Pz-H^%0jm>)9^%_Hie|is%sks69BYvmQRD=2=oPt;2C0K<^;DQ5hKm#aT'
            'fw!Ou5>j{%uEIy~KJ0+XQG7y%RUA;v27Ob_kS5<|AxRS<2@iEm9V1zii+~Xm0Alh(s|oWHabK&+I<|xDx|zL&QZ}}LQUi$*_d_Yi'
            'jX@GikwjSZY+Ev6L_wWQb3ft%5v-L*#_pa9qdGiZh%e$8gIdjW1=zk|pSO+bXlW#GjsVS&j9{@evb)6trf*_OE!0?M^4fseQ`k)M'
            'NLon~b9f+stR!Wkt5LR5Mn6Kcr*}ndPeKt`KKx&+qnEf`>;B(hef?CAktEg1ItV1|wEYBqM&|3RonVVF*4-`*>@EY%GXRbq3ht^W'
            '>NE^_+<Iga{AyNfc@$C6d3Y5TKh|fQ*`3VC{+SjC+9~Hg`q}2OX)idS+h#CfS`0=2k2z&?thAG1^FdXoaktmja=)9n*hW~<1u-LY'
            'pTcc4^f%0B@X1a1v<9ES=V#yx_!7Q?JMcAp1K+}TYVPIpi@Qzz0>1mfgYR#2Gy4blv7r1D{M`5KxBloC_`~pqdsrj)@$)C{{HxCh'
            'j$lWgHJupd{}&(lXTUbPZqgC^-}<#NHIF4wJjw_HsE7DdJQ3`bsfA^F))_PHwkX!2<nOBE*jP;|#Y5w(CX4W5)@t(z@%uo?EDYH`'
            'sHZ#{x0uILCiy|h@^%r*^LStotGv^_q<b~EkN%mP>&Lfyg)HkW-WjrJj@thMxwn9q3km=L'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Modify.1.1()'


    _FIXED_PORT_ID_ = 407
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{_if>u(%a72h>^IGdN7khE%OdX++DQ)iu2KzS5ZuCs2f&F-4Dot8>vn4P)1_u8{F!#r$nT11LkR7)eZs8fN2fFkjR'
        '4}3sELR1t9ArSure*k{~;!F6QduMlN*Xsl$RU%QY$9K*>_dI{+oXMRd?|$!6LH$V{^?P<`J7pu}fixX?+iW?!Y*=2`_d*%*G&#A('
        'gKcT?^`6huchb4n(yynp$!R0tUyFGd84>M^LUQ^BcVrhw>`}^NhICyXD3Y}(h^;6N#+V&7T(gU-9*)gz%XG_a2^nghE!(|vQ(u!N'
        ')5bOrLg~50>G-Ye`JJ>{tQNnOz6L=JGl~M)iX$GTFN5s?x(%q(<mj^Gjy)8lWY}h8YLyN;?gyl$+$PgJ>v;}0-BE2$8Z8+a4tG0|'
        'fOKGLnXpsWvtg&p$;H(^13Fe-!n+#1f+mGG(q@``)CeQfwaviJGun$=;%su(4>-ix=0@nnfdv_k7`A7n$>(l(%=ID`@UFMbStK~q'
        '6lJy%a+^gSvpm1Yq#H)uw3*jtAe3&WoPzPgT6FP<VA<1S)uQ;gm=$yS-V0zF>;&+xVZ$5JH6!JTCz5L`ZFO62oAF&4M&W#47#Xn^'
        'Z+ih3P)ptSP;zS3v~65J>HzUb^6+G<Z+p^44BWzxytN_c<&Xp{Ko;@zh$^SDr?bgSKCV_xSW`S8&R3_Z1qvK-5y3J%ms~m^Y=Xe-'
        'rOAW0OzdLkrt-@o?T)7gcX*e({nWUeoZoOm*>SnO;zqo~gAsbDFs)7fX530nAXt3Ul2I?M-c8PB-Z$E0ri@>G<lN)cB1MfpeZ*)v'
        'VVXSN*I*bwP$nAxJxxwMD<iGP8h*_rN<LzEewwg@n1sD<%X1`x?tBdnhJDEC4W9>Q<OTV}w}gaq#aEIGOP*_)5qBq&lF~#OaF_BH'
        '^k?g_<CsBjALTJ)+jL@{zLm~ar{9L>znU4t!l?(FrrY67?(;|<B+{1AHFsfJ9N5wk<o0<f`*o#@JfsJZ)&6xnIZlZiJ0?i0MItS{'
        '9U`Uqu5Y>uf$DLKLy+6>#w)eLw0Jc~D87NW#2G<&#8-i*qx7L<8YZDUk8;63=2{&RIC^5Ovbxw@TyHehdEq9H^qm7afCwbW2r^AK'
        'm8DH*kSK0)q8*qP?IJ>^m$PSrodp8WW~$_T{eH5PYKt!#H!Jn$)}POW5lMD~_;&T~kQGnP=K$Gg^)$#6%WsN`*b{Gv?}{`AT-qEu'
        'P<YtsUUCMpzRPXH_kzek&exL%GORNweGO&B<T(9sWDBvgiaNEclKLHZxVQjF6dqNRDPMxn^4uu!9H`89BOZ`Rkl}F)0gMvXfoE~='
        '5cXl4V;U{Mhb~N$)5N^|WcgZ|OrA!B(dP|ehL9zoG!J!wO!veSFaEn&DAWOk1i1w7rA0<uSlGi}myy_vyA}Z71{Sl8_2ti&**fsk'
        'bDbVTa7&wo9E>S&nG6-S0y}q54p``zp<q`Qt`OT0=t+##-YhoffVXXwMZ$VI6?muzwuEWHs>fz&&+#k`(ZK&5AuT~y*t{(PPOR0_'
        'b%W|lFjp=$IgEpF(tIH`57{g)cgpNaxs2<ey{b9=^FVj?JJJquNG6yyok)0bM}RRd>Y6=f2})AZU1=6mH-Nj44co9KMJJmjCftSA'
        '7Psd<Ut;VkThylWJqaSWLpqw;vM`g$9O-V+p0+ivbhIcOBJD^VG>29#AIxxQEpSykea6E#8TW~tQ}Kd$NoT{$BhYj<D|h=K32#lb'
        'HoktHR;S}pD9Izpv8?9rt8~xc<;l^yOcY#vpWc5`ToTvCRq+S$Me#@Rek^{tC*G@zABi8&il2y|il2#}i(iOeieHIeC+9zP?Wum}'
        'bsc{P5ifr8CZhYF#|nj-=}KRv4OFKJkB5AS!;3+$%ocs$kv!}>1>Hd3gpz)tSRvbn3?aXTJjvRKjG<yev6=G;4ml2Ub#f5_vEPx{'
        'YeAHD8&uq$$Aw<GR9YVda^GRFJR+*An0U$!D%jwSuC%ZT{;>-|`&%f%BmhNG82bcADn&{pW$fBKaC#IsIn{CPqB^QtEqVzUA>p_Z'
        '4w-}$=Uw0NdOF)OWnG{_n6*gQGbs{OShoRKjJhstsC(6Auqdh&p#HY*^U$b=vLzi77-<b)=MccPRSgWwrDd?<yC&}C^W(Q5z|EkO'
        'F>VK5H-`Z8>e<2@H^Pk_5y5Ve>LhVI;w6(oX&45DS~r)t9lc&#24SQQyXqdz2Jf}kZFEPGY6@c?Ktz)UHmHEHn}~!R8S;6s4xu1q'
        'V_^hO@lJ1G%f9`fN8dK{z%l?78<+@wQ&K1bv>k9MGfP8h`!J{_Qj$`qs@h~3(P7kyd`qh^Iz*WHe&Cswpb!?`4kt5}2-X~>Xl9xW'
        'U~M3sqp)Rgu}TFdb*x)R5SX@YV$;?j6T+FC&f<Nygu8r-vw8IL*ntv(47d6L4P!*+7DNYv0jey^i`@t@Sc4`DORzU^Zq4Twayd5-'
        'XxPit9_iZY1z}^Bi5a==ah(LJsn;<vNFSYkqyQa652*ukbVgxq$LtIS5FCWBNE>bQ+>QH32qovl(PNOB{N6HUtRsr@Nb4?L%ZY8J'
        'm3vj)LtYp`CmiVwphZVJiWvbFyVBhPDZA=lnIo9-VoQwKdEBN-i7q^~&kG2PsF#ycZ)(kFDO45);I}|vIXADOvrG6avqB!pE+2>*'
        '`!<O>&T`y`Ful53C(D?gAHLNXTSi2Ls(-*(1U$l}=r$-E?h&&SEi!7{eWo8+cp339NW2L~nJm=-_562(r{NygWP%2m|3Aw7tW%`9'
        '>G##5>NJYt75wWr8vE$<WHSY#sUcDS?AUhx?B&5(1|pU}t2>;r?cZwRS@b<@dO!8}enx(cwrBQ}kL~OBNz7pAzo3WxOK68ajdtk$'
        '!?#G{PlI+y{29|BO%)j8Y9E|SE&`zRC$PW}s0a8lKCv^5Qn&OdH8HaCe$3mGjn2AZ_OxAlacbfuD{j|egAdNBX>>Y2jVjC0%YRIG'
        'sfOS)n2S({+>mGDAJ1+p<vyugn)s<sA4~g&p7=55f&9rz5TF@WUt@|BzsBTjH<KSjkLvFLSu6bd{m7>p)d|yT;XZ@!2#eDj^=iHG'
        'Lfxn|n}b0-$E|kv?qS%Ss5jP)<;F(+#stBp4#R1BrE!o<)uV^faB*p=vbJX2sMJ>~lf*iG7;dLlz-gsfSz2#2zf4~WpIIsMGKx<`'
        '?GTj)Y7Q4vWykc3R#d^VYID?77LLti>8LOl4yD>k{np~ml^X`ujS5NgR0V_Vysm)sVWQtq=n<Tn%UlJ_HTh#wTs({vXO>rPR*dyV'
        '!??NFe6BLV!j}$Z;l{?g(O5RtRu`8hG5gq|EJX3Rwz0a}Xs%Cm{^Pk%I|?;7uNMo2&8xJ0hL$I3d4`rR(DFPjH)#11Ej3zRqU9DX'
        '7A*!XU0Nh9JG6wf+@a-FTJ~sp1Is<f)-wu6Ft1+APpo@z^TNo-7$8*aMAToKBQxuudAxtc&tvV3uB5u?%%GypOomj#E3T1F;gw1D'
        '+x!8k_6aQEe_3vxzK?91?}FKWd2(WGK1LK7I;*??S5Y>Pg1UC6xOt2?es~2Awfx}vcBgoc`u1M&KxdrWU%b*`b1<wu)1W<`{Xf^f'
        'uP&R9lIDQlU{LmQUtKo;N+$gaEq|xwZ-Wr7eW!R&^X^e&5x2_!0oVSVF{T>;00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
