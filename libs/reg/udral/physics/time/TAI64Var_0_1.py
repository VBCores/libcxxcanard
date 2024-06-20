# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/time/TAI64Var.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.562151 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.time.TAI64Var
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class TAI64Var_0_1:
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
                 value:          None | reg.udral.physics.time.TAI64_0_1 = None,
                 error_variance: None | int | float | _np_.float32 = None) -> None:
        """
        reg.udral.physics.time.TAI64Var.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.time.TAI64.0.1 value
        :param error_variance: saturated float32 error_variance
        """
        self._value:          reg.udral.physics.time.TAI64_0_1
        self._error_variance: float

        if value is None:
            self.value = reg.udral.physics.time.TAI64_0_1()
        elif isinstance(value, reg.udral.physics.time.TAI64_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.time.TAI64_0_1 '
                             f'got {type(value).__name__}')

        self.error_variance = error_variance if error_variance is not None else 0.0  # type: ignore

    @property
    def value(self) -> reg.udral.physics.time.TAI64_0_1:
        """
        reg.udral.physics.time.TAI64.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.time.TAI64_0_1) -> None:
        if isinstance(x, reg.udral.physics.time.TAI64_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.time.TAI64_0_1 got {type(x).__name__}')

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

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
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
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.physics.time.TAI64Var.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> TAI64Var_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.time.TAI64_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "error_variance"
        _f1_ = _des_.fetch_aligned_f32()
        self = TAI64Var_0_1(
            value=_f0_,
            error_variance=_f1_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.physics.time.TAI64Var.0.1'
        assert isinstance(self, TAI64Var_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'error_variance=%s' % self.error_variance,
        ])
        return f'reg.udral.physics.time.TAI64Var.0.1({_o_0_})'

    _EXTENT_BYTES_ = 12

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{@*>ZEqAe5I$Z4$w6r&+J0z}aQlHKYO;BOCQaZ&0wQX3G^8Y=1sWFb?%dhxuD#gakgJ4LKD2^rr6S?>H}zl98Q)zl'
        'AyBD3-RZpcygZ(HW@djm`RBD}BYf(MWjC`~9>o@n<hlHrCpkoMs*6%v>A=_TZ8=k=t}?LQEy2I?lh6E9KT(gwiWhi((Lg7vGQ;zz'
        '6kRJ*8#!4(w7t5%aOEyHz8;Nt!C0x47mfP#-TwNOZ#7!Se)G?KeJ1A48JScLtlvS~??AOL<?E3(33)a|(~L9jc<czGINsY7BlU%U'
        '1LwtQF*X1p&hB{eL0|FwyAYH{7ShRGL@>T3I|{OO<)8!RaBR-RiF9!es^f%jtsuITTNf8PLv$DFk2eQqNG-a7XW!Bhh2&R%$JZam'
        ')^U|_lN~hlyh`v&ryQ3HSCp?$#+goiz4AbDr7fgdWjkzRe{C7$ytI%pD^&_?ZfS9LdUg)K+q1LF;d`H993o#Oygq**1#!~t<@Tu;'
        '6XFw#*U6wXka7o^e^H-{+j0-GxYWkQGV>etcx-iLQow^8;*ulS`ZWFJGV%4;CQ@l{lXhQWaE{F&cA<$o$4iNVh}IdMBT-<_fl(Zn'
        'pO#gU%QVLPRXO<`=GXfA1a2b-LSo5NFSTfvlI!bpA-&OTG#614y`z|(j|I1g&46;0)m@o_e<3D+`0GTYvDFVZ3z{2@?690Ckh2Nl'
        'TxpkQW>OP%%gE^&ycFhOCgdR!uE-}N_FbhNu(r_!a{^c|9LvonBa19#)3UZUY#WNwvQ?)G`M3f`^uZfDtO%Y@1>LkVgptXEN6Y}v'
        'rvt13H6k>ATS3o3NI8?1Wzd#LOU7+5mQ^NLV7kqg=9cCcF3&A4&ax6&tq~FKl9b_@?1`lso!b(PN!39IP6q*JxWaZo5(&5`0IIkB'
        'L^FXYG31lwunYOV&5qF(LPE3{nEqZ0R#pY$c>Aay8lGFtYze7sOR$V%43T=IV4w{ch!i5WRvA<`ER!~^tnJ??Xob)qL*%Y>T?&A%'
        'oRt|6c1lF5%f5RGj!vrrV;fOoR(r|rrx{PV3NgoO-oNB5Zf0!$A&Lb!2BShT;S7o7WQyE0gWw0q2q!cc*6$0<_7pK2I?#bW(*fFn'
        'yd}_)N|9~Y<EhKL<Z>S6EE^Pa0>~Z+ibH91No7r@ruw!SlNcGg&hQRc|9NGx-3)FskAC`FSD7~d0hdLgU|@iYw~?j)2Uf6h1li>w'
        'vZzTtF3GX3FAci!up43tyEmVGefGL^x5D!lKKA=@eInMSui3kd*lv+%Y&O^<zJ)?#uP374Mp`3L&9JMVic=wR=!o_D{Y{=xg&YwQ'
        '8+5u+<w%U~o2O`Dm**AuKm0^%<)uw<G?qO>zBO7Uc-=xO8W_0Xd$c%BLjzfc+O1JiYrM2LPGGO3g2XYpQ6)ABgJGm+TTIpsZ0W;U'
        'h6878E!W%~no;7j789R~OX7>?Xs_TMC0&Ixs2;-tOep{u_tCZf8r6OuZyfx*e*HR3&O1IhKZmuU4PFnYC6+9q`1?VRBM;|ynm6f`'
        '4Nj*p?*oe2#}&5ZY--RVLW={7f7myo=DNbx5-J-z5)B|~Yup_bMJ8f-DD7Am9OJuO=3!(vS8-EKhqoExSqReGtid6O#MDatr1TR-'
        '0}{lS6thQSTqu!LV)})MHpGmWpAeVD74el=5R2k#u_TtoRdKBzAH4h=o<U*-=Z)avy0{sVAifc;ecEj9uUZGF^wABi2&j51C+o2u'
        'C9zG?d(&I3-4gd&$1q3tTPxxL{(eNiF|tN%_b_}<tYSz;uq5;dg&qxs?h!AKY!l<6e*kq;Bwt4g000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)