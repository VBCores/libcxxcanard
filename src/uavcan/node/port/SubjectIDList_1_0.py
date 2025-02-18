# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/port/SubjectIDList.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.305423 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.SubjectIDList
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
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
class SubjectIDList_1_0:
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
        uavcan.node.port.SubjectIDList.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param mask:        saturated bool[8192] mask
        :param sparse_list: uavcan.node.port.SubjectID.1.0[<=255] sparse_list
        :param total:       uavcan.primitive.Empty.1.0 total
        """
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
            raise RuntimeError('Malformed union uavcan.node.port.SubjectIDList.1.0')
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8200, \
            'Bad serialization of uavcan.node.port.SubjectIDList.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> SubjectIDList_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _uni0_ = _des_.fetch_aligned_array_of_bits(8192)
            assert len(_uni0_) == 8192, 'saturated bool[8192]'
            self = SubjectIDList_1_0(mask=_uni0_)
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
            self = SubjectIDList_1_0(sparse_list=_uni1_)
        elif _tag0_ == 2:
            _des_.pad_to_alignment(8)
            _uni2_ = uavcan.primitive.Empty_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = SubjectIDList_1_0(total=_uni2_)
        else:
            raise _des_.FormatError(f'uavcan.node.port.SubjectIDList.1.0: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8200, \
            'Bad deserialization of uavcan.node.port.SubjectIDList.1.0'
        assert isinstance(self, SubjectIDList_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.mask is not None:
            _o_0_ = 'mask=%s' % _np_.array2string(self.mask, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.sparse_list is not None:
            _o_0_ = 'sparse_list=%s' % _np_.array2string(self.sparse_list, separator=',', edgeitems=10, threshold=100, max_line_width=1000000)
        if self.total is not None:
            _o_0_ = 'total=%s' % self.total
        return f'uavcan.node.port.SubjectIDList.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4097

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8e-CtK0{^9$+i%>)6^D;(T~?B1%T_EqNo`HrTx3UD=hCE(dr9Ss0F_xsvE{%)&=9lB(ay+RlI09#ZCbZ-FM$ONkOj>AcLfR*'
        '=wpGr6z!XHhCD0nZg!oA7_fg_a%MPlF5fxy{`l7yPDAm>E+y?i2VvFMB2_$8U+{V;s(vGGC9zgU<aX|+2vrL&gROQV@~8Qw$N8gt'
        '*-rW@ibR@Au+#S<6-WJ#C;W)FaQelJ?>2Z;jp9I5lQ=ciyIFllG|a}$50y5#t@yhl)i~d+H1!ExKh3={55CMF=XTcT#-ysA8KLvv'
        ';nE}ad^jq%6YENZ!O>=B{D2$o8@EII@`&ka%G<epVO{Ns;6o8Lja+lL`j0i|i%_&gWN5Jwdr4AfGPR2%X0OL_DENSRX8pP{eptK)'
        'kBU2NaBch+S}B)Hc5$=2fSXpmfzN905t;@5p5MW3`r7a);Azmi&_PzW)3{Q?8_Klv8ZbNV*F&A#*Sh;W8jV{vgTHfo;<_^B>F?rC'
        '+OIwC$4PG4s6}+URgXi}$n8Q+v|_Y^K_`Bch?JW+?Twj+ROlG_jy-cnB*LiS<Bs_c+~(y~9C+$>7KS`+501jcc6peI{HuJ~8|&yg'
        'o_*YJsfdo<;(Nu_lrw4;a-8Cgxv|jEXl}8W@Tds2+gaUBmNRy|#r1<6=LRtz<^GlwOhtj%W2s0|q0#G_8Fw?lOSP>;%8D&i*;bkf'
        'wz|q_*p*C+pvu;HsEgaYUfzw0`#HYsY<W_7UcPA0eZnzzFm6UgoxF&tF?ZLbS;J(h=zlh2UmBfaxjZ3Hb~8zy#_Z{N^O9Y-hbCx7'
        'BG`zGXo|Fd<yX8p`Kr7mFCP@vnJCRIJqzvx3$}72j$9O)qbcX*=ffu-udUt3sj@Dw+Y8+=LLZ>LoD=#orgEnUA0Bqs#W~a4DQ~#D'
        '7|WG)y2j_VXG`ALmzWXGg~BfMu)?pmO9r{^aQT^3Qe>ETfpcbqBhc~#d(z)_`R+Tj`6|e7+ta>|v$P@bK`8u$V_MlMC!wn6c6t-B'
        'xVP!<KE*&CyMo~&V+XopiNb-6I5KG*;wHtO5ve-_0w=3ua`>reVjSXok7$IanJm4B>p1_RxUJ;&%%KmfZ&lx{I)mlLW&VOMxyF5^'
        '4njzsUDXiz0ea;s%~-`L%*AfXqo&XdN3uX{D|9ofw~GMQiD+Q_HVQjebGag~l!ks=zDxcqQg4$7fr^^nNl<+H0eQw{)Es6Xay%(V'
        '=UxR}e$$(mxA5=!BbT0K-g(DJkC!>?jnnT5`aS7%yyHzdJ=XCm^nBXsRL7ffI@$4NolbPT6EuF#>G6(tlIESF_2y~*X{YlY?+obz'
        '=?kQ1Nf$}ak)9`gk@O|fmq~v_dV%yJ=@Ka;{W0lJNPkND3hAq)uaUk^x=ebB^fKuiq${MWq*c-@q;HbGMfx`BJET7&eV6n-(w~!F'
        'C4Hat8tE@ce@Xf)(qEH)K>C|fGr2(*C28OAp4l_q0<!H&by-b&;88(%yzY&;S|=|*!8s#B^ei&S<#IH%;<#ey3J&Iq>m2%mwt_+1'
        'x74{iE?=HkmL~lNMOpEl;RIU*ImlbJZ%(-=?*^-u8(2|<c26t#^#4PiQoWhgn8sT8p=*RNgZUbBmn`1yDKW0(aKjK0tS*=<AXt>N'
        '5j=3?TsFI^#nd)y#pT@o5>*0VXzAHHEFp_jLJlchz12#vgBUCy(xCZv59Gt!a!>wYS^iNzl7EtamizLt{EMCLf%wT{fqr($CkI6d'
        '80yQfhN1<Wm%b*Vpt14qXrjOXQGkd7L=+ex3J_6%hyp|uAff;f1&AmxKolUN01*X<C_qF3A_@>ufQSM_6d<Ai5e0}SKtur|3J_6%'
        'hyp|uAff;f1&Am>L;)fS5K(}L0z?!bq5u&Eh$uir0U`<zQGkd7L=+&R01*X<C_qF3A_@>ufQSM_6d<Ai5e0}SKtur|3J_6%hyq=r'
        'K<6-*CQNLw*kTr4TPy1u4>4(U(ZUs#E^3yU#KZ7A>7gQ*Sw(sTLt2^nvXyyKys2_yZFB9$#@46Q&&ZJCRsJ6P&7N+=CCjq>tz4A<'
        'm9?FZ#sK91cJ86<e2o8OBlAf9RsPK`_I)M|$)o%4<041E(B<&nlT~L9yMUe%*d8#Y8Mf3-vBGqW2Y067tZ0N*wfaIZ?C%SxJdCq2'
        'K)yT>XgZwaD9r-3jjcl#8fIc9@gpR}<)azw<chv&wc)zLlo$PmZX>B$8vBu$VRzuVy}}7A?4iJBIo`$XGV?HI*e#`;#YxfPUBlgI'
        ')k<*TU22V2%W6>^cVz}&>W1`sxo|DHS`ae@ep$8$&fWF2J>?tTd`|WG$8+k=5vz{w{i_`I@9(WMbH&&4V09@cz9;{=Gl_mJ%ZDp2'
        '_!We}8>lIjqnn3t9JpVmg`7o#&zFt=qO4*3xzPJTk-7634mpg%ozL+Xeq*_A7e54Qm3_O29d`LY2B|NxOrZ?gmwk_YN7<6~+wwnj'
        '^-XPTexPntiVs4vVP$_*foAx0d4G6;u6_#>MKK;I5dZ)'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
