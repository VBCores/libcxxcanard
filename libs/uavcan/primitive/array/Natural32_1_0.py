# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/primitive/array/Natural32.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.942852 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Natural32
# Version:       1.0
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
class Natural32_1_0:
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
                 value: None | _NDArray_[_np_.uint32] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Natural32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint32[<=64] value
        """
        self._value: _NDArray_[_np_.uint32]

        if value is None:
            self.value = _np_.array([], _np_.uint32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.uint32 and value.ndim == 1 and value.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint32  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _NDArray_[_np_.uint32]:
        """
        saturated uint32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.uint32] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.uint32 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint32  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated uint32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Natural32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Natural32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint32, _len0_)
        assert len(_f0_) <= 64, 'saturated uint32[<=64]'
        self = Natural32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Natural32.1.0'
        assert isinstance(self, Natural32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Natural32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{`t<NpIU$5EgeP&hG3hvn!jj?@6mRK;dFKiJP>!6*MKim_#W`ASuHx5WqRKZ~y{*fM4%E`e*p)b1!XgKKf^Lo+vM>'
        '<0MXO2W{<($eH=R`QE%oO5+*TfBXGtq5YQ~YmU^CT3B)u76)D!{Nz<aR&uM2db5!PDHGY&XKCE3rmdKLH_~KcT%3C)UW#I7xRF;U'
        'zti%Ds$NuT#z8$ugCSP(;@BH0J@yFWh1ai%%yx%ZoCJ+X_=U`R-nkwZpg`dl@k(Spu9v29P-&$s5kH9KRLuv8%=ju`VQoRpX1C_0'
        'o|{UE*`a0NQkTf~J@?2;mTy=znEGExYxmN&x-4XM7Ns4&W#r7SSY*B5M@cXkvD(*B$_827&DY~rg47M$=>#|=w(2FRTW{2u@DFBt'
        '`{#%xtn`R{C|y*b!q4KV$acF)>P0m#t}P}SYgMvM#MJbvK{_I!obBqk+!wMqxp@C@F2X+sw(s~SK#`RGX^Ga|N|=c3%-r%8$Z4hN'
        'Kkr4h<;x(=i}s9eJIl*7x6!0yupCJ;Qm-_^ph`tTR&P-8Qri6|O%{7;BVH(y=~n%Kw$#6#?RnIQs$R;XH-^eZ%gC5TbXJNKzx{D5'
        '483?{Nu=oxd0~r*UqumYo>cssonqV})V`-)G{~N^CQF0mB>m{ty<sXX0m^No|44E<#MQ1}J&0(N<OPLc!OkqXtF6$Jcu-_)frHxl'
        ')Y_kP>QxSU$7amiKm(nFncu7O+UoLw0VW5#gWI&k2NtanHqYb9LiasyjDt<EnZuUcXUkk$myLrS*ur637cW`Kw*9Rb*b3V??C9v-'
        '`Oa9_4m&vPT9Su6Wbb`1JnV#B9CqiiI{CLq?4I|=LNDy*u=kA`$V<L`E8>DZu$ROBxjK`U11rYEKG@IU;If)1g8YX*h!+mPK@Nwz'
        '>P24SJMzJNa0m`_IQmw-6h$$|J}L(sfukIp&iOk2(Ohtho@+Rf^Ehu)F7uvTm3(j<PH;Fimvhk$$oiaKwH$B~PH{N%&OIT7L(vp_'
        'c2#r3X*k27IJZuE666^>x9U0IEEGAMfA4h?g5oc%i4Hgi=Q&(l*xOUYSzNrom)0yVT!4!lN-L@Zp$Kz%O*O$KC~>%w=hz{ix2tQO'
        '4=%$M4%b#(3qlg^`nu?Yt8k6OjiqPhB5_}tJ1;laO$%Iy8ys$ZP|XNU*xT!>6>h>U4tEybFU5A<=pA!+-F3iixWnPz2iJ}m2!H>R'
        '=!Uy+kHdrI&*2TqaYvrTho4Lz+=mAoKKrQp5({yB{z=yW58*Qo<xZ`6i`qgq-1MS$bDUd8v7q3nf&~>vRV-*Ys$oILQ5^>ioH1~~'
        '#2FI@ED|w+j)D^kIx0@6=x8{hp`+u3js*&}aMZwpiK8YK=-PrZOkr8UDFw?aPN`Vda7x3nj#D~16l&vyfsTn2COQ^QSTF!HIH2H+'
        'f&(hfs5qeEjD`a`&gfV+aLT~4iBl$)Eu6A=tHP+;dO|H{Kianc?Z2iQvgPmKHSUJ&jc%y@3$U=!4XsHxWUq2J<h<)Wy9V8m)4c=#'
        '*>1?m|1a>r>W1W+PqlY<qZ^v*hHOF=H@cxE-B9;g+31E=+70FJmm>LgY;;2((GBI_M;qPHdUQinW8U(|=@N?;PLc?;6&zDw3~d$1'
        'RJ1i5)6mv&Ovh;*`wW~ma8|)S6MYq@O`KJ+&q80rX^Rw0Vo||K1&b<9s#w%;Qp2K-lREl3&g#$y)7YorG!YP*poG(~Pe+?rDV2e?'
        'iDM?(7LHjsOG${ETn74-%Ay7be3(U_G8i~%V9~@$lUg7-Bl3;R$Y)TQ?$#PrkrhO%;$^*yCZ29(B%h_e6#gIn&Lrz`YpfYFIRdMR'
        '*V#7rMKH{2ZnF`mZcr1Cvz>0zXvI}Vj*z)cFZD%c$&WCoh-_1TBMFB4rFC2sGvzYn_8W3mt2P4)tTv)FZiFJU*>K9@$P4Ajv{ea%'
        'svEPxRw(l>%u^GQnfZ*Ds29yVjm|uE*ZicnbhUJ)B&UEPm1E0Z*Y^@q7t2X%!s4Nz%EW8`Pya9fqJKFbr(NqB$!+iVYPBF5Tr!Fy'
        '@2$)xuC`l%-RkZx{qe_ny-R-sh_~w=-5vk{'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
