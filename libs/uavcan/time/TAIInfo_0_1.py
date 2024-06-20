# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/time/TAIInfo.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:15.454335 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.TAIInfo
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
class TAIInfo_0_1:
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
    DIFFERENCE_TAI_MINUS_GPS:         int = 19
    DIFFERENCE_TAI_MINUS_UTC_UNKNOWN: int = 0

    def __init__(self,
                 difference_tai_minus_utc: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.time.TAIInfo.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param difference_tai_minus_utc: saturated uint10 difference_tai_minus_utc
        """
        self._difference_tai_minus_utc: int

        self.difference_tai_minus_utc = difference_tai_minus_utc if difference_tai_minus_utc is not None else 0  # type: ignore

    @property
    def difference_tai_minus_utc(self) -> int:
        """
        saturated uint10 difference_tai_minus_utc
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._difference_tai_minus_utc

    @difference_tai_minus_utc.setter
    def difference_tai_minus_utc(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1023:
            self._difference_tai_minus_utc = x
        else:
            raise ValueError(f'difference_tai_minus_utc: value {x} is not in [0, 1023]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.difference_tai_minus_utc, 1023), 0), 10)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.time.TAIInfo.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> TAIInfo_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "difference_tai_minus_utc"
        _f0_ = _des_.fetch_aligned_unsigned(10)
        self = TAIInfo_0_1(
            difference_tai_minus_utc=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.time.TAIInfo.0.1'
        assert isinstance(self, TAIInfo_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'difference_tai_minus_utc=%s' % self.difference_tai_minus_utc,
        ])
        return f'uavcan.time.TAIInfo.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{@j)ZEqYk5Kc>9(rbZMsVZIsbt^!va@kz&+9Vgmhms~JT$)CCp_QOod3Swh(>;4-dy`yMB>DkFrIkRc`7!(h{t17B'
        '8SlMpN(17)+}?OS^LRY-Jaa#u`TfsJQ~pz2&jyJ}(jYWU3z~{&G)h?z#;TtwBP?^p+q+ihvCTEx8)VGAa<^Z&AKb0tY$$0T)@O2h'
        '5K|dg(PzQly^RgoRj!y0512MWNyn#(^WO}gU%Ady=hV;cg)1(G)LJc~+%n^yfWH%vjNfv_*>%CvWP+d;Ce+f<BCM0PXIk`y6$c1('
        'UmDSqEZLBj^_V_>oQq*3Y?w0Hv)pxR;5??rhJBSV$FCOGwnvU|Td)di4{!-j^po3h#nsSQDif-cs-u^A#LpJ*C8FD9n#q`jmWr@1'
        'WNyOT#;!OMCMtH1|2i`@wZ|EWa}BRqGTA^PW)B&Y1X4>N0NLMLtrO8DPo+AP0omx1T>9raG0YOH$TOx@P^;~6VaNeZb4L1fKw?g1'
        'j}br#86SJ~JH6kb7jno&%82E-%UGrfc+t6(LiXylgk?-7@JN&-!Wu#&kqSG&uquMHNupJh8(Ri8q^nh*up{szX-bUBb<E6(;OwD*'
        '6H_u^RM!bqpb=3zs6a9UfYh%*`kZiUGqW;3&tz~Yo{Eemf(A<W=JD73CZidYM66^I)OH0X6#ZxgX@H6(s!P_Wwj5n1EM_UwumDGe'
        '*N!1n5`aXE__lyD2*`a!q_QM8jHuiik+9MgoNirdqS^2U>x9Dt2EfSOJWWX|AVUyZ12CPi1TS|EF1C8_WdiH?EfPYl-;GU%8xOTW'
        'lq<CwfzN%oQv4>*-{k1q^7v2i)w%KK`P{#KyxXs-Bn$1OCb(T_l$JalTNbMCw9wM5TJE5wRkhqj%blua5iNJCmL;?-RxQhDS*lvv'
        'Xj!gUmK$hkR}d~QfTdZ*yo{Ke3snnZZZ@kHMA)oiUdHInD&{uEYF06~eXPZbpSF*+RJHh6%T){Jr`fLh!ECgunA@0*RyEIUJbP=B'
        '=VqhfceSb(|IVGUpJrnL@wDz%EqKz_VrAEYkF`{*-7{EU%|^3PAJ!{UKicqD3hhM7dh(><dx@oGFO4__>kk)^u{7%gDHvdvm}%sP'
        'zyT$`Q%tWaiG*p#49sWvwc*qIooW67|CnF@rKHdM8|&+9J8N63Ya#dyA8c&x?}lG(?>c^?_+wn&$e&$t1l=?#eqc&D#0#zTI+cP8'
        '-%;4hz*X4ILn30JUceWgZLn`?+2^ATgaY$TI-D4;@-!h32KL$VePBe46AcJWJY#x7nLrC%aW3>t?uw5_;>C_K%?xVgG3lD#@foJ+'
        'C|i8CxX{%!MyrAK_2Dz>(F`i=jx!M??~^y=wpQl0lqT}V+`<ip`&*r@hmW=}$5RlG2gAU;Rcd${ffX|qArGTLITc_e!mse#{8PTd'
        '7juwTkPe_bV5-EuEZzzIO@*1#HWZ25Dz1d3IKV>6!i<7=7U%IR6_G10Yy<5cZKL%Si1n#?P)@FJ{5YKnco8yhwMroqBdu}8hglw_'
        'A`Ug{<tfIUj0=#mbLH3qe(*wFad|kp1dU)Jz{_wJWql^()Bqe*WgIOIK%m@9e&ew`jf#yo3Qmc43Ifs<629YMZ5v-@pj5tQhKiV#'
        'ec&rX`3Ayy1R$3;Ozv6L7ctp`Ep<XuqedESu%4hO8T${-JLWGe{e|ey>+Yms4HwzCC%n3F%~0*W2l?`l&9DLH<}h|0>%Tr4LeL1u'
        '2UuN|rs~jmF~XAn!uQE6@YSgG#tXP_mTdaf#(1^%$SdT{&E1<LnH&v5GVez)g8=<hsK>1QAJwm|4l)jjrCA2$P@a6$v0l|7AE@sh'
        ';vr`en;+V{m#PT1RT6>VBx4}hL2XP0U^7sAvIkBQVPdFa+5-~m`Wb*4j0W(rCP4L}^MMdz4WrGN3+!;HP`)TeIma|tAqO}tMk$o;'
        'XCt<l44QCQ`}%KJT>4VjP5*nBjfu8+D^!^)$VpDjpdTrS3bp@$^%V@#82({~gOSpcf%#k*!&sI${$26zc1dync!^V7-GY&a>cQ))'
        'eD+s&t5f^UMDTARD?PZ*bRNMuVM2DD%lJT#@ZmfT;?Tv2zlJPHrT;^*l}E@z!QVemGgi|K000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)