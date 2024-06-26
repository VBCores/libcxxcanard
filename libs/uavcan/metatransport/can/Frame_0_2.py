# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/metatransport/can/Frame.0.2.dsdl
#
# Generated at:  2024-06-20 11:16:14.190707 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.Frame
# Version:       0.2
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.metatransport.can

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Frame_0_2:
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
    def __init__(self, *,
                 error:                       None | uavcan.metatransport.can.Error_0_1 = None,
                 data_fd:                     None | uavcan.metatransport.can.DataFD_0_1 = None,
                 data_classic:                None | uavcan.metatransport.can.DataClassic_0_1 = None,
                 remote_transmission_request: None | uavcan.metatransport.can.RTR_0_1 = None) -> None:
        """
        uavcan.metatransport.can.Frame.0.2
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param error:                       uavcan.metatransport.can.Error.0.1 error
        :param data_fd:                     uavcan.metatransport.can.DataFD.0.1 data_fd
        :param data_classic:                uavcan.metatransport.can.DataClassic.0.1 data_classic
        :param remote_transmission_request: uavcan.metatransport.can.RTR.0.1 remote_transmission_request
        """
        self._error:                       None | uavcan.metatransport.can.Error_0_1 = None
        self._data_fd:                     None | uavcan.metatransport.can.DataFD_0_1 = None
        self._data_classic:                None | uavcan.metatransport.can.DataClassic_0_1 = None
        self._remote_transmission_request: None | uavcan.metatransport.can.RTR_0_1 = None
        _init_cnt_: int = 0

        if error is not None:
            _init_cnt_ += 1
            self.error = error  # type: ignore

        if data_fd is not None:
            _init_cnt_ += 1
            self.data_fd = data_fd  # type: ignore

        if data_classic is not None:
            _init_cnt_ += 1
            self.data_classic = data_classic  # type: ignore

        if remote_transmission_request is not None:
            _init_cnt_ += 1
            self.remote_transmission_request = remote_transmission_request  # type: ignore

        if _init_cnt_ == 0:
            self.error = uavcan.metatransport.can.Error_0_1()  # Default initialization
        elif _init_cnt_ == 1:
            pass  # A value is already assigned, nothing to do
        else:
            raise ValueError(f'Union cannot hold values of more than one field')

    @property
    def error(self) -> None | uavcan.metatransport.can.Error_0_1:
        """
        uavcan.metatransport.can.Error.0.1 error
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error

    @error.setter
    def error(self, x: uavcan.metatransport.can.Error_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.Error_0_1):
            self._error = x
        else:
            raise ValueError(f'error: expected uavcan.metatransport.can.Error_0_1 got {type(x).__name__}')
        self._data_fd = None
        self._data_classic = None
        self._remote_transmission_request = None

    @property
    def data_fd(self) -> None | uavcan.metatransport.can.DataFD_0_1:
        """
        uavcan.metatransport.can.DataFD.0.1 data_fd
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data_fd

    @data_fd.setter
    def data_fd(self, x: uavcan.metatransport.can.DataFD_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.DataFD_0_1):
            self._data_fd = x
        else:
            raise ValueError(f'data_fd: expected uavcan.metatransport.can.DataFD_0_1 got {type(x).__name__}')
        self._error = None
        self._data_classic = None
        self._remote_transmission_request = None

    @property
    def data_classic(self) -> None | uavcan.metatransport.can.DataClassic_0_1:
        """
        uavcan.metatransport.can.DataClassic.0.1 data_classic
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data_classic

    @data_classic.setter
    def data_classic(self, x: uavcan.metatransport.can.DataClassic_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.DataClassic_0_1):
            self._data_classic = x
        else:
            raise ValueError(f'data_classic: expected uavcan.metatransport.can.DataClassic_0_1 got {type(x).__name__}')
        self._error = None
        self._data_fd = None
        self._remote_transmission_request = None

    @property
    def remote_transmission_request(self) -> None | uavcan.metatransport.can.RTR_0_1:
        """
        uavcan.metatransport.can.RTR.0.1 remote_transmission_request
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._remote_transmission_request

    @remote_transmission_request.setter
    def remote_transmission_request(self, x: uavcan.metatransport.can.RTR_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.RTR_0_1):
            self._remote_transmission_request = x
        else:
            raise ValueError(f'remote_transmission_request: expected uavcan.metatransport.can.RTR_0_1 got {type(x).__name__}')
        self._error = None
        self._data_fd = None
        self._data_classic = None

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if self.error is not None:  # Union tag 0
            _ser_.add_aligned_u8(0)
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.data_fd is not None:  # Union tag 1
            _ser_.add_aligned_u8(1)
            _ser_.pad_to_alignment(8)
            self.data_fd._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.data_classic is not None:  # Union tag 2
            _ser_.add_aligned_u8(2)
            _ser_.pad_to_alignment(8)
            self.data_classic._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.remote_transmission_request is not None:  # Union tag 3
            _ser_.add_aligned_u8(3)
            _ser_.pad_to_alignment(8)
            self.remote_transmission_request._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        else:
            raise RuntimeError('Malformed union uavcan.metatransport.can.Frame.0.2')
        _ser_.pad_to_alignment(8)
        assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 568, \
            'Bad serialization of uavcan.metatransport.can.Frame.0.2'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Frame_0_2:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _des_.pad_to_alignment(8)
            _uni0_ = uavcan.metatransport.can.Error_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Frame_0_2(error=_uni0_)
        elif _tag0_ == 1:
            _des_.pad_to_alignment(8)
            _uni1_ = uavcan.metatransport.can.DataFD_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Frame_0_2(data_fd=_uni1_)
        elif _tag0_ == 2:
            _des_.pad_to_alignment(8)
            _uni2_ = uavcan.metatransport.can.DataClassic_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Frame_0_2(data_classic=_uni2_)
        elif _tag0_ == 3:
            _des_.pad_to_alignment(8)
            _uni3_ = uavcan.metatransport.can.RTR_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Frame_0_2(remote_transmission_request=_uni3_)
        else:
            raise _des_.FormatError(f'uavcan.metatransport.can.Frame.0.2: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 568, \
            'Bad deserialization of uavcan.metatransport.can.Frame.0.2'
        assert isinstance(self, Frame_0_2)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.error is not None:
            _o_0_ = 'error=%s' % self.error
        if self.data_fd is not None:
            _o_0_ = 'data_fd=%s' % self.data_fd
        if self.data_classic is not None:
            _o_0_ = 'data_classic=%s' % self.data_classic
        if self.remote_transmission_request is not None:
            _o_0_ = 'remote_transmission_request=%s' % self.remote_transmission_request
        return f'uavcan.metatransport.can.Frame.0.2({_o_0_})'

    _EXTENT_BYTES_ = 71

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.UnionType = _restore_constant_(
        'ABzY8eh+kJ0{`t@TWlLwdM2qG<zvh8Ep}{=J#lRL_@>B?9V^*foXcjlJ<HU{RWAWUiDM60ieyR3mA5G1Ezm+i2~<E>K<z`3KD1TQ'
        'J_J}a6@oql#i9`UP%Mg~P*Jqaqkz6F3KY;||9|E`!<pfn;YE~UC$q@<jLz-<csTzz|M||D!$*UE^yud?>wopL<%ij7wlJBl8kJn8'
        'ko#$7u3${2=SvIaQZ-jI8uif+in&tp{fA|v@mb^2&l<ne;Ps(&F|z<=XBIOL<}<~~1*4X!RWikDxm2l5V$RzYt3opUz^GKAeZ!2^'
        'M?R$M&l(~o62IU0S)<O<nOd!qn_H|I)yBurwE~b+t5F|%J7*NKO)&e?*-R~yt|3COa^SsMWpTc?STQ`9&7lyqKde+rm4-QDjsmba'
        '0yFo2+%U)L`|oD5*<A6y*Q9x*eli&5gHkRFpZY^c+}7b^&gE+9f>FF*GaEv$&H<cQqdu6<mgXDg#Nu40e#A8r>A8pY2wP3FM!90l'
        'XKF^a@o9Z5eJ{6UWYdT}4aVN7A4*qCi<Nl;3JONLoB<2<5ljlXIr#eS!uPmz7jr*@!HPczR?QNAH;Hl%D$bXRwMwY~ppB)PQ7LBN'
        '@>F?ou8^BgSB(3M1+?27;cBBkY!73je!w%3jrxF<J7x{$<kaN#NgSa@t?_OHKAf4U0=9}#tl^M7$juv#PtA+<58izJ9er-GsvFo!'
        'uNc_XOS+M(nMOs=6!l!O25sQ3$rK6?_4`KAs30P$e-Cdn9WF9@Hdlo&eJ)d+Hzsjp=L&#zLViun;Ro|I|KE-J{x@>9pICpt2Y<@1'
        'Z6IALH|n~olj_5Txe^Q%e7=;iP=cEPf&O|KA;SIS+@Ztic{2z1kNLy;LAs$@Dw)5ArSB{j3Yp47e<}3vAX8X08h_Z}LSL!Qfn$~J'
        'jv6AlI0qkhAy<SO3okNDcrlV*C}rW>!@flv+r?Hyg3<v@6Dwkn{vM*ghbbMwbZ|u^seBaEp%t-@${D8nR>XcxlPlr?ro$^@jM^Qf'
        'dgIjo5T*xL#9>UwR>ToZ53GoznC@Q@$1r6p;wkF)IHsd3;so{oG^Qgf;w0HQMR-n=Jq^==6>)~_p2al2B6PC<j6H7R9Hq}vdY;k?'
        'lul53ky1|SB}y+-dWF)flwPBBlG5iWouc$Qr8g*jp3<9?-lFscN^es-P3eo2zC`H{D1DjIS15gz($^@xL+K2qvy_^YE>XHn=_;jb'
        'l&({{LFp!?Ta<3wX(}0~ixcvK%Zq7wF(WT#<%KCPmgL2<yjYbNYw}`UUTnyVO?j~;FShAo5uORgQW=N|pEi^?SDjl#+8r`%vcFiL'
        'K<=@5gu7@4>BL1Qmm1J)ToS)|%z2!gRX$GM0=9hnt(NBrcXg9+x|vXR^Lhmcr($u+kHdRwg1W5i?Tt*;=(tDKW4K(&E#zvs2k`hf'
        '@&OF*{i2cmF$~>(qvCzqUJwkvg!xRhhCBoh=6|g}byqgVs*`U*Sqh6F8i@ZMJ|vE&tF=rqo2g{oPs>m3Z_VaE^CCVhP0jh_=d3F*'
        'cMPAY=7e3rFgaxYxA`ws^YW+Wm3Pdm=5ySfGOwFA%;(LU<}LFD^R_u%KiM)U-shJ2GCrdYU%!40s_3~a-XiyMMrE>LzG}X1n|{mu'
        'k;C9Wajt&kV)bKhmWufJE(Sgx>ZA740UnJQ00s7T*EaQ@O_T6RKM-*kh7ScZKZ5_yws3sh$MFNi@p0n#As@#N5XUEo<Kx8fG2(be'
        '9M6d38F4%#j%UR2j5wYV$1~!1=Hqxq9M6d38F4%#j%UR2j5wYV$1~!1MjX$G;~8;0BaUap@r*d05yvy)ct#x0h~pV?JR^>0#PN(c'
        'o)O10;&?_J&xqq0aXcfAXT<T0IGz#5Gvatg9M6d38F4%#j%UR2j5wYV$1~!1MjX$G;~8;0BaUap@r*d05yvy)ct#x0h~pV?JR^>0'
        '#PN(co=J{plH-}=cqTcXNsecd<C)}mCOMu-j%SkNndEpTIi5+5XOiQY<aj1Io~<mJU(&^#$32dLdl*&p4IO+#5AcmB{)ytB?|A%U'
        '`vwL*@T5pCM&1y4L*xz3DZt<ygncrW42q&B)k@J4#Bo_8+j(sMZ%#z4ng4G7r}<wU2DAe$0d1ZqVzK;r_@_-+dnOQNU}$^e#T|sU'
        '|7%zKzfQtd%^kLCKt@^zVQZYoXwVn7#)*uEd|~S-k<kc|(GZc*0FhCg$Y_kn=m3$?eqY$SkH~10$S6r<G(u!FOk^}fWHd-*G(cpO'
        'ATo**8O4Z<G$JF7$VekH(uj;SA|s8+NFy@Rh>SEMBaO&NBQny6j5H!6jmStNGSY~QG$JF7$VekH(uj;SA|s8+NFy@Rh>SEMBaO&N'
        'BQny6j5H!6jmStNGSY~QG$JF7$VekH(uj;SA|s8+NFy@Rh>SEMBaO&NBQny6j5H!6jmSuoWTZ(l(j*yal8iJ-Mw%oeO_Gr&$w-rA'
        'q)9T;BpGRvj5J9`nj|All949KNRwow`NP(MC~S=$)X{@F3R@#@h`d1&wpuH67}hmhK_Sndf`HKcr+j7rg2U5ry%-)GKGilTJdL`z'
        'y|R{R*46Lf8t7!BelT6j+)rD7(V}ZJ#7){E?lR!*DT;JI5|bD)x^>h8)=IQrKeZeFPyQx+^ymp1aYn=$7H8P5z`+%Gh%3Z>t`H+v'
        '7$jF1^0~qwxkAi0(HbOIh?6VqCs)`<u8<^G7$#R3Bv(j~E5yhZj*u%HCRaE_t}srnaFASKj9lRWxx#+m`oKPNg;8>aB)P%}xxz5H'
        '!VtN_Ai2T-xk7?mAx^FkBUj+$3Y=VllPhp?1x~KO$rU)c0w-7C<O-Zzfs-q6as^JVz{wRjxdJCw;N%LNT!E7-aB>AsuE5C^IJp8R'
        'SK#CdoLqsED{yiJPOiYo6*##9Cs*L)3Y=VllPhrP3S7DZm#)C2D{$!wT)G06uE3=$aOnzMx&oK3z@;m2=?YxB0++79r7Ljh3fvt`'
        'M&1y4!}s1BD3}~`g?6})%&&&lPboIyRVtZ>jr#EqGmr~8_NJ-VG1t3C@Icxq7z?=HD=0|(4-vyPe=AhP74S?sGoPzHY=}Gc!*Y*R'
        'Zy{#K;pFjmGsXMHyGGfl<y8B&e#72Qb;l=WVqX@c#LSOUu|x=^#6-L$-n8<>fTL>0;4eurPMH`&xAf4Br%a5X8}D=4LrzjI+WYH?'
        'Q72}N!C#V|0_zEe^fBh?7jh+qDcgtxj;b1S2rjg?IEX}cxWy8bj1wWYZ7&WXIohNNwUSUWPUP89TX94jC6aBy0HsHXcsuS(91~9w'
        'N#jUMqVB4_I4({Qu?J#;8YhVGyY5#!El$!y!Wl0pJt1}KUiuTK#A$laDDgtA)ASJP*@n=>89B4Tu|?F+?6^m9)|ns0gdT<;tv}lr'
        'd*T^!jvlpW)Ac>zC|&5A4e_ivPml0e_$Pz<=dkX@zS<TS#DokPAeX+gOMSN?E;^w|N1qc~$dIM)IK(A!nZh9ZyFCwma`*RpZP)CI'
        'E8;4JTpf=Cw7N>+*{)#{*Tf`+e)fI9?K|Q6u3Ht)i75&)yBZN_IYmL~uHzHe#SIF4y?4x2=zB`uHMjN*i+En#q`<rDF@x4ODOle#'
        'tm2k<fhGpcyK4&XuNU_mhqx`KX;RYD*g+4|G@03R+~P&?5>23j@57s5V;b+pSH3lT;s@eon$-0?zR=6dG$H)fK7)8gyh@W%&pnIZ'
        '{*27M<ISJ-=FeCqckME>S@wy)RLs(})?02;jk2t>?5^`DxRzL=DRIoIu?(dU?m`<5wWguv4Ah;4_9nDgqG_|Y?kd#&TvdNvU4IQ)'
        'd=b=UqkWroX!W(f-Dc<QHlXD%-EFtJZ@UStzme^?dvCu5J^Tv#Ac+AwNyXw__p|Np>4dK*=o&jqjmLZIkB9aL=CI3@9`CN#=`MN&'
        '2-tCID&AS&Gd=eWu(12oop`u~**;kSsAwd0Hy&)q+!Z?j-!_%{B<{Ahv?tc!L!rS`IgU1$T{csXcF8P!vR2EhftCRf8BeY3uKl%+'
        '?E_STkovseDAsp`0zL!*Nqw<%EE|2t0w0gyq`vM2(dM2Yf)7rhQormB*Vea&3x>oEE%i+Ry6wjg9gG+OO#KQml7#MHOvMt92}~G0'
        'FH&0kO`0F2l24L2okUS`m&NI%vn}KMEKZ{o7mLK{T@k0PvF*D!t+$)-?t(b2d%uV8tT?SV7ZkoX;xvBd^VYW;iPKV?w(o;ToDLSJ'
        'y?0C`PIoI#%e!mJzP}=Ix<_%^ekw)c^j?V5IM#MV;})k;B8~-!)6M)=aoU!ZV@h$_TOKS<OKCdRMx3^5EQ=NNv^L_jw{ClJI=Ftg'
        'I33<bElzjVE?AuIu5GJ0-CKLFIE|uUxBV=6dfFy&+SL<keb8B_;&e-YT-hJ$cGP7%ak{0~=`MP0BTl#UJ=1gF3URu{!fc-`_{8ZJ'
        'JLay~LG8;j<rb&6Nu1twYc3&co5X3$Cdyb~7L6`Td8kijTLr#t5~qEZQJGq9YE!#vf2{-it3C)liPNDd)^~)WYjHXh%SPX^bRbTL'
        'BHG*&M1kUTD6Xw<4HxRF4zzEA(QQ9|=)B_eHi^?sVfs-MWGb2PFaRpkyMfa|DYiX0Th(cK3I`r4>V1{*j|XEh^B?j*9g4;Be=^wi'
        'RmOw%L3=^(FrLJB7~g(NM;r7mV>$D%P|9Tcc)&%zFaUVvp%&5GCDGd@-}|>q@_#cZU&Ea;KT1tS%TLj}5kc=pj5}{PN6SzBU4Fu8'
        'cFZB+X!$8xetKM&pHRf*-tYH&zx>4Ioe(WQDc+5+@0e)$sn_MF=-r5D`RPe}Hv*STr}3_}CRTSGrnHt)o#m%HPJLWpx+|BaOuOt8'
        's}#$U)}qn4XZcB%hb=$J#U~wVaHx}{I^zM$Ps>o+>GG4Ty9%{GSJz)x)nBt(gfBm-+k`JawQr|herk?^y-cHS+u8C{`}V$fBdlHN'
        'LF3!)@{`jOs`*KKqj``0ab<rfAX;6bHm~=v{M13OsI*hZ-7P<L-8U-dC?ej8x3@6cCkq`dKPm0FM9~&I>tb4ICv^GAbq_XQQs}3('
        'faND=7j<WYi8sO*?FO^6<tLwI)Sr{i#^~L(zt)j`6u)f<pT~Ct#rlp=SQ0!5@H@w{(N`?E6o7EPj`xmeb59WUxct-+F6p%vvOeJI'
        'c=^eV&RN@0E$i$$y5Qv}_nQ$kgt+)5F^(tXn-QrK347@&r6&L`2doLix#mJTm2iQz*Pq&h?R*W&ITP%OQ>mj9d?J-PQmG%G6MQ0-'
        '`n!FCPxO*Rq*C{;QcpGSnn<PYP^ES@oJT5kbb`+ltWw*0bFfN{`9Uf*mVFYUQrqR>Dz#nbQKVAuiAvpl`<<)QiW7W#R;d*y_=G8?'
        '9jMfb6MWkD+JQ=~IKijezC%=M#R)z;x6s)MKD(h(lWM%(dV<exsMKz2K_~cxsMG<2*|9z=&4!%d(^jS4HT#{Y)XlBrJ5Z@ZQLOI>'
        'Mb|2ID3*=BV(Cz&4n?%NCx}!h_^5Ghb%m?nI<Q9t-d3I96RuM4F*?NwKJ8R$N23<2yQ5O8Bz3P!z1@6MVg%n}NZ-Rl`s=6O$kp^p'
        're^5X-^$hIP5oXWb6?NQ*K!YxhT`W;&nth<6knitvyiD)bMv7;V)}~?elZ~br-QMW{YU=K@I?;Knf>`c$1FUyKmQkSC6f8SY^l?S'
        'bN%yw*97sEWhdn5esSlq)cvtmxaL1V^QO^`wSJlx1?c;7-qfj{pCEMmpv8Eoc0XXXXV%Q_h)1Khdu`R{ZIrYo5O9jVjntmkxixkh'
        'sXd2uYwL(rB0YxrA-cIl3s`}oPI>h3q=o7*&P+WTIO0XLFsoFYOs`vr39mTo(y527Ph#P9>C(D|nD9Ek1FJqIUI*MB)Duk|+=Kd}'
        '%#V9fD^6#(ar5R#Uv}f>&5^$1#?6}}ebtSdH%I%L8#kB89nI6m%_VY2*R*kSi9F;qaW`^HL%Pw5+{%Bx6}gpvvlY3Of2$R_mH$F3'
        'ax4FKD{?D8<fLke-8oj_B`<a-{|8>|PX5bY>`wkGUhGc(t6uC*{%c<BPX3NgEFSl09Rc}Eiu`3o{;DE>O_9H@$lp-pZz}S)6#3i1'
        '`OZnbEd?i31zc4yttyyN70jv%OjW^>s$f}Fu&OFpQx&YM3N};)o2r5>Rl&BRz&XjWrJ#9mqL_KiLIW8XguS#T1A~zcLIYo5fcd`j'
        '5eK^r4cvjj!I02E1_q<P(7@fRJ2bG7wuT1oGYs8<fqVJg9T>Qm-Q9t~;WnXxCya502HrrX85(#4nPzC<Jr__X%>K|oC(QoPKqt)p'
        '&_K2Ptczy@Ljx4mgF*uo!h=Es|FW+yFhJaw<>zq)28i4Ku~2Vd;QTbbu2@#}1qO(FQht6{V1T&o9~<=s28dg6mYX*)IPQc7-oW4~'
        'Cp7Q|2FIMxz#AAGbwUGgU~t3<4ZMNDVJ9?bBA=2$jq;o@Ur^(O2EL%i2@QNfjT0L9f*L0@@C7waXy6NKoX`NVbL(z#7B_l4FRFPS'
        'l=rMCU;dIJe_4^gs>okc<gY98Hx&7siu^4_{&sM_`~lh4f)lC&t}2*T70jp#W>p2Is$fY~u&gRrRTZqM3f5Hx8>)g$Rl%03U|Ufj'
        'e?YgjAmr4Fza5Un@;}Fa{$K?D`Et1J!4*ecx=YaM6{n~yI=&)0z9KrlVlR)c_<GoNe1#}K*875!c+Uo$T;Wj=Lni@Ei>m#<(wb|B'
        'aOfl;4!I+?T?keVg-inMiOQ(e`cS|gUJBaDyKNjc3flAAvPakcEcVV1Yqy7I53Y^W+F{~M0ubvyz=>0U<DvU%<IwY{h4cvY{IoL('
        '7_=;o(ax3T9$CbTXzkr6)}GyfeXoeuo?PLi<%}~4NLZg0`^8?H`&Kb@AF-w_i1=jNNkAMX0mIhR1yP^EekSaG&XWbiZK1X}>>0}f'
        'etU@9LLE2>z;EuN7x!g38WUdJSLAf-f*1EyInw6?P5^k;nsi-hA}6jqXN}C|CUWA=I3Q1mOHJg;y^0b!?(8`T*v}HnO5~GJhLeCZ'
        '#JUpsHNcLO0L{?{CGxA*BtY)(8?Z(kk>eELc|`t#-Oo8|#4lS@fE$SXwmsqrKtBrDrvUkNM6P^W`yybsao+~y(}>+-_zAEmapUf&'
        'GsO580K3F}3-UF30w8jU`=)C@7>+sv>^Aag#Qv(p-b6l)*k6;Qe#x2wAo6L%-s4-lxEE^5+70F13-yV!56b(dF7AD@cQtw6&h_Q5'
        'D)QG9`Rj`O4MqN@B7aMfza5-U&%=O%6RHBPDwtLk%%}=xRRyN1U`bW5tSVSl6|AWW)>Q=?s)9{b!Ir9ETTwvqKtO@#wV@{_I`FO@'
        'M$y4{H9A0^?oV`pPl%xC04;p`(ZK-WzT%4xn$K8&bdUh-i2KqL79B|Bm#lrrhdj}Nf0z7|9v!H6OV3bl6dgp-!DAgAkVLrO+O9P('
        'w^d!NpAFozRV>xo?Ato6+_&}a`|q~w*Xn4yRt6=@{68jRvHUOKpK7>HxgYEV>65QWeX?RKl;C4o;1+U_RVqT>Z!Q|un$Gb9W{rEf'
        'qLJ0_l`6V@B=4oR3Z~R0laVeN>5`Ey$(zh_%J#Rk+uzdUZygeiy=Gyqn}_m$H4JX{RsJg^gTKb*i>Xog=kJqkmoLWN#uW)5h8uoj'
        '_*fDH`nu!tw1QDF$`zw(6l)eIP3rHPxvCET)l6WJQu$iJcwiLlC6C&}vZ3dSdahR0i_o@O&deK=jr{$AuJ(+!TNDY|NBY|Xw2#!T'
        'Ig|fgJe2%1T;TcVq|}IY=kN&g%Xj4N5g@G8bTiXUWbS<YN+<sxxAm36i?aX#'
    )
    assert isinstance(_MODEL_, _pydsdl_.UnionType)
