# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/file/407.Modify.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.103454 UTC
# Is deprecated: yes
# Fixed port ID: 407
# Full name:     uavcan.file.Modify
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
import uavcan.file

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Modify_1_0:
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
                     source:                None | uavcan.file.Path_1_0 = None,
                     destination:           None | uavcan.file.Path_1_0 = None) -> None:
            """
            uavcan.file.Modify.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param preserve_source:       saturated bool preserve_source
            :param overwrite_destination: saturated bool overwrite_destination
            :param source:                uavcan.file.Path.1.0 source
            :param destination:           uavcan.file.Path.1.0 destination
            """
            _warnings_.warn('Data type uavcan.file.Modify.Request.1.0 is deprecated', DeprecationWarning)

            self._preserve_source:       bool
            self._overwrite_destination: bool
            self._source:                uavcan.file.Path_1_0
            self._destination:           uavcan.file.Path_1_0

            self.preserve_source = preserve_source if preserve_source is not None else False

            self.overwrite_destination = overwrite_destination if overwrite_destination is not None else False

            if source is None:
                self.source = uavcan.file.Path_1_0()
            elif isinstance(source, uavcan.file.Path_1_0):
                self.source = source
            else:
                raise ValueError(f'source: expected uavcan.file.Path_1_0 '
                                 f'got {type(source).__name__}')

            if destination is None:
                self.destination = uavcan.file.Path_1_0()
            elif isinstance(destination, uavcan.file.Path_1_0):
                self.destination = destination
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_1_0 '
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
        def source(self) -> uavcan.file.Path_1_0:
            """
            uavcan.file.Path.1.0 source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._source

        @source.setter
        def source(self, x: uavcan.file.Path_1_0) -> None:
            if isinstance(x, uavcan.file.Path_1_0):
                self._source = x
            else:
                raise ValueError(f'source: expected uavcan.file.Path_1_0 got {type(x).__name__}')

        @property
        def destination(self) -> uavcan.file.Path_1_0:
            """
            uavcan.file.Path.1.0 destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._destination

        @destination.setter
        def destination(self, x: uavcan.file.Path_1_0) -> None:
            if isinstance(x, uavcan.file.Path_1_0):
                self._destination = x
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_1_0 got {type(x).__name__}')

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
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 1840, \
                'Bad serialization of uavcan.file.Modify.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Modify_1_0.Request:
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
            _f3_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f4_ holds the value of "destination"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_0.Request(
                preserve_source=_f0_,
                overwrite_destination=_f1_,
                source=_f3_,
                destination=_f4_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 1840, \
                'Bad deserialization of uavcan.file.Modify.Request.1.0'
            assert isinstance(self, Modify_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'preserve_source=%s' % self.preserve_source,
                'overwrite_destination=%s' % self.overwrite_destination,
                'source=%s' % self.source,
                'destination=%s' % self.destination,
            ])
            return f'uavcan.file.Modify.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 600

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{_ie{c9Y@8J29vmd|#aShbTT)S0-gIe~nVOCf1~s$xg2xkz#44_x}Oo!gze8MHgI*`3wt451FRsRIiMcnhU1q~9&{'
            'heDw=ltS~T^bhDC(dV7nyW2ZSDgB{PgVAc{o%i#3pLs`*PW*WJ;)45EzLbulJc>I(E;7Yq^^o^s(FsD6q$XEZROPvwB321Lqr0P2'
            'R8OjvcdK`*c6l;TT8pfb3+1^xHY-9~WMWq2sX+4tDqbk~UdVN)ub_L&M5;gP?1;Auk=v?V3id>nE2Bx%sr&W!ld8MeU3jm0w<^yB'
            '+}cd_3M=yJJ5YOs&l9Ptd}>pPIGQ@r3L<WKV9C3qj;9$#srDdo=5=FY!S!r3XM&!xK`ivZN_YpQA<u1)m`GIev*o4RV+C}qa|3%@'
            'w1r3(epu~P<!6H2avkw3YASla=*d=jKFtK&*%Lu-iY$Z=CxXa?Rr!^hhG}D2CK9tJn3aNgi4MD$i-=jnLX(b|(zz8pVy4d^sPv#y'
            'LGeZJx_n-~SbtsaF3OkW=j9i?-HT9~4Kq|Xh)@lsxpkGeTCU&fJ8O+)CiYcs^VP94%Ces5n@mWA<?Jn&XK(W;g8A73$mh!!4$u0Y'
            'Q4uh3A3vJehM$*na&Q5@$X8}UIaPnP%4eFmy3LVIc~(9>29A6dV40pPUpxXfS;j|I`P_YuRjj<}>aszrv-Lk0h*%^-TaP1@eEFWv'
            ')j*5rmbPLbvKe`Vu;f$yxagIq0hW}9%8sgTT3)EDAM`0rwZ2<3=U(nE5^DVE6G1P|tMckNf+>CwjGh0zD$l;ItdHXkeyu$!j|V2L'
            'N_Lcze3bM|tN^;@Efg5}p`yQ)ii}&6H5)&a3dNP*EHB<LI^<U9Lq#cQlFWprzJ>hx?IMnOHaZ}AGT7sBA*v6mc6aGRRQ_9aGQNvb'
            '&+TwM5IZ6jRvqQiZjkVOq!tJI9zklX%jGXo8huC~5ZiimygWsXTf`iq-9-{z_%KIHi~W>q$3WXfPr#7^)!5s5d|VD2g7P7DNi#rr'
            'B6Yy?C|xd>kP_;1+W`MuX+0!x^z@xKZg1>t+<j}uotLWo+_*UK1B^h9%rMi^j>|NUCyk=Y)BTKxv<ieQZPwpJJ8Rv=_W&X1=lB1U'
            'FRiVO2f>?fY=7<U*K23wk7^6D?50yyqFinea?l%jk|&k#$gj#D$Vc*t{Gb3`MglPqJfiAx`82S;FQOndnGMkM+vT%0*9FwRfy-if'
            'ihjhZ2khL&{j=|y`Uxt$xCTm;hHjH%se)i=w9QP6kj1_g8KndrUi1LqAQJ;r7Ivq!kKCN}YymxF5EmOM?_BS!cPQnRC5~PWB+ubX'
            'Mr}@ntiZ+Z%c~DwKEAN94JstcC3<gdFw(;E5!Mn$ZZn}n5Pk$MX7}!HzS?1T!JkIQBL;A*h~)x`3Ajw<j$6T<LtF<ek9jWHm9;CR'
            'HV1o>Vz<`D;tKe-k86>*o=#;3_d%qPTBsVaHm$`b^b`&LA4(NUG7*Ws0y(kX$ln`uzho<&){a1O04J{(UW=TyMQ6}qS2`V-L-g*>'
            '8J`EcyWi1vz#*le&0{M~F_2IULkS<TP*Rgp>@Ko`rUBSOH|!yogih8bB|;<WP(&-QwHUj`Hhk(*qadUQ6eIVUMVdH^mENT_pKF+m'
            'y(<DP4HXXZX;wQ&E1YHvTHVT6@pPxwez@iql@ipUlA<oQXHMouBT9BCO)fO!IS$&4N8+04_i;bkp};cDQ^<Kw#kc{y{z!<lX?{FH'
            '<&^IhC2?r7++M?wAxNXnQLNgmht|aQ_3K|kk<pE-b@6!|n_*5rCMV$`I)*DvN#SFZDaTczXaP4aEMIG8U?0YKhLTbbA-qEG=DrlL'
            'sR@fi!)|PBv(1|f43vnxQ^_59&y&W383sRJPXz~<8@u1e1ep5ms=HLoGH#P-Pu8Q+fq~#PY@V4NUr0j8pV0mn<t4c)+w!mSRrxph'
            'aUp;DSpIBV{#<_4mcNj{l)sX{mcNm|mA{j}FPFc({>pejogoJK$HyRnf1O-d*y38Hj$M#N8ierCWCDOa8+F)5n#M}xW9*_b<5Da7'
            'h0;tAq#CJR&`CXQ)e4;ws%!(gtFD~da}WuT`k}&F53cn4kP^`<44N9QzTd~VM&{9YiBn=+8C*}I8i@+A2>peIqvIvQDIB0?%Zrp)'
            '+cAj)W}zdI#UnyeBXpSEa7W!lN}FI?a!xqsKsaDRk)*L1c~Yu_)gaBho+Pox2??(I``~p(!zmV=U1tm##bplYKlI};-YNOGv4CRS'
            'e}bSMxltkSv^Jqi>~q)^tMgWP4RNQqpP8gVl&kJL#E!PGIFJ^3vu@zVaVuKrb3|h@%rkxlhjsKuU!iN=VeRaAHQ4u6k1#}9H#--p'
            '@x*`yy64%OK*CVvVzov6nJD;1v;bR!(Il7S{2`8UZm8?Q<7|>5)XjO}1T3+VWxO@@c6?iSkDRA8(7V@!vUC{NX>;;-d;=QdX_^@x'
            'N`kO7LqTb35&Oq3&^k5sJrv<Wh#dt_47*lf%40o5gCMnij>X7xagJgNI*a|J1zRcMY!y!)tRRR?<-21*BN>+O!gWVRJPb{tEikx+'
            'NY-v3-?$F$q#{HwH=a#XmYaXv&<0&0btl&1krBQL+}p=vV$wdo{U`uBh*8@Ea`q|5`Y|6&-f1{U%!+7y&KnjFzO<a5hrZAzttmd;'
            'r&_folv^LW(qUXgE-HP^*`X@TuoI4qCe-55jys=-id{)|A<C|$S5}B-OcBbtJkRIU1(Bdq2dV&A*ipkvzvv@x6I9kF<hMp-xw7ie'
            'nGip#dfu@r5ffL7G$L2$RnFHCsduJ*v&_Z$zt0+Dn?OYF#w@%Z!ACHPp^V`0DVRMpBeTgpkorl6H-U#q;~kQe!@WA<KL7LNYr6J5'
            'FBZ}}@BdG-`6OJV=jC6zi*C|blzaF;9yAWf`3K-J2pyXWjnB?4H_u+4oMjMV&9i>OnOpvo7j9$j`NQ#p((~)J_&S!?PaPDWTleFW'
            'JR{G_XZ+tpE@2#6$2j!ye?KD0zfZ;?`42pz>G6fP?$#$4%1a<9|Chonkhl-<WBv~t3@^@a_!sA)$ZFQHnNK$RCjni5y}k9|*r5-8'
            'S!^Q*pImT{_NC^d-DQq8|9QwJ9qs%ZGOv;e9u)up'
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
            uavcan.file.Modify.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            """
            _warnings_.warn('Data type uavcan.file.Modify.Response.1.0 is deprecated', DeprecationWarning)

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
                'Bad serialization of uavcan.file.Modify.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> Modify_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f5_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f5_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_0.Response(
                error=_f5_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Modify.Response.1.0'
            assert isinstance(self, Modify_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Modify.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 48

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8e-CtK0{@j(-D@0G6yMaQ*`!TOiHU_O9T94Zb&`r0@TH{5MwUr-md&Q>L%H0Uxx44;?96cIPRtgR7O}Q)!9Z_O!H@d!Ac9~~'
            '#0MX21;xLrp1ZTzY}yUF3%hgoe*Dhw+;h(F%(bI;3KNCSN1aL9K^lZMNtxg@<X5Q|GMo5uD~VGsnO2jlEaWX52K9Er^lg3ax_(d3'
            't7C*m5fd5;YI0MG%$J#92e*uph_(>obVj#*8rcnw*c)-c8*RJB(j<;jTrHAqCQ=?p25RhbcYIqrBTnIlzOL1ALZuYk%Op$n6@3`z'
            '-X^U^*EkD<eIgSippp`4*uhvn2@~pMKd+JyF?w?XruGcO$t$>Rw!8h*VRjQ?u7_`<-I=W@<;{o%<w&w769=#3IPth7A&Z(4v@?yY'
            'e40wqiUVZzoSLid0hwd=3a)LKCA^8khq|WKQzVr%3aAMBfo^6Vx-z;=!weZ5B|+?KRnRy)qlznd#dt>cNWdw0zB@YWOv4NCBAm|='
            'j<}8n8x}CIU94yK{AD|dV5teq0dI>nDshg6d+4yF#v6kAW;Vt3weGm%f-`ahok%@2cHzIcOm0=2iu*=|lxj7%)}aMU@LJahT-<p0'
            'a2UApid!dZ?p9^>aVY1=Fi6F+dl)BYbSMv(S5``!n`E_ADVGM(nj8l0L>ZCFwbDx6t-Xa{>SEbu_IV3Sg0&JXT}v<;EW9hQjIB7b'
            'sFhF&mINxTB<7J!Eg9o%zy<SVEZX`Ync1OSD_1Trua{Q|{%(~Fo28Q7L^h_(ETae(Ppv4H7UmfbtVS%539}>>O(yeQX*)&ckFb~<'
            'hQ-ucdA&sHu1nUJYp<6E-0<n4ZrI(b6L*blR+m=>fju+S4Vir0+^SaHT76*f&+el!HPa`5#B1l8YEWN-Gw>?B3~O)+TyWq`r~`#7'
            '@HR9+LIUr@Rrm-#fL%}-ici3>ihYXNpl_)u(%?HRAW1AF;eoEGlO&BZ;WJ_aKumsUHD(?m_p}<XVmsKWn%UbZWg`nHH4qzdKaz0V'
            '=*N*1afn6Fb|e!<6x8V?^Fr<u!J1iU?Cz^Ds>88dd=bYO)M~0D!1e`u(Kf21rIEZD0yIT3f<@BE?l$+CzJ)2ZP+_UbYXfFaU^B@='
            'X~hl9;lBK_;)IEgM%hLgy%5cw-4nHa2}NM}=zpzFT;g)Q^M8}|^iw@S;zTR!Fp#v}@?!KEnQyRGj4i@gcRMt&yYw|rA2@a>xTl`1'
            '(jeeb^RZ3vt68mNVMs;$(N$RbSkF7tyQzo$GszLOQ_MW{v&AFRUT{En%wWv47>ocObBg9zVK>F*gQ`xWPOq(GUMF#}jj+56Vn${j'
            'g*#~IZ<tHrlbi5q1wMn%=iv+Z625}F@HKn`-@<ol=9R^zy{3L3c<}wrPG<iAKjxHwf}eYy{ni`(0)H6Za35>r0e=6)oqzQh!Ex-!'
            ')20){-2dVO|Mb~L*G)QN|J%4WqUNv!@>dx_0QC?b`5VE0nOaz;=bRDKZu4RtNdBIh#l~t%DH<4GHJ*nTvsRl|h~N7{W?{$<Ks{Zf'
            'QIpkJ!X!T|S>DM*xrhh)v5LE$OS)fy2k4)<xn6ubSIE-t;@ts@=BWKICn2@-3km=L'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Modify.1.0()'


    _FIXED_PORT_ID_ = 407
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8e-CtK0{_if>u(%a75C=pZ1WCDtENpaDO5JK*GUDGM^WYa(OR2bo3)*mN@ch^bJzFUvopgyY;RgbirOlXMxv-w!55%NJj&w('
        'ACQm`6$K##;-BCT;D0E;bMNf#?0TJGq)JrE-SM4s&-?t&xzpQ6-u=rXWBR}Jv7qBbj$5%J5i0JgTfFItie>xlz>iccvh;yf5pFA6'
        'taSpBy^~G8o_#BuNKaXz_+}!a*otXij-{vOg{#^);tWzAvy|tFP?N02VPeNgIK=Fz<?%K|J)H1un|qa(f(|v`QLRp;VZ>zVxV0_9'
        'NckRdI({>MekZGzs$*|uuR~Fb$8o5dNi3r56|mjMwjNcM9$i$zb^3~wEr-Y4n6%&VAS5f*Ho4|G-**M~2CaF(YO2_Bg|`t)Xa}Y?'
        'ho9QM13z6!FRgSL(6P!K-qq+8EE#(<Yh>vstSIK5!$YUY=x)-KXVNo4D4@=^up&PRZRl{sa(p{Wzc}wR&yQIs+Wxj+u@uZuRM>hX'
        '92Wb`_Ja;nUK9)NFu%n>sJx9z2F4E?)#am-<xh`SOY&24LQWdF7r`{#2@ze(K{S-dV;zYn(`!pDEv>N4#IB0sXsWA>idj>%{7^`k'
        'rR6=8o?PLM1M!0akdLMhkM{buuN>sSP5czS4Lz?!q~I8Ik<Sd6ax#B9lb$W+)e46<<vDqwn>g|klBItxy}VD_gdy)_>4P^pcCm9q'
        '$7Pmwhf71aqAk2`X<SJ!tb38#@PxDE#bQH*1N1Oq+_?Hq(o9bvSpsgWxRX_b^n4zDt3__g`PB!`Jy9)D)|k^rtfm`f=@VTG`uPK6'
        ';^Duu^yG6YHg>Gy&s?MQu;m9?%JyRtb=pneRY<xEH3S&`p`b4ZBIL0j77O2&3c;0MPcP2-p3P(7jU*+bi82%()h+1H)Dzd`VP_BJ'
        'F>9N<iO9a2O;pF<M&!SdJHy7Q2OHem5DgKCSna3MmeuCFa4imOnGEu}ytMz?%0nH}1ITK(52weea1)n<v|1w4v9}|XwAc-}rxB>0'
        'GzAp7g=oB5yK`8+Rv?t$##`cyBs>!6#4}m?P&y8mP@Ttx<R1#HNeLW1vAVD_+n8NjZs_yUOCRk92YLVzNRa_#8gFP%bGKJ0UV5Sx'
        'a+`LMA>)hrGr`VGwe%KJNbC8={d6hUW?!;yEYzQ0dm&dwrnv<9y=u^BCDIE8K(?A41M<Z3J90tZm2b))$SeU|Is!IOdN|pg^fYpP'
        'S2$MShp~m4uczm7th1<mE$zkhIQ_V)iQHL1pW4+${SG2rngJwApSsDRK!MQqy*Tt;m@IZ<5t2(#;Ykw-j25<m$U<%(_Tigj1}(sc'
        '1ZL?eVqUpkxmF>UXE9;)1xxY>x`b5bk!g_GUHRlopFBJ^RtFRk<PyA>XBlx}Q3rc%Mrt$R*#LY8Sj^Vf7QawoYrs$6b2|*ltsE8!'
        'Fs8(1D$>{r?A$>+V3Ers$*#^^CAJaJlNjs032aURZ(C@Kg!ObP^wAF-1=oUAhfUC)>)QsRf&V*F*^)#!qNM;%tl2SrgZfK2St&OJ'
        'oP%^Se4(|7*o3HTRM^!@1>#`6?m6A_KzIE&$_{x*E|}nMEd69df-wZOd577Oij-{EmL)U|Ko+WD8@{CMWD~?hc(B?Q&g7TMj7_sy'
        '<GR3CAo4cIMs7R{H*w}FZ;SSfuOZSkstBmGqi~S-y;|9yVc%Qes&~4K`)_jYqdAu;lz<M^PV!(I<Yam@B4^vukA%l~goAO&9Wm{<'
        'TIi4Qj=(m}UGRBRx#$3fzavCY6yF`8BJy{coVeqMQ9O+yLl8$VLa=hNCbfF9uU~%(K}I!B<-zB!>+eML(>n<bQ88S3<P_e`GNrM~'
        '7G>m(Hp|4C`H&A`JVZ#ThG1UeZAB&&km*q_?)YqOw$2vk84#!~qDm%TlrJ05cx3>=&*W3V9^}SbjtMX@ue0iSGKjcEpgoq4MtcT='
        'XYulZ!SRJCg#01B|BSpWughuqNBI@`C;34le|$&2SC>DLKb??2lRuZgknhW1%3sM}%ip9IK6~xy?tnS~4Dz>k00RF$Ha1q{o(eR&'
        'z>72p;h~5GNcON(VY5NtDiL*a7m?|PTG1cmW=cVdk=g>B<kMEpP&1*(7E*Ughto3{L<GcsM`5oCRaz}j31<od{XAVwy?65(o=4%e'
        'H4|TlLDwXr(N;D#!9Ve!Xm^Y96bewWMM*%Yt&v10X5u*_bUTzu1=AsRRv*<9DZK>Rl5#>T2fzUmigw`o9Ro_au^vD($|p(eamoZ;'
        '{Vm`+qu~@ATCNrbkD{3)^>3MR826c|TUf|q^gltV?&wh=s+1SOO6+pT6;s1fc%I^#aVzxO1)!YL&o<t8F(hut7=DZOz>VXvD5K6{'
        'jUQs3F*7)%qc&O!RjUtsT8?3Z_a^ENhR9gY&Pm`KV890Td3FPtu%jX|Ri^rEE9geB09hNIo-e!pgB@MpP}Kv+S<gj?o7O@T#Dq#Q'
        '<K@1#-ELtt(wfphuWu77ro(8b#mQge4Pb}|LFjW^QVL6dN06J!g#NBJG<Qwjha5BnS3_`5ur39rOs?A~5V*F*vFR8rju1>iXYsyW'
        'hOB_{YzkK%?7)anMO)p3hBIQm1=TeeaohG2FGdd5V9CrJ{Ec?78VDP;T(~y%QEvEhLocX><dv9{JH9YQpzl5=Cwk>$%8v}7gBZ0<'
        'LJnT#Sj*)by?YuC60*V?<MV>Vy*Dkb=g1pcuQbKIb;?=Cl;yFpU3s>fINB<2TFap*44@N^bb8QYvK>92fQnshZ-JCe2UjNvX8gpK'
        'Lw+9isWzgGNbQLN(jx8@v^1N>@(D_nnI8Df5Lix5>FjJ1KC67*iB((lR80bhR2^nH97DKXi#EkFWar24HO3Z^5s@CVaC-zEK`4eY'
        'N{4&o>`0FcI(LujdmdgyKJ*H2gi}UqwNF3)eebEiCk&aSd*1&aW${W_qU+@!swF*Xl;o@U*BvzW(3uP1ArKwv6LrrHZ5Pj8>78XD'
        'V#Tv&!Wr8BogtpU-1Gk7z0|||Ir%kgUpu~+d}!Z{Px7ohCoh_BB9}1^eGcQ$2L~UK<ez)vko+qy(RBI3UAOk(`ScP1%6usdEs1`B'
        'pWzQ13^&f3=EgZPvx;#n`jZWQ5{UAr?b=I+Mqc>ktvY=0;dy;&A1_|owdd&Nzec>&-wICS`iMT{MIu-KcrLA6`0{jl<QGkIEbBUY'
        '<TtBx#ghwRh++61AFT?$J6pW1A2pv#@=^GW`;i}7u8z3WkKO0{zyOO=>-B1V`Ng`m&}j6&R}{F_KKke&>`v5|*Q~|m_4@n>#SR^W'
        ')A-WzemYf;9>~Jkxw(baRcn5szO*n(ty2f#c5(@vmKqClYs-zV(FfIMmnx!y<`dI6M6H2_!x`P#8St7LSk_~XzPv_5SJ!M%nTrQ9'
        'ZK-~9_Quk@g>`*_w0U{~_x&l;0qOfqcc3s|DrmSYbil%pKcvN_gJ^Mjap}f_wYI!$-I#4Wzc9kXmk;FO<@GgddC^*3nVlQO?2!X`'
        'i1KlDePw02u{JXJPZYj@Y1G`jUK$(QoTlaTv^+)2v$TAfmKSK5r{$}()M$B`mYcNLv{<yXX;HN7&=S#do0ivTxl7BNSb)iQ_r12B'
        ');KbJW4((o&kTIC0zxHjO!GA#xU=?#$NP8uBG#TYozyg)v*>7NM?)&%l`u%B@rslGHh)B>eHu&jU$&cP?xWl0yI{6gpMn~jj}t|X'
        '&RX{Ws><e3P}gpkHjfd<kFUX@m+#--ZkO)S-`*?j8;tXNn^)E!4*I=k9JI&t{~fsJtIOtNWI5nB?6tkZSC`GdlS}_b%Rg!Phe=^L'
        'xAy(gJ>7ek28*Ow`44*{a9Pb9000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
