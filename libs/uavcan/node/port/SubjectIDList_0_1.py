# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/port/SubjectIDList.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:15.312138 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.node.port.SubjectIDList
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_
import uavcan.node.port
import uavcan.primitive

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class SubjectIDList_0_1:
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
    CAPACITY: int = 8192

    def __init__(self, *,
                 mask:        None | _NDArray_[_np_.bool_] | list[bool] = None,
                 sparse_list: None | _NDArray_[_np_.object_] | list[uavcan.node.port.SubjectID_1_0] = None,
                 total:       None | uavcan.primitive.Empty_1_0 = None) -> None:
        """
        uavcan.node.port.SubjectIDList.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param mask:        saturated bool[8192] mask
        :param sparse_list: uavcan.node.port.SubjectID.1.0[<=255] sparse_list
        :param total:       uavcan.primitive.Empty.1.0 total
        """
        _warnings_.warn('Data type uavcan.node.port.SubjectIDList.0.1 is deprecated', DeprecationWarning)

        self._mask:        None | _NDArray_[_np_.bool_] = None
        self._sparse_list: None | _NDArray_[_np_.object_] = None
        self._total:       None | uavcan.primitive.Empty_1_0 = None
        _init_cnt_: int = 0

        if mask is not None:
            _init_cnt_ += 1
            self.mask = mask  # type: ignore

        if sparse_list is not None:
            _init_cnt_ += 1
            self.sparse_list = sparse_list  # type: ignore

        if total is not None:
            _init_cnt_ += 1
            self.total = total  # type: ignore

        if _init_cnt_ == 0:
            self.mask = _np_.zeros(8192, _np_.bool_)  # Default initialization
        elif _init_cnt_ == 1:
            pass  # A value is already assigned, nothing to do
        else:
            raise ValueError(f'Union cannot hold values of more than one field')

    @property
    def mask(self) -> None | _NDArray_[_np_.bool_]:
        """
        saturated bool[8192] mask
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mask

    @mask.setter
    def mask(self, x: _NDArray_[_np_.bool_] | list[bool]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.bool_ and x.ndim == 1 and x.size == 8192:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._mask = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.bool_).flatten()
            if not x.size == 8192:  # Length cannot be checked before casting and flattening
                raise ValueError(f'mask: invalid array length: not {x.size} == 8192')
            self._mask = x
        assert isinstance(self._mask, _np_.ndarray)
        assert self._mask.dtype == _np_.bool_  # type: ignore
        assert self._mask.ndim == 1
        assert len(self._mask) == 8192
        self._sparse_list = None
        self._total = None

    @property
    def sparse_list(self) -> None | _NDArray_[_np_.object_]:
        """
        uavcan.node.port.SubjectID.1.0[<=255] sparse_list
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._sparse_list

    @sparse_list.setter
    def sparse_list(self, x: _NDArray_[_np_.object_] | list[uavcan.node.port.SubjectID_1_0]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 255:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._sparse_list = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.object_).flatten()
            if not x.size <= 255:  # Length cannot be checked before casting and flattening
                raise ValueError(f'sparse_list: invalid array length: not {x.size} <= 255')
            self._sparse_list = x
        assert isinstance(self._sparse_list, _np_.ndarray)
        assert self._sparse_list.dtype == _np_.object_  # type: ignore
        assert self._sparse_list.ndim == 1
        assert len(self._sparse_list) <= 255
        self._mask = None
        self._total = None

    @property
    def total(self) -> None | uavcan.primitive.Empty_1_0:
        """
        uavcan.primitive.Empty.1.0 total
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._total

    @total.setter
    def total(self, x: uavcan.primitive.Empty_1_0) -> None:
        if isinstance(x, uavcan.primitive.Empty_1_0):
            self._total = x
        else:
            raise ValueError(f'total: expected uavcan.primitive.Empty_1_0 got {type(x).__name__}')
        self._mask = None
        self._sparse_list = None

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if self.mask is not None:  # Union tag 0
            _ser_.add_aligned_u8(0)
            assert len(self.mask) == 8192, 'self.mask: saturated bool[8192]'
            _ser_.add_aligned_array_of_bits(self.mask)
        elif self.sparse_list is not None:  # Union tag 1
            _ser_.add_aligned_u8(1)
            _ser_.pad_to_alignment(8)
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.sparse_list) <= 255, 'self.sparse_list: uavcan.node.port.SubjectID.1.0[<=255]'
            _ser_.add_aligned_u8(len(self.sparse_list))
            for _elem0_ in self.sparse_list:
                _ser_.pad_to_alignment(8)
                _elem0_._serialize_(_ser_)
                assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
        elif self.total is not None:  # Union tag 2
            _ser_.add_aligned_u8(2)
            _ser_.pad_to_alignment(8)
            self.total._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        else:
            raise RuntimeError('Malformed union uavcan.node.port.SubjectIDList.0.1')
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8200, \
            'Bad serialization of uavcan.node.port.SubjectIDList.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> SubjectIDList_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _uni0_ = _des_.fetch_aligned_array_of_bits(8192)
            assert len(_uni0_) == 8192, 'saturated bool[8192]'
            self = SubjectIDList_0_1(mask=_uni0_)
        elif _tag0_ == 1:
            _des_.pad_to_alignment(8)
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 255:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
            _uni1_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
            for _i0_ in range(_len0_):
                _des_.pad_to_alignment(8)
                _e0_ = uavcan.node.port.SubjectID_1_0._deserialize_(_des_)
                assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
                _uni1_[_i0_] = _e0_
            assert len(_uni1_) <= 255, 'uavcan.node.port.SubjectID.1.0[<=255]'
            _des_.pad_to_alignment(8)
            self = SubjectIDList_0_1(sparse_list=_uni1_)
        elif _tag0_ == 2:
            _des_.pad_to_alignment(8)
            _uni2_ = uavcan.primitive.Empty_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = SubjectIDList_0_1(total=_uni2_)
        else:
            raise _des_.FormatError(f'uavcan.node.port.SubjectIDList.0.1: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8200, \
            'Bad deserialization of uavcan.node.port.SubjectIDList.0.1'
        assert isinstance(self, SubjectIDList_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.mask is not None:
            _o_0_ = 'mask=%s' % _np_.array2string(self.mask, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.sparse_list is not None:
            _o_0_ = 'sparse_list=%s' % _np_.array2string(self.sparse_list, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.total is not None:
            _o_0_ = 'total=%s' % self.total
        return f'uavcan.node.port.SubjectIDList.0.1({_o_0_})'

    _EXTENT_BYTES_ = 4097

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8e-CtK0{^9$+iw&{7KhJ(FJl{n!NHIVxUwOMA@&e*Tf%NOYc7_YW{6`<L=+{hn(6XXo1X68?&`slU9x7gSz)Q9j6~(XTWO_8'
        'd5n~oRq{qobsyU^lNs_5B>44oS5;S?%Xdz*GxF`3<B<Q+^Ksity`bWzBJp|Pf5B^ksJQj08AqwFgwfO2Mc_B_(%Wdq!aO$TADRbd'
        'L65n97>dM5&=Yq;KMH#vkGdgm;`Fl_Z`FBN2_sKb;wVv-+gWW()Ya<sn|`W{F1sy}q&VNMH2yJNKQ<0HrT>_RMo+n1sl=~kN~Gp9'
        'Tzbf!_eU8$y5ft#JJ`&m>v6?hWp}8bA2K~jc-!b_R{U+@-4tO%$z^-1_gK@e2t-qaiWVEPmpHK|^IJG#>S`1Pg7=wc%B}gz4f59*'
        'r-VDK^HjM_w33nYdTwoR0Xwa74WCu*BWsqg%{p$=O%)G4o_O60?PfJSfh)zl?yI(`0@EXIEl7=iWpAGcqjAfs|F_XcuKKDt{cZe7'
        '`_+ftC^ni6TO@5aYf<3Wjh?NFW`tHy=)@0Wk#H3y-7!;_J~~FesZXqnSSWw+xI^weyLovT2OhhX1p!am{iATP77sFEzA+0<sgu_5'
        '>?3Z|59!!VzMWr<Tcc(H$0<(9j)hK&<`&yA5A#sFmDTKIIjKjQJiTXdt{34^?ruoI{LmBIED>=cQuKPtl)dTUrN8NmgymbPu#F@W'
        'Y-x$nu!~tLyb4?4L7Ly@wc>7=-#7TOlf_BpY5A-^^)biT!MGU~b@D8x#`JBKWObD#qW9UPer|Y*8F@q=bxID{Op?bjd%E5{uV?R|'
        '2^yjBRzoEkBI#ZEoHH$7mgnV#-P}5(g}J4p!Jc4Nm#;;kjY4%W<+S{K@Z`hQ<-0gl*5p-vW-pA;2WT(rgr1Bkujk>zgS~Ze&ctTI'
        '>-H|ja(RWW@p<*hyv4-2u`U#Pwu=>Rtz9t4ZimZHr7uN>iRW2o);R*r?CPWLrp<TPn$7h+b4wq0(<n>o0v`mzjX9>39=8(sHKQli'
        '5R2Pu_U>a0)Y3%^7a3X59g2M%SdT)LL;-G6Y%7u2Lm+Un8YYLEhz7<XzW0Dec$%@od$^AEABx?I(I@tOSh-Yry<!b!l+FBESMn71'
        'l~@QNby|L1m|gVBWty>sQ<#n2goh20G91Y~vFW3mS*@K1a2ks`#&12hbH&I-d9g6`8}e=PU!Hnv-1Gdf@v8*Ir|*+zY(`CE_94gP'
        'VzhC}=<@5%jJ$z=S032(Eb`7dM0&W$S!aZPkJ9fkt0Ns}-0Go@Q>Nz=R>wQeq}8#GGi7zO;~b&!(^e06oTD`F7_B!$^N(Ad={P4y'
        'XGxzSJxMx8dW!Tk>9eHIkv>oQ0_hpjv!wH+jPym)KajpedXDsE(pN}dC0!srPkMp$HPS`WCDID%Mbg(vFOj}M`X=dHq;HeHL;6S3'
        '%cSp;ULpMx>7Pm8BmE2M`=oy@G?S}zQIPgE=ZQYCS3ovxsV=H%7d*-ck5`?Nt#$IkBb+lNL{B1vY%YfbD~>IOw%}l{*v_FRXv-M1'
        'JxiThxB2q4vNY!2%gc)M1SjY`$U)wy{&>tr`ChQ5auq9zNbS=yKK*&XQ>r&pDW-8M+`u+Mn8AFR*-I8}c9j@ga=2oM2v!r!77#2-'
        'sS@0?<7_tDs>S?G){Kg|y(Ovuz`)Y8v0p;wsD$iOxN@TzV+YY+KBPkPwRYwGTXI|eeL?<1K9FC^f65*CQ2t9#bV2-RzCbU#<fGlZ'
        '1Pt`$Hv`cE)=S?KQP9}<cQ{d?k0?My0U`?Y5e0}SKtur|3J_6%hyp|u=pzacQGkd7L=+&R01*X<C_qF3A_@>ufQSM_6d<Ai5e0}S'
        'Ktur|3J_6%hyp|uAff;f1&Am>L;)fS5K(}L0z?!bq5u&Eh$uir0U`<zQGkd7L=+&R01*X<C_qF3A_@>ufQSM_6d<Ai5e0}SKtzE('
        'qCjUqmqt~ju-IZ2U0E*b8xJsP(!7PsD_z(qGKmMluhPR0ZD!@^;SFeIW{OtkQU0d#wdJ+tYpWZdP(LFBidXqJ>^Hl*5t}Rv@&h?1'
        '|1YasAC>^*Pg{3Twm!mtGTC}GIFIC4^51%{=Q9bj=u%%E-F+7qIRHjl4DUW!Wpcj@=o*3T0rOLaEp<aIvNXbjThnlsH$qFP|Ak=K'
        '-{(-dA7z1ue7PskbU4XUntA>vwhmdKn2MOhkB|VD4=1sc%loFKy6p-Rp7$GR8%fnnu^)*Tb_cfG%bl>u?h9;|qZV$LsrwPbZYkj`'
        'it`rl3hpNLn=vljqSkn+s22Hg7bo$hc1X9EbJvoq1u;|Lmu0)}+<TtZ$6Uo5PpLlteM;RqVAa9B?}}mH|7M+;&cBxXt4lHQ9r?el'
        'G4yLuK5TKpuOI|oUri|=+}wv_-~A#j<P;KorfB@<WEJDjhTiXr%&kvx$bJ-VeU88I8_RaP_#sd&@8~(~u#5jONL-0!3Z>t^>^JN?'
        '%$BUzmOs$dkJZvlU)?C@AB1GX^3JdV&G6~M&fo%F`2~fdSi2|@000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
